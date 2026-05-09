---
title: Phase 1 Execution Contingency & Rapid Recovery Playbook
project: resistance-research
prepared: 2026-05-09
audience: thorn (user)
purpose: Comprehensive failure-mode playbook for Phase 1 distribution execution with pre-decided recovery procedures
---

# Phase 1 Contingency & Rapid Recovery Playbook

## Overview

This document outlines failure scenarios that can occur during Phase 1 execution (Gist publication, email delivery, institutional engagement) and provides pre-decided recovery procedures so launch-day surprises don't derail execution.

**Key principle**: Anticipate, detect, respond. No improvisation under time pressure.

---

## FAILURE MODE TAXONOMY

### Category 1: Email Delivery Failures
**Likelihood**: Medium (3-7% depending on contact database cleanliness)

#### 1.1 Domain Blocklisting

**Signal**: Batch of emails bouncing with "550 5.7.1 — Our system has detected an unusual volume of unsolicited mail originating from your IP"

**Root causes**:
- Substack/institutional email infrastructure flagged as spam source due to prior distribution
- ISP rate-limiting on simultaneous sends (>100 emails in 5-min window)
- Contact list contains many corporate addresses that auto-report spam

**Detection** (automated):
- Gmail: Reports via Substack delivery status within 1-2 hours
- Substack: "Bounce summary" dashboard shows % bounced
- Threshold: >5% bounce rate (vs. 0.5% normal) = trigger recovery

**Recovery Procedure**:

1. **Immediate (within 1 hour of detection)**:
   ```
   STOP all additional sends (if still in progress)
   Substack → Dashboard → Review bounce list
   Export bounced emails to CSV
   Separate genuine bounces from soft-bounces (ISP throttling)
   ```

2. **Diagnosis (next 30 min)**:
   - [ ] Are >80% bounces from same domain (e.g., all @law.edu)? → Domain-level blocklisting
   - [ ] Are >80% bounces same ISP (e.g., Microsoft 365)? → ISP rate-limiting
   - [ ] Are bounces scattered? → List quality issue (likely invalid addresses)

3. **Recovery Actions per Diagnosis**:

   **If Domain-Level Blocklist** (e.g., all .edu bouncing):
   - Wait 48 hours for ISP blocklist to expire
   - Resend to bounced addresses May 15 (3 days after initial Wave 1)
   - Use institutional email if available (law.edu domain) instead of Substack
   - Or: Request manual review from ISP (Substack → domain owner contact form)
   - Expected outcome: 60-70% redelivery success after 48-hour wait

   **If ISP Rate-Limiting** (Microsoft 365 throttling):
   - Slow down resend: Max 20 emails/hour instead of batch send
   - Resend over 3-day window (May 10-12) instead of 2-hour window
   - Use institutional email if available (reduces "unsolicited" flag)
   - Expected outcome: 85-90% redelivery success at slower rate

   **If List Quality Issue** (scattered bounces):
   - Compare bounce list against Wave 2 contact list (check for overlap pattern)
   - If >50% of Wave 1 bounced: possible list corruption (escalate to user for manual review)
   - If <10% bounced (normal): Proceed with Wave 2 as planned (single bad list is acceptable)

4. **Timeline**:
   - Immediate: STOP & Diagnose (30 min)
   - Resend window: May 13-15 (post-checkpoint)
   - Escalation: If >20% bounce rate, contact user for manual remediation guidance

5. **Success criteria**:
   - Resend achieves ≥60% redelivery
   - No further blocklisting (wait period respected)

---

#### 1.2 SMTP Credential Failure

**Signal**: All emails fail to send with "401 Unauthorized" or "Invalid credentials"

**Root cause**: 
- Substack/institutional SMTP credentials expired or revoked
- Environment variable missing or misconfigured
- Authentication token refreshed by provider (OAuth)

**Detection** (immediate):
- Substack dashboard shows 0 emails sent (vs. expected 30+)
- Gmail/institutional account shows no new emails in "Sent" folder
- Error logs show authentication failures

**Recovery Procedure**:

1. **Immediate (5 min)**:
   ```
   Verify Substack/institutional account login works manually
   Check environment variables (.env file): echo $SUBSTACK_API_KEY
   If empty: source ~/.env && verify again
   ```

2. **If credentials are valid but API fails**:
   - [ ] Substack: Sign in to dashboard, generate new API key
   - [ ] Institutional: Request new SMTP credentials from IT
   - [ ] Update environment variables
   - [ ] Test with single email send (to own address)
   - [ ] Wait 15 min for token propagation
   - [ ] Resend full Wave 1 batch

