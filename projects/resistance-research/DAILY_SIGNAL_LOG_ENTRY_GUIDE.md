---
title: "Daily Signal Log Entry Guide — Domain 51 Wave 1"
subtitle: "Decision Tree for Translating Contact Responses into Signal Codes"
created: "2026-06-05"
updated: "2026-06-14"
version: 2.0
status: production-ready
wave_1_execution: "June 14-15, 2026 (execute immediately)"
t7_checkpoint: "June 17-18 (earliest) or June 21-22 (standard T+7 after June 14-15 send)"
cross_references:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - T7_CHECKPOINT_DECISION_AUTOMATION.md
---

# Daily Signal Log Entry Guide
## Translating Wave 1 Responses into Signal Codes

*Updated June 14, 2026. Wave 1-2 emails have not yet been sent as of today. This guide answers one question: when something happens with a contact, which Signal_Code do I enter in Sheet 1 of the measurement dashboard? The guide has been updated to reflect the June 14 execution state and June 17-18 / June 21-22 T+7 checkpoint window. Any person filling in the log should reach the same conclusion for the same event. No ambiguity.*

---

## Situation as of June 14, 2026

Wave 1 (CLC + Issue One) and Wave 2 (Common Cause CA, LWV CA, Clean Money) have not been sent. The task is to send them as soon as possible. If both waves execute June 14-15:

- T+3 checkpoint: June 17-18 (delivery confirmation)
- T+7 checkpoint: June 21-22 (Phase 2 gate decision)
- No-response waiting periods: adjusted from the original June 16 / June 20 / June 24 dates to reflect the actual send date

The June 17-18 date in the task specification functions as the calendar-fixed earliest checkpoint regardless of send date. If data is sparse at June 17-18 (because sends only went out June 14-15), treat June 17-18 as a T+3 delivery confirmation check and June 21-22 as the actual T+7 gate.

---

## Signal Code Definitions

**STRONG**: The organization is actively engaging with the research in a way that suggests it will influence their work. Not just "they read it" — they responded, forwarded, requested follow-up, or committed to action. STRONG signals count toward the T+7 gate threshold.

**MODERATE**: The organization received the research and responded positively but has not committed to any specific use. They are interested but non-committal. Routing to the right person counts as MODERATE. MODERATE signals do not count toward the T+7 gate threshold — see T7_CHECKPOINT_DECISION_AUTOMATION.md for rationale.

**WEAK**: No substantive engagement. Non-response after the waiting period, polite decline, auto-reply only, or bounced email.

**PENDING**: Default code for every SEND row. Not a signal — it is a placeholder. Replace with STRONG / MODERATE / WEAK when an outcome is known.

**N/A**: Used for informational NOTE rows only (e.g., "Gist URL confirmed accessible June 14"). Not a signal.

---

## Master Decision Tree

Run through this tree top-to-bottom for every event. Stop at the first matching branch.

