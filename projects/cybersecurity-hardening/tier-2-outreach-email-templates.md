---
title: "Tier 2 Outreach Email Templates — Four Sector-Specific Variants"
project: cybersecurity-hardening
created: 2026-04-30
status: ready-for-use
item: 31 — Tier 2 Distribution Execution
depends-on: ITEM14_TIER2_MESSAGING_ANALYSIS.md, tier-2-regional-messaging.md, tier-2-sector-contact-lists.md
gist-url: "https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108"
---

# Tier 2 Outreach Email Templates

**How to use this document**: Four sector templates follow. Each has a subject line, opening hook, two-to-three paragraph body, call to action, and signature block. Personalization variables are marked `{{like this}}`. Fill these before sending — generic sends to named individuals are worse than no send at all.

These templates extend and deepen the preliminary templates in `TIER2_DISTRIBUTION_PREP.md` and `TIER2_MESSAGING_TEMPLATES.md`. They incorporate the sector analysis from `ITEM14_TIER2_MESSAGING_ANALYSIS.md` and the jurisdiction-specific framing from `tier-2-regional-messaging.md`. Do not use the older templates from prior documents unless specifically updating to these versions.

**Shared principle across all four**: Every template leads with the sector's institutional mandate before describing the corpus. The corpus is positioned as a tool that extends what the recipient already cares about — not as a new thing that requires justification. The difference in response rate between a mandate-first and corpus-first open is significant.

---

## Template A: Digital Rights Organizations

**Best for**: EFF, CDT, STOP, Access Now, Privacy International, EPIC, Just Futures Law, Tor Project, Mozilla, Fight for the Future, noyb, Restore the Fourth

**Framing rationale** (from ITEM14): Digital rights organizations evaluate material on evidentiary quality, not humanitarian appeal. They need to know the corpus is sourced well enough to cite in policy briefs and legal filings. Lead with the litigation and policy-citation angle. The corpus's differentiator is methodological: every claim traceable to a primary source (FOIA document, government contract, federal court filing). Civil liberties framing outperforms harm-reduction framing with this sector, except for Access Now (operational helpline) where practical utility for at-risk populations should lead.

---

### Subject Line Options

**Primary**: `Data broker pipeline driving deportation targeting — sourced threat model (FOIA + court filings)`

**Variant A (for EFF, EPIC, Just Futures Law)**: `ELITE threat model — FOIA-sourced documentation for policy and litigation use`

**Variant B (for Access Now Helpline)**: `Commercial surveillance gap in standard opsec advice — relevant to Helpline population`

