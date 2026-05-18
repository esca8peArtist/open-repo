---
title: "Wave 1 Response Tracking Template"
created: 2026-05-18
status: ACTIVE — begin populating at 10:00 UTC May 18, update as responses arrive
scope: "Real-time response classification, engagement scoring, per-constituency tracking, and Phase 2 signal aggregation for 40–45 Tier 1 organizations"
audience: "thorn — living document through May 25 Week 1 checkpoint"
companion_files:
  - WAVE_1_COMPLETION_CHECKLIST.md
  - WAVE_1_CONTINGENCY_DECISION_TREE.md
  - WAVE_1_DAILY_MONITORING_TEMPLATE.md
  - PHASE_2_LAUNCH_DECISION_TRIGGERS.md
---

# Wave 1 Response Tracking Template

**Purpose**: Capture every response signal from Wave 1 Tier 1 outreach in a structured format that enables Phase 2 decision-making by May 25.  
**Update frequency**: Real-time upon receipt of each response. Daily Gist view count deltas at each monitoring check.  
**Decision output**: Section 6 aggregate scores feed directly into WAVE_1_CONTINGENCY_DECISION_TREE.md to select Phase 2 scenario.

---

## SECTION 1: Engagement Scoring Scale

Apply one score to each contact at each monitoring checkpoint. A contact's score can only increase over time — once upgraded, do not downgrade unless a reply explicitly withdraws interest.

| Score | Label | Definition |
|---|---|---|
| 0 | No Response | No reply, no Gist view delta attributable to this contact, no mention detected |
| 1 | Opened / Clicked | Gist view count delta suggests link-follow, OR OOO autoresponse received (confirms live delivery), OR email opened via read receipt — but no substantive reply |
| 2 | Acknowledged | Replied with brief acknowledgment ("Thank you, I'll review") with no substantive content — confirms receipt and live address |
| 3 | Engaged | Reply references specific content (domain number, finding, framing), asks a methodological or procedural question, or forwards to a named colleague |
| 4 | High-Value Signal | Reply indicates institutional adoption pathway: offers to feature in publication/syllabus/testimony, requests follow-up call, passes to clinic or policy team with named contact, or requests permission to cite/share |
| 5 | Adoption Signal | Organization publicly cites, references, or distributes the proposal; or replies with a concrete collaboration proposal (co-authorship, briefing invitation, coalition integration) |

**Scoring rule**: When in doubt between two scores, assign the lower one. The decision thresholds in WAVE_1_CONTINGENCY_DECISION_TREE.md are calibrated to conservative scoring.

---

## SECTION 2: Response Classification Taxonomy

When a reply arrives, classify it into exactly one primary category plus any applicable secondary tags.

### Primary Categories

**ADOPTION_SIGNAL** — The contact or organization is moving toward incorporating the proposal into their work. Markers: requests for citation format, offers to feature in a publication, mentions sharing with colleagues by name, references a policy window the proposal addresses.

**METHODOLOGY_QUESTION** — The contact is engaging with the research framework rather than the conclusions. Markers: asks how domains were selected, questions a finding's sourcing, requests the underlying data, asks about the comparative methodology. This is a high-quality engagement signal from academic contacts — it means they are evaluating it seriously, not dismissing it.

**INSTITUTIONAL_INQUIRY** — The contact is exploring whether their organization can use this. Markers: asks if there is a shorter version for a specific audience, asks about the proposal's legal framework for applicability to their state, asks whether the authors are available for a briefing or panel. This is the primary signal to watch for from unions and immigration legal aid organizations.

**PARTISAN_PUSHBACK** — The contact responds with ideological objection rather than substantive critique. Markers: frames the proposal as partisan advocacy rather than analytical research, challenges framing as "political," requests the proposal take a different position on a contested issue. This is not a failure signal — it is information about messaging calibration for that constituency.

**POLITE_DECLINE** — The contact explicitly declines further engagement but does so without substantive objection. Markers: "Not my area," "We focus on [different issue]," "Not accepting unsolicited submissions at this time." Log the reason — this informs which organizations to skip in Tier 2.

**NO_RESPONSE** — Default classification for any contact who has not replied by the 72-hour mark. Reviewed at May 25 checkpoint to determine whether to attempt follow-up.

### Secondary Tags (apply as many as relevant)

- `VOCABULARY_ADOPTION` — Reply uses terminology from the proposal without quoting it (signals absorption of framing)
- `CROSS_DOMAIN_INTEREST` — Contact asks about domains beyond those highlighted in their specific email
- `REFERRAL_GIVEN` — Contact names a specific colleague or organization to contact
- `FOLLOW_UP_REQUESTED` — Contact requests a follow-up email, call, or document
- `MEDIA_FLAG` — Contact is a journalist or media outlet requesting more information
- `OPPOSITION_RESEARCH` — Contact appears to be gathering information for an adversarial response
- `BOUNCE_RESOLVED` — Originally bounced, alternate address confirmed working

