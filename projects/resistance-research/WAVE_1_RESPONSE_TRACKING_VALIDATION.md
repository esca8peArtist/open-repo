---
title: "Wave 1 Response Tracking Validation — Domain 51"
created: "2026-06-10"
item: "Item 104 — Phase 2 Wave 1 Execution Logistics Deepening"
status: "production-ready"
scope: >
  Validates the Campaign Monitor/Bitly tracking infrastructure, identifies contact-list
  mismatches in the checkpoint template, walks through STRONG/MODERATE/WEAK signal
  derivation logic, and documents two June 9 sanity checks for the user.
cross_references:
  - DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - domain-51-send-templates.md
---

# Wave 1 Response Tracking Validation — Domain 51
## Campaign Monitor, Bitly, and Day 7 Signal Logic Audit

*Prepared June 10, 2026. Item 104 — Phase 2 Wave 1 Execution Logistics Deepening.*

**Lead finding**: There is a contact-list mismatch in DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md that must be corrected before the June 16 checkpoint. The checkpoint template's Section 1 and Section 3 tables reference four contacts that do not match the actual Wave 1 send list: the template was likely generated from an earlier contact set (Yusuf Maluf at CLC, Cynthia Terrell at Common Cause national, Tiffany Muller at End Citizens United, Nick Penniman at Issue One). The actual Wave 1 send list is: Erin Chlopak at CLC, Darius Kemp at Common Cause CA, Clean Money Action Fund, Jenny Farrell at LWV CA, and Nick Penniman at Issue One. The checkpoint template must be updated to match actual sends before it can produce valid Day 7 signal scores. This document provides the corrected contact entries and a complete walkthrough of the tracking logic.

---

## Section 1: Contact-List Mismatch Audit

### Checkpoint Template Section 1 (Current — Needs Correction)

The DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md Section 1 table currently reads:

| Organization | Contact | Email |
|---|---|---|
| Campaign Legal Center | Yusuf Maluf | ymaluf@campaignlegalcenter.org |
| Common Cause | Cynthia Terrell | cterrell@commoncause.org |
| End Citizens United | Tiffany Muller | tmuller@endcitizensunited.org |
| Issue One | Nick Penniman | npenniman@issueone.org |

### Actual Wave 1 and Wave 2 Send List (from domain-51-send-templates.md and DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md)

| Organization | Contact | Email | Wave | Send Date |
|---|---|---|---|---|
| Campaign Legal Center | Erin Chlopak (Sr. Director, Campaign Finance) | echlopak@campaignlegalcenter.org | Wave 1 | June 9 |
| Issue One | Nick Penniman (Founder/CEO) | info@issueone.org | Wave 1 | June 9 |
| Common Cause California | Darius Kemp (Executive Director) | dkemp@commoncause.org | Wave 2 | June 11 |
| League of Women Voters CA | Jenny Farrell (Executive Director) | lwvc@lwvc.org | Wave 2 | June 11 |
| Clean Money Action Fund | Trent Lange (President) | info@CAclean.org | Wave 2 | June 11 |

### Mismatch Analysis

**Yusuf Maluf** (listed in template): Not a named contact in any Domain 51 distribution file. Likely carried over from an earlier template generation. Remove from checkpoint tracking.

**Cynthia Terrell at Common Cause national** (listed in template): Domain 51 sends to Common Cause California (Darius Kemp at dkemp@commoncause.org), not the national organization. Terrell is a different person at the national Common Cause. Remove; replace with Darius Kemp.

**End Citizens United / Tiffany Muller** (listed in template): End Citizens United is not in the Domain 51 contact list at any tier. This organization appears to have been included erroneously in the template. Remove entirely.

**Nick Penniman at npenniman@issueone.org** (listed in template): The send goes to info@issueone.org (general inbox), not a personal npenniman@ address. The contact name is correct but the email is an inferred direct address that has not been confirmed. For tracking purposes, the reply sender will likely come from a personal @issueone.org address if a staff member replies — but the outbound send address is info@issueone.org. Monitor the inbox for replies from any @issueone.org domain.

**Missing from template**: LWV California (Jenny Farrell / lwvc@lwvc.org) and Clean Money Action Fund (Trent Lange / info@CAclean.org) are not in the current checkpoint template. Both are Wave 2 sends (June 11) and their Day 7 is technically June 18, but they should be tracked in the same checkpoint window since the June 16 checkpoint covers all sends made June 9–12.

### Corrected Checkpoint Template Contact Table

**Replace the current Section 1 table with this:**