**Variant C (for STOP, referencing #PowerDownSurveillance)**: `ELITE data supply chain documentation — primary sources for #PowerDownSurveillance work`

---

### Email Body

```
To {{name}} at {{institution}}:

{{institution}}'s work on {{specific campaign or focus area — e.g., the commercial 
surveillance of immigrant communities / the #PowerDownSurveillance campaign / the 
GDPR enforcement of data broker ecosystems}} directly maps onto a corpus I've built 
documenting the same infrastructure from a different angle. I want to share it with 
you before pushing it to broader distribution.

The short version: ICE's Palantir ELITE platform converts commercial data broker 
purchases — location data from app SDK networks, Medicaid records, DMV data — into 
ranked deportation target lists through "address confidence scores." This is not 
speculation. Every claim in the threat model is sourced to FOIA-obtained procurement 
documents, government contracts, or federal court filings, structured so each claim 
is individually citable. The data broker section documents the specific vendors and 
purchase mechanisms in ELITE's data supply chain — Venntel/Gravy Analytics for 
location data, Thomson Reuters CLEAR for identity resolution, LexisNexis Risk 
Solutions for background data — with contract amounts and FOIA sources for each.

Two things in the corpus that may be directly useful to {{institution}}'s work: 
First, the confidence-scoring mechanism documentation — how ELITE translates 
administrative record aggregation (utility bills, DMV records, Medicaid enrollment) 
into ranked deportation priority — is detailed enough to support policy argument or 
litigation claims about the Fourth Amendment implications of warrantless commercial 
data purchase. Second, the Part 0 opt-out section documents the California DELETE 
Act's DROP platform as a pathway for residents without government-issued ID — a gap 
in existing opt-out guidance that {{institution}}'s policy or legal work may not have 
addressed. Both sections are structured for citation, not just reference.

If this is useful for ongoing policy work, litigation, or research at {{institution}}, 
I'd welcome a brief conversation. If it belongs with a specific team — privacy policy, 
surveillance litigation, legal — any routing you can provide is appreciated.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

**Signature**:
```
[Your name]
[Optional: affiliation or "independent researcher"]
[Optional: Signal number for secure follow-up]
```

---

### Personalization Notes by Organization

**EFF (Saira Hussain / Eva Galperin)**: Reference EFF's January 2026 report on ELITE/Medicaid data. "You've documented the ELITE/Medicaid angle in January 2026 — the corpus extends that with additional FOIA-sourced contract documentation on the commercial data broker supply chain that feeds ELITE separately from the Medicaid integration." Contact saira@eff.org directly; cc eva@eff.org.

**CDT (Tom Bowman)**: Reference his public characterization of ICE's data broker purchases as an attempt to "rebrand surveillance as a commercial transaction." "Your framing of data broker purchase as Fourth Amendment evasion is exactly the argument the corpus provides empirical grounding for."

**STOP (Michelle Dahl / Will Owen)**: Reference #PowerDownSurveillance campaign and STOP's win in the Thomson Reuters class action. "STOP's class certification against Thomson Reuters documents exactly the commercial-to-government data pipeline the corpus maps — this documentation may be useful for the ongoing campaign work."

**Access Now (Mohammed Al-Maskati)**: Modify body — lead with operational utility, not policy-citation framing: "Your Helpline operators work with undocumented populations who face the ELITE threat the corpus documents. Part 0 of the countermeasures playbook — data broker opt-outs accessible without technical expertise — may be directly integrable into Helpline workflow for this population." Send to help@accessnow.org.

**EPIC (Jeramie Scott)**: "The procurement document methodology in this corpus mirrors EPIC's own FOIA-sourced surveillance reporting. The DROP platform documentation (California DELETE Act pathway for residents without ID) is a specific gap in opt-out mechanism coverage that your Project on Surveillance Oversight may not have addressed yet."

**Just Futures Law (Paromita Shah)**: Reference EFF's 2025 Award for Leading Immigration and Surveillance Litigation won by Just Futures Law. "You're building cases in exactly this space — the FOIA-sourced contract documentation on ELITE's data supply chain is primary-source material for the type of surveillance litigation your organization has been litigating."

**Privacy International**: Add a line on international vendor scope: "The data broker supply chain documentation covers international vendor relationships — the SDK location data networks that feed ELITE operate globally, not just in US markets."

---

## Template B: Academic Cybersecurity Programs

**Best for**: CMU CyLab, UC Berkeley CLTC, MIT IPRI, Harvard Berkman Cyberlaw Clinic, UW Allen School, Stanford Cyber Policy Center, Georgia Tech IISP, Northeastern CPI, UT Austin CS, Johns Hopkins ISI, UCSD CESR, NYU Center for Cybersecurity

**Framing rationale** (from ITEM14): Academic programs evaluate material on methodological defensibility. They need to know they can cite or assign this without exposing themselves to critique. The primary ask is curriculum use or citation as a primary-source reference — not endorsement. Peer review framing is strategically smart: framing the outreach as an invitation to technical review positions researchers as contributors rather than audiences. The academic sector has longer conversion cycles (6-18 months); an initial positive response is a win even if curriculum integration takes a full semester cycle to materialize.

---

### Subject Line Options

**Primary**: `Primary-source threat model for ELITE commercial surveillance — potential curriculum resource or research reference`

**Variant A (for legal-focused programs like Harvard Berkman)**: `FOIA-sourced surveillance contract documentation — potential clinical case material`

**Variant B (for usable security programs like CMU CyLab, UW Allen School)**: `Accessibility-first countermeasures for commercial surveillance — usable security case study`

**Variant C (for policy-focused programs like UC Berkeley CLTC, Stanford Cyber Policy)**: `Commercial data broker deregulation as government enforcement infrastructure — documented case study`

---

### Email Body

```
Dear {{name or "program team"}} at {{institution}},

I'm writing to share a documented threat model that may have research or curriculum 
value for {{institution}}'s work in {{specific focus: usable security / surveillance 
policy / applied privacy / cyberlaw / data broker ecosystems}}.

The corpus documents ICE's Palantir ELITE platform — the system that aggregates 
commercial data broker purchases (location data from app SDK networks, Medicaid 
records, DMV data) into "address confidence scores" used to rank deportation targets. 
The methodological basis: every claim in the threat model is sourced to FOIA-obtained 
government documents, published procurement contracts, or federal court filings. The 
model documents not just what ELITE does but where each data category originates — 
the commercial data broker supply chain, the data integration architecture, and the 
confidence-scoring mechanism. It is structured to be usable as a primary-source 
reference in research on commercial surveillance, data broker ecosystems, and the 
intersection of algorithmic decision-making with enforcement.