3. **If unable to restore credentials**:
   - [ ] Escalate to user: "Substack/institutional credentials unavailable"
   - [ ] Alternative: Use Gmail SMTP directly if user account available
   - [ ] Or: Manual email send (acceptable for Wave 1, but not scalable)

4. **Timeline**: 15-30 min to restore and verify

---

#### 1.3 Rate-Limiting by Institutional ISP

**Signal**: Emails rejected with "421 try again later" or "429 too many requests"

**Root cause**: Batch send of 100+ emails in 5-minute window triggers ISP anti-spam

**Detection** (real-time):
- Substack dashboard shows "Delivery delayed" status
- Emails arrive 1-3 hours later instead of immediate

**Recovery Procedure**:

1. **Immediate**: Do nothing (ISP will auto-retry within 24 hours)

2. **Monitor**: Check Substack dashboard every 2 hours
   - If >50% still delayed after 3 hours → escalate to Step 3
   - If <10% delayed after 2 hours → proceed (normal)

3. **If prolonged delay** (>6 hours, >50% pending):
   - [ ] Check ISP blocklisting status (Substack dashboard)
   - [ ] Resend remaining emails at slower rate (20/hour)
   - [ ] Or use different email service (Gmail, institutional if available)

4. **Success criteria**: 95%+ emails delivered within 24 hours

---

### Category 2: Low/No Response

**Likelihood**: Medium (10-40% depending on organization sector)

#### 2.1 Wave 1 Response Rate <5% (Expected: 10-15%)

**Signal**: After 48 hours, Substack shows <2 opens + <1 click per 10 recipients

**Root cause**:
- List quality (many invalid email addresses, retired staff)
- Subject line ineffective (email flagged as spam or ignored)
- Message content not compelling enough to trigger response
- Timing: Sent Friday afternoon (less likely to receive attention)

**Detection** (automatic at 24h, 48h checkpoints):
- Substack dashboard: % opened < 10%
- No replies in institutional email inbox

**Recovery Decision Tree**:

```
Is response rate <5%?
├─ YES: Subject = [Checklist item 2.1 recovery]
│       └─ Has Wave 2 already been sent?
│            ├─ NO → Escalate to user for approval
│            │       Before Wave 2, consider:
│            │       (A) Resend Wave 1 with revised subject (48 hrs later)
│            │       (B) Proceed with Wave 2 (might have higher response)
│            │       (C) Investigate list corruption (sample 5 contacts for validity)
│            └─ YES → Too late (Wave 2 already out)
│                     Proceed with Wave 3, monitor overall engagement
└─ NO: Proceed normally (response rate expected variance)
```

**If list quality suspected** (>30% email bounces):
- Sample 10 contacts: call/LinkedIn to verify employment + current role
- If >50% of sample invalid: Escalate to user, request alternative contact list
- If <20% invalid: Proceed (normal corporate turnover)

**If subject/messaging suspected** (low opens despite valid addresses):
- Resend Wave 1 with 3 alternative subjects (A/B test)
- Best performer: use for Wave 2
- Expected improvement: Opens typically increase 30-50% with optimized subject

**Timeline**: 48h detection → 24h decision window → Resend/proceed by May 12

---

#### 2.2 High Bounce Rate (>10%)

**Signal**: Substack shows "Bounced" count > 10% of recipients

**Root cause**:
- Contact database stale (list from 2024, staff turnover)
- Email addresses in list are generic (e.g., info@org, admin@org) instead of individual
- Multiple names per organization, some invalid

**Recovery**:
- **If 10-15% bounce**: Normal (corporate staff turnover). Proceed with Wave 2-3.
- **If 15-25% bounce**: Elevated. Before Wave 2, sample list (20-30 random contacts): call 5-10 to verify current contact info. If >50% unreachable, request list refresh from org partner.
- **If >25% bounce**: List corruption. Escalate to user: "Wave 1 list has 30%+ invalid addresses. Recommend stopping waves, investigating source list, and restarting with fresh contacts."

**Timeline**: 1-2 hours to sample and remediate before Wave 2

---

### Category 3: Institutional Response

**Likelihood**: Low (1-3% negative responses, 5-15% substantive engagement)

#### 3.1 Objection / Institutional Rejection

**Signal**: Reply with objection to framework, methodology challenges, or partisan framing

**Examples**:
- "We don't distribute unsolicited policy frameworks"
- "This appears to advocate for specific party positions"
- "We need internal legal review before endorsing"
- "Distribution through our email violates our governance policy"

**Detection** (continuous monitoring):
- Set up email rule: Route replies to separate folder
- Check folder daily during May 9-31 window

