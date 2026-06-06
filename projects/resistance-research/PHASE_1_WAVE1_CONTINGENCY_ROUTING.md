---
title: "Phase 1 Wave 1 — Contingency Routing and Failure Mode Handling"
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  Failure mode diagnosis and recovery procedures for Phase 1 Wave 1 distribution
  (June 10-13 sends). Activated from PHASE_1_WAVE1_DAY7_DECISION_TREE.md when
  Path C or FAILURE is reached, or when any single metric falls into a failure band
  independent of composite score.
checkpoint_date: "June 17, 2026"
companion_files:
  - PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md
  - PHASE_1_WAVE1_DAY7_DECISION_TREE.md
  - DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
---

# Phase 1 Wave 1 — Contingency Routing and Failure Mode Handling

**When to run this document**:
- Composite score falls in Path C (8-17) or FAILURE (0-7) per the Decision Tree
- OR any single metric triggers a failure band (see Section 0 below)
- OR if measurement itself is blocked (Gist inaccessible, emails bounced, data unavailable)

**Do not run this document for Path A or Path B routing.** Those paths are handled entirely in the Decision Tree.

---

## SECTION 0 — Single-Metric Failure Triggers

These fire independently of composite score. Check each metric at Day 7 even if composite score is MODERATE.

| Metric | Failure Threshold | Trigger Description | Go to Section |
|--------|-----------------|---------------------|---------------|
| Email open rate | <10% | Unusually low — suspect delivery issue or subject line failure across entire batch | Section 1 |
| Gist clicks | 0 (confirmed delivery) | Emails delivered but no Gist link clicked at all | Section 2 |
| Reply rate | >30% open + 0 clicks + 0 replies | Opens confirmed but no click-through or reply | Section 3 |
| Bounce rate | >10% | More than 1 in 10 addresses invalid | Section 4 |
| Measurement unavailable | Cannot access Campaign Monitor, Bitly, or Gmail | Data collection blocked | Section 7 |
| Delivery unconfirmed | No record of send in outgoing folder | Emails may not have been sent | Section 8 |

---

## SECTION 1 — Email Open Rate <10%: Delivery or Subject Line Failure

### When this fires:
Open rate confirmed below 10% across all constituencies combined. This is significantly below the 20-40% MODERATE band and suggests a systemic issue, not audience mismatch.

### Diagnosis tree:

```
STEP 1: Is the low open rate across all constituencies, or just some?

  All constituencies <10%:
    -->  SYSTEMIC issue (sender, subject line, or timing)
    -->  Continue to Step 2

  Only 1-2 constituencies <10%, others 20%+:
    -->  CONSTITUENCY-SPECIFIC issue
    -->  Go to Section 5 (constituency-specific weakness)

STEP 2: Check for spam flagging

  Send a test email from the same account to yourself.
    Arrives in inbox within 5 min?
    YES  -->  Sender account is clean. Subject line is the probable cause.
              Go to Step 3.
    Goes to spam / delayed >15 min?
    YES  -->  Sender reputation issue. Go to Section 4A (sender reputation).

STEP 3: Audit subject lines used in June 10-13 sends

  Pull subject lines from DISTRIBUTION_EXECUTION_LOG.md for all June 10-13 sends.
  Check each subject line against this blocklist:
    BLOCKLIST: "reform", "democratic framework", "feedback request" (as noun phrases in isolation),
    "survey", "action needed", "urgent", "respond by", capital letters in subject,
    exclamation marks, bracketed phrases at start [like this], multiple colons
  
  Any matches?
    YES  -->  Subject line was likely spam-filtered on .edu or nonprofit servers.
              Execute Subject Line Revision (Section 1A below).
    NO   -->  Subject lines appear clean. Other cause suspected.
              Check timing (Step 4) and sender domain (Step 5).

STEP 4: Check timing of sends

  Were sends executed during:
    a) Late Friday afternoon (after 14:00 UTC Friday)
    b) Monday before 12:00 UTC (buried in morning inbox)
    c) Holiday period (Memorial Day, July 4 window, academic calendar break)
    d) A major news event that dominated all inbox attention
  
  YES  -->  Timing was likely the primary friction. 
            Execute re-send with timing correction (Section 1B).
  NO   -->  Timing appears clean. Continue to Step 5.

STEP 5: Check sender domain reputation

  Run a quick search: "[your sender domain] spam OR blacklist"
  Check if sender domain appears in: mxtoolbox.com/blacklists
  
  Blacklisted?
    YES  -->  Sender domain has email reputation issue. Section 4A (sender reputation).
    NO   -->  Sender domain is clean.
              If Steps 1-5 all clear with no cause found, proceed to Section 6 (no cause found).
```

