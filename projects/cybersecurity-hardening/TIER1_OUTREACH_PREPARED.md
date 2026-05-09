---
title: "Tier 1 Outreach Package — Ready for Manual Execution"
project: cybersecurity-hardening
created: 2026-04-26
status: ready-for-execution
prepared-by: research-agent
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
---

# Tier 1 Outreach Package — Ready for Manual Execution

**Prepared for**: Anya  
**Date prepared**: 2026-04-26  
**Corpus Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108  
**Estimated execution time**: 35–50 minutes for all five organizations

---

## What This Document Is

This is a complete, ready-to-send outreach package for Tier 1A distribution of the OpSec corpus (threat model + countermeasures playbook + implementation guide). It contains:

- Verified contact information for all five Tier 1A organizations
- Personalized email drafts for each, tailored to their specific focus and audience
- Delivery method for each (direct email vs. web contact form)
- A send-tracking checklist
- Notes on what to do if you get a response

All five organizations are immigration legal aid organizations with direct client relationships with the population most at risk from ICE's ELITE targeting system. They are the highest-priority distribution targets in the corpus.

**Do not use the Gist URL from TIER_1A_OUTREACH.md** — that file contains a placeholder URL from an earlier draft. The correct published URL is the one at the top of this document.

---

## Pre-Send Checklist (5 minutes before starting)

- [ ] Open the Gist URL and confirm it loads: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Copy the Gist URL to your clipboard
- [ ] Insert your name wherever `[Your name]` appears in drafts below
- [ ] Add any local context you have with a specific organization (personal connection, mutual contact)
- [ ] Create a tracking record (text file, spreadsheet, or note) with these columns:
  ```
  Organization | Method | Date/Time Sent | Response Received | Follow-up Date
  ```

---

## Organization 1: National Immigration Law Center (NILC)

**What they do**: The largest immigration legal nonprofit in the United States. Policy, litigation, and direct services for low-income immigrants and their families. High reach into the legal community.

**Why this corpus is relevant for them**: Their legal teams advise clients and allied organizations on how to navigate enforcement risk. The threat model's primary-source structure is directly useful for their advocacy and litigation work, and Part 0 (data broker opt-outs) is actionable for their clients immediately.

### Verified Contact Information

| Field | Value |
|-------|-------|
| General email | info@nilc.org |
| Web contact form | https://www.nilc.org/about-us/contact-us/ |
| Phone | (213) 639-3900 (Los Angeles HQ) or (202) 216-0261 (DC office) |
| Mailing address | 3450 Wilshire Blvd. #108-62, Los Angeles, CA 90010 |
| Executive Director | Marielena Hincapie |
| COO (IT oversight) | [title; email format: {lastname}@nilc.org] |
| Press contacts | Elizabeth Beresford (917-648-0189), Andrea Alford (703-477-1075) |
| Spanish-language press | Nery Espinosa (214-263-1294) |

**Recommended delivery**: Send via web contact form at https://www.nilc.org/about-us/contact-us/ AND email to info@nilc.org. The form ensures it reaches whoever monitors organizational inquiries; the email creates a direct reply path.

**Confidence on contact info**: High. General email and form confirmed via their website. Staff email format ({lastname}@nilc.org) confirmed via multiple press releases.

---

### NILC Email Draft

**Subject**: Resource for NILC legal team — primary-sourced OpSec guide for Palantir ELITE threat landscape

**Body**:

> Hi NILC team,
>
> I'm sharing a resource I think is directly relevant to your work defending undocumented clients and their families against ICE enforcement.
>
> The federal government is using Palantir's ELITE platform to generate "address confidence scores" for deportation targeting — pulling from Medicaid records, DMV records, commercial data brokers, and location data sold by smartphone apps without a warrant. Palantir's IRS contract maps financial relationships across organizations and individuals connected to groups under tax scrutiny — creating a data surface beyond immigration enforcement. A newly published three-part guide documents this surveillance infrastructure in full (all sourced from FOIA disclosures, government contracts on USASpending.gov, and court filings) and provides step-by-step countermeasures organized by risk tier.
>
> The guide also addresses communications verification: the NRSC March 2026 Talarico deepfake case established a real-world precedent for voice and video manipulation targeting political and legal figures, and the countermeasures playbook includes protocols for verifying the identity of callers and video contacts in sensitive contexts.
>
> The highest-leverage section for NILC's clients requires no technical expertise: Part 0 walks through submitting opt-outs to the 20 data brokers that ICE queries without warrants. It takes 2–4 hours and directly degrades the confidence scoring used in ELITE targeting. There is a documented path for California residents without government-issued ID (using AB 60/AB 1766 state IDs to access California's DELETE Act DROP platform) — which may be particularly useful for your California-based clients.
>
> The full corpus is three documents published at a single link:
>
> - Threat model: What government systems can actually see (Palantir ELITE, NSA Section 702, Venntel location data, DOGE database consolidation), with primary source citations
> - Countermeasures playbook: Specific actions organized by threat tier
> - Implementation guide: Exact steps, verification checkpoints, troubleshooting
>
> https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
>
> Given NILC's reach into the immigration legal community, I'd recommend sharing this with your affiliated programs — especially Part 0 and the Tier 1 checklist, which clients can act on immediately.
>
> Happy to discuss any of this or answer questions about the sourcing.
>
> [Your name]

---

## Organization 2: CLINIC — Catholic Legal Immigration Network, Inc.

**What they do**: National network of 400+ Catholic-affiliated immigration legal programs. CLINIC's reach across affiliated programs makes it a force multiplier — one successful contact here can seed the guide across hundreds of direct-service programs nationwide.

**Why this corpus is relevant for them**: Their affiliated programs serve a high volume of clients at direct enforcement risk. A resource they can pass to affiliates directly multiplies its reach. The implementation guide is designed to be client-accessible, making it suitable for their community legal education work.

### Verified Contact Information

| Field | Value |
|-------|-------|
| General/national email | national@cliniclegal.org |
| Web contact form | https://www.cliniclegal.org/ (contact link in site nav) |
| Main website | https://www.cliniclegal.org |
| Headquarters | Silver Spring, MD (Washington DC metro area); also Oakland, CA |

**Recommended delivery**: Email to national@cliniclegal.org with the draft below. This is the primary organizational contact email confirmed via their website.

**Confidence on contact info**: High. national@cliniclegal.org confirmed as the main inquiry email.

---

### CLINIC Email Draft

**Subject**: New resource for CLINIC affiliates — data broker opt-out guide for clients facing ICE enforcement

**Body**:

> Hi CLINIC team,
>
> I wanted to share a newly published guide that I think is directly useful for your 400+ affiliated legal programs and their clients.
>
> ICE is using Palantir's ELITE platform to generate "address confidence scores" for deportation targeting — pulling from Medicaid records, DMV records, commercial data brokers, and smartphone location data without a warrant. Palantir's IRS contract maps financial relationships across organizations and individuals connected to groups under tax scrutiny — creating a data surface beyond immigration enforcement. A new three-part corpus documents this surveillance infrastructure in detail (all sourced from FOIA and court filings) and provides practical, tiered countermeasures.
>
> The corpus also covers communications security: the NRSC March 2026 Talarico deepfake case demonstrated that voice and video impersonation is now being deployed against legal and political figures, and the countermeasures playbook includes verification protocols for sensitive calls and video contacts.
>
> The highest-leverage section for your affiliate network: Part 0 of the implementation guide provides step-by-step instructions for submitting opt-outs to the data brokers that ICE queries. No technical expertise required, 2–4 hours per person, and it directly reduces the data available to ELITE targeting algorithms. There's a specific path for California residents without government-issued ID.
>
> The corpus:
>
> - Threat model: Confirmed government surveillance capabilities, all primary-sourced
> - Countermeasures playbook: Actions by threat tier (data broker opt-outs through device hardening)
> - Implementation guide: Exact steps with verification checkpoints
>
> https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
>
> Given CLINIC's infrastructure for reaching affiliated programs, I'd recommend considering distributing this to your network as a client resource — especially Part 0 and the Tier 1 checklist. The implementation guide is designed to be accessible to clients with no technical background.
>
> Happy to answer any questions about the content or discuss how to adapt it for your network's use.
>
> [Your name]

