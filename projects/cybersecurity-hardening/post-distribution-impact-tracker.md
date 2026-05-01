---
title: "Post-Distribution Impact Tracker — Cybersecurity-Hardening Corpus"
project: cybersecurity-hardening
created: 2026-05-01
status: ready-for-use
session: 717
depends-on: TIER1_DISTRIBUTION_PREP.md, TIER2_DISTRIBUTION_PREP.md, tier-2-success-metrics.md
---

# Post-Distribution Impact Tracker

**Purpose**: Define how to measure whether the Tier 1 corpus distribution actually moved the needle — adoption tracking mechanisms, feedback collection protocol, effectiveness metrics, community engagement patterns, and time-gated success thresholds for the 30/90/180-day and 12-month checkpoints. This document drives iteration on Tier 2 and Tier 3 messaging based on real feedback rather than assumptions.

**Lead finding**: Most organizations that receive policy or security guidance documents do not respond or report back. Design all tracking and measurement systems to work under sparse data conditions. A 25-35% acknowledgment rate from Tier 1 immigration legal organizations is a realistic ceiling, not a floor. Signal comes from a small number of high-quality responses plus observable downstream citations, not from mass response rates.

---

## Section 1: Tier 1 Organization Adoption Tracking Mechanisms

### What You Are Trying to Detect

Adoption is not a single event. It proceeds through stages, and most organizations will stall somewhere in the middle rather than completing full implementation. Track stage-of-adoption, not binary yes/no.