---

### Section 1A — Subject Line Revision Protocol

**When to activate**: Subject line audit identified probable spam-trigger words OR open rate <10% with clean sender and clean timing.

**What to do**:

1. Draft 3 alternative subject lines for each constituency. Use these as templates:
   - Law Schools: "Research on [specific topic] — for [Clinic name or course area]"
   - Immigration/Civil Rights: "[Case or campaign name] — related research for your work"
   - Academic: "[Author/topic] findings relevant to your [current research / Spring syllabus]"
   - Faith/Labor/Mutual Aid: "Resource for [specific campaign or organizing context]"
   - Campaign Finance: "[Specific legislation or case] — research that may be useful for [their work]"

2. Send the revised subject line to 2-3 test contacts (contacts not yet reached in June 10-13 window — use Tier 2 contacts or secondary email addresses from contact list).

3. Monitor for 48 hours. If test opens occur, the subject line revision is confirmed effective.

4. Execute re-send to non-opening Wave 1 contacts with revised subject line. Wait 7 days from original send before re-sending to same addresses (7-day minimum to avoid spam-flag stacking).

5. Log in DISTRIBUTION_EXECUTION_LOG.md: "Subject line revision executed [date] — original vs. revised subject lines documented here."

**Do not re-send to the same contacts with the same subject line.** A second identical email accelerates spam flagging.

---

### Section 1B — Timing Correction Protocol

**When to activate**: Original sends fell in a low-engagement timing window.

**Optimal re-send windows** (for institutional / policy / academic contacts):
- Tuesday, Wednesday, Thursday between 09:00-11:00 local recipient time
- Avoid: Monday before 10:00, Friday after 14:00, holiday-adjacent weeks
- For .edu contacts: avoid end-of-semester exam periods (late April/May, mid-December), beginning of fall semester (first two weeks September)
- For nonprofit contacts: avoid end-of-fiscal-year weeks (June 25-30, December 26-31)

**Re-send procedure**: Use revised subject line (Section 1A) when timing-correcting. Do not re-send with original subject even if timing was the primary cause — the combination of new timing + new subject maximizes open rate recovery.

---

## SECTION 2 — 30% Opens + 0 Gist Clicks: Gist URL Broken or Untrustworthy Appearance

### When this fires:
Email open rate is acceptable (20%+) but Gist click count is zero despite confirmed opens. Emails are being read but the Gist link is not being clicked.

### Diagnosis tree:

```
STEP 1: Verify each Gist URL is accessible

  Open each Gist URL from PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md Section 2
  in a fresh incognito window.
  
  Any URL returns 404 or 403?
    YES  -->  Gist is inaccessible. Section 2A (Gist inaccessible).
    NO   -->  All Gists load. Continue to Step 2.

STEP 2: Check whether Gist link appears in email body

  Pull the sent emails from DISTRIBUTION_EXECUTION_LOG.md.
  Open each sent email copy.
  Is the Gist URL present in the email body as a clickable hyperlink?
  
    NO (raw URL pasted, not hyperlinked)  -->  May not display as clickable on some clients.
                                               Section 2B (link formatting).
    NO (URL omitted entirely)             -->  Gist link was never included.
                                               Re-send with corrected email body.
    YES (hyperlinked, confirmed clickable) -->  Continue to Step 3.

STEP 3: Assess whether Gist URL appears trustworthy

  gist.github.com URLs can trigger two concerns in recipients:
  a) "Why is this on GitHub instead of a website or PDF?" — institutional credibility signal
  b) Unfamiliarity with Gist as a format — recipient may not click an unknown URL type

  Check the email body: does it include an explanation of what Gist is,
  OR a reassurance about the link format?
    NO  -->  Execute trust-framing addition (Section 2C).
    YES -->  Trust framing is present; click barrier may be content-level friction.
             Section 5 (content mismatch diagnosis).

STEP 4: Check whether Bitly short links are live

  Click each Bitly short link manually. Does it resolve to the correct Gist?
  
    NO  -->  Bitly link is broken (expired or misconfigured). Section 2A.
    YES -->  Bitly links are live. Open rate + no click suggests content friction.
             Section 5.
```

