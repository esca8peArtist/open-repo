---
title: "Post-Wave 1 Phase 1 Measurement Framework"
created: 2026-05-17
updated: 2026-05-17
status: PRODUCTION-READY — Use May 18–21 for hourly monitoring
scope: "Wave 1 execution monitoring, Phase 1 success measurement, Phase 2 approval gate"
audience: "thorn — read May 17 evening or May 18 morning; reference document through May 21"
companion_files:
  - PHASE_1_WAVE1_EXECUTION_PREP.md
  - POST_WAVE_1_SYNTHESIS_AND_TIER2_TRANSITION.md
  - assessment/phase-1-baseline-metrics.md
  - measurement-and-iteration-framework.md
---

# Post-Wave 1 Phase 1 Measurement Framework

**Purpose**: This is your operational reference for the 72 hours following May 18 send. It gives you hourly monitoring structure, pass/fail thresholds, decision rules for Batch 2/3 and Phase 2, a dashboard specification, contingency scenarios, and the Domain 42 integration timeline.

**How to use**: Read this document once before launch. Then return to Section 1 each time you sit down to check signals. All other sections are reference material for decisions that arise from what you observe.

---

## 1. Wave 1 Execution Checklist and Monitoring Timeline

### Pre-Send Block: May 18 07:00–09:00 UTC

Before any email leaves your outbox, confirm:

- [ ] All 5 Gist URLs load in incognito (main proposal, exec summary, litigation tracker, Domain 37, Domain 42)
- [ ] Test email to yourself delivered to inbox, not spam, within 3 minutes
- [ ] All 5 templates: zero `{{...}}` placeholders remain
- [ ] All 5 templates use Path A+37 block only — PATH A and PATH B paragraphs deleted
- [ ] Elias email uses `melias@elias.law` (not perkinscoie.com)
- [ ] Callais framing: "decided April 29, 2026 — redistricting cascade underway" (not "pending")
- [ ] Record Gist view count baseline (manual incognito check) for all 5 Gists
  - Main proposal baseline: ___
  - Executive summary baseline: ___
  - Litigation tracker baseline: ___
  - Domain 37 baseline: ___
  - Domain 42 baseline: ___

**If any checkbox is unchecked: do not send. Resolve the blocker first. A 2-hour delay is not a failure; a broken email to Marc Elias is.**

---

### Send Block: May 18 09:00–10:30 UTC

| Time (UTC) | Action | Log Entry |
|------------|--------|-----------|
| 09:00 | Send Email 1: Ryan Goodman — ryan.goodman@nyu.edu | Time sent: ___ |
| 09:10 | Check sent folder — confirm no bounce notification at 10 min | Bounce? Y/N |
| 09:15 | Send Email 2: Wendy Weiser — wweiser@brennancenter.org | Time sent: ___ |
| 09:30 | Send Email 3: Erica Chenoweth — erica_chenoweth@hks.harvard.edu | Time sent: ___ |
| 09:45 | Send Email 4: Ian Bassin — ian@protectdemocracy.org | Time sent: ___ |
| 10:00 | Send Email 5: Marc Elias — melias@elias.law | Time sent: ___ |
| 10:15 | Check for any bounce notifications across all 5 | Bounce count: ___ |
| 10:30 | Scan inbox for any immediate out-of-office replies (confirms delivery) | OOO received from: ___ |

**Record post-send Gist baselines at 10:30 UTC** (immediately after last send, before any contact opens links). These are your H+0 counts.

---

### Hours 0–6: May 18 09:00–15:00 UTC — Initial Monitoring

**Check at H+1 (10:00 UTC), H+3 (12:00 UTC), H+6 (15:00 UTC)**

At each checkpoint:

1. **Bounce check**: Any delivery failure notifications? If yes, go immediately to Contingency Scenario A.
2. **Out-of-office detection**: An OOO reply is a *positive* signal — it confirms delivery. Log recipient name and return date.
3. **Early reply scan**: Any substantive reply within 6 hours is exceptional. Goodman and Elias have the fastest reply cycles (48–72 hours typical); do not expect replies in this window, but log any that arrive.
4. **Gist view count delta**: Check all 5 Gists. Record current count minus baseline. Target: 0–5 views at H+6 (institutional contacts on .edu often read email hours after receipt).

**H+6 Status Entry** (write 2 sentences in your log):
- "Sends: X of 5 confirmed delivered, Y bounced. Gist view delta: Z views. Early replies: [names or 'none']."

---

### Hours 6–24: May 18 15:00 UTC — May 19 09:00 UTC — Initial Engagement Window

This is the primary first-day engagement window. Most institutional contacts check morning email between 09:00–11:00 their local time. East Coast recipients (Goodman, Weiser, Bassin, Elias) will see the email in their late morning on May 18; Harvard's Chenoweth is also Eastern.

**Check at H+8 (17:00 UTC), H+12 (21:00 UTC), H+24 (09:00 UTC May 19)**

At each checkpoint:

1. **Reply classification**: Any replies? Classify immediately using this taxonomy:
   - **Integration signal** — contact explicitly mentions applying the framework to current work. Highest value.
   - **Implementation question** — contact asks how to use a specific domain operationally.
   - **Referral** — contact offers to forward to a colleague or team member.
   - **Clarification question** — contact asks about a specific claim, citation, or domain.
   - **Critique** — substantive methodological or factual challenge. This is also high-value.
   - **Acknowledgment only** — "Thanks, I'll take a look." Low value but confirms receipt.
   - **Decline** — "Not relevant to my work right now."
   - **No reply** — normal at H+24; not a signal yet.

2. **Gist view count delta**: Check all 5 Gists. Expected at H+24: 5–15 views across all 5 Gists if contacts have opened and clicked through. A single institutional reader opening all 5 Gists = 5 views. Two or three contacts clicking = 10–25 views.

3. **Forwarding signal check**: Scan for any view-count spikes above 3x the individual contact average. A single contact who forwarded to their team will spike the Gist count.

**H+24 Status Entry**:
- "Reply count: X of 5. Classifications: [list types]. Gist delta H+24: Z. Notable: [anything unusual]."

---

### Hours 24–48: May 19 09:00 UTC — May 20 09:00 UTC — Full Response Window

This is the highest-yield monitoring period. Based on the Phase 1 baseline metrics (phase-1-baseline-metrics.md Section 2), Batch 1 personalized outreach to senior institutional leaders should yield 15–25% reply rate at 48 hours, potentially 30–40% with this level of personalization.

**Check at H+36 (21:00 UTC May 19), H+48 (09:00 UTC May 20)**

At each checkpoint:

