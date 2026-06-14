---
title: "Phase 2 Email Campaign — Master Checklist"
domain: "51 — Campaign Finance / Dark Money"
created: "2026-06-14"
status: "production-ready"
total_emails: 5
hard_deadline: "2026-07-01"
estimated_total_time: "2.5 hours active (Wave 1 + Wave 2 combined)"
---

# Phase 2 Email Campaign — Master Checklist
## Domain 51: Campaign Finance / Dark Money | 5 Emails | June 14-15, 2026

This document is the single-page overview. It does not replace the wave checklists — it tells you the sequence, timing, and what to do if something goes wrong.

---

## Status at a Glance (June 14, 2026)

| Item | Status |
|------|--------|
| Wave 1 (CLC + Issue One) | OVERDUE — scheduled June 9, execute today |
| Wave 2 (Common Cause CA, LWV CA, Clean Money) | OVERDUE — scheduled June 12, execute today or tomorrow |
| All 5 email templates | PRODUCTION-READY — copy-paste, zero editing except your name/contact |
| All 5 contact addresses | VERIFIED CURRENT (June 5-11, 2026) |
| Gist URL | LIVE as of June 14 — confirm before first send |
| Days remaining to hard deadline | 17 days (July 1, 2026) |
| Recoverable? | YES — both waves complete by June 15 = on track |

---

## Execution Timeline

Execute in this order. Adjust start times to your schedule — the stagger intervals are fixed, start times are flexible.

**Recommended same-day execution (both waves, single session):**

| Time (UTC) | Action | File |
|------------|--------|------|
| T+0 | Pre-flight: confirm Gist URL live, decide your name/contact info | This document |
| T+0 | Send Email 1 — CLC (echlopak@campaignlegalcenter.org) | `WAVE_1_EXECUTION_CHECKLIST.md` |
| T+90 min | Send Email 2 — Issue One (info@issueone.org) | `WAVE_1_EXECUTION_CHECKLIST.md` |
| T+180 min | Send Email 3 — Common Cause CA (dkemp@commoncause.org, CC: info@commoncause.org) | `WAVE_2_EXECUTION_CHECKLIST.md` |
| T+270 min | Send Email 4 — LWV CA (lwvc@lwvc.org) | `WAVE_2_EXECUTION_CHECKLIST.md` |
| T+360 min | Send Email 5 — Clean Money Action Fund (info@CAclean.org) | `WAVE_2_EXECUTION_CHECKLIST.md` |
| T+360 min | Verify all 5 timestamps in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | Execution log |

**Total wall-clock time**: 6 hours from first send to last send (but only ~45 minutes of active work; the rest are background waits).

**If splitting across two days:**
- Day 1 (today): Wave 1 only — 2 emails, 90-minute stagger, ~30 minutes active
- Day 2 (tomorrow): Wave 2 only — 3 emails, 90-minute stagger per send, ~45 minutes active

---

## All 5 Recipients at a Glance

| # | Wave | Organization | Contact | Email |
|---|------|-------------|---------|-------|
| 1 | Wave 1 | Campaign Legal Center | Erin Chlopak, Sr. Director | echlopak@campaignlegalcenter.org |
| 2 | Wave 1 | Issue One | General inbox | info@issueone.org |
| 3 | Wave 2 | Common Cause California | Darius Kemp, Executive Director | dkemp@commoncause.org |
| 4 | Wave 2 | LWV California | Jenny Farrell, Executive Director | lwvc@lwvc.org |
| 5 | Wave 2 | Clean Money Action Fund | Campaign Operations | info@CAclean.org |

---

## Pre-Flight (Do Once Before Starting Either Wave)

- [ ] Load Gist URL in browser: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — confirm it resolves
- [ ] Decide your name and contact info (you will paste these into every email):
  - YOUR_NAME: _______________________________
  - YOUR_CONTACT_INFO: _______________________________
- [ ] (Wave 2 only) Check Ballotpedia for California Fair Elections Act: https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026) — confirm it is still active

---

## Post-Campaign Logging Template

After all 5 emails are sent, update `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md` and optionally add an entry to `WORKLOG.md` using this format:

```
## [DATE] UTC — Domain 51 Phase 2 Wave 1+2 Sends Complete

**Wave 1:**
- Send 1 (CLC): [TIME] UTC — delivered
- Send 2 (Issue One): [TIME] UTC — delivered

**Wave 2:**
- Send 3 (Common Cause CA): [TIME] UTC — delivered
- Send 4 (LWV CA): [TIME] UTC — delivered
- Send 5 (Clean Money Action Fund): [TIME] UTC — delivered

**Bounces**: [none / list any]
**T+7 checkpoint**: [DATE — 7 days from Wave 1 send]
**Status**: All 5 sends complete. Monitoring phase begins.
```

---

## Reply Logging Template

When a reply arrives, log it in `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md` (Reply Received field) and optionally in WORKLOG.md:

```
## [DATE] UTC — Domain 51 Reply Received

**From**: [Name / Organization / email address]
**Classification**: STRONG / MODERATE / WEAK / NONE
**Summary**: [1-2 sentences describing what they said]
**Action taken**: [Replied within 24h / No reply needed / Flagged for Wave 3 follow-up / etc.]
```

**Classification guide:**

| Classification | What it looks like |
|---------------|-------------------|
| STRONG | Named staff reply with substantive content; request for conversation; citation request; request to share with colleagues |
| MODERATE | Auto-acknowledgment with a named contact; out-of-office with a specific person's name (that person becomes a follow-up target) |
| WEAK | Generic form reply with no named contact; "please remove" (log and remove from future contact list) |
| NONE | No reply — leave as PENDING through Day 14, mark NO RESPONSE after Day 14 |

---

## T+7 Checkpoint

7 days after Wave 1 send, check your inbox for replies. This is the key Phase 2 gate.

**What to check:**
1. Any reply from @campaignlegalcenter.org
2. Any reply from @issueone.org
3. Any reply from @commoncause.org
4. Any reply from @lwvc.org
5. Any reply from @caclean.org
6. Search spam folder for each of these domains

**Composite signal and Phase 2 routing:**

| Signal | Condition | Phase 2 Action |
|--------|-----------|----------------|
| STRONG | 4+ STRONG replies across all 5 contacts | Activate Domain 48 + Domain 57 in parallel (June 21-27) |
| MODERATE | 2-3 STRONG replies | Activate Domain 48 sequentially; hold Domain 57 for secondary June 28 checkpoint |
| WEAK | 0-1 STRONG replies | Hold both domains; review contingency options; user decision required |

Full logic: `DOMAIN_51_JUNE_16_DECISION_LOGIC.md`

---

## Risk Mitigation

### Risk 1: Gist URL returns 404

Do not send until resolved. Recreate the Gist from `projects/resistance-research/domain-51-campaign-finance-dark-money.md`. Use `GIST_TEMPLATE_DOMAIN_56.md` as format reference. This takes 10 minutes. Replace the URL in all unsent email bodies before sending.

### Risk 2: Email bounce

Use backup addresses for the two contacts that have them:
- CLC (echlopak@): backup is info@campaignlegal.org
- Common Cause CA (dkemp@): backup is ca@commoncause.org

For Issue One, LWV CA, and Clean Money Action Fund: log the bounce, do not resend to a guessed address.

### Risk 3: California Fair Elections Act removed from November ballot

Modify Wave 2 subject lines from "California Fair Elections Act campaign" to "California campaign finance reform analysis." The email bodies remain substantively valid — the dark money architecture research does not depend on the ballot measure being active. Full decision tree: `DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md`, Section 6.

### Risk 4: Zero replies at Day 7

This is within normal range. National DC policy organizations (CLC, Issue One) take 3-7 business days to route external research. California campaign organizations (Common Cause CA, LWV CA) are in campaign crunch mode. Zero replies at Day 7 does not indicate delivery failure. Continue monitoring to Day 14 before drawing conclusions or taking follow-up action.

### Risk 5: Zero replies at Day 14 (all 5 contacts)

Send Wave 3 follow-up to Common Cause CA only (dkemp@commoncause.org). Template is in `WAVE_2_EXECUTION_CHECKLIST.md`, Step 7 (Conditional Wave 3). Do not send follow-ups to CLC before Day 14 (the CLC Day-14 follow-up template is in `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md`). Do not send follow-ups to Issue One, LWV CA, or Clean Money Action Fund in this distribution cycle.

---

## File Index

| File | Purpose |
|------|---------|
| `WAVE_1_EXECUTION_CHECKLIST.md` | Step-by-step Wave 1 execution with inlined email bodies — open this to send |
| `WAVE_2_EXECUTION_CHECKLIST.md` | Step-by-step Wave 2 execution with inlined email bodies — open this to send |
| `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md` | Record send timestamps and replies here |
| `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md` | Full Wave 1 package with extended response monitoring + contingency follow-up templates |
| `DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md` | Full Wave 2 package with path routing + Wave 3 conditional template |
| `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` | Phase 2 activation decision tree (T+7 relative) |
| `DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md` | Ballot removal contingency + SB-299 fallback research plan |
| `WORKLOG.md` | Log send activity and replies here (optional but recommended) |

---

## Phase 2 Wave 3 Planning Note

Wave 3 (Domains 48 and 57) activation decision occurs at the T+7 checkpoint. Domain 48 (Criminal Justice / Civic Exclusion) and Domain 57 (Multilateral Withdrawal) are the next domains in the Phase 2 sequence.

- Domain 48: June 17-18 checkpoint planning (activation if T+7 shows STRONG signals from Wave 1+2)
- Domain 57: Hold until August 10 (UN General Assembly prep window)

No Wave 3 work is required before completing both Domain 51 waves.

---

*Created June 14, 2026. Covers Domain 51 Phase 2 Wave 1 and Wave 2 only. Hard deadline: July 1, 2026 (California Fair Elections Act messaging infrastructure lock). 17 days remain as of June 14.*
