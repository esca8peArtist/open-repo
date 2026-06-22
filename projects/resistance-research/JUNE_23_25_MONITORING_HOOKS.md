---
title: "June 23-25 Monitoring Hooks"
subtitle: "SCOTUS tracking, Senate Finance markup monitoring, inbox signal detection"
created: "2026-06-22"
session: "3911"
status: "background monitoring reference — check as needed"
---

# June 23-25 Monitoring Hooks

*Session 3911 | June 22, 2026*

**Purpose**: Background monitoring checklist for external signals during June 23-25 checkpoint window. These are "passive intelligence" triggers — check them once per day, but do not stop T+7 tasks if nothing new appears.

---

## SCOTUS Opinion Monitoring

### Supreme Court Opinion Schedule

**What to monitor**: supremecourt.gov/opinions/slipopinion/25

**Check timing**: 9:00 AM ET daily (June 23-25, and beyond)
- SCOTUS typically releases opinions 6:30–10:00 AM ET on opinion days
- Monday-Thursday during Term are most likely opinion days (rare on Friday)
- Check every morning; check again mid-afternoon if uncertainty

**Cases to watch for**:

| Case Number | Case Name | Expected timing | Domain trigger | Action |
|-----------|-----------|-----------------|-------------|--------|
| 24-38 | Little v. Hecox | June 2026 any day | Domain 50 IMMEDIATE distribution | STOP all tasks; execute 30-min contingency protocol |
| 24-43 | West Virginia v. B.P.J. | June 2026 any day | Domain 50 IMMEDIATE distribution | STOP all tasks; execute 30-min contingency protocol |
| 25-332 | Trump v. Slaughter | June-July 2026 | Domain 51 messaging update | Messaging enhancement (secondary, ~10 min) |
| 25-365 | Trump v. Barbara | June-July 2026 | Domain 58 rapid response | Domain 58 execution (~20 min) if adverse ruling |

**How to search SCOTUS website**:
1. Go to supremecourt.gov/opinions/slipopinion/25
2. Use Ctrl+F to search for case numbers: 24-38, 24-43, 25-332, 25-365
3. If found, click to view opinion PDF
4. Read first page to confirm holdings + ruling direction

**Verification rule**: Do NOT rely on news alerts. Always verify the actual opinion at supremecourt.gov before executing any contingency protocol.

---

## Senate Finance Committee Monitoring

### OBBBA / CTC Markup Tracking

**What to monitor**: Senate Finance Committee markup schedule (Domain 59 activation trigger)

**Expected window**: June 24-30, 2026
- Senate Finance Committee typically holds weekly markups on Tuesdays-Thursdays
- OBBBA-related CTC legislation may be included in broader tax/revenue markups
- If markup is active during Domain 59 Wave 2 send window (June 24), this confirms forced activation decision

**How to check**:
1. Visit: https://www.finance.senate.gov/ (Senate Finance homepage)
2. Look for: "Markup Schedule" or "Weekly Schedule"
3. Search for: "OBBBA" or "CTC" or "child tax credit" in weekly agenda
4. Check for: EPI, Demos, NELP organizational presence at markup

**Action if markup is active June 24-25**:
- This confirms forced Domain 59 Wave 2 activation on June 24 morning
- Send EPI + Demos emails as planned (timing is correct)
- Add to DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md: "Senate Finance markup active June [date]. Forced activation decision confirmed."

**Where to log finding**: CHECKIN.md or DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md

---

## Inbox Monitoring for Reply Signals

### Daily Inbox Check Procedure

**What to monitor**: Replies from Domain 51, 48, 59 Wave 1 contacts

**Timing**: Check inbox every morning (before 9:30 AM) on June 23, 24, 25

**Who to expect replies from**:

| Domain | Contact | Email | Expected reply window |
|--------|---------|-------|----------------------|
| Domain 51 | CLC (Erin Chlopak) | echlopak@campaignlegalcenter.org | June 23-24 (if sent June 16-17) |
| Domain 51 | Issue One (Nick Penniman) | info@issueone.org | June 23-24 |
| Domain 48 | Sentencing Project (Nicole Porter) | nporter@sentencingproject.org | June 23-25 (if sent June 16-18) |
| Domain 48 | Prison Policy Initiative | info@prisonpolicy.org | June 23-25 |
| Domain 59 | CBPP | info@cbpp.org | Already replied (June 17); check for upgrade signal |
| Domain 59 | MomsRising | info@momsrising.org | Already replied (June 17); check for upgrade signal |
| Domain 59 | AFL-CIO | [use afl-cio.org contact] | First-reply window June 23-24 |
| Domain 59 | ITEP | info@itep.org | First-reply window June 23-24 |
| Domain 59 | NWLC | info@nwlc.org | First-reply window June 23-24 |