1. **Reply rate running total**: How many of 5 have replied? This is your leading indicator for tier assessment.
2. **Domain pull identification**: Which domains are contacts asking about? Log every domain mentioned. This directly informs Phase 2 sequencing.
3. **Forwarding chain detection**: Has any contact mentioned forwarding or copied someone new? Log the new contact name and organization — this is a warm introduction for Batch 2.
4. **Gist view velocity**: Are views accelerating or flat? Acceleration (view rate increasing day-over-day) signals organic sharing. Flat views after H+48 suggests limited forwarding.
5. **Policy uptake signal watch**: Any reply that mentions "we're working on X brief" or "this would be relevant for our upcoming Y" is a policy uptake signal. Flag immediately.

**H+48 Status Entry**:
- "Reply rate: X/5 (Y%). Domain pull: [list]. Forwarding signals: [list or 'none']. Policy uptake signals: [describe or 'none']. Gist total views: Z."

---

### Hours 48–72: May 20 09:00 UTC — May 21 09:00 UTC — Extended Window + Initial Analysis

This window catches slower responders (Harvard and Brennan Center have 5–10 day cycles; some Batch 1 replies will arrive here). It is also the window for initial synthesis.

**Check at H+60 (21:00 UTC May 20), H+72 (09:00 UTC May 21)**

At each checkpoint:

1. **Secondary contact requests**: Any new contacts introduced by Batch 1 contacts? These are warm entry points for Batch 2.
2. **Reply depth assessment**: For any replies received, are they getting deeper? A follow-up question after an initial acknowledgment signals increasing engagement.
3. **Silence pattern analysis**: If 2 or more Batch 1 contacts have not replied by H+72, check whether their silence follows a pattern (same organization type? same domain focus?). Silence at H+72 is not failure — Chenoweth and Weiser are the slower responders. But if Goodman and Elias (fastest cycle contacts) are both silent, something may be wrong.
4. **H+72 Gist view count final snapshot**: Record all 5 Gist counts. This is your baseline for the initial analysis.

**H+72 Initial Analysis** (30 minutes, May 21 morning UTC):
- Pull all data from H+0 through H+72 into a summary table
- Calculate reply rate (X/5), engagement classification breakdown, domain pull distribution, Gist view total
- Compare to targets in Section 2
- Make the preliminary PASS/NEAR-MISS/FAR-MISS determination
- Write 1-paragraph "state of play" entry — this feeds the Phase 2 approval gate decision in Section 5

---

## 2. Phase 1 Success Metrics Framework

### The Four Measurement Tiers

The following targets are calibrated against the benchmarks in `assessment/phase-1-baseline-metrics.md` Section 2, which establishes a 15–25% adjusted reply rate baseline for personalized senior-leader outreach and a "high engagement threshold" of engagement score ≥3.5.

---

#### Tier (a): Batch 1 Response Rates

Primary behavioral signal. Because Batch 1 is intentionally small (5 contacts), these are qualitative thresholds, not statistical ones.

| Metric | FAR-MISS | NEAR-MISS | PASS | EXCELLENT |
|--------|----------|-----------|------|-----------|
| Reply rate by H+72 | 0–1 replies (0–20%) | 2 replies (40%) | 3 replies (60%) | 4–5 replies (80–100%) |
| Average engagement score | Below 1.5 | 1.5–2.4 | 2.5–3.4 | 3.5+ |
| Integration signals (contacts mentioning use in work) | 0 | 0 | 1+ | 2+ |
| Implementation questions (how-to-use) | 0 | 1 | 1–2 | 3+ |
| Acknowledgment-only responses | Majority of replies | Half of replies | Minority | None |

**Scoring method**: The engagement scoring formula from `POST_WAVE_1_SYNTHESIS_AND_TIER2_TRANSITION.md` Phase 1.2 applies:
```
engagement_score = (reply_score × 0.6) + (gist_clicks × 0.2) + (opened_24h × 0.2)
```
Reply scores: Integration signal = 5, Implementation question = 4, Referral = 4, Clarification = 3, Critique = 3, Acknowledgment = 1, Decline = 0, No reply = 0.

**Domain pull distribution** (secondary metric within Tier a): Which domains are generating engagement? Log by domain. If Domain 37 (election protection) is generating 2x+ mentions relative to other domains, this is an amplifying signal consistent with the Path A+37 strategy. If Domain 1 (voting rights) or Domain 58 (tribal sovereignty, if included) are generating early pull, note for Phase 2 sequencing.

---

#### Tier (b): Forward and Share Rates

Forwarding is the highest-value short-window signal because it indicates the contact judged the material worth routing to institutional colleagues.

| Metric | Target | How to Detect |
|--------|--------|---------------|
| Explicit forwarding offer ("I'll send this to...") | 1+ by H+72 | Reply content |
| New contact introduced by Batch 1 | 1+ by H+72 | Reply CC, or "you should talk to X" |
| Gist view count spike (3x individual-contact average) | 1+ Gist | View count monitoring |
| Out-of-organization reach (contact mentions it to someone outside their org) | Any | Reply content |

**Forward chain tracking template**: When a Batch 1 contact forwards, create an entry:
```
Contact who forwarded: [Name]
Forwarded to: [Name, Organization if known]
Date detected: [Date]
Context: [Quote or paraphrase from reply]
Warm intro available? [Y/N — if Y, use for Batch 2 outreach]
```

**Target for PASS**: 1 forwarding chain confirmed by H+72.
**Target for EXCELLENT**: 2+ forwarding chains, reaching organizations not on the Batch 2 list.

---

#### Tier (c): Policy Uptake Signals

Policy uptake signals are replies or inferred behaviors indicating that a contact plans to use the framework in an active work product (brief, hearing, report, litigation, testimony).

| Signal Type | Definition | Detection |
|-------------|------------|-----------|
| Explicit integration | Contact says "I'm using this for [specific work product]" | Reply content |
| Brief-relevant mention | Contact mentions a pending case, filing, or hearing the framework applies to | Reply content |
| Organizational routing | Contact says they're forwarding to their policy, legal, or comms team | Reply content |
| Follow-up request | Contact asks for a specific domain's deeper materials | Reply content + additional Gist views |
| Call request | Contact proposes a call to discuss | Reply content |

**Target for PASS**: 1 policy uptake signal by H+72.
**Target for EXCELLENT**: 2+ policy uptake signals, including at least one explicit integration or call request.

**Note on attribution lag**: True policy uptake (a brief that cites the framework, a Senate hearing background memo) will not be detectable within 72 hours. What you are measuring in this window is *intent signals*, not confirmed adoption. Confirmed adoption tracking follows the 30/60/90-day methodology in `measurement-and-iteration-framework.md` Part I.

---

#### Tier (d): Reputational Amplification

The least time-sensitive metric but worth establishing a H+72 baseline.

