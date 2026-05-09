---
title: "Tier 1 Success Measurement Framework — Policy-Contact Cohort (Senators, Think Tanks, Law Schools)"
project: cybersecurity-hardening
created: 2026-05-09
revised: 2026-05-09
version: 2.0
status: production-ready
item: 17 — Cybersecurity-Hardening Tier 1 Success Measurement Framework
cohort: "25 high-leverage policy contacts (senators/senate staff, think tanks, law schools)"
depends-on:
  - tier-1-success-metrics-framework.md
  - tier-1-measurement-dashboard-spec.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER_2_PILOT_LAUNCH_READINESS.md
supersedes: v1.0 (immigration legal aid cohort — see tier-1-success-metrics-framework.md for that cohort)
---

# Tier 1 Success Measurement Framework
## Policy-Contact Cohort: Senators, Think Tanks, and Law Schools

**Lead finding**: Policy-contact outreach lives or dies on the Day 14 meeting acceptance number. For this cohort — legislative staff, think tank fellows, and law school clinics — an email that generates a meeting is worth ten emails that generate replies. The primary conversion event is not a click or a response; it is a scheduled 30-minute call. Design every metric, every follow-up, and every escalation around that conversion.

**Why this document exists**: Every measurement framework is only useful if it is written down *before* the campaign starts. Post-hoc metrics confirm what already happened. Pre-defined thresholds enable fast correction. Print this document before sending Wave 1. Refer to it every Friday during Weeks 1–6. Do not improvise thresholds under pressure.

**Cohort scope**: 25 contacts across three sectors — senate offices / senate staff (estimated 8–10), think tanks and policy organizations (estimated 8–10), and law schools with civil liberties or surveillance law clinics (estimated 5–7).

**Note on parallel cohort**: The immigration legal aid cohort (12–45 direct-service organizations) is tracked separately in `tier-1-success-metrics-framework.md` and `tier-1-measurement-dashboard-spec.md`. This document covers the policy-facing cohort only. KPI targets differ substantially between the two cohorts because the conversion event, institutional rhythm, and adoption signal are different.

---

## 1. KPI Definitions and Targets

All KPIs use the format: **Metric** | **Target** | **Data Source** | **Escalation Threshold**

Benchmark context: Government and policy email outreach consistently outperforms general commercial email. Government-sector emails average 30.5% open rates (HubSpot, 2024); nonprofit advocacy emails average 28–40% (M+R Benchmarks 2025). For a curated 25-contact list with personalized subject lines and a named contact at each organization, targets above these averages are realistic. Personalized subject lines increase open rates by 26–30% over generic templates (Campaign Monitor, 2025).

---

### 1A. Primary KPIs — Email Engagement

**Email open rate (proxy: Bitly click rate)**
- Definition: Percentage of sent emails where the recipient clicked the corpus link (tracked via Bitly short URL). Because Apple Mail Privacy Protection and Gmail proxy loading inflate raw open tracking, use Bitly clicks as the more reliable engagement signal.
- Target: 45% click rate across all 25 sends by end of Week 2 (Day 14). This represents approximately 11–12 organizations clicking the link.
- Data source: Bitly free-tier dashboard. Check daily during Week 1, every other day during Weeks 2–3.
- Escalation: If click rate falls below 30% by Day 10 (fewer than 7–8 clicks), the subject line is failing or the emails are landing in spam. Trigger the subject line audit protocol in Section 3.

**Email reply rate**
- Definition: Percentage of sends that received any substantive reply within 14 days (excludes auto-responders and out-of-office messages that do not contain forwarding information).
- Target: 20% overall reply rate by Day 21. For the policy cohort, 20% is the minimum viable signal — this means 5 of 25 contacts replied with anything beyond an automated response. Strong signal is 30%+ (7–8 replies).
- Data source: Gmail tracking spreadsheet, `reply_received` column.
- Escalation: If reply rate is below 10% (fewer than 2–3 replies) at Day 14, contact function routing is the likely problem. Legislative staff and think tank fellows rarely check general inboxes. Verify that sends went to named individuals, not press@, info@, or contact@ addresses.

**Reply quality ratio (Stage 1+ within all replies)**
- Definition: Percentage of replies that demonstrate reading beyond the subject line — references a specific section, asks a substantive question, requests a meeting, or identifies a colleague to loop in. Generic "thank you, received" replies are Stage 0 and do not count toward this metric.
- Target: 60% of all replies are Stage 1+ by Day 21. If 5 contacts replied, at least 3 of those replies should be substantive.
- Data source: Gmail tracking spreadsheet, `reply_type` column (Stage0-Acknowledgment / Stage1-Question / Stage1-MeetingRequest / Stage1-Routing / Stage1-Declination).
- Escalation: If fewer than 40% of replies are Stage 1+, the message is reaching the wrong function — communications directors rather than legislative assistants, or law school administrators rather than clinic directors. Rewrite the opening line to name the specific function you intend to reach ("I'm writing to the staff handling digital surveillance policy" rather than "I'm writing to Senator X's office").

---

### 1B. Primary KPIs — Meeting Acceptance

**Meeting acceptance rate**
- Definition: Number of organizations that confirmed a 30-minute briefing call as a percentage of all sends made.
- Target: 60% of contacted organizations accept a briefing call by Day 42 (end of Week 6). This means 15 of 25 organizations schedule a call. This target is ambitious by cold-outreach standards but realistic for a highly targeted cohort where the briefing addresses material relevant to the contact's active professional concerns (surveillance law, civil liberties, legislative oversight).
- Data source: Calendar bookings (Google Calendar). One row per confirmed call in the meeting tracker.
- Note on realistic range: Congressional Management Foundation research shows that policy briefings organized with 4–6 weeks of lead time and a specific, expert-led offer achieve high meeting rates with legislative staff. The 60% target assumes all sends are well-personalized and the offer is concrete ("20-minute briefing on Palantir's ELITE targeting system with primary-source documentation").
- Escalation: If meeting acceptance falls below 30% (fewer than 7–8 confirmed calls) by Day 28, the call-to-action in the initial and follow-up emails is too vague. Replace "happy to discuss" with a specific offer containing a time, a duration, and a deliverable.

