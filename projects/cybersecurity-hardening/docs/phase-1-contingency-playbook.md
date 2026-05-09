---
title: "Phase 1 Contingency Playbook — Decision Trees for Launch Scenarios"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
executor: Anya
cross-references:
  - docs/phase-1-launch-runbook.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER1_EXECUTION_RUNBOOK.md
  - docs/phase-1-gist-creation-walkthrough.md
---

# Phase 1 Contingency Playbook — Decision Trees for Launch Scenarios

**Purpose**: Pre-decided response procedures for the five most common Phase 1 launch failure modes. Reading this document before launch means you will not need to make decisions under time pressure when a scenario occurs.

**Use this document**: At the first sign of any of the five scenarios below, navigate directly to that section. Each includes: symptom description, root cause analysis, a decision tree, response actions, and timing requirements.

**Confidence level**: These scenarios are based on the failure modes documented in TIER1 outreach precedent (Model Penal Code distribution, ABA Model Rules rollout, Brennan Center policy release patterns) and general email campaign operational experience. Likelihood estimates are rough; severity assessments are grounded in actual impact on campaign timeline.

---

## Scenario 1: High Email Bounce Rate

**Trigger**: More than 3 bounces (permanent delivery failures) from any single send wave, or bounce rate exceeding 15% of all sends cumulatively.

**Symptoms**:
- Gmail inbox shows delivery status notification: "Message undeliverable," "No such user," or "Domain not found"
- Bounced emails appear in your sent folder with a red warning indicator
- Recipient email addresses in the format `{firstname}@{org}.org` produce bounce when the org's email server rejects the format

**Root Cause Analysis**:

Before taking action, spend 5 minutes diagnosing which type of bounce you have:

| Bounce Type | Indicator | Severity |
|-------------|-----------|----------|
| Permanent (hard) bounce | "550 No such user" or "5.1.1 user unknown" | High — research alternate immediately |
| Soft bounce | "452 Mailbox full" or "421 Service unavailable" | Medium — retry after 48 hours |
| Domain-level rejection | "550 Domain not found" or "5.4.1" | High — domain may have changed; verify org's current domain |
| Spam rejection | "550 Message rejected as spam" | High — review email content for spam triggers |

**Decision Tree**:

```
START: Bounce received
│
├─ IF bounce type = soft (mailbox full / temporarily unavailable)
│   └─ Action: Wait 48 hours; retry once. If bounces again, treat as permanent.
│
├─ IF bounce type = permanent (user unknown / domain not found)
│   │
│   ├─ IF bouncing org is one of the 5 named Day 1 contacts
│   │   └─ IMMEDIATE: Research alternate contact
│   │       Steps: (1) Check org website "Contact Us" page for current email
│   │               (2) Search "[org name] press contact" in news databases
│   │               (3) Try web contact form as fallback
│   │               (4) If no alternate: mark "Unreachable" in spreadsheet
│   │
│   ├─ IF bounce rate > 15% of a single wave (3+ of 5 contacts)
│   │   └─ STOP that wave. Do not send remaining emails from same wave.
│   │       Action: Audit contact list for that wave. Are all addresses
│   │               from the same source? Were they verified on org websites?
│   │               Fix the contact list before continuing.
│   │
│   └─ IF bounce is from a regional contact (not named Day 1 org)
│       └─ Research alternate. Common domain errors for regional orgs:
│           - .org vs. .com vs. .net (verify on org's own website)
│           - Hyphenated domains (e.g., make-the-road.org vs. maketheroadny.org)
│           - Organization renamed since email was sourced

DOMAIN-SPECIFIC NOTES (known verification from TIER1_OUTREACH_PREPARED.md):
- CLINIC domain is cliniclegal.org — NOT clinic.org (different organization)
- RAICES domain is raicestexas.org
- CDM domain is cdmigrante.org — NOT centrocdm.org
- Always verify .org vs. .com before each send
```

**Response Actions**:

1. Log every bounce in tracking spreadsheet immediately: Organization | Bounce Type | Date | Action Taken
2. Apply `Tier1-Outreach/Bounce` label to the bounce notification in Gmail
3. For permanent bounces: research alternate contact within 1 hour; do not let the research drag beyond the current send day
4. Update TIER1_CONTACTS section of tracking spreadsheet with corrected contact information
5. If web form is the only fallback for a named organization: use it. Confirmed fallback forms are in `TIER1_OUTREACH_PREPARED.md` (NILC: nilc.org/about-us/contact-us/)