| Signal | Expected at H+72 | Tracking Method |
|--------|-----------------|-----------------|
| Framework-specific media mention | 0 (too early) | Google Alerts — set up if not already live |
| Academic social media share | 0–1 (possible from Chenoweth) | Manual Bluesky/Twitter scan for names |
| External citation in published work | 0 (minimum lag: 2 weeks) | Google Scholar alert (set up now) |
| Mention in a newsletter or blog | 0 (minimum lag: 1 week) | Manual scan of Just Security, Democracy Docket |

**H+72 baseline action**: Set up Google Alerts for "35-domain framework", "democratic renewal proposal", "prosecutorial weaponization 22 cases" if not already running. These produce no results now (verified per `assessment/phase-1-baseline-metrics.md` Section 1) — any hit that appears in the days following the send is attributable to Wave 1.

---

### Overall Pass/Near-Miss/Far-Miss Determination

**PASS**: 3 or more of the 4 tiers meet their targets as defined above. Specifically:
- Tier (a): 3+ replies by H+72, average engagement score ≥2.5, at least 1 integration or implementation signal
- Tier (b): 1+ confirmed forwarding chain
- Tier (c): 1+ policy uptake signal
- Tier (d): N/A at H+72 — upgraded to a metric by May 28

PASS triggers: Batch 2 launch on schedule (May 22, 15 contacts).

**NEAR-MISS**: Exactly 2 of the 4 tiers meet their targets. Common NEAR-MISS patterns:
- Pattern 1: Good reply rate (Tier a PASS) but no forwarding (Tier b miss) and no policy uptake (Tier c miss) — indicates the message is landing but not catalyzing. Response: adjust Batch 2 outreach to include a more specific operational ask.
- Pattern 2: Good reply rate and forwarding (Tiers a+b PASS) but no policy uptake signals (Tier c miss) — indicates broad interest but no immediate activation. Response: proceed with Batch 2 but include domain-specific one-pagers for Batch 2 contacts.
- Pattern 3: Low reply rate (Tier a miss) but 1 policy uptake signal from the replies received (Tier c PASS) — indicates the contacts who engaged are high-quality. Response: proceed with Batch 2 focused on the sectors that generated the policy uptake signal.

NEAR-MISS triggers: Modified Batch 2 launch (see Section 3).

**FAR-MISS**: 0–1 of the 4 tiers meet their targets. Requires diagnostic sequence before any further sends (see Contingency Scenarios in Section 7).

---

### Secondary Metrics: Operational Intelligence

Collect these regardless of PASS/NEAR-MISS/FAR-MISS outcome. They inform Batch 2/3 sequencing.

| Secondary Metric | What to Record | Why It Matters |
|-----------------|----------------|----------------|
| Median reply time | Hours from send to first reply | Faster reply = more time-pressured need; informs subject line framing for Batch 2 |
| Domain distribution of questions | Which domains are mentioned by name | Direct input to Phase 2 domain prioritization |
| Contact type of highest responders | Academic, legal, policy org | Indicates which sector has highest near-term activation potential |
| Question patterns | What are people confused about? | Reveals framing gaps for Batch 2 template revision |
| Geographic / institutional clustering | Are replies clustering around one organization type? | If 3 of 5 replies come from legal (Goodman, Elias, Bassin), that is a sector signal |
| OOO return dates | When will non-replies be back? | Determines whether silence is permanent or temporary |

---

## 3. Phase 1 Batch 2 and 3 Decision Framework

### The Three Decision Paths

#### Path A: Wave 1 PASS — Launch Batch 2 May 22

**Trigger**: PASS determination from Section 2.

**Batch 2 Configuration** (15 contacts, May 22 send):
Expand from Wave 1 core (law, policy org) to Tier 2 academic and think-tank contacts. The full Tier 2 contact list is in `execution/tier-2-organizational-contact-list.md`. Priority contacts for Batch 2:

*Academic track (priority contacts for Batch 2 A)*:
- Steven Levitsky (Harvard, comparative authoritarianism) — use Chenoweth engagement as social proof in personalization
- Daniel Ziblatt (Harvard, democratic backsliding) — same social proof approach
- Jack Balkin (Yale Law, constitutional crisis) — use Goodman engagement signal as warm framing
- Heather Gerken (Yale Law Dean, democracy and election law) — connect to Domain 37 and Callais cascade
- Samuel Issacharoff (NYU Law, election law) — Elias connection as social proof; Watson v. RNC hook

*Think tank track (priority contacts for Batch 2 A)*:
- CAP Democracy team (Maya Wiley or current VP Democracy equivalent) — use Bassin/Protect Democracy engagement as bridge
- Brookings Institution (election security or democracy fellow) — connect to Domain 37 five-mechanism taxonomy
- ACLU Voting Rights Project (director) — Callais cascade + Watson v. RNC pending; direct Domain 1 hook
- Common Cause (national policy director) — election administration + Domain 37 operational hook
- Democracy Forward (litigation director) — executive overreach domains; use Elias engagement signal

*Election-protection track (Domain 37 Hybrid, priority for Batch 2 A+37)*:
Due to Path A+37 selection, 5–7 of the 15 Batch 2 slots should be election-protection orgs receiving the Domain 37 supplemental Gist (https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0):
- State Voices (election infrastructure coordination)
- Verified Voting Foundation
- CISA Advisory Council contact (if accessible)
- National Vote at Home Institute (mail voting EO challenge context)
- Election Protection Coalition (866-OUR-VOTE) director

**Batch 2 send protocol**: Same 15-minute send spacing as Batch 1. Send in three sub-groups of 5 on May 22, 23, 24 to maintain response tracking clarity. Do not send all 15 in one burst.

---

#### Path B: Wave 1 NEAR-MISS — Modified Batch 2

**Trigger**: NEAR-MISS determination from Section 2.

**Modified Batch 2 strategy**: Focus on warm-introduction pathways rather than cold Batch 2 sends.

**Step 1 — Leverage Batch 1 engagement**: For every Batch 1 contact who replied (even acknowledgment-only), send a brief follow-up by May 21:
> "Thank you for your response. Given your work on [their specific domain], could you suggest a colleague who focuses particularly on [election law / comparative backsliding / prosecutorial accountability]? I'm expanding outreach to a small set of additional contacts before wider distribution."

This converts existing engagement into warm introductions for Batch 2.

**Step 2 — Sector-focused targeting**: If NEAR-MISS was driven by good replies from legal contacts (Goodman, Elias) but silence from academic/policy org contacts (Weiser, Chenoweth, Bassin), concentrate Batch 2 on the legal sector:
- Law school election law clinics (Michigan, Stanford, Arizona)
- Democracy Docket staff counsel (beyond Elias himself)
- Elias Law Group associates who may engage independently
- NAACP LDF voting rights team

