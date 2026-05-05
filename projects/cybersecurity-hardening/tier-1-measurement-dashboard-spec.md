---
title: "Tier 1 Measurement Dashboard Spec"
project: cybersecurity-hardening
created: 2026-05-05
status: ready-for-use
item: 42 — Tier 1 Success Metrics & Feedback Loop Architecture
depends-on: tier-1-success-metrics-framework.md, tier-1-feedback-collection-protocol.md, adoption-tracking-dashboard-spec.md
---

# Tier 1 Measurement Dashboard Spec

**Lead finding**: The dashboard for a 12-organization campaign does not need software. What it needs is a consistent reporting template that can be completed in under 30 minutes from the tracking spreadsheet. The value of the dashboard is not visualization — it is forcing a weekly reading of the data so that early warning signals are not missed. Anomalies that stay invisible for three weeks become problems that require course corrections. Anomalies spotted at week one are usually fixable in a morning.

---

## 1. Weekly Tracking Visualization

Complete every Monday morning for the duration of the active outreach phase (Weeks 1–6). Use the tracking spreadsheet as the data source. The report takes 15–20 minutes.

### Weekly Status Report Template

```
TIER 1 OUTREACH — WEEKLY STATUS
Week: [N]  |  Report Date: [YYYY-MM-DD]  |  Campaign Day: [N]

--- SEND STATUS ---
Total organizations in scope: 12
Sends completed this week: [N]
Cumulative sends: [N] / 12
Sends not yet made: [N]  →  Reason: [pending research / scheduling / user action]

--- RESPONSE SUMMARY ---
Cumulative replies received: [N] ([N]% of sends)
New replies this week: [N]
Reply type breakdown:
  Positive (Stage 1+): [N]
  Routing (forwarding): [N]
  MoreInfo (questions): [N]
  Negative (declined): [N]
  Conversion (action taken): [N]
  No reply yet: [N]

--- CLICK ANALYTICS ---
Bitly cumulative clicks: [N]
New clicks this week: [N]
Click-to-send ratio: [N]%  (target: ≥50% by Week 3)
Referrer sources: [List from Bitly dashboard]

--- REFERRAL PIPELINE ---
New warm contacts generated: [N] (cumulative: [N])
Organizations referred to: [List]
Referral factor to date: [new contacts] / [sends] = [X.X]

--- ADOPTION SIGNALS ---
Stage 2+ organizations this week: [N] (cumulative: [N])
Most advanced stage reached: Stage [N] by [Org Name]
Case study eligibility flags: [N] organizations at Stage 3+

--- ANOMALY FLAGS ---
Organizations with no reply at Day [N+]: [List]
Bounced emails (undeliverable): [List]
Low-quality replies (generic acknowledgment only): [List]
Negative feedback patterns: [Describe if any]

--- TOP PRIORITY ACTIONS FOR NEXT WEEK ---
1. [Action]
2. [Action]
3. [Action]
```

### Key Numbers to Watch Each Week

**Week 1 focus**: Send completion and first reply emergence. If no replies by Day 7, the deliverability check-in goes out.

**Week 2 focus**: Reply rate trajectory. The 25–35% acknowledgment threshold should be approaching by end of Week 2. If below 15%, escalate to subject line audit (see Section 4).

**Week 3 focus**: Stage-of-adoption distribution. What percentage of replies are Stage 1+ vs. Stage 0? If more than half of replies are generic routing responses with no specific engagement, the personalization did not land.

**Week 4 focus**: Referral factor. Question 3 from the 30-day follow-up should start generating new warm contacts. A referral factor below 1.0 at Week 4 means secondary distribution is not happening.

---

## 2. Monthly Reporting Template

Produce at 30 days, 60 days, and 90 days post-launch. The 90-day report is the primary Tier 2 launch decision gate. Each report should take approximately 30 minutes.

### Monthly Impact Summary Template