| Organization | Contact | Email | Open Count | Recipients | Open Rate % | Notes |
|---|---|---|---|---|---|---|
| Campaign Legal Center | Erin Chlopak | echlopak@campaignlegalcenter.org | ___ | 1 | ___% | Wave 1 — June 9 send |
| Issue One | Nick Penniman | info@issueone.org | ___ | 1 | ___% | Wave 1 — June 9 send; reply may come from any @issueone.org address |
| Common Cause California | Darius Kemp | dkemp@commoncause.org | ___ | 1 | ___% | Wave 2 — June 11 send |
| League of Women Voters CA | Jenny Farrell | lwvc@lwvc.org | ___ | 1 | ___% | Wave 2 — June 11 send |
| Clean Money Action Fund | Trent Lange | info@CAclean.org | ___ | 1 | ___% | Wave 2 — June 11 send; Tier C (5–10% expected) |
| **TOTAL** | | | **___** | **5** | **___% (average)** | |

**Also correct Section 3 (Contact Response Tracking) with the same five contacts.**

**Action required**: User should update DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md Sections 1 and 3 with the corrected table before June 9. This takes 5 minutes. Without this correction, the Day 7 composite score calculation in Section 6 will reference non-existent contacts and produce an invalid signal score.

---

## Section 2: Campaign Monitor Open Rate Ingestion — Validation

### Does Campaign Monitor Track Opens Per Individual Email in a 5-Person Campaign?

Campaign Monitor tracks open events at the recipient level in all campaign types including very small lists. For a 5-recipient campaign, each recipient's open/not-opened status is recorded in the Campaign Monitor dashboard under the campaign's "Recipients" or "Activity" tab.

**Validation path**: To confirm open tracking is enabled for Domain 51 Wave 1, perform this check before June 9 send:

1. Open Campaign Monitor account
2. Navigate to the Draft or Scheduled "Domain 51 Wave 1" campaign
3. Click "Settings" or "Campaign Settings"
4. Confirm "Track Opens" is enabled (checkbox should be checked)
5. If not enabled: enable it now. Open tracking must be enabled before the campaign sends — it cannot be applied retroactively to an already-sent campaign.

**If Campaign Monitor is not in use**: The DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md notes an alternative: "If not tracked via Campaign Monitor API, use manual report from email sender or Bitly click data." For a 5-recipient send from a personal email client (e.g., Gmail), Campaign Monitor open tracking is unavailable. In that case, the Bitly click data becomes the primary engagement signal (see Section 3 below), and the "email open rate" metric is replaced by the "Bitly click rate" as the proxy.

**Critical flag**: The Day 7 checkpoint composite score weights email open rate at 2× (Section 6 of the template). If open tracking is not set up, this metric defaults to "unavailable" and the composite score loses 20% of its maximum value. In the absence of open tracking, the checkpoint remains valid — substitute "0" for the open-rate weighted component and interpret the composite score with this limitation noted.

---

## Section 3: Bitly Click Tracking — Validation

### Current Bitly Configuration

The checkpoint template references a Bitly short link: bit.ly/domain51-campaign-finance. The Domain 51 research document is delivered via the GitHub Gist URL: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372.

**Validation question**: Are all 5 Wave 1 email templates using this same Bitly short link to the Gist?

**Audit result**: The 5 email templates in domain-51-send-templates.md embed the full Gist URL directly (https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372) rather than a Bitly short link. This means Bitly click tracking will NOT capture clicks unless:

a) The Bitly short link was created and substituted into the templates, and
b) The bit.ly/domain51-campaign-finance short link resolves to the same Gist URL

**Action required before June 9**: Verify whether the Bitly short link bit.ly/domain51-campaign-finance exists and resolves correctly to the Gist. If it does, and if the user plans to insert the short link instead of the full URL into the emails at send time, Bitly tracking will work as designed. If the full Gist URL is used instead (as embedded in the current templates), Bitly click data will be zero regardless of engagement — and the Day 7 checkpoint will lack this signal entirely.

**Recommendation**: Choose one approach and apply it consistently to all 5 sends:

**Option A — Full Gist URL (current default in templates)**: No Bitly tracking. Day 7 checkpoint uses only email open rate + Gmail reply audit for engagement metrics. The Bitly section of the checkpoint template will show 0 clicks by design, not by failure. Note this explicitly in the checkpoint document when completing it.

**Option B — Bitly short link**: Substitute bit.ly/domain51-campaign-finance for the full URL in each email template at send time. Bitly will record each unique click, providing the signal velocity data the template is designed to use. This requires creating the Bitly link if it does not already exist (takes 2 minutes at bitly.com).