**Meeting completion rate**
- Definition: Percentage of scheduled calls that are actually held (not cancelled, rescheduled, or ghosted).
- Target: 75% of scheduled calls complete within 7 days of the agreed date.
- Data source: Calendar records. Mark each call as Completed, Rescheduled, or Cancelled.
- Escalation: If more than 30% of scheduled calls are cancelled or no-showed, the scheduling process is not qualifying intent. Add a brief written question before confirming a time slot: "To make the call most useful — are you focused primarily on legislative oversight implications, civil liberties litigation angles, or operational security for your team's communications?" A contact who answers this question has demonstrated substantive interest.

---

### 1C. Primary KPIs — Security Adoption Signals

**Security adoption response rate (Week 4–6 follow-up)**
- Definition: At Week 4–6, a short follow-up email goes to all contacts who attended a briefing call. The email asks three questions: (1) Have you been able to implement any of the OpSec practices from the briefing? (2) Has the threat model informed any policy discussions or legislative priorities in your office/organization? (3) Is there another contact in your network who should receive this briefing?
- Target: 10%+ of contacted organizations report a positive adoption signal by Week 6. For 25 contacts, that means 2–3 organizations report implementing a practice, updating a policy position, or identifying a referral. This target is conservative — adoption signals in policy contexts are slow-developing.
- Data source: Email follow-up replies. Tracking spreadsheet `adoption_signal` column (Yes/No/Partial).
- Escalation: If zero adoption signals at Week 6, the briefing calls were informational but did not produce actionable outcomes. The Week 6 escalation protocol (see Section 4, Scenario 4) applies.

---

### 1D. Secondary KPIs — Distribution Quality

**Bounce rate**
- Definition: Percentage of sends that resulted in a permanent delivery failure (hard bounce — email address does not exist, domain does not accept mail, or inbox is full).
- Target: Below 5% (fewer than 1–2 bounces in a 25-contact send). A bounce rate above 5% indicates the contact list was assembled from stale sources.
- Data source: Gmail bounce notifications. Log each bounce in the tracking spreadsheet immediately.
- Escalation: If bounce rate exceeds 8% (2+ bounces), stop the remaining wave sends. Validate all remaining contact emails against the organization's current website staff directory and LinkedIn before proceeding. A 10%+ bounce rate requires a full list re-validation before any further sends.

**Unsubscribe / cease-contact rate**
- Definition: Percentage of contacts who explicitly request no further contact. (Policy contacts are less likely to use a formal unsubscribe; track explicit "please remove me" replies as unsubscribes.)
- Target: Below 2% (fewer than 1 explicit cease-contact request per 25 sends). If a contact asks to be removed, remove immediately and do not follow up.
- Diagnostic: If the unsubscribe rate exceeds 2%, the message is being perceived as mass email rather than targeted expert outreach. Review the personalization quality of the remaining unsent drafts before proceeding.

**Reply-to-meeting conversion rate**
- Definition: Of all contacts who replied with a Stage 1+ response, what percentage agreed to a briefing call?
- Target: 70% of Stage 1+ replies convert to a scheduled call. If 7 contacts sent Stage 1+ replies, at least 5 should be on the call calendar.
- Data source: Tracking spreadsheet. Cross-reference `reply_type` = Stage1+ with `meeting_scheduled` = Yes.
- Diagnostic: If conversion is below 50%, the follow-up email asking for a call is not closing the loop effectively. The follow-up should be sent within 24 hours of a Stage 1+ reply and should contain a specific proposed time and a one-sentence description of what the call will cover.

---

### 1E. Secondary KPIs — Framework Adoption Signals

Track these signals as they appear; they are not measurable on a weekly basis.

| Signal | Definition | Target Timeline | Data Source |
|--------|-----------|----------------|-------------|
| Tier 2 playbook request | Contact asks for sector-specific variant or additional materials | Weeks 3–8 | Email threads |
| Internal sharing signal | Contact mentions sharing briefing with a colleague, committee, or team | Weeks 2–6 | Meeting notes or email |
| Legislative reference | Contact mentions using threat model in committee prep or constituent briefing | Months 2–4 | Follow-up calls or email |
| Sector-specific adaptation request | Contact asks whether the guide can be adapted for their state/committee/clinic | Weeks 4–8 | Email threads |
| Referral generated | Contact provides a warm introduction to another policy contact | Weeks 3–12 | Direct referral reply |

A contact showing two or more of these signals within 8 weeks is a strong candidate for inclusion in the Tier 2 pilot cohort.

---

### 1F. Lagging Indicators — Months 2–3

These metrics are not measurable during the active distribution period. Schedule a dedicated review at Day 90.

**Policy uptake**
- Definition: Any Tier 1 organization (senate office, think tank, law school clinic) cites the framework in a published document — committee briefing, amicus brief, policy report, law review article, legislative proposal, or regulatory comment.
- Target: 1+ documented policy citation by Month 3; 3+ by Month 6.
- Monitoring: Set Google Alerts for unique corpus terms ("ELITE address confidence score," "Palantir ICE ELITE," "DROP platform immigration") before Day 1 sends. Check Overton.io quarterly for policy document citations. Check CourtListener for amicus brief citations.

