# Wave 1 Recovery Execution SOP
## Resistance-Research Phase 2 Wave 1 Email Distribution — Step-by-Step User Action Guide

**Date**: June 14, 2026  
**Status**: Overdue (scheduled June 9-10; recovery window open until July 1)  
**Recovery Window**: 17 days remaining from today  
**Time Estimate**: 90 minutes (CLC email + Issue One email, including verification)

---

## Overview

Wave 1 distribution requires TWO email sends (CLC + Issue One) with a 90-minute stagger between them. This SOP walks through the exact steps using your email client (Gmail, Outlook, Apple Mail, or Thunderbird).

**Key Success Criteria**:
- ✅ Both emails sent from your personal email account (for sender authenticity and deliverability)
- ✅ Both emails delivered successfully (check inbox of CLC and Issue One)
- ✅ Gist URL remains accessible in sent email text (for recipients to click)
- ✅ Send times logged in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md within 5 minutes of sending

---

## Step-by-Step Execution

### FIRST EMAIL: Campaign Legal Center (CLC)

**Recipient**: Erin Chlopak (echlopak@campaignlegalcenter.org)  
**Subject Line**: `Urgent: Democratic Accountability Reform Research — Domain 51 Campaign Finance Analysis`  
**Send Time**: **NOW** (or within 5 minutes)  
**Template Location**: `domain-51-send-templates.md` (Section A)

#### Instructions:

1. **Open your email client** (Gmail web, Outlook web, Apple Mail, Thunderbird)
   - Ensure you're logged into YOUR personal email account (not a shared account)
   
2. **Create a new message**
   - To: `echlopak@campaignlegalcenter.org`
   - Subject: Copy from `domain-51-send-templates.md` Section A (subject line)
   
3. **Compose the email body**
   - Open `domain-51-send-templates.md` in a browser tab
   - Section A contains the full email template
   - **CRITICAL**: Do NOT modify the Gist URL (keep it as-is)
   - Optional: Personalize the salutation ("Dear Erin," works; "Hi Erin" also fine)
   - Copy the entire template text into your email compose box
   
4. **Send the email**
   - Click "Send"
   - **Record the send time** (note it down: HH:MM UTC)
   
5. **Verify delivery** (immediate, within 30 seconds)
   - Go to Gmail/Outlook "Sent" folder
   - Confirm the email appears with a green checkmark (✓) or "Sent" status
   - If you see a red X or "Failed": STOP and proceed to "Email Send Failure Recovery" section below
   
6. **Record in execution log**
   - Open `projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`
   - In "Wave 1 Execution Log" section, add a row:
   ```
   | CLC | Erin Chlopak | echlopak@campaignlegalcenter.org | HH:MM UTC | Sent | Delivered |
   ```
   - Note: "Delivered" status will be confirmed when Erin opens the email (updated June 21)

---

### WAIT 90 MINUTES

**Timer**: Set a phone alarm or laptop reminder for **+90 minutes from now**

- Use this time to (1) verify CLC email landed in inbox (optional; email should arrive within 2-5 min), (2) prepare for Issue One send

---

### SECOND EMAIL: Issue One (Democracy Reform Alliance)

**Recipient**: info@issueone.org  
**Subject Line**: `Urgent: Democratic Accountability Reform Research — Domain 51 Campaign Finance Analysis`  
**Send Time**: **90 minutes after CLC send**  
**Template Location**: `domain-51-send-templates.md` (Section B)

#### Instructions:

1. **Open a fresh email compose**
   - To: `info@issueone.org`
   - Subject: Copy from `domain-51-send-templates.md` Section B (same as CLC subject, or similar)
   
2. **Compose the email body**
   - Open `domain-51-send-templates.md` Section B
   - Copy the full email template into your compose box
   - **CRITICAL**: Do NOT modify the Gist URL
   - Optional: Personalize salutation
   
3. **Send the email**
   - Click "Send"
   - Record the send time (HH:MM UTC, exactly 90 minutes after CLC send)
   
4. **Verify delivery**
   - Check "Sent" folder for green checkmark
   - Confirm "Sent" status
   
5. **Record in execution log**
   - Update `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`:
   ```
   | Issue One | info@issueone.org | info@issueone.org | HH:MM UTC | Sent | Delivered |
   ```

---

## Email Send Failure Recovery

### If Email Returns "Failed" or "Bounced"