**Inbox check procedure**:
1. Search for sender email address (e.g., echlopak@campaignlegalcenter.org) to find their reply
2. Read reply subject + first paragraph
3. Apply signal classification (see SIGNAL CLASSIFICATION section below)
4. Record in JUNE_23_25_CHECKPOINT_EXECUTION_CHECKLIST.md status tables
5. If 3+ STRONG signals or any unexpected engagement surge: flag in CHECKIN.md

**Note on spam filtering**: If you expect a reply but do not see it:
1. Check spam folder (Gmail / Outlook)
2. Search inbox for sender domain (e.g., "from:campaignlegalcenter.org")
3. If found in spam: mark as "Not Spam" and log in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md: "CLC reply was in spam folder — mark as not spam for future emails"

---

## Signal Classification Summary

Use this reference while reading inbox replies during June 23-25:

| Signal | What to look for | Example language | Action |
|--------|-----------------|------------------|--------|
| **STRONG (S)** | Named individual (not inbox); specific action requested or offered | "Can we set up a call?" / "I'm forwarding to our team who works on this" / "Can you send our full research proposal?" | Counts toward T+7 routing decision. Activates Tier 2 or accelerates timeline. |
| **MODERATE (M)** | Generic inbox reply + interest expressed; OR named individual + forward to team (no follow-up) | "Thank you, this is relevant to our work" / "I've sent this to our research director" | Counts toward T+7 routing decision at MODERATE threshold. May activate single Tier 2 contact. |
| **WEAK (W)** | Auto-reply or form response; no substantive content engagement; no individual name | "We received your message, thanks" / "Out of office, back June 30" | Does NOT count toward routing decision. If 0 replies after 72+ hours, triggers delivery diagnostic. |
| **BOUNCE (B)** | Hard bounce (address invalid) or OOO with no alternate contact provided | Hard bounce message / "I'm out of office with no coverage" | Requires action: re-verify address on organization website, resend within 48 hours. Log attempt. |
| **No reply (--)**  | No email received 48-72 hours after send | Absence of email | Normal at T+7 for cold outreach. Not a failure signal. Recount on Day 14 (June 30). |

---

## Tier 2 Activation Signals

If you receive a reply that contains these phrases, this is likely STRONG:

### Domain 51 (Campaign Finance)
- "Can we discuss your findings on [specific topic]"
- "I'm forwarding this to our policy director"
- "This connects to our current work on California ballot initiatives"
- "Our research team is interested in this angle — can you send the full document?"
- "We're planning a June-July campaign, your framing is helpful"

### Domain 48 (Criminal Justice)
- "We're integrating this into our Virginia voting rights work"
- "Can you brief our litigation team?"
- "This connects to our Callais redistricting analysis"
- "We'd like to feature this in our July newsletter"

### Domain 59 (Economic Precarity / CTC)
- "Our research team is using this for the Senate Finance markup"
- "Can we co-distribute this to our networks?"
- "This is exactly the framing we need for the June 30 deadline"
- "I'm forwarding this to our policy team; they'll follow up"

---

## Emergency Protocol: Surge in Replies

**If you receive 5+ replies to a single domain send within 24 hours**:

1. **Do not panic** — this is actually good signal
2. **Log immediately** in CHECKIN.md: "Domain [X] reply surge detected: [count] replies received June [date]"
3. **Assess signal quality**: Apply signal classification to each. Count STRONG vs MODERATE
4. **Do NOT change routing decisions** — continue with planned T+7 routing as scheduled
5. **Update distribution execution log** with surge note: "Unexpected engagement surge. [count] replies, [count] STRONG. T+7 routing decision unchanged."
6. **Potential follow-up**: If 3+ STRONG received before scheduled Tier 2 send, you may accelerate Tier 2 activation (send same afternoon instead of next day). Document in execution log.

---

## No-Reply Scenario: Delivery Diagnostic

**If by June 25 (Day 8-9 depending on send date) you have 0 replies from any contact in a domain**:

1. **Load Gist URL** in browser to confirm HTTP 200 (page loads)
   - Domain 51 Gist: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
   - Domain 48 Gist: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8
   - Domain 59 Gist: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba
   - If 404: recreate using contingency procedures (files: DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md, etc.). Resend.

2. **Send test email to yourself**:
   - From the same sending account used for outreach
   - Subject: "Test: does this reach my inbox?"
   - 1 sentence of body text, no links
   - Check if it reaches your inbox (not spam folder)
   - If spam folder: Adjust sender reputation or subject line. Resend outreach to 1 contact with plain text (no links).

