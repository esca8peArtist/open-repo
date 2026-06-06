---
title: "Wave 1 Pre-Execution Checklist — Domain 51 (Campaign Finance)"
created: 2026-06-06
session: resistance-research-agent (Session 2957)
wave_1_execution_date: "June 10, 2026 14:00 UTC"
wave_1_contacts: "Campaign Legal Center + Issue One (90 min user action)"
wave_2_execution_date: "June 12-13, 2026 14:00 UTC"
wave_2_contacts: "Common Cause CA + LWV CA + Clean Money Action Fund"
---

# Wave 1 Pre-Execution Checklist — Domain 51 Distribution

*Authoritative pre-send verification for the June 10-12 Domain 51 Wave 1 + Wave 2 execution. Each item must be checked before opening the send templates. Total verification time: approximately 20 minutes.*

---

## Most Important Finding

**The Domain 51 California Fair Elections Act urgency frame is confirmed active.** The CA Fair Elections Act (SB 42) was placed on the November 2026 ballot by Governor Newsom (signed October 2, 2025). The campaign committee "Californians for Fair Elections" launched February 2026 — led by Common Cause CA, CA Clean Money Action Fund, and LWV CA. The July 1 messaging infrastructure window remains the correct hard deadline. No urgency-frame patch required.

**Domain 59 OBBBA urgency frame requires patching before any sends.** See WAVE_1_NEWS_INTEGRATION.md for the mandatory patch. The Senate Finance markup window framing is obsolete — the OBBBA was signed July 4, 2025. Domain 59 sends must use the updated OBBBA implementation and Medicaid crisis framing.

---

## Section 1: Document Verification (7 domains — confirm production-ready)

### Wave 1 Active Send Domains

| Domain | File | Gist URL | Status | Last Verified |
|--------|------|----------|--------|---------------|
| Domain 51 (Campaign Finance) | `domains/domain-51-campaign-finance-dark-money-architecture.md` | https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | PRODUCTION-READY | June 5, 2026 (contact verification pass) |
| Domain 59 (Economic Precarity) | `domains/domain-59-economic-precarity-and-civic-participation.md` | https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba | PRODUCTION-READY — urgency frame patch required (see WAVE_1_NEWS_INTEGRATION.md) | June 3, 2026 |

### Hold Domains (not sending in Wave 1-2)

| Domain | File | Gist URL | Hold Until | Reason |
|--------|------|----------|------------|--------|
| Domain 57 (Multilateral Withdrawal) | `domains/domain-57-multilateral-withdrawal-and-us-commitment-collapse.md` | https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61 | August 10, 2026 | UNGA prep window |
| Domain 48 (Criminal Justice) | `domains/domain-48-criminal-justice-civic-exclusion.md` | (no Gist created yet) | Pending Gist creation | Pre-distribution prep incomplete |
| Domain 49 (Callais VRA) | `domains/domain-49-callais-vra-redistricting-emergency.md` | (no Gist created yet) | Pending Gist creation | Callais decision (Apr 29, 2026) requires domain update — see WAVE_1_NEWS_INTEGRATION.md |
| Domain 50 (Healthcare Democracy Nexus) | `domains/domain-50-healthcare-democracy-nexus-obbba-nvra.md` | (no Gist created yet) | Pending Gist creation + OBBBA update | OBBBA enacted July 2025 — implementation framing needed |
| Domain 54 (Youth Civic Power) | `domains/domain-54-youth-civic-power-structural-barriers.md` | (no Gist created yet) | August 1, 2026 | Pre-midterm window |

---

## Section 2: Email Templates Verified

### Wave 1 Templates (June 10 — Campaign Legal Center + Issue One)

| Template | File | Contacts | Placeholder Fills Required | Status |
|----------|------|----------|---------------------------|--------|
| CLC Email | `domain-51-send-templates.md` — Email 4 | echlopak@campaignlegalcenter.org (Erin Chlopak, Senior Director) OR info@campaignlegal.org | `[YOUR_NAME]`, `[YOUR_CONTACT_INFO]` — 2 fills | VERIFIED READY |
| Issue One Email | `domain-51-send-templates.md` — Email 5 | info@issueone.org | `[YOUR_NAME]`, `[YOUR_CONTACT_INFO]` — 2 fills | VERIFIED READY |