**Timeline**: Bounce investigation must complete within the same day the bounce is received. Delayed investigation means delayed re-send, which risks missing the contact's inbox during their responsive window.

**Impact on campaign**: A bounce rate above 15% is a signal to pause and audit before continuing. A bounce rate below 15% is within normal range for cold outreach to organizational inboxes.

---

## Scenario 2: Reply Volume Exceeds Response Capacity

**Trigger**: More than 8 replies received in a single day, or total replies exceeding the time you can dedicate to personalized responses (roughly 20–30 minutes per engagement response).

**Symptoms**:
- Gmail inbox shows multiple responses from different organizations in a single day
- Responding thoughtfully to each reply would take more than 2 hours that day
- You feel pressure to respond quickly to all of them

**Note on context**: Receiving many replies is a positive signal, not a problem. The challenge is managing response quality when volume is high. A poor response to an engaged contact damages a relationship that took months of corpus work to initiate. Do not rush responses to hit an arbitrary timeline.

**Decision Tree**:

```
START: Reply volume high
│
├─ IF volume = 8-15 replies over multiple days (not same-day spike)
│   └─ No change to process. Respond to each in priority order:
│       Priority 1: Engagement responses (questions, sharing intent)
│       Priority 2: Acknowledgment responses (light follow-up needed later)
│       Priority 3: Declination (Template R3, close same day — fast)
│       Reply within 24 hours to all Priority 1; 48 hours to Priority 2.
│
├─ IF volume = 5+ Engagement responses in a single day
│   │
│   ├─ OPTION A: User has capacity → Personalized responses to each
│   │   Recommended: respond in order of organization priority
│   │   (named Day 1 orgs first, regional contacts second)
│   │
│   └─ OPTION B: User does not have capacity that day
│       Deploy templated bridge response (15 min total for all):
│       Template:
│         "Thank you for the response — this is on my radar and I'll follow up
│          with substantive notes within 48 hours. In the meantime, the full
│          corpus is at [BITLY_URL] and the most actionable section for your
│          context is Part 0 (data broker opt-outs, no technical expertise
│          required, 2–4 hours)."
│       Then: prioritize responses over next 48 hours, starting with the
│       organization that expressed the most specific interest.
│
└─ IF volume exceeds 15 replies/day (unexpected viral spike)
    └─ Pause new sends (Waves 3–5) to avoid further volume increase.
        Assess: Is this sustainable? Are the replies from high-value organizations?
        If yes: allocate 2–3 hours/day to response management for 3–5 days.
        If no: deploy template bridge, identify 5 highest-value respondents,
        prioritize those, and send Template R2 light acknowledgment to the rest.
```

**Response Actions**:

1. Create a `CSH-Priority-Replies` Gmail label for any Engagement response from a named national organization (NILC, CLINIC, RAICES, ILRC, NLG) — these are the highest-leverage relationships.
2. Draft and save a "bridge" template in Gmail (compose → Templates) for days when personalized responses aren't feasible same-day.
3. Do not pause entire campaign unless volume is genuinely unmanageable. High reply volume is Phase 1 success.
4. Log all responses in the Response_Log sheet (Sheet 3 of tracking spreadsheet) regardless of when you reply.

**Timeline**: Engagement responses (Class 1) require a reply within 24–48 hours. Beyond 48 hours, the engaged contact loses momentum and may deprioritize the corpus. The bridge template buys 48 hours without sacrificing the relationship.

---

## Scenario 3: Press or Media Inquiry During Phase 1

**Trigger**: A journalist, podcast host, or social media account contacts you about the corpus or the outreach campaign.

**Symptoms**:
- Email from a journalist address (often ending in a news organization domain) asking about the corpus or the campaign
- Social media direct message asking about the Gist
- A contact from your outreach list mentions the corpus publicly (Twitter/Bluesky/Mastodon) and tags you or the Gist URL

**Why this matters**: Media coverage during Phase 1 can substantially accelerate corpus distribution — or it can create an uncontrolled narrative if you are unprepared. The decision of whether to engage and how must be made within 2–4 hours of the inquiry.

**Decision Tree**:

```
START: Press or media inquiry received
│
├─ SOURCE: Journalist from a major outlet (NYT, WaPo, The Intercept, 404 Media,
│          Wired, EFF Deeplinks, Freedom of the Press Foundation, ProPublica)
│   │
│   ├─ IF on-record interview request (they want to quote you by name)
│   │   └─ ESCALATE TO USER IMMEDIATELY (this is a decision that requires
│   │       user review, not an autonomous response).
│   │       Interim reply (send within 2 hours):
│   │       "Thanks for reaching out. I'm reviewing your request and will
│   │        respond within [24 / 48] hours. In the meantime, the full
│   │        corpus is publicly available at [BITLY_URL]."
│   │
│   └─ IF background briefing (off-record, context only)
│       └─ Acceptable to respond without user escalation if:
│           (a) The outlet is credible and relevant to the corpus audience
│           (b) You are confident in the primary-source basis of all claims
│           Response: Offer 30-min background briefing, "not for attribution."
│           Key message points (see below).
│
├─ SOURCE: Independent journalist, blogger, or newsletter writer
│   ├─ IF publication has relevant readership (privacy, immigration, civil liberties)
│   │   └─ Same as major outlet background briefing — offer briefing call
│   │       or email Q&A, "not for attribution" unless user approves on-record.
│   │
│   └─ IF publication is low-quality, partisan, or adversarial
│       └─ Decline politely: "Thanks for the interest. The full corpus is
│          publicly available at [BITLY_URL]." Do not offer briefing.
│
├─ SOURCE: Social media account (activist, advocacy org, influencer)
│   └─ Do not respond to unsolicited social media DMs. If they share the
│       corpus publicly (repost, link), that is amplification — positive signal.
│       No response needed. Log in Amplification_Tracker.
│
└─ SOURCE: Unknown / suspicious (no clear affiliation)
    └─ Politely decline: "The full corpus is publicly available at [BITLY_URL].
       No further comment at this time."
```

**Key Message Points for Background Briefing**:

If you do a briefing call or email Q&A (background only), these are the three points to convey clearly:

1. **Primary-source basis**: Every factual claim in the threat model is sourced to FOIA disclosures, government contracts on USASpending.gov, court filings, or primary investigative reporting. The corpus is not an opinion document.

2. **Target audience**: The corpus is designed for the populations most at risk from the surveillance infrastructure it documents — immigration legal aid organizations, community organizations serving undocumented clients, and mutual aid networks. It is not a political document; it is a practical safety guide.

3. **Access**: The full corpus is publicly available at `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`. Anyone can access and share it.

**If media inquiry results in coverage**: Log in Amplification_Tracker. If coverage appears online, note the URL and estimated audience size. This is a significant amplification signal — accelerate Tier 2 outreach timing if relevant outlets are covering the corpus.

**Timeline**: Press inquiry responses must be sent within 2–4 hours. Journalists on deadline cannot wait. If the deadline is shorter, the bridge response buys you time.

---

## Scenario 4: Organization Requests Modifications to the Corpus

**Trigger**: A contact replies with substantive feedback requesting changes to the corpus content — corrections, additions, framing adjustments, or sector-specific customization.

**Symptoms**:
- Reply text includes phrases like "the guide says X, but we have found Y," or "could you add a section on Z," or "the framing in section W doesn't work for our clients"
- Reply is substantive and comes from someone who appears to have read the corpus carefully
- Reply asks whether an updated version is planned

**This is a positive signal**: Organizations providing content feedback are engaged with the corpus at a deep level. They are potential Phase 2 adoption partners.

**Decision Tree**:

```
START: Modification request received
│
├─ TYPE: Factual error (incorrect statistic, outdated contract figure,
│         wrong agency name, broken URL citation)
│   └─ Do NOT modify Phase 1 corpus mid-campaign. Consistency matters —
│       recipients who received the corpus on Day 1 should see the same
│       version as recipients on Day 15.
│       Action:
│         (1) Log the error in "Phase 1 Feedback Log" (see below)
│         (2) Respond: "Thanks for catching this. We're documenting all
│             feedback for a quarterly review and update. The updated
│             version will be published at the same URL in July."
│         (3) Verify whether the error is in the Gist or in the tracking
│             spreadsheet. If it's a citation that affects legal advice,
│             flag as Priority 1 for the quarterly update.
│
├─ TYPE: Strategic addition (new topic, new threat vector, sector-specific
│         content the org wishes existed)
│   └─ Action:
│         (1) Log in "Phase 1 Feedback Log" under "Phase 2 candidates"
│         (2) Assess: Is this a request that maps to an existing Phase 2
│             domain? (See `PHASE_2_SEQUENCING.md` for domain candidates)
│         (3) Respond: "This is on our Phase 2 roadmap. The next version
│             (targeting [June/July]) will include [topic]. We'll notify
│             you when it's published."
│         (4) Add the contact to a Phase 2 notification list in your
│             tracking spreadsheet.
│
├─ TYPE: Framing issue (language doesn't resonate with their audience,
│         tone is off for their organizational context)
│   └─ Action:
│         (1) Log in "Phase 1 Feedback Log" under "Framing feedback"
│         (2) Respond with acknowledgment: "Thanks for this — this kind
│             of feedback is exactly what helps us refine the materials
│             for different contexts."
│         (3) If the org wants to create an adapted version for their
│             audience: support this. The corpus is open-source. An adapted
│             version they distribute to their network is amplification.
│             Offer to review their adapted version before they publish.
│         (4) Flag for Phase 2 messaging refinement.
│
└─ TYPE: Scope creep or out-of-scope request (unrelated topic, political
          framing the project doesn't support, etc.)
    └─ Action: Politely decline. "The corpus is focused specifically on
        [surveillance infrastructure and countermeasures]. Expanding to
        [unrelated topic] is outside our current scope, but thanks for
        the suggestion."
```

**Phase 1 Feedback Log**:

Create a document titled "Phase 1 Feedback Log" (a new tab in your tracking spreadsheet, or a standalone document). Columns:

| Date | Organization | Contact | Feedback Type | Feedback Summary | Priority | Action Taken |
|------|-------------|---------|--------------|-----------------|---------|-------------|
| | | | Factual error / Strategic addition / Framing issue / Scope creep | | High/Medium/Low | |

Do not modify the Phase 1 Gist based on any single feedback event during the active campaign. All modifications go into the quarterly review process.

**Timeline**: Respond to modification requests within 48 hours. The contact is engaged; do not let them go cold.

---

## Scenario 5: Technical Email Delivery Failure

**Trigger**: Emails appear to be sent (in your Gmail sent folder) but recipients report not receiving them, or Bitly shows zero clicks despite multiple sends.

**Symptoms**:
- Emails are in your Gmail sent folder but no responses received after 5+ days
- Bitly click counter shows 0 or very low clicks despite 20+ sends
- A contact you emailed directly tells you they never received your message
- Gmail shows a "Sending..." status that never resolves

**Root Cause Analysis**:

This scenario has several distinct causes requiring different fixes. Spend 15 minutes diagnosing before taking action.

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| 0 Bitly clicks from 20+ sends | Emails landing in recipient spam | Ask 1–2 contacts to check spam; review email content |
| Emails in sent folder but 0 responses after 7 days | Silent spam filtering (emails delivered to spam without bounce) | Send test to personal email; check if it lands in spam |
| "Sending..." never resolves | Gmail SMTP rate limit hit | Stop sending for 24 hours; check Gmail settings |
| Emails not in sent folder | Gmail account issue | Check Gmail settings → Sent Mail |
| Single recipient reports non-receipt | Individual org's spam filter blocking your domain | Use web contact form for that org as fallback |

**Decision Tree**:

```
START: Suspected delivery failure
│
├─ STEP 1: Verify the problem is real.
│   Send a test email from your outreach account to your personal email.
│   │
│   ├─ IF test email arrives in personal inbox → No account-level issue.
│   │   Problem may be recipient-specific or content-specific.
│   │   Continue to STEP 2.
│   │
│   └─ IF test email lands in personal spam → Content or authentication issue.
│       See "Fix: Spam content" below.
│
├─ STEP 2: Ask a trusted contact to check spam.
│   Contact one or two people you know personally. Ask them to check their
│   spam folder for an email from your outreach address.
│   │
│   ├─ IF email is in their spam → Content or sender reputation issue.
│   │   See "Fix: Spam content" below.
│   │
│   └─ IF email is NOT in their spam → Your email is being delivered to
│       them. The issue may be specific to organizational email filters.
│       Continue to STEP 3.
│
├─ STEP 3: Check organizational-level filtering.
│   Some organizations (particularly large nonprofits and legal aid orgs)
│   use aggressive spam filtering that silently discards cold outreach.
│   │
│   └─ Action: For organizations with web contact forms (NILC, others),
│       use the form as a fallback. Form submissions bypass email spam filters.
│       Log in spreadsheet: "Resent via web form — [date]"
│
└─ STEP 4: If Gmail account itself is the issue.
    Symptoms: Cannot send new emails; Gmail shows "Account suspended" warning.
    └─ Action: Check Gmail → Settings → General → Account information.
        If suspended: Follow Google's account recovery process.
        If rate limited: Stop all sends for 24–48 hours. Gmail limits free
        accounts to 500 emails/day (well above your campaign rate of 5/day).
        If you have been sending test emails and campaign emails simultaneously,
        you may have hit a per-hour limit. Reduce send pace.
```

