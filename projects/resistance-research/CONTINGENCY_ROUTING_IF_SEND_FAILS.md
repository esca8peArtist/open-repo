---
title: "Domain 59 — Contingency Routing if Wave 2 Send Fails"
subtitle: "Immediate Recovery Playbook for Bounces, Rejections, & Non-Delivery"
created: "2026-06-25"
status: "PRODUCTION-READY"
execute_when: "Email bounces detected OR multiple rejections received within 48h of Wave 2 sends"
recovery_window: "48 hours from bounce detection"
---

# Domain 59 — Contingency Routing if Wave 2 Send Fails

**Immediate action guide if Wave 2 sends (EPI, Demos, NELP) bounce, are rejected, or produce a pattern of failures.**

Execute this playbook within **48 hours** of detecting bounce/failure. Delays beyond 48 hours close the recovery window for re-send viability during the OBBBA June 25–30 window.

---

## Trigger Conditions (When to Execute This Playbook)

Execute immediately if ANY of the following occur June 24–26:

| Trigger | Action | Timeline |
|---------|--------|----------|
| **Hard bounce** from any contact (e.g., "user unknown," "invalid recipient") | Verify address; resend within 48h | Start within 2h of bounce |
| **Multiple soft bounces** from same org (e.g., "mailbox full," "server temporarily unavailable") — 2+ in 24h | Wait 6h; resend once; if fails again, escalate to alt contact | Start within 6h of first bounce |
| **Rejection message** (e.g., "This email address cannot receive external mail" or "Contact form submission failed") | Switch to alternative contact or channel (phone, LinkedIn, contact form) | Start within 2h of rejection |
| **Pattern of failures**: All three Wave 2 sends bounce (EPI + Demos + NELP) | Systematic issue (e.g., email server problem, authentication failure); diagnose before blanket resend | Execute diagnosis within 4h |
| **Zero open rate 24h post-send** + Gist views <5 | Probable non-delivery; verify sender address; resend | Execute by 48h post-send |

---

## Step 1: Diagnosis (Within 2 Hours of Failure)

**What to check:**

### 1.1: Verify the Bounce

Check your email **sent folder** and **spam/bounce folder** for:
- Hard bounce message (from mail daemon, delivery failure notification)
- Soft bounce indicator (temporary unavailable, try again)
- Rejection message (policy rejection, format issue)

**Example bounce messages:**
- Hard: "550 5.1.2 The email account that you tried to reach does not exist"
- Soft: "421 4.7.0 [TSS08] Messages from X.X.X.X temporarily deferred"
- Rejection: "This email address is not set up to receive mail"

**Action per bounce type**:
- **Hard bounce**: Email address is invalid or account no longer exists. Proceed to 1.2.
- **Soft bounce**: Temporary issue (mail server down, mailbox full). Proceed to 1.3.
- **Rejection**: Email system block (policy, format, or security). Proceed to 1.4.

### 1.2: If Hard Bounce — Verify Contact Address from Org Website (5 min)

Go to the bounced organization's website and search for current contact info.

**EPI Address Verification**:
- URL: https://www.epi.org/about/contact/
- Original email: researchdept@epi.org
- **If researchdept@epi.org is NOT listed**: Search for "research director" or "policy research" contact
  - Look for named individuals on epi.org/about/staff
  - If found: get their direct email if listed, or use research@epi.org + subject line "For [Name], Research Department"
  - If no direct email: use epi.org contact form (see 1.4 if using form)
- **If researchdept@epi.org IS listed**: The bounce may be intermittent. Proceed to 1.3 (soft bounce recovery)

**Demos Address Verification**:
- URL: https://demos.org/contact
- Original email: info@demos.org
- **If info@demos.org is not working**: Search demos.org for named policy contact
  - Current president: Taifa Smith Butler (may have direct email policy)
  - Look for policy director contact
  - If found: use that email
  - If no email found: use demos.org contact form