```
TIER 1 OUTREACH — MONTHLY IMPACT SUMMARY
Report Period: Launch through [Date]  |  Report Date: [Date]

=== DISTRIBUTION SUMMARY ===
Total sends: [N] / 12 named contacts
Send completion rate: [N]%
Pending sends: [N] — Reason: [text]

=== RESPONSE METRICS ===
Overall reply rate: [N]% (target: ≥40% by Day 30, ≥50% by Day 60)
Week-over-week reply rate trend: [Increasing / Flat / Declining]
Stage breakdown of all contacts:
  Stage 0 — Receipt only: [N]
  Stage 1 — Review signal: [N]
  Stage 2 — Internal discussion: [N]
  Stage 3 — Partial implementation: [N]
  Stage 4 — Sustained adoption: [N]
  Stage 5 — External citation: [N]
  No reply: [N]

=== SECTOR AGGREGATES ===
Tier 1A (Immigration Legal Aid):
  Sends: [N]  Replies: [N] ([N]%)  Highest stage: [N]
  Fastest response latency: [N] days  Average: [N] days
Tier 1B (Community-Based Organizations):
  Sends: [N]  Replies: [N] ([N]%)  Highest stage: [N]
  Fastest response latency: [N] days  Average: [N] days
Tier 1C (Mutual Aid Networks):
  Sends: [N]  Replies: [N] ([N]%)  Highest stage: [N]
  Fastest response latency: [N] days  Average: [N] days

=== ADOPTION PATTERN EMERGENCE ===
Organizations demonstrating adoption signals: [N] of [N] contacted
Adoption signal types observed:
  [ ] Resource page inclusion
  [ ] Staff training reference
  [ ] Client-facing distribution
  [ ] Forward to affiliated programs/network
  [ ] Part 0 implementation reported
  [ ] Protocol change (intake or communication)
  [ ] Published citation
Highest adoption organization: [Org Name] — Stage [N]

=== OUTLIER INSTITUTIONS ===
Highest-performing contact (quality of engagement): [Org Name]
  What made it work: [text]
Lowest-performing contact (no engagement or negative): [Org Name]
  Likely reason: [text]
Unexpected responder (type not anticipated): [Org Name or type]
  Why this matters: [text]

=== CONTENT FEEDBACK SUMMARY ===
Most cited corpus section (from replies): [Section name]
Most cited gap: [text or "none yet"]
Most cited barrier: [text or "none yet"]
Feedback requiring corpus update: [Y/N — describe if Y]

=== REFERRAL NETWORK ===
Total warm contacts generated: [N]
Referral factor: [N] (warm contacts / initial sends)
Top referral source: [Org Name] — generated [N] referrals
Referral organizations pending contact: [List]

=== GIST TRAFFIC ===
Total views: [N]
This period delta: +[N]
Top referrer source: [text from Gist dashboard]
Interpretation: [Flat / Slow growth / Moderate growth / Spike]

=== GATE STATUS ===
30-day gate: [PASS / BELOW TARGET / FAIL]  Key metric: [text]
Gate decision: [Proceed to follow-up wave / Hold for diagnosis]

=== ADJUSTMENTS BEFORE NEXT PERIOD ===
1. [action]
2. [action]
3. [action]
```

---

## 3. Institution-Specific Analysis

The 12 named Tier 1 contacts fall into three organizational types with meaningfully different response patterns. Over the 90-day tracking period, the following hypotheses about sector variation should be tested against actual data.

### Response Speed by Sector Type

**Hypothesis**: Mutual aid networks (Tier 1C) respond fastest because they have less email volume, more direct staff who handle all functions, and the security culture orientation predisposes them to engage quickly with threat-relevant material.

**Hypothesis**: Immigration legal aid organizations (Tier 1A) with national reach (NILC, CLINIC, ILRC) respond more slowly than regional community organizations (Tier 1B) because they receive more unsolicited resources and have more layers of routing.

**Test method**: At 30 days, calculate average response latency by sector type. Log:

```
Tier 1A average latency (days): [N]
Tier 1B average latency (days): [N]
Tier 1C average latency (days): [N]
Fastest individual contact: [Org] at [N] days
Slowest individual contact with any reply: [Org] at [N] days
```

If Tier 1A is demonstrably slower than Tier 1B or 1C, that informs the sequencing strategy for Phase 2 outreach to similar organizational types.

### Adoption Speed by Sector Type

**Hypothesis**: Community-based organizations (Tier 1B) adopt faster in terms of distributing the corpus to their networks, because they have community education infrastructure and regularly share resources with their membership. Their "adoption" is mostly forwarding and social sharing rather than institutional policy change.