**Stage model** (adapted from SAFETAG's civil society security adoption research):

| Stage | Definition | Observable Signal |
|-------|-----------|-------------------|
| 0 — Receipt | Organization received the material | Email opened, form submission acknowledged, no follow-up needed |
| 1 — Review | Someone read beyond the subject line | Reply with a routing message, question, or specific reference to content |
| 2 — Internal discussion | Material circulated internally | Reply referencing "sharing with our tech team" or "discussed in staff meeting" |
| 3 — Partial implementation | At least one action taken (e.g., data broker opt-outs started, Part 0 reviewed) | Follow-up reply citing a specific element; observable policy reference |
| 4 — Sustained adoption | Ongoing reference; integrated into client-facing materials or training | Corpus appears in org's resource list, newsletter, or legal aid toolkit |
| 5 — External citation | Published reference in policy document, brief, training curriculum, or filing | Google Scholar alert, web mention, or direct notification |

The Tier 2 success-metrics document already calibrates reply and conversion rate targets by sector (20% reply, 2-3 conversions for digital rights; 10% reply, 1-2 conversions for academic). For Tier 1, the equivalent targets are:

- **Receipt acknowledgment**: 35% of Tier 1A immigration legal aid contacts acknowledge receipt within 30 days
- **Stage 2+ adoption**: 20% of contacted organizations reach internal discussion or higher within 90 days
- **Stage 4+**: 10% demonstrate sustained adoption within 180 days

These targets are calibrated against nonprofit cold outreach benchmarks. Internews's SAFETAG evaluation (the most directly comparable framework for civil society digital security guidance) found that "most organizations" that received audits improved security practices, but did not report specific percentages. Commercial cold email research sets the baseline: nonprofits and mission-driven orgs see reply rates of 10-16% on targeted, personalized outreach — meaningfully higher than the 5% average for general commercial email. Tier 1 targets assume a 25% reply rate ceiling on high-personalization sends to named contacts, consistent with the Tier 2 success metrics rationale already documented.

### Citation and Reference Tracking

Set up passive tracking infrastructure before Tier 1 goes out. These cost nothing and catch citations without active monitoring:

**Google Alerts** (free): Create alerts for:
- `"Palantir ELITE" immigration security`
- `"esca8peArtist" OR "gist.github.com/esca8peArtist"`
- `"opSec" "undocumented" immigrants 2026`
- Organization name + "data broker" + "opt-out"

Alerts fire via email when new indexed pages match the query. False positive rate is high; check weekly, not daily.

**GitHub Gist traffic**: The GitHub Gist URL (`https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`) shows view counts in the Gist dashboard. Log the view count at launch, at 30 days, 90 days, and 180 days. Growth trajectory matters more than absolute numbers. A Gist with 200 views at 30 days and 800 views at 90 days indicates organic sharing is occurring. A flat Gist (200 → 210 views) suggests the distribution is not producing referral traffic.

**Web mention tracking**: Set a monthly calendar reminder to search for the Gist URL in DuckDuckGo and Google (include the full URL in quotes). Any indexed page that embeds or cites the URL is a Stage 5 citation.

**Policy database tracking**: Search Overton.io (free tier available) quarterly for references to the core document concepts. Overton indexes published policy documents, government reports, and think tank outputs in English and tracks which documents cite which. Set a reminder to search for "Palantir ELITE" and "undocumented immigrants operational security" in Overton at 90-day intervals.

### Implementation Signals Without Direct Feedback

Most organizations will not email back to say "we implemented your recommendations." Observable signals that adoption is occurring without a reply:

- The Gist URL appears in a Twitter/X thread, Mastodon post, or LinkedIn update from a known Tier 1 organization's account
- A paralegal or attorney at a Tier 1 org asks a specific technical question via the email thread (indicates Part 0 or technical countermeasures were read)
- A Tier 1 organization's published newsletter, blog post, or resource page references data broker opt-outs, digital security for undocumented clients, or Palantir ELITE — even without citing the corpus directly, this indicates the topic reached their editorial pipeline
- A referral from a Tier 1 contact to a Tier 3 researcher or journalist (someone contacts you saying "I was referred by [Tier 1 org]")

---

## Section 2: Feedback Collection Framework

### Design Principle: Make Feedback Frictionless

The number one cause of zero feedback is friction. Long surveys, complex forms, and multi-step processes produce near-zero completion rates from busy legal aid staff. The entire feedback ask must fit in a single paragraph of the follow-up email with a one-click or single-reply structure.

### 30-Day Follow-Up Email (Template)

Send 30 days after initial contact. Subject line: `Following up — [Org Name] + digital security corpus`.

Body:

> Hi [Name] — I'm writing to follow up on the digital security corpus I sent on [Date]. No action required on your part. I'm simply tracking whether the material reached useful hands and whether any part of it was actionable.
>
> If you have 60 seconds: Did it reach the right person at [Org Name]? (Reply with "yes", "no — should go to [Name]", or "still reviewing.")
>
> That's the whole ask. Anything more detailed you want to share is welcome, but not required.

This produces stage-of-adoption data from a single-word reply. It is designed to remove the barrier of having to compose a substantive response.

### 90-Day Follow-Up (Three Questions)

Send 90 days after initial contact, regardless of whether the 30-day follow-up produced a reply.

> Hi [Name] — three months since the digital security corpus reached you. A brief check-in:
>
> 1. Did any part of the guidance get reviewed, shared, or implemented? (Yes / Partially / Not yet / Not the right fit)
> 2. What's the biggest gap — what should the corpus cover that it doesn't?
> 3. Is there another person or organization who should have this?
>
> Reply with just the numbers if that's easier. Your feedback directly shapes the next version.

Question 3 activates referral networks. It is the most valuable question in the framework because it extends reach without additional outreach effort. Every referral adds a warm contact who received the corpus from a trusted source.

### 180-Day Follow-Up (Case Study Ask)

Send 180 days after initial contact. This follow-up is conditional — only send to organizations that showed Stage 2+ adoption by the 90-day mark.

> Hi [Name] — following up one more time on the digital security corpus. If [Org Name] has implemented any of the guidance, I'd like to document it as an anonymized case study — what worked, what the barriers were, what changed for clients. This would strengthen the guidance for other organizations in similar situations.
>
> Would a 20-minute call or a few written questions work? Your organization would be anonymized unless you prefer attribution.
>
> If this isn't the right moment, no pressure. I'll circle back in the fall.

Case study interviews follow a five-question guide:

1. What was the digital security posture of your client intake process before you reviewed the corpus?
2. Which specific elements of the corpus were implemented? (data broker opt-outs, communication protocol changes, device hygiene, other)
3. What barriers prevented full implementation?
4. What changed for clients as a result?
5. What would make this guidance more useful for your organization's context?

### Feedback Aggregation

Log all feedback in the CSV tracker (`feedback-collection-template.csv`) under the `feedback_summary` field. Preserve verbatim quotes from 90-day replies — these will drive Tier 2 and Tier 3 messaging adjustments. Specifically watch for:

- Consistent gap mentions (e.g., "we needed Spanish-language materials" from 3+ organizations → produce a Spanish-language summary before Tier 2)
- Consistent friction points (e.g., "the technical sections are too complex for our staff" → add a non-technical summary document)
- Consistent referral patterns (e.g., multiple organizations referring to the same intermediary → add that intermediary to Tier 2 outreach list)

---

## Section 3: Effectiveness Metrics

### What "Effective" Means for This Corpus

The corpus's purpose is to reduce the risk of immigration enforcement actions against people who implement its guidance. Measuring this directly is impossible — you cannot know how many ICE encounters did not happen because someone performed data broker opt-outs or adopted Signal. Measure proxy indicators instead.

### Proxy Metrics (Observable Without Direct Access to Client Data)

**Organizational capacity metrics** (collected via follow-up survey):
- Number of organizations that updated their client intake security protocols as a result of the corpus
- Number of organizations that added digital security training to staff onboarding
- Number of organizations that established Signal or secure communication channels with clients specifically because of the corpus

**Resource diffusion metrics** (observable externally):
- Number of times the Gist URL appears in organizational resource pages, newsletters, or toolkits
- Number of attorney or paralegal audiences reached through organizational training events that incorporated corpus content (ask implementing orgs to estimate reach)
- Number of community education sessions that used corpus content (Part 0, data broker opt-outs) as a structured handout

**Technical implementation signals**:
- Reports of clients successfully completing data broker opt-outs (observable via follow-up with implementing orgs)
- Adoption of recommended communication tools (Signal, ProtonMail) in client-facing workflows
- Reduced use of unencrypted communication channels for sensitive client information

### Organizational Maturity Model (Before/After)

For organizations that complete a 180-day case study interview, use a simple 5-point maturity scale across four dimensions to capture before/after state:

| Dimension | 1 (None) | 3 (Partial) | 5 (Full) |
|-----------|---------|------------|---------|
| Client data handling | No documented protocol | Protocol exists, inconsistently followed | Written protocol, trained staff, audited quarterly |
| Communication security | Unencrypted email and phone standard | Signal used for some sensitive communications | Signal + ProtonMail standard for all client comms |
| Device hygiene | No policy | Staff briefed, no enforcement | Full device encryption, MDM policy, annual training |
| Data broker exposure | No mitigation in place | Some clients referred to opt-out resources | Systematic opt-out process integrated into client intake |

Target: 30% of case study organizations show a +1 or better improvement on at least two dimensions within 180 days of initial contact.

### Measurement Challenges and Workarounds

**Challenge 1: Organizations won't share internal metrics.** Workaround — ask about observable behaviors rather than metrics. "Did any attorney attend a training that used this material?" is answerable. "What is your digital security incident rate?" is not.

**Challenge 2: Attribution is impossible.** Any organization that implemented data broker opt-outs in 2026 may have done so because of this corpus or because of the EFF, ProPublica, or another source. Workaround — don't claim attribution; collect self-reported connection. Ask "did this corpus contribute to the decision?" not "was this corpus the reason?"

**Challenge 3: Most feedback comes from the most engaged minority.** Organizations that reply and implement will over-represent the impact in feedback data. Organizations that did nothing will be invisible. Workaround — track non-response explicitly. For every 100 sends, record the number with no reply at 30 days, 90 days, and 180 days. This gives a realistic denominator for all rate calculations.

**Challenge 4: Timelines are long.** A legal aid organization may not implement guidance until a significant ICE enforcement action creates urgency. Effectiveness may spike at unpredictable moments. Workaround — maintain an evergreen follow-up system. Log every Tier 1 contact as "open indefinitely" until they explicitly decline further contact. Re-engage after major enforcement news events.

---

## Section 4: Community Engagement Patterns

### GitHub Gist as a Proxy for Open-Source Engagement

The corpus is published as a GitHub Gist rather than a full repository, which limits certain engagement signals (no stars, no forks, no pull requests on a Gist). If the corpus is later migrated to a full GitHub repository, the following metrics become available: star trajectory, fork count, open issues, and pull request contributions.

In the current Gist format, track:

**View count trajectory** (log monthly):
- Launch baseline: record on send day
- 30 days: compare to launch
- 90 days: compare to 30-day mark
- 180 days: compare to 90-day mark

A healthy trajectory for a targeted distribution of this size: 300-500 views in the first 30 days, leveling off to 50-100 incremental views per month thereafter as organic search and referral traffic drives slow but steady access. Comparable security guidance Gists (e.g., Christopher Allen's digital rights documentation on GitHub) show similar long-tail patterns — most views occur after the initial distribution wave through organic citation.

**Referral patterns**: If you have access to GitHub traffic analytics on the Gist (available if it's under your authenticated account), check the referrer breakdown at 30-day intervals. Traffic from digital rights organization domains (eff.org, accessnow.org, cdt.org) indicates Tier 2 engagement. Traffic from law school or .edu domains indicates academic uptake.

### Social Media Monitoring

Track mentions of the corpus and related terms across platforms where Tier 1-3 audiences are active:

**Mastodon/fediverse**: Search `#opsec`, `#undocumented`, `#immigration`, and `#palantir` weekly in the first month, then monthly. Save any post that references the corpus or its core concepts.

**Twitter/X**: Monitor `palantirELITE`, `immigration opsec`, and `data broker immigration`. Alert threshold: any retweet or thread involving a Tier 1-2 organization account.

**LinkedIn**: Monitor the EFF, NILC, ACLU, RAICES, and Access Now company pages for posts mentioning digital security, surveillance, or Palantir. LinkedIn organic reach for policy content is low but engagement from professional networks is high-quality.

**Reddit**: Monitor r/privacy, r/netsec, r/immigration for threads referencing the corpus or its specific claims (ELITE system, data broker opt-outs, Palantir immigration surveillance).

The realistic expectation for social media engagement at Tier 1 launch: zero organic mentions in the first 30 days unless the user shares the Gist URL directly in a social post or a Tier 1 organization shares it through their own channels. Social signal comes primarily from Tier 2 outreach (digital rights organizations and researcher communities have active social presences).

### Policy Database and Media Monitoring

**Overton** (overton.io, free tier): Search quarterly for "immigration" + "operational security" + "data broker" in policy documents. Any citation of the corpus in a published policy document, NGO report, or government filing is a Stage 5 event.

**Google Scholar**: Set an alert for the document's title or key phrases. Scholar indexes preprints, NGO reports, and working papers — expect a 6-18 month lag before academic citations appear, consistent with the Tier 2 academic conversion timeline.

**Media monitoring**: If a journalist from The Intercept, ProPublica, The Guardian, or a regional immigration beat reaches out following the Tier 2 press organization outreach, this is a Stage 5 event. Track reporter name, outlet, and date of contact. Any published article is a Stage 5 citation.

---

## Section 5: Long-Horizon Success Indicators and Assessment Gates

### Assessment Gate Structure

All gates use the organization-level CSV tracker as the data source. Calculate metrics at each gate; do not estimate or project forward.

**30-Day Gate (June 15 if Tier 1 launches mid-May 2026)**

| Metric | Threshold | Action if Below |
|--------|-----------|----------------|
| % Tier 1A orgs acknowledging receipt | ≥35% | Resend to non-responders with shorter subject line and one-sentence body before 45-day mark |
| % expressing intent to review | ≥15% | Audit personalization quality of non-responding sends; rewrite two weakest subject lines |
| Reply type breakdown | >50% of replies at Stage 1 or higher | If most replies are Stage 0 routing ("I'll pass this along"), add a specific one-line ask to the follow-up: "Has the document reached the person who handles client digital security?" |
| Gist view count | Baseline + ≥100 views | If view count is flat, verify the Gist URL was correct in all sends |

**90-Day Gate (August 15 if Tier 1 launches mid-May)**

| Metric | Threshold | Action if Below |
|--------|-----------|----------------|
| % orgs reporting at least one implementation action | ≥25% | Before Tier 2 launch, revise implementation guide's "Quick Start" section to remove barriers identified in 30-day feedback |
| Evidence of policy or training change | At least 1 documented case | Prioritize one case study interview before Tier 2 begins; use as proof point in Tier 2 outreach |
| Referral contacts generated | ≥3 new warm contacts | If follow-up question 3 ("Is there someone else who should have this?") produced no referrals, add the explicit question to the 90-day follow-up template |
| Gist view trajectory | Month 2 > Month 1 (organic growth signal) | If flat, consider publishing a public Mastodon or LinkedIn post about the corpus at the 90-day mark to generate referral traffic |

**Tier 2 Launch Prerequisite Check (90-day gate is the primary prerequisite gate)**

Before launching Tier 2 (~4 weeks after Tier 1 = approximately June 12-15), confirm:
- At least one Tier 1 organization has acknowledged the corpus (not just receipt — at least Stage 1 engagement)
- No material errors have been surfaced by Tier 1 feedback that would embarrass the sender in Tier 2 technical circles
- The Gist URL still loads correctly and is not rate-limited or restricted

Tier 2 does not require Tier 1 to achieve full conversion. A single Stage 2+ engagement from Tier 1 is sufficient proof that the corpus is reaching real audiences, which strengthens Tier 2 outreach credibility.

**180-Day Gate (November 15)**

| Metric | Threshold | Action if Below |
|--------|-----------|----------------|
| % orgs demonstrating sustained adoption | ≥40% of Stage 2+ contacts | Target the September re-engagement wave at Stage 1 contacts who showed interest but did not convert |
| Corpus cited in published policies/guidelines | ≥3 | If below, this indicates Tier 3 (academic/researcher) outreach has not yet converted; adjust expectations and extend timeline |
| Case study interviews completed | ≥2 | Use case studies as social proof for Tier 2 follow-up wave and Tier 3 outreach emails |

**12-Month Gate (May 2027)**

| Metric | Definition |
|--------|-----------|
| Tier 1 impact | Framework cited in at least 5 organizational resource lists, toolkits, or training curricula |
| Tier 2 impact | At least one peer-reviewed citation, conference paper, or published policy brief references the threat model |
| Tier 3 impact | Community reach: organizations that received the corpus have collectively trained or advised ≥500 individuals |
| Policy influence | Framework referenced in a legal filing, amicus brief, legislative testimony, or published civil rights organization position paper |

The 12-month policy influence metric is a stretch target, not a baseline expectation. Most think tank frameworks that achieve policy citation do so within 6-18 months of distribution to the right intermediaries (the academic sector and legal aid networks are the primary pipeline for this). The realistic 12-month outcome is Tiers 1 and 2 converted, strong community adoption, and early signals of academic or legal citation.

### Red Flags Requiring Intervention

- **Zero replies from Tier 1A organizations after 45 days**: Either the contacts are wrong (verify nilc.org, raicestexas.org, ilrc.org), the subject line is blocking delivery, or the send volume triggered spam filtering. Investigate deliverability before attempting a second send.
- **Consistent feedback that corpus is "too technical"**: The non-technical summary and Part 0 standalone document should be produced before the 90-day follow-up wave. This is the most likely content gap based on the audience profile.
- **Multiple organizations citing the same missing element**: If 3+ organizations in feedback mention the same gap (e.g., Spanish-language materials, Know Your Rights legal addendum, phone-specific guidance for communities with limited laptop access), treat this as a required corpus update before Tier 2.
- **Gist URL changes or GitHub account suspension**: Maintain a backup distribution URL (a second Gist or a public Google Doc) and update all follow-up templates if the primary URL becomes unavailable.

### Tier 2 and Tier 3 Adjustments Based on 90-Day Findings

The 90-day assessment gate is the primary input to Tier 2 and Tier 3 strategy. Before launching Tier 2, review:

1. **Message framing**: If Tier 1 feedback shows organizations engage more with the Part 0 (data broker opt-outs) than the technical countermeasures, lead the Tier 2 digital rights outreach with the threat model angle (which is what digital rights organizations will engage with most) rather than the implementation guide.

2. **Format**: If Tier 1 feedback shows PDFs are more useful than a long Gist, produce a PDF summary before Tier 2 sends go out. Digital rights organizations are more likely to circulate a linked PDF than a Gist URL.

3. **Proof points**: Any Stage 3+ adoption by a Tier 1 organization becomes a credibility signal for Tier 2 outreach. "NILC's tech team reviewed and shared internally" (if accurate and with permission) is a stronger opening than a cold introduction.

4. **Missing audience segments**: If referral question responses from Tier 1 repeatedly point to an organization type not on the Tier 2 or Tier 3 lists (e.g., domestic violence shelter networks that serve mixed-status families, or labor union legal departments), add those organizations to the Tier 2 or Tier 3 contact lists before the next wave.

---

## Baseline Measurement Before Tier 1 Launch

Before sending a single Tier 1 email, record the following baseline data points. This makes the 30-day and 90-day measurements meaningful.

- **Gist view count**: Log on launch day
- **Google Alert results**: Note any existing web mentions of the corpus URL or key phrases before launch
- **Overton search results**: Run the baseline policy citation search before launch; note zero results as the starting point
- **GitHub Gist referrer data**: Log current referrer breakdown if available
- **Social media baseline**: Search the corpus URL and key phrases on Mastodon, Twitter, and LinkedIn; record zero results as baseline

---

*Document complete. Use in conjunction with `feedback-collection-template.csv` for operational tracking and `adoption-tracking-dashboard-spec.md` for monitoring infrastructure.*