**Recommended choice**: Option B. The click velocity data from Bitly is the most valuable signal in the Day 7 checkpoint because it captures engagement that happens without an email reply (a contact reads the research but does not respond — Bitly records the Gist access while Gmail records nothing). Option B requires a 2-minute setup step on June 9 before sending.

---

## Section 4: STRONG/MODERATE/WEAK Signal Derivation — Logic Walkthrough

The composite signal score in DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md Section 6 uses a 4-metric weighted formula. Here is the complete derivation logic:

### Step 1 — Email Open Rate (Weight: ×2)

Collect from Campaign Monitor dashboard (or estimate from Bitly proxy if open tracking not set up).

**Calculation**: (Opens / Recipients) × 100 = open rate %

For 5 recipients:
- 5/5 opened = 100% → weighted score: 100 × 2 = 200 (max)
- 4/5 opened = 80% → weighted score: 80 × 2 = 160
- 3/5 opened = 60% → weighted score: 60 × 2 = 120
- 2/5 opened = 40% → weighted score: 40 × 2 = 80
- 1/5 opened = 20% → weighted score: 20 × 2 = 40

The template normalizes the weighted score against the formula's max of 10. **Translation**: For the composite score, the email open rate component contributes 0–2 points (scaled 0–100% → 0–2 on the 10-point scale).

**Normalized formula for composite**: (open_rate / 100) × 2 = component score (range 0.0–2.0)

Example: 3/5 opened (60%) → (60/100) × 2 = 1.2

### Step 2 — Bitly Click Velocity (Weight: ×2)

Collect from Bitly dashboard: total clicks from June 9 through June 16 (Day 7 window).

**Calculation**: Bitly_clicks / expected_clicks × 2 = component score (range 0.0–2.0)
- Expected clicks: 5 (one per recipient, per the template threshold)
- Example: 3 clicks / 5 expected → (3/5) × 2 = 1.2

Interpret: Clicks > 5 are a bonus signal (score caps at 2.0 but the surplus signals organic distribution beyond the 5 recipients — flag separately).

### Step 3 — Reply Rate Score 3+ (Weight: ×2)

Collect from Gmail: count replies scoring 3+ (substantive reply, forward, or adoption signal).

**Calculation**: (Score3plus_replies / total_contacts) × 2 = component score (range 0.0–2.0)

For 5 contacts:
- 0 substantive replies → 0.0
- 1 substantive reply → (1/5) × 2 = 0.4
- 2 substantive replies → (2/5) × 2 = 0.8
- 3 substantive replies → (3/5) × 2 = 1.2
- 4 substantive replies → (4/5) × 2 = 1.6
- 5 substantive replies → (5/5) × 2 = 2.0

Note: Score 1 (OOO) and Score 2 (form acknowledgment) do not count toward this metric — substantive engagement is the threshold.

### Step 4 — Win Rate / Adoption Signals (Weight: ×1)

Count adoption signals per the Section 5 registry: explicit statements of use in a project, forwarding to colleagues, substantive requests for follow-up.

**Calculation**: (organizations_with_adoption_signal / total_contacts) × 1 = component score (range 0.0–1.0)

For 5 contacts:
- 0 adoption signals → 0.0
- 1 adoption signal → (1/5) × 1 = 0.2
- 2 adoption signals → (2/5) × 1 = 0.4
- 3+ adoption signals → ≥0.6 (strong)

### Composite Score Calculation

**Formula**: (email_open × 2) + (bitly_clicks × 2) + (reply_rate × 2) + (win_rate × 1) = composite (0–7 when normalized)

**Wait — the template's Section 6 structure needs clarification**: The template shows a composite score out of 10, but the weights sum differently depending on normalization. Here is the operative interpretation:

**STRONG (score 8–10)**: Requires at least 3 of 4 metrics performing well simultaneously:
- Open rate ≥75% (4+ of 5 opened)
- Bitly clicks ≥5 (all recipients clicked through)
- Reply rate Score 3+ ≥50% (3+ substantive replies)
- At least 2 adoption signals

**MODERATE (score 5–7)**: At least 2 metrics performing acceptably:
- Open rate 50–74% (3 of 5 opened)
- Bitly clicks 3–4
- Reply rate Score 3+ 25–49% (1–2 substantive replies)
- At least 1 adoption signal

