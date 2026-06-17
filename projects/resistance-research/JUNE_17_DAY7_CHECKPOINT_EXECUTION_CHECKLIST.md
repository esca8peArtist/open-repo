---
title: "June 17-18 Day 7 Checkpoint Execution Checklist"
created: "2026-06-17"
status: "production-ready"
execution_window: "June 17-18, 2026 — activate after Wave 1-2 emails sent"
domains_covered: [48, 51, 59]
hard_deadlines:
  - "June 25-30: Senate Finance CTC markup (Domain 59)"
  - "July 1: California Fair Elections Act ballot deadline (Domain 51)"
  - "July 15: Virginia Right to Vote Coalition integration (Domain 48)"
estimated_execution_time: "2-3 hours (post-checkpoint routing)"
purpose: "Zero-setup checkpoint execution framework for June 17-18 Day 7 checkpoint"
---

# June 17-18 Day 7 Checkpoint Execution Checklist

*Resistance Research — Day 7 Checkpoint Framework*
*Built June 17, 2026. Ready for execution upon Wave 1-2 email send confirmation.*

---

## How to Use This Checklist

Execute sections in order. Each section is self-contained and takes 10-30 minutes. Total execution time: 2-3 hours. No discovery required — all data sources, thresholds, and action sequences are pre-populated.

The checkpoint answers one question: **What is the engagement signal strength per domain (STRONG / MODERATE / WEAK), and what Tier 2 activation does each signal authorize?**

Once you have signal strengths for all three domains, Section 6 routes to the correct activation sequence. Sections 7 and 8 cover timeline contingencies and failure recovery.

---

## Section 1: Pre-Checkpoint Verification (15 minutes)

Complete all checks before entering the decision logic. Record results in the fields below.

### 1.1 Email Send Status Per Domain

**Critical prerequisite**: The Day 7 checkpoint is only meaningful if Wave 1-2 emails were sent. If sends are still pending, the checkpoint date shifts. See Section 7 for timeline contingency logic.

**Domain 59 — Economic Precarity / CTC**

Wave 1 send window: June 9-11, 2026 (EXECUTED per package header)

```
Status confirmation:
[ ] AFL-CIO (feedback@aflcio.org) — Send date: __________ Bounced? Y/N
[ ] CBPP (cbpp@cbpp.org) — Send date: __________ Bounced? Y/N
[ ] NWLC (info@nwlc.org) — Send date: __________ Bounced? Y/N
[ ] MomsRising (info@momsrising.org) — Send date: __________ Bounced? Y/N
[ ] ITEP (itep@itep.org) — Send date: __________ Bounced? Y/N

Total D59 sends confirmed: ___ / 5
Hard bounces: ___
Delivery rate: ___%
```

Source for sends: `domain-59-send-log-june1.md`

**Domain 51 — Campaign Finance / Dark Money**

Wave 1-2 send window: June 14-15, 2026 (status: ready, may still be pending)

```
Status confirmation:
Wave 1:
[ ] CLC — Erin Chlopak (echlopak@campaignlegalcenter.org) — Send date: __________ Bounced? Y/N
[ ] Issue One (info@issueone.org) — Send date: __________ Bounced? Y/N

Wave 2:
[ ] Common Cause CA — Darius Kemp (dkemp@commoncause.org) — Send date: __________ Bounced? Y/N
[ ] LWV California (lwvc@lwvc.org) — Send date: __________ Bounced? Y/N
[ ] Clean Money Action Fund (info@CAclean.org) — Send date: __________ Bounced? Y/N

Total D51 sends confirmed: ___ / 5
Hard bounces: ___
Delivery rate: ___%
```

Source for sends: `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`

**Domain 48 — Criminal Justice / Civic Exclusion**

Wave 1-2 send window: June 16-19, 2026

```
Status confirmation:
Wave 1:
[ ] Sentencing Project — Nicole D. Porter (nporter@sentencingproject.org) — Send date: __________ Bounced? Y/N
[ ] Prison Policy Initiative (info@prisonpolicy.org) — Send date: __________ Bounced? Y/N

Wave 2:
[ ] Brennan Center — Sean Morales-Doyle (brennancenter.org web form) — Send date: __________ Bounced? Y/N
[ ] Worth Rises — Bianca Tylek (info@worthrises.org) — Send date: __________ Bounced? Y/N
[ ] CLC — Blair Bowie / Restore Your Vote (info@campaignlegal.org) — Send date: __________ Bounced? Y/N
[ ] M4BL Policy Table (info@m4bl.org) — Send date: __________ Bounced? Y/N

Total D48 sends confirmed: ___ / 6
Hard bounces: ___
Delivery rate: ___%
```

