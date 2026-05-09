---
title: "Tier 1 Success Measurement Framework — Phase 1 Execution (25+ Organizations)"
project: cybersecurity-hardening
created: 2026-05-09
status: approved-baseline
item: 17 — Tier 1 Phase 1 Success Measurement Framework
depends-on: tier-1-success-metrics-framework.md, tier-1-measurement-dashboard-spec.md, TIER_2_PILOT_LAUNCH_READINESS.md
coordinates-with: TIER1_OUTREACH_EXECUTION_PLAN.md, TIER2_DISTRIBUTION_PREP.md
---

# Tier 1 Success Measurement Framework

**Purpose**: Establish measurement baselines BEFORE Phase 1 sends begin, so real data can be compared to defined thresholds as outreach happens. Every decision — on Tier 2 timing, escalation, and scope — should come from this framework, not from impression.

**Phase 1 scope**: 25 immigration legal aid organizations (core audience, Weeks 1–3 distribution)
**Tier 2 pilot window**: Weeks 4–11 post-Phase-1-send; decision gate Week 6
**Key documents**: `TIER_2_PILOT_LAUNCH_READINESS.md` (Tier 2 success metrics), `TIER1_OUTREACH_EXECUTION_PLAN.md` (execution cadence)

---

## 1. Key Success Metrics (KPIs)

All KPIs follow the format: **Metric Definition** → **Target** → **Data Source** → **Escalation if Below Target**

---

### 1A. Email Engagement

**Open / Click Proxy (Bitly click rate)**
- Definition: Percentage of sent emails where the recipient clicked the corpus Gist link (Bitly short URL)
- Target: ≥25% click rate by end of Week 2 (cumulative, all sends to date)
- Data source: Bitly free-tier dashboard (clicks / sends, updated daily)
- Escalation if below target: If click rate <15% at Day 10, subject line is failing — audit subject line variants and identify the underperforming version. Switch to the stronger variant immediately. If click rate <10% at Day 14, suspect deliverability issue (spam folder, blocked domain); run deliverability check at mail-tester.com and test an alternate sending address

**Reply rate (any reply)**
- Definition: Percentage of sends that received any reply within 14 days (excludes OOO auto-responses and bounces)
- Target: ≥25% overall reply rate by Day 21; immigration legal aid subsector target ≥30%
- Data source: Gmail tracking spreadsheet, `response_received` column
- Escalation if below target: If reply rate <15% at Day 14, audit contact quality (are you reaching named individuals or general inboxes?). If below 10% after both initial and follow-up waves, pivot to phone escalation for the 5 highest-priority named organizations

**Reply quality ratio (Stage 1+ within all replies)**
- Definition: Percentage of all replies that show evidence of reading beyond the subject line — asks a question, references a specific section, requests a meeting, or expresses forwarding intent. Generic "thank you, will file" responses are Stage 0
- Target: ≥50% of all replies are Stage 1+ by Day 21; ≥65% by Day 42
- Data source: Gmail tracking spreadsheet, `reply_type` column (Engagement / Acknowledgment / Routing / Declination / Conversion)
- Escalation if below target: If <30% of replies are Stage 1+ at Day 21, message is reaching the wrong contact function (communications generalist rather than legal or program staff). Rewrite personalization to emphasize client-facing utility and route to program directors, not communications teams

---

### 1B. Meeting Acceptance

**Meeting schedule rate**
- Definition: Number of organizations that scheduled a call, Zoom session, or in-person meeting as a percentage of all sends made
- Target: ≥20% of sends result in a scheduled meeting by Day 42 (end of Week 6)
- Data source: Calendar bookings + tracking spreadsheet `meeting_scheduled` column
- Escalation if below target: If <10% meeting rate by Day 28, the call-to-action in follow-up emails lacks specificity. Replace "happy to discuss" with a concrete offer: "I can do a 20-minute walkthrough of Part 0 and the threat model — here are two times this week if helpful." Specific offers convert at 2–3x the rate of open-ended offers

