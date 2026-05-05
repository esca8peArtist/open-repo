---
title: "Recipient Feedback Template — Tier 1 Distribution"
project: cybersecurity-hardening
created: 2026-05-05
status: production-ready
use: Survey (async email) + interview script (synchronous call or Signal exchange)
companion: tier-1-effectiveness-framework.md, tier-1-feedback-collection-protocol.md
---

# Recipient Feedback Template

**Purpose**: Structured feedback collection from Tier 1 organizations at the 90-day mark. Used in two modes: (1) async email survey for contacts who have engaged but are unlikely to take a call, and (2) interview script for contacts who have indicated willingness to discuss in depth (Stage 2+).

**Design principle**: The hardest implementation feedback to collect is also the most valuable: what prevented adoption, not what enabled it. Most survey instruments optimize for positive confirmation. This template is calibrated to surface barriers and gaps because those are the inputs that drive corpus revision before Phase 2.

**Privacy note**: Do not record or transcript calls without explicit consent. Do not attribute specific quotes to organizations without permission. Use anonymized aggregates in any public-facing reporting ("two immigration legal aid organizations reported...").

---

## Part 1: Async Email Survey (90-Day Mark)

Send to all contacts at Stage 1 or above who have not explicitly opted out of follow-up. This is the full written version; a briefer version appears in the Day 90 follow-up template in `tier-1-feedback-collection-protocol.md`. Use this longer version when a contact has shown substantive engagement and you want richer data.

---

**Subject**: Three questions about the OpSec guide — 5 minutes, your call whether to answer