**NELP Address Verification**:
- URL: https://nelp.org/about-us/contact/
- Original email: info@nelp.org
- **If info@nelp.org is not working**: Search for policy director contact
  - Current president: Rebecca Dixon
  - Look for worker classification or policy team contact
  - If found: use that email
  - If no email found: use nelp.org contact form

**After verification**:
- If you find NEW email address: Record it. Proceed to Step 2 (resend to new address).
- If address is CONFIRMED (address was correct; bounce is intermittent): Proceed to 1.3.
- If NO VALID EMAIL found: Proceed to 1.4 (use contact form).

### 1.3: If Soft Bounce — Retry Logic (Minimum 6h gap)

Soft bounces are usually temporary (mail server down, mailbox full).

**Action**:
1. **Wait 6 hours** from first bounce before retrying
2. **Resend the same email** to the same address (no changes needed)
3. **Log**: Note bounce type + resend time in send log
4. **Monitor**: If second send bounces again → escalate to hard bounce recovery (1.2)

**If soft bounce resolves after retry**: Continue normal monitoring (DOMAIN_59_TIER_2_RESPONSE_TRACKING_DASHBOARD.md). Resend counts as successful send.

### 1.4: If Rejection or Contact Form Required — Use Alternative Channel

If email address doesn't exist or org uses contact form only:

**For EPI contact form** (epi.org/about/contact/):
- Fill out contact form with:
  - **To**: "Research Team / Heidi Shierholz" (or select "research" category if form has drop-down)
  - **Subject**: "Democratic participation framing for EPI wage research — OBBBA implementation year" (same as email subject)
  - **Message**: Copy-paste the body from DOMAIN_59_TIER2_SEND_TEMPLATES.md Template A (no [YOUR_NAME]/[YOUR_EMAIL] placeholders this time — fill those in)
- **Log**: Add to send log: "EPI send via contact form, [date], [time]"
- Form submissions are less reliable than direct email. Call EPI research line (if available) at 202-775-8810 to confirm form was received.

**For Demos contact form** (demos.org/contact/):
- Fill out contact form with:
  - **To**: "Policy Team / Taifa Smith Butler" or select "research" option
  - **Subject**: "Democratic participation research for Demos — OBBBA implementation and economic justice" (same as email subject)
  - **Message**: Copy-paste Template B body from DOMAIN_59_TIER2_SEND_TEMPLATES.md
- **Log**: "Demos send via contact form, [date], [time]"

**For NELP contact form** (nelp.org/contact/):
- Fill out contact form with:
  - **To**: "Policy Team / Rebecca Dixon"
  - **Subject**: "Democratic participation framing for NELP's worker classification and wage work — OBBBA implementation" (same as email subject)
  - **Message**: Copy-paste Template C body from DOMAIN_59_TIER2_SEND_TEMPLATES.md
- **Log**: "NELP send via contact form, [date], [time]"

---

## Step 2: Resend to Verified Address (Within 48 Hours of Original Bounce)

If you've identified a corrected email address (from 1.2), resend immediately.

### 2.1: Resend Template

Use the **exact same email** you originally sent, but to the NEW verified address.

**Template (example for EPI, if sending to research@epi.org instead of researchdept@epi.org)**:

Subject line: [SAME AS ORIGINAL]

Body: [SAME AS ORIGINAL — no changes]

**Why no changes?** The content is solid. The problem was routing, not framing. Changing the email based on a single bounce will confuse decision-makers who receive multiple versions.

### 2.2: Log the Resend

In your send log, add:

| Contact | Original Email | Bounce Type | Verified New Email | Resend Date | Resend Time (UTC) | Status |
|---------|---|---|---|---|---|---|
| EPI | researchdept@epi.org | Hard bounce — invalid recipient | research@epi.org | June 25 | 14:30 | Resent |

### 2.3: Monitor for Delivery

After resend, monitor for:
- **24h confirmation**: Did it deliver (no bounce in 24h)?
- **48–72h check**: Did they open it? (If tracking is available)
- **72h+ check**: Any reply?

If resend also bounces → escalate to Step 3 (alternative contact or contingency analysis).

