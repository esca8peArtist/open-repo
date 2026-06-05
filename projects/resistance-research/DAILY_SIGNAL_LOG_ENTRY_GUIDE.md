---
title: "Daily Signal Log Entry Guide — Domain 51 Wave 1"
subtitle: "Decision Tree for Translating Contact Responses into Signal Codes"
created: "2026-06-05"
item: "Exploration Queue Item 84 — Deliverable 2"
status: "production-ready"
wave_1_execution: "June 9, 2026"
cross_references:
  - PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE_DOMAIN51.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - T7_CHECKPOINT_DECISION_AUTOMATION.md
---

# Daily Signal Log Entry Guide
## Translating Wave 1 Responses into Signal Codes

*Prepared June 5, 2026. This guide answers one question: when something happens with a contact, which Signal_Code do I enter in Sheet 1 of the measurement dashboard? Any person filling in the log should reach the same conclusion for the same event. No ambiguity.*

---

## Signal Code Definitions

**STRONG**: The organization is actively engaging with the research in a way that suggests it will influence their work. Not just "they read it" — they responded, forwarded, requested follow-up, or committed to action.

**MODERATE**: The organization received the research and responded positively, but has not committed to any specific use. They are interested but non-committal. Routing to the right person counts here.

**WEAK**: No substantive engagement. Non-response after 3+ days, polite decline, auto-reply only, or bounced email.

**PENDING**: Default code for a SEND row. Not a signal — it is a placeholder. Replace with STRONG / MODERATE / WEAK when an outcome is known.

**N/A**: Used for informational NOTE rows that are not signals (e.g., "Gist URL confirmed accessible on June 8").

---

## Master Decision Tree

Run through this tree top-to-bottom for every event. Stop at the first matching branch and use that code.

```
EVENT RECEIVED
    |
    +-- BOUNCE (mailer-daemon reply, delivery failure)
    |       |
    |       `--> Signal_Code: WEAK
    |            Event_Type: BOUNCE
    |            Notes: Enter bounce error code; flag in Contingency Trigger Log
    |
    +-- AUTO-REPLY ONLY (out-of-office, generic acknowledgment, no human content)
    |       |
    |       +-- OOO includes a named alternate contact or direct phone
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: OOO
    |       |            Notes: "OOO; alternate contact [Name] identified — follow up after [return date]"
    |       |
    |       `-- OOO with no alternate contact, or generic "thanks for contacting us"
    |               `--> Signal_Code: WEAK
    |                    Event_Type: OOO
    |                    Notes: "Generic OOO; no routing upgrade"
    |
    +-- HUMAN REPLY RECEIVED
    |       |
    |       +-- Reply contains ANY of these:
    |       |   - Explicit statement of organizational commitment ("we will use this in...")
    |       |   - Forward to colleagues mentioned explicitly ("sharing with our research team")
    |       |   - Request for follow-up meeting or call
    |       |   - Request to adapt or republish the research
    |       |   - Cites the research in a question (indicates they read it substantively)
    |       |   - Provides a substantive counterpoint or addition (engagement, not dismissal)
    |       |       `--> Signal_Code: STRONG
    |       |            Event_Type: REPLY
    |       |
    |       +-- Reply contains ANY of these:
    |       |   - Positive acknowledgment without commitment ("thank you, very interesting")
    |       |   - Routing to another staff member without explicit use statement
    |       |   - Request for more information about the research itself
    |       |   - General expression of alignment ("we care about this issue")
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: REPLY
    |       |
    |       `-- Reply contains ANY of these:
    |           - Polite decline ("not currently our focus")
    |           - Request to be removed from correspondence
    |           - Response makes clear research is not relevant to their current work
    |               `--> Signal_Code: WEAK
    |                    Event_Type: REPLY
    |
    +-- GIST CLICK DETECTED (via Bitly or GitHub view count spike)
    |       |
    |       +-- Click within 48 hours of send AND from a location consistent with org geography
    |       |       `--> Signal_Code: MODERATE
    |       |            Event_Type: GIST_CLICK
    |       |            Notes: "Bitly click detected [X] hours post-send; probable [org name] reader"
    |       |
    |       `-- Click cannot be attributed to specific org (general traffic spike)
    |               `--> Signal_Code: MODERATE (log anyway — counts toward total engagement signal)
    |                    Event_Type: GIST_CLICK
    |                    Notes: "Unattributed Gist view spike; possible organic amplification"
    |
    +-- NO RESPONSE AFTER WAITING PERIOD (see per-org timelines below)
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

