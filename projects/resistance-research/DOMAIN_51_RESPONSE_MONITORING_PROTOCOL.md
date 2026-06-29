---
title: "Domain 51 — Wave 1-2 Response Monitoring Protocol"
created: "2026-06-29"
status: "production-ready"
scope: "Post-send monitoring for Wave 1 (CLC, Issue One) and Wave 2 (Common Cause CA, LWV CA, Clean Money Action Fund)"
t7_checkpoint: "T+7 from actual send date (expected July 6 if sends execute June 29)"
gist_url: "https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372"
companion_files:
  - DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md
  - DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md
  - DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
  - PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md
---

# Domain 51 — Wave 1-2 Response Monitoring Protocol

**June 29, 2026 — Active monitoring begins immediately after first send.**

This protocol covers the five Wave 1-2 contacts (Campaign Legal Center, Issue One, Common Cause California, LWV California, Clean Money Action Fund). It specifies what to check, when to check it, how to classify what you find, and what actions each classification triggers. The protocol operates in parallel with normal email use — no dedicated monitoring sessions are required until the T+7 checkpoint.

---

## Section 1 — Email Open Tracking

Domain 51 sends are plain-text emails from a personal Gmail account. Gmail does not provide read receipts or open tracking. Two proxies serve as open indicators.

### 1.1 Bitly Click Rate as Open Proxy

Before sending any Wave 1-2 email, shorten the Gist URL at bitly.com. Create one short link and use it in all five emails:

**Gist URL**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

**Bitly setup** (one-time, 3 minutes):
1. Log in to bitly.com (free account is sufficient)
2. Click "Create new" → paste the Gist URL
3. Set custom back-half to `d51-research` (example: bit.ly/d51-research)
4. Save. Copy the short link. Replace the Gist URL in every email template with this short link before sending.

**Reading click data**:
- Log in to bitly.com → click your link → select "Clicks" tab → set date range to "Last 14 days"
- Check weekly (not daily — daily granularity is not useful until a spike appears)
- Bitly shows click count by date. A click within 72 hours of a specific send is strong evidence the recipient (or a colleague they forwarded to) opened the email

**Spike rule**: 3+ clicks in a single day = the link was forwarded to a group, not just read by one individual. Cross-reference the spike date against your send dates in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md.

**Limitation**: Bitly clicks tell you the link was accessed, not who accessed it. A click from an organization confirms delivery and interest but cannot distinguish between the named contact and a colleague they forwarded to. Treat Bitly clicks as MODERATE-level confirmation unless paired with a direct reply.

### 1.2 Gmail Audit Trail

After sending each email, immediately copy the sent timestamp from Gmail to DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md. This is the baseline record. Check these two additional signals within Gmail:

**Bounce detection**: Within 2 hours of each send, check your inbox for a Mail Delivery Failure notice from Google or the recipient's mail server. A hard bounce from any of the five addresses requires immediate action (see Section 5, Contingency Routing). If no bounce arrives within 2 hours, treat delivery as confirmed.

**Reply thread**: All replies land in your inbox as threads to the original email. Gmail's default view makes this easy to identify. No filtering setup required.

### 1.3 Manual Open Log

In DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md Sheet 1 (Daily Signal Log), log each Bitly click event as an event row with Event_Type = GIST_CLICK and Signal_Code = MODERATE. This creates a timestamped record that feeds the open rate calculation in Sheet 5 even when no direct reply has been received.

---

## Section 2 — Click Tracking via Bitly

The Bitly link serves a dual function: it tracks clicks as an open proxy and it is the reader's only path to the research document. Keep the Bitly link consistent across all five Wave 1-2 emails so aggregate click data reflects interest from the full recipient pool.

**Weekly monitoring procedure** (5 minutes):
1. Open bitly.com
2. Click the d51-research link → Clicks tab → Last 14 days
3. Note total clicks and identify any single-day spikes
4. Enter the week's click count in Sheet 2 of DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md (Gist_Clicks_Week1 column for Days 1-7; Gist_Clicks_Week2 for Days 8-14)
5. If a spike occurred, note the date and the contact whose send preceded it by 24-72 hours