---

## SECTION 3: Per-Contact Response Log

Update in real time. Add rows as responses arrive. Do not delete or overwrite — log each new response event as a new row for the same contact.

### Law Schools and Academic Institutions

| Date/Time (UTC) | Contact Name | Organization | Response Type | Score | Primary Category | Secondary Tags | Key Content Summary | Follow-Up Required |
|---|---|---|---|---|---|---|---|---|
| ___ | Ryan Goodman | NYU Law / Just Security | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | Erica Chenoweth | Harvard Kennedy School | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Law contact 3] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Law contact 4] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Law contact 5] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |

**Law school sector aggregate as of [date]**: ___ / ___ contacts responded. Highest score: ___. Avg score: ___.

### Immigration Legal Aid Organizations

| Date/Time (UTC) | Contact Name | Organization | Response Type | Score | Primary Category | Secondary Tags | Key Content Summary | Follow-Up Required |
|---|---|---|---|---|---|---|---|---|
| ___ | [Immigration contact 1] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Immigration contact 2] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Immigration contact 3] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |

**Immigration legal aid sector aggregate as of [date]**: ___ / ___ contacts responded. Highest score: ___. Avg score: ___.

### Think Tanks and Policy Organizations

| Date/Time (UTC) | Contact Name | Organization | Response Type | Score | Primary Category | Secondary Tags | Key Content Summary | Follow-Up Required |
|---|---|---|---|---|---|---|---|---|
| ___ | Wendy Weiser | Brennan Center | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | Ian Bassin | Protect Democracy | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | Marc Elias | Elias Law Group | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Think tank 4] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Think tank 5] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |

**Think tank sector aggregate as of [date]**: ___ / ___ contacts responded. Highest score: ___. Avg score: ___.

### Labor Unions

| Date/Time (UTC) | Contact Name | Organization | Response Type | Score | Primary Category | Secondary Tags | Key Content Summary | Follow-Up Required |
|---|---|---|---|---|---|---|---|---|
| ___ | [Union contact 1] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Union contact 2] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |
| ___ | [Union contact 3] | ___ | ___ | ___ | ___ | ___ | ___ | Y/N |

**Union sector aggregate as of [date]**: ___ / ___ contacts responded. Highest score: ___. Avg score: ___.

---

## SECTION 4: Gist View Count Tracker

Record manually via incognito browser at each monitoring checkpoint. Delta = current count minus H+0 baseline.

| Checkpoint | UTC Time | Main Proposal Views | Exec Summary Views | Domain 37 Views | Domain 42 Views | Domain 56 Views | Domain 57 Views | Domain 58 Views | Notes |
|---|---|---|---|---|---|---|---|---|---|
| H+0 Baseline | 10:00 May 18 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | Post-send baseline |
| H+2 | 12:00 May 18 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| H+6 | 16:00 May 18 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| H+12 | 22:00 May 18 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| H+24 | 10:00 May 19 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| H+48 | 10:00 May 20 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| H+72 | 10:00 May 21 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Week 1 | 10:00 May 25 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

**Gist view interpretation guidelines**:
- Delta of 1–5 views in H+0 to H+24: Consistent with 1–2 recipients clicking. Low engagement but not zero.
- Delta of 6–15 views in H+0 to H+24: Multiple recipients clicking, or one recipient reviewing multiple times. Positive signal.
- Delta of 16+ views in H+0 to H+24: Strong signal — multiple recipients reviewing actively, or a single recipient sharing the link within their organization.
- Disproportionate delta on a specific domain Gist (e.g., Domain 37 jumps significantly while main proposal does not): A contact followed through to the domain supplement, indicating deep engagement beyond the introductory email.

---

## SECTION 5: Per-Constituency Response Timing Expectations

Different constituencies have structurally different response cycles. Use this table to interpret silence correctly — silence is not a negative signal if you are within the expected response window.

| Constituency | Expected First Reply Window | Why | Fast Reply Signal (within 48h) | Slow Reply Signal (days 5–10) |
|---|---|---|---|---|
| Law schools (academic) | Days 5–10 | Academics manage inboxes weekly; research email treated as low urgency absent a deadline | Suggests contact is actively monitoring the policy space or has prior relationship context | Normal — do not interpret as weak interest |
| Immigration legal aid | Days 2–5 | Legal aid orgs are high-volume, but policy staff check email more frequently than academics | Strong positive — org is under capacity pressure and still replied, indicating relevance |  Normal — these orgs are resource-constrained |
| Think tanks / policy orgs | Days 2–5 | Policy org staff are inbox-active but triage cold outreach after internal meetings | Strong positive — reply before internal review means individual champion | Day 5 reply suggests it went through internal routing first — still positive |
| Labor unions | Days 3–7 | Union staff manage large member communications; policy research takes internal routing | Strong — union policy staff reviewed and responded without internal approval cycle | Normal — expect federation approval loops |
| Other academic | Days 5–14 | Highly variable; depends on semester schedule | Strong — researcher is actively following the space | May simply reflect semester timing |