The corpus is three parts: a threat model (~440 lines, FOIA-sourced claims throughout), 
a countermeasures playbook (~635 lines, tiered by technical capacity and calibrated to 
the documented attack surface rather than generic best practice), and an implementation 
guide (~1,030 lines, verified step-by-step with troubleshooting). {{CURRICULUM_ANGLE}} 
The countermeasures section is where I'd most value technical peer review from 
researchers with {{institution}}'s expertise — if there are gaps or errors that your 
team's security research would identify, I'd genuinely want to know before the corpus 
reaches wider distribution.

I'm sharing this openly and am not seeking endorsement — only feedback from people 
with the expertise to evaluate whether the technical claims hold up. If it fits a 
course or research context at {{institution}}, I'd be glad to discuss; if not, any 
routing to a colleague for whom it is relevant would be appreciated.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1eu7d108
```

**Signature**:
```
[Your name]
[Optional: affiliation]
[Contact email]
```

---

### {{CURRICULUM_ANGLE}} Variants by Program

**CMU CyLab (Lorrie Cranor — usable privacy)**: "For curriculum use, the Part 0 opt-out section is explicitly designed with accessibility-first principles — no technical expertise required, plain-language instructions, accessible without government-issued ID. This design approach is illustrative for usable privacy research and courses on security tool design for non-technical users."

**UC Berkeley CLTC (Ann Cleaveland — applied policy research)**: "For research use, the ELITE case study documents a specific policy consequence of commercial data broker deregulation: a deregulated commercial data market became a government enforcement infrastructure without any explicit legislative decision. The mechanism — purchase rather than seizure — is the policy gap the corpus maps empirically."

**MIT IPRI (cross-disciplinary law-technology)**: "The corpus is structured for cross-disciplinary use — legal citations (FOIA-sourced procurement documents, court filings) alongside technical documentation (data flow architecture, confidence-scoring mechanism). The dual-audience structure mirrors IPRI's own cross-disciplinary research orientation."

**Harvard Berkman Cyberlaw Clinic (Christopher Bavitz — clinical law)**: "For clinical case development, the FOIA-sourced procurement contracts and federal court filings in the threat model are primary-source material of the type your clinic uses for surveillance law case development. The DROP platform documentation (California DELETE Act pathway for residents without ID) raises a specific shield law question your hotline lawyers should be aware of: if an undocumented source's data was already in the commercial broker pipeline before a journalist-source relationship began, does the shield law protect that data?"

**UW Allen School (Roesner / Kohno — human-centered security)**: "For research in human-centered security, the countermeasures are calibrated to a specific, documented attack surface rather than generic best-practice maximalism. The tiering by user technical capacity and the explicit accessibility design of Part 0 are empirical design decisions driven by the threat model — a methodology case study for security tool design under realistic constraint."

**Stanford Cyber Policy Center**: "The ELITE case study documents the governance failure that results when commercial surveillance purchase evades constitutional warrant requirements. The implications for surveillance policy — how should regulation distinguish between commercial data purchase and Fourth Amendment-constrained surveillance? — are directly in scope for policy research at {{institution}}."

**Georgia Tech IISP / Northeastern CPI (applied crypto, privacy-preserving systems)**: "For research in privacy-preserving systems, the countermeasures section's data minimization architecture — documenting which data flows can be interrupted by technical means versus which require policy intervention — maps the boundary between technical and policy solutions in a documented real-world system."

---

## Template C: Researcher Communities

**Best for**: DEF CON community, CCC, Black Hat, ShmooCon, USENIX/ACM researchers, Citizen Lab, Mastodon infosec community, individual security researchers

**Framing rationale** (from ITEM14): Security researchers are trained to distrust overconfident claims. The peer-to-peer posture — "I'm sharing this for technical review before wider distribution, because I may have missed things" — reads as credible in this community. Technical correction is welcome; endorsement is not the goal. The framing "looking for critique before pushing harder to mainstream channels" signals the author treats researchers as genuine quality reviewers, not as legitimation rubber stamps.

---

### Subject Line Options

**Primary**: `ICE/Palantir ELITE threat model — looking for technical critique before wider distribution`

**Variant A (for DEF CON / conference CFP)**: `ELITE commercial surveillance architecture — documentation + countermeasures, proposing for [conference] CFP`

**Variant B (for CCC — civil liberties framing)**: `Commercial data purchase as Fourth Amendment evasion — FOIA-sourced architecture documentation`

**Variant C (for Black Hat — enterprise/CISO framing)**: `Commercial data broker supply chain as adversarial intelligence collection — threat modeling case study`

**Variant D (for Citizen Lab)**: `ELITE data supply chain documentation — seeking peer review from surveillance technology researchers`

---

### Email Body

```
Hi {{name or "team"}},

