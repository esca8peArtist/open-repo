---
title: "Distribution Checklist: OpSec Corpus"
project: cybersecurity-hardening
created: 2026-04-26
status: ready
---

# Distribution Checklist: OpSec Corpus

This document lists where to share the corpus, in what order, and what to say when sharing it. The corpus addresses a population under active threat — distribution speed matters.

---

## Priority Order

Distribute to **direct-need networks first**, then to **amplifier networks**, then to **researcher/policy networks**. Do not do these simultaneously if bandwidth is limited — the direct-need audience is the reason the corpus exists.

---

## Tier 1: Direct-Need Networks (Highest Priority)

These are the channels closest to the people who face immediate threat from ICE's ELITE system, Palantir's data integration, and location data harvesting.

### 1A. Immigration Legal Aid Organizations

Organizations that work directly with undocumented clients and their families.

| Organization | Contact point | Notes |
|-------------|---------------|-------|
| National Immigration Law Center (nilc.org) | Staff mailing list or contact form | Share with their tech/security team specifically |
| CLINIC — Catholic Legal Immigration Network | clinic.org/contact | 400+ affiliated programs nationally |
| RAICES (raicestexas.org) | communications@raicestexas.org | High-volume client base in Texas |
| Immigrant Legal Resource Center (ilrc.org) | Has a publications/resources channel | May want to host as a resource |
| National Lawyers Guild (nlg.org) | Tech & Law committee | NLG has Signal expertise; will understand the threat model |

**What to send**: The executive summary (from `publication-prep.md`) as the email body. Attach or link the full corpus. Specifically call out Part 0 (data broker opt-outs, no technical expertise required) as immediately actionable for their clients.

---

### 1B. Community-Based Organizations Serving Immigrant Communities

These are the ground-level organizations that have direct trust relationships with the people most targeted.

- **Local interfaith sanctuary networks**: Search "[city] sanctuary network" — most have Signal groups or email lists
- **CASA (casaforall.org)**: Large mid-Atlantic immigrant advocacy organization with community education infrastructure
- **Make the Road Network (maketheroadamerica.org)**: Has state chapters with community education programs
- **United We Dream (unitedwedream.org)**: National DACA-focused network with communications infrastructure
- **Centro de los Derechos del Migrante (centrocdm.org)**: Organizes migrant workers in Mexico and the U.S.

**What to send**: A simplified version of the Tier 1 checklist from the implementation guide. The full corpus may overwhelm community educators — consider extracting Part 0 and the Tier 1 checklist (Part 7) as a standalone two-page handout for community distribution. Do not modify the technical content, but a plain-language cover sheet in Spanish and English is worth creating.

---

### 1C. Mutual Aid Networks

Mutual aid networks communicate directly with people who may not be reached by formal legal organizations.

- **National Bail Fund Network (nationalbailfund.org)**: Knows how to reach people in legal jeopardy
- **Local mutual aid networks**: Search "[city] mutual aid" — most have Slack, Signal, or Telegram groups
- **Food Not Bombs local chapters**: Street-level presence in most major cities
- **Anarchist Black Cross**: Prison support network with experience in security culture

**What to send**: Part 0 (data broker opt-outs) and the Tier 1 checklist. These audiences understand operational security intuitively — emphasize that Part 0 is the highest-leverage action and takes 2–4 hours.

---

## Tier 2: Security and Digital Rights Amplifiers

These organizations and communities will both use the corpus and amplify it to their own audiences.

### 2A. Digital Rights Organizations

| Organization | Notes |
|-------------|-------|
| Electronic Frontier Foundation (eff.org) — Deeplinks | Can publish a feature linking to the corpus; contact press@eff.org |
| Fight for the Future (fightforthefuture.org) | Campaign-focused digital rights org; active on immigration/surveillance |
| Center for Democracy & Technology (cdt.org) | Policy-focused; good for congressional staff and researchers |
| Access Now (accessnow.org) | International focus but strong U.S. presence; has digital security helpline |
| Freedom of the Press Foundation (freedom.press) | Focused on journalists; will spread to that network specifically |

**What to send**: The full corpus URL plus the executive summary. EFF in particular may want to cite the threat model section in their own reporting — the primary-source structure is designed for this.