**Recovery Decision Tree**:

```
Is objection substantive vs. blanket rejection?
├─ BLANKET REJECTION (e.g., "We don't distribute external materials"):
│   └─ Response: "Thank you for the response. We respect your distribution policies.
│       If you'd like to review framework internally for your own use, we're happy to share link."
│       (Do not escalate, do not change messaging, move forward)
│
├─ METHODOLOGY CHALLENGE (e.g., "Your framing of voting rights is too broad"):
│   ├─ Is it a simple misunderstanding?
│   │  └─ YES → Reply with 2-3 sentence clarification, invite continued dialogue
│   │          Do not change framework
│   │
│   └─ Is it substantial (e.g., "Domain 1 misses Section 4 of VRA")?
│       └─ YES → Thank them, note gap for Phase 2 update, invite ongoing collaboration
│                Do not change framework for Phase 1
│
└─ PARTISAN FRAMING CLAIM (e.g., "This favors Democrats"):
    └─ Response: "We designed framework using [democratic principles], not party platform.
       The specific policies are implemented differently across state/federal levels.
       Examples: [cite 2-3 examples where both parties support similar mechanisms].
       Invite them to flag specific policy areas for Phase 2 detail."
       Do not change framework.
```

**Key principle**: No mid-campaign framework changes. Objections are logged for Phase 2 refinement, not Phase 1 emergency updates.

**Timeline**: Reply within 24 hours. Do not let email thread cascade into extended debate.

---

#### 3.2 Request for More Information / Deeper Engagement

**Signal**: Reply asking for: presentation availability, research methods, specific domain deep-dive, follow-up call, etc.

**Expected frequency**: 5-15% of contacted orgs

**Recovery**:
1. **Log the engagement** (highest-value outcome):
   - [ ] Add to "Phase 2 Adoption Candidates" tracking spreadsheet
   - [ ] Note specific interest area (e.g., "Voting Rights Domain", "Implementation roadmap")

2. **Respond within 24 hours**:
   - [ ] Provide brief bio/credentials
   - [ ] Point to relevant domain files (e.g., Domain 1 for voting rights interest)
   - [ ] Offer call/presentation if feasible
   - [ ] Set expectation: "Phase 1 distribution is foundational outreach; Phase 2 is deeper engagement"

3. **Escalate if presentation requested** (outside normal email scope):
   - [ ] User decision: offer call/presentation or defer
   - [ ] If offered: schedule within 2 weeks (by May 24)

**Timeline**: Reply within 24 hours. Deep engagement (calls/presentations) logged for Phase 2.

---

#### 3.3 Media/Press Inquiry

**Signal**: Reply from journalist / media organization requesting framework details, author background, or coverage coordination

**Frequency**: Low (1-3% of distribution)

**Recovery**:

```
Does request indicate:
├─ BACKGROUND RESEARCH (journalist reviewing for possible coverage)?
│   └─ Response: Provide summary + point to github/public Gist, offer phone call
│              Do NOT send unpublished materials, do NOT coordinate timing
│              Log as "Press Interest" for Phase 2 amplification
│
├─ ON-THE-RECORD COVERAGE REQUEST (wants quotes/interview)?
│   └─ Escalate to user: "Press coverage opportunity for [date]"
│       User decides: accept interview / defer / provide written statement
│
└─ COORDINATION REQUEST (offer to promote in exchange for joint messaging)?
    └─ Escalate to user: "Partnership request from [media org]"
       User decides: accept / decline / refer to Phase 2 formal partnerships
```

**Key principle**: Media gets public materials + offer of background conversation. No exclusive arrangements, no messaging coordination for Phase 1.

**Timeline**: Reply within 2 hours (press operates on tight deadlines). Escalation to user within 1 hour.

---

### Category 4: Technical Failures

**Likelihood**: Low (2-5%), but high-impact

#### 4.1 Gist Creation Error

**Signal**: GitHub Gist creation fails, or Gist created but content displays incorrectly (encoding issues, formatting broken)

**Root cause**:
- GitHub API timeout (rare but possible)
- File size exceeds GitHub limits (v. unlikely, but possible if all domains included)
- Character encoding issue (special characters in domain text)
- Network failure mid-upload

**Detection** (immediate):
- [ ] Verify Gist creation by visiting GitHub URL directly
- [ ] Check rendering (does text display, or are there character encoding artifacts?)
- [ ] Confirm all sections present (scroll to bottom)

**Recovery**:

1. **If Gist failed to create**:
   - [ ] Retry creation immediately
   - [ ] If fails again: Create as .md file in GitHub repo instead (takes 2 min, same result)
   - [ ] Update contact list template with repo URL instead of Gist URL

2. **If Gist created but content broken**:
   - [ ] Delete Gist (GitHub → Gist settings → Delete)
   - [ ] Recreate with character encoding check: convert .md file to UTF-8 (no BOM)
   - [ ] Retest rendering

3. **If already sent emails with broken Gist URL**:
   - [ ] Send follow-up email within 2 hours: "Previous Gist had rendering issue, updated version at [new URL]"
   - [ ] Expected outcome: 20-30% of recipients will click updated link

**Timeline**: 10-30 min to remediate

---

#### 4.2 Email Template Merge Failure

**Signal**: Emails sent with broken variables (e.g., "Dear {{first_name}}" instead of "Dear John")

**Root cause**:
- Email template merge logic failed
- Contact database field names don't match template variables
- Substack/institutional template not configured correctly

**Detection** (spot-check):
- Check Substack "Sent" folder: Sample 3 emails to verify merge worked
- Sample from different organizations (check if all botched or just some)

**Recovery**:

1. **If single org broken** (e.g., "Dear {{first_name}}" at University A):
   - [ ] Find root cause: Check contact list field name vs. template variable
   - [ ] Fix template variable or contact field
   - [ ] Resend to University A only with corrected template
   - [ ] Expected outcome: Clean resend, 24-hour delay

2. **If all recipients broken** (all emails say "Dear {{first_name}}"):
   - [ ] STOP immediately (further sends would all be broken)
   - [ ] Fix template merge logic
   - [ ] Resend Wave 1 with corrected template (acceptable, common in distribution)
   - [ ] Update Wave 2 template before sending

3. **Severity**: This is recoverable but looks unprofessional. Recover + move forward.

**Timeline**: 15-30 min to fix + resend

---

### Category 5: Coordination Failures

**Likelihood**: Low (1-3%), but high-reputational-impact

#### 5.1 Duplicate Sends

**Signal**: Organization reports receiving email twice in same day

**Root cause**:
- Contacts list has organization appearing twice (e.g., org_president@org.edu + org_director@org.edu under same org)
- User manually sent additional email after batch send
- Batch send reran due to error recovery

**Detection** (post-send):
- Organization replies: "We received this twice"
- Or user confirms duplicate

**Recovery**:

1. **Response to organization**: "Thank you for flagging. Our contact list included two individuals from your organization. We apologize for the redundancy. Please share framework with relevant colleagues as needed."

2. **Prevent further duplicates**:
   - [ ] Deduplicate contact list for Wave 2-3
   - [ ] Remove duplicate entries (keep primary contact)
   - [ ] Note: Not a major issue, acceptable at 0-5% duplication rate

**Timeline**: 10 min to acknowledge + fix for next wave

---

#### 5.2 Org A Forwards to Network, Creates Attribution Confusion

**Signal**: Organization forwards framework to 50-person network with their own branding/framing

**Expected frequency**: Positive outcome (1-5% of orgs)

**Recovery**:

1. **Do not intervene**: This is amplification, not a failure
2. **Log as Phase 2 candidate**: Org A showed capacity to amplify and endorse
3. **Track second-order engagement**: If 50-person network replies, log as institutional network reach, not org reach

**Timeline**: None (monitor + log)

---

### Category 6: Scaling / Demand Response

**Likelihood**: Medium (10-25% if Phase 1 performs well)

#### 6.1 Unexpectedly High Response Volume

**Signal**: >30% open rate, >10% reply rate, inbox flooded with substantive engagement

**What it means**: Framework resonated more strongly than expected. Excellent outcome.

**Recovery**:

1. **Delegate response**: If user unable to reply to 50+ emails, establish triage:
   - [ ] Response template for routine inquiries (prepared in advance)
   - [ ] Escalate substantive/partnership requests to user
   - [ ] Log all contacts for Phase 2 outreach

2. **Expect**: If this occurs, Phase 2 planning may accelerate (more demand for deeper engagement)

3. **Timeline**: Allocate 3-5 hours/week for May 30 if high-volume response occurs

---

#### 6.2 Request for Distribution to Additional Sectors

**Signal**: Organization replies: "We'd like to share this with our network in [healthcare / labor / academic] sector"

**What it means**: Phase 2 starts inside Phase 1 (excellent outcome)

**Recovery**:

1. **Log** as "Phase 2 Candidate Network"
2. **Respond**: "We're deeply grateful. Our Phase 2 expansion is designed to reach sector-specific communities. We'll prioritize [healthcare] in our next wave (targeted for June)."
3. **Escalate to user**: "Network amplification request for [sector]"