Source for sends: `DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md`

### 1.2 Gist URL Live Check

Load each URL in a browser. All three must return HTTP 200 with content visible before any send references are evaluated.

```
[ ] Domain 59: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba — STATUS: ______
[ ] Domain 51: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 — STATUS: ______
[ ] Domain 48: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8 — STATUS: ______
```

If any Gist returns 404: recreate before proceeding. Do not attribute zero Gist clicks to weak engagement until confirmed live.

### 1.3 External Deadline Verification

```
[ ] Senate Finance markup status: https://www.finance.senate.gov/hearings
    Result: Markup still active / Markup closed (circle one)
    If markup closed → pivot Domain 59 to "Build the 2027 Reform Coalition" frame per
    DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 7 Contingency 1

[ ] California Fair Elections Act ballot measure: https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026)
    Result: Still active / Qualified / Failed to qualify (circle one)
    If failed to qualify → Domain 51 Tier 2 strategy shifts; see DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md

[ ] Montana I-194 status: ballotpedia.org (search Montana I-194 2026)
    Result: Still active / Qualified / Not yet qualified (circle one)

[ ] Virginia Right to Vote Coalition: July 15 organizational integration deadline still operative?
    Result: Confirmed / Changed (note changes below)
```

### 1.4 Delivery Rate Gate

If any domain delivery rate is below 80%:

```
DELIVERY DIAGNOSTIC (5 minutes):
1. Identify bounced addresses in the send log
2. Check for domain-level deliverability issues (mass bounce from one domain)
3. Re-send to hard-bounce addresses using fallback addresses per contact verification files
4. Do NOT proceed to signal assessment until delivery is above 80%

Bounced addresses:
Domain 59: _______________________________________________
Domain 51: _______________________________________________
Domain 48: _______________________________________________
```

---

## Section 2: Coalition Leverage Matrix Review (20 minutes)

Review the strongest engagement signals per domain before entering the decision tree. This prevents a mechanical threshold application that misses qualitative signal quality.

### 2.1 Domain 59 — Most Important Engagement Signals

The Coalition Leverage Matrix identifies CBPP as the highest-value Phase 1 anchor for the Senate Finance CTC markup window. A CBPP reply — even one sentence connecting the democratic participation frame to CTC refundability — is analytically more significant than three form-acknowledgment replies from lower-priority contacts.

**Priority signal hierarchy for Domain 59:**

| Rank | Organization | Why Priority | What Counts as STRONG |
|------|--------------|--------------|----------------------|
| 1 | CBPP | Senate Finance testimony access; primary CTC citation source | Any substantive engagement with the democratic participation argument |
| 2 | ITEP | Quantitative foundation for Domain 59 claims | Reference to the $0 benefit analysis or cognitive bandwidth mechanism |
| 3 | MomsRising | 5M member network; direct Senate Finance constituent contact | Any mention of sharing with Congressional contacts or Senate outreach |
| 4 | NWLC | Active CTC Senate campaign; gendered caregiving pathway alignment | Request for additional materials or campaign integration |
| 5 | AFL-CIO | Federation inbox; variable routing lag | Direct reply from a named Legislative Affairs staff member |

**Record engagement signal from each:**

```
CBPP response: _________________________________ Score: STRONG / MODERATE / WEAK / NONE
ITEP response: _________________________________ Score: STRONG / MODERATE / WEAK / NONE
MomsRising response: ___________________________ Score: STRONG / MODERATE / WEAK / NONE
NWLC response: _________________________________ Score: STRONG / MODERATE / WEAK / NONE
AFL-CIO response: ______________________________ Score: STRONG / MODERATE / WEAK / NONE

Domain 59 STRONG count: ___
Domain 59 any-reply count: ___
Domain 59 Gist click count (from GitHub Gist view stats): ___
```

### 2.2 Domain 51 — Most Important Engagement Signals

Campaign Legal Center is the highest-value anchor for Domain 51. CLC has direct litigation docket overlap with the FEC enforcement collapse analysis. A response from Erin Chlopak is the most predictive signal of organizational usefulness for the July 1 California deadline.

**Priority signal hierarchy for Domain 51:**