---

## Organization 3: RAICES (Refugee and Immigrant Center for Education and Legal Services)

**What they do**: Texas-based immigration legal aid and advocacy, with offices in San Antonio, Austin, Corpus Christi, Dallas–Fort Worth, and Houston. High-volume direct client services in one of the highest-enforcement states. Also does significant national communications and advocacy work.

**Why this corpus is relevant for them**: Texas is a primary ELITE deployment zone. RAICES clients are directly in the threat landscape documented in the corpus. Their communications team amplifies resources to their network and to the public.

### Verified Contact Information

| Field | Value |
|-------|-------|
| Communications email | communications@raicestexas.org |
| General phone | (833) 372-4237 |
| Mailing address | P.O. Box 786100, San Antonio, TX 78278 |
| San Antonio office | 131 Interpark Blvd, San Antonio, TX 78216 |
| Austin office | 3000 S IH-35 #200, Austin, TX 78704 |
| Director of Communications | Thaís Silva-Marques |
| Contact page | https://raicestexas.org/contact |

**Recommended delivery**: Direct email to communications@raicestexas.org — this is the most direct path to Thaís Silva-Marques (Director of Communications) and the team most likely to act on this.

**Confidence on contact info**: High. communications@raicestexas.org confirmed across multiple sources. Director of Communications name confirmed via professional directory.

---

### RAICES Email Draft

**Subject**: OpSec resource for Texas clients — Palantir ELITE threat model and data broker opt-out guide

**Body**:

> Hi RAICES communications team,
>
> I'm sharing a newly published security guide that I think would be valuable for your clients in Texas facing ICE enforcement risk.
>
> This guide maps the actual surveillance systems the federal government is using — including Palantir's ELITE platform, which generates "address confidence scores" by pulling from Medicaid records, DMV records, commercial data brokers, and phone app location data without a warrant — and provides specific countermeasures that clients can implement. Palantir's IRS contract maps financial relationships across organizations and individuals connected to groups under tax scrutiny — creating a data surface beyond immigration enforcement that extends to advocacy organizations like RAICES.
>
> Given RAICES' presence in Texas, this is particularly relevant: Texas is a primary operational zone for ELITE, and the guide documents how the system prioritizes enforcement targets by pulling data from state government records and commercial brokers that operate heavily in Texas.
>
> The guide also addresses communications verification: the NRSC March 2026 Talarico deepfake case demonstrated that synthetic voice and video is being used to impersonate trusted contacts, and the countermeasures playbook includes protocols for verifying caller and video identity in sensitive legal and advocacy contexts.
>
> Key sections:
>
> - Threat model: What government systems can see (Palantir ELITE, NSA Section 702, Venntel location data, LexisNexis DHS contract), all primary-sourced from FOIA and contracts
> - Countermeasures playbook: Specific steps by threat level
> - Implementation guide: Exact steps with verification checkpoints — designed for clients without technical background
>
> The highest-impact section for most clients: Part 0, data broker opt-outs. No technical expertise needed, 2–4 hours, directly reduces the data ICE uses to target people.
>
> https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
>
> Happy to discuss the content or answer questions about specific sections.
>
> [Your name]

---

## Organization 4: Immigrant Legal Resource Center (ILRC)

**What they do**: National policy and resource organization serving legal programs nationwide. Strong documentation, publications, and training infrastructure. They publish widely-used practice guides for immigration practitioners. If they add this corpus to their resource library or cite it in their publications, it reaches their entire practitioner network.

**Why this corpus is relevant for them**: ILRC's strength is producing and distributing resources to legal practitioners. The threat model's primary-source structure is specifically valuable for an organization that produces citable practitioner resources. Part 0 (data broker opt-outs) is immediately distributable through their existing client-facing channels.