---

## Step 3: Alternative Contact Routing (If Resend Still Bounces)

If the verified address ALSO bounces, you have a systematic issue. Escalate to alternative contact.

### 3.1: Find Alternative Contact at Same Organization

Do NOT give up. Large organizations have multiple contact points.

**EPI alternative contacts** (if research@epi.org also bounces):
- **Look for**: "Policy Research" department on epi.org staff page
- **Search for** named researchers: Look at epi.org/people or media bylines for policy researchers
- **Alternative emails to try** (in order of likelihood):
  1. Direct email of named researcher (e.g., name@epi.org, if staff page lists it)
  2. policy@epi.org (if exists)
  3. communications@epi.org + subject "Please forward to: Research Director"
  4. EPI phone line: 202-775-8810 — call and ask "What's the correct email for research submissions?"
- **Last resort**: epi.org contact form (see 1.4)

**Demos alternative contacts** (if info@demos.org also bounces):
- **Look for**: Policy directors on demos.org/leadership
- **Alternative emails to try** (in order):
  1. Direct email of named policy director (e.g., name@demos.org)
  2. policy@demos.org (if exists)
  3. Demos phone: 212-633-6580 — ask "What's the policy research contact email?"
  4. demos.org contact form (see 1.4)

**NELP alternative contacts** (if info@nelp.org also bounces):
- **Look for**: Lawyer/researcher on nelp.org/about-us/staff or similar
- **Alternative emails to try** (in order):
  1. Direct email of named staff (e.g., name@nelp.org)
  2. policy@nelp.org (if exists)
  3. NELP phone: 202-602-5818 — ask for policy research contact
  4. nelp.org contact form (see 1.4)

### 3.2: Send Alternative Contact Email

Send to the alternative email (or call with message request).

**Optional framing for alternative contact email**:

---

Subject: Research on economic precarity and democratic participation — forwarding to [DEPARTMENT]

Dear [Org] team,

I recently sent research on economic precarity and civic participation to [ORIGINAL ADDRESS], but received a bounce-back notification. I'm reaching out to your policy/research team to ensure this reaches the appropriate contact.

[Same body as original email]

If this should reach a different contact within your organization, please let me know.

Thank you,
[Your name]

---

**Send to**: Alternative email address
**Log**: Add to send log: "[Org] — resend attempt #2 to [alternative email], [date]"

### 3.3: Phone Follow-Up (If Email Route Exhausted)

If you've tried 2–3 email addresses and all bounce, make a brief phone call.

**Phone script** (1-minute call):

---

"Hi, I'm [Your Name]. I sent a research document on economic precarity and democratic participation to [Org] [timeframe] ago. I received bounce-back notifications, so I want to make sure it reaches the right person. Do you know who on your policy/research team should receive this?"

*Listen for direction, then:*

"Great. Can you confirm their email address is [EMAIL]? I want to make sure I send it correctly this time."

*After confirmation:*

"Perfect. I'll send it to [contact] right now. Do you think they'll be interested in research on how economic policy affects voter participation?"

*If yes:* "Excellent. I'll follow up in a week to see if it reached them."
*If no:* "Understood. Do you know of anyone at [Org] who works on that intersection?"

---

**Call targets** (in order of likelihood to help):
1. Organization main line → ask for research/policy department receptionist
2. Research director's office (if available)
3. General operations line

**After call**: Get the confirmed correct email address. Send email immediately. Log call attempt.

---

## Step 4: If Pattern Emerges — Assess Recipient Type Issue

If ALL THREE Wave 2 sends (EPI + Demos + NELP) bounce with the same error pattern, it's not a routing issue — it's a sender problem.

### 4.1: Diagnose Sender Problem