I'm distributing a threat model and countermeasures corpus on ICE's Palantir ELITE 
system to {{researchers in this community / security researchers}} before pushing it 
harder to mainstream channels, specifically because I want technical eyes on it first.

What ELITE does, per FOIA disclosures and federal court filings: aggregates commercial 
data broker location data (purchased from app SDK networks without a warrant), Medicaid 
enrollment records, DMV data, and other commercial sources into "address confidence 
scores" used to rank deportation targets. The threat model documents the data flows and 
source categories with citations — this is not advocacy conjecture, it is documented 
procurement architecture with named vendors, contract amounts, and FOIA source 
references for each claim. The commercial data broker supply chain section documents 
Venntel/Gravy Analytics (location data), Thomson Reuters CLEAR (identity resolution), 
and LexisNexis Risk Solutions (background data) with their specific roles in ELITE's 
data pipeline.

The countermeasures playbook is where I'd most want technical review. It covers: 
data broker opt-outs (Part 0, designed for non-technical users — no expertise required), 
GrapheneOS migration, Signal/Tor/VeraCrypt deployment, and network hardening (DNS over 
HTTPS, VPN, router configuration hardening). I've verified the tooling recommendations 
against the documented attack surface, but I'm not infallible about what I've missed. 
{{TECHNICAL_SPECIFIC_GAP}} If you find technical errors, gaps in the countermeasures, 
or places where the threat model overstates or understates the documented capability, 
I'd genuinely like to know. I'm treating critique as a contribution.