| Rank | Organization | Why Priority | What Counts as STRONG |
|------|--------------|--------------|----------------------|
| 1 | Campaign Legal Center (Chlopak) | Constitutional team; FEC enforcement docket; Hawaii/Montana charter model relevance | Any substantive engagement with the constitutional analysis |
| 2 | Issue One | ReFormers Caucus; DISCLOSE Act coalition; FEC reform research | Request for distribution to their newsletter or ReFormers Caucus |
| 3 | Common Cause CA | California Fair Elections Act campaign operations | Mention of integrating research into ballot campaign materials |
| 4 | LWV California | Voter education network; California reach | Request to distribute to league membership |
| 5 | Clean Money Action Fund | Direct ballot campaign operations | Any engagement from Trent Lange's team |

**Record engagement signal from each:**

```
CLC (Chlopak) response: ________________________ Score: STRONG / MODERATE / WEAK / NONE
Issue One response: ____________________________ Score: STRONG / MODERATE / WEAK / NONE
Common Cause CA response: ______________________ Score: STRONG / MODERATE / WEAK / NONE
LWV CA response: _______________________________ Score: STRONG / MODERATE / WEAK / NONE
Clean Money AF response: _______________________ Score: STRONG / MODERATE / WEAK / NONE

Domain 51 STRONG count: ___
Domain 51 any-reply count: ___
Domain 51 Gist click count: ___
```

### 2.3 Domain 48 — Most Important Engagement Signals

The Sentencing Project is the highest-value anchor for Domain 48 because their "Locked Out" data is the primary empirical source for the document. A response from Nicole Porter is analytically equivalent to CBPP for Domain 59 — it validates the research as a legitimate extension of their work.

**Priority signal hierarchy for Domain 48:**

| Rank | Organization | Why Priority | What Counts as STRONG |
|------|--------------|--------------|----------------------|
| 1 | Sentencing Project (Porter) | Primary data source; "Locked Out" series; state advocacy; Virginia coalition | Any substantive engagement with Virginia or Florida analysis |
| 2 | Prison Policy Initiative (Wagner) | Jury exclusion and housing barrier research is primary source for Sections 2.2 and 2.5 | Engagement with the democratic design extension of their synthesis |
| 3 | Worth Rises (Tylek) | LFO research is foundational to Section 4 poll tax analysis | Any reference to the Florida Amendment 4 case study |
| 4 | Brennan Center (Morales-Doyle) | Readmission Act constitutional theory is new litigation avenue | Any routing to their Virginia or constitutional litigation teams |
| 5 | CLC / Restore Your Vote (Bowie) | Direct operational hook — Restore Your Vote is cited in Section 8 | Any engagement with the Virginia July 15 deadline |

**Record engagement signal from each:**

```
Sentencing Project response: ___________________ Score: STRONG / MODERATE / WEAK / NONE
PPI response: __________________________________ Score: STRONG / MODERATE / WEAK / NONE
Worth Rises response: __________________________ Score: STRONG / MODERATE / WEAK / NONE
Brennan Center response: _______________________ Score: STRONG / MODERATE / WEAK / NONE
CLC/RYV response: ______________________________ Score: STRONG / MODERATE / WEAK / NONE
M4BL response: _________________________________ Score: STRONG / MODERATE / WEAK / NONE

Domain 48 STRONG count: ___
Domain 48 any-reply count: ___
Domain 48 Gist click count: ___
```

---

## Section 3: Tier 2 Activation Decision Logic (15 minutes)

After recording signal scores, apply this logic per domain to determine Tier 2 activation status. Do not activate Tier 2 before running Section 6 (Checkpoint Decision Gate) — signal scores alone do not determine activation; composite threshold logic governs.

### 3.1 Domain 59 Tier 2 Activation Logic

**Tier 2 contacts (activate T+6 from Wave 1 send if threshold met):**
- Economic Policy Institute — Heidi Shierholz (researchdept@epi.org — verify before send)
- Demos — Taifa Smith Butler (info@demos.org)
- National Employment Law Project — Rebecca Dixon (info@nelp.org)
- National Housing Law Project — Policy team (info@nhlp.org)

**Activation threshold:**
```
2+ STRONG replies from Wave 1 Tier 1 → ACTIVATE all four Tier 2 contacts
1 STRONG reply from Wave 1 Tier 1 → SELECTIVE activation: EPI + NELP only (higher alignment)
0 STRONG replies from Wave 1 Tier 1 → HOLD Tier 2 until Day 14; reassess July 1
```

**Domain 59 Tier 2 decision (fill in after Section 2.1):**
```
D59 STRONG count: ___
Decision: ACTIVATE ALL / SELECTIVE (EPI+NELP) / HOLD (circle one)
Activation date: _________________
```