**Step 3 — Modified ask**: NEAR-MISS Batch 2 emails should include a more specific, lower-friction ask than Wave 1. Instead of "I'd value your feedback on this framework," use: "I'm specifically seeking practitioners who can verify whether the Domain 37 five-mechanism analysis matches your operational experience. 20 minutes by phone or a written response to two questions would be sufficient."

**Modified Batch 2 target**: 10 contacts (not 15), focused on warm introductions and high-sector-alignment contacts only. Launch May 22–24.

---

#### Path C: Wave 1 FAR-MISS — Diagnostic Sequence

**Trigger**: FAR-MISS determination from Section 2 (0–1 tiers meeting targets).

**Do not send Batch 2 until diagnostic is complete.**

Diagnostic sequence (see full detail in Section 7 Contingency Scenarios):

1. **Email delivery check** (30 min): Verify all 5 contacts via institutional directory. Re-confirm email formats. Check spam folder on sending account. If any email bounced and wasn't caught, resend to fallback address.
2. **Contact list quality check** (30 min): Are all 5 contacts still in the roles verified in the Wave 1 Execution Prep? If any contact has changed roles since May 15, the personalization hook may have misfired.
3. **Domain quality check** (30 min): Re-read the email you sent to one contact in full. Does the personalization accurately reference their recent work? Does the domain hook connect to their current priorities?
4. **Message framing check** (20 min): Does the email clearly state what you want from the contact? Is the ask specific and low-friction? Did you include the Path A+37 block without the deleted Path A and B blocks (clean template)?

**After diagnostic**: If delivery failure confirmed — resend to fallback addresses and reset the clock to H+0. If framing failure confirmed — revise templates, test with 2 contacts, do not scale to Batch 2 until 1 revised-template response is received.

---

### Batch 3 Positioning