**Attribution rule**: If CLC is sent June 29 and a 4-click spike appears June 30, attribute the clicks to CLC in Sheet 2. If a spike appears 5+ days after all sends with no clear attribution, log it as "Unknown / forwarded" in the Notes column.

**Threshold**: The research has five recipients. A total click count above 5 within 14 days indicates either multiple readings by individuals, forwarding to colleagues, or both. Above 10 total clicks is a strong forward signal warranting a note in CHECKIN.md.

---

## Section 3 — Escalation Signal Detection

### 3.1 Reply Pattern Detection

Check your inbox at the following intervals — not continuously:

| When | What to check | Time required |
|------|--------------|---------------|
| Day 1 (send day) | Bounce detection only | 1 minute |
| Day 3 | First reply scan (search for @campaignlegalcenter.org, @issueone.org, @commoncause.org, @lwvc.org, @CAclean.org) | 2 minutes |
| T+7 (7 days after send) | Full reply assessment + T+7 checkpoint decision | 15 minutes |
| T+14 | Late reply catch; final pre-Wave 3 assessment | 10 minutes |

**Gmail search strings to use at each check** (copy and paste into Gmail search):

```
from:(@campaignlegalcenter.org OR @issueone.org OR @commoncause.org OR @lwvc.org OR @CAclean.org)
```

This surfaces all replies from the five recipient domains, including replies from staff members other than the named contact (indicating internal routing).

### 3.2 Forward Detection

Direct forward detection is not possible without read-receipt tools. Infer forwarding from two signals:

1. **Bitly spike**: A cluster of clicks 24-72 hours after a send, especially 3+ clicks in one day, indicates the link was shared within an organization
2. **Reply from a different staff member**: If someone at CLC other than Erin Chlopak replies (e.g., from the general info@campaignlegal.org address or from another @campaignlegalcenter.org address), the email was internally routed. This is an escalation indicator — log as MODERATE at minimum, and upgrade to STRONG if the replying staff member is senior (Director-level or above)

When a reply arrives from a name not on your contact list but from the correct domain, log it in Sheet 1 with the actual sender name in Column F (Contact_Name) and add a note: "Internally routed from [original contact]."

### 3.3 Out-of-Office Handling

An out-of-office (OOO) reply is an automated confirmation that your email reached a live inbox and has not bounced. Extract the following from OOO replies:

- **Return date**: Note when the named contact returns. If the return date falls before your T+14 checkpoint, that contact's T+7 assessment remains open
- **Alternate contact named**: If the OOO message names a specific colleague to contact in their absence, that person becomes a Wave 3 follow-up target. Log the alternate contact's name and email in Sheet 1 Column H (Notes)
- **OOO signal classification**: Log OOO replies as MODERATE (delivery confirmed; named contact will see the email on return)

---

## Section 4 — Reply Categorization Framework

Every reply falls into exactly one of four categories. Classify within 24 hours of receipt and log in Sheet 1.

### STRONG — Escalation Activated

**Definition**: A named staff member at the organization engages with the substantive content of the research. The threshold is low: even one sentence of specific content engagement qualifies.

**What this looks like across the five contacts**:

- **CLC (Erin Chlopak)**: Any reply from Chlopak or another @campaignlegalcenter.org address that references the Hawaii/Montana charter theory, Citizens United, FEC enforcement, or campaign finance reform specifically. A request to discuss, a question about the research, or a mention that it has been shared with a colleague all qualify.
- **Issue One**: Any reply from an @issueone.org address that references FEC reform, the DISCLOSE Act, state ballot measures, or the ReFormers Caucus. A reply from Cory Combs (media contact: ccombs@issueone.org) indicating internal routing qualifies.
- **Common Cause CA (Darius Kemp)**: Any reply referencing the California Fair Elections Act, Citizens United, or the Section 6.3 charter theory. A reply from info@commoncause.org (national routing) indicating the California office received the email and engaged also qualifies.
- **LWV CA (Jenny Farrell)**: Any reply referencing the ballot measure campaign or California campaign finance reform. Even a "Thank you, we will review" from a named staff member at lwvc.org qualifies.
- **Clean Money Action Fund**: Any reply from @CAclean.org or Trent Lange directly. Given their small staff and active campaign posture, any non-automated reply from this org qualifies as STRONG.