**Media amplification**
- Definition: A contacted organization (or a person they referred the briefing to) amplifies the threat model to press or academic networks — op-ed citing the framework, press interview referencing the corpus, academic conference presentation.
- Target: 1+ media or academic amplification by Month 3.
- Monitoring: Google Alerts for named Tier 1 organizations + "surveillance" or "ICE" or "Palantir."

**Tier 2 pipeline**
- Definition: Number of Tier 1 contacts who request participation in the Tier 2 pilot program — asking to receive sector-specific playbooks, requesting a second call for a larger audience, or introducing the corpus to their professional network for distribution.
- Target: 2–3 of 25 contacts request Tier 2 pilot participation by Day 60.
- Data source: Email threads; meeting notes from briefing calls.

---

## 2. Tracking Infrastructure and Data Collection

### 2A. Email Tracking Setup

**Bitly URL tracking (required)**
- Create a free Bitly account with a non-primary email address before Wave 1.
- Create a single short URL for the corpus Gist link (e.g., `bit.ly/palantir-briefing`).
- Use this short URL in all 25 emails — do not use different URLs for different contacts, as this fragments your click analytics.
- Check Bitly dashboard daily during Weeks 1–2. Record cumulative click count in the tracking spreadsheet each Friday.
- Bitly provides: total clicks, unique clicks, referrer source, and geographic location. Referrer source is the most useful for detecting internal forwarding (if you see clicks from an IP block associated with a Senate office or university, that is a positive internal distribution signal).

**Gmail label structure**
Create these nested labels before sending Wave 1. Apply labels immediately upon sending each email.

```
Tier1-Policy/
  Sent
  Reply-Stage0-Acknowledgment
  Reply-Stage1-Question
  Reply-Stage1-MeetingRequest
  Reply-Stage1-Routing
  Reply-Declined
  OOO-Active
  Bounce-Unresolved
  Follow-Up-Pending
  Meeting-Scheduled
  Meeting-Completed
```

**Manual tracking spreadsheet (Google Sheets)**

The tracking spreadsheet is the authoritative record for all campaign data. Create it before Wave 1. Structure:

**Tab 1: Master Contact List**
Columns: Organization | Contact Name | Role | Email | Sector (Senate / Think-Tank / Law-School) | Send Date | Email Status (Sent / Bounced / OOO) | Notes

**Tab 2: Email Engagement**
Columns: Organization | Send Date | Bitly Click (Y/N) | Click Date | Reply Received (Y/N) | Reply Date | Reply Type (Stage0 / Stage1-Question / Stage1-Meeting / Stage1-Routing / Declined) | Follow-Up Sent (Y/N) | Follow-Up Date

**Tab 3: Meeting Schedule**
Columns: Organization | Contact Name | Meeting Date | Meeting Format (Zoom / Phone / In-Person) | Duration (Actual) | Attendees | Key Issues Discussed | Follow-Up Requested (Y/N) | Follow-Up Item

**Tab 4: Adoption Signals**
Columns: Organization | Week-4-Follow-Up Sent (Y/N) | Response Received (Y/N) | Response Date | Practice Implemented | Policy Action Referenced | Tier-2-Interest (Y/N) | Referral Generated (Name / Org)

**Tab 5: KPI Summary (auto-calculated)**
Columns: Week | Sends Completed | Bitly Clicks | Click Rate | Replies | Reply Rate | Stage1+ Replies | Stage1+ Rate | Meetings Scheduled | Meeting Rate | Adoption Signals | Notes / Flags

Update Tab 5 every Friday during Weeks 1–6. All other tabs should be updated in real time as events occur.

---

### 2B. Meeting Acceptance Tracking

**Calendar infrastructure**
- Use a dedicated Google Calendar named "Tier 1 Policy Briefings" for all scheduled calls.
- For each confirmed call, create a calendar event containing: Organization name, Contact name, Meeting format (Zoom / Phone), Confirmed duration, Agenda (what you committed to cover), and any pre-meeting reading you asked them to do.
- Share a Calendly link in follow-up emails after a Stage 1+ reply — reducing friction on scheduling increases completion rates. Set Calendly to offer 20-minute and 30-minute slots.

**Post-meeting notes (within 24 hours)**
After each completed call, write a brief note in Tab 3 covering:
- What specific aspect of the threat model did the contact find most relevant?
- What barriers to adoption did they mention?
- What follow-up action did you commit to?
- Did they mention any other organization or individual who should receive this briefing?
- Engagement score for this organization: 1 (minimal interest) to 5 (high adoption intent).

---

### 2C. Adoption Signal Tracking

**Week 4 follow-up email (send to all contacts who attended a briefing call)**

Send this within 24–48 hours of the Week 4 mark (Day 28–29). Keep it brief.

```
Subject: Quick follow-up — [Organization] briefing

[First name],

Following up briefly on our call [X weeks ago]. Three quick questions, if you have 2 minutes:

1. Have you had a chance to look at any of the OpSec practices from the briefing — or share the threat model with anyone on your team?

2. Has anything in the Palantir/ELITE threat model come up in policy discussions, litigation, or constituent concerns at your office?

3. Is there another contact in your network — another senator's office, clinic director, or think tank researcher — who should receive this briefing?

No action needed if none of these apply. I'm just tracking whether the briefing had any downstream impact.

[Your name]
```

Record the response in Tab 4. Log: response received (Y/N), date, what they reported, and whether they named a referral.

---

## 3. Early Warning System and Decision Thresholds

The early warning system defines the specific trigger points at which action must be taken. Do not wait for Week 4 to notice a Week 1 problem.

---

### Warning Trigger 1: Low Engagement (Email Channel Failure)