---

### Section 2A — Gist Inaccessible: Recovery Procedure

**When to activate**: Any Gist URL returns 404, 403, or fails to load.

**Recovery steps** (10-15 minutes per Gist):

1. Check GitHub account status: log in to github.com/esca8peArtist and verify account is active and not suspended.
2. Navigate to https://gist.github.com/esca8peArtist — are any Gists visible?
   - If no Gists visible: account issue. Contact GitHub support or use backup account.
   - If other Gists visible but specific Gist missing: Gist was deleted or visibility changed.
3. Recreate the Gist from the source document using `gh gist create` CLI:
   ```bash
   gh gist create /path/to/domain-file.md --public --desc "Title here"
   ```
4. Record the new Gist URL in DISTRIBUTION_GIST_URLS.md (update the canonical record).
5. Send a brief correction email to all Wave 1 contacts who clicked the old link (Bitly data shows who clicked): "I'm sending a corrected link — the previous URL was inaccessible. Here is the updated resource: [new URL]"
6. Do not send the correction to contacts who did not click — they may not have noticed the broken link.

---

### Section 2B — Link Formatting Issue

**When to activate**: Gist link present in email but not formatted as hyperlink, or displays as raw URL.

**Fix procedure**:

1. In the re-send email, format the URL as an anchor tag:
   ```html
   <a href="https://gist.github.com/esca8peArtist/[ID]">Research: [Title]</a>
   ```
2. If using plain text email: include the full URL on its own line with the text "Link: " before it. Plain text emails should not use bare inline URLs without labeling.
3. Test: send the corrected email to yourself and confirm the link is clickable in both Gmail and Outlook views.

---

### Section 2C — Trust Framing for Gist URLs

**When to activate**: Email body does not explain the Gist format; institutional recipients may be hesitant to click unknown links.

**Add this sentence before the Gist URL in any re-send or follow-up**:
> "The research is hosted as a public document on GitHub Gist — a standard academic sharing format used by law schools and policy organizations. It requires no login and has no tracking."

For more conservative audiences (faith organizations, labor union staff not in policy roles), add:
> "I can also send you a PDF copy by reply email if you prefer."

This reduces click friction without changing the primary channel.

---

## SECTION 3 — Opens + Clicks but 0 Replies: CTA Clarity or Domain Quality Issue

### When this fires:
Open rate and Gist click rate are both acceptable, but zero substantive replies received at Day 7.

### Diagnosis tree:

```
STEP 1: Check reply wait time — is 0 replies at Day 7 actually expected?

  Review constituency timing norms:
    Law Schools: 5-14 day reply cycle (faculty email is not their primary inbox)
    National Nonprofits (CLC, Issue One, Brennan Center): 3-7 day cycle
    State-Level Nonprofits (Common Cause CA, LWV CA): 2-5 day cycle
    Faith Organizations: 7-21 day cycle (governance processes)
    Labor Unions: 5-14 day cycle (depends on cycle in collective bargaining calendar)
    Mutual Aid (local): 1-5 day cycle (more informal; faster but also more variable)
    Academic (policy school): 7-21 day cycle

  Were ALL Wave 1 sends to constituencies with >7-day norms?
    YES  -->  0 replies at Day 7 is EXPECTED, not a failure signal.
              Continue monitoring. Run Day 14 checkpoint June 24.
    NO   -->  Some contacts (e.g., state nonprofits, local mutual aid) should have replied
              within 7 days if engaged. Continue to Step 2.

STEP 2: Review the Call to Action in each email

  Pull each sent email from DISTRIBUTION_EXECUTION_LOG.md.
  Find the closing paragraph / CTA.
  
  Does the CTA ask for a specific action?
    Examples of clear CTA: "Would you be willing to share this with your team?"
                            "I would welcome a 15-minute call if this connects to your current work."
                            "Is there a specific section I can expand for your context?"
    Examples of weak CTA: "Let me know your thoughts."
                           "I'd love to hear any feedback."
                           "Please review when you have a moment."
  
  Weak CTA found?
    YES  -->  CTA friction likely. Execute CTA revision for Day 14 follow-up (Section 3A).
    NO   -->  CTA is clear. Continue to Step 3.

STEP 3: Assess domain quality as perceived by audience

  The recipient opened and clicked — they are interested. But they did not reply.
  Common reasons for read-without-reply in policy/academic contexts:
    a) Content is dense — they want to read more before engaging
    b) Colleague with more specific expertise would be a better fit — they're considering a forward
    c) Organizational policy restricts email replies to unsolicited external research
    d) The domain topic connects but the framing doesn't match their current work context
  
  Evidence of (a) or (b): likely to resolve organically by Day 14-21.
  Evidence of (c): check org's public engagement policy (some foundations and national nonprofits
                   require that incoming research be submitted through a formal intake process).
  Evidence of (d): constituency routing mismatch. Section 5.
  
  If no evidence of any (a-d): wait for Day 14. Opens + clicks is a strong leading indicator
  of eventual reply — the Day 7 window is simply early for policy-focused recipients.
```