**Hypothesis**: Legal aid organizations (Tier 1A) adopt more slowly in terms of forwarding and sharing, but produce higher-quality adoption signals when they do (practitioner training, clinical resource, protocol change) because their professional structure demands more deliberate uptake.

**Hypothesis**: Mutual aid networks (Tier 1C) produce the fastest Gist click-through rates because their networks have high security awareness and immediately share links within Signal groups and Telegram channels.

**Test method**: At 60 days, compare stage-of-adoption distribution by sector and Bitly click-through rate by sector. A sector with high Stage 1 and low Stage 2 suggests the corpus is being read but not circulated. A sector with high referral counts but low Stage 2 suggests the corpus is being shared without internal review.

### Correlation Between Personalization Quality and Response Rate

Track `personalization_score` (1=generic / 2=org-specific / 3=named-contact-with-specific-reference) for each of the 12 sends. At 30 days, calculate reply rate by personalization score. Research consistently shows 2.76× better performance from highly targeted sends vs. broadcast sends. If the data shows a meaningful gap between personalization score 3 sends and personalization score 1–2 sends, this confirms that extra personalization effort in Phase 2 is justified.

---

## 4. Anomaly Detection

Define "anomaly" operationally — a condition that requires a decision, not just an observation.

### Type 1: Non-Response After 2 Weeks

**Definition**: A named Tier 1 contact with verified contact information shows zero engagement (no reply, no Bitly click) at Day 14 post-send.

**Non-anomaly interpretation**: At Day 14, non-response is common. It is not a failure. It becomes an anomaly at Day 21 if the Week 1 follow-up also produced no reply.

**Anomaly threshold**: Zero reply and zero click at Day 21 from a named contact with a verified direct email.

**Decision tree**:
1. Was the email sent to a direct named contact or a general inbox? If general inbox → research a named contact and resend with different subject line.
2. Did the email end up in spam? Check Bitly clicks — if zero, may never have been opened. Try sending from a different email address.
3. Is there a known reason for non-response (org in organizational transition, leadership change, known high enforcement activity creating staff overwhelm)? Log as "extenuating circumstances — re-engage after 45 days."
4. None of the above → resend with shorter, different subject line and a one-sentence body: "Following up on a digital security guide for immigration legal teams — would a 30-second reply confirming receipt be possible? [URL]"

### Type 2: Low-Quality Replies

**Definition**: A reply that acknowledges receipt but shows no evidence of reading and provides no routing information. Common form: "Thank you for sharing. We will keep this on file."

**Why this is an anomaly**: It is neither a Stage 0 routing response (no forwarding occurred) nor a Stage 1 review signal (no specific reference to content). It suggests the email reached someone whose role is to acknowledge external communications without triage responsibility.

**Action**: Reply thanking them and asking a direct routing question: "Happy to hear it reached you. If someone at [Org] handles client digital security resources, could you route this there? I want to make sure it reaches someone who can evaluate whether it's actionable for your clients."

### Type 3: Negative Feedback Patterns

**Definition**: Two or more replies identifying the same critical concern about the corpus (technical complexity, incorrect information, inappropriate scope, tone, missing legal caveats).

**Single negative is not a pattern**: One organization finding the corpus inappropriate for their context is expected. The corpus is written for people with general technical literacy, not for clients with no internet access. Some organizations will correctly identify that it does not serve their specific population.

**Pattern threshold**: Two or more organizations identifying the same substantive concern is a signal requiring evaluation.

**Categories**:
- **Factual concern**: Verify the claim against primary sources. If wrong, update Gist immediately and re-send corrected version with a note.
- **Scope concern**: "This is too technical for our clients." Add a non-technical one-page summary. Do not revise the corpus itself unless the technical sections are demonstrably wrong.
- **Legal concern**: "This contains advice that could put clients at risk." Escalate to legal review before proceeding with further distribution.
- **Privacy concern**: "Sharing data broker names could flag people who opt out." Evaluate whether the concern has merit. The corpus is explicit that this is a risk mitigation step, not an elimination of surveillance risk.

### Type 4: Unexpected Organization Types Responding

**Definition**: A response comes from an organization not in the 12 named contacts and not on the regional follow-up list — a referral that lands from an entirely unanticipated sector.