**Semester note**: May 18 is mid-to-late spring semester at most US institutions. Faculty may be in exam/grading periods. Response rates from academic contacts before June 1 may be lower than typical due to semester-end load, not lack of interest. Do not reclassify an academic contact as disengaged until after June 15.

---

## SECTION 6: Key Signals to Watch — Vocabulary Adoption and Deep Engagement Markers

These are the qualitative signals that indicate the proposal is having substantive impact, distinct from a mere acknowledgment or courtesy reply.

### Vocabulary Adoption Signals

The highest-confidence indicator of genuine impact is when a contact uses language from the proposal in their reply without directly quoting it. This means the framing has been absorbed rather than skimmed.

Phrases to watch for in replies:
- "democratic infrastructure" (proposal's framing for the 40 domains collectively)
- "domain-based" analysis or "domain sequencing" (the proposal's diagnostic methodology)
- "accountability gap" or "institutional accountability" used in the specific way the proposal uses it
- References to specific domain numbers (e.g., "Domain 37's electoral security framework") without prompting
- "policy window" language echoing the proposal's urgency framing

If a contact uses any of these phrases, tag their log entry with `VOCABULARY_ADOPTION` — this is a Score 3+ signal even if the content seems brief.

### Cross-Domain Interest Signals

The proposal covers 40 domains. If a contact who received an email focused on Domain 37 (electoral security) asks a question about Domain 42 or Domain 56, they have read beyond the highlighted domain. Tag with `CROSS_DOMAIN_INTEREST`. This indicates:
- The contact reviewed the full proposal, not just the highlighted section
- There is interest in the research program as a whole, not just the targeted domain
- The contact may become an amplifier across domains if they adopt the work

### Deep Engagement Markers

These are the signals that indicate a contact is seriously evaluating adoption:
- Asks for the methodology appendix or source list (indicates fact-checking prior to citation)
- Asks whether the proposal has undergone peer review (indicates considering academic use)
- Asks about the author's institutional affiliation (indicates considering formal collaboration)
- Requests a PDF version for offline circulation (indicates planning to share at a meeting)
- References a specific policy window or deadline that aligns with a domain finding (indicates active calendar integration of the research)

---

## SECTION 7: Aggregate Response Rate Tracker

Update at each monitoring checkpoint. This feeds Phase 2 decision-making.

| Metric | May 18 H+24 | May 19 H+48 | May 21 H+72 | May 25 Week 1 |
|---|---|---|---|---|
| Total contacts sent | ___ | ___ | ___ | ___ |
| Total responses received (any type) | ___ | ___ | ___ | ___ |
| Raw response rate (any response / total sent) | ___% | ___% | ___% | ___% |
| Substantive response count (Score 3+) | ___ | ___ | ___ | ___ |
| Substantive response rate (Score 3+ / total sent) | ___% | ___% | ___% | ___% |
| High-value signals (Score 4+) | ___ | ___ | ___ | ___ |
| Gist total delta (all Gists, H+0 to current) | ___ | ___ | ___ | ___ |
| Hard bounces confirmed | ___ | ___ | ___ | ___ |
| Follow-ups required | ___ | ___ | ___ | ___ |

**Classification as of May 25 Week 1 checkpoint**:
- STRONG: Substantive response rate ≥40% (Score 3+ from ≥40% of total sent contacts)
- MODERATE: Substantive response rate 25–40%
- WEAK: Substantive response rate <25%

**Current classification**: ___ (update at each checkpoint)

---

## SECTION 8: Sentiment Classification

For each substantive response, record a sentiment classification separate from the response category.

| Sentiment | Definition | Implication |
|---|---|---|
| POSITIVE | Contact expresses agreement, utility, or value of the research for their work | Proceed with follow-up and deepen engagement |
| NEUTRAL | Contact acknowledges without expressing agreement or disagreement | Standard follow-up, let engagement develop naturally |
| SKEPTICAL | Contact expresses doubt about methodology, scope, or framing without adversarial framing | Engage directly with the specific concern — skeptical experts who become convinced are high-value advocates |
| ADVERSARIAL | Contact frames the proposal as partisan, dangerous, or inappropriate for their organization | Do not engage further unless they raise a specific substantive objection that can be addressed factually |

**Sentiment distribution as of May 25**: ___ POSITIVE / ___ NEUTRAL / ___ SKEPTICAL / ___ ADVERSARIAL
