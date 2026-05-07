---
title: "Phase 2 Threat Briefing: Union Organizers and Labor Networks"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
audience: Union organizers, labor union staff, shop stewards, labor network coordinators, AFL-CIO affiliates, independent unions, worker centers, domestic worker networks
distribution-tier: Phase 2 — Priority Constituency 4
companion-playbooks:
  - activist-organizing-playbook.md
  - phase-2-activist-organizing-security-playbook.md
  - opsec-playbook.md
  - device-hardening-guide.md
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
next-review: 2026-08-07
---

# Phase 2 Threat Briefing: Union Organizers and Labor Networks

**For**: Union organizers, labor union staff, shop stewards, labor network coordinators, worker centers, and domestic worker networks
**Date**: May 7, 2026
**Prepared by**: Cybersecurity Hardening Project (public-source research corpus)
**Companion resource**: Full OpSec corpus — https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

---

## Why Labor Organizers Are Targeted in May 2026

Labor organizing in 2026 sits at the intersection of two threat systems that have previously operated largely independently: immigration enforcement and political surveillance. The convergence is documented and operational.

Workers who participate in labor organizing and who also have immigration vulnerability face a specific compounded threat: employer-initiated cooperation with ICE that converts a workplace dispute into a deportation action. The NLRB's traditional framework for protecting immigrant workers during organizing campaigns has been significantly weakened under the current administration, with new NLRB leadership rolling back General Counsel Jennifer Abruzzo's electronic monitoring guidance and signaling a less aggressive enforcement posture on employer surveillance of organizing activity.

The second threat vector is broader but affects all organizers regardless of immigration status: the DHS and State Department AI-powered social media surveillance program, confirmed operational through three labor union lawsuits filed in federal court in October 2025, has demonstrably chilled protected labor speech. Over 60% of UAW members and over 30% of CWA members who were aware of the surveillance program reported changing their social media activity. This chilling effect operates before any enforcement action — the mere existence of the surveillance program suppresses protected activity.

---

## Current Threat Landscape — May 2026

### Threat 1: DHS Penlink PLX — Real-Time Location Tracking of Organizers

The Department of Homeland Security awarded a $2.9 million contract to Penlink PLX, a surveillance system that intercepts, aggregates, and analyzes live communications from phone calls, texts, and internet activity. Penlink collects cellphone location data from advertising SDK networks and allows users to search that data to understand which cellphones were in specific locations at specific times, and what other locations those cellphone users have visited.

Privacy advocates have documented ICE using Penlink to identify and track individuals who observed ICE enforcement operations. The system enables location-based profile construction without a warrant, without probable cause, and regardless of citizenship or immigration status.

**What this means for labor organizing**: Organizers who attend rallies, picket lines, union meetings, or worker center events at predictable locations and times are generating persistent location history that is accessible via Penlink to any DHS component — including ICE. For organizing campaigns in sectors with high concentrations of immigrant workers (agriculture, food processing, domestic work, hotel and hospitality), an organizer's presence at repeated organizing events builds a location pattern that can be used to identify and target immigrant workers through their association with a known organizer.

**Source**: Prism Reports, "DHS is Buying Access to Real-Time Location Data — The Latest Expansion of Its Invasive Surveillance Technology" (April 29, 2026) — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/

---

### Threat 2: AI-Powered Viewpoint Surveillance — UAW/CWA/AFT Lawsuit

The United Automobile Workers, Communications Workers of America, and American Federation of Teachers filed suit in U.S. District Court for the Southern District of New York in October 2025 against the Departments of State and Homeland Security. The suit documents a mass surveillance program that uses AI and automated technology to monitor the social media accounts of visa holders and lawful permanent residents — targeting those who express political viewpoints the administration disapproves of.

U.S. agencies — including State, DHS, USCIS, and ICE — have contracts with Babel Street, ShadowDragon, and similar platforms for tools that continuously monitor social media at scale. The EFF, which joined the lawsuit, documented that the program goes beyond passive monitoring: flagged individuals face visa revocation proceedings, deportation filings, and in some documented cases, detention.

**Documented chilling effect (from lawsuit discovery)**:
- Over 60% of UAW members aware of the program had changed their social media activity
- Over 80% of UAW members who were noncitizens had changed their social media activity
- Over 40% of CWA members who were noncitizens had changed their activity

This is not a speculative future risk. It is a documented present suppression of labor speech.

**What this means for labor organizations**: Your member communications, public social media accounts, and organizing campaign materials are under continuous monitoring by AI tools operating under federal contracts. Any content characterizing organizing activity as political protest — immigration rallies, sanctuary city advocacy, calls for worker justice tied to immigration enforcement — is within the documented targeting parameters of the surveillance program.

**Source**: EFF, "Labor Unions, EFF Sue Trump Administration to Stop Ideological Surveillance of Free Speech Online" — https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online

---

### Threat 3: Babel Street Persistent Monitoring — Organizers as Permanent Subjects

Babel Street holds confirmed DHS, ICE, CBP, and State Department contracts. Its "persistent search" feature continuously monitors any new content appearing online that matches flagged individuals, keywords, or geographies — without a new query being initiated. Once an organizer is flagged (through protest attendance, social media, or association with a targeted organization), all future public content they generate is automatically monitored.

Amnesty International's 2025 investigation documented Babel Street being deployed specifically against political organizers, with DHS using keyword searches to identify "radicalized groups" and flag individuals for visa revocation. Importantly, the designation "radicalized" in this context is based on keyword matching in political advocacy content — not on any criminal conduct.

**What this means for labor networks**: Organizers with public-facing roles in labor campaigns — shop stewards who post on union social media, organizers who speak at public events that generate social media coverage, workers who testify at NLRB hearings — are the most exposed. Their public presence is the entry point for persistent surveillance designation.