**Meeting completion rate**
- Definition: Percentage of scheduled meetings that were held (not cancelled or ghosted)
- Target: ≥75% of scheduled meetings complete
- Data source: Calendar records; tracking spreadsheet
- Escalation if below target: If >25% cancellation rate, organizations are scheduling without genuine interest — the initial engagement bar is too low. Qualify more before scheduling by asking for a brief written question or a sentence on their intended use before confirming time

---

### 1C. Training Adoption (Post-Meeting Engagement)

**Post-meeting engagement rate**
- Definition: Percentage of organizations that held a meeting and then took a concrete next step within 21 days: guide download confirmation, forwarding to a named colleague, requesting a follow-up session, or committing to include the corpus in a resource list
- Target: ≥60% of post-meeting organizations show engagement signal within 21 days of the meeting
- Data source: Follow-up emails; tracking spreadsheet `post_meeting_action` column
- Escalation if below target: If <40% post-meeting engagement at Day 60, the meeting did not produce a clear deliverable or ask. Send a one-question follow-up within 5 days of each meeting: "One thing that would make this most useful to your team — what would that be?"

**Guide download confirmation**
- Definition: Organization confirms Part 0 or the full guide was distributed to staff or clients (self-reported or evidenced by referral to the Gist link in their materials)
- Target: ≥5 organizations confirm guide distribution by Day 60
- Data source: Follow-up replies; Bitly click trajectory post-meeting (spike in clicks after a meeting date indicates internal forwarding)
- Escalation if below target: If <3 confirmations by Day 45, organizations reviewed the guide but did not share it. Identify whether the barrier is format (PDF more shareable than Gist URL) or content (too technical for client distribution). If format, produce the Part 0 one-pager before follow-up wave

**Follow-up question volume**
- Definition: Number of specific follow-up questions received about corpus content (not logistics questions) within the first 45 days
- Target: ≥10 substantive content questions across the 25 organizations
- Data source: Email threads; meeting notes
- Escalation if below target: If <5 follow-up questions by Day 30, the corpus is not prompting active engagement. This is a leading indicator of low adoption. Add a direct ask in the 30-day follow-up: "What's one thing in Part 0 that seems unclear or uncertain for your context?"

---

### 1D. Organizational Adoption Signals

**Leading indicators** (Days 14–45)

| Signal | Definition | Target |
|--------|-----------|--------|
| Internal forwarding | Organization forwards corpus to named colleague or team before formal adoption | 4+ organizations by Day 30 |
| Resource page reference | Corpus linked or referenced in org's internal resource list | 2+ by Day 45 |
| Staff briefing scheduled | Organization commits to briefing staff on corpus content | 2+ by Day 45 |
| Client distribution | Corpus or Part 0 distributed to clients or community members | 1+ by Day 45 |

**Lagging indicators** (Months 2–6)

| Signal | Definition | Target |
|--------|-----------|--------|
| Protocol change | Org modifies client intake, security onboarding, or communication protocol citing corpus | 1+ by Month 4 |
| Published resource | Corpus appears in org's published practitioner toolkit, newsletter, or website | 2+ by Month 6 |
| Staff training deployment | Org conducts internal training using corpus content | 1+ by Month 4 |
| Referral generation | Org provides warm introduction to another organization | 4+ new contacts by Day 90 |

**Timeline**: Leading indicators emerge Weeks 3–6. Lagging indicators emerge Months 2–6. Do not measure lagging indicators at the 30-day mark.

---

### 1E. Policy Uptake

**Downstream policy asks**
- Definition: Organization makes a specific ask of another institution, policymaker, or funder that references the corpus or the threat model — training deployment request, budget ask for security infrastructure, committee briefing referral, comment letter incorporating corpus content
- Target: 1+ documented policy ask by Month 3; 3+ by Month 6
- Data source: 90-day follow-up survey question 1; case study interviews
- Escalation if below target: If zero policy asks by Month 4, organizations are treating the corpus as an internal resource rather than an advocacy tool. Add a specific prompt in the 60-day follow-up: "Has anything in the threat model surfaced issues your organization is raising with funders, partners, or policymakers?"