---

### 2B. Security Research Communities

| Community | Channel | Notes |
|-----------|---------|-------|
| Privacy Guides community (privacyguides.org/forum) | Forum post | High-quality audience; may surface gaps worth addressing in a v2 |
| r/privacy (reddit.com/r/privacy) | Subreddit post | Large audience; will generate both signal boosts and critical feedback |
| Signal app community channels | Signal group chats for security practitioners | Effective for word-of-mouth among security-aware activists |
| Hacker News (news.ycombinator.com) | Show HN post | Can reach technical practitioners who will both use and improve the corpus |
| Techdirt community | Comment thread or tip to Masnick | Tim Cushing/Mike Masnick cover surveillance law; may write about the threat model |

---

### 2C. Journalist Networks

| Outlet/Contact | Notes |
|----------------|-------|
| The Intercept — theintercept.com/tips | Broke the Palantir IRS story; will recognize the threat model's sourcing |
| 404 Media — 404media.co | Broke the ELITE user guide story; will know this corpus |
| ProPublica — propublica.org/tips | Immigration enforcement coverage |
| The Guardian US — guardian.com/tips | Strong immigration surveillance coverage |
| Freedom of the Press Foundation press contacts | Can seed to their journalist network directly |

**What to send**: The executive summary and a note that the threat model is built on primary sources (FOIA, court filings, government contracts). These journalists have covered Palantir — they will recognize the sourcing as credible.

---

## Tier 3: Policy and Advocacy Networks

These are channels where the corpus has slower but longer-term impact.

### 3A. Civil Rights Legal Organizations

| Organization | Notes |
|-------------|-------|
| ACLU — aclu.org/contact | Strong Palantir-specific work; the threat model is compatible with their framing |
| Center for Constitutional Rights (ccrjustice.org) | Litigation-focused; may use threat model in civil rights cases |
| Brennan Center for Justice (brennancenter.org) | Policy-focused; covers surveillance law extensively |
| Electronic Privacy Information Center (epic.org) | FOIA specialists; will value the primary-source structure |

---

### 3B. Academic Researchers

- **Surveillance Studies Network**: International network of surveillance researchers
- **Critical Infrastructure Studies**: Academic community studying commercial surveillance
- **Law school clinics**: Immigration, civil rights, and technology law clinics often produce public-facing resources

**What to send**: The threat model section specifically, with a note that the corpus is designed to be primary-source citable.

---

### 3C. Labor Organizing Networks

| Network | Notes |
|---------|-------|
| Jobs With Justice (jwj.org) | National labor rights network with immigration justice focus |
| Service Employees International Union (seiu.org) | Large union with many immigrant members |
| United Farm Workers (ufw.org) | Agricultural workers; high immigration status risk |
| IWW (iww.org) | Industrial Workers of the World; historically strong security culture |

---

## Sharing Scripts

Adapt these for the channel. Do not copy-paste verbatim — personalize for the relationship.

### Email (for organizational contacts)

**Subject**: Resource — practical OpSec guide for immigration enforcement threat landscape

**Body**:

> I'm passing along a practical security guide I think is directly relevant to [organization]'s work.
>
> The short version: The federal government is using Palantir's ELITE platform, which generates "address confidence scores" to prioritize deportation targets by pulling from Medicaid records, DMV records, commercial data brokers, and location data sold by smartphone apps without a warrant. The guide explains these systems in detail — all sourced from FOIA disclosures, court filings, and government contracts — and then gives step-by-step instructions for what individuals can do about it.
>
> The most important section requires no technical expertise: Part 0 walks through submitting opt-outs to the data brokers that ICE queries without warrants. It takes 2–4 hours and directly degrades the confidence scoring used in ELITE targeting. There's a specific path documented for California residents without government-issued ID (using AB 60/AB 1766 state IDs to access the California DELETE Act's DROP platform).
>
> The corpus is three documents:
> - Threat model (what the government can actually see, with sources)
> - Countermeasures playbook (what to do about it, by threat tier)
> - Implementation guide (exact steps, verification checkpoints, troubleshooting)
>
> [URL]
>
> Happy to discuss if useful.

---

### Signal/Slack/Discord (for community channels)