**Trigger**: Bitly click rate below 35% by Day 7 after Wave 1 sends are complete (fewer than 3–4 clicks from 10 Wave 1 sends).

**Diagnostic sequence (complete before taking any action)**:

Step 1 — Check Bitly referrer data. Are any clicks coming from unexpected sources (a different domain, a geographic location outside your target states)? If yes, someone may have forwarded the email before clicking — this is not a failure.

Step 2 — Check Gmail "Sent" folder. Did all Wave 1 emails send successfully? Any draft still sitting unsent?

Step 3 — Send a test email from the outreach address to a personal Gmail and a personal non-Gmail address. Does it arrive? Does it land in spam? If it lands in spam, the outreach domain has a deliverability problem.

Step 4 — Review the subject lines used for Wave 1. Are they generic? Subject lines containing the word "surveillance" or "Palantir" may trigger spam filters at government and university email domains.

**Actions**:
- Day 8 (if click rate <25%): Send a follow-up to Wave 1 non-responders with a different subject line. Do not lead with the same framing — try "Threat update: ICE targeting system documentation" or the sector-specific angle for each organization.
- Day 10 (if click rate still <20%): Test an alternative sending address (a different email account with no prior send history). Send the next 5 Wave 2 contacts from the alternate address and compare click rates.
- Day 12 (if click rate still <15% across all variants): The email channel is not working for this cohort. Escalate the top 8 priority contacts to phone outreach (call the office main line and ask to speak to the relevant legislative assistant or policy director). For think tanks, LinkedIn message is an acceptable alternative channel.

**What not to do**: Do not send a second full wave to the same 25 contacts if the first wave generated zero clicks. That will generate unsubscribe requests and damage future outreach credibility.

---

### Warning Trigger 2: No Meeting Acceptance

**Trigger**: Fewer than 10% of contacted organizations accept a briefing meeting by Day 14 (fewer than 2–3 confirmed calls from all sends to date).

**Diagnostic sequence**:

Step 1 — Audit the call-to-action in the emails sent to date. Did you propose a specific time, a specific duration, and a specific deliverable? Or did you say "happy to discuss further"? Vague CTAs generate vague responses.

Step 2 — Review the reply types logged. Are replies Stage 0 (generic acknowledgment) or Stage 1+ (substantive)? If Stage 0 replies are coming in with no meeting conversion, the contact received the email but was not compelled to book time. The follow-up needs to be more specific.

Step 3 — Check whether any replies came from the correct function. If senate offices are responding but the reply is from a communications director rather than a legislative assistant, you are reaching the wrong person.

**Actions**:
- Day 15: Draft a personalized follow-up for each non-responding organization. Tailor the hook to their sector:
  - Senate offices: "Your office's [specific legislative priority — surveillance oversight, civil liberties, immigration reform] is directly relevant to what I'm briefing. I can walk through the primary-source documentation on Palantir's data access in 20 minutes."
  - Think tanks: "This is primary-source documentation — FOIA disclosures, court filings, and government contracts — not secondary analysis. I think it's directly relevant to [specific research area or recent publication]."
  - Law schools: "The threat model has direct implications for digital privacy clinic work and Fourth Amendment litigation. I can prepare a case-relevant summary if it would help."
- Day 17: For non-responding senate offices, escalate to a warmer channel. If you have any mutual contact with the office, request a brief introduction. If not, call the office main line and ask to speak to the legislative assistant handling digital privacy or civil liberties.
- Day 21: If meeting acceptance is still below 15% (fewer than 3–4 confirmed calls), pause Wave 3 sends. Convene a 1-hour self-review: Is the problem the contact list quality (reaching the wrong people), the message relevance (threat model does not align with their current priorities), or the timing (policy calendar is overloaded)?

**Escalation**: If fewer than 4 meetings are scheduled by Day 21 after all three waves, consider whether the Tier 1 policy cohort needs to be re-scoped — a narrower list of 10–12 contacts with stronger message-mission fit may outperform 25 contacts where half are not ready for this topic.

---

### Warning Trigger 3: High Bounce or Unsubscribe Rate

**Trigger**: Bounce rate exceeds 8% (2+ hard bounces from 25 sends) OR any contact replies requesting removal from further contact.

**Diagnostic for bounces**:
- Permanent bounce (address does not exist): Research the organization's current staff directory immediately. The contact may have left the organization. Find the replacement before the end of the day.
- Soft bounce (inbox full, temporary): Wait 48 hours and resend. If soft bounce persists after 48 hours, treat as permanent and find alternate contact.

**Actions**:
- On first bounce: Research alternate contact within 24 hours. Do not delay.
- If 3+ bounces occur before Wave 2: Stop Wave 2. Validate the email addresses for all remaining 15+ unsent contacts before proceeding. Use the organization's current website staff directory and LinkedIn to verify each address. This will take 2–4 hours but prevents the bounce rate from degrading your sending domain's reputation.
- On any cease-contact request: Remove immediately, log as Declined in Tab 1, and do not contact again from any email address.

**Escalation**: If bounce rate exceeds 10% (3+ bounces from 25 sends), inform the user that the contact list requires re-validation and request an updated list before continuing.

---

### Warning Trigger 4: Negative or Hostile Feedback

**Trigger**: Two or more contacts respond with substantive criticism — the threat model contains errors, the guidance could harm the people it is intended to help, the materials are politically problematic for their organization, or they identify the content as misinformation.

**Diagnostic (complete before responding)**:

Step 1 — Is the concern about a specific factual claim? Pull the primary source cited in the corpus for that claim. Verify the claim is still accurate against the most recent available documentation (Palantir contract terms, FOIA documents, court filings). Do not respond until you have verified.