**Institutional changes informed by guides**
- Definition: Observable institutional change that can be attributed to guide content with medium or high confidence (see attribution criteria in Section 6)
- Target: 2+ medium-confidence institutional changes by Month 6
- Data source: Self-reported connection (90-day survey); timing differentiation (change within 60 days of corpus receipt with no other major catalyst)
- Attribution confidence: High if unique content marker present (ELITE address confidence score, DROP platform path, verification checkpoint structure); Medium if timing-consistent but no unique marker; Low if general topic adoption from multiple possible sources

---

## 2. Weekly Cohort Tracking Dashboard

Phase 1 distributes across three waves. Cohort-level metrics track each wave separately to detect early performance divergence.

### Wave Structure

| Wave | Days | Target Organizations | Send Volume |
|------|------|---------------------|-------------|
| Wave 1 | Days 1–5 (Week 1) | Named national legal aid orgs + top 5 regional | 10 sends |
| Wave 2 | Days 8–12 (Week 2) | Community-based orgs + second-tier regional legal aid | 10 sends |
| Wave 3 | Days 15–19 (Week 3) | Mutual aid networks + catch-up sends | 5–8 sends |
| Follow-up | Weeks 4–5 | Non-responders from all waves | Variable |

### Cohort-Level Metrics Table

Complete every Friday. Data source: Gmail tracking spreadsheet.

```
PHASE 1 COHORT TRACKING — Week [N]

WAVE 1 (Days 1–5)
  Sends completed: [N] / 10
  Bitly clicks: [N]  (click rate: [N]%)
  Replies received: [N]  (reply rate: [N]%)
  Stage 1+ replies: [N]  ([N]% of replies)
  Meetings scheduled: [N]
  Status: [On track / Below threshold / Escalate]

WAVE 2 (Days 8–12)
  Sends completed: [N] / 10
  Bitly clicks: [N]  (click rate: [N]%)
  Replies received: [N]  (reply rate: [N]%)
  Stage 1+ replies: [N]  ([N]% of replies)
  Meetings scheduled: [N]
  Status: [On track / Below threshold / Escalate]

WAVE 3 (Days 15–19)
  Sends completed: [N] / 5–8
  Bitly clicks: [N]  (click rate: [N]%)
  Replies received: [N]  (reply rate: [N]%)
  Stage 1+ replies: [N]  ([N]% of replies)
  Status: [On track / Below threshold / Escalate]

CUMULATIVE
  Total sends: [N] / 25
  Overall click rate: [N]%  (target: ≥25%)
  Overall reply rate: [N]%  (target: ≥25%)
  Stage 1+ rate within replies: [N]%  (target: ≥50%)
  Meetings scheduled: [N]  ([N]% of sends, target: ≥20%)
  Adoption signals logged: [N]
```

### Email-to-Adoption Funnel

The campaign has four conversion stages. Track organizations at each stage cumulatively.

```
SENDS (25)
  ↓ [click-through: target ≥25%]
ENGAGED READERS (≥6 organizations)
  ↓ [Stage 1+ reply: target ≥50% of replies]
QUALITY CONVERSATIONS (≥4 organizations)
  ↓ [meeting or explicit adoption signal: target ≥20% of sends]
ADOPTION PIPELINE (≥5 organizations)
  ↓ [confirmed distribution or protocol change: target ≥3 by Day 90]
DOCUMENTED ADOPTIONS (≥3 by Day 90)
```

### Success Thresholds Per Wave