### 3.2 Domain 51 Tier 2 Activation Logic

**Tier 2 contacts pre-identified (13 total — outreach sequencing: initial 3 → secondary 5 → extended 5):**

Initial 3 (highest priority):
- True North Research — Lisa Graves (info@truenorthresearch.org)
- Montana I-194 Campaign (via ballotpedia.org — search Montana I-194 2026 campaign)
- Michigan Clean Elections Coalition (via michiganadvance.com)

Secondary 5 (activate after initial 3 respond or 7 days pass):
- New Mexico Common Cause (via commoncause.org/new-mexico)
- Issue One ReFormers Caucus (via issueone.org/about/reformers-caucus)
- ACLU Voting Rights Project — Sophia Lin Lakin (slakin@aclu.org)
- UCLA Election Law Center — Rick Hasen (rhasen@law.ucla.edu)
- Loyola Law School — Justin Levitt (jlevitt@lls.edu)

Extended 5 (activate upon Tier 1-2 confirmation):
- End Citizens United — David Donnelly (info@endcitizensunited.org)
- Public Citizen — Craig Holman (cholman@citizen.org — shortform handle, confirmed)
- Brennan Center — Saurav Ghosh (ghoshs@brennan.law.nyu.edu)
- Democracy 21 — Fred Wertheimer (fwertheimer@democracy21.org — shortform handle, confirmed)
- OpenSecrets (info@opensecrets.org)

**Activation threshold (June 25 checkpoint for July 1 California deadline):**
```
4+ STRONG from Waves 1-2 → Activate all 13 Tier 2 contacts immediately (initial 3 → secondary 5 → extended 5)
2-3 STRONG from Waves 1-2 → Activate initial 3 + secondary 5; hold extended 5 pending July 1 assessment
0-1 STRONG from Waves 1-2 → Activate initial 3 only; hold all others until June 25 checkpoint

Domain 51 STRONG count: ___
Decision: FULL (all 13) / PARTIAL (initial 3 + secondary 5) / MINIMAL (initial 3 only) (circle one)
Activation date: _________________
```

### 3.3 Domain 48 Tier 2 Activation Logic

**Tier 2 contacts (civil rights organizations — activate on strong signal):**
- NAACP Legal Defense Fund — Janai Nelson (info@naacpldf.org)
- ACLU of Virginia — Mary Bauer (acluva@acluva.org) — contingency if M4BL unresponsive
- Fines and Fees Justice Center — Joanna Weiss (info@finesandfeesjusticecenter.org)
- PPI follow-up (if Wave 1 produced engagement: Wendy Sawyer or Leah Wang for data validation)

**Activation threshold (June 27 checkpoint for July 15 Virginia deadline):**
```
2+ STRONG from Waves 1-2 → Activate NAACP LDF + FFJC immediately; ACLU VA on June 27
1 STRONG from Waves 1-2 → Activate FFJC only (highest LFO alignment); hold LDF for June 27
0 STRONG from Waves 1-2 → Contingency escalation (see Section 8); activate ACLU VA via contingency path

Domain 48 STRONG count: ___
Decision: FULL (LDF + FFJC + ACLU VA) / PARTIAL (FFJC only) / CONTINGENCY (circle one)
Activation date: _________________
```

---

## Section 4: Gist Tracking Per Domain (15 minutes)

GitHub Gist click counts provide a secondary engagement signal independent of email replies. A contact may click the Gist link without replying — this is a MODERATE signal (confirmed delivery + interest). Multiple clicks from a single IP block suggest organizational routing (the contact forwarded internally).

### 4.1 Accessing Gist View Counts

GitHub Gist does not provide a built-in analytics dashboard. Use the following approach:

**Method 1 — GitHub API (most reliable):**
```
curl -H "Accept: application/vnd.github+json" \
  https://api.github.com/gists/{GIST_ID}
```

Replace {GIST_ID} with the ID from each URL:
- Domain 59: `70b18a6f26dc879e3399c6d147d882ba`
- Domain 51: `6dce895c5192e6a3ba2abfed40733372`
- Domain 48: `00c1423e3da7bb4693fa285ec87f18a8`

Look for the `forks` and `history` fields in the API response. History entries show timestamps of access or modification events. A high number of history entries with access timestamps after the send date = confirmed engagement.

**Method 2 — Gist stars and comments:**
Load each Gist URL directly. Check:
- Stars (bottom of page) — public engagement signal
- Comments — any comment is an extremely strong signal (publicly engaged)
- Fork count — a fork means someone copied the content (strong engagement)