**Short version**:

> Posting this because it's directly relevant to people in our network facing immigration enforcement risk.
>
> This is a three-part guide: what the federal government's surveillance systems actually do (sourced from contracts and court filings), what you can do to protect yourself, and exact step-by-step instructions.
>
> Most important action for most people: Part 0, data broker opt-outs. No tech expertise needed. 2–4 hours. Directly reduces your profile in the databases ICE queries without warrants.
>
> [URL]

**For technical channels** (add this):

> For those who want the technical depth: the threat model section covers Palantir's ELITE/ImmigrationOS/LCA stack, NSA Section 702, Venntel location data pipeline, and DOGE's master database project — all with primary source citations. The countermeasures go up to Tier 3 (GrapheneOS, VPN-then-Tor, VeraCrypt, Qubes OS).

---

### Social Media (Twitter/Mastodon/Bluesky)

**Thread opener**:

> The federal government is using Palantir's ELITE platform to generate "address confidence scores" for deportation targeting — pulling from Medicaid records, DMV records, location data harvested from your phone apps, all without a warrant.
>
> There are documented steps you can take to reduce your exposure. Here's a sourced, step-by-step guide:
> [URL]

**Follow-up tweet**:

> The most important action requires no technical expertise: submit opt-outs to the data brokers that ICE queries. Takes 2–4 hours. Directly degrades the confidence scoring that drives targeting.
>
> Part 0 of the guide walks through the 20 highest-priority brokers, including a path for undocumented California residents.

---

### Reddit Post (r/privacy, r/immigration, r/opsec)

**Title options**:
- "Practical OpSec guide specific to ICE/Palantir surveillance — sourced from FOIA and court filings, step-by-step implementation"
- "What the government's ELITE deportation targeting system actually does, and what you can do about it"
- "Three-part security guide: Palantir surveillance threat model + countermeasures + implementation steps"

**Body**:

> I'm sharing a three-document guide that maps the actual surveillance infrastructure (Palantir ELITE/ImmigrationOS/LCA, NSA PRISM, Venntel location data, DOGE master database) against specific countermeasures people can implement.
>
> Everything in the threat model is sourced from primary sources — FOIA disclosures, government contracts (USASpending.gov), court filings, and investigative reporting from The Intercept, 404 Media, and EFF. No speculation.
>
> The implementation guide works by tier: Tier 1 (journalists, advocates, healthcare workers) needs only data broker opt-outs and Signal configuration. Tier 2 (activists, organizers, people with immigration status vulnerability) adds GrapheneOS + VPN-then-Tor. Tier 3 (people with reason to believe they're direct investigation targets) adds Qubes OS, VeraCrypt, Monero, and hardware security keys.
>
> [URL]
>
> Happy to answer questions about specific sections.

---

## Post-Distribution Steps

1. **Track where you shared it** — so you can follow up with responses, corrections, or version 2 when the threat model needs updating.

2. **Set a quarterly review date** — the threat model is current as of April 2026. Section 702 reauthorization, DOGE litigation, and Palantir contract expansions are all evolving. A quarterly update note (even just "last reviewed [date], no material changes") maintains credibility.

3. **Create a feedback channel** — if you publish via GitHub Gist, the comments section works. For a wider distribution, a Signal note or ProtonMail address for corrections is appropriate.

4. **Corrections protocol** — if a factual error is found in the threat model, update the Gist and note the correction at the top of the threat-model.md file with a date. Do not silently edit.

---

## What to Expect After Distribution

**Likely positive responses**: Security practitioners will recognize the primary-source structure as unusual and will spread it. Immigration advocates will forward Part 0 widely. The AB 60/AB 1766 DROP path will be cited specifically by California-based advocates.

**Likely criticism**: Some readers will argue that individual countermeasures are insufficient against a determined adversary with full government resources. The corpus agrees — it explicitly states this in the executive summary and conclusion. The response: the corpus targets the bulk commercial surveillance infrastructure, not a targeted investigation. These are different threat models.

**Likely questions**: "Is this legal?" Yes — everything described is legal in the United States. Opt-outing from data brokers is a statutory right. Signal encryption is legal. GrapheneOS is legal. Tor is legal. VeraCrypt is legal.