**Scenario A**: Email bounces with "Invalid recipient" or "Address rejected"
- **Likely cause**: Email address typo or recipient no longer active
- **Recovery**: Use the backup contact from `WAVE_1_BACKUP_CONTACT_ROSTER.md`
  - CLC: Contact Saurav Ghosh (sghosh@campaignlegalcenter.org) with note: "Original recipient Erin Chlopak was unavailable; forwarding per alt contact."
  - Issue One: Contact Michael Beckel (michael@issueone.org) with same note
- **Timeline impact**: 30-minute delay per failed send; recovery adds 1-2 hours total

**Scenario B**: Email marked "Spam" or "Blocked by recipient server"
- **Likely cause**: Your email provider flagged as bulk/automation
- **Recovery**: Resend from a different email account if available (ask a trusted colleague to relay)
- **Fallback**: Post to Gist as public update (no recipient needed); notify via Discord if available

**Scenario C**: "Connection timeout" or "SMTP error"
- **Likely cause**: Email provider temporary outage
- **Recovery**: Wait 5 minutes, retry send
- **If persists**: Switch email providers (use Gmail if Outlook failed, etc.)

---

## Gist Fallback Option

**If email delivery fails for both CLC and Issue One**, you can use the Gist URL directly:

1. **Public Gist is live at**: https://gist.github.com/esca8peArtist/[GIST_ID]/domain-51-campaign-finance
2. **Send a message via LinkedIn** (if available) to target contacts with message: "I've published research on campaign finance reform here: [GIST_URL]. I'd value your feedback."
3. **Fallback is slower** (manual outreach per contact) but **eliminates email delivery risk**

---

## Post-Send Verification Checklist

✅ **Both emails sent** (CLC + Issue One)  
✅ **Send times logged** in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md  
✅ **Sent folder shows green checkmarks** (no failure messages)  
✅ **Gist URL is still accessible** (test by clicking the URL from your sent email)  
✅ **Total elapsed time** should be ~90 min CLC + 90 min wait + 5 min Issue One = 3 hours total

---

## Next Steps After Wave 1 Sends Complete

1. **Wait for responses** (June 21-23 open rate tracking)
2. **Log responses** in `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md` (when you receive replies)
3. **June 17 prep**: Prepare Wave 2 emails (Darius Kemp + Jenny Farrell + Clean Money) for June 12 send (if Wave 1 sent June 9; adjust if sent later)
4. **June 17 Day 7 checkpoint**: Review engagement metrics using `PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md`

---

## Contact Information Reference

| Organization | Contact Name | Email | Notes |
|---|---|---|---|
| Campaign Legal Center | Erin Chlopak | echlopak@campaignlegalcenter.org | PRIMARY (verified June 5, 2026) |
| Issue One | info@issueone.org | info@issueone.org | PRIMARY (verified June 5, 2026) |
| CLC Backup | Saurav Ghosh | sghosh@campaignlegalcenter.org | Use if Erin unavailable |
| Issue One Backup | Michael Beckel | michael@issueone.org | Use if main email bounces |

---

## Email Template Quick Reference

**Template A (CLC)**: Subject and body in `domain-51-send-templates.md`, Section A  
**Template B (Issue One)**: Subject and body in `domain-51-send-templates.md`, Section B

Both templates are **copy-paste ready** — no modifications needed except optional salutation personalization.

---

## Questions / Troubleshooting

**Q: Can I send both emails at the same time?**  
A: No — 90-minute stagger is required to avoid batch-send detection filters. Send CLC first, wait 90 min, send Issue One.

**Q: What if I send them the other way around (Issue One first)?**  
A: Impact is minimal (not a blocker), but may reduce response rates slightly. Preferred order: CLC → 90 min wait → Issue One.

**Q: Does the email need to come from my personal account?**  
A: YES. Sender authenticity is critical for recipient trust. Do NOT send from an automated/organizational account. Email must show your name as sender.

**Q: Can I use a template Gmail or Outlook feature?**  
A: Yes, if you want. Just ensure the Gist URL and contact names are not templated (copied by hand from `domain-51-send-templates.md`).

**Q: Should I follow up if they don't respond?**  
A: Wait until June 21 (7 days) before follow-up. If no response by June 21, check engagement metrics (Gist clicks, email opens) before deciding on outreach.

---

## Success Acknowledgment

Once both emails are sent and logged:

**IMPORTANT**: Please reply to this SOP document with:
- Timestamp of CLC send (HH:MM UTC)
- Timestamp of Issue One send (HH:MM UTC)
- Confirmation that both emails show "Sent" status (not bounced)

This will trigger Day 7 checkpoint automation on June 21 (or June 17 if sent today June 14).