---

### Section 3A — CTA Revision for Follow-up Emails

**Day 14 follow-up CTA template** (use for any non-replying contact who opened and clicked):

```
Subject: [Original subject] — quick follow-up

Hi [First name],

I wanted to follow up briefly on the research I shared [June 10/11/12/13]. 
I noticed you had a chance to review it [if you know they clicked — omit if unsure].

[1 sentence connecting their specific recent work to a section in the research]

Would it be useful if I sent you a shorter summary of the [specific section most relevant to their work]? 
Or if there's a colleague who'd be a better fit for this material, I'm happy to reach out directly.

[Your name]
```

**Key principles**:
- One specific question, not an open-ended "let me know your thoughts"
- Offer to reduce the burden (shorter summary, direct colleague referral)
- Do not repeat the full Gist URL — they already have it
- 3 paragraphs maximum

---

## SECTION 4 — Bounce Rate >10%: Contact Address Failure

### When this fires:
More than 1 in 10 emails sent in June 10-13 returned a delivery failure notification.

### Diagnosis and recovery:

```
STEP 1: Identify bounced addresses

  Search inbox for: subject:("Mail delivery failed" OR "Undeliverable" OR "failure notice")
  after:2026/06/09 before:2026/06/18
  
  List all bounced addresses: ___________________________

STEP 2: Categorize bounce type

  Hard bounce (permanent failure — "address does not exist"):
    -->  Address is stale. Must find corrected address before any re-send.
    -->  Corrected address sources: org website staff page, LinkedIn, org contact form

  Soft bounce (temporary failure — "mailbox full" or "server temporarily unavailable"):
    -->  Retry the same address after 48-72 hours.
    -->  If second attempt also soft-bounces, treat as hard bounce.

STEP 3: Find corrected addresses

  Priority sources for address correction:
    a) Org website staff directory (fastest, most reliable)
    b) LinkedIn — use the "Contact info" section on their profile
    c) Email pattern inference: if org has [first].[last]@org.org pattern confirmed
       from other contacts, apply the pattern
    d) Org contact form — submit via website and note submission in DISTRIBUTION_EXECUTION_LOG.md
    e) Direct phone call (last resort — only if email is the only channel and deadline is imminent)

STEP 4: Re-send to corrected addresses

  Wait at least 24 hours between the bounce detection and the re-send.
  Use a revised subject line (see Section 1A) for all re-sends to bounced addresses.
  Send one contact at a time, not in a batch — allows bounce detection per address.
  
  Log all re-sends in DISTRIBUTION_EXECUTION_LOG.md:
  "[Date] Re-send to [Org] at [corrected address] — original [bounced address] was stale"

STEP 5: Restart Day 7 clock

  After re-sends to corrected addresses, restart the Day 7 clock from the corrected send date.
  The June 17 checkpoint metrics only count for contacts who received the email.
  For bounced contacts: their Day 7 checkpoint is 7 days after the corrected re-send date.
  Log the new Day 7 date for each re-sent contact.
```

---

### Section 4A — Sender Reputation Issue

**When to activate**: Self-test email from sender account goes to spam OR sender domain appears on a blacklist.

**Recovery steps**:

1. Do not send any more emails from the flagged account for 48-72 hours.
2. Check if the sending account has been sending too many emails in a short window (>50 in 24 hours can trigger spam filtering on free email accounts).
3. Options for short-term recovery:
   - Use a secondary email account for Phase 1 Wave 1 re-sends (create one with the same name format for consistency)
   - Request removal from spam blacklists: mxtoolbox.com/blacklists has removal links for major lists
   - Switch to distribution via a dedicated email service (Mailchimp, Campaign Monitor) for remaining sends