Do not mark WEAK before these waiting periods have elapsed. Marking too early wastes a potential upgrade.

| Organization | Tier | Mark WEAK After | Rationale |
|---|---|---|---|
| CLC | A | 5 business days (June 16) | DC policy organizations respond within 5 days if they will respond at all; T+7 checkpoint aligns |
| Issue One | A | 5 business days (June 16) | Same rationale as CLC |
| Common Cause CA | B | 7 business days (June 20) | Campaign mode means later inbox attention; allow a full week |
| LWV CA | B | 7 business days (June 20) | Same as Common Cause CA |
| Clean Money | C | 9 business days (June 24) | Tier C with lowest expected response rate; allow maximum patience |

**Rule**: If the T+7 checkpoint arrives (June 16–18) before the waiting period has elapsed for a Tier B or C org, mark PENDING at the checkpoint and WEAK only after the waiting period has elapsed. The T+7 determination uses whatever signals are available — PENDING counts as zero signal, not WEAK.

---

## Per-Organization Signal Criteria

### Campaign Legal Center (CLC) — Tier A

**What counts as STRONG for CLC**:
CLC has a specific staff mandate to engage with external campaign finance research. STRONG signals reflect research utility to their litigation docket or policy advocacy:

- Erin Chlopak (Senior Director, Campaign Finance) responds with any substantive content — even one sentence about the FEC enforcement shutdown or AI PAC analysis
- Response from any CLC researcher or litigator who identifies a specific utility ("we're citing this in a brief")
- Forward to CLC communications team (implies potential publication amplification)
- Request to speak with the research author
- Gist view spike + reply from a CLC email domain within 72 hours

**Example — STRONG**: "Erin Chlopak responds: 'Thank you — your 200-day FEC enforcement shutdown data aligns with our pending litigation. Sharing with our enforcement team. Can I put you in touch with our press contact?'" → STRONG. She engaged the substance, forwarded internally, and escalated to media.

**Example — STRONG**: "Chlopak responds: 'Your AI PAC analysis is new to us. We've been tracking OpenAI but hadn't seen the Anthropic formation data. Our research team will review.'" → STRONG. "Our research team will review" is an explicit internal forwarding commitment with substantive engagement.

**What counts as MODERATE for CLC**:
- General inbox auto-acknowledgment with a named response coordinator ("Your message has been received. For research inquiries, contact [name] at [email]")
- OOO from Chlopak with named alternate contact
- Reply from general info@ inbox that routes to a different department ("Forwarding to our policy team")
- Positive acknowledgment without specific engagement ("Thank you for sharing this important research")

**What counts as WEAK for CLC**:
- No response by June 16 (5 business days post-send)
- Generic organizational form response with no routing
- Bounce from echlopak@campaignlegalcenter.org (re-send to info@campaignlegal.org immediately)
- Reply stating research is outside their current focus

**CLC-specific note**: CLC litigates FEC enforcement cases directly. If any reply references active litigation — even tangentially — escalate Signal_Code to STRONG regardless of other content. A reply that says "this may be relevant to our pending case" from any staff member is a STRONG signal even without a commitment.

---

### Issue One — Tier A

**What counts as STRONG for Issue One**:
Issue One's organizational identity is built around the campaign finance reform narrative. STRONG signals reflect research utility to their advocacy communications or policy work:

- Nick Penniman or any named Issue One staff responds with substantive engagement
- Reply mentions sharing the AI PAC analysis ("we hadn't seen the Anthropic PAC formation data — this is new")
- Forward to Issue One's ReFormers Caucus contacts (former elected officials — a STRONG network multiplier)
- Request to cite the research in an Issue One publication or report
- Reply indicating research will be used in Congressional testimony preparation

**Example — STRONG**: "Issue One staff responds: 'Your enforcement deadlock analysis is consistent with what we've documented in our Strengthening the Rules series. Sharing with Nick [Penniman] and our policy director. Would you be open to a brief call?'" → STRONG. Named forwarding chain + call request.

**Example — STRONG**: "Nick Penniman responds: 'Our research team is reviewing your AI PAC section. The Anthropic formation data wasn't on our radar. Can you share your sourcing?'" → STRONG. Substantive engagement with novel data, sourcing request indicates intent to use.

**What counts as MODERATE for Issue One**:
- Reply from info@ routing to policy team: "I've forwarded to our research team"
- Positive acknowledgment: "Thank you — this is very relevant to our current work" (no specific content engagement)
- OOO from info@ with staff member named as alternate
- Gist click from info@issueone.org domain within 72 hours (attributable via email timing)