```
EVENT RECEIVED
    |
    +-- BOUNCE (mailer-daemon reply or delivery failure notification)
    |       |
    |       `--> Signal_Code: WEAK
    |            Event_Type: BOUNCE
    |            Notes: Enter bounce error code; flag in Contingency Trigger Log (Sheet 6)
    |            Immediate action: Re-send to backup address (see per-org backup list below)
    |
    +-- AUTO-REPLY ONLY (out-of-office or generic acknowledgment, no human content)
    |       |
    |       +-- OOO names a specific alternate contact or direct phone number
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: OOO
    |       |            Notes: "OOO; alternate [Name] identified — follow up after [return date]"
    |       |            Action: Calendar reminder to follow up after stated return date
    |       |
    |       `-- OOO with no alternate contact, or generic "thanks for contacting us"
    |               `--> Signal_Code: WEAK
    |                    Event_Type: OOO
    |                    Notes: "Generic OOO; no routing upgrade"
    |
    +-- HUMAN REPLY RECEIVED
    |       |
    |       +-- Reply contains ANY of these (STRONG indicators):
    |       |   - Explicit organizational commitment ("we will use this in...")
    |       |   - Forward to colleagues mentioned explicitly ("sharing with our research team")
    |       |   - Request for follow-up meeting or call
    |       |   - Request to adapt or republish the research
    |       |   - Cites the research in a question (shows they read it substantively)
    |       |   - Provides substantive counterpoint or addition (engagement, not dismissal)
    |       |   - Mentions active litigation, pending legislation, or campaign use case
    |       |   - Requests sourcing for specific data points (implies intent to use)
    |       |       `--> Signal_Code: STRONG
    |       |            Event_Type: REPLY
    |       |            Notes: Quote the key phrase that indicates STRONG; include contact name
    |       |
    |       +-- Reply contains ANY of these (MODERATE indicators):
    |       |   - Positive acknowledgment without commitment ("thank you, very interesting")
    |       |   - Routing to another staff member without explicit use statement
    |       |   - Request for more information about the research itself
    |       |   - General expression of alignment ("we care about this issue")
    |       |   - OOO from a named decision-maker with named alternate contact
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: REPLY
    |       |            Notes: Note what specific phrase made this MODERATE not STRONG
    |       |
    |       `-- Reply contains ANY of these (WEAK indicators):
    |           - Polite decline ("not currently our focus")
    |           - Request to be removed from correspondence
    |           - Response makes clear research is not relevant to their current work
    |               `--> Signal_Code: WEAK
    |                    Event_Type: REPLY
    |                    Notes: Note reason for WEAK classification; do not re-contact
    |
    +-- GIST CLICK DETECTED (via Bitly dashboard spike)
    |       |
    |       +-- Click within 48h of send AND from a timing pattern consistent with org geography
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: GIST_CLICK
    |       |            Notes: "Bitly click detected [X] hours post-send; probable [org name] reader"
    |       |
    |       `-- Click cannot be attributed to specific org (traffic spike with no send correlation)
    |               `--> Signal_Code: MODERATE (log anyway — counts toward total engagement)
    |                    Event_Type: GIST_CLICK
    |                    Notes: "Unattributed Gist view spike; possible organic amplification"
    |
    +-- NO RESPONSE after waiting period (see per-org waiting periods below)
    |       `--> Signal_Code: WEAK
    |            Event_Type: NOTE
    |            Notes: "No response at [X] days post-send; marking WEAK at this checkpoint"
    |
    `-- SEND LOGGED (initial outreach)
            `--> Signal_Code: PENDING
                 Event_Type: SEND
                 Notes: "Template [Email X] sent to [address] at [UTC time]"