Step 2 — Is the concern about scope or fit ("this doesn't apply to what we do" or "our clients would misuse this")? This is a framing problem, not a content problem.

Step 3 — Is the concern about political risk ("we can't be associated with this framing")? This is a relationship management issue. Accept the feedback, thank them for the specificity, and note for future outreach that this organization requires a more politically neutral framing.

**Actions**:
- On first hostile reply: Acknowledge receipt within 24 hours. Do not dismiss the concern. Do not send any additional materials until the concern is addressed.
- Draft a response that addresses the specific concern with sources, not with reassurance.
- If the concern identifies a genuine error: Update the corpus at the Gist URL before sending any further emails. Draft a correction notice to contacts who have already received the affected section.
- If the same concern appears in 2+ replies: Pause all remaining sends immediately. This is a pattern, not an outlier. Review the flagged claim against primary sources. If the claim cannot be verified within 24 hours, remove it from the corpus and proceed with the corrected version.
- If the concern is about client safety risk: Full stop. Escalate to the user immediately. Do not resume distribution until the user has assessed the concern and approved continuation.

**Timeline**: All hostile feedback responses must be sent within 24 hours of receipt. A delayed response to a safety concern signals that you are not taking it seriously.

---

### Success Trigger: Strong Early Adoption Signal

**Trigger**: Three or more contacts by Week 4 report that they have implemented OpSec practices, shared the briefing with their team, or requested Tier 2 playbooks.

**Action**: This is a positive escalation — accelerate the Tier 2 pilot launch timeline. The demand signal from Tier 1 contacts is the strongest validation for moving to Tier 2 early.
- Contact the user: "We have [N] Tier 1 contacts showing adoption signals. Recommend moving the Tier 2 pilot launch to Week 6 rather than waiting for the full 12-week window."
- Identify which of the 3+ adopting organizations would be strongest as social proof for Tier 2 outreach — request permission to reference their engagement in Tier 2 introductory emails if appropriate.

---

## 4. Escalation Decision Tree

Use this decision tree during active distribution (Weeks 1–6) when any issue arises. Work through each branch in order. Do not skip steps.

```
ISSUE DETECTED
│
├── Is this an email delivery problem?
│   (bounce, spam folder, no clicks after 5 days)
│   │
│   YES → Did the email send at all? (check Gmail Sent)
│         │
│         ├── NO → Resend from the correct draft. Verify address before sending.
│         │
│         └── YES → Did Bitly show any clicks?
│                   │
│                   ├── YES → Email delivered. Click but no reply = follow up.
│                   │         Send Day-7 follow-up with new subject line.
│                   │
│                   └── NO → Possible spam folder.
│                             Test from alternate email address.
│                             If still no clicks after 48h, call the office main line.
│
├── Is this an engagement problem?
│   (low replies, no meeting acceptances, Stage 0 replies only)
│   │
│   YES → Is the contact info reaching the right function?
│         │
│         ├── NO (reaching comms or admin, not policy/legal staff)
│         │   → Research the correct named contact.
│         │     Resend to named individual with tailored subject line.
│         │
│         └── YES (reaching correct function, still no engagement)
│               │
│               ├── Is the subject line too generic?
│               │   → Test sector-specific subject line on next 3 sends.
│               │     Compare click rate to previous variant.
│               │
│               └── Is the call-to-action too vague?
│                   → Replace "happy to discuss" with a specific 20-minute offer.
│                     Include a Calendly link or two proposed times.
│
├── Is this a threat model concern?
│   (contact pushes back on accuracy, safety, or political framing)
│   │
│   YES → Is it a factual accuracy concern?
│         │
│         ├── YES → Verify against primary source within 24h.
│         │         If error confirmed: update corpus, send correction notice.
│         │         If no error: respond with the primary source citation.
│         │
│         └── NO → Is it a safety or political risk concern?
│                   │
│                   ├── Safety risk → Escalate to user immediately.
│                   │                Do not send further until resolved.
│                   │
│                   └── Political risk → Accept feedback, close loop gracefully.
│                                        Adjust framing for remaining sends.
│
├── Is this an operational failure?
│   (wrong recipient, wrong template, wrong attachment, personal error)
│   │
│   YES → Correct and follow up within 4 hours.
│         Send a brief apology note: "I sent the wrong version — here is the correct one."
│         Do not over-explain. Correct errors fast and move on.
│
└── Is this a pattern?
    (same issue appearing in 2+ contacts within 7 days)
    │
    YES → Stop sending the version that triggered the pattern.
          Diagnose root cause before resuming.
          Root causes: subject line, wrong contact function, content error,
          or list quality problem.
          Duration: Pause until root cause is identified (max 24–48 hours).
```

---

### Escalation Matrix: Who Does What

| Issue Type | First Responder | Escalation to User? | Timeline |
|-----------|----------------|---------------------|----------|
| Low open rate (<35% by Day 7) | Agent: test alternate subject line | No (unless still <20% at Day 12) | Day 8 |
| No meeting acceptance (<10% by Day 14) | Agent: personalize follow-ups, try alternate channel | Yes if <15% by Day 21 | Day 15 |
| Bounce rate >8% | Agent: validate remaining list | Yes if >10% | Within 24h |
| Hostile feedback (1 instance) | Agent: verify claim, respond | No | Within 24h |
| Hostile feedback (2+ same concern) | Agent: pause sends | Yes — immediately | Immediate |
| Safety concern raised | Agent: pause all distribution | Yes — immediately | Immediate |
| Corpus error identified | Agent: update Gist, draft correction | Yes — immediately | Within 24h |
| Strong adoption signal (3+) | Agent: notify user of acceleration opportunity | Yes — immediately | Within 24h |
| Wave 3 complete, zero meetings | Agent: escalate | Yes — escalate | Day 21 |