**Immediate action on STRONG**: Reply within 24 hours. Offer either (a) a one-page summary they can share internally or (b) a brief conversation on the Hawaii/Montana constitutional theory. Log the reply in Sheet 1 and update the Signal_Code column for that organization's SEND row to STRONG.

### MODERATE — Continue Monitoring

**Definition**: An automated acknowledgment that names a specific staff member or confirms routing to a team, OR an OOO reply with a return date, OR a Bitly click spike attributable to this organization without a direct reply.

**Examples**: "Thank you for reaching out, I've shared this with our policy team." Generic automated replies that include the organization's name but no content engagement. OOO from Darius Kemp that names his return date.

**Action on MODERATE**: No immediate reply needed. Continue to T+7 or T+14. If a MODERATE signal arrives from an org, that org has not dropped off — the assessment window remains open.

### COLD — No Action Required

**Definition**: No reply, no Bitly click attributable to this org, no bounce. The email was delivered but has not produced any observable signal. This is normal for 40-60% of cold policy outreach in the first 7 days.

**Action on COLD**: None until T+7. At T+7, reassess whether to hold for T+14 or activate a follow-up. See DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md for the T+7 decision logic.

### SPAM / BOUNCE — Contingency Required

**Definition**: A hard bounce (Mail Delivery Failure from the mail server) or a reply categorized as spam (e.g., a generic "This email address is not monitored" auto-reply with no staff routing).

**Action on BOUNCE**: Within 24 hours. Check the bounce reason. If it is a "User Unknown" or "No such address" error, the contact email is dead. Consult DOMAIN_51_CONTACT_REACHABILITY_SNAPSHOT.md for the backup address. Attempt the backup address within 24 hours and log the resend in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md.

**Known backup addresses**:
- CLC: info@campaignlegal.org (if echlopak@campaignlegalcenter.org bounces)
- Common Cause CA: ca@commoncause.org (if dkemp@commoncause.org bounces)
- Clean Money Action Fund: Trent.Lange@CAclean.org (if info@CAclean.org bounces)

---

## Section 5 — Monitoring Calendar

Calculate your actual monitoring dates from the Wave 1 send date. Fill in the blanks:

| Checkpoint | Days After Send | Calendar Date (if sent June 29) | Action |
|-----------|----------------|--------------------------------|--------|
| Bounce check | 0 (same day) | June 29 | Check inbox for Mail Delivery Failure |
| Day 3 | 3 | July 2 | First reply scan; classify any received replies |
| T+7 (primary gate) | 7 | July 6 | Full checkpoint — run DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md |
| T+14 (secondary gate) | 14 | July 13 | Late reply assessment; final pre-Wave 3 decision if T+7 was inconclusive |
| T+30 (full assessment) | 30 | July 29 | Total engagement count; compare to expected metrics; note for PHASE_2_BATCH_SEQUENCING |

**Congressional calendar overlay**: Congress returns July 11 from the June 29-July 10 State Work Period recess. Policy organizations staffed by Hill-adjacent contacts (CLC, Issue One, Brennan Center) may have reduced response bandwidth through July 4-10. T+7 falls on July 6, which is within the holiday/recess window. If T+7 response signal is weak, do not immediately conclude low interest — hold to T+14 before triggering the low-response contingency.

---

## Section 6 — Integration with Existing Infrastructure

This protocol feeds directly into:

- **DOMAIN_51_IMPACT_DASHBOARD_TEMPLATE.md**: Every reply, click, OOO, and bounce logged here updates the formula-driven metrics in that dashboard
- **DOMAIN_51_WAVE_2_ACTIVATION_DECISION_TREE.md**: The T+7 checkpoint reads the STRONG/MODERATE/COLD/SPAM counts from this log to determine Wave 2 and Wave 3 activation
- **PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md**: If sends slip past June 30, the Success Path section in that file uses the same monitoring protocol; Branch A-C contingencies do not change the monitoring categories, only the timing of checkpoints
- **DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md**: This file is the source of send dates used to compute T+7 and T+14 calendar dates

Do not create additional tracking documents. All response events are logged in Sheet 1 of the dashboard. The execution log records send events only (timestamps, confirmed delivery, bounce status).

---

*Produced June 29, 2026. Active monitoring begins immediately after first Wave 1 send. No further setup required.*