### Verified Contact Information

| Field | Value |
|-------|-------|
| Press/communications email | kbello@ilrc.org (Kemi Bello, Communications Manager) |
| Press phone | (415) 321-8568 |
| Publications store | https://store.ilrc.org/publications |
| Main website | https://www.ilrc.org |
| Press room | https://www.ilrc.org/press-room |
| General contact page | https://www.ilrc.org/contact |

**Recommended delivery**: Email to kbello@ilrc.org (Communications Manager) — this is a confirmed direct contact, more likely to act on an external resource than a generic form. Frame as a resource for their publications/media list.

**Confidence on contact info**: High. Kemi Bello (Communications Manager) confirmed via press room research with direct email and phone number verified.

**Note**: ILRC does not provide direct legal services to individuals. Their distribution path is through their practitioner network and publications, not direct client services. The email draft is framed accordingly.

---

### ILRC Email Draft

**Subject**: New primary-sourced security guide for your practitioner network — ELITE threat model and client countermeasures

**Body**:

> Hi Kemi,
>
> I wanted to share a comprehensive security guide that I think fits well into ILRC's resources for legal practitioners.
>
> This corpus documents the federal government's immigration enforcement surveillance infrastructure — Palantir's ELITE address confidence scoring system, the data broker pipeline (LexisNexis, Venntel, Babel Street), NSA Section 702 collection, and the DOGE cross-agency database consolidation — and provides step-by-step countermeasures organized by risk tier. Notably, Palantir's IRS contract maps financial relationships across organizations and individuals connected to groups under tax scrutiny — creating a data surface beyond immigration enforcement with direct implications for the legal organizations and practitioners in ILRC's network.
>
> What makes this resource unusual for the field: it's sourced entirely from primary documents — FOIA disclosures, government contracts on USASpending.gov, court filings, and investigative reporting from 404 Media, The Intercept, and EFF. The threat model is citable by practitioners advising clients on enforcement risk. The corpus also covers emerging social engineering vectors: the NRSC March 2026 Talarico deepfake case established a real-world precedent for voice and video manipulation, and the countermeasures playbook includes verification protocols practitioners can recommend to clients and colleagues.
>
> The three documents:
>
> - Threat model (primary-sourced): ELITE/ImmigrationOS, NSA Section 702, Venntel, DOGE master database
> - Countermeasures playbook: Tiers 1–3, from data broker opt-outs to device hardening
> - Implementation guide: Step-by-step with verification checkpoints, designed for clients with no technical background
>
> https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
>
> I'd suggest ILRC consider making this available through your practitioner resource channels — in particular Part 0 (data broker opt-outs) and the Tier 1 checklist, which practitioners can distribute directly to clients concerned about enforcement exposure.
>
> Happy to answer any questions about the sourcing or content.
>
> [Your name]

---

## Organization 5: National Lawyers Guild (NLG)

**What they do**: Membership organization for progressive lawyers, law students, and legal workers. Strong track record on civil liberties, protest support, and security culture. NLG's Mass Defense Committee is particularly relevant — it coordinates legal support for people facing government targeting.

**Why this corpus is relevant for them**: NLG members already understand operational security at a conceptual level. The threat model's legal sourcing (court filings, FOIA, government contracts) aligns with NLG's practitioner culture. The Mass Defense Committee is the most natural entry point — they support people at highest enforcement risk.

### Verified Contact Information

| Field | Value |
|-------|-------|
| Mass Defense Committee | massdef@nlg.org |
| General communications | communications@nlg.org |
| Press inquiries | press@nlg.org |
| Membership/committee inquiries | membership@nlg.org |
| Main phone | (212) 679-5100 |
| Mailing address | P.O. Box 1266, New York, NY 10009-8941 |
| Main website | https://www.nlg.org |

**Note on Tech & Law Committee**: The NLG website does not list an active "Tech & Law Committee" in their current committee directory. The closest relevant bodies are: Mass Defense Committee (massdef@nlg.org) and the general communications office. The previous outreach template's reference to a "Tech & Law committee" appears to be outdated or informal. Route through Mass Defense and Communications.