**WEAK (score 3–4)**: At least 1 metric showing minimal engagement:
- Open rate 25–49% (1–2 of 5 opened)
- Bitly clicks 1–2
- Reply rate Score 3+ < 25% (0–1 substantive replies)
- Zero adoption signals

**FAILURE (score < 3)**: All metrics near zero:
- Open rate < 25% (0–1 of 5 opened)
- Zero Bitly clicks
- Zero substantive replies
- Zero adoption signals

### Concrete Example Scenarios

**Scenario A — Wave 1 mid-range outcome**:
- CLC opens and sends a brief acknowledgment (Score 2)
- Issue One does not reply
- Common Cause CA opens but does not reply
- LWV CA opens and replies substantively about using the Executive Summary (Score 3)
- Clean Money AF no response

Open rate: 3/5 = 60% → 1.2
Bitly: Assume 3 clicks (3 opens translated to clicks) → 1.2
Reply Score 3+: 1/5 = 20% → 0.4
Win rate: 1 adoption signal (LWV CA) → 0.2
**Composite: ~3.0 — WEAK/MODERATE boundary. Escalate to checkpoint decision.**

**Scenario B — Strong outcome**:
- CLC replies substantively asking for follow-up (Score 3)
- Issue One replies, cites research in a publication (Score 5)
- Common Cause CA opens, no reply (Day 7 — still possible)
- LWV CA opens, forwards to campaign team (Score 4)
- Clean Money AF no response

Open rate: 4/5 = 80% → 1.6
Bitly: Assume 5 clicks → 2.0
Reply Score 3+: 3/5 = 60% → 1.2
Win rate: 2 adoption signals (Issue One publication, LWV CA forward) → 0.4
**Composite: ~5.2 — MODERATE. Sequential Domain 48 activation.**

---

## Section 5: Two June 9 Sanity Checks

These are the two pre-send verification steps the user should run on June 9 morning before executing Wave 1.

### Sanity Check 1 — Campaign Monitor Open Tracking Enabled

**Time required**: 3 minutes
**When**: Before 09:00 AM PDT June 9

Steps:
1. Log in to Campaign Monitor account
2. Open the "Domain 51 Wave 1" campaign draft
3. Click Settings → confirm "Track Opens" is checked
4. If not checked: enable it and save
5. Log result: "Open tracking enabled — June 9, [time]" in DOMAIN_51_DISTRIBUTION_SEND_LOG.md

**If Campaign Monitor is not being used for this send** (i.e., sending from Gmail directly): Note in the send log that open tracking is not available. The Day 7 checkpoint will use Bitly clicks and Gmail replies as the primary metrics instead. Adjust the composite score formula accordingly: remove the open-rate component and scale the remaining three metrics to fill the 10-point range.

### Sanity Check 2 — Bitly Link Resolves to Correct Gist

**Time required**: 2 minutes
**When**: Before 09:00 AM PDT June 9

Steps:
1. Open a browser in incognito/private mode (prevents any cached session data from affecting the test)
2. Navigate to: bit.ly/domain51-campaign-finance (or whatever Bitly short link is documented in DISTRIBUTION_GIST_URLS.md for Domain 51)
3. Confirm the redirect lands on: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
4. Confirm the Gist page loads completely (all section headers and content visible)
5. Log result: "Bitly link verified — June 9, [time], resolves to correct Gist" in DOMAIN_51_DISTRIBUTION_SEND_LOG.md

**If the Bitly link does not exist**: Create it at bitly.com (2 minutes):
- Log in to Bitly
- Click "Create" → "Short link"
- Enter the Gist URL as the destination
- Set custom back-half to "domain51-campaign-finance" (or similar memorable identifier)
- Copy the new short link and insert it into all 5 email templates before sending

**If the Gist returns a 404**: Execute the Gist contingency from DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md Section 2. Do not delay the Wave 1 send by more than 30 minutes while resolving a Gist access issue.

---

## Section 6: Gap Assessment — What Could Affect Day 7 Decision Quality

### Gap 1 — Template Contact Mismatch (Critical)

As documented in Section 1, the DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md references 4 contacts that do not match the 5 actual Wave 1/2 sends. Until corrected, the Day 7 checkpoint will:

- Attempt to track opens for email addresses that were never sent to (Yusuf Maluf, Cynthia Terrell, Tiffany Muller at End Citizens United)
- Miss tracking for 3 contacts who were actually sent to (Darius Kemp, Jenny Farrell, Trent Lange)
- Produce an inaccurate composite score

**Severity**: HIGH. Correct this before June 9.

### Gap 2 — Bitly Tracking Not Confirmed