**Timeline**: Respond within 24 hours

---

### Category 7: Reputational / Political Response

**Likelihood**: Low (1-5%), but manageable if expected

#### 7.1 Framework Misrepresented in Media / Online

**Signal**: Article quotes framework but misrepresents findings, or partisan attack on framework methodology

**Example**: "Alleged Democratic proposal to defund law enforcement" (misquoting Section 9 on police reform)

**Recovery**:

1. **Do not engage** in real-time media correction (too slow, too visible)
2. **Log the misrepresentation**: Add to "Known Criticisms" tracking
3. **Escalate to user**: "Press misrepresentation flagged at [source]"
4. **For Phase 2**: Build FAQ addressing common misrepresentations (prevent cascade)

**Timeline**: Flag to user within 24 hours. No emergency response unless directed by user.

---

## DECISION THRESHOLDS & TRIGGERS

### Go / No-Go Checkpoints

| Checkpoint | Trigger | Threshold | Action |
|-----------|---------|-----------|--------|
| **Day 1 (Wave 1 complete)** | Bounce rate | >15% | Diagnose list quality |
| | Open rate | <5% | Optional: Resend Wave 1 with revised subject |
| | Send success | <90% | Stop, troubleshoot before Wave 2 |
| **Day 2 (Wave 1 engagement)** | Response rate | >3% | Proceed normally (good engagement) |
| | Response rate | <1% + low open rate | Optional: Pause Wave 2, investigate messaging |
| | Negative responses | >10% objections | Log for Phase 2, proceed (normal variance) |
| **Day 7 (Post-Wave 3)** | Total engagement | >5% overall response | Phase 1 success, proceed to Phase 2 planning |
| | Total engagement | 1-5% response | Phase 1 modest, analyze results before Phase 2 |
| | Total engagement | <1% response | Phase 1 underperformed, escalate for analysis |

### Escalation Procedures

**GREEN** (proceed):
- Send >90% successfully
- Open rate >5%
- Response rate >2%
- Bounce rate <15%
- No systemic technical failures

**YELLOW** (proceed with caution):
- Open rate 2-5% (possible messaging issue)
- Response rate 1-2% (possible list quality issue)
- Bounce rate 10-15% (monitor for pattern)
- Recovery action implemented (resend, list fix)

**RED** (pause and escalate):
- Send <90% (technical failure)
- Bounce rate >25% (list corruption)
- Response rate <1% + open rate <2% (fundamental messaging issue)
- Systemic technical failure preventing sends
- Unmanageable duplicate send cascade

---

## PRE-LAUNCH CHECKLIST

Before Phase 1 distribution begins, verify:

- [ ] Email templates tested with 3 test recipients (no merge errors)
- [ ] Gist created and rendering correctly (all sections present)
- [ ] Contact list deduplicated (zero duplicate organization entries)
- [ ] Substack/institutional credentials verified working
- [ ] Backup email method ready (if Substack fails, use Gmail)
- [ ] Response monitoring set up (email rule routing replies to folder)
- [ ] This playbook reviewed and pre-decisions made
- [ ] User contact information verified (for escalations)

---

## SUMMARY OF PRE-DECIDED RESPONSES

| Scenario | Pre-Decided Action | Timeline |
|----------|-------------------|----------|
| Domain blocklisting | Wait 48h, resend Wave 1 | Resend May 13 |
| ISP rate-limiting | Slow down resend (20/hour) | Resend May 13-15 |
| SMTP credential failure | Regenerate credentials, test, resend | 15-30 min |
| <5% response after 48h | Investigate, optional resend Wave 1 | Decision by May 12 |
| >10% bounce rate | Sample list, proceed if <20% invalid | 1-2 hours |
| Objection reply | No-change response, log for Phase 2 | Within 24 hours |
| Press inquiry | Offer call, escalate if on-record | Within 2 hours |
| Gist rendering fail | Recreate with UTF-8 fix | 15-30 min |
| Duplicate send | Acknowledge, deduplicate for Wave 2 | 10 min |
| High engagement | Triage + log Phase 2 candidates | Ongoing |

---

## EXECUTION READINESS

This playbook is complete. User can execute Phase 1 with confidence that common failure modes have pre-decided recovery paths. No improvisation needed.

**Next step**: User decision on Path A (execute Wave 1 now) vs Path B (defer to May 13).

---

*Prepared by: Autonomous Orchestrator Session 918*
*Status: PRODUCTION-READY*
*Last updated: 2026-05-09 07:45 UTC*
