---
title: "Tier 2 Labor Organizer Implementation Guide: Union Security Operations and Strike-Era Digital Defense"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Tier 2
audience: Union organizers, shop stewards, labor campaign coordinators, AFL-CIO affiliates, independent unions, worker centers, domestic worker networks
depends_on:
  - activist-organizing-playbook.md
  - phase-2-activist-organizing-security-playbook.md
  - phase-2-threat-briefing-labor-organizers.md
  - opsec-playbook.md
word_count: ~2,400
---

# Tier 2 Labor Organizer Implementation Guide

**Most important finding**: As of May 2026, the legal framework protecting union digital communications from employer surveillance has been significantly weakened. Former NLRB General Counsel Jennifer Abruzzo's 2023 guidance limiting employer monitoring of organizing activity on personal devices is no longer being enforced by the current NLRB leadership. This means employers can and do monitor company-issued devices, company networks, and company email for organizing activity — and face no NLRB penalty for doing so. The operational response is complete compartmentalization: union organizing communications must never touch employer infrastructure. Not once.

---

## Part 1: Union Organizational Security — Communications, Meetings, and Physical Presence

### 1.1 Internal Communications Architecture

The threat model for union organizers in 2026 has three distinct layers that each require a different countermeasure.

**Layer 1: Employer surveillance of company infrastructure.** Email, Slack, Teams, and any device issued by or connected to employer networks is legally observable by the employer during work hours, and employer review of these communications for organizing activity carries no current NLRB penalty under the current enforcement posture. *Source: Institute for Free Speech, Anti-SLAPP Report 2025 — https://www.ifs.org/anti-slapp-report/*

**Layer 2: Government surveillance via DHS social media monitoring and Penlink location data.** The UAW, CWA, and AFT filed suit in October 2025 against DHS and State over AI-powered social media surveillance that chilled protected labor speech among over 60% of union members who were aware of the program. Penlink PLX, a $2.9M DHS contract, aggregates cellphone location data from advertising SDK networks — it can reconstruct which organizers attended which meetings based on their phone's location history. *Source: EFF lawsuit summary and Prism Reports Penlink coverage.*

**Layer 3: SLAPP litigation risk.** Employers in high-conflict campaigns have used strategic litigation to obtain discovery of organizer communications as a secondary objective — the lawsuit is the mechanism for the subpoena. As of March 2026, 40 states plus DC have anti-SLAPP laws. No federal anti-SLAPP law exists. The Free Speech Protection Act (introduced December 2024 by Reps. Raskin and Kiley) remains in committee. *Source: Public Participation Project — https://anti-slapp.org/your-states-free-speech-protection*

**Required communications architecture for any active organizing campaign**:

| Communication type | Required tool | Prohibited tools |
|---|---|---|
| Organizer-to-organizer strategy | Signal (disappearing messages enabled) | Email, SMS, Slack, Teams, Facebook Messenger |
| Organizer-to-member broad messaging | Signal broadcast list or union-managed Proton account | Company email, Facebook groups with employer members |
| Public campaign communications | Dedicated social media account (Proton-registered, not personal) | Personal social media accounts with real name |
| Internal documents (contracts, member lists, financial records) | Proton Drive or encrypted local storage | Google Drive, Dropbox, OneDrive, iCloud |
| Legal communications with union counsel | Signal or ProtonMail only | Any employer-adjacent platform |

### 1.2 Meeting Security

**Physical meeting security for organizing committee sessions**:

- Do not hold organizing committee meetings in employer-owned facilities or common areas where employer-installed cameras may be present.
- For sensitive planning meetings: conduct in private homes or union halls that you control. Assume any commercial meeting space (hotel conference room, Airbnb) may have unknown audio surveillance capability.
- Phones in meetings: Have all attendees silence devices and leave them in another room or in a Faraday pouch (available for $20–40 — brands: Mission Darkness, Faraday Defense). Phones in active meetings are microphone risks regardless of whether any app has been deliberately installed for surveillance.
- For meeting notes: one designated note-taker records on paper. After the meeting, notes are photographed and stored in Proton Drive. Paper is destroyed. No meeting notes in Google Docs.

**Virtual meeting security**:

- Use Signal for voice or video calls among core organizing committee (up to 40 participants).
- For larger membership meetings: Jitsi Meet (self-hosted or via meet.jit.si) over Signal for meeting coordination. Zoom, Teams, and Google Meet transmit meeting content through U.S.-based servers subject to subpoena.
- Do not record virtual organizing meetings. Meeting recordings are a subpoena target and create a verbatim discoverable record of everything said.

### 1.3 Media Security

Your organizing campaign will generate press interest at critical moments. A poorly managed media interaction can reveal member identities, internal strategy, or financial information that employer attorneys will use in litigation.

**Media security protocol**:

- Designate a single media spokesperson per campaign. All other organizers decline to comment and direct to the spokesperson.
- The spokesperson communicates with journalists via Signal only — not via email or phone that generates carrier records.
- Before any press release or public statement is issued, it is reviewed by union counsel (this takes 24 hours — plan accordingly for breaking events).
- Member identities are never disclosed to press without explicit written consent from the member.

---

## Part 2: Contractual Leverage Points — Cybersecurity in Collective Bargaining

### 2.1 Employer Device Ownership and Monitoring Clauses

When negotiating contracts, the digital surveillance provisions are often overlooked but have significant long-term implications for organizing and member rights.

**Provisions to seek in all new contracts**:

1. **Device ownership clarity**: The contract should specify that employer-issued devices may not be used for organizing activity (protecting the employer's legitimate interest) AND that personal devices may not be subject to employer monitoring or search. This creates a clean separation that protects members' personal phone privacy.

2. **Electronic monitoring notice requirements**: At least 14 states (including New York — ESPA 2022, Connecticut — PA 22-15, and Delaware) require employers to provide written notice before monitoring employee electronic activity. If your state has such a requirement, the contract should specify the notice language and channel.

3. **Remote work cybersecurity**: Remote work agreements should specify what VPN and monitoring tools the employer may deploy on work devices for network security — and explicitly exclude personal devices and personal networks. Employer-supplied VPNs on work devices are a common surveillance vector; the contract should define the scope.

4. **Cyber insurance and data breach obligations**: The contract should require the employer to maintain cyber liability insurance covering member data (Social Security numbers, financial information, health data) and to notify the union of any data breach affecting member data within 72 hours.

### 2.2 Negotiating Cybersecurity Agreements as Part of a First Contract

For campaigns still working toward a first contract, cybersecurity provisions can be a leverage point that employers often concede readily because they want compliance, not just the appearance of security. Frame it as: "We're asking for what your insurer already requires."

---

## Part 3: Strike Preparation Security — Three-Level Escalation Protocol

### Level 1: Low-Intensity Union Operations (Standard Organizing Campaign)

At this level, the primary threats are employer monitoring of company systems and passive social media surveillance. The security posture is compartmentalization without significant operational friction.

**Level 1 checklist** (30-minute setup for each new organizing committee member):

- [ ] Install Signal on personal phone (not employer-issued device)
- [ ] Enable disappearing messages (1 week for all organizing conversations)
- [ ] Enable Signal Lock (Settings → Privacy → Screen Lock → require fingerprint/PIN to open Signal)
- [ ] Create a ProtonMail account with a username that does not include real name (use for internal organizing email only)
- [ ] Review personal social media: remove employer from follower/following lists on personal accounts; set to maximum privacy; do not post about organizing campaign from personal accounts
- [ ] Delete social media apps from employer-issued device if present

**Time to deploy**: 30 minutes per person. Can be done during a lunch break.

### Level 2: High-Risk Campaign (Employer Has Legal Team Active, NLRB Charges Filed, or SLAPP Litigation Initiated)

At this level, employer attorneys are seeking discovery of organizer communications. The threat has escalated from surveillance to litigation. The security posture must harden accordingly.

**Level 2 additions**:

- [ ] All organizing committee meeting notes moved to encrypted storage immediately (paper notes photographed, stored in Proton Drive, originals destroyed)
- [ ] Union counsel reviews all external communications before release
- [ ] Member contact list moved from Google Sheets/Excel to encrypted local storage or Proton Drive — not synced to any cloud service accessible by U.S. subpoena
- [ ] Personal phone location tracking reviewed: Settings → Privacy → Location Services — review all apps with "Always" location access and revoke for all non-essential apps
- [ ] Delete advertising ID: Android → Settings → Privacy → Ads → Delete Advertising ID; iPhone → Settings → Privacy & Security → Tracking → Allow Apps to Request to Track (off)
- [ ] Anti-SLAPP research: identify your state's anti-SLAPP law and confirm with union counsel whether it applies to the specific claims being threatened. Public Participation Project — https://anti-slapp.org/your-states-free-speech-protection

**SLAPP defense playbook (if employer files suit)**:

1. Immediately retain or consult union counsel with anti-SLAPP experience.
2. File an anti-SLAPP special motion to strike within the statutory deadline (varies by state — as short as 60 days in California).
3. Preserve all organizing communications under litigation hold (do not delete, do not disable disappearing messages for existing conversations — pause disappearing messages for the duration of litigation).
4. Counter-sue for attorney fees if your state's anti-SLAPP law provides fee-shifting (California, New York, Washington, Texas all do).
5. Contact the Reporters Committee anti-SLAPP legal guide for attorney referrals — https://www.rcfp.org/anti-slapp-legal-guide/

### Level 3: Strike Execution (Active Work Stoppage)

Strike conditions create the highest-intensity threat environment for labor organizers: employer PI surveillance of picket lines, potential police or DHS surveillance, and legal exposure for organizers who cross lines between protected concerted activity and unprotected conduct.

**Level 3 additions (implement 72 hours before strike authorization)**:

- [ ] Establish a dedicated strike communications channel: Signal group with all picket captains, strike coordinator, and union counsel. No new members added after strike begins without verbal verification from a known member.
- [ ] Vehicle protocol: assume Flock Safety ALPR is active at or near picket sites. If your license plate appearing at multiple picket locations in multiple jurisdictions creates legal exposure (e.g., in jurisdictions where court injunctions limit picket participation), use alternate transportation or park away from the picket site.
- [ ] Drone awareness: LAPD used Skydio X10 drones (capable of facial recognition from 2,500 feet) 31+ times at a single protest in January 2026. During high-visibility strikes, assume aerial surveillance is active. Face coverings (masks, hats with brims) meaningfully limit facial recognition accuracy from aerial platforms.
- [ ] Signal broadcast list for member updates during strike: updates go to a strike coordinator, who sends to the broadcast list. Broadcast lists in Signal are one-way — recipients cannot see each other's contact information.
- [ ] All organizing and financial records backed up to encrypted offline storage before strike begins. During a strike, employer may attempt emergency injunctions that include asset discovery; all sensitive documents should be off any cloud server.

**Digital organizing tools for strike action**:

- Strike pledges and member lists: encrypted Google Form (with Workspace account configured to limit data sharing) OR Proton Forms. Never use a personal Google account for member data.
- Real-time strike coordination: Signal group (up to 1,000 members in Signal groups as of 2025) for picket captains; Signal broadcast for broader member updates.
- Media: Pixelfed (open-source Instagram alternative, self-hosted) for picket line photos — avoids Facebook/Instagram metadata and advertising SDK tracking. If using mainstream social media, post only after stripping photo metadata (iOS 15+ automatically strips location from shared photos if Privacy settings are correct; Android requires manual verification).

---

## Part 4: Member Training — Rapid Deployment at Scale

### 4.1 One-Hour Member Security Briefing

Designed to deploy to an entire local union membership at a single meeting or across multiple shop-floor sessions.

**Format**: 30 min presentation + 30 min hands-on

**Presentation talking points (non-technical language)**:

"Your employer can see everything you do on your work computer, your work email, and your work phone. That includes anything about the union. To keep our organizing safe, we use Signal — a messaging app that keeps our conversations private, even from our employer.

Social media is the second thing. When you post about organizing or about our campaign on your personal Facebook or Instagram, your employer's lawyers may screenshot it and use it in court. Our rule is: nothing about the union on your personal social media until we give the all-clear.

The third thing is your phone's location. Apps on your phone track where you go and sell that information. We're going to show you how to stop that right now — it takes two minutes."

**Hands-on (30 minutes)**:

- 10 min: Group Signal install. Trainer walks everyone through installation. Goal: every person in the room has Signal on their phone before they leave.
- 10 min: Location tracking opt-out. Trainer walks through iOS and Android location and ad tracking settings step by step on a projected screen.
- 10 min: Social media privacy check. Trainer walks through setting personal accounts to private and reviewing recent posts for organizing content.

### 4.2 Train-the-Trainer Model for Union-Wide Deployment

**Goal**: 20 unions can deploy this to their membership within one week of receiving this guide.

**Required per local**:

- 1 designated security coordinator (can be shop steward, communications chair, or any digitally-comfortable member)
- 2 hours training for the security coordinator (this guide + one walkthrough call with district staff)
- Member briefing materials: printed one-page handout (below) + QR code to Signal install

**One-page member handout template** (print and distribute at membership meeting):

```
PROTECT OUR UNION — THREE STEPS

1. INSTALL SIGNAL
   Download: signal.org/install
   We use Signal for union business because
   your employer cannot read it.

2. CHECK YOUR PHONE'S LOCATION
   iPhone: Settings → Privacy & Security →
   Location Services → set Social Media apps to NEVER
   Android: Settings → Privacy → Location → set
   Social Media apps to DENY

3. KEEP UNION TALK OFF PERSONAL SOCIAL MEDIA
   Nothing about our campaign on Facebook,
   Instagram, or TikTok until the union says it's safe.

Questions? Contact [Security Coordinator Name] via Signal.
```

**Success metrics for union deployment**:

- [ ] 80%+ of organizing committee has Signal installed and using it for internal communications (7 days post-training)
- [ ] Member contact list moved off Google Sheets and into encrypted storage (30 days)
- [ ] Anti-SLAPP legal consultation completed with union counsel (if in a high-risk campaign)
- [ ] Security coordinator trained and documented (so knowledge transfers if they leave the role)

---

## Part 5: Tool Recommendations and Trade-offs

| Tool | Cost | Setup Time | Best For | Limitation |
|---|---|---|---|---|
| Signal | Free | 5 min | All internal organizing communications | Requires smartphone; friction for older members |
| ProtonMail | Free / $3.99/mo | 10 min | Organizing email that may be subpoenaed | Only fully E2E between Proton users |
| Proton Drive | Included / $3.99/mo | 15 min | Member lists, contract drafts, strike documents | Swiss jurisdiction — significant but not absolute barrier to U.S. process |
| Jitsi Meet | Free | 5 min | Virtual membership meetings | No central server for data retention, but call metadata may persist at ISP level |
| Faraday pouch | $20–40 one-time | 0 min | Blocking phone location at sensitive meetings | Inconvenient; must educate members on use |
| Pixelfed | Free (self-hosted) | 2 hours for setup | Strike photos without Facebook surveillance | Requires technical administrator; lower reach than Instagram |

---

## Sources

1. EFF, "Labor Unions, EFF Sue Trump Administration to Stop Ideological Surveillance of Free Speech Online" — https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online
2. Prism Reports, "DHS is Buying Access to Real-Time Location Data — Penlink PLX" (April 29, 2026) — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/
3. Public Participation Project, "State Anti-SLAPP Laws" — https://anti-slapp.org/your-states-free-speech-protection
4. Institute for Free Speech, "Anti-SLAPP Statutes: 2025 Report Card" — https://www.ifs.org/anti-slapp-report/
5. Reporters Committee, "Anti-SLAPP Legal Guide" — https://www.rcfp.org/anti-slapp-legal-guide/
6. EFF, "How Cops Are Using Flock Safety to Surveil Protesters and Activists" (November 2025) — https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/
7. EFF, "Operations Security (OPSEC) Trainings: 2025 in Review" (December 2025) — https://www.eff.org/deeplinks/2025/12/operations-security-opsec-trainings-2025-review
8. Cybersecurity Best Practices for Unions — Union.dev — https://union.dev/blog/articleid/45/union.dev/cybersecurity-best-practices
9. Cybersecurity Best Practices for Anti-SLAPP Lawyers — PATFox/Blueprint for Free Speech — https://www.antislapp.eu/curriculum-hub/cybersecurity-best-practices-for-anti-slapp-lawyers
10. EFF Surveillance Self-Defense — https://ssd.eff.org/
11. Amnesty International, "Caught in the Net" (Babel Street investigation) — https://www.amnesty.org/en/documents/amr51/7101/2023/en/
12. RBT CPAs, "Union Strong, Cyber Smart: The Importance of Cybersecurity Plans for Unions" — https://www.rbtcpas.com/thought-leadership-articles/unions/union-strong-cyber-smart-the-importance-of-cybersecurity-plans-for-unions/