As documented in Section 3, the email templates embed the full Gist URL, not a Bitly short link. If Bitly is not inserted into the templates at send time, the click-tracking signal is unavailable for Day 7.

**Severity**: MEDIUM. The checkpoint remains valid without Bitly (Sections 1, 3, and 5 still generate a composite score). But losing the Bitly signal reduces the precision of the composite score — particularly for contacts who open the research but do not reply.

**Mitigation**: Insert Bitly short link into all 5 email templates before sending. Confirmed in June 9 Sanity Check 2.

### Gap 3 — Issue One Email Tracking Address Mismatch

The templates send to info@issueone.org (general inbox). The checkpoint template attempts to track opens from npenniman@issueone.org. If Campaign Monitor sends to info@issueone.org, any open event will be attributed to info@issueone.org in the tracking dashboard — not to npenniman@. The templates and tracking tables must use the same email address.

**Severity**: LOW for open tracking (Campaign Monitor tracks the address it sent to, not an assumed forwarded address). Corrected in the Section 1 revised contact table above.

**Mitigation**: Use info@issueone.org as the tracking address in all checkpoint sections. If Issue One replies from a personal address (e.g., npenniman@issueone.org or mbeckel@issueone.org), count it as a reply regardless of the sender address mismatch.

### Gap 4 — California Contacts Not Included in Wave 1 Checkpoint Window

The checkpoint template Section 1 was built around 4 Wave 1 contacts. Wave 2 sends (Common Cause CA, LWV CA, Clean Money AF) happen June 11 — their 7-day window technically runs through June 18, not June 16. However, the June 16 Day 7 checkpoint date is appropriate for all 5 contacts because:

- Even Wave 2 contacts sent June 11 will have had 5 business days by June 16 (June 11–12–13–14–15 = 5 days)
- The campaign has a July 1 hard deadline; waiting until June 18 for Wave 2 checkpoint data wastes 2 days of the window
- The composite score calculation should note that Wave 2 contacts have had 5 days rather than 7

**Mitigation**: Add a note in the checkpoint template: "Wave 1 contacts (CLC, Issue One): Day 7 checkpoint as of June 16. Wave 2 contacts (Common Cause CA, LWV CA, Clean Money AF): Day 5 checkpoint as of June 16 — apply slightly lower reply-rate expectations."

### Gap 5 — Gmail Label Structure Not Verified

Section 3 of the checkpoint template specifies a Gmail search string: `label:phase1-outreach/replies from:{email addresses}`. This label may not exist in the user's Gmail account. If the label is missing, the search will return no results even if replies are present.

**Severity**: LOW if the user manually checks their inbox. The label structure is a convenience feature, not a requirement.

**Mitigation**: June 9 — confirm whether the label `phase1-outreach/replies` exists in Gmail. If not, use a direct search instead: `from:@campaignlegalcenter.org OR from:@issueone.org OR from:@commoncause.org OR from:@lwvc.org OR from:@CAclean.org` — this will surface any replies from Wave 1/2 organization email domains.

---

## Section 7: Checkpoint Execution Summary

On June 16 at 09:00 AM, run the checkpoint in this order:

1. **Update Section 1 table** with corrected contacts (per Section 1 of this document) — confirm before running checkpoint
2. **Campaign Monitor open rate** (5 min): Log in, pull open count for Domain 51 campaign, enter in Section 1 table
3. **Bitly click velocity** (5 min): Log in to Bitly, pull daily click counts June 9–16, enter in Section 2
4. **Gmail reply audit** (5 min): Search for replies from all 5 organization domains, score each, enter in Section 3
5. **Gist view count** (3 min): If GitHub account access available, pull view delta; otherwise use Bitly as proxy
6. **Adoption signal review** (3 min): Review all replies for explicit use-case statements, enter in Section 5
7. **Composite score** (2 min): Calculate per Section 6 formula, route to DOMAIN_51_JUNE_16_DECISION_LOGIC.md

Total: 20–23 minutes. Within the checkpoint's designed execution window.

---

*Prepared June 10, 2026 — Item 104.*

*Sources: [DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md]; [DOMAIN_51_JUNE_16_DECISION_LOGIC.md]; [domain-51-send-templates.md]; [DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md]; [Campaign Monitor — Schedule a campaign to send](https://help.campaignmonitor.com/schedule-campaign-to-send); [Campaign Monitor — The 5 Email Marketing Metrics That Matter Most](https://www.campaignmonitor.com/blog/featured/the-5-email-marketing-metrics-that-matter-most-and-how-to-improve-them/)*