**Wave 1 (Days 1–5) — Named National Organizations**
- Minimum viable: 1 reply within 7 days
- On track: 3+ replies with 1 Stage 1+ by Day 10
- Below threshold: 0 replies and 0 Bitly clicks at Day 7
- Pivot trigger: Email open rate proxy (Bitly clicks) <10% at Day 7 → switch to phone outreach for NILC, CLINIC, RAICES immediately. Do not wait until Week 2 to escalate for named national organizations

**Wave 2 (Days 8–12) — Community Organizations**
- Minimum viable: 2 replies within Day 14
- On track: 4+ replies with 2+ Stage 1+ by Day 14
- Below threshold: <2 replies at Day 14
- Pivot trigger: If Wave 2 underperforms Wave 1 by more than 10 percentage points on reply rate, the community organization framing differs from legal aid framing sufficiently to require a subject line adjustment before remaining sends

**Wave 3 (Days 15–19) — Mutual Aid Networks**
- Minimum viable: 1 reply within Day 21
- On track: 2+ replies with Signal-format engagement
- Below threshold: 0 replies at Day 21
- Pivot trigger: Mutual aid networks that are not responding to email are more likely to respond to Signal outreach. If 0 replies from Wave 3 email at Day 21, switch to direct Signal message to known mutual aid Signal group administrators (do not mass-post in public groups)

---

## 3. Early Warning System

### Failure Scenarios and Detection Triggers

**Scenario A: Low Engagement (Email Channel Failure)**
- Detection trigger: Total Bitly clicks <5 across all sends by Day 7 (indicating emails are not being opened, or the link is not compelling)
- Early warning signal: Bitly click rate <10% on any single wave after 3+ business days
- Response timeline: Identify within 24 hours of trigger; pivot decision within 48 hours

**Scenario B: Security Incident at a Tier 1 Organization**
- Detection trigger: A Tier 1 organization reports a security incident, enforcement raid, or data breach during the active outreach period; or public reporting surfaces a security incident at a targeted organization
- Early warning signal: Google Alert on organization name + "raid" / "ICE" / "breach" / "arrest"; local immigration enforcement news monitoring
- Response timeline: If incident detected, pause outreach to that organization immediately. Do not send scheduled follow-ups. Shift to checking in as a supportive contact rather than a resource distributor

**Scenario C: Contact Turnover**
- Detection trigger: Email bounce (permanent delivery failure), out-of-office indicating the contact is no longer at the organization, or follow-up reply from a different person indicating the original contact left
- Early warning signal: Any permanent bounce at any named contact; OOO messages indicating departure rather than vacation
- Response timeline: Research alternate contact within 24 hours of detection. Pre-identified fallbacks for the five named national organizations should be ready before Day 1 (see Section 4)

**Scenario D: Hostile Reception**
- Detection trigger: A recipient replies requesting removal from all contact, expresses concern about the corpus's safety implications for their clients, or identifies a substantive error in the guidance that could increase client risk
- Early warning signal: Explicit refusal; any reply mentioning client safety risk or requesting that distribution stop
- Response timeline: Respond within 24 hours. Do not dismiss any safety concern. Full protocol in Section 4D

**Scenario E: Low Reply Quality (Pattern of Stage 0 Routing)**
- Detection trigger: >60% of all replies are generic acknowledgments with no routing information by Day 21
- Early warning signal: First 5 replies are all "thank you, will file" with no specific engagement
- Response timeline: Assess at Day 14. If pattern holds, add a routing question to the follow-up: "Is there someone at your organization who handles practitioner security resources? I want to make sure this reaches the right person."

---

### Escalation Decision Tree