Batch 3 (additional 20–25 contacts, state-level and coalition orgs) follows Batch 2 by 5–7 days regardless of path. Batch 3 has the same structure as Path A Batch 2 but focuses on:
- State-level election officials and AG democracy programs
- Civil rights coalition directors (NAACP LDF, Lawyers' Committee)
- Labor organizations (EPI, AFL-CIO Democracy Program)

Batch 3 benefits from any social proof generated by Batch 1 and 2 replies. If Goodman or Weiser has replied substantively, name them in the Batch 3 personalization ("this framework has received early engagement from [Just Security / Brennan Center] — I'm expanding to a small set of state-level practitioners").

---

## 4. Phase 1 Measurement Dashboard Template

### Tab Structure

Create this as a Google Sheet with 5 tabs. All tabs draw from the same source entries in Tab 1.

---

#### Tab 1: Daily Contact Tracking

**One row per contact-event** (each reply, each check-in, each new signal). Not one row per contact.

| Field | Type | Instructions |
|-------|------|-------------|
| Date | Date | YYYY-MM-DD |
| Contact name | Text | Full name |
| Organization | Text | Org abbreviation (BCJ, DD, HKS, etc.) |
| Batch | Number | 1, 2, or 3 |
| Event type | Dropdown | Send / OOO / Reply / Bounce / Forwarding-signal / Gist-spike / Call-request |
| Reply type | Dropdown | Integration / Implementation / Referral / Clarification / Critique / Acknowledgment / Decline / None |
| Domains mentioned | Text | Comma-separated domain numbers (e.g., "1, 37, 57") |
| Engagement score | Number | Calculate per formula: (reply_score × 0.6) + (gist_clicks × 0.2) + (opened_24h × 0.2) |
| Forward chain? | Boolean | Y/N — if Y, add new contact in next row |
| Policy uptake signal? | Boolean | Y/N — if Y, describe in Notes |
| Notes | Text | Quote or paraphrase the key signal content |

**Example entries**:
```
2026-05-18 | Goodman | Just Security | 1 | Send | None | — | 0 | N | N | Sent 09:00 UTC
2026-05-18 | Goodman | Just Security | 1 | OOO | None | — | 0 | N | N | Returns May 19 — confirmed delivery
2026-05-19 | Goodman | Just Security | 1 | Reply | Implementation | 28, 29 | 3.4 | N | Y | "Would be useful for our OLC series — can you expand on the Venezuela hybrid theory?"
```

**Sort order**: By date descending (most recent at top). Filter by "Batch" column to isolate Batch 1 view during early monitoring.

---

#### Tab 2: Weekly Summary — 7 KPI Metrics

Update this tab every Monday (or every Sunday evening). The 7 KPIs:

| KPI # | Metric | Week 1 (May 18–24) Target | Week 2 (May 25–31) Target | Cumulative Target (30 days) |
|-------|--------|--------------------------|--------------------------|----------------------------|
| KPI-1 | Batch 1 reply rate (%) | 40–60% | — | — |
| KPI-2 | Average engagement score | 2.5+ | 2.5+ across all batches | 2.5+ |
| KPI-3 | Integration signals (count) | 1+ | 2+ | 4+ |
| KPI-4 | Active forwarding chains (count) | 1+ | 2+ | 4+ |
| KPI-5 | Policy uptake signals (count) | 1+ | 2+ | 5+ |
| KPI-6 | New contacts introduced via warm intro | 0–2 | 3–5 | 10+ |
| KPI-7 | Domain pull distribution (top 2 domains) | Record | Record | Identify top 3 |

**Status coding for each KPI**:
- Green (On Track): At or above linear interpolation between Day 0 and 30-day target
- Yellow (Watch): 50–80% of interpolated target
- Red (Action Required): Below 50% of interpolated target

**Chart framework** (optional for visual overview): A single sparkline per KPI showing weekly trend. In Google Sheets: `=SPARKLINE(B2:G2)` across the weekly data columns gives an inline trend indicator.

---

#### Tab 3: Engagement Source Tracking

Tracks which contacts are generating the most downstream activity (forwarding, introductions, policy uptake signals).

| Contact | Org | Batch | Reply? | Forwarded? | New contacts introduced | Policy uptake signals | Domains mentioned | Overall influence score |
|---------|-----|-------|--------|------------|------------------------|----------------------|-------------------|------------------------|
| Ryan Goodman | Just Security | 1 | — | — | — | — | — | — |
| Wendy Weiser | Brennan Center | 1 | — | — | — | — | — | — |
| Erica Chenoweth | Harvard HKS | 1 | — | — | — | — | — | — |
| Ian Bassin | Protect Democracy | 1 | — | — | — | — | — | — |
| Marc Elias | Elias Law Group | 1 | — | — | — | — | — | — |

**Overall influence score** = (reply_engagement_score) + (forwarding_chains × 2) + (policy_uptake_signals × 2) + (new_contacts × 1.5)

A contact with a low engagement score but high influence score (e.g., replied briefly but forwarded to 3 colleagues) should be prioritized for follow-up.

**Domain traction by contact**: If Goodman mentions Domains 28/29 and Elias mentions Domains 1/37, the combined picture indicates your legal contacts are engaging with executive overreach and election interference domains specifically. This informs which domains to lead with in Batch 2.

---

#### Tab 4: Policy Uptake Tracker

A dedicated tab for confirmed organizational interest in applying the framework.

| Date | Contact | Organization | Domain(s) | Signal type | Work product mentioned | Status | Next action | Notes |
|------|---------|-------------|-----------|-------------|----------------------|--------|-------------|-------|
| — | — | — | — | Explicit integration / Briefing request / Call request / Org routing | (hearing, brief, report, campaign, etc.) | Pending / Active / Confirmed | Follow up by [date] | — |

**Signal type definitions**:
- **Explicit integration**: Contact says they are using the framework for a named work product.
- **Briefing request**: Contact asks for a domain-specific briefing (indicates operational interest).
- **Call request**: Contact wants a phone or video conversation (indicates high engagement).
- **Org routing**: Contact has forwarded to their policy, legal, or comms team (indicates organizational process is engaged).

**For each confirmed policy uptake signal**: Schedule a follow-up within 5 business days. The follow-up offer is a domain-specific brief (2–3 pages) tailored to their stated work product — see `measurement-and-iteration-framework.md` Part V (Institutional Adoption Facilitation steps 1–5) for the full facilitation sequence.

---

#### Tab 5: Reply Sentiment Classifier

Classifies all replies received by sentiment category for trend monitoring.

**Four categories**:

| Category | Definition | Implication |
|----------|------------|-------------|
| Enthusiastic Adopt | Contact expresses clear intent to use the framework; may ask operational questions | Follow up within 2 days; offer domain brief |
| Cautious Interest | Contact is engaged and asking questions but non-committal about use | Follow up at 2 weeks; send domain-specific brief proactively |
| Resource Constrained | Contact acknowledges value but cites capacity limitations ("too busy right now") | Set 90-day follow-up; convert "not now" to conditional commitment |
| Low Interest | Generic reply or decline; no domain-specific engagement | Log and close for now; revisit in Wave 3 if relevance increases |

**Tally by batch** (updated weekly):

| Sentiment | Batch 1 (5 contacts) | Batch 2 (15 contacts) | Batch 3 (25 contacts) | Total |
|-----------|---------------------|----------------------|----------------------|-------|
| Enthusiastic Adopt | — | — | — | — |
| Cautious Interest | — | — | — | — |
| Resource Constrained | — | — | — | — |
| Low Interest / No Reply | — | — | — | — |

**Threshold watch**: If "Resource Constrained" category is growing disproportionately (3+ of 5 Batch 1 contacts), this signals that the timing or ask volume may be wrong. Consider whether a more modest initial ask would convert more contacts to "Enthusiastic Adopt." If "Low Interest" dominates after Batch 2, initiate the framing-failure diagnostic (Contingency Scenario C).

---

## 5. Phase 2 Approval Gate Criteria

### What Phase 2 Is

Phase 2 refers to the expanded research track: new domain research (Domains 38–42 and others from the Phase 2 candidates list), broader distribution to Tier 2 and Tier 3 contacts, and potential publication-adjacent activity (op-ed pitches, Substack strategy, law review engagement). The Phase 2 target start is May 22+, with a 4–6 week research and distribution sprint through late June.

### Objective Gate Criteria

Phase 2 launch requires confirmation of ALL four of the following:

**Gate 1 — Phase 1 PASS or NEAR-MISS Confirmed**:
Section 2 PASS/NEAR-MISS determination is made (not FAR-MISS). FAR-MISS triggers diagnostic sequence first; Phase 2 does not launch until the diagnostic produces a NEAR-MISS or better on the revised send.

**Gate 2 — Minimum 2 Policy/Org Uptake Signals**:
At least 2 contacts across Batch 1 and 2 have indicated organizational interest in applying the framework. This can be: 2 integration signals from Batch 1, or 1 Batch 1 signal + 1 Batch 2 signal, or a confirmed forwarding event where the downstream contact also signaled interest. The threshold is 2 because a single signal could be an outlier; two independent signals from different organizations indicate meaningful pull.

**Gate 3 — No Significant Negative Feedback**:
No pattern of substantive negative feedback that would require framework revision before wider distribution. A single critique is not disqualifying (and is valuable). A pattern — two or more contacts raising the same factual or framing objection — requires review before Phase 2. The revision rule from `measurement-and-iteration-framework.md` Part III applies: "two or more Tier 1 contacts expressing the same concern within 30 days triggers revision queue."

**Gate 4 — User Approval Decision**:
The user (thorn) reviews the H+72 analysis and makes an explicit go/no-go call. No Phase 2 activity launches autonomously. The gate-4 check-in is scheduled for May 20 evening UTC (after H+72 data is collected, before Batch 2 send date of May 22).

---

### Phase 2 Decision Options

#### Option A: Immediate Phase 2 Research Start (May 22+, Aggressive Timeline)

**Trigger**: PASS + 2+ uptake signals + no negative feedback pattern.

**Research track**:
- Begin Phase 2 domain research on highest-demand domains identified from Phase 1 domain pull
- Domains 38–42 from Phase 2 candidates list; Domain 42 (DEA hearing) has hard deadline (see Section 6)
- Target: 2 new Phase 2 domains complete by June 15

**Distribution track**:
- Batch 2 send May 22 (15 contacts)
- Batch 3 send May 27 (20–25 contacts)
- Domain 42 amplification send May 22–26 (see Section 6 for contact subset)

**Timeline**: May 22 → Batch 2 → May 28 (Domain 42 DEA deadline) → May 31 analysis → June 1 Batch 3 → June 15 Phase 2 domain draft #1 complete.

**Option A is correct when**: Wave 1 shows institutional demand and the research pipeline should accelerate to meet it. Do not delay Phase 2 when there is confirmed pull.

---

#### Option B: Extended Phase 1 Before Phase 2 (1–2 Additional Weeks)

**Trigger**: NEAR-MISS + some uptake signals but below the 2-signal threshold, or Gate 3 requires template revision.

**What changes**: Delay Phase 2 research by 1–2 weeks. Use the extension period to:
- Complete Batch 2/3 outreach and gather 2+ uptake signals before beginning Phase 2 domain research
- If Gate 3 triggered, revise 1 or more email templates based on the feedback pattern and re-test with 3 contacts before Batch 3

**Timeline**: Batch 2 sends May 22–24 → full response window May 22–28 → Phase 2 gate re-evaluated May 28 → Phase 2 launch June 1–3 if gates pass.

**Option B is correct when**: Wave 1 data is directionally positive but there is insufficient signal clarity to justify the research investment. The extra 1–2 weeks typically yield 3–5 additional contacts who provide the uptake signals needed for confident Phase 2 sequencing.

---

#### Option C: Phase 2 Pilot with Subset (3 of 4 Domains, Defer Others)

**Trigger**: PASS or NEAR-MISS but domain pull is concentrated in specific domains, or Phase 2 research capacity is limited.

**What changes**: Begin Phase 2 research only on the 3 domains with confirmed Phase 1 pull. Defer research on low-demand Phase 2 domains until Month 2–3.

**Selection rule**: Choose Phase 2 research domains based on the domain pull distribution from Tab 7 (weekly KPI summary). If Domains 37, 1, and 57 dominate the pull distribution, begin Phase 2 research on those 3. If Domain 42 has the hard DEA deadline (May 28), it automatically gets a slot regardless of pull metrics.

**Timeline**: Same as Option A, but research scope is restricted. Produces faster, higher-quality output on the most-demanded domains rather than broader but shallower coverage.

**Option C is correct when**: You want to accelerate on what's working and not over-invest in domains that Phase 1 feedback suggests may need different framing before they gain traction.

---

### Decision Tree

```
Wave 1 PASS?
├── YES → Gate 2: 2+ uptake signals?
│   ├── YES → Gate 3: No negative feedback pattern?
│   │   ├── YES → Gate 4: User approval?
│   │   │   ├── YES → Option A (aggressive) or C (focused) → Launch May 22
│   │   │   └── NO → Hold for user decision
│   │   └── NO → Revise templates → Option B → Re-evaluate May 28
│   └── NO → Option B (extend Phase 1) → Re-evaluate May 28
├── NEAR-MISS → Option B → Modified Batch 2 → Re-evaluate May 28
└── FAR-MISS → Diagnostic sequence (Section 7) → Re-evaluate after diagnostic
```

---

## 6. Domain 42 (DEA Hearing) May 28 Integration

### What Domain 42 Is

Domain 42 covers the DEA hearing scheduled for May 28, 2026. The associated Gist is confirmed live at https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab. This is a hard-deadline domain — any distribution or amplification that aims to influence the hearing or related comment periods must land by approximately May 26 to allow recipients time to act.

### Timeline Integration

```
May 18 (06:00 UTC)     → Wave 1 send (5 contacts; Domain 42 Gist included in infrastructure but not primary focus)
May 18–20              → Monitoring window (watch for Domain 42 mentions in replies)
May 20 (evening UTC)   → H+72 analysis + Phase 2 gate review
May 22–23              → Batch 2 send (15 contacts); Domain 42 secondary wave targeting (5-7 contacts, subset below)
May 24–25              → Batch 3 prep; Domain 42 comments may be filing-window ready for engaged contacts
May 26                 → Last day for Domain 42 amplification to reach contacts with time to act
May 28                 → DEA hearing — internal checkpoint: measure any Domain 42 forwarding chain activity
May 28 (end of day)    → Phase 1 → Domain 42 forwarding chain analysis: did any Batch 1/2 contact use Domain 42 content?
```

### Contact Subset for Domain 42 Amplification (Batch 2/3 Secondary Wave)

Within the Batch 2 and 3 contact lists, identify contacts with specific DEA-adjacent relevance:

**Primary DEA-relevant contacts** (send Domain 42 Gist as supplemental with Batch 2 email, May 22–23):
- ACLU Drug Policy project director or equivalent — DEA administrative procedures intersect with civil liberties domains
- Drug Policy Alliance contacts — organizational mandate directly relevant; high probability of comment filing
- NORML or equivalent cannabis law reform organization — if within Batch 2/3 scope
- Harm Reduction Coalition contacts — DEA scheduling decisions affect harm reduction policy
- Any medical professional organizations within your contact universe that engage on scheduling or prescribing rules

**For contacts in this subset**: Add a specific Domain 42 paragraph to their email:
> "Given your work on [drug policy / DEA administrative procedure], I want to flag Domain 42 specifically — it covers the May 28 DEA hearing and the structural context for the scheduling review. The Gist is at [Domain 42 URL]. If you or your colleagues are considering filing comments, the domain analysis may be directly relevant to the statutory and administrative arguments."

**Secondary DEA-relevant contacts** (forwarding target, Batch 3 or warm intro):
- Law school administrative law clinics — DEA proceedings are standard administrative law material
- Center for American Progress or Brookings health policy staff — drug policy intersects with broader healthcare domains
- Any Senate HELP Committee or Judiciary Committee staff contacts accessible via existing warm intros

### Domain 42 Forwarding Chain Tracking

Create a separate row category in Tab 1 (Daily Contact Tracking) for Domain 42-specific events:

```
2026-05-22 | [Contact] | [Org] | 2 | Send | None | 42 | — | N | N | Domain 42 supplemental included
2026-05-25 | [Contact] | [Org] | 2 | Reply | Policy uptake | 42 | 4.2 | Y | Y | "Forwarding to our policy team for comment filing"
```

**May 28 internal checkpoint measurement**: At end of day May 28, log:
- How many contacts received the Domain 42 Gist (primary + supplemental sends)?
- How many showed specific Domain 42 engagement (views, domain-specific replies)?
- How many forwarded Domain 42 materials?
- Was the Domain 42 Gist referenced in any observable comment filing activity?

This checkpoint produces the Phase 1 → Domain 42 forwarding chain analysis that feeds Phase 2 domain sequencing for the DEA-adjacent Domains 43–45 range.

### Domain 42 Messaging Variants

**Time-urgency framing** (use for contacts with institutional capacity to file comments):
> "The DEA hearing is May 28 — Domain 42 is timed specifically to this window. If your organization is considering a comment or amicus position, the analysis is available now at [URL]."

**Research-framing** (use for academic contacts without comment-filing capacity):
> "Domain 42 covers the DEA hearing as a case study in administrative rulemaking under political pressure. Given your research on [executive unilateralism / administrative state], this may be a useful current-event hook."

**Coalition-framing** (use for civil rights or advocacy organizations):
> "The Domain 42 analysis connects the DEA hearing to the broader pattern of executive use of administrative procedure to achieve policy outcomes without legislation — the same pattern as Domains 25 (FISA), 26 (civil service), and 34 (congressional authority). If your coalition is working on any of these adjacent domains, Domain 42 adds a current hook."

---

## 7. Contingency Scenarios and Recovery Paths

### Scenario A: Email Delivery Failure

**Definition**: One or more Wave 1 emails bounced, or no reply from any of 5 contacts and no OOO receipts by H+48 (absence of any signal at all).

**Detection**: Bounce notifications in inbox, or visible non-delivery report. If zero OOO replies after H+48, also suspect delivery.

**Diagnostic steps** (30 min):
1. Check spam folder on sending account — some email clients file bounce notifications as spam.
2. Verify all 5 email addresses against institutional directory right now (takes 5 min per contact; institutional pages update faster than any stored list).
3. Send a test email to yourself from the same sending account — did it arrive? If not, your sending account may be flagged.
4. Check SMTP logs if accessible on your email provider.

**Recovery protocol**:
- For specific bounced address: Resend within 24 hours to fallback address (all fallbacks are in `PHASE_1_WAVE1_EXECUTION_PREP.md` Section 1 table). Use a revised subject line — remove any of: "framework," "reform" as standalone noun phrases.
- For account-level spam flag: Move to Gmail or Outlook for resend; use a clean account; send one test to yourself first.
- **Do not declare delivery failure until H+48 with no signals at all.** A single OOO reply is proof of delivery.

**Decision threshold**: If 2+ of 5 emails bounced, reset the Wave 1 clock to the date of successful resend. The 72-hour monitoring window runs from the corrected send.

---

### Scenario B: Low Engagement from Batch 1

**Definition**: Reply rate below 20% by H+72 (0–1 replies), average engagement score below 1.5, and no forwarding signals.

**Diagnostic steps** (90 min total, before any further sends):

**Step 1 — Contact quality check** (30 min):
Visit each of the 5 institutional pages. Have any contacts changed roles since May 15 verification? A contact who left their organization or moved to a new role will have a reduced institutional inbox responsiveness (their old email may still work but their attention is elsewhere).

**Step 2 — Reframe messaging diagnostic** (20 min):
Re-read the email you sent to one contact. Answer these questions:
- Is the opening sentence about the contact's recent work, or about the framework? (Should be about their work.)
- Is the ask specific? ("I'd value your feedback" is vague; "Would the Domain 37 analysis be useful for your current election-protection docket?" is specific.)
- Is the email under 400 words? (Institutional emails over 400 words have significantly lower reply rates; the executive summary Gist handles the length problem.)
- Did you include both the main proposal Gist AND the executive summary Gist? (Executive summary is the correct first-click for busy contacts.)

**Step 3 — Extend the window before pivoting** (20 min judgment):
Weiser (Brennan Center) and Chenoweth (Harvard) have documented 5–10 day response cycles. If H+72 has 0–1 replies but Goodman (2–3 day cycle) and Elias (2–3 day cycle) are silent, investigate. If Goodman and Elias are silent and it's H+72, you have a signal problem. But if it's Goodman who replied and Weiser/Chenoweth/Bassin haven't yet, wait to H+120 (Day 5) before concluding low engagement.

**Recovery options**:
- Option 1 — Extend window to Day 7 before FAR-MISS determination: rational if the silent contacts have slower documented cycle times.
- Option 2 — Targeted resend with modified subject: Send a second email to silent contacts at Day 5 with a modified subject line. Frame as a follow-up with a more specific ask: "Following up with one specific question on Domain 37..."
- Option 3 — Pivot to warm introduction strategy: Use any contact who has replied (even acknowledgment) as a bridge to the others. "Wendy — I've also been in touch with Ryan Goodman on this. Would you be open to a brief conversation with both of you?"

**Decision threshold**: If H+120 (Day 5) still shows 0–1 replies AND no Gist views above baseline (meaning the emails are not being opened), declare Delivery Failure and go to Scenario A rather than Scenario B.

---

### Scenario C: Negative Feedback Pattern

**Definition**: Two or more Batch 1 contacts raise the same factual objection, framing critique, or concern about the framework.

**Single critique**: Do not trigger Scenario C for a single contact's objection. A critique from one contact is information — log it, assess it against the source material, respond substantively. It is the most intellectually valuable type of reply.

**Pattern trigger**: Same critique from 2+ contacts (e.g., two contacts question the same statistic; two contacts say the framing of a domain overstates the evidence; two contacts express concern about the framework's ideological positioning).

**Assessment steps**:

1. **Factual accuracy check**: Is the critique correct? Compare the objection to the source citation in the domain file. If the contact is right — there is an error — fix it immediately. Do not wait for a third critique. Correct the Gist (GitHub Gist allows edits without changing the URL), and send a correction note to any contact who raised the issue.

2. **Framing appropriateness check**: Is the critique about the evidence or about how the evidence is framed? If the evidence is sound but the framing is perceived as advocacy, the fix is: add a "diagnostic framing" caveat that foregrounds problem description over prescriptive reform. This is the "failure mode 2" from `measurement-and-iteration-framework.md` Part III.

3. **Response strategy**: For each contact who raised a substantive critique, respond within 48 hours. Do not be defensive. Acknowledge the concern specifically, explain the evidentiary basis (or the correction if there is an error), and ask a clarifying question that deepens engagement. A contact who critiques substantively is an engaged contact.

**Decision threshold for Batch 2**: If the pattern affects a domain that appears in the Batch 2 email templates (e.g., Domain 37 is in the election-protection track emails), revise the template before sending Batch 2. A 24-hour delay to revise 1 template is worth it; sending a template with a known framing problem to 15 contacts amplifies the problem.

---

### Scenario D: High Engagement but No Policy Uptake

**Definition**: Strong reply rate (3+ of 5 replies), strong engagement scores (average ≥3.0), good forwarding signals — but at H+72 there are no replies indicating anyone is actively using the framework for current work.

**Why this happens**: Enthusiastic but not yet activated. Contacts find the framework credible and interesting but haven't found the specific leverage point where it connects to their current docket or research agenda.

**This is not a failure at H+72.** Policy uptake signals typically emerge at Day 7–14, not Day 1–3. A Scenario D reading at H+72 is common and expected.

**Recovery / amplification actions**:

1. **Extend observation to Day 14**: Do not take remedial action before Day 7. The policy uptake signal window for institutional contacts is 7–21 days, not 72 hours.

2. **Proactive domain connection at Day 5–7**: For each Batch 1 contact who replied with enthusiasm or cautious interest (but no uptake signal), send a brief domain-specific follow-up at Day 5:
   > "Given your response, I pulled together the 2-page brief for Domain [X] — specifically the [section most relevant to their work]. Given that [their current case/research], this section may be directly applicable. Would a brief call this week be useful?"

3. **Phase 2 research adjustment**: If Scenario D persists after Day 14, it indicates the framework may be strong on problem diagnosis but weak on operational utility. Phase 2 domain research should prioritize "operational brief" format — shorter, more implementation-focused documents — over comprehensive domain analyses.

4. **Direct Phase 2 outreach research**: Identify whether the Batch 1 contacts have specific current deadlines (hearing dates, filing deadlines, conference presentation dates) where the framework analysis would be directly applicable. Surfacing the timing connection is often what converts "interested but not activated" to "using now."

---

## 8. Cross-Domain Success Signals

### Engagement Hypothesis by Domain

Based on the contact composition of Batch 1 and the domain focus areas documented in `measurement-and-iteration-framework.md` Part I, the following domain engagement distribution is predicted for Wave 1:

| Domain | Contacts Most Likely to Engage | Engagement Probability | What High Engagement Looks Like |
|--------|-------------------------------|----------------------|--------------------------------|
| Domain 37 (Federal Election Interference) | Weiser (BCJ), Elias (DD), Goodman (JS) | High — all three have current dockets | Specific questions about the five-mechanism taxonomy; requests for election-security subsections |
| Domain 1 (Electoral Architecture / Voting Rights) | Weiser, Elias, Bassin | High — domain is directly operational for all three | References to current cases (Watson v. RNC, Callais cascade); request for Domain 1 deep-dive |
| Domains 28/29 (War Powers / Prosecutorial Weaponization) | Goodman (JS) | Very high — Just Security's editorial focus | Publication interest signal; request for Domain 28/29 collaboration |
| Domain 57 (Multilateral Withdrawal / International Institutions) | Chenoweth (HKS) | Moderate — adjacent to comparative democratic backsliding | Academic engagement; possible syllabi or research agenda interest |
| Domain 58 (Tribal Sovereignty) | Bassin (Protect Democracy) | Moderate — constitutional structure overlap | Brief-relevant framing; connection to retaliatory prosecution pattern |
| Domains 6/35 (Judicial Independence) | Bassin, Weiser | High — Wilcox/Slaughter active; universal injunction reform | Case-connected questions; potential amicus brief relevance |

**Baseline hypothesis**: Domain 37 should show 2x engagement relative to average across other domains, given that all five Batch 1 contacts operate in election-protection-adjacent spaces and Path A+37 was explicitly chosen to prioritize this track.

---

### Phase 2 Sequencing Rule Derived from Engagement Signals

Apply this rule after H+72 data is collected:

> **If Domain 37 shows 2x engagement versus the average across other domains mentioned in replies, Phase 2 research should prioritize election-security domains (38, 39, 40) rather than the general Phase 2 candidates list.**

This rule reflects the logic from `measurement-and-iteration-framework.md` Part IV: "Phase 2 domain research should not proceed on a fixed internal schedule. It should respond to what the distribution feedback is revealing about demand."

**Operationalization**: After H+72, count domain mentions in all replies. If Domain 37 mentions ≥ (total mentions ÷ number of domains mentioned) × 2, trigger the election-security sequencing rule. Record in your Phase 2 gate assessment.

---

### Feedback Loop: Post-Wave-1 Analysis to Phase 2 Research Prioritization

Synthesize Wave 1 signals into a Phase 2 research queue update. This is a 20-minute exercise after the H+72 analysis:

**Step 1**: List all domains mentioned in replies (from Tab 1, "Domains mentioned" column).

**Step 2**: Rank by mention frequency.

**Step 3**: Cross-reference with urgency multipliers:
- Domain 42 (DEA hearing): Hard deadline May 28 — automatic priority regardless of mention frequency.
- Domain 37 (2026 midterms): Advocacy window open through November — priority if engagement is high.
- Domains 1/6/29: High current policy velocity (see `assessment/phase-1-baseline-metrics.md` Section 3) — deep demand likely but ambient activity makes attribution harder.

**Step 4**: Produce a ranked Phase 2 research list:
```
1. [Domain X] — [Y] mentions + [urgency reason] → Phase 2 Week 1
2. [Domain Y] — [Z] mentions + [urgency reason] → Phase 2 Week 1–2
3. [Domain Z] — [mentions] + [urgency reason] → Phase 2 Week 2–3
...
```

**Step 5**: Include this ranked list in the Phase 2 gate assessment document (the go/no-go decision memo due May 20 evening UTC) so the user has both the PASS/NEAR-MISS/FAR-MISS determination and the Phase 2 research queue in a single decision document.

---

### Cross-Domain Cascade Indicators

Watch for these cross-domain signals in replies — they indicate the framework is functioning as an integrated system rather than isolated domain documents:

| Signal | Meaning | Response |
|--------|---------|----------|
| Contact cites two or more domains in the same reply | They understand the systemic framing, not just individual domain content | Offer to facilitate the cross-domain brief format; this is a Level 2 framework adoption signal |
| Contact asks about the relationship between two domains | They are building their own analytical application of the framework | High-value; answer directly and ask what work product they're building toward |
| Contact references the "35-domain" structure by name | They have internalized the overall architecture | Log as a vocabulary adoption event per `assessment/phase-1-baseline-metrics.md` Section 1 |
| Contact mentions citing the framework to a colleague | Unprompted citation in conversation = organic adoption beginning | Log as a second-order amplification signal; ask if the colleague would be open to direct contact |

---

## Quick Reference Summary

**May 18 morning**: Pre-flight checklist complete, baseline Gist counts recorded, sends at 09:00–10:00 UTC.

**May 18 evening**: H+6 check (bounce scan + early OOO + first Gist delta).

**May 19 morning**: H+24 check (first reply scan + classification + Gist delta).

**May 19 evening**: H+36 check (forwarding signals + domain pull + engagement scoring).

**May 20 morning**: H+48 check (full reply rate calculation + preliminary tier assessment).

**May 20 evening UTC**: H+72 analysis + PASS/NEAR-MISS/FAR-MISS determination + Phase 2 gate assessment + user approval request for Phase 2.

**May 21**: Based on determination — either Batch 2 preparation begins (PASS/NEAR-MISS) or diagnostic sequence runs (FAR-MISS).

**May 22**: Batch 2 send (if approved) including Domain 42 supplemental sub-wave to DEA-relevant contacts.

**May 26**: Last day for Domain 42 amplification before May 28 DEA hearing.

**May 28**: DEA hearing — internal checkpoint for Domain 42 forwarding chain analysis.

---

*Document version 1.0 — produced May 17, 2026 for May 18–21 operational period.*
*Cross-references: PHASE_1_WAVE1_EXECUTION_PREP.md (Batch 1 contacts, Gist URLs, fallback addresses), POST_WAVE_1_SYNTHESIS_AND_TIER2_TRANSITION.md (Tier 2 scoring methodology, go/no-go decision format), assessment/phase-1-baseline-metrics.md (Section 2 engagement benchmarks, Section 5 failure mode taxonomy), measurement-and-iteration-framework.md (Tier 1/2/3 metrics tables, institutional adoption facilitation, bridge node tracking), phase-1-measurement-dashboard-spec.md (View 1 Summary Dashboard, confidence scoring, automation setup).*