4. Before resuming sends from any account, run the self-test protocol (send to yourself, confirm inbox delivery) to verify the account is clean.

---

## SECTION 5 — Constituency-Specific Weakness: Differential Engagement Analysis

### When this fires:
Strong engagement on some constituencies (Domains 39/56 contacts, e.g., civil rights and immigration) but weak on others (Domains 58/59 contacts, e.g., law schools, faith, or labor). This is a routing signal, not a failure — it tells you which Phase 2 domains to prioritize.

### Diagnosis matrix:

| Pattern | Likely Interpretation | Phase 2 Routing Implication |
|---|---|---|
| Law schools strong, faith/labor weak | Research framing is academic; not yet translated for organizing contexts | Prioritize Phase 2 domains with law school primary audience (Domain 58: Tribal Sovereignty) before faith/labor domains |
| Immigration/civil rights strong, academic weak | Operational urgency (active litigation) drives engagement; academic cycle timing issue | Proceed with Phase 2 civil rights distribution immediately; hold academic sends until fall semester |
| Labor strong, civil rights weak | Labor union training cycles are active; civil rights orgs have competing priorities | Accelerate Domain 59 (Economic Precarity) for labor context; hold broader civil rights framing for July-August window |
| Mutual aid strong, national nonprofits weak | Local coordinators are most engaged; national staff are resource-constrained | Route Phase 2 distribution through local chapters, not national HQs |
| Campaign finance strong, all others weak | Domain 51 audience is highly specific; general proposal framing not resonating with other constituencies | Do not expand constituencies at this stage; deepen Domain 51 engagement before broadening |
| Faith strong, all others weak | Faith networks have mobilization infrastructure; used for door-to-door, community meetings | Route through faith-to-labor bridge contacts (Interfaith Worker Justice) for cross-constituency amplification |

---

### Section 5A — Subject Line and Framing Revision by Constituency

If a specific constituency shows <20% open rate while others are at 30%+, the subject line or framing is the likely cause. Use these revised openers:

**Law Schools** (academic — signal domain expertise, not reform):
- Original framing tendency: "Democratic reform proposal — feedback request"
- Revised: "Research on [specific constitutional mechanism / case / doctrine] — for your [Clinic/Seminar]"

**Immigration / Civil Rights** (urgency — connect to active litigation or campaign):
- Revised: "[Case or campaign name] — research supporting your current work"

**Academic (Policy Schools)** (specificity — connect to their published work):
- Revised: "On [their research topic] — findings that may be relevant to [specific paper or project]"

**Faith Organizations** (moral framing — connect to social justice mission):
- Revised: "Resource for [congregation's / coalition's current campaign or justice focus]"

**Labor Unions** (operational — connect to specific bargaining or legislative cycle):
- Revised: "Research on [specific labor policy] — for your [bargaining cycle / training / legislative campaign]"

**Mutual Aid** (immediacy — make the resource usable today):
- Revised: "Resource for [specific local issue] — immediate use case for [neighborhood / network name]"

---

## SECTION 6 — No Root Cause Found: Escalation to User

### When to activate:
All checks in Sections 1-5 are clean (delivery confirmed, Gist accessible, sender clean, CTA clear, timing correct) and open rate and reply rate remain zero at Day 7.

### What to do:

This is the rarest scenario. Before escalating, run one final check: contact list quality assessment.

**Contact list quality assessment** (10 minutes):
1. Pick 3 contacts at random from the June 10-13 send list.
2. Google each person's name + organization.
3. For each: are they still at that organization? Did they recently change roles?
4. For each: do they appear to be active in the policy/academic space (recent publications, social media, event appearances)?

If 2 of 3 contacts show signs of role changes or reduced activity, the contact list may be systematically outdated despite prior verification. This is a list quality issue, not a content issue.

**If contact list quality confirmed as the issue**: Execute stakeholder substitution (Section 6A).

**If contact list quality is fine**: Escalate to user via CHECKIN.md with the full diagnostic findings. Use the FAILURE PATH template in PHASE_1_WAVE1_DAY7_DECISION_TREE.md, Part 2, Failure Path.

---

### Section 6A — Stakeholder Substitution