3. **Verify contact addresses**:
   - Check organization website (published after June 1, 2026) for current contact email
   - Do not rely on template addresses alone
   - Example: Campaign Legal Center public contact directory: campaignlegalcenter.org/about/staff/
   - If address differs from template: Update template and resend to 1 contact; wait 48 hours before expanding

4. **Assess message quality**:
   - Reread the email template you sent
   - Is the subject line clear and relevant? Or does it seem generic/spammy?
   - Are there any spam trigger words (excessive caps, financial jargon, multiple links)?
   - Consider personalizing subject line for CA contacts (Domain 51): Include "Californians for Fair Elections" or "California ballot" in subject if not already present

5. **Document findings in execution log**:
   - Record: "Delivery diagnostic run [date]. Gist [status: loads/404]. Test email [status: inbox/spam]. Contact addresses [verified/updated]. Resend to [contact] with [specific change]."

6. **Recount on June 30** (Day 14): If still 0 replies after 14 days with confirmed delivery, switch from "weak signal" to "systematic delivery failure." May need to use alternate channels (LinkedIn, phone, coalition referral).

---

## Notes & Contingencies

### If SCOTUS Decision Overlaps with T+7 Checkpoint

Example scenario: Little v. Hecox decision publishes 9:00 AM June 24 (while you are doing Domain 59 inbox check)

**Action**:
1. Stop Domain 59 inbox check
2. Execute Little v. Hecox contingency (30 min: Gist creation + 3 emails + logging)
3. Resume Domain 59 inbox check after contingency is complete
4. Continue with Domain 59 forced activation decision on schedule

**No delay to T+7 timing**: SCOTUS contingency executes in parallel with T+7, not sequentially.

### If reply pattern suggests timing mismatch

Example: Domain 51 emails sent June 16, but by June 25 you have only 1 reply from 2 contacts

**Possible explanations**:
1. **Emails hit spam folder**: Run delivery diagnostic (see above)
2. **Send timing was off**: Check sent folder timestamp. If emails sent late June 16 (after 5 PM), responses may arrive June 24-25 instead of June 23-24
3. **Contact out of office**: Check for OOO auto-replies. If contact has named alternate, log alternate and follow up after OOO window

**Action**: Update DISTRIBUTION_EXECUTION_LOG.md with timing note; adjust Day 14 checkpoint (June 30) expectations accordingly.

---

## Files to Keep Open During June 23-25

1. **This file** (JUNE_23_25_MONITORING_HOOKS.md) — Reference for signal classification
2. **JUNE_23_25_CHECKPOINT_EXECUTION_CHECKLIST.md** — Daily task list with status tables
3. **JUNE_23_25_CONTINGENCY_ACTIVATION_PROTOCOLS.md** — For SCOTUS decision trees
4. **supremecourt.gov/opinions/slipopinion/25** (browser bookmark) — Check 9:00 AM daily
5. **senate.gov/committees/rules-administration/** or **finance.senate.gov** — Check for markup schedule
6. **DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md** — Log all Domain 51 activity
7. **DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md** — Log all Domain 48 activity
8. **DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md** — Log all Domain 59 activity

---

## Quick Reference: What Needs Immediate Action?

| Signal | Timing | Action |
|--------|--------|--------|
| **Little v. Hecox or BPJ decision published** | Anytime, June 23-25+ | STOP all tasks. Execute 30-min Domain 50 distribution. Resume after logging. |
| **Trump v. Barbara adverse ruling** | Anytime, June 23-25+ | Execute 20-30 min Domain 58 rapid response. Resume after logging. |
| **Trump v. Slaughter overrules Humphrey's Executor** | Anytime, June 23-25+ | Update Domain 51 messaging (~10 min). Resume after logging. |
| **Senate Finance markup active June 24-25** | Check daily | Confirms Domain 59 forced activation. Proceed as planned. |
| **CLC or Issue One reply (Domain 51)** | Expected June 23-24 | Score signal. Count STRONG. Update routing decision if needed. |
| **Sentencing Project reply (Domain 48)** | Expected June 23-25 | Score signal. Count STRONG. Update routing decision if needed. |
| **Surge of 5+ replies to any domain** | Check inbox 2x daily | Log surge in CHECKIN.md. Assess signals. Do NOT change routing, but note for acceleration opportunity. |
| **0 replies by June 25 from Domain 51/48** | If happens | Run delivery diagnostic. Recount on June 30 (Day 14). |

---

*Prepared June 22, 2026 (Session 3911). These are passive intelligence checklist items — check them once per day, but do not interrupt T+7 checkpoint work if nothing urgent appears. SCOTUS decisions and Senate markup activity may trigger contingency protocols that override normal checkpoint timing.*