```
[ANY REPLY RECEIVED]
  ↓
  Is it Stage 1+ (question, meeting request, forwarding intent)?
    YES → Reply within 24h using R1-Engagement template → Track in spreadsheet → Schedule follow-up
    NO  → Reply with R2-Acknowledgment → Set 10-day follow-up reminder

[NO REPLY AT DAY 7 — named national org]
  ↓
  Did Bitly show any clicks?
    YES → Email delivered, not compelling → Revise subject line, resend once with alternate variant
    NO  → Possible deliverability failure → Test alternate channel (web form or phone) within 48h

[NO REPLY AT DAY 14 — any organization]
  ↓
  Is this a named national priority org (NILC, CLINIC, RAICES, ILRC, NLG)?
    YES → Escalate to phone call to communications office
    NO  → Send R2-Acknowledgment follow-up with specific question; close at Day 21 if still no reply

[BOUNCE DETECTED]
  ↓
  Research alternate contact immediately (≤24h)
    Named org → Check org website for current staff; use fallback contact from pre-identified list
    Regional org → Check org website; fall back to web form if no direct email found
    No alternate found → Mark "Unreachable — closed"; do not send again

[SECURITY INCIDENT AT ORG DETECTED]
  ↓
  Pause all outreach to that organization
  ↓
  Is the corpus part of the incident (e.g., org received corpus and was raided)?
    YES → Escalate to user immediately; do not send further until user assessment
    NO  → Hold for 14 days minimum; send brief check-in (not resource distribution) after 14 days

[HOSTILE RECEPTION — safety concern about corpus]
  ↓
  Acknowledge receipt of concern within 24h
  ↓
  Is the concern about client safety risk?
    YES → Pause distribution of affected section immediately; escalate to user; assess within 5 business days
    NO (scope mismatch, "not for us") → Accept gracefully; close loop; log as Declined

[PATTERN OF 2+ SAME CONCERN]
  ↓
  This is not a one-off — diagnose the concern type
    Technical error → Verify against primary sources; update Gist if confirmed; re-send corrected version
    Scope mismatch → Adjust framing for remaining sends; do not revise corpus
    Legal concern → Pause until legal review; escalate to user
```

---

## 4. Contingency Response Protocols

### 4A. Low Engagement — Pivot Strategy

**Threshold**: <10% overall Bitly click rate after Wave 1 (Day 7) OR <10% reply rate after both Wave 1 and Wave 2 (Day 14)

**Time limit**: All pivot decisions must be made by Day 10 for Wave 1 underperformance, Day 17 for Wave 2 underperformance. Do not wait longer — each day of delay costs follow-up window time.

**Diagnostic sequence (complete before pivoting)**:
1. Bitly check: Are clicks near zero, or clicks present but no replies? Zero clicks = email not opened. Clicks without replies = email opened but insufficient compelling pull.
2. Subject line audit: Compare click rates across the A/B/C subject line variants. If one variant has >2x the click rate of others, drop the underperformers immediately.
3. Contact quality check: Were Wave 1 sends to named individuals or general inboxes? General inboxes for immigration legal aid organizations typically route through a communications team that is not the right function for this resource.

**Pivot actions**:
- Subject line failure → Test two new subject lines immediately on next 5 sends before continuing
- Contact function failure → Research program directors and legal staff by name; re-route to named individuals
- Email channel failure entirely (clicks near zero across all variants) → Escalate top 5 priority orgs to phone within 48 hours; test LinkedIn message for 3–5 secondary orgs
- General engagement failure after all adjustments → Shift remaining budget to Tier 1C mutual aid network Signal outreach, which has lower friction for communities with existing security culture

**Alternative contact channels** (in priority order):
1. Phone call to communications office (named national orgs only)
2. LinkedIn connection request + note (for identifiable named contacts)
3. Web contact form (when email bounces or goes unanswered)
4. Signal direct message (mutual aid networks and security-culture orgs)
5. Warm introduction from a known mutual contact (if available)

---

### 4B. Organizational Incident During Tier 1

**Scenario**: An organization targeted in Phase 1 experiences an ICE enforcement action, security breach, staff arrest, or organizational crisis during the 3-week outreach window.