**When to activate**: Contact list is outdated OR primary tier contacts are unreachable.

**Substitution principle**: Replace national directors with state-level counterparts or operational staff. National directors have high signal value but low response rate. State-level affiliates have more capacity for external engagement and more specific use cases for the research.

**Substitution map by constituency**:

| Original contact type | Substitution target | Where to find them |
|---|---|---|
| National nonprofit executive director | State chapter director or program manager | Org website, state affiliates page |
| Law school professor (big name) | Clinical faculty, adjunct, or visiting professor | Law school clinic directory |
| National union leadership | State AFL-CIO director or local chapter president | AFL-CIO state council websites |
| National faith coalition | Regional or local faith justice organizer | Faith in Action local chapter list |
| National civil rights org | Local chapter or legal aid society in your state | State ACLU chapter, state civil rights coalition |

**Re-send procedure**: Use a simplified 2-paragraph pitch (not the full framework overview). Lead with the one finding most operationally relevant to the specific contact's work. Do not reference the full 40-domain scope — use the specific domain most relevant to their work.

---

## SECTION 7 — Measurement Unavailable: Data Collection Blocked

### When this fires:
One or more data sources (Campaign Monitor, Bitly, Gmail) are inaccessible and engagement metrics cannot be collected for the June 17 checkpoint.

### Fallback measurement hierarchy:

| Primary source unavailable | Fallback | Fallback reliability |
|---|---|---|
| Campaign Monitor (open rate) | Bitly clicks as open proxy (click ≈ confirmed delivery + interest) | 70-80% correlation |
| Bitly (click tracking) | GitHub Gist view count (authenticated GitHub session) | 80-90% correlation |
| GitHub Gist analytics | Gmail reply count only (no click data) | Low confidence; only confirms reply rate |
| Gmail access blocked | Manual count from sent folder reply threads | Moderate — miss any replies not in sent thread |

**If ALL data sources are blocked** (most severe case):
- Do not delay the checkpoint — record "DATA UNAVAILABLE" in the CHECKIN.md checkpoint template
- Proceed to Phase 2 routing on best available signal from manual inbox review
- Flag in CHECKIN.md under "Needs Your Input": "Day 7 checkpoint data collection blocked — [which tools unavailable]. Manual inbox review found [X] replies. Requesting user verification of open rate and Gist analytics."

---

## SECTION 8 — Delivery Not Confirmed: Emails May Not Have Been Sent

### When this fires:
No record in outgoing mail folder for June 10-13 sends, OR sends were marked as drafts and not actually sent.

### Verification steps:

1. Open Gmail sent folder. Search: `sent:2026/06/09..2026/06/14 to:(campaignlegal.org OR issueone.org OR commoncause.org OR lwvc.org OR cleanmoney.org)`
2. Are sent emails visible with timestamps?
   - YES: Sends confirmed. Return to Section 1 (delivery/open rate diagnosis).
   - NO: Sends not confirmed.
3. Check Drafts folder for any unsent emails.
4. If emails are in Drafts and were never sent: execute sends now. The Day 7 window starts from the actual send date, not June 10.
5. Log all actual send timestamps in DISTRIBUTION_EXECUTION_LOG.md.
6. Set a new Day 7 checkpoint date: 7 days after the actual send date.
7. Update CHECKIN.md: "Phase 1 Wave 1 sends confirmed delayed — actual send date [DATE]. New Day 7 checkpoint: [DATE + 7]."

---

## SECTION 9 — Recovery Procedures by Root Cause (Quick Reference)