```

---

## No-Response Waiting Periods by Organization

Do not mark WEAK before the waiting period has elapsed. The waiting periods below assume a June 14-15 send date. Adjust if actual send date differs.

| Organization | Tier | Send Date | Mark WEAK After | Adjusted Deadline | Rationale |
|---|---|---|---|---|---|
| CLC | A | June 14-15 | 5 business days | June 21 | DC policy organizations respond within 5 days if they will respond at all |
| Issue One | A | June 14-15 | 5 business days | June 21 | Same rationale as CLC |
| Common Cause CA | B | June 14-15 | 7 business days | June 23 | Campaign mode — allow a full week for inbox attention |
| LWV CA | B | June 14-15 | 7 business days | June 23 | Same as Common Cause CA |
| Clean Money | C | June 14-15 | 9 business days | June 25 | Tier C lowest expected rate; allow maximum patience |

**Rule**: If a checkpoint arrives before the waiting period has elapsed, mark PENDING at the checkpoint (not WEAK). PENDING counts as zero signal at that checkpoint but preserves the upgrade possibility. Mark WEAK only after the waiting period has definitively elapsed with no response.

**T+7 rule for Tier B/C organizations**: If the T+7 checkpoint falls before Common Cause CA's or LWV CA's waiting period has elapsed, their status is PENDING at T+7. The T+7 STRONG signal count in Sheet 5 (cell B4) is calculated from confirmed STRONG signals only — PENDING rows do not contribute.

---

## STRONG Signal Evidence Thresholds

What separates STRONG from MODERATE is evidence of organizational intent, not just individual interest. Use these evidence thresholds:

**STRONG requires at least ONE of**:
- Named forwarding action ("I'm forwarding this to [Name] / our [team/committee/director]")
- Specific use case identified ("this is relevant to [specific project/litigation/campaign]")
- Meeting or call request
- Request to adapt, cite, or republish
- Mention of current litigation, pending legislation, or campaign where research applies
- Requesting sourcing for a specific data point (implies verification for use)
- Any staff member other than the primary contact engaging (implies internal circulation)

**MODERATE requires at least ONE of**:
- Human reply with positive tone but no specific use case
- Generic routing ("forwarding to our team")
- OOO with named alternate
- Gist click within 48h of send
- Request for more information about the research (not about a specific use)

**A reply is STRONG even if the contact doesn't explicitly say "we will use this"** — if they demonstrate they read it substantively (referencing specific data, asking about methodology, connecting it to their active work), that is STRONG. The test is: does this reply suggest they found it actionable?

---

## Per-Organization Signal Criteria

### Campaign Legal Center (CLC) — Tier A

**Primary contact**: Erin Chlopak, Senior Director for Campaign Finance Policy
**Send address**: echlopak@campaignlegalcenter.org (backup: info@campaignlegal.org)

**What counts as STRONG for CLC**:
CLC litigates FEC enforcement cases and campaign finance reform directly. STRONG signals reflect research utility to their litigation docket or policy advocacy:

- Chlopak or any CLC staff responds with any substantive content — even one sentence about FEC enforcement shutdown or AI PAC analysis
- Reply from any CLC researcher or litigator identifying specific utility ("we're citing this in a brief")
- Forward to CLC communications team (implies potential publication amplification)
- Request to speak with the research author
- Any reply referencing active litigation — even tangentially ("this may be relevant to our pending case") — escalate to STRONG regardless of other content
- Gist view spike + reply from a CLC email domain within 72 hours (two-signal confirmation)

**Example — STRONG**: "Chlopak responds: 'Thank you — your 200-day FEC enforcement shutdown data aligns with our pending litigation. Sharing with our enforcement team. Can I put you in touch with our press contact?'" Forward confirmed, litigation link, media escalation. Clear STRONG.

**Example — STRONG**: "Chlopak responds: 'Your AI PAC analysis is new to us. We've been tracking OpenAI but hadn't seen the Anthropic formation data. Our research team will review.'" Internal review commitment with substantive engagement. STRONG.

**Example — MODERATE**: "CLC info@ responds: 'Thank you for sharing this important research. I've forwarded to our policy team.'" Positive but no named recipient, no use case. MODERATE.

**What counts as WEAK for CLC**:
- No response by June 21 (5 business days after June 14 send)
- Generic organizational form response with no routing to a named person
- Bounce from echlopak@campaignlegalcenter.org (re-send immediately to info@campaignlegal.org; log in Contingency Trigger Log)
- Reply stating research is outside their current focus

---

### Issue One — Tier A

**Primary contact**: Nick Penniman, CEO / Founder
**Send address**: info@issueone.org

**What counts as STRONG for Issue One**:
Issue One's identity is built around bipartisan campaign finance reform narrative and their ReFormers Caucus (former elected officials). STRONG signals reflect research utility to their advocacy communications, policy work, or ReFormers network:

- Penniman or any named Issue One staff responds with substantive engagement
- Reply mentions sharing the AI PAC analysis as novel data ("we hadn't seen the Anthropic PAC formation data")
- Forward to Issue One's ReFormers Caucus contacts (former elected officials — network multiplier)
- Request to cite the research in an Issue One publication or report
- Reply indicating research will be used in Congressional testimony preparation
- Any reference to specific legislation, reform bills, or campaign where research applies

**Example — STRONG**: "Issue One staff: 'Your enforcement deadlock analysis is consistent with what we've documented in our Strengthening the Rules series. Sharing with Nick [Penniman] and our policy director. Would you be open to a brief call?'" Named forwarding, call request, series connection. Clear STRONG.

**Example — STRONG**: "Penniman: 'Our research team is reviewing your AI PAC section. The Anthropic formation data wasn't on our radar. Can you share your sourcing?'" Sourcing request = intent to verify for use. STRONG.

**Example — MODERATE**: "Issue One info@ responds: 'I've forwarded to our research team.' No specific content." Routing without substance. MODERATE.

**What counts as WEAK for Issue One**:
- No response by June 21 (5 business days after June 14 send)
- Bounce from info@issueone.org (no backup address available — log and note)
- Generic form acknowledgment with no routing to a named person

---

### Common Cause California — Tier B

**Primary contact**: Darius Kemp, Executive Director
**Send address**: dkemp@commoncause.org (backup: ca@commoncause.org)

**Decision-maker note**: Kemp's attention is currently on "Californians for Fair Elections" ballot campaign operations — signature collection, donor outreach, coalition coordination. Research that advances the ballot campaign directly (not general policy research) receives faster attention. Frame relevance to the California ballot campaign in any follow-up.

**What counts as STRONG for Common Cause CA**:

- Kemp or any named Common Cause CA staff connects research explicitly to ballot campaign ("this FEC analysis could support our July press push")
- Forward to "Californians for Fair Elections" coalition partners (Clean Money Action Fund, LWV CA)
- Request to incorporate research into voter guide or campaign materials
- Request for a meeting or call with the research author before July 1 CA messaging deadline
- Response from national Common Cause that routes to California ballot campaign team

**Example — STRONG**: "Kemp: 'The Hawaii SB 2471 angle is exactly what we need for our messaging on out-of-state dark money. Can I share this with our coalition partners? We're finalizing our July strategy.'" Campaign utility identified, explicit forward request, named use case. STRONG.

**Example — STRONG**: "CA staff: 'This is being circulated at our coalition meeting on June 20. We'll report back on whether the group wants to incorporate it into voter education materials.'" Coalition circulation with evaluation intent. STRONG.

**Example — MODERATE**: "Reply acknowledging receipt: 'Very relevant to our work — I'll make sure the team sees it.'" Positive but non-committal. MODERATE.

**Special rule — coalition forward as network multiplier**: If Common Cause CA forwards to a "Californians for Fair Elections" coalition member and that member contacts you independently, log as a new STRONG row with Organization: Common Cause CA and Notes: "Coalition forward — [responding org name]. Network multiplier event."

**What counts as WEAK for Common Cause CA**:
- No response by June 23 (7 business days after June 14 send)
- Bounce from dkemp@commoncause.org (re-try ca@commoncause.org; log)
- Reply stating organization is too focused on campaign execution to engage external research

---

### League of Women Voters California — Tier B

**Primary contact**: Jenny Farrell, Executive Director
**Send address**: lwvc@lwvc.org

**Use case note**: LWV's primary utility for this research is voter education materials, not litigation or policy advocacy. The Executive Summary of Domain 51 is the most immediately usable component because it is excerptable into voter guides. Frame follow-up around voter education if initial reply is non-committal.

**What counts as STRONG for LWV CA**:

- Farrell or named LWV staff explicitly mentions voter guide, member education, or voter education use case
- Forward to LWV National (lwv.org) or to California chapter voter services committee
- Request to excerpt the Executive Summary for an LWV publication
- Reply mentioning research will be shared at an LWV member meeting or chapter convening
- Request for a simplified or shorter version for member distribution

**Example — STRONG**: "Farrell: 'Your Executive Summary is exactly the format we use in voter guides. Forwarding to our Voter Services Committee to discuss including this in our June voter education packet.'" Specific use case, named committee, forwarding action. STRONG.

**Example — STRONG**: "LWV CA program staff: 'This aligns with our ballot measure education priorities. Can we discuss incorporating this into chapter briefings before the July 1 distribution window?'" Distribution window awareness + meeting request. STRONG.

**Example — MODERATE**: "General acknowledgment: 'Thank you for sharing — the League values this work.'" Positive but no specifics. MODERATE.

**What counts as WEAK for LWV CA**:
- No response by June 23 (7 business days after June 14 send)
- Bounce from lwvc@lwvc.org
- Reply that research is not relevant to current member education priorities

---

### Clean Money Action Fund — Tier C

**Primary contact**: Trent Lange, President
**Send address**: info@CAclean.org (verify at yesfairelections.org day-of send)

**Base rate note**: Clean Money's realistic response distribution has essentially two outcomes — STRONG (any substantive reply, given the Tier C 5-10% base rate) or WEAK (no response). The MODERATE band is narrow. Trent Lange has held the President role since 2009. The organization is in active ballot campaign execution. Their primary activity is signature collection and donor outreach, not external research engagement. Any human engagement with research content is a positive outlier.

**What counts as STRONG for Clean Money**:
Given Tier C base rates, any substantive human reply is STRONG. The bar is deliberately low:

- Any human reply from info@CAclean.org that is not a form response, generic OOO, or decline
- Trent Lange personally responds (named individual engagement)
- Any staff member engages with any part of the research content
- Forward to "Californians for Fair Elections" coalition coordinator

**Example — STRONG**: "Lange: 'Thanks — the AI PAC section is something we've been trying to explain to donors. Can we reference this in our fundraising materials?'" Any substantive content engagement counts. STRONG.

**Example — STRONG**: "Staff: 'We're sharing this with our campaign communications director. The Hawaii SB 2471 model is directly relevant to our messaging.'" Named recipient, specific utility. STRONG.

**What counts as MODERATE for Clean Money** (narrow band):
- Auto-reply naming a specific staff contact ("For press inquiries, contact [Name]")
- Reply forwarding to campaign communications without specific content engagement

**What counts as WEAK for Clean Money**:
- No response by June 25 (9 business days after June 14 send)
- Bounce from info@CAclean.org — log "verification required"; do not delay other sends; verify at yesfairelections.org on June 16 or later
- Generic form acknowledgment with no routing to named person
- Polite decline citing campaign capacity constraints

---

## Signal Code Upgrade Rules

Once a Signal_Code is set, do not edit the original row. If a contact escalates after an initial weak signal, add a NEW row:

**Scenario A**: CLC is logged as WEAK on June 21 (no response by T+5). On June 23, Chlopak replies with substantive engagement.
**Action**: Add new row — Date: 06/23/2026, Org: CLC, Signal_Code: STRONG, Event_Type: REPLY, Notes: "Late reply post-T+7; STRONG; upgrades CLC status to Confirmed for T+14 assessment."
**Dashboard effect**: Sheet 3 formula picks up STRONG automatically. CLC Status changes from "Pass" to "Confirmed." Sheet 5 B4 (STRONG count) increases. Annotate the T+7 checkpoint row in Sheet 4 Column K: "CLC was WEAK at T+7 assessment; upgraded to STRONG by June 23 reply — see T+14 checkpoint."

**Scenario B**: Common Cause CA is MODERATE on June 17 (OOO with named contact Sarah Morris). On June 24, follow-up to Morris produces a substantive reply.
**Action**: Add new row — Date: 06/24/2026, Org: Common Cause CA, Signal_Code: STRONG, Event_Type: REPLY.

---

## Realistic Signal Distribution Scenarios

These three scenarios illustrate what the Daily Signal Log looks like at T+7 and how they route.

### Scenario 1: STRONG outcome (B4 = 4 or 5)

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Notes |
|------|---|---|---|---|---|---|
| 06/14 | CLC | A | SEND | PENDING | Erin Chlopak | Email 4 sent |
| 06/14 | Issue One | A | SEND | PENDING | Nick Penniman | Email 5 sent |
| 06/15 | Common Cause CA | B | SEND | PENDING | Darius Kemp | Email 1 sent |
| 06/15 | LWV CA | B | SEND | PENDING | Jenny Farrell | Email 2 sent |
| 06/15 | Clean Money | C | SEND | PENDING | Trent Lange | Email 3 sent |
| 06/14 | CLC | A | GIST_CLICK | MODERATE | Unknown | 4 Bitly clicks within 24h of CLC send |
| 06/15 | Issue One | A | REPLY | STRONG | Nick Penniman | "AI PAC section new to us — sharing with research team" |
| 06/16 | CLC | A | REPLY | STRONG | Erin Chlopak | "Aligns with pending litigation — can I connect you to press?" |
| 06/17 | Common Cause CA | B | REPLY | STRONG | Darius Kemp | "Hawaii angle is exactly what we need for July messaging" |
| 06/18 | LWV CA | B | REPLY | STRONG | Jenny Farrell | "Forwarding to Voter Services Committee for June packet" |
| 06/21 | Clean Money | C | NOTE | WEAK | Unknown | No response at T+7 — marking WEAK |

Sheet 5 B4 = 4 STRONG → T7 Gate Status = "STRONG — ACTIVATE PHASE 2"

### Scenario 2: MODERATE outcome (B4 = 2-3)

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Notes |
|------|---|---|---|---|---|---|
| [sends as above] | | | | | | |
| 06/15 | Issue One | A | REPLY | STRONG | Nick Penniman | "Sharing with research team — AI PAC section is new" |
| 06/16 | CLC | A | OOO | MODERATE | Unknown | OOO: Chlopak returns June 20; alternate Sarah Jones identified |
| 06/17 | Common Cause CA | B | REPLY | MODERATE | Darius Kemp | "Very relevant — I'll make sure the team sees it" |
| 06/18 | LWV CA | B | GIST_CLICK | MODERATE | Unknown | 2 clicks 30h after LWV send |
| 06/21 | Clean Money | C | NOTE | WEAK | Unknown | No response at T+7 |

Sheet 5 B4 = 1 STRONG → T7 Gate Status = "WEAK — DEFER AND DIAGNOSE"

But wait: if Chlopak returns June 20 and replies by June 21-22 (T+7 actual window), B4 may increase to 2. The PENDING OOO means this is worth monitoring at T+7. Do not finalize the T+7 determination until June 21-22 to allow for the Chlopak return-date reply.

### Scenario 3: WEAK outcome (B4 = 0-1)

| Date | Organization | Tier | Event_Type | Signal_Code | Contact_Name | Notes |
|------|---|---|---|---|---|---|
| [sends as above] | | | | | | |
| 06/15 | CLC | A | GIST_CLICK | MODERATE | Unknown | 1 click 24h post-send |
| 06/15 | Issue One | A | OOO | WEAK | Unknown | Generic OOO; no alternate contact named |
| 06/17 | Common Cause CA | B | OOO | MODERATE | Darius Kemp | OOO until June 18; Sarah Morris identified as alternate |
| 06/21 | LWV CA | B | NOTE | WEAK | Unknown | No response at T+7 waiting period |
| 06/21 | Clean Money | C | NOTE | WEAK | Unknown | No response at T+7 waiting period |

Sheet 5 B4 = 0 → T7 Gate Status = "WEAK — DEFER AND DIAGNOSE"
Action: Run root-cause diagnosis (see T7_CHECKPOINT_DECISION_AUTOMATION.md WEAK branch). Follow up with Kemp's alternate (Sarah Morris) per the MODERATE OOO signal. Do not abandon — late signals may come in through June 23-25.

---

## What Not to Log

The following events do not require a row in the Daily Signal Log:

- Forwarding the email to yourself as a draft backup before sending
- Verifying the Gist URL is accessible (enter only if a problem is found)
- Reading your own draft emails before sending
- Calendar reminders or task notes about future sends
- The orchestrator reading this file

Log only external events: sends, replies, bounces, OOO messages, Gist click spikes, and substantive notes about contact behavior.

---

## Quick Reference Card

**STRONG** = substantive reply / forward confirmed with named recipient / meeting request / adoption commitment / novel data engagement / active litigation or campaign connection / sourcing request

**MODERATE** = positive but non-committal reply / generic routing to "the team" / OOO with named alternate / Gist click within 48h post-send

**WEAK** = no response past waiting period / polite decline / generic form response / bounce / OOO with no routing upgrade

**PENDING** = used only on SEND rows; replace with STRONG / MODERATE / WEAK when outcome known

**Waiting periods (June 14-15 send)**:
- CLC: 5 business days → June 21
- Issue One: 5 business days → June 21
- Common Cause CA: 7 business days → June 23
- LWV CA: 7 business days → June 23
- Clean Money: 9 business days → June 25

**T+7 gate**: B4 ≥ 4 = STRONG (activate Phase 2) | B4 = 2-3 = MODERATE (conditional) | B4 ≤ 1 = WEAK (defer and diagnose)

---

*Version 2.0 — Updated June 14, 2026. Reflects pending send state and adjusted checkpoint window. Sources: DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md (June 5 verification), PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4, T7_CHECKPOINT_DECISION_AUTOMATION.md.*