**Immediate response (within 24 hours of incident detection)**:
1. Pause all scheduled outreach to that organization — do not send follow-ups or second waves
2. Remove the organization from the active send queue in the tracking spreadsheet; mark "Incident hold — [date]"
3. Do not send the corpus as outreach during or immediately after an active incident — this is the wrong timing and potentially the wrong framing

**Assessment (Days 3–14 post-incident)**:
- Is the incident ongoing (continued enforcement activity) or contained (single event)?
- Has the organization's contact information changed (staff arrested, office temporarily closed)?
- Is there a public statement from the organization that indicates capacity to engage?

**Re-engagement timing**:
- Ongoing incident: Hold until active enforcement subsides; re-evaluate after 30 days
- Contained incident: Check in as supportive contact (not resource distribution) after 14 days; offer the corpus as a resource only if they express interest

**Media coordination**: If the incident generates press coverage relevant to the ELITE threat model, assess whether the corpus should be shared with journalists covering the story — but only after confirming the organization has no objection to being referenced.

---

### 4C. Contact Turnover

**Pre-identified fallback contacts for named national organizations** (verify current at time of send):

| Organization | Primary Contact | Fallback |
|-------------|----------------|----------|
| NILC | nilc.org contact form (tech/security) | info@nilc.org; general contact escalates |
| CLINIC | national@cliniclegal.org | CLINIC website staff directory; communications team |
| RAICES | communications@raicestexas.org | Executive team via website; state office contacts |
| ILRC | kbello@ilrc.org (Kemi Bello) | publications@ilrc.org; general org contact |
| NLG Mass Defense | massdef@nlg.org | NLG national office main line; chapter coordinators |

**Turnover response protocol**:
1. When a bounce or OOO departure signal is detected, research the new contact within 24 hours
2. Do not resend to the old contact email — verify the new contact before resending
3. When contacting the new contact, do not assume familiarity: treat as a cold contact even if the previous contact acknowledged receipt
4. If no new contact can be identified within 7 days, use the web contact form as a neutral channel and note in the body that you are attempting to reach whoever handles digital security or legal technology resources

**Institutional vs. individual relationships**: Track which organizations have built a relationship with the corpus itself (forwarded it, referenced it, acknowledged its value) vs. organizations where the relationship was with a specific contact who left. For institutional relationships, re-contact can reference the prior engagement; for individual relationships, re-contact is a cold start.

---

### 4D. Hostile Reception

**Definition**: Any reply that (a) explicitly requests no further contact, (b) expresses that the corpus content could put clients at risk, (c) accuses the corpus of containing dangerous advice, or (d) reports the sender as spam.

**Immediate response protocol**:
1. Reply within 24 hours. Acknowledge the concern directly without dismissing it.
2. Do not resend to this organization under any circumstances.
3. Log as "Declined — safety concern raised" in the tracking spreadsheet. Note the specific concern described.

**Security implication assessment** (for safety concerns, not general "not for us" responses):
- Does the concern identify a specific section that could increase client risk?
  - If YES: Pause distribution of that section to ALL remaining targets until assessed. Escalate to user within 48 hours.
  - If NO (general concern, tone mismatch, "clients aren't ready for this"): Accept the feedback as a scope signal. No pause required. Adjust framing for remaining sends if the concern reflects a pattern.

**Documentation**: All hostile receptions with substantive safety concerns are logged permanently in the tracking spreadsheet regardless of outcome. Do not delete or archive these entries. They are the most important feedback in the corpus's early distribution history.

**Withdrawal protocol**: If distributing to an organization appears to have created risk for that organization or its clients (e.g., a recipient reports that receiving the corpus triggered adverse attention), stop all outreach immediately, escalate to user, and do not resume until user assessment is complete.

---

## 5. Tier 1 to Tier 2 Transition Criteria

### Success Benchmarks Required to Trigger Tier 2 Pilot

Per `TIER_2_PILOT_LAUNCH_READINESS.md`, the Phase 1 gate criteria must be met before any pilot contact goes out:

| Criterion | Minimum Required | Strong Signal |
|-----------|-----------------|---------------|
| Organizations contacted | ≥25 | ≥25 (full scope) |
| Response rate (any reply) | ≥5% (≥2 of 25) | ≥25% (≥6 of 25) |
| Stage 1+ quality engagement | ≥1 verified Stage 1+ reply | ≥3 Stage 1+ |
| Corpus accessible | Gist publicly accessible, no login wall | — |
| No active safety concerns | Zero unresolved client safety concerns | — |

**Gate assessment date**: End of Week 3 (Day 21). If gate is met, pilot invitations to FPF, NLG Mass Defense, and CLS Philadelphia go out Monday–Wednesday of Week 4.

**If gate is not met at Day 21**: Delay pilot launch by 1 week. Diagnose whether the shortfall is a numbers problem (not enough sends completed) or an engagement problem (sends completed but not converting). A numbers problem is recoverable; an engagement problem requires messaging adjustment before the pilot launch.

### Timeline Assumptions

| Phase | Timing | Gate |
|-------|--------|------|
| Wave 1 sends | Days 1–5 (Week 1) | Bitly click check Day 7 |
| Wave 2 sends | Days 8–12 (Week 2) | Reply rate check Day 14 |
| Wave 3 sends + follow-ups | Days 15–21 (Week 3) | Phase 1 gate assessment Day 21 |
| Decision gate — Tier 2 launch | Day 21 (end of Week 3) | Must meet minimum criteria |
| Tier 2 pilot invitations sent | Days 22–24 (Week 4 Mon–Wed) | Contingent on Day 21 gate |
| Tier 2 pilot adoption assessment | Day 36 (Week 6 end) | 60%+ adoption → proceed full wave |
| Full Tier 2 wave authorization | Week 10 (pilot debrief) | 2+ messaging refinements, 1+ policy ask |
| Full Tier 2 wave launch | Week 11 | 33-organization wave |

**Maximum Phase 1 active window**: 21 days (3 weeks) for sends. Follow-up loop runs through Week 5. Long-tail follow-up (90-day survey) runs through Day 90.

### Data Review Cadence

- **Weekly during Phase 1 (Weeks 1–5)**: Complete the cohort tracking dashboard every Friday (15–20 minutes from tracking spreadsheet). Compare to thresholds in Section 2.
- **Day 21 review**: Formal gate assessment. Check all five Tier 2 pilot launch criteria. Decision: launch, delay, or escalate.
- **Day 42 review** (6-week): Adoption signal emergence check. How many organizations are at Stage 2+? Is the corpus in active circulation at any organization?
- **Day 90 review**: Primary Tier 2 go/no-go decision for full 33-organization wave. Compile 30-day follow-up results, count Stage 3+ organizations, assess referral factor.
- **Monthly post-Phase-1 (Months 4–6)**: Lagging indicator monitoring. Protocol changes, published citations, policy asks. These require passive monitoring (Google Alerts, Overton search, direct check-in) not active outreach.

---

## 6. Attribution and Downstream Tracking

### Connecting Guide Usage to Policy Asks

**Survey-based attribution (90-day follow-up)**:
Send a 3-question follow-up email at Day 90 to all organizations that showed Stage 1+ engagement:

1. "Has your organization distributed or referenced this guide since we last spoke? If so, in what format — staff briefing, client distribution, resource list, other?"
2. "Has anything in the threat model shaped discussions about security tools, client intake protocols, or data practices at your organization?"
3. "Is there someone else in your network — another organization or individual — who should have this guide?"

Question 1 captures adoption evidence. Question 2 surfaces policy asks or institutional changes. Question 3 activates the referral pipeline.

**Commitment tracking**: For organizations that indicate in a meeting or follow-up that they intend to take a specific action (share with their board, include in next training, post to their resource page), log the commitment and the date. Follow up at the date specified if no evidence of completion. Do not chase the commitment more than once.