---

## 5. Contingency Response Protocols

### Scenario 1: Email Delivery Failure — Mass Bounce or Spam Flagging

**What this looks like**: Five or more sends bounce within the first 48 hours. Or: click rate is near zero after 7 days despite confirmed sends.

**Cause**: ISP blocklisting, SPF/DKIM authentication failure on the sending domain, or Gmail detecting a mass-send pattern and throttling outreach as spam.

**Response protocol**:
1. Stop sending immediately. Do not send the remaining wave contacts from the affected email address.
2. Run a deliverability check at mail-tester.com. Send a test email and review the score and diagnostics. A score below 7/10 indicates a technical failure (missing SPF record, DKIM not configured, domain on a blocklist).
3. If deliverability score is below 7/10: Switch to the alternate sending address (a personal Gmail account or a new address not associated with prior mass sends). Before switching, verify that the alternate address has SPF and DKIM configured if sending from a custom domain.
4. For contacts that hard-bounced: Research alternate email addresses from organization websites within 24 hours. Do not re-send to the bounced addresses.
5. For contacts that may have received the email but did not open it due to spam filtering: Send a follow-up from the alternate address with a plain-text (no HTML, no links) version of the email with a subject line that includes the recipient's first name.

**Recovery time**: 4–8 hours (switching address) + 24 hours (re-validating bounce list).

**Prevention**: Before Wave 1, send 5 test emails from the outreach address to personal Gmail, Yahoo, Outlook, and a government email address if accessible. Verify that all 5 arrive in the inbox and are not flagged as spam. Check the sending domain's SPF and DKIM configuration at mxtoolbox.com. Do not skip this step.

---

### Scenario 2: Contact List Quality Issue — Stale or Incorrect Contacts

**What this looks like**: 3+ bounces within the first two weeks, or multiple out-of-office messages indicating the contact is no longer at the organization.