**What counts as WEAK for Issue One**:
- No response by June 16 (5 business days post-send)
- Bounce from info@issueone.org
- Generic form acknowledgment with no routing

---

### Common Cause California — Tier B

**Decision-maker hierarchy note**: Darius Kemp is Executive Director as of June 2025. He may be reachable directly at dkemp@commoncause.org (recommended send address) or via ca@commoncause.org (general). The ballot campaign mode means Kemp's attention is on "Californians for Fair Elections" operational work. Research that advances the ballot campaign receives faster attention than general policy research.

**What counts as STRONG for Common Cause CA**:
Signal criteria are weighted toward direct ballot campaign utility:

- Kemp or any named Common Cause CA staff replies and explicitly connects research to ballot campaign ("this FEC analysis could support our July press push")
- Forward to "Californians for Fair Elections" coalition partners (Clean Money Action Fund, LWV CA)
- Request to incorporate research into voter guide or campaign materials
- Request for a meeting or call with the research author before July 1 CA deadline
- Response from national Common Cause (info@commoncause.org) that routes to California ballot campaign team

**Example — STRONG**: "Darius Kemp responds: 'The Hawaii SB 2471 angle is exactly what we need for our messaging on out-of-state dark money. Can I share this with our coalition partners? We're finalizing our July messaging strategy.'" → STRONG. Campaign-specific utility identified, explicit forward request, named use case.

**Example — STRONG**: "CA staff responds: 'This is being circulated at our coalition meeting on June 15. We'll report back on whether the group wants to incorporate it into our voter education materials.'" → STRONG. Coalition circulation + explicit intent to evaluate for use.

**What counts as MODERATE for Common Cause CA**:
- Reply acknowledging receipt and expressing general interest ("Very relevant to our work — I'll make sure the team sees it")
- OOO from Kemp with a named campaign staff alternate contact
- Forward to national Common Cause policy team (not CA-specific but upward routing)
- Gist view spike in the 48 hours after June 11 send (California attribution)

**What counts as WEAK for Common Cause CA**:
- No response by June 20 (7 business days post-send)
- Bounce from dkemp@commoncause.org (try ca@commoncause.org; log and note)
- Generic form acknowledgment
- Reply stating the organization is too focused on campaign execution to engage with external research

**Common Cause CA-specific note**: A response from any "Californians for Fair Elections" coalition member (even if not Common Cause itself) triggered by a Common Cause CA forward counts as a network multiplier event. Log it as a new STRONG row with Organization: Common Cause CA and Notes: "Coalition forward — [name of responding org]."

---

### League of Women Voters California — Tier B

**Decision-maker hierarchy note**: Jenny Farrell is Executive Director. LWV's primary use case for this research is voter education materials, not litigation or policy advocacy. The Executive Summary of Domain 51 is the most immediately usable component for LWV because it is excerptable into voter guides.

**What counts as STRONG for LWV CA**:
Signal criteria center on voter education and member communication utility:

- Farrell or named LWV staff explicitly mentions voter guide, member education, or voter education use case
- Forward to LWV National (lwv.org) or to California chapter voter services committee
- Request to excerpt the Executive Summary for an LWV publication
- Reply mentioning the research will be shared at an LWV member meeting or chapter convening
- Request for a simplified or shorter version for member distribution

**Example — STRONG**: "Jenny Farrell responds: 'Your Executive Summary is exactly the format we use in voter guides. I'm forwarding to our Voter Services Committee to discuss including this in our June voter education packet.'" → STRONG. Specific use case identified, explicit forwarding action, named committee.

**Example — STRONG**: "LWV CA program staff responds: 'This aligns with our ballot measure education priorities. Can we discuss incorporating this into our chapter briefings before the July 1 distribution window?'" → STRONG. Specific distribution window awareness + meeting request.

**What counts as MODERATE for LWV CA**:
- General acknowledgment: "Thank you for sharing — the League values this work"
- OOO from lwvc@lwvc.org with named staff contact
- Reply routing to LWV member services team (not voter education specifically)
- Gist click from a lwvc.org or lwv.org email domain

**What counts as WEAK for LWV CA**:
- No response by June 20 (7 business days post-send)
- Bounce from lwvc@lwvc.org
- Reply that research is not relevant to their current member education priorities
- Generic form acknowledgment

---

### Clean Money Action Fund — Tier C

**Decision-maker hierarchy note**: Trent Lange is President and has held the role since 2009. The organization is in active ballot campaign execution mode. The send address info@CAclean.org was confirmed June 5, 2026 via yesfairelections.org. Clean Money Action Fund is the campaign execution arm of the California Clean Money Campaign — their primary activity is signature collection, donor outreach, and ballot campaign operations, not external research engagement.