| Root Cause | Recovery Action | Time Required | Files to Update |
|---|---|---|---|
| Subject line spam-filtered | Revise subject + re-send to 2 test contacts + wait 48h for test results | 30 min + 48h wait | DISTRIBUTION_EXECUTION_LOG.md |
| Gist URL broken | Recreate Gist via `gh gist create`, update DISTRIBUTION_GIST_URLS.md, send correction email | 15-30 min | DISTRIBUTION_GIST_URLS.md + CHECKIN.md |
| Gist link missing from email | Re-send with corrected email body | 20-30 min | DISTRIBUTION_EXECUTION_LOG.md |
| No CTA in email | Re-send follow-up with specific question (Section 3A template) | 15 min | DISTRIBUTION_EXECUTION_LOG.md |
| Bounce rate >10% | Find corrected addresses, re-send, restart Day 7 clock | 45-90 min | DISTRIBUTION_EXECUTION_LOG.md + contact list |
| Sender spam reputation | Switch to secondary account or email service | 30 min setup + 48h reputation recovery | DISTRIBUTION_EXECUTION_LOG.md |
| Constituency-specific framing mismatch | Revise subject + opening paragraph per Section 5A templates | 20-30 min per constituency | DISTRIBUTION_EXECUTION_LOG.md |
| Contact list outdated | Stakeholder substitution per Section 6A | 60-90 min | DISTRIBUTION_OUTREACH_CONTACTS.md |
| All systems clean, no engagement | Escalate to user via CHECKIN.md | 15 min | CHECKIN.md |
| Emails never sent | Send now; restart Day 7 clock | 60-90 min for full batch | DISTRIBUTION_EXECUTION_LOG.md + CHECKIN.md |

---

## SECTION 10 — Domain-Strength-Based Phase 2 Routing

**Activate when**: Aggregate signal is MODERATE or WEAK but there is differential strength across domains in the same wave.

If Domains 39/56 (civil service, healthcare infrastructure — earlier waves) showed strong engagement but Domains 58/59 (Tribal Sovereignty, Economic Precarity) are generating weak signal in this wave:

```
Strong 39/56 + Weak 58/59:
  -->  Route Phase 2 research investment toward Domain 58 (higher constitutional resonance
       with law school audiences who responded to 39/56)
  -->  Hold Domain 59 expansion until Domain 58 generates engagement signal
  -->  Rationale: Domain 58 (Tribal Sovereignty) is the bridge domain — it connects the
       institutional/constitutional framing that 39/56 audiences respond to with the
       economic justice framing of Domain 59

Strong 58/59 + Weak 39/56:
  -->  Expand Domain 59 (Economic Precarity) immediately — labor/mutual aid audiences
       are already engaged
  -->  Use Domain 59 engagement as the "economic justice bridge" to re-approach 39/56
       audiences with a different framing angle

All weak equally:
  -->  Do not differentiate by domain — the issue is systemic (delivery, framing, timing)
  -->  Run root-cause diagnosis in Sections 1-5 before any domain-specific routing
```

---

## SECTION 11 — Escalation to User: Templates

### Template A — Single-metric failure requiring user input

```
## Phase 1 Wave 1 — [Metric] Failure Signal [June 17, 2026]

[Single-metric failure type: email open rate <10% / Gist 0 clicks / bounce rate >10%]

What happened: [1 sentence description]
Root cause diagnosis: [what was checked and what was found]
Recovery action taken: [what has already been done without user input]
What requires user decision: [the specific decision needed]

Options:
A) [Option A with time estimate]
B) [Option B with time estimate]

Recommendation: [which option and why in 2 sentences]

User decision requested by: [date/time, 48h from now]
If no response by [date/time]: default action = [Option X]
```

### Template B — Composite failure requiring full Phase 2 hold

```
## Phase 1 Wave 1 FAILURE — Full Diagnostic Summary [June 17, 2026]

Composite score: ___/40 (FAILURE threshold)
Path: FAILURE (per PHASE_1_WAVE1_DAY7_DECISION_TREE.md)

Diagnostic findings:
- Delivery confirmed: Y / N
- Gist URLs live: Y / N
- Bounce rate: ___/total = ___%
- Subject line audit: [CLEAN / ISSUE FOUND: description]
- Sender reputation: [CLEAN / FLAGGED]
- Root cause identified: [YES: description / NO: all checks clean]

Phase 2 hold: Domain 51 HOLD / Domain 59 HOLD / Domain 54 research continues

User options:
A) Stakeholder substitution + framing revision — resend to state-level secondary contacts
B) Channel shift — submit to Lawfare/Just Security/policy journals
C) Hold until Day 30 (July 10) — let any delayed organic engagement arrive
D) Cancel this distribution track; reallocate to Phase 3 preparation

Recommendation: [option] because [2-sentence rationale]

User decision required by: [June 19, 48 hours from now]
If no response: default to Option C (hold)
```

---

*Prepared June 6, 2026. Companion to PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md and PHASE_1_WAVE1_DAY7_DECISION_TREE.md.*

*Sources for timing norms: [PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md]; [DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md]; [phase-1-adoption-tracking-script.py — LeadingIndicatorDetector class]*