{{CONFERENCE_OR_COMMUNITY_SPECIFIC_CTA}}

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1eu7d108
```

**Signature**:
```
[Your name]
[Handle or affiliation if applicable]
[Signal or secure contact if appropriate for the community]
```

---

### {{TECHNICAL_SPECIFIC_GAP}} Variants

**For device security researchers**: "The GrapheneOS migration section in particular — I've documented the migration pathway but haven't fully addressed the threat model implications of baseband modem firmware, which remains an unresolved gap in most hardening guides for this population."

**For network security researchers**: "The DNS-over-HTTPS and VPN hardening section documents the recommended configuration but doesn't fully address the timing correlation attack surface on Tor for users on ISPs with limited traffic diversity — if this is a known gap in the literature I may have missed, I'd want to know."

**For data broker/privacy researchers**: "The commercial data flow documentation (app SDK → data broker → ICE purchase) is built from FOIA contracts and press coverage; I'm uncertain whether the full scope of Venntel/Gravy Analytics SDK partnerships is captured in public documentation, and whether there are additional data broker vendors in the ELITE supply chain that haven't appeared in public records."

**For surveillance architecture researchers (Citizen Lab framing)**: "I'm particularly uncertain about the completeness of the DOGE cross-agency integration section — the interoperability status of Palantir Foundry instances across DHS, IRS, SSA, and HHS is contested in public reporting, and I may be understating or overstating the current operational integration level."

---

### {{CONFERENCE_OR_COMMUNITY_SPECIFIC_CTA}} Variants

**DEF CON 34 (CFP open, deadline May 1, 2026)**: "I'm considering submitting a briefing to DEF CON 34 on the ELITE data supply chain architecture — treating it as a reverse-engineering problem: how does a commercial surveillance system become government enforcement infrastructure? If anyone has built on similar surveillance architecture documentation for a DEF CON talk, I'd welcome advice on how to structure the technical presentation. CFP contact: talks@defcon.org."

**CCC (40C3, December 2026)**: "The CCC community's work on state surveillance architecture is the peer context I'd most want this in. The Ethics, Society & Politics track at 39C3 covered exactly the intersection this corpus documents. If the call for participation for 40C3 opens in the coming months and this seems like a fit, I'd be interested in discussing a submission."

**Black Hat (CISO/enterprise framing)**: "For the enterprise security community: the ELITE data supply chain is a model for how adversaries aggregate commercial data at scale to build targeting intelligence. The architecture — SDK location data networks → data broker → enforcement agency query — generalizes beyond immigration enforcement to any scenario where an adversary purchases commercially collected data for targeting purposes. This is a supply chain risk that shows up in threat modeling for any organization whose employees' commercial data exposure creates adversary intelligence value."

**Mastodon/Fediverse post**: "Sharing for technical critique: [link]. Specific questions I'd welcome input on: (1) Is the GrapheneOS migration pathway still accurate with the current version? (2) Is the Tor usage section for non-technical users appropriately calibrated to the documented ELITE threat, or is it overkill/underkill? (3) Are there commercial data broker vendors in the ELITE supply chain that public records don't yet capture? Thread below. [Proceed with thread format]"

**Citizen Lab (peer institution framing)**: "I'm aware of Citizen Lab's prior work on surveillance technology documentation — the ELITE corpus uses the same FOIA-plus-technical-analysis methodology that Citizen Lab reports deploy. I'd value technical review from your team specifically because you've been building this type of documentation longer than I have, and because an error in this corpus that reaches a vulnerable population is the type of outcome worth preventing."

---

## Template D: Journalist Organizations and Press Contacts

**Best for**: Freedom of the Press Foundation (training team), IRE, CPJ, RCFP, SPJ, NAHJ, AAJA, The Intercept, ProPublica, The Guardian US

**Framing rationale** (from ITEM14): Journalist organizations have one primary concern: will this hold up when a source is at risk? The corpus's value to journalists is not general surveillance awareness — journalists are not naive about surveillance — but the specific commercial data layer that existing source protection training does not address. An undocumented source who follows standard journalist-recommended opsec (Signal, encrypted device, safe meeting location) may still be exposed through commercial data their apps have already sold to brokers that ELITE queries. This gap is documented, and documenting it is the corpus's most direct contribution to journalist source protection.

---

### Subject Line Options

**Primary**: `Source protection gap — undocumented sources and the commercial surveillance layer that opsec training misses`

**Variant A (for FPF training team)**: `Curriculum resource — commercial data broker surveillance not covered in standard source protection training`

**Variant B (for IRE/NICAR)**: `Data pipeline case study — ELITE commercial surveillance documentation for data journalism training`

**Variant C (for RCFP Legal Hotline)**: `Shield law question raised by pre-existing commercial data exposure of undocumented sources`

**Variant D (for The Intercept / ProPublica — press outreach)**: `Primary-source documentation on ELITE data supply chain — sharing for coverage follow-up`

---

### Email Body

```
Dear {{name or "team"}} at {{institution}},

Journalists protecting undocumented sources face a surveillance layer that most 
source protection training doesn't cover: the commercial data broker ecosystem 
that ICE queries without warrants to generate deportation targeting scores.

ICE's Palantir ELITE system pulls location data purchased from smartphone app SDK 
networks, Medicaid records, and DMV databases to build "address confidence scores" 
on deportation targets. An undocumented source who follows standard journalist-
recommended opsec — Signal for communications, encrypted device, careful about 
meeting locations — may still be exposed through commercial data their apps already 
sold to brokers before the journalist-source relationship began. This gap is 
documented in the threat model with FOIA-obtained contracts and court filings, not 
inferred.

{{JOURNALIST_ORG_SPECIFIC}}

The corpus covers both the threat and the practical countermeasures — not generic 
digital hygiene, but steps calibrated to the specific documented attack surface of 
ELITE. The threat model section documents the data flow with primary-source citations 
(FOIA contracts, named vendors, contract amounts) at a level of specificity that 
supports reportable journalism as well as training. 

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1eu7d108

