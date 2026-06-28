---
title: "Email Deliverability Test Results"
project: career-training
phase: "2"
created: 2026-06-28
status: test-protocol-and-pre-execution-findings
test-subscriber: testcareertraining@protonmail.com
---

# Email Deliverability Test Results

**Purpose**: Document the Kit.com platform test protocol, pre-execution research findings, and execution results (to be filled in after user completes account creation). This document covers what can be established through research (platform deliverability benchmarks, test setup, expected results, known risks) and leaves clear blanks for user-executed test data.

**Confidence note**: Sections marked [RESEARCH] contain pre-verified data. Sections marked [TO BE EXECUTED] require the user to run the actual test and fill in results. Sections marked [BLOCKER IDENTIFIED] flag issues that may prevent successful test completion.

---

## Test Setup

### Test Subscriber

**Email address**: testcareertraining@protonmail.com  
**Purpose**: Receive the Day 0 welcome email and subsequent sequence emails as if a real subscriber  
**Instructions**:
1. Create this ProtonMail account before running the test (ProtonMail is free at protonmail.com, no credit card required)
2. After Kit account is set up, subscribe this address via the Residential GC Path signup form
3. Use tag `residential-gc` (confirm it was applied correctly in Kit's Subscribers view)
4. Verify the account in ProtonMail and watch for the Day 0 welcome email

**Why ProtonMail for testing?**  
ProtonMail has aggressive spam filtering and is not a corporate email server with pre-warmed relationships to Kit's sending domains. If emails arrive in ProtonMail's primary inbox, they will almost certainly arrive in Gmail and Outlook inboxes as well. If they land in spam on ProtonMail, investigate before sending to any real subscribers.

**Additional test accounts to check (optional but recommended)**:
- A Gmail account you control — Gmail's Promotions tab placement vs. Primary inbox is the real-world deliverability test that matters most for this audience
- An Outlook/Hotmail account — Microsoft's filtering is distinct from Google's; construction professionals are more likely to use Outlook if they have a company email

---

## Section A: Delivery Latency

### [RESEARCH] Expected Delivery Times

Based on Kit platform documentation and independent testing (2025-2026):

| Email Type | Expected Delivery Window | What Causes Delay |
|---|---|---|
| Automation welcome email (Day 0) | 1-5 minutes after subscribe | Kit's automation processing queue; longer during peak send times (10 AM - 2 PM local) |
| Sequence email (Day 3) | Delivered at the scheduled time ± 15 minutes | Kit's job scheduler; no user action required |
| Broadcast email (manual send) | 1-10 minutes for small lists; 30-90 min for 10,000 subscriber sends | Proportional to list size |

### [TO BE EXECUTED] Actual Delivery Times

Log the following after running the test:

| Email | Subscribe Time (UTC) | Email Received Time (UTC) | Latency | Inbox Tab (Primary/Promotions/Spam) |
|---|---|---|---|---|
| Day 0 Welcome | [fill in] | [fill in] | [fill in] | [fill in] |
| Day 3 Module Deep-Dive | [fill in] | [fill in] | [fill in] | [fill in] |
| Day 7 Case Study Teaser | [fill in] | [fill in] | [fill in] | [fill in] |

**Success threshold**: All 3 emails delivered within 10 minutes of trigger time (or within 30 minutes if Kit queue is delayed). Landing in Promotions tab is acceptable; landing in Spam is a failure requiring investigation.

---

## Section B: Spam Folder Check

### [RESEARCH] Kit Deliverability Benchmarks

From independent testing (not Kit's own marketing):

- **Kit's claimed delivery rate**: 99.8% — but this measures server acceptance (the receiving server accepted the email), not inbox placement. These are not the same metric.
- **EmailToolTester independent test (2025)**: 88.2% average deliverability across all major inbox providers. Solid but not best-in-class.
- **EmailDeliverabilityReport.com test (most recent available)**: 76.59% of Kit emails reached the primary inbox; 19.83% landed in spam.
- **Kit-specific spam rate threshold**: Gmail requires sender spam complaint rate below 0.10%. Kit accounts that send unsolicited email or have high complaint rates get their deliverability degraded.

**What affects deliverability on a new Kit account**:

1. **New sender domain**: A brand-new Kit account has no sending history. The first few emails to real addresses will be scored by receiving servers against Kit's shared IP reputation, not your personal reputation. Kit maintains solid shared IP reputation, so this works in your favor initially.

2. **"Powered by Kit" footer**: The mandatory branding footer on free-plan emails includes a link to Kit.com. This is a known sender signal that receiving servers recognize — generally positive, as Kit is a reputable ESP (Email Service Provider) with active spam management.

3. **Subject line content**: Avoid spam trigger words in subject lines: "FREE," "GUARANTEED," "$$," exclamation marks in sequence (e.g., "You're in!!!"). The subject lines in WELCOME_SEQUENCE_DRAFT.md are clean in this regard.

4. **Sending domain authentication**: Kit sends from a shared domain by default. For best deliverability, add a verified sending domain in Settings > Email Sending. This adds SPF, DKIM, and DMARC authentication from your own domain, which significantly improves inbox placement. Set up before reaching 100 subscribers.

5. **Subscriber engagement**: The highest deliverability signal is subscribers who open emails. Early in your list's life, every open and click improves your sender reputation. This is why Email 2 (case study scenario) is designed to prompt engagement — not just as content, but as a deliverability mechanism.

### [TO BE EXECUTED] Actual Spam Folder Check

| Provider | Email 1 | Email 2 | Email 3 | Notes |
|---|---|---|---|---|
| ProtonMail | Primary / Promotions / Spam | Primary / Promotions / Spam | Primary / Promotions / Spam | [fill in] |
| Gmail (if tested) | Primary / Promotions / Spam | Primary / Promotions / Spam | Primary / Promotions / Spam | [fill in] |
| Outlook (if tested) | Primary / Promotions / Spam | Primary / Promotions / Spam | Primary / Promotions / Spam | [fill in] |

**Action if any email lands in spam**:
1. Do not proceed to Phase 2 subscriber acquisition until spam placement is resolved
2. Check: Is the subject line triggering spam filters? Test with Mail-Tester.com (free tool — paste email content and get spam score)
3. Check: Is sender domain authenticated? (Settings > Email Sending > Sending Domain)
4. Check: Is your account sender reputation clean? (Kit dashboard > Account > Deliverability if available)
5. Consider: ProtonMail is more aggressive than Gmail. If email lands in ProtonMail spam but not Gmail, that is acceptable (ProtonMail users are not your primary audience)

---

## Section C: Email Opens and Clicks

### [RESEARCH] What the Free Plan Tracks

Kit's free Newsletter plan includes:
- **Open tracking**: Yes — Kit embeds a 1x1 tracking pixel in each email. Open is recorded when pixel loads. Apple Mail Privacy Protection (iOS 15+) pre-fetches pixels, inflating open rates for Apple Mail users. This affects all ESPs equally.
- **Click tracking**: Yes — Kit wraps all links with redirect URLs. Every link click is recorded with timestamp.
- **Individual subscriber engagement**: Yes — in Subscribers view, you can see each subscriber's open and click history
- **Aggregate broadcast analytics**: Yes — broadcasts show open rate, click rate, unsubscribes
- **Automation analytics**: The free plan's basic automation shows subscriber counts through each step; full step-by-step analytics may require paid plan (verify in dashboard)

### [TO BE EXECUTED] Open and Click Results

After sending Email 1 and receiving it at the test subscriber address:

1. Open the email (this triggers the open event)
2. Click at least one link in the email (this triggers the click event)
3. Check Kit dashboard: Broadcasts or Automations > Email 1 stats

| Metric | Expected | Actual |
|---|---|---|
| Email 1 open recorded | Yes (within 1 min of opening) | [fill in] |
| Email 1 click recorded | Yes (within 1 min of clicking) | [fill in] |
| Test subscriber shows in Subscribers view with tag `residential-gc` | Yes | [fill in] |
| Open tracking works for sequence emails | Yes | [fill in — check after Email 2 arrives] |

---

## Section D: Automation Trigger Test

This is the highest-risk test. It validates whether the path-based routing automation works as designed on the free plan.

### [BLOCKER IDENTIFIED] Critical Platform Risk

**Finding from pre-execution research**: Multiple independent sources (including Mailsoftly, Automation Atlas, startupowl.com Kit review) indicate that the Kit free plan's "1 basic visual automation" does NOT include conditional branching (if/then logic). Branching logic — routing subscribers to different email variants based on their tag — requires the Creator paid plan ($33/month).

**Impact on the path-routing automation**: The PHASE_2_3_EXECUTION_ROADMAP.md design ("single automation with path-tag branching, free plan compatible") may not be implementable as described. The automation may only support a simple trigger-action: "subscriber added → send welcome email" without the ability to check the subscriber's tag and route accordingly.

**The workaround that does not require branching** (also documented in PHASE_2_3_EXECUTION_ROADMAP.md Contingency B):

Path routing does not require conditional branching if each signup form enrolls subscribers directly into the correct Sequence at subscribe time. The sequence is the path-specific email series. The form is the routing mechanism.

- Residential GC form → at subscribe, auto-enroll in "Residential GC Welcome Sequence"
- Industrial GC form → at subscribe, auto-enroll in "Industrial GC Welcome Sequence"
- Specialty Sub form → at subscribe, auto-enroll in "Specialty Sub Welcome Sequence"
- Generic form → at subscribe, auto-enroll in "Generic Welcome Sequence"

If this is possible, the branching automation is unnecessary. **The test is: can you configure a Kit form to auto-enroll subscribers in a specific Sequence at subscribe time?**

### [TO BE EXECUTED] Automation Test Protocol

**Test A: Branching automation test** (confirm whether branching is available on free plan)

1. In Kit's Automation builder, create a new visual automation
2. Set trigger: "Subscriber added to any form"
3. Attempt to add a condition step: "IF subscriber has tag `residential-gc`" → branch to send Email A; ELSE → send Email B
4. Document: Does the UI allow adding a condition step, or does it prompt for plan upgrade?

**Result**:
- [ ] Condition step available → branching works on free plan → build the path-routing automation as designed
- [ ] Condition step locked behind paywall → branching NOT on free plan → use Sequences workaround below

**Test B: Sequence direct-enroll test** (confirm workaround)

1. Create a Sequence in Kit: Sequences > New Sequence > "Residential GC Welcome Sequence"
2. Add Email 1 content to the sequence
3. Go to Forms > Residential GC Path form > Settings
4. Look for an option to "Enroll subscribers in a sequence" at subscribe time
5. Select "Residential GC Welcome Sequence"
6. Subscribe the test email via the Residential GC form
7. Verify: Does the test subscriber get enrolled in the Sequence? Does Email 1 arrive?

**Result**:
- [ ] Sequence direct-enroll works → path routing via forms is the production approach → no branching automation needed
- [ ] Sequence direct-enroll not available on free plan → escalate; consider Creator plan upgrade or a single-email-per-path broadcast approach

**Test C: Tag trigger timing test** (how quickly does automation fire after subscribe?)

1. Subscribe testcareertraining@protonmail.com via the Residential GC Path form
2. Record the exact time of subscribe
3. Record the time the welcome email arrives at testcareertraining@protonmail.com
4. Record the time the tag `residential-gc` appears on the subscriber in Kit's Subscribers view

**Expected results**:
- Tag applied: Within 10 seconds of subscribe
- Welcome email (Day 0): Within 5 minutes of subscribe
- Subscriber visible in list: Within 30 seconds of subscribe

**Actual results**:

| Event | Expected Time (from subscribe) | Actual Time | Notes |
|---|---|---|---|
| Tag `residential-gc` applied | < 10 seconds | [fill in] | |
| Test subscriber appears in Subscribers list | < 30 seconds | [fill in] | |
| Day 0 welcome email received | < 5 minutes | [fill in] | |
| Day 0 email opens tracked in dashboard | < 5 minutes after opening | [fill in] | |

---

## Section E: Integration Surprises

### [RESEARCH] Known Surprises Identified Pre-Trial

These are issues that the research phase surfaced, before account creation:

| Surprise | Severity | Impact on Phase 2 |
|---|---|---|
| API access may require paid plan | Medium | Future quiz-to-tag integrations blocked until Creator upgrade; core email delivery unaffected | 
| Visual automation branching may require paid plan | High | Path routing requires workaround (Sequences per path); extra setup but functional |
| "Powered by Kit" badge mandatory on free plan | Low | Professional appearance mildly affected; no functional impact; remove at first paid upgrade |
| Creator Network Recommendations mandatory on free plan | Low | Other creators' newsletters may be suggested to your subscribers; not configurable without paid plan |
| Mailchimp free plan removed automations in Feb 2026 | Informational | Confirms Kit is the right choice; no action needed |
| Kit free plan has no email support | Low | Community forum only; resolution time for issues may be slow; document workarounds here |
| "Unlimited sequences" claim unverified | Medium | May be limited to 1 sequence on free plan (conflicting sources); test required |

### [TO BE EXECUTED] Actual Integration Surprises Encountered

Document any surprise not listed above:

| Surprise Encountered | Date/Time | Severity | Resolution or Workaround |
|---|---|---|---|
| [fill in] | [fill in] | [fill in] | [fill in] |

---

## Overall Test Result

### Success Criteria (from Exploration Queue Item 22)

| Criteria | Status |
|---|---|
| All 3 emails deliver to inbox within 5 min | [TO BE EXECUTED] |
| No spam folder placement | [TO BE EXECUTED] |
| Automation trigger works OR blocker identified and workaround confirmed | [TO BE EXECUTED] |
| Timestamps logged for all deliveries | [TO BE EXECUTED] |
| API access status documented | [TO BE EXECUTED — see KIT_ACCOUNT_SETUP_CHECKLIST.md Step 3] |

### Pre-Execution Assessment (Research-Based)

**Confidence that Kit delivers emails to inbox without spam**: 88% (based on EmailToolTester 88.2% deliverability benchmark; new accounts on Kit's shared IP typically land in inbox for low-volume sends to opted-in addresses).

**Confidence that the 3-email sequence sends without error**: 95% (Kit is a mature platform; basic sequence sending is reliable for all plan levels).

**Confidence that path-routing automation works as designed in PHASE_2_3_EXECUTION_ROADMAP.md**: 40% (conditional branching on the free plan is disputed by multiple sources; high probability that the workaround via Sequences is required).

**Confidence that API access is available on the free plan**: 50% (Kit's pricing page and help docs contradict each other directly; test required to determine actual state).

**Overall platform fitness for Phase 2**: High. The core functionality — subscriber capture, email delivery, tag application at subscribe — is solid and well-supported on the free plan. The automation limitation is manageable via the Sequences workaround. The API gap affects Phase 3+ integrations only. Kit remains the correct platform choice.

---

## If Test Fails: Escalation Path

### Failure Mode 1: Emails land in spam

**Immediate actions**:
1. Set up verified sending domain (Settings > Email Sending) — 24-48 hours DNS propagation
2. Test again after domain verification
3. If still in spam: Use Mail-Tester.com to identify specific spam triggers
4. If still in spam after fixes: This is a Platform B (Mailchimp) escalation. See PHASE_2_EMAIL_SERVICE_COMPARISON_MATRIX.md for setup comparison.

### Failure Mode 2: Automation branching not available on free plan

**Immediate actions**:
1. Implement the Sequences workaround (Test B above)
2. If Sequences are also limited on the free plan: Build a single universal welcome sequence (no path branching); use Email 2 (Day 3) as the path-selection email — subscriber self-selects path by clicking a link, which applies the correct tag
3. This delays path-specific content by 3 days but stays within free plan limits

### Failure Mode 3: API access requires paid plan

**No immediate action required**. API access is not needed for Phase 2 core email delivery. Defer to Creator plan upgrade trigger (300+ subscribers and need for second automation).

### Failure Mode 4: Kit limits Sequences to 1 on free plan

**Escalation**: This would block the Sequences workaround for path routing. Options:
1. Upgrade to Creator plan ($33/month) — unlocks unlimited sequences and automations
2. Use a single welcome sequence with a Day 0 path-selection email (subscriber clicks their path → tag applied via Kit link trigger → subsequent emails personalized manually or via broadcast segments)
3. Evaluate Mailchimp Standard ($20/month for 500 contacts) as an alternative that includes Customer Journeys automation

---

## Sources

- [Kit Email Deliverability Best Practices 2026 — Warmy.io](https://www.warmy.io/blog/convertkit-deliverability-not-working-improve-email-deliverability/)
- [ConvertKit Emails Going to Spam: How to Fix — InboxAlly](https://www.inboxally.com/blog/convertkit-emails-going-to-spam-and-how-to-fix-it/)
- [Kit Review 2026 — Emailtooltester](https://www.emailtooltester.com/en/reviews/convertkit/)
- [Kit ConvertKit Review 2026 — StartupOwl](https://startupowl.com/reviews/kit-convertkit)
- [ConvertKit Pricing 2026: Plans, Costs — JustPricing](https://justpricing.com/convertkit-pricing)
- [Kit Free Plan Review — Matt Giaro](https://mattgiaro.com/kit-free-plan-review/)
- [ConvertKit Review 2026 — Automation Atlas](https://automationatlas.io/tools/convertkit/)
- [ConvertKit Free Plan 2026: What's Included — Mailsoftly](https://mailsoftly.com/blog/kit-free-plan/)
- [Visual Automations Conditions — Kit Help Center](https://help.kit.com/en/articles/2502665-visual-automations-conditions)
- [Kit Pricing — kit.com/pricing](https://kit.com/pricing)