**Source**: Amnesty International, "Caught in the Net" — https://www.amnesty.org/en/documents/amr51/7101/2023/en/

---

### Threat 4: Flock Safety ALPR and Protest Vehicle Tracking

EFF's November 2025 investigation documented more than 50 federal, state, and local agencies running hundreds of Flock Safety automated license plate reader (ALPR) searches specifically against vehicles present at labor and political organizing events — the 50501 protests (February), Hands Off (April), and No Kings (June and October 2025).

Flock Safety's ALPR network operates across 5,000+ communities. A vehicle's license plate appearing at labor organizing events across multiple dates is permanently stored and queryable — building a record of organizing activity that does not depend on any digital communication being monitored.

**The intersection with immigration enforcement**: For labor campaigns in sectors with high concentrations of immigrant workers, an organizer's vehicle appearing at multiple organizing events can be correlated with Penlink location data and ELITE address confidence score updates for workers who also appear at those locations. The result is that organizing activity produces immigration enforcement intelligence without any phone, email, or social media surveillance being required.

**Source**: EFF, "How Cops Are Using Flock Safety to Surveil Protesters and Activists" (November 2025) — https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/

---

## Sector-Specific Response Architecture

### Step 1: Social Media Compartmentalization for Organizing Campaigns (Immediate)

The AI viewpoint surveillance program creates a specific protocol need for labor organizations: separation between public organizing communications and internal strategic planning.

- **Public social media accounts**: Operate on the assumption that all content is monitored by Babel Street persistent search. Only post content you are willing to have reviewed by a federal agency. Do not post content combining political organizing with immigration advocacy that would give Catch and Revoke monitoring a basis for visa-related action against immigrant members.
- **Internal organizing communications**: Use Signal for all strategic communications among organizers. The UAW/CWA/AFT lawsuit has not produced an injunction — the surveillance program continues to operate during litigation. Signal stores nothing compellable.
- **Member communications with immigration vulnerability**: For organizing campaigns involving immigrant workers, share companion corpus Part 0 (data broker opt-out guide) as standard intake material. The commercial location data their devices generate is the primary attack surface for ICE.

### Step 2: Vehicle and Physical Security Protocol for Events (30 Days)

The Flock Safety ALPR documentation requires organizers to treat their vehicles as tracked entities at any labor organizing event that has political visibility:

- For high-visibility events: consider whether organizer vehicles need to park away from the event site and walking is feasible
- For events in jurisdictions with documented ALPR deployment: assume license plate data is being captured and stored
- For organizers with immigrant workers who also attend events: brief them specifically on the vehicle tracking documentation and on the correlation between ALPR data and ELITE address confidence scores

The activist organizing playbook (phase-2-activist-organizing-security-playbook.md in the companion corpus) contains the full vehicle and physical security protocol.

### Step 3: Know Your Rights Training — DHS Administrative Subpoenas (30 Days)

DHS has issued administrative subpoenas to Google, Meta, Reddit, and Discord seeking the identities of anonymous social media account operators — and these platforms have voluntarily complied with some requests. This is not a future risk: it is a documented capability being actively used.

For labor organizations with anonymous or pseudonymous social media accounts used for organizing:
1. Understand that the platform's compliance with a DHS administrative subpoena does not require a warrant or judicial approval
2. Any account tied to an organizer's personal email, phone number, or payment method creates a discoverable link to their real identity
3. For accounts that must maintain operational separation: use dedicated email (Proton account not linked to personal information), payment methods without personal identifiers, and account registration via Tor or a trusted VPN

---

## Playbooks Available

- **activist-organizing-playbook.md** — Full-length counter-surveillance guide for organizing and protest contexts, including Babel Street, drone surveillance, ALPR, and biometric ID at protest perimeters
- **phase-2-activist-organizing-security-playbook.md** — Condensed May 2026 version with specific protocol for organizers by role (communications coordinator, legal observer, frontline organizer)
- **opsec-playbook.md** — Core operational security applicable to all organizing staff
- **device-hardening-guide.md** — Device hardening protocols including border-crossing guidance for organizers who travel

---

## Timeline

- **Now**: Brief organizing staff on social media compartmentalization; implement Signal for internal strategic communications
- **30 days**: Vehicle protocol training; DHS administrative subpoena know-your-rights briefing
- **June 12, 2026**: FISA 702 deadline — watch for warrant reform outcome
- **August 7, 2026**: Quarterly review of this briefing
- **Fall 2026**: Midterm election — elevated threat window for organizing events correlated with electoral politics

---

## Sources

1. Prism Reports: DHS Buying Access to Real-Time Location Data via Penlink PLX (April 29, 2026) — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/
2. EFF: Labor Unions, EFF Sue Trump Administration over Ideological Surveillance — https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online
3. FedScoop: State, DHS Sued by Union Groups over AI-Fueled Surveillance — https://fedscoop.com/social-media-ai-surveillance-unions-state-dhs-lawsuit/
4. EFF: How Cops Are Using Flock Safety to Surveil Protesters and Activists (November 2025) — https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/
5. Citizen Lab: Uncovering Webloc — Analysis of Penlink's Ad-Based Geolocation Surveillance Tech — https://citizenlab.ca/research/analysis-of-penlinks-ad-based-geolocation-surveillance-tech/
6. Amnesty International: Caught in the Net (Babel Street investigation) — https://www.amnesty.org/en/documents/amr51/7101/2023/en/
7. FedScoop: Acting ICE Director Denies Existence of Database Tracking US Citizens — https://fedscoop.com/ice-dhs-database-surveillance-technology-hearing/

---

*Briefing date: May 7, 2026. Corpus reflects surveillance landscape as of May 7, 2026. Quarterly review: August 7, 2026.*