{{JOURNALIST_CTA}}
```

**Signature**:
```
[Your name]
[Optional: Signal number if relevant to source protection context]
[Optional: SecureDrop reference if approaching a newsroom directly]
```

---

### {{JOURNALIST_ORG_SPECIFIC}} Variants

**Freedom of the Press Foundation (training team)**: "FPF's source protection training is the most rigorous standard in the field, and this is not a critique of that training — it's a documentation of a threat vector that the training cannot currently address because the threat model documentation didn't exist. The countermeasures playbook's Part 0 (data broker opt-outs, no technical expertise required) and the communication security section are designed to be integrable into existing source protection training curricula. They cover the commercial data layer that Signal and device encryption do not address. Given FPF's 'Digital Security 101: Crossing the U.S.-Mexico Border' module developed with EFF and UT El Paso, your team has the context to evaluate whether this fills the gap I believe it does."

**IRE / NICAR**: "For IRE's custom newsroom training program and NICAR curriculum: the threat model section — documenting the ELITE data supply chain with primary sources (FOIA contracts, named vendors, data flow architecture) — is ready-made case study material for data journalism training on commercial data pipeline investigation. It illustrates a complete commercial data flow from app SDK collection through broker intermediation to government enforcement use, with documented primary sources at each step. NICAR conferences have featured digital security sessions; this is a specific and current case study rather than a general framework."

**CPJ**: "CPJ's Journalist Assistance Network partners with FPF, RCFP, IWMF, and PEN America to provide immigration resources to journalists at risk. The corpus's threat model documents the specific commercial surveillance infrastructure that creates risk for journalists covering immigration and for undocumented sources of any journalist. The commercial data broker documentation covers internationally operating vendors — the same SDK location data networks that feed ELITE operate globally — which extends the relevance beyond US-based journalists."

**RCFP (Legal Hotline)**: "For the Legal Hotline's attorneys: the corpus raises a specific unresolved shield law question. If an undocumented source's commercial data (location history, app behavior, purchase records) was already in the data broker pipeline before the journalist-source relationship began, does the shield law protect that data when ICE queries a broker that holds it? The corpus does not resolve this question — it surfaces it with the documentation of ELITE's data supply chain. Hotline attorneys should know this gap exists because journalists seeking advice on protecting undocumented sources may be facing it without knowing the legal question is open."

**SPJ (Journalists Toolbox)**: "The SPJ Journalists Toolbox is the most widely used digital resource reference for working journalists. The corpus is a candidate for inclusion in the Digital Security section: it covers a specific documented threat (ELITE commercial surveillance) that existing Toolbox resources don't address, with countermeasures calibrated to that threat rather than generic digital hygiene. The DROP platform documentation (California DELETE Act pathway for residents without government-issued ID) is specifically novel and not covered in current Toolbox resources."

**NAHJ / AAJA**: "For {{NAHJ/AAJA}} members who cover immigration enforcement and who come from communities with documented surveillance exposure: the corpus is relevant both professionally (as a documented source of information on ELITE for reporting) and personally (as a guide to countermeasures for community members). The commercial data broker opt-out section is accessible without technical expertise and without government-issued ID — relevant for community members in mixed-status households."

**The Intercept / ProPublica (direct press outreach)**: "I'm sharing primary-source documentation that extends previous coverage of ELITE and Palantir's role in immigration enforcement. The FOIA-sourced contract documentation covers the commercial data broker supply chain in more granular detail than has appeared in public reporting — specific vendors, contract amounts, data categories purchased. The DROP platform documentation (California DELETE Act pathway for residents without ID) is a specific gap in the data broker opt-out landscape that hasn't appeared in prior coverage. I'm sharing this as source material, not requesting coverage — use it however is useful to your reporting, including just as background."

---

### {{JOURNALIST_CTA}} Variants

**FPF (training integration ask)**: "If the training team would be willing to review whether Part 0 and the communications security section are integrable into existing FPF curriculum, I would value that feedback — both for improving the corpus and because FPF's imprimatur on source protection training content carries more weight with working journalists than the corpus carries on its own."

**IRE (training resource offer)**: "If IRE's training program covers digital security topics in newsroom visits or NICAR sessions, I'd welcome a conversation about whether this case study material could be useful. I'm not seeking a sponsorship or formal partnership — a simple pointer to the right person at IRE for evaluating digital security training resources would be helpful."

**RCFP (legal question framing)**: "I'm not seeking a legal opinion from the Hotline — I'm flagging that the question exists. If Hotline attorneys are aware of relevant case law or shield statute language that addresses pre-existing commercial data exposure for journalist sources, I'd genuinely want to know to make the corpus more accurate."

**SPJ (Toolbox submission)**: "I would welcome the opportunity to submit the corpus for consideration as a Journalists Toolbox resource. Please direct me to the appropriate submission process if one exists."

**The Intercept / ProPublica / The Guardian (press — no ask)**: "No response necessary — sharing in case it's useful. Happy to discuss any of the sourcing or provide the original FOIA documents if that would help your verification process. Contact me via Signal at [number] or via SecureDrop."

---

*Templates complete — 4 sectors, 20+ subject line options, full personalization variable documentation. For contact details to populate {{name}} and {{institution}}, see `tier-2-sector-contact-lists.md`. For sequencing and calendar, see `tier-2-distribution-calendar.md`.*