**Fix: Spam Content**

If your email is landing in spam, review the email text for common spam triggers. Remove or replace any of the following:

- All-caps words or phrases (e.g., "URGENT" or "FREE GUIDE")
- Multiple exclamation points
- Unverified or suspicious-looking links (use the Bitly short URL, not bare Gist URL)
- Excessive use of "click here" or "visit this link"
- Long subject lines (keep under 60 characters)
- Attachments (you should not be attaching files — link to Gist only)

After revisions, re-test by sending to your personal email. If it no longer lands in spam, resume sends.

**Fix: Sender Reputation**

If the issue persists after content review, your outreach email domain may have a poor sending reputation. Options:

1. **Use a different "from" address**: Create a new Gmail account for outreach. Before switching, decide whether you want replies to go to the new address or the original.
2. **Use a mail merge service**: Mailchimp (free tier, up to 500 contacts), Lemlist, or SendInBlue have better sending infrastructure and deliverability rates than personal Gmail. The tradeoff: emails will have an "unsubscribe" footer, which may reduce credibility for this specific corpus.
3. **Use web contact forms exclusively**: For organizations with forms (NILC), this bypasses email entirely. Less scalable for a 50-contact campaign but reliable.

**Timeline**: Delivery failure investigation requires resolution within 24 hours. If you cannot diagnose the issue same-day, pause the campaign and use web contact forms as a temporary fallback for any remaining named organizations.

---

## All-Scenarios Post-Incident Logging

After resolving any scenario, add an entry to the Notes column of the relevant tracking spreadsheet rows and to a separate "Incident Log" sheet:

| Date | Scenario Type | Trigger | Root Cause | Resolution | Campaign Impact | Phase 2 Note |
|------|--------------|---------|-----------|-----------|----------------|-------------|
| | | | | | (delay, no impact, positive) | (what to do differently in Phase 2) |

This log is the primary input for improving Phase 2 execution. The incidents you encounter in Phase 1 are the best signal for what to pre-solve before scaling to 45+ contacts in Tier 2.

---

## Quick Reference: Scenario Decision Table

| Scenario | Severity | First Action | Time to Resolve |
|----------|---------|-------------|----------------|
| High bounce rate (>15%) | High | Stop that wave; audit contact list | Same day |
| Soft bounce (single contact) | Low | Wait 48h; retry once | 48 hours |
| High reply volume | Positive | Prioritize Engagement; bridge template if needed | 24–48 hours |
| Press inquiry — major outlet | High | User escalation within 2 hours; bridge reply | 2–4 hours |
| Press inquiry — minor/unknown | Low | Decline politely; log | Same day |
| Modification request | Medium | Acknowledge; log in feedback log; respond within 48h | 48 hours |
| Email in recipient spam | High | Content review; test resend | Same day |
| Gmail account issue | High | Follow Google recovery; use web forms as fallback | Same day |
| Social media amplification | Positive | Log in Amplification_Tracker | No action needed |

---

## Escalation to User

The following scenarios require user escalation before any response or action:

1. **On-record interview request from a major publication**: User must approve before any interview or on-record quote.
2. **Legal threat or cease-and-desist letter**: Halt all sends immediately. User decision required before any response.
3. **Hostile response from a government entity or law enforcement contact**: Do not respond. Alert user immediately.
4. **Security incident** (evidence that your outreach account has been compromised or that someone is monitoring the campaign): Alert user immediately, pause all sends.

For all other scenarios, the decision trees in this document provide sufficient guidance for autonomous resolution.
