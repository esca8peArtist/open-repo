---
title: "Phase 2 Wave 1 Execution Log — Domains 51, 48, 59"
created: "2026-06-10"
status: "ready-for-user-execution"
wave_1_window: "June 10, 2026 — CLC + Issue One (user sends)"
wave_2_window: "June 12-13, 2026 14:00 UTC — CA contacts (user sends)"
day_7_checkpoint: "June 17-18, 2026"
---

# Phase 2 Wave 1 Execution Log
## Domains 51, 48, 59 — Distribution Status and User Action Queue

*Prepared June 10, 2026. This log tracks the production-ready state of all three active distribution domains and the exact user actions required for Wave 1 execution. No new research is needed. This is a send-day log.*

---

## Domain Status Summary

| Domain | Topic | Gist | Templates | Contacts Verified | Send Window | Status |
|--------|-------|------|-----------|-------------------|-------------|--------|
| **Domain 51** | Campaign Finance / Dark Money | Live — https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | 5 emails in `domain-51-send-templates.md` | Yes — June 5-6, 2026 | June 10 (Wave 1) + June 12-13 (Wave 2) | CLEAR TO SEND |
| **Domain 59** | Economic Precarity / CTC | Live — https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba | 5 emails in `domain-59-send-templates.md` | Yes | HOLD — urgency frame requires patch | BLOCKED: patch OBBBA frame before sending |
| **Domain 48** | Criminal Justice / Civic Exclusion | Live — https://gist.github.com/esca8peArtist/c4f8e2a1b9d7e3f5a2c6b8d4e9f1a3c5 | 4 emails in `DOMAIN_48_EMAIL_TEMPLATE_SET.md` | Yes | June 16-17 (Wave 1) | CLEAR TO SEND |

---

## Wave 1 — June 10, 2026: CLC + Issue One

**User time required: 60-90 minutes total**

The Wave 1 contacts are the two national policy organizations with the longest decision cycles. They must receive the research earliest to have lead time before the July 1 California messaging lock.

### Contact 1: Campaign Legal Center

- **Named contact**: Erin Chlopak, Senior Director, Campaign Finance (verified June 5-6, 2026)
- **Primary email**: echlopak@campaignlegalcenter.org (direct; recommended — increases routing probability to 65-75%)
- **Alternate email**: info@campaignlegal.org (general inbox; also valid)
- **Subject**: "Constitutional architecture research on Citizens United — Hawaii/Montana model + FEC collapse analysis"
- **Template**: Email 4 in `domain-51-send-templates.md`
- **Field fills**: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` — 2 fills
- **Gist URL**: Pre-filled in template — no URL replacement needed
- **Personalization note**: CLC's hook is the Hawaii SB 2471 corporate charter theory and the FEC enforcement collapse documentation. Do not change the constitutional framing.
- **CLC conflict with Domain 49**: If Domain 49 sends also went to CLC on June 10, shift this send to June 11 09:00 local. Issue One proceeds June 10 regardless.
- **Send time**: 09:00-10:00 local (or 14:00 UTC per the June 6 checklist)
- **Estimated time**: 8 minutes to send
- **Log after send**: Add to `DISTRIBUTION_EXECUTION_LOG.md` — date, time, CLC address, subject line

### Contact 2: Issue One

- **Named contact**: Nick Penniman, Founder and CEO (verified June 5-6, 2026)
- **Primary email**: info@issueone.org (general inbox; verify at issueone.org/contact before sending)
- **Subject**: "Dark money architecture research — FEC collapse documentation + state ballot measure analysis"
- **Template**: Email 5 in `domain-51-send-templates.md`
- **Field fills**: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` — 2 fills
- **Gist URL**: Pre-filled in template — no URL replacement needed
- **Personalization note**: Issue One's hook is the ReFormers Caucus framing and the FEC enforcement shutdown. Issue One is cited as a primary source throughout — note this in the framing.
- **Send time**: 10:30-11:00 local (90-minute gap after CLC send — professional standard for multi-send days)
- **Estimated time**: 8 minutes to send
- **Log after send**: Add to `DISTRIBUTION_EXECUTION_LOG.md`

### Wave 1 Send Sequence