**Recommended delivery**: Email to massdef@nlg.org (primary — most directly relevant) and CC or separately email communications@nlg.org. Mass Defense is the most active committee with direct connection to the threatened population.

**Confidence on contact info**: High. All emails confirmed via NLG's official contact page. Committee structure confirmed via their committee directory.

---

### NLG Email Draft

**Subject**: New OpSec corpus for NLG Mass Defense — Palantir ELITE threat model sourced from FOIA and contracts

**Body**:

> Hi NLG Mass Defense team,
>
> I'm sharing a newly published security corpus that I think will interest your committee and your membership — it bridges the legal and technical threat model for people facing immigration enforcement, protest support, and civil liberties risk.
>
> The guide documents federal surveillance systems against specific legal authorities and primary sources:
>
> - Palantir ELITE's "address confidence scores" (ICE contract, FOIA-documented operation)
> - NSA Section 702 collection scope (349,823 targets in 2025 — confirmed from Intelligence Community transparency reports)
> - Commercial data broker pipeline (LexisNexis $9.75M DHS contract, Venntel location data procurement, DOGE cross-agency database)
> - Clearview AI ICE contract ($9.2M, September 2025)
> - Palantir's IRS contract, which maps financial relationships across organizations and individuals connected to groups under tax scrutiny — creating a data surface beyond immigration enforcement with direct relevance to civil liberties and Mass Defense work
>
> All of the threat model is built on primary sources — USASpending.gov contracts, FOIA disclosures, court filings, and investigative reporting. It is structured to be citable.
>
> The corpus also covers social engineering and communications security: the NRSC March 2026 Talarico deepfake case is documented as a real-world example of voice and video impersonation targeting legal and political figures — a threat vector directly relevant to NLG members advising people under investigation.
>
> The countermeasures go from Tier 1 (data broker opt-outs, Signal configuration — no tech expertise required) through Tier 3 (Qubes OS, VeraCrypt, hardware security keys — for people with reason to believe they are direct investigation targets).
>
> https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
>
> I'd recommend sharing this with your membership and your security practices working groups. The implementation guide's verification checkpoints are specifically designed to prevent the false confidence problem — confirming that countermeasures actually worked rather than assuming they did.
>
> Happy to discuss the threat model sourcing or any specific sections.
>
> [Your name]

---

## Execution Checklist

Copy this section and check off each item as you complete it.

### Preparation (5 minutes)

- [ ] Gist URL confirmed accessible: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Your name inserted into all five drafts
- [ ] Tracking record created
- [ ] Personalization additions noted (any personal connections to specific orgs)

### Send Phase

- [ ] **NILC** — Email to info@nilc.org + web form at https://www.nilc.org/about-us/contact-us/
  - Date/time sent: _______________
  - Notes: _______________

- [ ] **CLINIC** — Email to national@cliniclegal.org
  - Date/time sent: _______________
  - Notes: _______________

- [ ] **RAICES** — Email to communications@raicestexas.org
  - Date/time sent: _______________
  - Notes: _______________

- [ ] **ILRC** — Email to kbello@ilrc.org (Kemi Bello, Communications Manager)
  - Date/time sent: _______________
  - Notes: _______________

- [ ] **NLG** — Email to massdef@nlg.org, optionally CC communications@nlg.org
  - Date/time sent: _______________
  - Notes: _______________

### Post-Send (5 minutes)

- [ ] All 5 sends confirmed (check sent folder or form confirmation screens)
- [ ] Tracking record updated with dates
- [ ] Follow-up reminders set for 5 business days after each send

---

## Hard-to-Reach Notes and Research Gaps

### NLG Tech & Law Committee
The NLG does not currently have an active Tech & Law committee in their published committee directory. Their current committee list covers animal liberation, anti-racism, disability justice, environmental justice, indigenous peoples' rights, international, labor/employment, mass defense, military law, prison abolition, queer caucus, and TUPOCC. The Mass Defense Committee (massdef@nlg.org) is the closest match for our purposes and is more directly relevant to people facing enforcement risk.