**This is not a problem — it is a discovery signal.** If a domestic violence organization reaches out after being referred by NILC, or if a labor union legal department inquires after a RAICES referral, this indicates the corpus has utility beyond the anticipated Tier 1 population. Log the organization type, add to the referral count, and assess whether to add a new category to the Tier 2 outreach list.

---

## 5. Comparison Framework

How does this campaign's success rate compare to similar proposals? Three applicable benchmarks:

### Benchmark 1: Civil Society Digital Security Guidance Distribution

Access Now's Digital Security Helpline reached 10,000 cases over approximately 7 years from launch (reported in 2021). That is roughly 1,400 cases per year, representing the aggregate adoption of their help-seeking model across a global civil society audience. This corpus targets a narrower, domestic population through direct outreach rather than help-seeking — a fundamentally different distribution model. Direct comparison is not meaningful, but the Access Now Helpline demonstrates that civil society security guidance does achieve meaningful adoption over multi-year timescales.

**What this tells us**: Adoption of security guidance in the civil society space is not rapid. Expect 12–24 months for the corpus to reach saturation within the Tier 1 audience, not 90 days.

### Benchmark 2: Cold Outreach to Nonprofits and Mission-Driven Organizations

Research on targeted B2B cold email campaigns (2024–2026 data) shows:
- General B2B average reply rate: 3–5%
- Nonprofit sector: exceeds 16.5% (lead this sector among all industries)
- Highly targeted campaigns with personalized hooks: 15–25% (top quartile)
- Follow-up sequences with 3-7-7 cadence: capture 93% of total replies by Day 17

This corpus outreach to 12 named contacts is not mass cold email — it is small-scale, high-personalization outreach to organizations with direct mission alignment. The expected reply rate of 25–40% is consistent with top-quartile personalized outreach performance, adjusted upward for the high mission alignment of the Tier 1 audience.

**What this tells us**: A 25–35% overall reply rate at 30 days is realistic and represents neither exceptional success nor disappointment. The benchmark that should concern you is reply quality, not just reply rate.

### Benchmark 3: Policy Framework Adoption by Professional Organizations

The ABA Model Rules of Professional Conduct (adopted 1983) achieved adoption by all 50 U.S. states plus DC over approximately 37 years (2.5 states/year). The Model Penal Code (1962) achieved adoption in 36 states over about 15 years (2.4 states/year). Both are legislative/regulatory adoption timelines — not comparable to organizational resource adoption.

The directly relevant non-legislative analog is practitioner guide adoption by professional associations. The SAFETAG security audit framework (Internews, first published ~2014) is widely cited in civil society security literature but does not publish adoption statistics. The EFF's Surveillance Self-Defense (ssd.eff.org) achieves tens of thousands of annual visitors but is passive web distribution, not active organizational outreach.

**What this tells us**: Regulatory and legislative adoption benchmarks are not useful for this campaign's timescale. The meaningful comparison is whether the corpus reaches the field practice of immigration legal aid organizations within 12–18 months — a timescale consistent with how practitioner guides spread through legal aid networks when actively distributed by trusted intermediaries like ILRC and CLINIC.

### Rate-Setting Summary

| Comparison Context | Rate | Applicable to This Campaign? |
|---|---|---|
| Model Penal Code state adoption | 2.4 states/year (legislative) | No — wrong mechanism |
| ABA Model Rules adoption | 2.5 states/year (professional regulation) | Partial — similar professional org structure |
| Brennan Center AVR adoption | 1.9–2.4 states/year (legislative) | No — wrong mechanism |
| Nonprofit cold email reply rate | 16.5%+ (mission-driven orgs) | Yes — baseline floor |
| Highly targeted mission-aligned outreach | 25–35% | Yes — realistic ceiling for this campaign |
| Civil society security guidance lifetime adoption | Years to saturation | Yes — long-horizon expectation |

---

*Dashboard spec complete. The weekly report template and monthly impact summary are ready to use immediately. No software setup required — copy both templates into a text document or Google Doc and complete from the tracking spreadsheet each week. For the full passive monitoring infrastructure (Google Alerts, Gist traffic logs, Overton searches), see `adoption-tracking-dashboard-spec.md`.*