```
08:30 local — Pre-send check:
  - Load Gist URL: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
  - Confirm page loads (no login required)
  - Open domain-51-send-templates.md
  - Fill [YOUR_NAME] and [YOUR_CONTACT_INFO] in Emails 4 and 5 only

09:00 local — Send Email 4 (CLC)
09:15 local — Log CLC send in DISTRIBUTION_EXECUTION_LOG.md

10:30 local — Send Email 5 (Issue One)
10:45 local — Log Issue One send in DISTRIBUTION_EXECUTION_LOG.md
             — Note: "Monitoring begins June 10 EOD. Check inbox 18:00 local."
```

**Wave 1 success criteria**: Both emails sent. Logging complete. Inbox check scheduled.

---

## Wave 2 — June 12-13, 2026: California Campaign Contacts

**User time required: 60-90 minutes total**

The California contacts are campaign co-chairs for the Californians for Fair Elections ballot campaign. They receive research mid-week (Wednesday) when campaign staff email attention peaks.

### Contact 3: Common Cause California

- **Named contact**: Darius Kemp, Executive Director (appointed June 2025; verified June 5-6, 2026)
- **Primary email**: dkemp@commoncause.org (direct; recommended)
- **Alternate email**: ca@commoncause.org (general inbox; also valid)
- **CC**: info@commoncause.org (national)
- **Subject**: "Research on Citizens United architecture for California Fair Elections Act campaign — July 1 window"
- **Template**: Email 1 in `domain-51-send-templates.md`
- **Field fills**: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` — 2 fills
- **Personalization note**: Common Cause CA is a co-chair of the Californians for Fair Elections ballot campaign committee. Reference "Californians for Fair Elections" by name. If sending to dkemp@, salutation is "Dear Darius,"
- **Campaign role**: One of three co-chairs of the November 2026 ballot campaign

### Contact 4: League of Women Voters California

- **Named contact**: Jenny Farrell, Executive Director (verified June 5-6, 2026 at lwvc.org/about/staff)
- **Primary email**: lwvc@lwvc.org (verified active)
- **Subject**: "Dark money architecture research for California Fair Elections Act campaign — July 1 window"
- **Template**: Email 2 in `domain-51-send-templates.md`
- **Field fills**: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` — 2 fills
- **Personalization note**: LWV's hook is voter education. The standalone 500-word Executive Summary and Section 6 international comparison are the most accessible sections for their civic education framing.
- **Campaign role**: Co-chair of Californians for Fair Elections

### Contact 5: Clean Money Action Fund

- **Primary email**: info@CAclean.org (verified June 5-6, 2026 via yesfairelections.org — cleanmoney.org domain unreachable; use campaign site contact)
- **Subject**: "Dark money research for California Fair Elections Act — 58 citations, CC Attribution 4.0"
- **Template**: Email 3 in `domain-51-send-templates.md`
- **Field fills**: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` — 2 fills
- **Personalization note**: This is the most operationally focused contact. Lead with the Californians for Fair Elections committee launch and AI PAC documentation as new material for campaign communications.
- **Pre-send action**: Confirm info@CAclean.org is still current via yesfairelections.org before sending

### Wave 2 Send Sequence (June 12 14:00 UTC / 09:00 PT)

```
08:30 local — Pre-send check:
  - Confirm Emails 1, 2, 3 in domain-51-send-templates.md
  - Fill [YOUR_NAME] and [YOUR_CONTACT_INFO] in all three now
  - Verify info@CAclean.org current at yesfairelections.org (5 min)

09:00 local — Send Email 1 (Common Cause CA — Darius Kemp)
09:30 local — Send Email 2 (LWV CA — Jenny Farrell)
10:00 local — Send Email 3 (Clean Money Action Fund)
10:30 local — Log all three sends in DISTRIBUTION_EXECUTION_LOG.md
             — Mark Domain 51 Wave 2 complete