**Method 3 — URL shortener tracking (if a shortener was used):**
If any send used a bit.ly or similar shortened URL, check the shortener dashboard for click counts per URL.

### 4.2 Recording Gist Metrics

```
Domain 59 Gist (https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba):
  Stars: ___  Comments: ___  Forks: ___
  API history entries after June 9: ___
  Assessment: HIGH engagement / MODERATE engagement / LOW engagement / NO engagement

Domain 51 Gist (https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372):
  Stars: ___  Comments: ___  Forks: ___
  API history entries after June 14: ___
  Assessment: HIGH / MODERATE / LOW / NO

Domain 48 Gist (https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8):
  Stars: ___  Comments: ___  Forks: ___
  API history entries after June 16: ___
  Assessment: HIGH / MODERATE / LOW / NO
```

**Note from Domain 59 Wave 1 results**: 3 Gist clicks were recorded alongside 2 email replies, for a total 40% response rate. This is the MODERATE-to-STRONG engagement benchmark. 5+ Gist clicks on subsequent domains would indicate STRONG engagement; 1-2 clicks is MODERATE; 0 clicks with email replies is still MODERATE; 0 clicks with 0 email replies is WEAK pending delivery confirmation.

### 4.3 Interpreting Gist Signals

| Gist Signal | Interpretation | Effect on Threshold |
|-------------|----------------|---------------------|
| Any comment on Gist | Publicly engaged — treat as STRONG regardless of reply | +1 STRONG equivalent |
| 3+ clicks on a Gist with 0 email replies | Interest confirmed, inbox routing failed | Run delivery diagnostic; attempt contact form re-send |
| Gist fork | Content being actively used by someone in the network | +1 STRONG equivalent |
| 0 clicks and 0 replies on a Gist that returns 200 | Delivery failure most likely, not engagement failure | Run delivery diagnostic |
| Gist returns 404 | Gist was deleted or URL is wrong | Recreate before assigning blame to engagement failure |

---

## Section 5: Response Categorization Matrix (15 minutes)

Classify each reply using this matrix before assigning a signal score. The categorization is the input to the checkpoint decision gate in Section 6.

### 5.1 Reply Types

**Substantive reply (Score 3-5, maps to STRONG signal):**

Definition: The reply contains at least one of the following:
- A named staff member engages with the specific content of the email (not just acknowledges receipt)
- A request for additional materials, a conversation, or internal routing
- A citation question or factual engagement with the domain research
- An indication the organization will distribute, cite, or use the research
- An offer to include in their testimony, newsletter, or advocacy materials
- Any follow-up question about the research methodology or conclusions

Examples:
- "Thank you for sending this. Our team is reviewing the CTC analysis and wanted to ask about the Dallas Fed study you cite — can you send the full citation?" → Score 5 (STRONG)
- "I've forwarded this to our policy team and we'd like to discuss the Hawaii charter theory with you." → Score 4 (STRONG)
- "This is useful research. We may reference it in our Senate Finance testimony." → Score 3 (STRONG)

**Boilerplate reply (Score 2, maps to MODERATE signal):**

Definition: A generic acknowledgment that confirms receipt but contains no substantive engagement. Subcategories:

- Auto-acknowledgment with a named contact in the signature → MODERATE (named person is a follow-up target)
- Out-of-office with a return date → MODERATE (follow up after return date)
- "Thank you for reaching out, someone will be in touch" with no further specifics → Score 2 (MODERATE)
- Auto-acknowledgment from a general inbox with no named contact → Score 1 (borderline WEAK)

**No reply (Score 0, maps to NONE — not yet WEAK):**

Definition: No reply received within 7 days of confirmed delivery. This is not yet a negative signal — it is within the normal range for national policy organizations. Assign NONE at Day 7; reassign WEAK only after Day 14 with no reply.

### 5.2 Sentiment Scoring

Beyond categorization, assess sentiment for any substantive reply:

| Sentiment | Indicators | Action |
|-----------|------------|--------|
| Aligned | Reply references agreement with the democratic design framing; uses similar language; asks about co-distribution | Priority: reply within 24 hours; offer one-page summary |
| Neutral/Analytical | Reply asks clarifying questions; requests data sources; neutral engagement with the analysis | Priority: reply within 48 hours; provide citations requested |
| Critical | Reply challenges the framing, disagrees with conclusions, or questions the research methodology | Priority: engage substantively; note as potential adversarial signal but not a reason to disengage |
| Logistical | Reply is about delivery, routing, or organizational process (e.g., "Please resend to this address") | Action: follow through on logistical request immediately; treat as MODERATE signal |