### Wave 2 Templates (June 12-13 — CA contacts)

| Template | File | Contacts | Placeholder Fills Required | Status |
|----------|------|----------|---------------------------|--------|
| Common Cause CA Email | `domain-51-send-templates.md` — Email 1 | dkemp@commoncause.org (Darius Kemp, Executive Director) OR ca@commoncause.org | `[YOUR_NAME]`, `[YOUR_CONTACT_INFO]` — 2 fills | VERIFIED READY |
| LWV California Email | `domain-51-send-templates.md` — Email 2 | lwvc@lwvc.org (Jenny Farrell, Executive Director) | `[YOUR_NAME]`, `[YOUR_CONTACT_INFO]` — 2 fills | VERIFIED READY |
| Clean Money Action Fund Email | `domain-51-send-templates.md` — Email 3 | info@CAclean.org | `[YOUR_NAME]`, `[YOUR_CONTACT_INFO]` — 2 fills | VERIFIED READY |

**Total field fills across all 5 emails**: 10 fills (2 per email). Gist URL is pre-filled in all templates — no URL replacement needed.

---

## Section 3: Contact Validation (Wave 1 Core Contacts)

Contact validation completed June 5-6, 2026. Results:

### Campaign Legal Center

- **Adav Noti**: Confirmed Executive Director (not Policy Director — title correction in templates is accurate). Source: campaignlegal.org/update/adav-noti-named-executive-director — effective January 1, 2024.
- **Erin Chlopak**: Senior Director, Campaign Finance — email format confirmed (echlopak@campaignlegalcenter.org). Organization active, conducting enforcement complaints and redistricting defense work as of June 2026.
- **Contact status**: VERIFIED ACTIVE. CLC filed a redistricting enforcement comment June 2, 2026 and is actively monitoring the 2026 election cycle.

### Issue One

- **Nick Penniman**: Founder and CEO (Executive Director equivalent). Source: issueone.org/team/nick-penniman
- **Contact email**: info@issueone.org — general inbox, current.
- **Organization status**: ACTIVE. Issue One continues operating National Council on Election Integrity and ReFormers Caucus as of 2026.
- **Contact status**: VERIFIED ACTIVE. No leadership change since template creation.

### Common Cause California

- **Darius Kemp**: Executive Director, appointed June 2025. Jonathan Mehta Stein departed. Source: commoncause.org/california/
- **Email**: dkemp@commoncause.org (direct) or ca@commoncause.org (general inbox)
- **Campaign role**: Common Cause California is one of the three co-chairs of the Californians for Fair Elections ballot campaign committee. Source: commoncause.org/california/press (campaign launch February 2026).
- **Contact status**: VERIFIED ACTIVE — directly involved in the November 2026 ballot campaign this email references. High-value contact.

### League of Women Voters California

- **Jenny Farrell**: Executive Director, LWV California. Source: lwvc.org/about/staff (verified June 5, 2026 per send template notation).
- **Email**: lwvc@lwvc.org
- **Campaign role**: LWV California is a co-chair of Californians for Fair Elections. The template's mission alignment ("voter education") is confirmed accurate.
- **Contact status**: VERIFIED ACTIVE.

### Clean Money Action Fund

- **Email**: info@CAclean.org (verified June 5, 2026 via yesfairelections.org — cleanmoney.org domain unreachable, official campaign contact used)
- **Organization status**: Operating as "Californians for Fair Elections" campaign committee for the November 2026 ballot. The yesfairelections.org campaign site is active.
- **Contact status**: VERIFIED ACTIVE — campaign is live and actively organizing.

---

## Section 4: Gist URL Accessibility