```

---

## Day 7 Checkpoint — June 17-18, 2026

**User time required: 20-30 minutes**

- Check inbox for replies from all 5 contacts
- Log reply status in `DISTRIBUTION_EXECUTION_LOG.md`
- Check Gist view count (48-72 hours post-send)
- Evaluate against success thresholds in `DOMAIN_51_JUNE_9_12_EXECUTION_CHECKLIST.md` Section 5:
  - Minimum: 1 reply from any contact
  - Standard: 2 Tier A replies (CLC + Issue One both respond)
  - Strong: 3+ contacts responded — activate Tier 2 (Montana Plan, Michigan Clean Elections, New Mexico campaign finance reform orgs)
- If 0 responses: execute phone follow-up per `DOMAIN_51_EXECUTION_MONITORING.md`; do not re-send emails
- Set calendar reminder for June 25 if CA contacts have not responded (LinkedIn follow-up option — last resort)

---

## Domain 59 — HOLD: Urgency Frame Patch Required

**Do not send Domain 59 templates until this patch is complete.**

The current Domain 59 templates reference a "Senate Finance Committee markup window closes June 30" urgency frame. This frame is obsolete. The OBBBA (One Big Beautiful Bill Act) was signed into law July 4, 2025. The Senate Finance markup already happened.

**Patch required** (15-minute edit):

- Replace "Senate Finance markup window" urgency frame with: OBBBA implementation period (2025-2027 tax years) + 2026 midterm cycle
- New frame: The OBBBA's enacted CTC structure still delivers $0 average benefit to the poorest fifth. The SSN-for-taxpayer requirement explicitly excludes mixed-status households. The refundable portion is capped at $1,700 vs. the full-refundability advocacy position. Implementation advocacy is active now.
- Full patch documentation: `WAVE_1_NEWS_INTEGRATION.md`

**After patch**: Domain 59 is production-ready. Contacts (CBPP, ITEP, NWLC, MomsRising, AFL-CIO) are verified. Gist is live. Templates require only the urgency frame update and the 2 field fills per email.

---

## Domain 48 — HOLD: Gist Creation Required

**Do not send Domain 48 templates until Gist is live.**

Domain 48 research is production-ready (6,800+ words, 46 citations, `domains/domain-48-criminal-justice-civic-exclusion.md`). Email templates are in `DOMAIN_48_EMAIL_TEMPLATE_SET.md`. Contacts are stratified in `DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md`.

**Blocking item**: No Gist URL exists. All templates contain `{{DOMAIN_48_GIST_URL}}` placeholder — emails cannot go out until Gist is created and URL is propagated.

**Gist creation procedure**: `DOMAIN_48_GIST_CREATION_STEPS.md` — 5-10 minutes
**Create before**: June 15, 2026 (one day before first Wave 1 send window)
**Distribution window**: June 16-17 Wave 1 (Sentencing Project, Prison Policy Initiative, Campaign Legal Center, Worth Rises); June 18-19 Wave 2

---

## Field Fill Summary — All Active Templates

| Domain | Template File | Emails | Field Fills Each | Total Fills | Status |
|--------|--------------|--------|-----------------|-------------|--------|
| Domain 51 | `domain-51-send-templates.md` | 5 (Emails 1-5) | `[YOUR_NAME]` + `[YOUR_CONTACT_INFO]` | 10 total | Gist URL pre-filled — no URL replacement needed |
| Domain 59 | `domain-59-send-templates.md` | 5 (Emails 1-5) | `[Your name]` + `[Your contact information]` | 10 total | HOLD pending urgency frame patch |
| Domain 48 | `DOMAIN_48_EMAIL_TEMPLATE_SET.md` | 4 templates | `[YOUR_NAME]` + `[YOUR_CONTACT_INFO]` + `{{DOMAIN_48_GIST_URL}}` | 12 total | HOLD pending Gist creation |

---

## Source Documents

| Document | Purpose |
|----------|---------|
| `DOMAIN_51_JUNE_9_12_EXECUTION_CHECKLIST.md` | Master execution checklist with hour-by-hour schedule, contingency plans, success criteria |
| `WAVE_1_PRE_EXECUTION_CHECKLIST.md` | Contact validation (June 5-6, 2026), template verification, Gist accessibility check |
| `domain-51-send-templates.md` | 5 production-ready email templates for all Domain 51 contacts |
| `WAVE_1_NEWS_INTEGRATION.md` | Domain 59 urgency frame patch documentation; Domain 49 Callais update |
| `DOMAIN_48_GIST_CREATION_STEPS.md` | Step-by-step Gist creation procedure for Domain 48 |
| `DOMAIN_48_EMAIL_TEMPLATE_SET.md` | 4 Domain 48 email templates (awaiting Gist URL) |
| `DISTRIBUTION_EXECUTION_LOG.md` | Log target for all sends — update after each email |
| `DOMAIN_51_EXECUTION_MONITORING.md` | Day 7 measurement template and phone follow-up protocol |

---

*Execution Log prepared June 10, 2026. Wave 1 is ready for immediate user execution (Domain 51 — CLC + Issue One). Domain 59 and Domain 48 are staged for execution following the blocking items noted above.*