### 5.3 Action Indicators

An action indicator is a phrase or request in a reply that signals the organization is ready to move from acknowledgment to action. These elevate any reply to STRONG regardless of other content:

- "Can we schedule a call?"
- "We'd like to include this in our testimony / briefing / newsletter"
- "I'm forwarding this to [named colleague]"
- "Can we co-sign / co-author / jointly submit?"
- "We're going to share this with our [state partner / coalition member / congressional contact]"
- Any request that requires the sender to do something beyond passively responding

### 5.4 Signal Score Summary (fill in before Section 6)

```
DOMAIN 59 SIGNAL SCORES:
AFL-CIO: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
CBPP: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
NWLC: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
MomsRising: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
ITEP: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Composite D59 signal: STRONG / MODERATE / WEAK (from Section 6 decision gate)

DOMAIN 51 SIGNAL SCORES:
CLC (Chlopak): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Issue One: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Common Cause CA: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
LWV CA: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Clean Money AF: Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Composite D51 signal: STRONG / MODERATE / WEAK (from Section 6 decision gate)

DOMAIN 48 SIGNAL SCORES:
Sentencing Project (Porter): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
PPI (Wagner): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Brennan Center (Morales-Doyle): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Worth Rises (Tylek): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
CLC / Restore Your Vote (Bowie): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
M4BL (Policy Table): Score ___ / Signal: STRONG / MODERATE / WEAK / NONE
Composite D48 signal: STRONG / MODERATE / WEAK (from Section 6 decision gate)
```

---

## Section 6: Checkpoint Decision Gate (10 minutes)

Apply these thresholds to determine the composite signal per domain, then route to the activation sequence in PHASE_2_T7_ROUTING_DECISION_TREE.md.

### 6.1 Threshold Definitions

**STRONG signal (proceed to Tier 2 immediately):**
- Domain 59: 2+ STRONG individual signals from Tier 1 contacts (Wave 1 = 5 contacts)
- Domain 51: 2+ STRONG individual signals from Wave 1-2 combined (10 contacts total)
- Domain 48: 2+ STRONG individual signals from Wave 1-2 combined (6 contacts)

Rationale for 30%+ threshold: The Coalition Leverage Matrix identifies 30%+ substantive reply rate as the minimum threshold for coalition formation viability. Below 30%, organizational relationships have not advanced beyond awareness. At 30%+, at least two organizations have signaled research value — sufficient to build initial coalition coordination.

**MODERATE signal (selective Tier 2, calendar-deadline domains only):**
- 1 STRONG individual signal, OR
- 3+ MODERATE individual signals (aggregate engagement without full substantive engagement), OR
- 0 STRONG but Gist click activity above threshold (3+ clicks on Domain 59; 2+ on Domain 51 or 48)

Rationale: One substantive engagement validates the research direction. Selective Tier 2 focuses resources on the organizations that showed interest while monitoring whether that interest converts to coalition action.

**WEAK signal (hold; reassess at Day 14):**
- 0 STRONG individual signals AND
- Fewer than 3 MODERATE signals AND
- Gist engagement at or near zero AND
- Delivery confirmed at 80%+

Rationale: Absence of evidence is not evidence of absence at Day 7. Most policy organizations require 7-14 days to route incoming research to the correct team. WEAK at Day 7 is a monitoring signal, not a termination signal.

### 6.2 Decision Gate Application

```
DOMAIN 59 DECISION GATE:
  STRONG count: ___ | MODERATE count: ___ | Gist clicks: ___
  Threshold met: STRONG / MODERATE / WEAK (circle one)
  Action: See Section 3.1 + PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1

DOMAIN 51 DECISION GATE:
  STRONG count: ___ | MODERATE count: ___ | Gist clicks: ___
  Threshold met: STRONG / MODERATE / WEAK (circle one)
  Action: See Section 3.2 + PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1

DOMAIN 48 DECISION GATE:
  STRONG count: ___ | MODERATE count: ___ | Gist clicks: ___
  Threshold met: STRONG / MODERATE / WEAK (circle one)
  Action: See Section 3.3 + PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1

Cross-domain coalition opportunity (fill in from routing decision tree):
  D51 + D59 both STRONG? Y/N → If YES, see PHASE_2_T7_ROUTING_DECISION_TREE.md Section 4
  D59 STRONG + D48 MODERATE? Y/N → If YES, see coalition bridge strategy Section 4
```