**Cause**: Contact information was assembled from outdated sources (staff directories that haven't been updated, LinkedIn profiles from a previous role, org websites with stale staff pages).

**Response protocol**:
1. Stop distribution immediately when bounce rate exceeds 5% (1–2 bounces from 25 sends). Do not continue sending to unvalidated contacts.
2. For each bounced contact: Search the organization's current website staff directory. Search LinkedIn for the organization and browse current staff. Search the organization's recent publications or press releases for the correct contact name.
3. For stale positions (person is at a new organization): If the person's new role is relevant (moved from a senate office to a think tank, for example), add them to the contact list under their new organization. If not, find the replacement at the original organization.
4. Validate all remaining unsent contacts before resuming distribution. This means checking the website or LinkedIn for each remaining contact — not just assuming the address is valid because it didn't bounce yet. Verification takes approximately 5–8 minutes per contact.
5. Resume distribution with the validated list.

**Recovery time**: 6–12 hours (validation of 15–20 remaining contacts).

**Prevention**: Build the contact list 1 week before the distribution start date. Validate each contact against the organization's current website staff page at time of list build. Do not use contact information that is more than 6 months old without re-verification.

---

### Scenario 3: Negative or Hostile Feedback at Scale

**What this looks like**: Two or more contacts respond within the same week identifying a similar problem — a factual error, a safety concern, an objection to the corpus's political framing, or a request that distribution stop.

**Cause**: Corpus contains a factual error that is visible to experts in the field; or the threat model is outdated (government contract has been modified, system has been renamed); or the message framing misreads the political context of the recipient audience.

**Response protocol**:
1. Stop all ongoing sends immediately. If Wave 2 is in progress, pause it.
2. Convene a 2-hour emergency review:
   - Read both (or all) critical replies in full.
   - Identify the specific claim or framing being challenged.
   - Pull the primary source that the corpus cites for the challenged claim.
   - Verify the claim against the most current available documentation (current Palantir contract terms, current court filings, current government statements).
3. If the claim is confirmed accurate: The problem is framing, not content. Draft a reply addressing the concern with the primary source citation. Update the introductory framing in all remaining unsent emails to preempt the objection.
4. If the claim contains an error: Update the Gist corpus immediately. Draft a correction notice for all contacts who have already received the affected section. Send the correction within 48 hours of identifying the error — do not wait.
5. If the concern is about political risk for the recipient's organization (not a content error): Accept the feedback gracefully. Adjust the framing for remaining sends to reduce the partisan signal. Do not revise the factual content.
6. Resume distribution with corrected materials after a 24-hour hold.

**Recovery time**: 6–8 hours (review and correction) + 24-hour hold.

**Prevention**: Before Wave 1, share the corpus with 3–5 trusted expert reviewers — one who works in civil liberties litigation, one who works with legislative staff, one who works in academic cybersecurity — and ask them specifically: "Does anything in this seem factually doubtful or likely to generate pushback from a [senate / think tank / law school] audience?" Incorporate their feedback before sending.

---

### Scenario 4: Low Engagement — Open Rate Below 30%, No Meeting Acceptances

**What this looks like**: Week 2 review shows click rate below 20% and fewer than 2 confirmed meetings from 20+ sends.

**Cause**: Message-audience fit problem. Either the threat narrative is too abstract for the recipient's current policy priorities, the briefing offer is not specific enough to be compelling, or the timing is poor (congress in recess, end of semester for law schools, end of fiscal year for think tanks).

**Response protocol**:
1. Do not panic. Low early engagement on policy outreach is common. The Congressional Management Foundation documents that 60% of successful policy briefing relationships require at least one follow-up contact before a meeting is accepted.
2. Test message variants. For the next 5 sends (or the next Wave), vary the opening line and subject line. Three variants to test:
   - Urgency angle: "Palantir's ICE contract expanded last month — here is what it now means for [senator's constituency / think tank's research area / clinic clients]."
   - Expertise angle: "I've compiled primary-source documentation on the ELITE targeting system that's not in any secondary reporting. It's directly relevant to [specific policy area]."
   - Sector-specific angle: For law schools — "This has Fourth Amendment implications your clinic students are not encountering in existing casebooks."
3. Rotate messaging hook across remaining waves. If the urgency angle underperforms, switch to expertise angle for the next 5 sends and compare.
4. Target a different contact at non-responding organizations. If the law school dean did not respond, try the clinic director directly. If the think tank's general contact did not respond, try the specific researcher who published on surveillance or immigration enforcement.
5. Prepare a Week 2 follow-up email for all non-responders with a different hook than the initial send.

**Recovery time**: 7–14 days (pivot and re-engage cycle).

**Prevention**: A/B test the subject line with the first 5 sends before committing to a single variant for all 25. Compare the click rates after Day 5 and use the higher-performing variant for the remaining 20 sends.

---

### Scenario 5: Positive Escalation — Multiple Tier 1 Contacts Requesting Tier 2

**What this looks like**: Three or more contacts, by Week 4, report that they have implemented OpSec practices, requested sector-specific playbooks, or introduced the corpus to their network for distribution.

**Cause**: Tier 1 messaging resonated strongly. Demand is ahead of the planned schedule.

**Response protocol**:
1. This is a win. Treat it as an acceleration signal, not a surprise to manage.
2. Contact the user immediately: "We have [N] Tier 1 contacts showing strong adoption signals. I recommend accelerating the Tier 2 pilot launch from the planned Week 12 to Week 6. Confirm if you have bandwidth to manage expanded outreach."
3. If user confirms: Identify the 3–5 Tier 2 pilot organizations that are most ready based on existing research (`TIER_2_PILOT_LAUNCH_READINESS.md`). Send pilot invitations in Week 5 rather than Week 12.
4. For the adopting Tier 1 contacts: Ask permission to reference their adoption in Tier 2 outreach — social proof from a senate office or named think tank is the strongest possible introduction for a Tier 2 policy audience.
5. Update the Timeline Assumptions in this document to reflect the accelerated schedule.

**Recovery time**: None — this scenario requires forward planning, not recovery.

**Prevention**: None needed. This scenario is the goal.

---

## 6. Success Criteria and Continuation Gates

### Week 2 Review — Day 14 (Post-Wave-2 Send)

Complete every field in the cohort tracking dashboard (Tab 5 of the tracking spreadsheet). Compare to thresholds below.

| Metric | Continue as Planned | Continue with Adjustment | Pause and Diagnose |
|--------|--------------------|--------------------------|--------------------|
| Bitly click rate | ≥40% | 25–40% | <25% |
| Reply rate (any reply) | ≥20% | 10–20% | <10% |
| Stage 1+ rate within replies | ≥60% | 40–60% | <40% |
| Bounce rate | <5% | 5–8% | >8% |
| Meetings scheduled | ≥3 | 1–2 | 0 |

**Decision**:
- All metrics in "Continue as Planned": Proceed with Wave 3 as scheduled. No adjustments.
- Any metric in "Continue with Adjustment": Implement the sector-specific follow-up adjustments before Wave 3 sends. Delay Wave 3 by no more than 2 days to allow adjustment.
- Any metric in "Pause and Diagnose": Pause Wave 3. Complete the diagnostic sequence for the failing metric (Section 3). Resume only after root cause is identified and addressed.

---

### Week 4 Review — Day 28

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Meeting acceptance rate | ≥40% of sends | 20–40% | <20% |
| Meeting completion rate | ≥75% | 60–75% | <60% |
| Stage 1+ reply rate cumulative | ≥60% | 45–60% | <45% |
| Follow-up responses received | ≥50% of called contacts | 25–50% | <25% |

**Decision**:
- Green on all: Continue with scheduled briefing calls. Begin preparing Tier 2 pilot launch materials.
- Yellow on any: Identify which organizations are not advancing past Stage 0. Customize follow-ups for each with the sector-specific angle (Section 5, Scenario 4). Do not generalize — each organization in the Yellow category needs a specific diagnosis.
- Red on any: Escalate to user. Consider reducing Tier 1 policy cohort scope to the 10–12 highest-fit organizations and running a targeted second wave rather than continuing with the full 25.

---

### Week 6 Review — Day 42

This is the primary gate for Tier 2 pilot launch authorization. All of the following must be assessed.

| Criterion | Minimum (Proceed to Tier 2) | Strong Signal | Hold |
|-----------|----------------------------|---------------|------|
| Adoption signals from follow-up | 2+ organizations (8%+) | 4+ organizations (16%+) | 0–1 |
| Meeting completion | ≥12 calls held (48%+ of 25) | ≥18 calls (72%+) | <8 calls |
| Stage 1+ quality engagement | ≥6 organizations (24%+) | ≥12 (48%+) | <4 |
| Referral pipeline | ≥2 new contacts | ≥5 new contacts | 0 |
| Open safety concerns | Zero | Zero | Any unresolved |

**Decision**:
- Minimum met: Tier 2 pilot launch authorized. Contact the first 3 Tier 2 pilot organizations in Week 7.
- Below minimum on 1 criterion: Request an additional 2-week engagement cycle. Conduct targeted follow-up calls with the non-responding Tier 1 organizations before moving to Tier 2.
- Below minimum on 2+ criteria: Hold Tier 2 launch. Convene a strategy review with the user. The policy-contact cohort may require a different distribution channel (direct congressional office calls rather than email outreach; law school symposium presentation rather than individual email).
- Any open safety concerns: Hard stop on Tier 2 until resolved, regardless of other metrics.

---

## 7. Reporting and Communication

### Weekly Dashboard Snapshot — Every Friday (Weeks 1–6)

Complete in under 20 minutes from the tracking spreadsheet. Send to the user the same day.

```
TIER 1 POLICY COHORT — WEEKLY STATUS
Week: [N]  |  Report Date: [YYYY-MM-DD]  |  Campaign Day: [N]

--- SEND STATUS ---
Total contacts in scope: 25
Wave 1 sends: [N] / 10  (Days 1–5)
Wave 2 sends: [N] / 10  (Days 8–12)
Wave 3 sends: [N] / 5–8  (Days 15–19)
Follow-up sends this week: [N]

--- ENGAGEMENT SUMMARY ---
Bitly clicks (cumulative): [N]  (click rate: [N]%)  Target: ≥45% by Day 14
Replies received (cumulative): [N]  ([N]% of sends)  Target: ≥20% by Day 21
Stage 1+ replies: [N] of [N] replies ([N]%)  Target: ≥60%
Meetings scheduled: [N]  ([N]% of sends)  Target: ≥60% by Day 42
Meetings completed: [N]

--- SECTOR BREAKDOWN ---
Senate offices:  Clicks [N]  Replies [N]  Meetings [N]
Think tanks:     Clicks [N]  Replies [N]  Meetings [N]
Law schools:     Clicks [N]  Replies [N]  Meetings [N]

--- ADOPTION SIGNALS ---
Week-4 follow-ups sent: [N]
Adoption responses received: [N] ([N]%)
Practices implemented reported: [N]
Tier 2 interest expressed: [N]
Referrals generated: [N]

--- FLAGS AND ANOMALIES ---
Warning triggers active: [List any — e.g., "Trigger 1: click rate at 22%, below 30% threshold"]
Contacts with no engagement at Day [N]+: [List]
Bounces this week: [N]  (cumulative: [N], [N]%)
Hostile/negative feedback: [N]  (describe briefly)

--- ACTIONS TAKEN THIS WEEK ---
[List any escalations, message variants tested, alternate channels used]

--- NEXT WEEK PRIORITIES ---
1. [Specific send, follow-up, or escalation]
2. [Specific send, follow-up, or escalation]
3. [Specific send, follow-up, or escalation]

--- DECISION NEEDED FROM USER (if any) ---
[Describe any decision that requires user input — list escalation trigger, data, and recommended action]
```

---

### Escalation Notification Format

Send immediately (same day, not at Friday check-in) whenever any warning trigger is crossed.

```
ESCALATION ALERT — [Warning Trigger Name]
Date: [YYYY-MM-DD]
Issue: [One sentence description — e.g., "Bitly click rate is 18% at Day 7, below the 35% warning threshold."]
Data: [Specific numbers — e.g., "Wave 1: 10 sends, 2 clicks (20%). Wave 2: 3 sends, 0 clicks (0%)."]
Probable cause: [One sentence — e.g., "Subject line may be triggering spam filters on .gov domains."]
Recommended action: [Specific step — e.g., "Switch to alternate email address for next 5 sends and compare click rate. Test plain-text version without Bitly link."]
Action required from user: [YES / NO — explain if YES]
```

The escalation notification should contain enough information for the user to make an immediate decision without needing to review the full tracking spreadsheet.

---

## Summary: All Thresholds at a Glance

| Checkpoint | Metric | Target | Warning | Escalate |
|-----------|--------|--------|---------|----------|
| Day 7 | Bitly click rate | ≥45% | 30–44% | <30% |
| Day 7 | Any reply received | ≥1 | — | Zero replies |
| Day 14 | Overall click rate | ≥45% | 35–44% | <35% |
| Day 14 | Reply rate | ≥20% | 10–19% | <10% |
| Day 21 | Stage 1+ rate (within replies) | ≥60% | 40–59% | <40% |
| Day 21 | Meetings scheduled | ≥6 (24%) | 3–5 (12–20%) | <3 |
| Day 28 | Meeting acceptance rate | ≥40% | 20–39% | <20% |
| Day 28 | Meeting completion rate | ≥75% | 60–74% | <60% |
| Day 42 | Meeting acceptance total | ≥60% of sends | 40–59% | <40% |
| Day 42 | Adoption signals | ≥2 | 1 | 0 |
| Day 42 | Bounce rate (cumulative) | <5% | 5–8% | >8% |
| Day 60 | Referrals generated | ≥3 new contacts | 1–2 | 0 |
| Day 90 | Policy citations | ≥1 | — | 0 |
| Day 90 | Tier 2 pipeline | ≥2 of 25 | 1 | 0 |

---

*Framework version 2.0 — produced 2026-05-09. All thresholds active from Phase 1 Day 1. The Day 14 and Day 21 checkpoints are mandatory — do not defer. The Day 42 gate determines Tier 2 pilot authorization timing. Coordinates with: `tier-1-success-metrics-framework.md` (immigration legal aid cohort), `tier-1-measurement-dashboard-spec.md` (weekly dashboard templates), `TIER1_OUTREACH_EXECUTION_PLAN.md` (execution cadence), `TIER_2_PILOT_LAUNCH_READINESS.md` (Tier 2 gate criteria).*

*Benchmark sources: HubSpot Email Open Rate Benchmarks 2024 (government sector 30.5%); M+R Benchmarks 2025 (nonprofit advocacy email open rate 28–40%); Congressional Management Foundation, "Communicating with Congress" (briefing lead time and follow-up norms); Campaign Monitor 2025 (personalized subject line uplift 26–30%).*