| Gist | URL | Last Confirmed | Status |
|------|-----|----------------|--------|
| Domain 51 (Campaign Finance) | https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | June 2, 2026 (creation confirmation) | CONFIRMED LIVE — pre-filled in all 5 templates |

**Action required before sending**: Spot-check the Gist URL in a browser to confirm it loads without authentication. If it returns 404, re-creation template is in `domain-51-research-runbook.md`.

---

## Section 5: Contingency Responses

### Scenario A: Low Open Rate / No Response (7-day monitoring)

If Day 7 (June 17-18) shows no replies from CLC or Issue One:

- Do not re-send to the same contacts
- Proceed with Wave 2 CA sends (June 12-13) regardless
- At Day 14 (June 24-25): send a single brief follow-up to info@ inbox rather than direct contact — frame as "Did this reach your research team?" not a re-pitch
- Log in `DISTRIBUTION_EXECUTION_LOG.md`

### Scenario B: Reply Requesting More Information

- Direct to the Gist URL for full text
- If they ask for a specific policy area deep-dive, flag in WORKLOG.md — may trigger Domain H or K research prioritization
- Reply within 24 hours

### Scenario C: Reply With Critical Feedback on Constitutional Analysis

This is the highest-value response type. CLC in particular may have expert feedback on the Hawaii SB 2471 corporate charter theory.

- Capture the exact substance of the critique
- Create a file `domain-51-expert-feedback-[organization].md` with full text
- Flag in WORKLOG.md under "Phase 3 Research Inputs"

### Scenario D: Organization Actively Hostile / Requests No Further Contact

- Log in `DISTRIBUTION_EXECUTION_LOG.md` as "Opt-out"
- Do not contact again
- This is rare but documented as a contingency

### Scenario E: Gist URL Inaccessible at Time of Send

- Re-check GitHub authentication status
- If Gist is deleted: re-create using `domain-51-research-runbook.md` procedure (15 minutes)
- If GitHub is down: hold send for 2 hours and retry
- Do not send emails with a broken Gist URL — the URL is the primary call-to-action

---

## Section 6: Timeline

| Date | Action | Duration | Owner |
|------|--------|----------|-------|
| **June 7 (Fri)** | User review of this checklist + WAVE_1_NEWS_INTEGRATION.md | 15 min | User |
| **June 8 (Sat)** | Spot-check Domain 51 Gist URL accessibility. Confirm template fill fields (10 fills). | 10 min | User |
| **June 9 (Sun)** | Final staging: open `domain-51-send-templates.md`, fill `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` in Emails 4 and 5 only. Do not fill Wave 2 emails yet. | 10 min | User |
| **June 10 (Mon) 14:00 UTC** | Send Email 4 (CLC — Erin Chlopak). Send Email 5 (Issue One — info@). 30-45 min apart. | 30-45 min | User |
| **June 10 post-send** | Log sent date, subject line, and contact name in `DISTRIBUTION_EXECUTION_LOG.md` | 5 min | User |
| **June 12 (Wed) 14:00 UTC** | Fill `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` in Emails 1-3. Send Email 1 (Common Cause CA). Send Email 2 (LWV CA). Send Email 3 (Clean Money Action Fund). | 60-90 min | User |
| **June 12 post-send** | Log sent dates in `DISTRIBUTION_EXECUTION_LOG.md` | 5 min | User |
| **June 17-18** | Day 7 checkpoint — review for replies. Log engagement signals in measurement spreadsheet. | 20 min | User |

---

## Section 7: Post-Send Signal Tracking

After each send, track in the Phase 1 measurement spreadsheet:

- Email sent timestamp
- Contact name and organization
- Reply received (Y/N)
- Reply type (engagement / information request / critique / opt-out)
- Gist view count (check 48 hours post-send)

Day 7 checkpoint (June 17-18): compare against PHASE_1_IMPACT_EVALUATION_ROUTING.md thresholds for Domain 51 activation decisions.

---

*Checklist created June 6, 2026 (Session 2957). Wave 1 execution June 10 14:00 UTC. Contact validation current as of June 6, 2026.*