### 6.3 Logging the Decision

After applying the gate, log the decision immediately:

```bash
# Autonomous execution (run from projects/resistance-research/):
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-checkpoint

# Manual logging if script not available:
# Open WORKLOG.md and record:
# Date: [June 17 or 18, 2026]
# D59 composite signal: [STRONG/MODERATE/WEAK]
# D51 composite signal: [STRONG/MODERATE/WEAK]
# D48 composite signal: [STRONG/MODERATE/WEAK]
# Tier 2 activations authorized: [list domains]
# Next checkpoint date: [June 24-25]
```

---

## Section 7: Timeline Contingencies (15 minutes)

### 7.1 If Email Sends Were Delayed to June 17

**Effect on checkpoint timing:**

If Wave 1-2 emails were sent June 17 (not June 9-15 as planned), the Day 7 checkpoint shifts to June 24. This is recoverable for all three domains:
- Domain 59: Senate Finance markup closes June 25-30. A June 24 checkpoint leaves 1-6 days for Tier 2 activation before the markup closes. Minimal but viable.
- Domain 51: California ballot deadline is July 1. A June 24 checkpoint leaves 7 days for Tier 2 activation. Adequate.
- Domain 48: Virginia July 15 deadline. A June 24 checkpoint leaves 21 days for Tier 2 activation. Comfortable.

**Action if sends delayed to June 17:**
```
Do not execute this checklist today. Return June 24 at 17:00 UTC.
Domain 59: Senate Finance timeline is now compressed to days. On June 24:
  - If 1+ STRONG: activate Tier 2 immediately on June 24 (no waiting)
  - If 0 STRONG: proceed with Tier 1 framing shift to post-markup coalition building
Domain 51: Timeline intact. Standard checkpoint execution June 24.
Domain 48: Timeline intact. Standard checkpoint execution June 24.
```

### 7.2 If Checkpoint Is Delayed to June 18

If the June 17 checkpoint cannot execute (user unavailable), run on June 18. No domain deadlines are critically affected by one day. Domain 59 loses one day of Tier 2 contact time before the Senate markup — this narrows the window but does not close it.

**June 18 adjustment:**
```
All Section thresholds apply without change.
Domain 59: Execute any Tier 2 activation the same day as the June 18 checkpoint — no additional delay.
Domain 51: No change to activation sequence.
Domain 48: No change to activation sequence.
```

### 7.3 If Checkpoint Delayed Further (June 19+)

**Domain 59 — Critical timeline:**

Senate Finance markup window closes June 25-30. If checkpoint executes June 19-23, Tier 2 activation can proceed but with progressively compressed timelines for organizational response:

| Checkpoint Date | Days Before Markup | Tier 2 Viable? |
|-----------------|---------------------|----------------|
| June 17 | 8-13 days | Fully viable |
| June 18 | 7-12 days | Viable |
| June 19 | 6-11 days | Viable (tight) |
| June 20 | 5-10 days | Viable (tight) |
| June 21-23 | 2-9 days | Marginal — send Tier 2 same day as checkpoint |
| June 24+ | 1-6 days | Shift to "Reform Coalition 2027" framing |

**Retiming logic for July 1 hard deadline (all domains):**

The July 1 hard deadline governs Domain 51 (California ballot measure deadline). If Phase 2 checkpoint activity has not completed by June 25, execute an emergency compression:

```
June 25 Emergency Compression (if checkpoint not yet run):
1. Run this checklist immediately
2. Domain 51: Accept any prior signal data; activate initial 3 Tier 2 contacts same day
3. Domain 59: If Senate markup still active, send Tier 2 same day; otherwise shift frame
4. Domain 48: Virginia July 15 deadline still 20 days away; standard execution still applies
```

### 7.4 July 1 Hard Deadline Implications

July 1 is the California Fair Elections Act ballot measure qualification deadline and the reference date for Phase 2 Tier 2 evaluation. After July 1:

- Domain 51 Tier 2 activation logic shifts from "California deadline urgency" to "Reform coalition 2027" framing
- All Domain 51 contact framing should reference "next legislative cycle" rather than the ballot measure
- Domains 59 and 48 deadlines (Senate Finance markup, Virginia July 15) remain operative

---

## Section 8: Failure Recovery (10 minutes)

### 8.1 If No Responses Across All Three Domains

**Condition**: 0 STRONG signals from Domain 59 + 0 STRONG signals from Domain 51 + 0 STRONG signals from Domain 48 by Day 7.