**Attribution confidence tiers**:
- High confidence: Organization references a unique corpus content marker in their output (California DELETE Act DROP platform path; Palantir ELITE address confidence score documentation; the verification checkpoint structure; the Tier 1/2/3 threat level framework) — these terms do not appear in any other guide
- Medium confidence: Adoption is timing-consistent (change occurs within 60 days of corpus receipt) and no other major catalyst (enforcement raid, press story, internal incident) is documented in the same window
- Low confidence: Organization adopts broadly consistent practices but uses no unique markers and no specific timing correlation can be established

**Only High confidence attributions should be cited externally** (in any Phase 2 proposal, public report, or social proof messaging to Tier 2 contacts). Medium confidence attributions inform internal iteration.

### Long-Term Monitoring Framework

**6-month follow-up (Day 180)**:
- Send a brief check-in to all Stage 2+ organizations (those that showed internal circulation or adoption signal)
- Ask: "We're updating the corpus for the July 2026 quarterly review. Has anything in your practice or your clients' context changed that should inform the next version?"
- Check Gist view count trajectory — sustained view growth at Month 6 indicates organic secondary distribution is ongoing
- Run Overton.io search for "ELITE Palantir" and "immigration surveillance countermeasures" to detect policy citation

**12-month follow-up (Day 365)**:
- Google Scholar search for unique corpus markers (ELITE address confidence score, DROP platform immigration)
- CourtListener search for corpus content cited in court filings, regulatory comments, or amicus briefs
- Organization website searches for named Tier 1 orgs: has any org published resources that reference corpus content?
- Run a lightweight survey of the 5 highest-engagement organizations: "What changes, if any, did this guide contribute to over the past year?"

**Monitoring infrastructure**:
- Google Alerts: Set up alerts for "Palantir ELITE immigration," "DROP platform California immigration," and any named Tier 1 organization + "digital security" before Day 1 sends
- Gist view log: Record total views monthly starting Day 1; log any spikes and correlate with outreach waves
- Bitly referrer data: Check monthly for referrer sources not in your direct sends (indicates organic sharing outside the direct recipient list)

---

## Summary: Minimum Viable Success Thresholds

| Phase | Metric | Minimum Required | Strong Signal | Failure Threshold |
|-------|--------|-----------------|---------------|-------------------|
| Week 1 | Any Bitly click | 1 click within Day 7 | 8+ clicks by Day 7 | Zero clicks Day 7 |
| Week 1 | Any reply | 1 reply within Day 10 | 3+ replies by Day 10 | Zero replies Day 10 |
| Week 2 | Reply rate | 10% of 20 sends | 25%+ | <5% |
| Day 21 | Phase 1 gate | 2 replies + Gist accessible | 6+ Stage 1+ replies | Gate fails |
| Day 42 | Meeting rate | 5 meetings of 25 sends (20%) | 8+ meetings | <3 meetings |
| Day 60 | Adoption signals | 3 leading indicators | 6+ leading indicators | Zero signals |
| Day 90 | Referral generation | 3+ warm new contacts | 8+ | Zero referrals |
| Week 6 | Tier 2 pilot adoption | 40% of 3 pilot orgs (2 of 3) | 80%+ | <40% |
| Week 10 | Pilot debrief | 60% adoption, 2 refinements, 1 policy ask | 100% adoption | <40% adoption |

---

*Framework baseline established: 2026-05-09. All thresholds active from Phase 1 Day 1. Weekly review cadence mandatory during Weeks 1–5. Day 21 gate is a hard decision point for Tier 2 pilot timing — do not skip it. Coordinates with: `TIER_2_PILOT_LAUNCH_READINESS.md` (pilot gate criteria), `tier-1-success-metrics-framework.md` (extended metric hierarchy), `tier-1-measurement-dashboard-spec.md` (weekly dashboard templates), `TIER1_OUTREACH_EXECUTION_PLAN.md` (execution cadence).*