Check:
1. **Are you sending from your correct email address?** (Confirm in sent folder)
2. **Is your email account being filtered as spam?** (Check if bounces mention "authentication" or "DKIM/SPF failed")
3. **Is your email domain flagged?** (If sending from a new domain/account, some orgs' filters may block it)

**Common causes**:
- You're sending from a Gmail account to an org with strict external email filters → emails get junked
- Your email has been flagged as spam by Gmail/Outlook (if sending from free account)
- Mass-send appearance (if you sent many emails in short time frame)

### 4.2: Recovery Options for Sender Problem

**Option A: Use Contact Forms** (see 1.4 above)
- Most reliable fallback
- Contact forms bypass email sender reputation filters
- Submit all three organizations via form if email route fails

**Option B: Forward Through Known Contact**
- If you have a relationship with someone at any of these orgs, ask them to forward your email internally
- Example: "I sent research on CTC and democratic participation to [Org]. Do you mind forwarding this internally to the research team? I've hit an email delivery issue."

**Option C: Resend from Institutional Email**
- If you have access to institutional email (university, nonprofit, etc.), resend from that address
- Institutional email has better deliverability than personal Gmail/Outlook
- Example: University email → higher trust score at recipient orgs
- Log: "Resend from institutional email [address], [date]"

**Option D: Post-Holiday Resend (July 7+)**
- If you can't resolve by June 30, wait for post-holiday resend (July 7–14 after Independence Day/July 4 recess)
- Resend to verified addresses during normal business week
- Update email routing strategy based on what you've learned in bounce diagnosis

---

## Step 5: If Send Fails But No Bounce — No-Reply Contingency

If email doesn't bounce (delivery appears successful) but produces zero open/click activity by 48h post-send:

### 5.1: Verify Delivery Without Bounce

**Indicators of non-delivery without bounce**:
- No bounce-back message received
- Email sent folder shows "delivered" status
- BUT: Gist view count <5 within 48h post-send
- AND: No reply by 48h (when open confirmation would be expected for active reader)

**Interpretation**: Email may have been delivered to spam folder, or recipient is not opening it.

### 5.2: No-Reply Recovery

**Option 1: Resend with Modified Subject Line**

---

Subject: [FOLLOW-UP] — Research on economic precarity and democratic participation

Dear [Contact],

I sent this research on [DATE] but haven't received confirmation of delivery. I'm sending it again to ensure it reaches your team.

[SAME BODY AS ORIGINAL]

Best,
[Your name]

---

**Send to**: Same address as original
**Timing**: 48–72h after original send (June 26–27 if June 24–25 original send)
**Purpose**: If email was caught in spam, modified subject + "[FOLLOW-UP]" tag may bypass filter on second send

**Option 2: Alternate Channel (Phone or Form)**

If resend also produces no activity:
- Call organization (see 3.3 above)
- Use contact form (see 1.4)
- Ask for direct email confirmation

---

## Contingency Decision Matrix (Quick Reference)

| Failure Type | Primary Action | Secondary Action | Fallback |
|---|---|---|---|
| **Hard bounce** | Verify address (1.2); resend to verified email (2.1) | If verified email also bounces: find alternative contact (3.1) | Phone follow-up (3.3) or contact form (1.4) |
| **Soft bounce** | Wait 6h; resend once (1.3) | If resend bounces: treat as hard bounce (1.2) | — |
| **Rejection message** | Use contact form (1.4) immediately | If form doesn't work: phone call (3.3) | — |
| **Pattern failure** (all three orgs bounce same way) | Diagnose sender problem (4.1) | Use contact forms for all three (1.4) | Institutional email resend (4.2 Option C) |
| **No reply + no bounce** | Resend with modified subject (5.2) | Alternate channel: phone or form | Post-holiday re-send (July 7+) |

---

## Resend Attempt Log (Fill In)

Keep this log during contingency execution:

| Org | Original Email | Sent Date | Bounce Detected | Bounce Type | Verified New Email/Contact | Resend 1 Sent | Resend 1 Status | Resend 2 Email/Channel | Resend 2 Sent | Final Status |
|---|---|---|---|---|---|---|---|---|---|---|
| EPI | researchdept@epi.org | June 24 | [ ] Yes [ ] No | — | research@epi.org | June 25 | [ ] Delivered [ ] Bounce | — | — | [ ] Success [ ] Failed |
| Demos | info@demos.org | June 24 | [ ] Yes [ ] No | — | — | — | — | — | — | [ ] Success [ ] Failed |
| NELP | info@nelp.org | June 25 | [ ] Yes [ ] No | — | — | — | — | — | — | [ ] Success [ ] Failed |

---

## When to Escalate Beyond This Playbook

If, after executing all steps above, you have:
- ✅ Sent to 2+ verified addresses per org
- ✅ Submitted 2+ contact forms
- ✅ Made phone follow-up call(s)
- ✅ Waited 48+ hours since last resend attempt

...and still have **zero confirmed deliveries** across all three orgs, **escalate to user decision**:

**Decision point**: "Should we pivot Tier 2 activation to alternative organizations (e.g., send to CBPP + MomsRising follow-up instead of pushing EPI/Demos/NELP further)?"

Contact user with:
- Count of resend attempts per org (3 attempts × 3 orgs = up to 9 attempts total if full contingency executed)
- Summary of findings (what worked, what didn't)
- Recommendation: "Suggest moving to Phase 2 follow-up with Wave 1 responders (CBPP + MomsRising) rather than further EPI/Demos/NELP escalation"

---

## Recovery Timeline Summary

| Hour | Action | Owner |
|---|---|---|
| 0 | Bounce detected in inbox | User (monitoring) |
| 0–2h | Diagnosis (1.1–1.4) | User |
| 2–6h | Address verification (1.2) | User |
| 6–24h | Resend to verified address (2.1) OR soft bounce wait (1.3) | User |
| 24–48h | Monitor for second bounce | User |
| 48–72h | If resend fails: alternative contact routing (3.1–3.2) or phone follow-up (3.3) | User |
| 72h+ | If still failing: decision point (escalate to user or pivot strategy) | User |

**Critical**: Do not exceed 48h from bounce detection without attempting resend. After 48h, the June 24–30 OBBBA window is too compressed to recover.

---

## Checklist: Did I Do This Right?

After executing contingency steps, verify:

- [ ] I identified the bounce/failure type (hard, soft, rejection, pattern)
- [ ] I verified at least one email address from the organization's website
- [ ] I sent at least one resend attempt to a verified/alternative address within 48h of bounce
- [ ] I logged all attempts in the resend log above
- [ ] If resend succeeded: I'm back on normal monitoring (DOMAIN_59_TIER_2_RESPONSE_TRACKING_DASHBOARD.md)
- [ ] If resend failed: I executed alternative routing (contact form, phone, or institutional email)
- [ ] If all alternatives failed: I escalated to user decision (pivot strategy or post-holiday re-attempt)

---

## Contact Reference (Copy for Quick Access)

### Websites for Address Verification

- **EPI**: https://www.epi.org/about/contact/
- **Demos**: https://demos.org/contact/
- **NELP**: https://nelp.org/about-us/contact/

### Phone Numbers (If Email Route Fails)

- **EPI**: 202-775-8810
- **Demos**: 212-633-6580
- **NELP**: 202-602-5818

### Original Templates (For Reference)

- **Full templates + send timing**: DOMAIN_59_TIER2_SEND_TEMPLATES.md
- **Contact verification baseline**: DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md (June 10, 2026 audit)

---

## Cross-References

- Daily monitoring dashboard: DOMAIN_59_TIER_2_RESPONSE_TRACKING_DASHBOARD.md (execute if bounce is resolved)
- Wave 2 send templates: DOMAIN_59_TIER2_SEND_TEMPLATES.md (reference email content)
- Activation decision tree: TIER_2_ACTIVATION_DECISION_TREE.md (execute if resends produce signals)
- Send log: domain-59-send-log-june1.md (update with bounce + resend attempts)

---

*Created June 25, 2026. Execute immediately if any Wave 2 email bounces or fails. Recovery window is 48 hours from bounce detection. No [TODO] placeholders — all steps actionable. Print Step 1–3 and keep at desk during June 24–30 send window.*