### NILC Technology/Security Team
NILC does not publish a dedicated technology or security team email. The IT function sits under the COO's office. The best entry point is info@nilc.org or the web form — from there, ask to be connected to whoever manages digital security resources for clients and affiliated programs. If you have a personal connection to any NILC staff, use that channel instead.

### ILRC Direct Contact
ILRC's contact page returned a 403 error during research, so the contact information above (Kemi Bello, Communications Manager, kbello@ilrc.org, (415) 321-8568) was confirmed via press room research and external directories. If this email bounces, the fallback is their general contact form at https://www.ilrc.org/contact.

### RAICES Direct Email
The communications@raicestexas.org address is the best confirmed contact. RAICES's main contact page does not list individual staff emails publicly, but the communications director role (Thaís Silva-Marques) is confirmed, and communications@raicestexas.org is the standard channel for press and partnership inquiries. If no response within 10 days, consider using the main phone line (833-372-4237) to ask for the communications team.

### CLINIC Contact Form Location
The clinic.org/contact URL in the earlier distribution checklist resolves to cliniclegal.org (CLINIC rebranded to use this domain). National@cliniclegal.org is the confirmed email; a web form backup exists at cliniclegal.org if the email doesn't get a response.

---

## After You Send: Response Handling

### Positive response ("we'd like to share this / thank you")
Reply: "Thank you — please let me know if your team or clients find gaps or have feedback. A v2 is planned for quarterly review given how quickly the surveillance landscape is evolving."

Offer: "If it would be useful, I can put together a plain-language one-page version of Part 0 in Spanish and English specifically for community distribution — just let me know."

### Question about technical content
Point to primary sources directly: FOIA documents, USASpending.gov for contract figures, court filings. The threat model section lists all sources in Section X. The sourcing is designed to be verifiable by legal practitioners.

### Concern about scope ("individual measures aren't sufficient against full government resources")
This concern is addressed directly in the corpus executive summary. The response: the corpus targets the bulk commercial surveillance infrastructure — data brokers, location data markets, ad-tech tracking — that operates without warrants at scale. It explicitly does not claim to protect against a targeted investigation with a valid court order. Those are different threat models, and the corpus is explicit about which one it addresses.

### "Is any of this legal?"
Yes — everything in the guide describes legal activities in the United States. Data broker opt-outs are a statutory right (CCPA, California DELETE Act, and broker-specific opt-out mechanisms). Signal, GrapheneOS, Tor Browser, VeraCrypt, and Mullvad VPN are all legal tools used by journalists, lawyers, and millions of ordinary people.

---

## What Comes Next: Tier 1B and 1C

After Tier 1A responses arrive (or after 10 days if no responses):

**Tier 1B — Community-Based Organizations**:
- CASA (casaforall.org): Large mid-Atlantic immigrant advocacy org
- Make the Road Network (maketheroadamerica.org): State chapters with community education programs
- United We Dream (unitedwedream.org): National DACA-focused network
- Centro de los Derechos del Migrante (centrocdm.org): Cross-border migrant worker organizing

**Tier 1C — Mutual Aid Networks**:
- National Bail Fund Network (nationalbailfund.org)
- Food Not Bombs local chapters
- Anarchist Black Cross

See DISTRIBUTION_CHECKLIST.md for full contact strategy and messaging for these groups.

**Tier 2 outreach** (digital rights amplifiers — EFF, Access Now, Fight for the Future) can run in parallel with Tier 1B/C if bandwidth allows.

---

## URL Discrepancy Note

The existing file `TIER_1A_OUTREACH.md` in this project directory contains a different Gist URL:  
`https://gist.github.com/esca8peArtist/2c5ba783bd06405749b7c3decebaa6d4`

That URL appears to be from an earlier draft or placeholder. The confirmed published Gist URL (from the task brief and confirmed as the live publication) is:  
`https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`

Use the URL in this document. Verify it loads before sending any emails.