**What counts as STRONG for Clean Money**:
Given the Tier C 5–10% base rate, any substantive reply is a STRONG signal. The bar is set lower because the expected outcome is no response:

- Any human reply from info@CAclean.org that is not a form response or decline
- Trent Lange personally responds (named individual engagement)
- Any reply from a Clean Money Action Fund staff member engaging with any part of the research
- Forward to "Californians for Fair Elections" coalition coordinator

**Example — STRONG**: "Trent Lange responds: 'Thanks — the AI PAC section is something we've been trying to explain to donors. Can we reference this in our fundraising materials?'" → STRONG. This is the full extent of what STRONG means for Clean Money — any substantive human engagement with content counts, given their operational focus.

**Example — STRONG**: "Clean Money staff responds: 'We're sharing this with our campaign communications director. The Hawaii SB 2471 model is directly relevant to our messaging.'" → STRONG. Forward with named recipient and specific utility identified.

**What counts as MODERATE for Clean Money**:
Clean Money's expected response distribution has essentially no MODERATE band — the realistic outcomes are STRONG (any substantive engagement) or WEAK (no response). A routing acknowledgment with a named contact counts as MODERATE:

- Auto-reply that names a specific staff contact ("For press and research inquiries, contact [Name]")
- Reply forwarding to campaign communications without specific engagement

**What counts as WEAK for Clean Money**:
- No response by June 24 (9 business days post-send)
- Bounce from info@CAclean.org (log "verification required"; investigate but do not delay other sends)
- Generic form acknowledgment
- Polite decline citing campaign capacity constraints

**Clean Money-specific note**: If info@CAclean.org bounces, do not investigate during the June 9–12 execution window. Log the bounce, mark WEAK, and note "Email verification required post-Wave 1." The other four sends take priority. Investigate clean money email address on June 14 or later.

---

## Signal Code Upgrade Rules

Once a Signal_Code is set, do not edit the original row. If a contact escalates after an initial weak signal, add a NEW row:

**Scenario**: You log CLC as WEAK on June 16 (no response by T+7). On June 18, Erin Chlopak replies with substantive engagement.
**Action**: Add a new row — Date: 06/18/2026, Organization: CLC, Signal_Code: STRONG, Event_Type: REPLY, Notes: "Late reply from Chlopak — substantive engagement post-T+7; STRONG signal; upgrades T+7 determination retroactively for T+14 checkpoint."
**Dashboard effect**: Sheet 3 formula picks up the STRONG signal and updates CLC status to "Confirmed." Sheet 5 STRONG count increases. The T+7 determination row in Sheet 4 should be annotated in column K: "T+7 determination was WEAK at time of assessment; upgraded to MODERATE/STRONG by June 18 Chlopak reply — see T+14 row."

**Scenario**: You log Common Cause CA as MODERATE on June 14 (OOO with named contact). On June 20, a follow-up to the named contact receives a substantive reply.
**Action**: Add a new row — Date: 06/20/2026, Organization: Common Cause CA, Signal_Code: STRONG, Event_Type: REPLY.

---

## What Not to Log

The following events do not require a row in the Daily Signal Log:

- Forwarding the email to yourself as a draft backup
- Verifying the Gist URL is accessible (enter only if a problem is found)
- Reading your own emails before sending
- Calendar reminders or task notes about future sends

Log only external events: sends, replies, bounces, Gist clicks, and substantive notes about contact behavior.

---

## Quick Reference Card (cut-and-keep)

**STRONG** = substantive reply, forward to colleagues confirmed, meeting request, adoption commitment, novel data engagement, campaign-specific utility identified

**MODERATE** = positive but non-committal, forward to team without specific use, OOO with named alternate, Gist click attributable to org within 48h post-send

**WEAK** = no response past waiting period, polite decline, generic form response, bounce, OOO with no routing upgrade

**PENDING** = used only on SEND rows; replace with STRONG/MODERATE/WEAK when outcome known

**Waiting periods before marking WEAK**: CLC: 5 days (June 16) | Issue One: 5 days (June 16) | Common Cause CA: 7 days (June 20) | LWV CA: 7 days (June 20) | Clean Money: 9 days (June 24)

---

*Prepared June 5, 2026. Sources: DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md (June 5 verification), PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4 (per-constituency success thresholds), PHASE_2_SEQUENTIAL_ACTIVATION_STRATEGY.md Section 3 (coalition leverage analysis).*