> Hi [Name],
>
> Three months since I sent the digital security guide for immigration legal teams. A few specific questions — not a survey form, just reply with whatever is useful. Any response, even partial, helps shape the next version.
>
> **Question 1 — Did your organization look at it?**
> Any of these:
> - [ ] Yes, [Name] reviewed it
> - [ ] We shared it with [team or partner]
> - [ ] It's on our list but hasn't happened yet
> - [ ] It's not the right fit for our work
>
> **Question 2 — If you or a colleague looked at it: what section mattered most?**
> - [ ] Part 0 (data broker opt-outs — the immediate action section)
> - [ ] The threat model (what the ELITE system actually does)
> - [ ] The implementation guide (device setup, Signal, Tor)
> - [ ] The Tier 1 checklist (the "start here" summary)
> - [ ] Haven't gotten to it yet
>
> **Question 3 — What's the biggest gap?**
> What should the guide cover that it currently doesn't — or what did you find missing for your specific work or clients?
>
> (One sentence is fine. "No gap" is a valid answer.)
>
> **Question 4 — What made implementation harder than expected?**
> If you or your clients tried any steps: what got in the way?
> - [ ] Too technical for clients/staff without tech background
> - [ ] Clients primarily use phones, not laptops — instructions don't apply
> - [ ] No Spanish-language version (critical gap for our client base)
> - [ ] Gist URL format is hard to share internally or print
> - [ ] Legal questions — unclear whether certain steps create documentation we'd prefer not to have
> - [ ] Staff capacity — couldn't prioritize it during active enforcement period
> - [ ] Other: [free text]
>
> **Question 5 — Who else should have this?**
> Is there a colleague, partner organization, or network that you think would find this directly useful?
> (If comfortable sharing a name or contact, that's helpful. If not, describing the type of organization is enough.)
>
> That's the full ask. Reply with whatever you have — even a single word per question is useful.
>
> [Your name]

---

## Part 2: Interview Script (Stage 2+ Contacts)

For contacts who indicate willingness to speak (by replying positively to the email survey or previously expressing interest in discussing). Use for a 20–30 minute call or synchronous Signal exchange. Skip questions where the email survey already provided a clear answer.

**Before the interview**: Review what you already know from their replies. The interview should deepen, not repeat, what the email collected.

---

### Opening (2 minutes)

> Thanks for taking the time. I have four areas I'd like to cover — adoption barriers, gaps in the guide's content, whether the threat model matched what your organization actually faces, and how it fits your sector's work specifically. We can stop at any point and I'll take whatever you're comfortable sharing.
>
> Before I start: anything you share will be used to improve the guide. I won't attribute quotes to [Organization] by name without asking you first. Is that okay?

---

### Section A: Adoption Barriers

These questions diagnose what delayed or prevented implementation. The goal is to understand the obstacle before assuming a content fix is the right solution.

**A1. Route to the right people**

> When the guide arrived, where did it land in your organization? Did it go directly to someone who could act on it, or did it take some routing?

*What you are listening for*: Routing failures (landed with communications staff, not program staff). If so: probe which role or department should have received it.

> If it needed to be routed, what happened — did it reach the right person eventually?

**A2. Time and capacity**

> Immigration legal organizations are under a lot of active pressure right now. Did staff capacity affect whether anyone had time to review this?

*What you are listening for*: Timing effects — the guide may be valuable but the distribution moment was wrong. Note whether a follow-up at a different time (e.g., after an enforcement pressure wave passes) would be more effective.

**A3. Technical accessibility**

> The implementation guide covers device hardening, encrypted messaging, and network configuration. For your clients or staff — what's the realistic technical baseline? Are people primarily using phones? Do they have reliable internet access?

*What you are listening for*: Phone-first vs. laptop-first populations; low-bandwidth or intermittent internet access; clients who rely on shared devices (public computers at legal aid offices). These constraints require different format solutions than the current Gist-format guide.

**A4. Legal and documentation concerns**

> Some organizations have raised questions about whether documenting that clients took security steps could create records that would complicate legal proceedings. Did that concern come up for your team?

*What you are listening for*: Legal caution about documentation trail (attorney-client privilege implications of writing down that a client changed their phone settings). This is a real concern in immigration legal practice and may require an explicit disclaimer in the corpus.

**A5. Language**

> For Tier 1B/1C only — your clients primarily communicate in [Spanish / other language]. The guide is currently English-only. Did that limit how you could use it?

---

### Section B: Guide Gaps

These questions identify missing content. The goal is to find scenarios the guide doesn't address, not just features the recipient would like to see.

**B1. Scenario coverage**

> Think about a client situation you've encountered in the past few months that felt like a security risk. Was there anything in that situation the guide didn't address?

*What you are listening for*: Specific scenarios — a client who had already been stopped by ICE and wanted to know if their phone was compromised; a client whose landlord was potentially reporting information to authorities; a family where some members had documents and others didn't. These are real threat scenarios that may not map to the guide's current tier structure.

**B2. The DROP platform and California-specific path**

> For California-based organizations — did the section on the California DELETE Act DROP platform and the AB 60 ID pathway make sense for your clients? Were there steps missing, or was it hard to explain to clients without a driver's license?

*What you are listening for*: Procedural gaps in the DROP platform walkthrough. The AB 60 state ID to DELETE Act pathway is the guide's most distinctive contribution for California-based undocumented residents. Any report that it was unclear or incomplete is a high-priority fix.

**B3. The "what happens after I take these steps" question**

> Did clients or staff ask what happens after they complete the opt-outs — whether brokers actually process them, how long it takes, whether it makes a meaningful difference?

*What you are listening for*: A gap in the guide around outcome expectations. The guide documents how to opt out, but may not adequately explain what to expect after opting out. Unrealistic expectations (belief that opt-outs make someone invisible to ICE) are a potential harm; under-realistic expectations (belief that opt-outs do nothing) undermine motivation. Both require content additions.

**B4. Missing scenarios for specific populations**

> Are there populations your organization serves that the guide doesn't seem written for? Elderly clients, clients without smartphones, clients who are DACA recipients vs. undocumented, mixed-status families?

*What you are listening for*: Audience gaps. The guide's Tier 1 population is implicitly mobile-phone-enabled, English-literate or Spanish-literate, and individually at risk. Elderly clients, clients with disabilities, or clients embedded in surveillance-heavy housing situations (detention-adjacent environments) may require different countermeasure logic.

---

### Section C: Threat Model Accuracy

These questions determine whether the guide's description of the ELITE system and its data sources matches what organizations actually observe on the ground. This is the hardest feedback to collect but the most important for credibility.

**C1. Does the ELITE documentation match what you see?**

> The guide's threat model describes ICE using Palantir's ELITE system to generate deportation targeting scores by pulling from data brokers, Medicaid records, and DMV records. Does that match what you're seeing in your clients' cases — how ICE seems to be finding people?

*What you are listening for*: Ground-level corroboration or contradiction. If legal aid attorneys say their clients are being found through employer records, school records, or social media rather than the commercial data broker pipeline, that is important signal — the guide's emphasis on data broker opt-outs may be overweighted relative to other threat vectors.

**C2. Threat tiers**

> The guide divides risk into tiers based on how visible someone is in the enforcement system — whether they've had prior encounters with ICE, whether they're in removal proceedings, etc. Did that tier structure map onto how your organization thinks about client risk levels?

*What you are listening for*: Whether the tier framework resonates with practitioners who are already assessing client risk. If legal aid organizations use a different risk categorization model in their own practice, the guide's tier structure may need adjustment to align with how practitioners already work.

**C3. Current threat landscape accuracy**

> The guide was documented in early 2026. Have you seen any developments since then — new data sources ICE is using, new enforcement patterns, new risks — that the guide doesn't reflect?

*What you are listening for*: Temporal gaps. The threat model is built from documents available as of early 2026. If there have been FOIA disclosures, court filings, or enforcement incidents since then that reveal new ELITE capabilities or data sources, those need to be incorporated in the next version.

---

### Section D: Organizational Fit

These questions identify which organizational types found the guide most useful — and why — to calibrate Tier 2 outreach.

**D1. Your organization's use case**

> Looking back at the past three months — what is the most useful thing the guide ended up doing for your organization, even if it wasn't how you expected to use it?

*What you are listening for*: Unanticipated use cases. The guide may have been most useful not as a client education tool but as a staff training reference, or not as a data broker opt-out guide but as a threat model for litigation purposes.

**D2. Fit relative to peer organizations**

> In your network — other organizations doing similar work — do you think this guide would be useful to them, or would it face the same barriers you experienced?

*What you are listening for*: Sector-wide generalizability. If the barriers this organization faced are idiosyncratic (specific staff capacity issue, specific client population constraint), the guide may still be broadly useful. If the barriers are structural to the sector (all high-volume immigration legal organizations are understaffed), the guide needs adaptation, not just distribution.

**D3. What this guide does that others don't**

> Are there other security guides or resources your organization uses? What does this guide do differently from what you already have?

*What you are listening for*: Differentiation signal. If the guide duplicates resources organizations already have, adoption will not happen regardless of quality. If it fills a genuine gap (the ELITE documentation angle, the DROP platform path, the Tier 1 checklist structure), that differentiation is what to emphasize in Phase 2 outreach.

---

### Closing (2 minutes)

> That covers everything I wanted to ask. Is there anything that came up in our conversation that you'd want me to know — something I didn't ask about?

> One last question: if I improve the guide based on feedback like yours — would [Organization] be willing to be named as an early user in future outreach to organizations like EFF or IRE? No obligation at all, and I understand if you prefer to stay anonymous.

*If yes*: Log as "named citation permitted" and record what specifically they're comfortable being cited on (e.g., "used guide in client intake" vs. "confirmed threat model accuracy").

*If no*: Log as "anonymous only" — use organization type but not name in any Phase 2 communications.

---

## Part 3: Aggregation Key

After collecting survey and interview data from 90-day contacts, aggregate responses into these four buckets before using feedback to make Phase 2 decisions.

### Adoption Barriers Aggregation

| Barrier | Count | Organizations | Response Required |
|---|---|---|---|
| Technical complexity above client capacity | | | Add simpler Part 0 summary |
| Phone-first / no laptop access | | | Produce mobile-optimized version |
| Spanish-language gap | | | Produce Spanish Part 0 |
| PDF format needed (not Gist) | | | Produce PDF before Tier 2 sends |
| Legal / documentation concerns | | | Add legal-context disclaimer |
| Staff capacity (timing problem, not content problem) | | | Re-engage at lower-enforcement-pressure moment |
| Wrong routing (communications, not programs staff) | | | Research program-staff contacts before re-engagement |

**Threshold for action**: Any barrier cited by ≥2 organizations is a required fix before Tier 2 launch.

### Guide Gaps Aggregation

| Gap | Count | Organizations | Phase 2 Priority |
|---|---|---|---|
| DROP platform instructions incomplete | | | Critical — most distinctive content |
| Post-opt-out outcome expectations missing | | | High |
| Scenario coverage (specific populations not addressed) | | | Medium — document; prioritize if ≥3 orgs cite |
| Temporal update needed (new ELITE capabilities) | | | Critical if factual; Medium if contextual |
| Mixed-status family scenarios | | | Medium |

### Threat Model Accuracy Aggregation

| Assessment | Count | Organizations |
|---|---|---|
| Confirmed accurate (threat model matches what orgs observe) | | |
| Partially accurate (some elements match, others less central) | | |
| Inaccurate in specific area (describe): | | |
| Can't assess (not seeing enough enforcement activity to evaluate) | | |

**Threshold for action**: Any factual inaccuracy cited by ≥1 organization requires immediate verification against primary sources before Tier 2 distribution.

### Organizational Fit Aggregation

| Sector | Most Useful Section | Unanticipated Use Case | Referral to Tier 2 Type |
|---|---|---|---|
| Immigration legal aid (1A) | | | |
| Community-based org (1B) | | | |
| Mutual aid network (1C) | | | |

Use the "Most Useful Section" column to calibrate Tier 2 messaging. If Tier 1A organizations most value the threat model (not Part 0), lead the Tier 2 digital rights outreach with the sourcing quality angle. If Tier 1B organizations most value Part 0, lead the Tier 2 journalist outreach with the source protection practical gap angle.

---

*Template complete. The async email survey (Part 1) is ready to send at Day 90 post-launch. The interview script (Part 2) is ready to use for any Stage 2+ contact who indicates willingness to speak. Log all responses in the `feedback-collection-template.csv` file under the relevant columns. See `tier-1-effectiveness-framework.md` Section 5 for how feedback results map to the Condition A / B / C triage framework.*