This is uncommon but possible for two reasons: (a) delivery failure, or (b) genuine engagement failure. Distinguish before responding.

**Step 1 — Delivery diagnostic (10 minutes):**
```
[ ] Check all three send logs for hard bounces
[ ] Verify all three Gist URLs return 200
[ ] Check if any email domains were flagged (Google Workspace, spam filters)
[ ] Check Gist click counts — any clicks at all?

If zero clicks on any Gist AND zero replies: likely delivery failure
If clicks on Gist but zero replies: engagement interest present, email routing failed
```

**Step 2 — Recovery routing based on diagnostic:**

If delivery failure: resend via contact form (each organization has a web inquiry form; use it as the primary backup). Do not wait for email delivery to be repaired — go to the contact form immediately. This is not a second send; it is a delivery repair.

If engagement failure (delivered, no reply): apply the following escalation sequence:

```
Domain 59 escalation path (0 replies by Day 14):
  → Identify any CBPP personal connections through organizational networks
  → Send to Senate Finance Committee staff directly (public contact available at finance.senate.gov)
  → Publish the Gist URL with explicit Senate Finance framing on organizational social channels

Domain 51 escalation path (0 replies by Day 14):
  → Direct send to CLC's campaign finance litigation team via a different staff contact
  → Contact Campaign Legal Center via their media contact for press framing
  → Escalate to Wave 3 contacts (ECU, Public Citizen, Democracy 21) without waiting for Tier 1 signal

Domain 48 escalation path (0 replies by Day 14):
  → Send directly to NAACP LDF (Tier 2) without waiting for Tier A signal
  → Contact Virginia Right to Vote Coalition directly via known state coalition members
  → ACLU of Virginia contingency path (acluva@acluva.org — Mary Bauer) as primary pivot
```

### 8.2 If Partial Responses — Selective Domain Advancement

**Condition**: 1-2 STRONG signals from one domain, 0 from others.

This is the most likely outcome and represents selective domain advancement:

**Protocol**: Advance the responding domain to Tier 2 immediately. Hold the non-responding domains at Day 14. Do not treat partial response as system failure — it is a signal that one domain's framing or organizational alignment is stronger.

```
If D59 STRONG but D51 + D48 WEAK:
  → Advance Domain 59 to Tier 2 immediately (Senate Finance window demands it)
  → Send Domain 51 follow-up to CLC only (highest-probability contact) on Day 14
  → Send Domain 48 follow-up to Sentencing Project only on Day 14
  → Reassess all three at July 1 checkpoint

If D51 STRONG but D59 + D48 WEAK:
  → Advance Domain 51 to Tier 2 initial 3 contacts
  → Domain 59: Tier 2 activation forced by Senate markup deadline regardless of signal
  → Domain 48: Hold at Day 14

If D48 STRONG but D59 + D51 WEAK:
  → Advance Domain 48 to NAACP LDF + FFJC
  → Domain 59: Forced activation regardless (markup deadline)
  → Domain 51: Day 14 assessment before further activation
```

### 8.3 User Input Escalation Triggers

Flag the following conditions in CHECKIN.md under "Needs Your Input" if they arise:

```
[ ] All three domains return WEAK signal at Day 14 (not just Day 7)
[ ] Senate Finance markup completes before any Domain 59 Tier 2 contacts are reached
[ ] California ballot measure disqualified before Domain 51 Tier 2 activates
[ ] Organizational opposition received (Score 1-2 reply that challenges research framing)
[ ] Any organizational contact requests removal from future sends
```

---

## Quick Reference Summary

| Domain | Send Count | Hard Deadline | STRONG Threshold | Tier 2 Count | Checkpoint Date |
|--------|-----------|----------------|------------------|--------------|-----------------|
| 59 (CTC) | 5 contacts | June 25-30 (markup) | 2+ STRONG from 5 | 4 contacts | June 17-18 |
| 51 (Dark Money) | 10 contacts (W1-W3) | July 1 (CA ballot) | 2+ STRONG from 5 (W1-2) | 13 contacts | June 17-18 |
| 48 (Criminal Justice) | 6 contacts | July 15 (VA coalition) | 2+ STRONG from 6 | 4 contacts | June 17-18 |

**Composite routing document**: PHASE_2_T7_ROUTING_DECISION_TREE.md

**Tier 2 activation templates**: PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md

**Autonomous execution**: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-checkpoint`

---

*Built June 17, 2026. All contacts verified: Domain 51 (June 10-11), Domain 59 (June 10), Domain 48 (June 5-16). Production-ready for Day 7 checkpoint execution.*
