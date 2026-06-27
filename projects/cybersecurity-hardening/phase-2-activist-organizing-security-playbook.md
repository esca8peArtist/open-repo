---
title: "Activist Organizing + Protest Security Playbook: Counter-Surveillance for Organizers and Protest Participants"
project: cybersecurity-hardening
created: 2026-05-07
last_updated: 2026-06-06
status: production-ready
phase: Phase 2
session: 875
version: 1.1
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
  - activist-organizing-playbook.md
  - THREAT_ENVIRONMENT_Q2_2026_UPDATE.md
  - PHASE_2_THREAT_INTEGRATION_CHECKLIST.md
confidence: high — grounded in documented government capabilities (Babel Street DHS contracts, LAPD drone flight records via The Intercept/DroneXL, Flock Safety EFF investigation, Mobile Fortify Minneapolis and Maine deployments, DHS administrative subpoenas to Google/Meta/Reddit/Discord, Palantir AIP social graph, Bi2 iris scanning contract June 2026, Clearview AI FBI protest use Biometric Update February 2026, DOGE SSA voter roll coordination Democracy Forward court filings, Thomson Reuters LEIDS-5 expiration LawNext), court filings, and EFF/Amnesty International primary source reporting; updated June 6, 2026 with five Q2 2026 patches
audience: Protest organizers, labor unions, activist networks, civil rights coalitions, legal observers, communications coordinators
word_count: ~4,400
changelog: v1.1 — Q2 2026 threat integration (5 patches): UPDATE-ACT-01 FBI + Clearview AI confirmed at protests, two class actions documented (Section 1.4 expansion); UPDATE-ACT-02 DHS admin subpoenas — four-hour timeline, Columbia University case, partial platform compliance (Section 1.5 expansion); UPDATE-ACT-03 DOGE SSA data as organizational threat (new Section 1.6); UPDATE-ACT-04 iris scanning at enforcement events (Section 1.4 addition); UPDATE-ACT-05 gait recognition future trajectory note (Section 1.2 footnote); plus Thomson Reuters LEIDS-5 expiration note (Section 1.1)
---

# Activist Organizing + Protest Security Playbook

**For organizers and legal advocates**: This guide maps the specific surveillance stack deployed against protest participants and political activists in the United States as of May 2026, and provides actionable countermeasures organized by role and implementation priority. The threat model is documented and operational.

Key facts that distinguish this guide from generic security advice: LAPD deployed drones 32 times over the March 28 No Kings protest and 31 times over the January 31 anti-ICE downtown Los Angeles protest; Flock Safety ALPR data was queried by 50+ agencies in connection with the 50501, Hands Off, and No Kings protests; DHS sent hundreds of administrative subpoenas to Google, Meta, Reddit, and Discord to unmask anonymous anti-ICE accounts, with Reddit, Meta, and Google voluntarily complying with some requests; ICE agents photographed protesters with Mobile Fortify in Minneapolis; and Portland residents lawfully observing an enforcement operation were biometrically scanned and threatened with placement on a domestic terrorism watchlist.

These are not emerging capabilities. They are in active deployment, with flight records, court filings, and investigative journalism to document each claim.

**Version 1.1 — Q2 2026 patch integration (June 6, 2026, updated June 27, 2026)**: Five critical threat updates have been applied to this version: (1) FBI agents confirmed using both Mobile Fortify and Clearview AI simultaneously at Minneapolis protests — two federal class action lawsuits (Hilton v. Noem, Tincher v. Noem) document FBI placing protest observers in domestic terrorism investigative databases (Section 1.4); (2) DHS administrative subpoenas issued in near-real-time against critics — four hours after a Philadelphia man emailed a DHS official, a subpoena went to Google; Columbia University targeted to identify a student protester (Section 1.5); (3) DOGE's unlawful access to Social Security Administration data — including staff wage histories — creates a new structural threat to activist organizations whose staff appear in federal benefit databases (Section 1.6); (4) ICE deployed iris scanning nationally June 1, 2026 via $25.1M Bi2 contract covering 1,570+ scanners — a second biometric step for protest observers and enforcement monitors who may be approached by agents (Section 1.4); (5) Thomson Reuters LEIDS-5 contract expired May 31, 2026; separate DHS contract renewed March 31, 2026 through 2029 — data broker opt-outs remain essential (Section 1.1 note). **Chatrie v. United States geofence warrant footnote and Flock Safety litigation update added June 27, 2026 (Sections 4.3 and 1.3).**

This playbook is a companion to `activist-organizing-playbook.md` (the full-length companion document), `threat-model.md`, and `opsec-playbook.md`. Cross-references are provided throughout.

---

## Section 1: Threat Model — The Five-Layer Surveillance Stack Against Activists

Defeating one layer while ignoring others provides false security. These five layers compound each other in documented enforcement actions.

### 1.1 Layer 1: Social Media OSINT — Babel Street Persistent Monitoring

**What it does**: Babel Street is a commercial OSINT platform with confirmed DHS, ICE, CBP, and State Department contracts. Its "persistent search" feature continuously monitors public content matching flagged individuals, keywords, or geographies — without a new query being initiated each time. The system automates surveillance at scale.

Amnesty International's 2025 investigation documented Babel Street being used against pro-Palestine student protesters, with DHS using keyword searches to identify "radicalized groups" and flag individuals for visa revocation, detention, and deportation. The "Catch and Revoke" initiative — operated by State Department in coordination with DHS and DOJ — uses AI to review social media for protest-related content by visa holders and revokes visas accordingly. As of 2026, Babel Street feeds directly into this pipeline.

**What this means for you**: Any public social media content — posts, profile photos, tagged locations, comments on protest-related pages — is continuously monitored once you are flagged. Content posted in the period before, during, and after a public action is the highest-risk window. Retrospective searches can also surface content posted months earlier.

*(June 2026 update — Thomson Reuters LEIDS-5 context for organizers: The LEIDS-5 contract between Thomson Reuters CLEAR and ICE expired May 31, 2026. As of June 6, no confirmed renewal has been announced for the ICE-specific vehicle; a separate DHS contract was renewed March 31, 2026, running through 2029. More than 200 Thomson Reuters employees signed a letter demanding non-renewal and a union shareholder campaign preceded the June 10, 2026 shareholder vote. ICE-Thomson Reuters relationships span multiple contract vehicles estimated at ~$60M, and Babel Street independently aggregates commercial records. CLEAR opt-out remains a recommended action for core organizers — LexisNexis Accurint opt-out and Thomson Reuters CLEAR opt-out reduce the commercial-data inputs to identity resolution regardless of which specific contract vehicle ICE uses.)*

**Countermeasure**: Section 3 — 72-hour pre-action social media protocol.

### 1.2 Layer 2: Aerial Surveillance — Drone Deployment at Protests

**Documented scale**: LAPD deployed Skydio X10 drones 31 times over a single anti-ICE protest in downtown Los Angeles on January 31, 2026, and 32 times over the March 28 No Kings protest, with drones lingering for up to seven hours over key protest sites. NYPD conducted 6,546 drone flights in the first half of 2025, a 3,200% increase since 2022. CBP flew a military-grade MQ-9 Predator drone over Los Angeles protests.

**Technical capability**: The Skydio X10 detects individuals from 8,000 feet, identifies people from 2,500 feet, and reads license plates from 800 feet. At operational altitude, face identification is possible even with ground-level masks when the subject looks up or when overhead angle exposure occurs.

**The key implication for countermeasures**: Ground-level masks defeat ground-level camera angles. They are much less effective against aerial surveillance at moderate altitude, which sees the top of a hat, not a face — but switches to clothing signature and movement pattern tracking to maintain individual continuity through a crowd.

*(Future trajectory note: LiDAR-based gait recognition — which can identify individuals by walking pattern regardless of facial covering or clothing — is in early domestic deployment at border installations. Not currently deployed at US protest sites. This technology, combined with aerial LiDAR drones, would defeat the clothing-based masking countermeasures in Section 4.2. Monitor for deployment announcements; current countermeasures remain adequate for 2026.)*

**Countermeasure**: Section 4.2 — clothing protocol for aerial surveillance.

### 1.3 Layer 3: Vehicle Tracking — Flock Safety ALPR

**Documented enforcement**: EFF's November 2025 investigation documented 50+ federal, state, and local agencies running hundreds of Flock Safety ALPR searches against protest-correlated plates across the 50501 protests (February), Hands Off (April), and No Kings (June and October 2025). Flock was simultaneously developing "Nova," which supplements ALPR data with commercial databases and breach data to track individuals without a warrant. *(June 27, 2026 update — Flock Safety litigation: A class action complaint (Gibbs Mura, filed April 3, 2026) alleges California privacy law violations and illegal sharing of ALPR data with out-of-state agencies. Washington State passed SB 6002 (March 30, 2026) restricting ALPR data access. These legal developments strengthen the threat framing but do not change countermeasures.)*

**The structural problem**: ALPR data is permanent and queryable. If your plate appears at protest sites across multiple events, that correlation is stored indefinitely and can be used to establish your presence at those events regardless of other countermeasures. Pattern correlation across events — not just single-event detection — is how protest activity mapping works in practice.

**Countermeasure**: Section 5 — vehicle de-correlation protocol.

### 1.4 Layer 4: Field Biometric Identification — Mobile Fortify at Protest Perimeters

**Documented use at protests**: ICE agents photographed protesters at protests in Minneapolis using Mobile Fortify (documented February 2026). In Portland, Maine, residents Colleen Fagan and Elinor Hilton were biometrically scanned while lawfully observing an immigration enforcement operation. An agent told Fagan: "Cause we have a nice little database." Another told Hilton she would be on a "domestic terrorist watchlist" if she kept attending such events. Both were US citizens. A class action challenging DHS's use of facial recognition against protesters was filed in federal court in February 2026.

**Activist-specific risk**: Even US citizens with no immigration vulnerability can be enrolled in a protest-related biometric database. ICE and FBI agents have described using facial recognition data from protests to add individuals to "domestic terrorist" databases, directly chilling First Amendment activity.

*(June 2026 update — FBI + Clearview AI at protests: ICE agents at Minneapolis protests are confirmed using at least two facial recognition systems simultaneously: Mobile Fortify (NEC engine against DHS HART database, 150M+ records) and Clearview AI (50B+ images scraped from the internet). FBI agents are independently using facial recognition at protests to add individuals to federal investigative databases. FBI database placement is not immigration enforcement — it creates federal criminal investigation exposure under a different legal basis with different downstream consequences. Two federal class action lawsuits document a pattern across multiple states: Hilton v. Noem (Maine) and Tincher v. Noem (Minnesota), both filed February 2026, document agents scanning observers' faces, photographing license plates, following people home, and informing them they are in "domestic terrorist databases." DHS officially denies the existence of a domestic terrorist database. Clearview's database is particularly relevant here because it contains protest photos, news photos, and any public image ever posted online — unlike the HART database, it does not require a prior arrest or government enrollment. Any public photo of you at any prior protest may be in Clearview's database.)*

*(June 2026 update — Iris scanning added to field toolkit: ICE deployed iris scanning capability nationally on June 1, 2026 via a $25.1M Bi2 Technologies contract covering 1,570+ handheld scanners. The scanners access a 5M+ record database from booking, arrest, and incarceration records across 47 states. For protest observers and enforcement monitors who may be physically approached by ICE agents, iris scanning is a second biometric identification step beyond photography. Iris scanning requires close physical contact, unlike Mobile Fortify photography. If approached by ICE agents, assert your right not to submit to biometric collection outside a formal arrest processing context and request attorney presence immediately. The legal status of compelled iris scanning in non-arrest encounters is unsettled — do not consent.)*

**Countermeasure**: Section 4.1 — physical countermeasures and Section 6 — legal response if approached.

### 1.5 Layer 5: Account Unmasking — DHS Administrative Subpoenas

**Documented enforcement**: DHS sent hundreds of administrative subpoenas to Google, Meta, Reddit, and Discord between late 2025 and early 2026 seeking to unmask the identities behind anonymous accounts that criticized ICE or posted ICE agent location alerts. Reddit, Meta, and Google voluntarily complied with some requests. DHS withdrew some subpoenas when challenged by ACLU attorneys in California and Pennsylvania rather than wait for a ruling. A lawsuit challenging the subpoenas (DHS, ICE sued over immigration subpoenas) was filed in April 2026.

**The critical point**: Administrative subpoenas require no judicial authorization before issuance. They are DHS's own instrument. If your account has ever been linked to your real identity through any data point — registration email, phone verification, IP address, payment method — DHS can reach that link.

*(June 2026 update — scale, timeline, and new cases: The scale of DHS administrative subpoenas has grown to hundreds of known instances. Google, Meta, and Reddit partially complied before legal challenges were mounted. Three documented cases expand the activist threat picture beyond anti-ICE social media accounts: (1) Jon Doe case — a Philadelphia-area man sent a single email to a DHS official criticizing DHS treatment of an asylum seeker; four hours later, DHS issued an administrative subpoena to Google seeking his identity and home address. About two weeks after Google notified him, two DHS agents and a local police officer appeared at his home. The ACLU moved to quash; DHS withdrew the subpoena before a ruling — but only because the man was notified in time and had legal support within the challenge window. (2) Columbia University was targeted with process seeking data on a student protester. (3) The Montco Community Watch case (Section 11) established that Meta notification may provide a 10–14 day challenge window — but that window requires legal representation to be useful. The practical implication: anonymous infrastructure must be established before any sensitive communication occurs. There is no retroactive anonymity. If your account already uses a real email, phone number, or payment method linked to your identity, a successful subpoena returns your identity before any legal challenge is possible.)*

**Countermeasure**: Section 3.3 — account architecture separation.

### 1.6 DOGE — Federal Data as Organizational Threat

**What happened**: In January–March 2026, court filings in the Democracy Forward lawsuit (AFSCME, AFT, and Alliance for Retired Americans v. DOGE) revealed that DOGE employees at the Social Security Administration improperly accessed records for 300M+ Americans — including immigration status, wage histories, bank account numbers, and home addresses. Court filings further revealed that a DOGE team member signed a "Voter Data Agreement" with an outside political advocacy group and sent the executed agreement to that group, coordinating to match federal benefit data against state voter rolls to "find evidence of voter fraud and to overturn election results in certain States." The SSA referred the DOGE employees for Hatch Act violations.

**Why this matters for activist organizations specifically**: This is the first documented case of federal benefit database access being coordinated with outside political organizations against named political adversaries. If your organization has any staff receiving government benefits (ACA/Medicaid enrollment, SSA wage reporting, any federal program), your organization's staff may appear as nodes in DOGE-accessible datasets. The same entity-resolution infrastructure documented in the Palantir threat model has a parallel in DOGE's access to SSA — wage histories, employer names, and home addresses are available across the SSA dataset.

**What you cannot change**: This data cannot be removed from SSA records. Staff cannot be removed from SSA wage history. This is a structural data exposure.

**What you can do**: (1) Financial separation — maintain clear separation between organizational financial identity and personal financial identity for all staff with organizational roles; (2) Minimize what commercial data brokers contribute on top of SSA exposure — data broker opt-outs reduce the ability to enrich SSA records with additional commercial data; (3) If your organization is a named political adversary of the current administration, consult with a privacy attorney about organizational exposure assessment. This threat does not have an operational countermeasure — it has a legal and structural response.

---

## Section 2: Who Is Surveilling, and What Is at Stake — Threat Actors by Role

Different participants face different primary threats. This section maps threat actors to participant types.

| Participant Type | Primary Threat Actors | Primary Threat | Highest-Impact Countermeasure |
|---|---|---|---|
| Frontline protest participant | LAPD/NYPD drones, Flock ALPR, Mobile Fortify | Biometric enrollment, vehicle tracking | Mask + hat + sunglasses, phone off, no personal vehicle |
| Lead organizer / event coordinator | Babel Street, DHS subpoenas to platforms, Palantir AIP | Long-term investigation, account unmasking | Account separation, 72-hour pre-action protocol, GrapheneOS |
| Visa holder / international student | Catch and Revoke pipeline, Babel Street | Visa revocation for public protest content | All social media private; no public protest-related posts |
| Legal observer | Drone + perimeter surveillance, device seizure | Identification in aerial database, documentary evidence seized | Tier 2 physical measures, upload documentation before returning home |
| Communications coordinator | DHS subpoenas, Babel Street persistent monitoring | Account identity unmasking | Full account-device separation (see Section 3.3) |
| Organizational leadership | Palantir AIP social graph, DOGE/SSA federal data, RICO-adjacent legal theories | Network mapping, organizational investigation, structural staff data exposure | Tier 3 + legal consultation on organizational risk; Section 1.6 |

---

## Section 3: Social Media Hygiene and Account Architecture

### 3.1 The 72-Hour Pre-Action Protocol

**72 hours before any public action**:
1. Set all social media accounts to maximum privacy: Instagram/Facebook (Settings > Privacy > Account Privacy > Private), X/Twitter (Settings > Privacy and Safety > Protect posts), TikTok (Settings > Privacy > Private Account)
2. Review the last 30 days of posts. Archive or delete anything identifying regular locations, travel patterns, home neighborhood, vehicle, or event planning details
3. Disable location tagging globally on all platforms (do not leave it as a per-post setting)
4. Do not post event logistics in public-facing formats. Use closed Signal groups with disappearing messages for operational coordination

**During the action**: Do not post from the protest site with location services enabled. If you post at all, post after leaving the area. Disable camera location access before leaving home (iOS: Settings > Privacy > Location Services > Camera > Never; Android: Settings > Apps > Camera > Permissions > Location > Deny).

**After the action**: Wait 48 hours before posting any documentation from personal accounts. Organizational documentation accounts must be operated under full identity separation (Section 3.3).

### 3.2 The Catch and Revoke Risk — Specific to Visa Holders

The Catch and Revoke pipeline is documented and operational. If you hold any visa category — including F-1, J-1, H-1B, or any other — public social media posts about protest participation carry a direct revocation risk. The mechanism does not require you to have done anything illegal. Documented enforcement has targeted constitutionally protected speech.

**Action**: Consult with immigration counsel before making any public statement at a protest or posting protest-related content under your real identity or any account that could be linked to your real identity. This is not a theoretical risk.

### 3.3 Account Architecture: Three Separate Threat Surfaces

Your **personal account** (linked to your real identity), your **organizing coordination account** (used within your group for operational communications), and any **public-facing organizational account** are three different threat surfaces with three different countermeasures. The central failure mode is treating them as interchangeable.

**Personal account**: Apply the 72-hour pre-action protocol. Avoid any cross-posting between personal and organizing accounts — any cross-post is an entity-resolution anchor linking the two identities.

**Organizing coordination accounts** (Signal groups, closed Discord servers): Membership limited to vetted participants. New member vetting requires in-person vouching from a known participant; digital vouching alone is insufficient. Enable disappearing messages (24-hour default) in all groups. No operational logistics (times, routes, staging points) in any group that includes unvetted members.

**Public-facing organizational accounts**: Assume everything here is monitored by Babel Street. Ensure the operator of this account has full identity separation from the account: separate email registered through Tor or a VoIP service, separate device that has never been signed into personal accounts, separate VoIP phone number not linked to the operator's carrier account. This defeats passive OSINT correlation; it does not defeat a targeted DHS subpoena, but it substantially raises the bar.

*(June 2026 subpoena update: DHS administrative subpoenas have been issued in response to a single email to a DHS official, within four hours of the communication. There is no grace period to establish anonymity after a communication that draws DHS attention. Anonymous infrastructure — separate email, VoIP phone number, dedicated device, VPN session — must be in place before any communication that could draw scrutiny. If your public-facing account already uses a Gmail address, a real phone number for verification, or has ever been accessed without a VPN from a device linked to your identity, a successful subpoena returns your real identity regardless of what you do afterward. The countermeasure is architectural: establish separation before the account exists, not after it has been flagged.)*

---

## Section 4: Physical Countermeasures Against Facial Recognition and Drone Surveillance

### 4.1 Ground-Level Countermeasures — The Mask/Hat/Sunglasses Combination

The combination is what matters. Each element alone provides partial protection; together they reduce recognizable facial features to approximately 20%, dropping recognition accuracy from 99%+ to 40–60%.

- **N95 or FFP2 medical mask** (not cloth): Covers the lower 40% of facial landmarks. Cloth masks provide visual obstruction but are more permeable to infrared cameras in low-light or nighttime conditions.
- **Hat with a full brim**: Reduces overhead and oblique-angle acquisition from elevated cameras and moderate-altitude drones. A baseball cap works; a wide-brim hat is better.
- **Wraparound or large-frame sunglasses**: Defeats periorbital feature extraction and reduces iris recognition capability.

**Legal note**: Wearing masks at protests is legal in most US jurisdictions. Anti-mask laws historically applied to specific contexts (KKK activities); wearing an N95 for health or privacy reasons is generally protected expression. Verify your local jurisdiction before the action — your NLG chapter can advise.

### 4.2 Aerial Surveillance Countermeasures — Clothing Protocol

At drone operational altitude (2,500+ feet for Skydio X10), identification switches from facial feature matching to clothing signature and movement pattern tracking when masks are worn. The aerial system tracks individuals by continuing to follow their distinctive clothing after losing facial coverage.

**Generic outer clothing**: Wear dark or neutral tones (gray, black, navy, dark olive). No logos. No bright colors. No distinctive patterns. When a crowd of protesters wears generic dark clothing, aerial re-identification becomes computationally expensive.

**Clothing change protocol**: Change at least one major outer layer (jacket, top layer, hat color) before leaving the protest area. This breaks the visual continuity chain that aerial and perimeter CCTV systems use to track individuals from inside a crowd to individual vehicle or transit connections. The handoff moment — from protest crowd to transit or parking — is where individual tracking reconnects dispersed protesters to identity anchors. Breaking the clothing signature at that transition point degrades this handoff.

**Umbrellas**: An open umbrella directly defeats overhead drone camera acquisition for the individual below it. In wet-weather protests or protests where drone presence is confirmed (check ADS-B Exchange at adsbexchange.com on a separate device), umbrella protocols for key organizers provide meaningful protection.

**Check for drones before entering the protest area**: Use ADS-B Exchange (adsbexchange.com) to check active aircraft and drone flights in the area. LAPD and NYPD drones are registered and appear on ADS-B tracking. A confirmed drone presence means aerial countermeasures are not optional.

### 4.3 IMSI Catchers at Protests

IMSI catchers (Stingrays, cell-site simulators) are deployed by law enforcement to collect IMEI numbers and cell tower connection data from all phones in an area. They establish that your device was present at a specific location at a specific time, even if they cannot intercept encrypted communications.

**Note on Geofence Warrant Constitutionality** *(June 27, 2026)*: The Supreme Court heard oral arguments in *Chatrie v. United States* on April 27, 2026, regarding whether geofence warrants violate Fourth Amendment protections, with a ruling expected summer 2026. That case addresses law enforcement's ability to obtain location data from carriers (like Google) via geofence warrant. While the ruling may constrain law enforcement's acquisition of carrier-sourced location data, it does not directly affect IMSI catcher operations or law enforcement's use of mobile phone signals to establish device presence at specific locations via administrative means. IMSI catchers operate by passively intercepting device signals in real time; they are distinct from geofence warrants (which require historical location queries from carriers). Continue to treat IMSI catchers as an active threat regardless of the *Chatrie* outcome.

**The countermeasure**: Power off your phone before entering the protest perimeter. Airplane mode is insufficient — baseband firmware on most devices still responds to cell tower authentication requests while the OS shows airplane mode enabled. Full power-off eliminates this. Store the powered-off phone in a Faraday bag (Mission Darkness, Silent Pocket — $20–$80) for additional security against residual baseband activity.

If you need a phone during the action (emergency contact, legal observer documentation), use a **dedicated burner device** — a prepaid phone purchased with cash, with no connection to your identity — and keep your primary phone powered off and bagged.

---

## Section 5: Vehicle and Transit Security

### 5.1 First Choice — Transit or Walk

Transit leaves no vehicle record in ALPR data. If you take public transit and pay with cash (not a transit card linked to your identity), there is no vehicle-based location record for that event.

### 5.2 If You Must Drive

- **Use a vehicle not registered to you**: Carpool in a friend's vehicle (their plates are not yours). Or request a rideshare with pickup at least 4–6 blocks from your departure point and dropoff at least 4–6 blocks from the protest site. Your pickup and dropoff points are linked to your rideshare account — they are not in the immediate ALPR field of view near the protest perimeter.
- **If driving your own vehicle**: Park at least 4–6 blocks from the protest site perimeter. Flock cameras concentrate near anticipated entry points. Vary your arrival and departure times. Do not use the same parking block or structure you used at previous protests.
- **Know the Flock camera locations in your area**: DeFlock.me (deflock.me) is an EFF-supported map of known Flock Safety ALPR camera locations. Route your vehicle approach to avoid documented camera positions when possible.

### 5.3 Temporal De-Correlation

ALPR data, cell tower location data, and social media posts from the same time window at the same location are analyzed together. De-correlation means introducing randomness into your timing signature:

- Vary your arrival and departure times. A consistent timing pattern is a behavioral fingerprint.
- Keep your phone powered off during the time your vehicle is in the area. Your phone's cell tower check-ins create a timeline that corresponds to your ALPR record. Both data points pointing to the same location at the same time strengthens any subsequent inference.

---

## Section 6: Emergency Communication and Legal Support Infrastructure

**The single most underprepared element of activist security is legal support infrastructure**. It must be established before the action. Not during it. Not after it.

### 6.1 What Every Participant Needs Before Leaving Home

1. **The NLG hotline written on skin** — in permanent marker on your forearm or upper arm, not stored only in your phone. The National Lawyers Guild Mass Defense Hotline: **(212) 679-2811**. Local NLG chapter numbers are available at nlg.org/chapters/ and should be used where available. Writing the number on skin means you have it even if your phone is seized, dead, or destroyed.

2. **A designated outside contact** — a trusted person who is NOT at the action, who knows your plan, will receive a check-in, and knows to escalate to NLG legal support if the check-in is missed. Establish the check-in time before leaving home. ("I will message you by 4:00 PM. If I haven't by 4:30 PM, call [NLG number] and tell them my last known location was [location].")

3. **A pre-written legal statement** — a card in your wallet stating: "I am exercising my right to remain silent. I request an attorney immediately." You do not have to say anything else.

### 6.2 If You Are Detained or Arrested

**Do not consent to device search**: Say: "I do not consent to a search of my device." Law enforcement may claim your phone contains evidence. You are not required to consent without a warrant. Consent produces access immediately; a warrant requires judicial authorization.

**Do not identify other participants**: You are not required to name who organized the action, describe other protesters, or provide contact information. Say only your name (if legally required in your state to identify yourself) and: "I am exercising my right to remain silent."

**Document before powering off**: If you have photos or video documenting police misconduct, upload them to a secure storage service before powering off your phone. Once the device is powered off and in BFU (Before First Unlock) state, Cellebrite extraction is severely limited — see `implementation-guide.md` Part 4.

### 6.3 National Lawyers Guild Integration

The NLG is the primary legal support infrastructure for political activists in the United States.

- **National Mass Defense Hotline**: (212) 679-2811
- **Local chapters**: nlg.org/chapters/
- **Legal Observer request**: Contact your local chapter before any planned action to request trained legal observers. Legal observers wear distinctive green hats and are trained to document police-protester interactions without participating. They are not legal counsel — they document; they do not advise in the moment.
- **Mass defense fund**: For large-scale arrests, NLG coordinates mass defense with legal representation and bail support

Additional resources:
- **ACLU**: aclu.org — filed suits challenging DHS subpoenas targeting anti-ICE accounts
- **EFF protest guide**: eff.org/know-your-rights
- **National Police Accountability Project**: nlg-npap.org — for civil rights claims from protest-related police misconduct

---

## Section 7: Infiltration Detection and Network Vetting

### 7.1 Documented Risk

Infiltration of activist organizations by law enforcement informants is documented from COINTELPRO through the 2020s:
- FBI and local law enforcement placed informants in Black Lives Matter organizing groups in multiple cities in 2020–2021
- Undercover law enforcement attended organizing meetings during Standing Rock protests
- DHS has used paid informants in immigration-adjacent advocacy networks

The digital equivalent: an account that appears to be a known organizer but is actually managed by law enforcement.

### 7.2 Practical Vetting Framework

**Vouching chain**: New participants should be introduced by an existing, trusted participant who can vouch for them from direct personal knowledge. "I've worked with them at another organization for two years" is a different trust signal than "I met them at the last protest."

**Tiered access**: Not every participant needs access to the same information. A new participant at a public meeting does not need to be in the Signal group where operational logistics are discussed. Access to higher-trust channels follows demonstrated participation, not arrival.

**Behavioral signals to watch**: Informants and provocateurs tend toward: pressing for aggressive tactics the group has not decided on; seeking specific logistical information beyond what their role requires; disappearing from the group after getting information and reappearing before planned actions; expressing positions designed to increase conflict within the group. None are individually conclusive, but patterns matter.

**No entrapment**: If a new participant begins pushing toward illegal activity (property destruction, violence, weapons), that is a documented law enforcement informant tactic. Redirect firmly. If the behavior continues, escalate to organizational leadership.

### 7.3 Compartmentalized Communication Structure

- **Public channel** (social media, website, newsletter): Public-facing only. No operational logistics.
- **General participant channel** (closed Signal group, closed Discord): Coordination among confirmed, vetted participants. Disappearing messages enabled (24 hours).
- **Core organizer channel** (separate, very small Signal group): Operational logistics — timing, routes, legal support contacts, escalation decisions. Never grows by self-selection; only added by existing core members.
- **Emergency/legal channel**: A check-in mechanism for outside contacts, used only if participants go silent. May be as simple as a Signal group with the outside contacts and NLG chapter number pre-loaded.

---

## Section 8: Implementation Checklists

### Checklist A: 3 Days Before Action

**All participants**:
- [ ] Set all social media accounts to maximum privacy
- [ ] Review and archive last 30 days of posts with location or organizing content
- [ ] Disable location tagging globally on all platforms
- [ ] Disable camera location access on phone
- [ ] Write NLG hotline on arm (test the marker — it should stay on for 24+ hours)
- [ ] Designate outside contact; confirm check-in time and escalation protocol
- [ ] Read EFF protest rights guide: eff.org/know-your-rights

**Lead organizers (additional)**:
- [ ] Confirm legal observer request with local NLG chapter
- [ ] Verify that all Signal organizing groups have disappearing messages enabled (24 hours)
- [ ] Confirm bail fund contact and capacity for planned action
- [ ] Brief all confirmed participants on the check-in protocol

### Checklist B: Day-Of

**All participants**:
- [ ] Wear generic, non-distinctive outer clothing (dark/neutral, no logos)
- [ ] Bring N95/FFP2 mask, brimmed hat, and large-frame sunglasses
- [ ] NLG hotline confirmed to be on skin
- [ ] Outside contact has confirmed check-in time
- [ ] Phone powered off before entering protest perimeter; placed in Faraday bag if available
- [ ] No personal vehicle at protest site (transit, carpool, or rideshare 4–6 blocks away)
- [ ] Bring a change of outer layer (packable layer, hat swap)
- [ ] Change outer layer before leaving protest area

**Lead organizers (additional)**:
- [ ] Check ADS-B Exchange for active drone flights: adsbexchange.com
- [ ] Confirm burner device is charged and separate from primary phone
- [ ] Confirm core organizer Signal channel has disappearing messages on
- [ ] Conduct 5-minute legal brief for participants at start of action: right to remain silent, right to refuse consent to search, check-in protocol, NLG number

### Checklist C: Post-Action

**All participants**:
- [ ] Check in with outside contact immediately after leaving the area
- [ ] Power on primary phone only after departing the protest area
- [ ] Change outer layer before entering transit or parking area if not already done

**Lead organizers (additional)**:
- [ ] Confirm all participants have checked in; escalate any missed check-ins to NLG
- [ ] Upload any documentation (video, photos of police misconduct) to NLG secure storage before going home
- [ ] Wait 48 hours before posting any documentation from personal social media accounts
- [ ] If any arrests occurred: coordinate with NLG mass defense and bail fund immediately
- [ ] Conduct brief post-action debrief (within 48 hours): Did any surveillance indicators appear? Were any new participants behaving unusually? Does the threat level need to be upgraded?

### Checklist D: Ongoing Organizational Security

- [ ] Every 90 days: Re-submit LexisNexis data broker opt-outs for core organizers (or subscribe to Incogni for automation)
- [ ] Every 90 days: Submit Thomson Reuters CLEAR opt-out for core organizers: optout.thomsonreuters.com
- [ ] Monthly: Review privacy settings on all organizational accounts — platforms reset permissions after updates
- [ ] Before each action: Re-run the 72-hour pre-action protocol
- [ ] Quarterly: Review vetting process for new participants in core organizer channels
- [ ] Annually (or if your organization is named in political targeting): Consult with a privacy attorney regarding DOGE/SSA organizational staff data exposure — Section 1.6
- [ ] If any surveillance indicator escalates (DHS subpoena received, device seized, law enforcement contact): Activate Level 2 security posture and consult with legal counsel before the next action

---

## Section 9: Tier-by-Tier Implementation

### Tier 1: Essential (All Participants at Any Public Action — No Exceptions)

Time to implement: 2 hours. Cost: $0.

1. Write the NLG hotline on your arm before leaving home: (212) 679-2811 or local chapter number
2. Disable phone location services for all apps before leaving home
3. Set social media to private at least 72 hours before the action; archive recent location/organizing posts
4. Designate an outside contact with check-in time and escalation protocol
5. Read EFF's protest rights guide (eff.org/know-your-rights) — 5 minutes
6. Wear generic, non-distinctive outer clothing — dark/neutral, no logos. Change outer layer before leaving protest area.

### Tier 2: Intermediate (Regular Participants, Event Coordinators, Anyone with a Public Organizing Role)

All of Tier 1, plus:

7. Bring N95/FFP2 mask, brimmed hat, and wraparound sunglasses to every action. Wear them together — the combination is what matters.
8. Power off your phone before entering the protest perimeter; store in Faraday bag. Use a dedicated burner device ($25–$50 prepaid, cash-purchased) if you need a phone during the action.
9. No personal vehicle at protest sites. Use transit, carpool in someone else's vehicle, or rideshare with pickup/dropoff 4–6 blocks away.
10. Enable disappearing messages (24 hours) in all organizing Signal groups.
11. Complete LexisNexis Accurint opt-out: https://optout.lexisnexis.com/. California residents: complete DROP platform: https://privacy.ca.gov/drop/. Also submit Thomson Reuters CLEAR opt-out: optout.thomsonreuters.com (reduces commercial data available to multiple federal surveillance stacks regardless of which specific ICE contract vehicle is active).
12. Know your rights regarding biometric requests: If approached by ICE agents at or near enforcement operations, you have the right to decline iris scanning and biometric requests outside formal arrest processing. Say: "I do not consent to biometric collection. I am requesting an attorney." The legal status of compelled iris scanning in non-arrest encounters is unsettled — assert the right and document the interaction.

**Equipment cost**: N95 box ($15–$25), Faraday bag ($20–$80), prepaid burner phone ($25–$50). Total: under $150.

### Tier 3: Advanced (Lead Organizers, Public Profiles, Active Investigation Targets)

All of Tier 2, plus:

12. GrapheneOS on a dedicated protest device (grapheneos.org): auto-reboot set to 18 hours, strong passphrase, duress PIN configured. Details in `implementation-guide.md`.
13. Full account separation architecture for any public-facing organizational account: separate email (registered through Tor), separate VoIP phone number, separate device with no personal account history.
14. If you are a visa holder or DACA recipient: consult with immigration counsel before making any public statements at protests or posting protest-related content. Document Catch and Revoke risk is real.
15. Establish a documentation provenance practice for recorded public statements: keep original video files with timestamp metadata and share with legal contacts immediately after recording, as a defense against deepfake fabrication.
16. Subscribe to Incogni ($7.99/month) for automated quarterly data broker maintenance across 420+ brokers.
17. Legal consultation with a civil liberties attorney specifically regarding your organizational exposure — not just a Know Your Rights briefing.

---

## Section 10: Escalation Matrix

### Level 1: Baseline Organizing (No Specific Threat)

Standard organizing activities: meetings, public events, public social media presence, leafleting.

**Minimum measures**: Tier 1 (Sections 4.1, 5.1, 6.1 — NLG number, social media private 72 hours before, outside contact, generic clothing, know your rights). Signal for all organizing communications with disappearing messages.

**Indicators that move you to Level 2**: You learn you are the subject of a DHS administrative subpoena; law enforcement approaches you for questioning about organizing activity; you receive an FBI visit; your precheck status changes; you have reason to believe an informant is present in your organization.

### Level 2: Elevated Threat (Specific Indicators of Investigation)

All Tier 2 measures, plus: legal consultation with a civil liberties attorney; notification of your organization's legal support structure; implementation of the compartmentalized communication structure (Section 7.3); counter-surveillance protocols for meetings; review all accounts for exposure.

**Indicators that move you to Level 3**: You are detained and questioned; you are served with legal process; device is seized; you have direct evidence of an informant in your organization.

### Level 3: Active Investigation or Infiltration Confirmed

All Tier 3 measures, plus: all organizing communications move to GrapheneOS devices with full compartmentalization; leadership briefing on surveillance indicators and vetting protocols; legal counsel actively retained and briefed on current situation; assessment of whether reduced public visibility is warranted during the threat window.

**Note**: Level 3 does not mean stopping organizing activity. Many organizations have operated at Level 3 security posture for extended periods while remaining effective. It means adjusting the posture while continuing the work.

---

## Section 11: Case Studies

### Case Study 1: Maine ICE Observers (February 2026)

Portland, Maine residents Colleen Fagan and Elinor Hilton were lawfully observing and recording ICE enforcement operations in public spaces. ICE agents:
- Photographed and biometrically scanned both residents using Mobile Fortify
- Recorded their license plate numbers
- Told Fagan: "Cause we have a nice little database"
- Told Hilton she would be on a "domestic terrorist watchlist" and that agents "would come to your house later tonight"

Both were US citizens engaging in constitutionally protected activity. A lawsuit filed by Protect Democracy and Drummond Woodsum in February 2026 challenges this as unconstitutional retaliation. The case establishes that Mobile Fortify is not being used only against immigration targets — it is being used to surveil and intimidate anyone who observes enforcement operations.

**Lesson**: Physical biometric collection at enforcement events is not limited to undocumented individuals. Legal observers, citizen documentarians, and any bystander who approaches an enforcement operation should apply the Tier 2 physical countermeasures before approaching.

### Case Study 2: Montco Community Watch (Facebook/Instagram, early 2026)

"Montco Community Watch," a Facebook and Instagram page that posted bilingual alerts about ICE sightings in Montgomery County, Pennsylvania, was targeted by a DHS administrative subpoena to Meta seeking the identity of the account operator. Meta notified the account holders, who had a 10–14 day window to challenge. The ACLU filed to block the subpoena in federal court, arguing it targeted constitutionally protected speech. DHS withdrew the subpoena rather than wait for a ruling.

**Lesson**: The subpoena was withdrawn when challenged — but only because the account holders were notified in time and had legal support available within the challenge window. If Meta had not notified them, or if they had lacked legal support, DHS would have obtained their identity without any legal contest. The countermeasure is full account-device separation so that even a successful subpoena does not return the operator's real identity.

### Case Study 3: Philadelphia DHS Subpoena — Four-Hour Response Time (February 2026)

A Philadelphia-area man, identified in court filings as Jon Doe, read a Washington Post article about a DHS attorney's misleading arguments in an asylum case and sent a short email to that attorney's publicly available DHS email address, urging DHS to "apply principles of common sense and decency." Four hours after sending the email, DHS issued an administrative subpoena to Google seeking his identity, home address, and account records. About two weeks after Google notified him, two DHS agents and a local police officer appeared at his home to interrogate him about the email.

The ACLU moved to quash the subpoena in federal court; DHS withdrew it before a ruling. The case is documented in ACLU v. DHS (Doe v. DHS).

**Lesson**: DHS is monitoring incoming communications in near-real-time and subpoenaing platform records within hours of an interaction that draws attention. The subpoena tool is being used against protected speech by US citizens, not only against anonymous social media accounts. The critical point is that the man was notified by Google and had legal support available in time to challenge. If Google had complied without notification, or if the man had not contacted legal support within the challenge window, DHS would have obtained his identity without any legal contest.

### Case Study 4: Minneapolis Protest — Clearview AI + FBI Database (February 2026)

Photographs and video from Minneapolis protests in early 2026 show federal agents using facial recognition on phones while wearing tactical gear. The Biometric Update confirmed that ICE agents were using both Mobile Fortify and Clearview AI simultaneously. FBI agents were also present and using facial recognition to populate federal investigative databases.

Two class action lawsuits — Hilton v. Noem (filed February 2026, Maine) and Tincher v. Noem (filed February 2026, Minnesota) — document a pattern of agents scanning observers' faces without consent, photographing license plates, following protesters to their vehicles, and informing them they were being added to domestic terrorism databases. DHS officially denies the existence of a domestic terrorist database.

**Lesson**: The threat at protests is not a single tool operated by a single agency. Mobile Fortify (ICE ERO, HART database), Clearview AI (ICE HSI and FBI, 50B+ images), and IMSI catchers are being operated simultaneously by agents from different agencies with different investigative authorities. FBI database placement creates federal criminal investigation exposure that is categorically different from immigration enforcement consequences. The countermeasures in Section 4 address the biometric collection layer; the account architecture countermeasures in Section 3 address what happens after collection when agents attempt to resolve a face to an identity.

### Case Study 5: No Kings Protest Drone Surveillance (March 28, 2026)

LAPD flight data analyzed by The Intercept and DroneXL showed drones deployed 32 times over the March 28 No Kings protest, with some drones orbiting protest sites for up to seven hours. A heat map showed extended coverage over the Metropolitan Detention Center and Little Tokyo — areas with both political significance and high immigrant community presence. CBP separately flew a military-grade MQ-9 Predator drone over Los Angeles protests.

**Lesson**: Seven-hour drone coverage means the aerial surveillance window extends well before and after the protest's formal duration. Clothing change protocol should be applied not just during the protest but before departing the broader area. Checking ADS-B Exchange before approaching the protest area is meaningful — if drones are active before the crowd assembles, aerial surveillance began before you arrived. The Predator drone deployment by CBP adds a federal surveillance layer that operates at higher altitude and with longer endurance than LAPD's Skydio X10 drones.

---

## Section 12: Resource Directory

### Legal Support
- **National Lawyers Guild — Mass Defense Hotline**: (212) 679-2811 | nlg.org/massdefenseprogram/
- **NLG Legal Observer Program**: nlg.org/massdefenseprogram/los/
- **NLG Chapter Hotlines**: nlg.org/chapters/
- **ACLU Know Your Rights at Protests**: aclu.org/know-your-rights/protesters-rights
- **EFF Protest Guide**: eff.org/know-your-rights
- **National Police Accountability Project**: nlg-npap.org

### Bail Funds
- **National Bail Fund Network**: bailfundnetwork.org (directory of community bail funds by state)
- **AFL-CIO and affiliated unions**: labor union legal defense and bail support for labor-adjacent protest situations

### Security Tools
- **Signal**: signal.org (encrypted messaging — disappearing messages essential)
- **GrapheneOS**: grapheneos.org (hardened mobile OS)
- **Mullvad VPN**: mullvad.net (no-logs VPN)
- **Tor Browser**: torproject.org
- **Faraday bags**: Mission Darkness (mosequipment.com) or Silent Pocket (silentpocket.com) — $20–$80
- **Briar**: briarproject.org (Tor-routed mesh messenger, no phone number required)

### Surveillance Monitoring
- **ADS-B Exchange**: adsbexchange.com (track active drone and aircraft flights in real time)
- **DeFlock.me**: deflock.me (EFF-supported map of known Flock Safety ALPR camera locations)

---

## Summary: Five Things That Matter Most

If a participant will only do five things, these are the five:

1. **Write the NLG hotline on your arm** — not stored in a phone that can be seized: (212) 679-2811
2. **Wear generic dark clothing, mask, hat, and sunglasses** — the combination defeats both ground-level and moderate-altitude aerial identification
3. **Power off your phone before entering the protest perimeter** — defeats IMSI catchers and prevents Cellebrite extraction if seized
4. **Set all social media to private 72 hours before the action** — closes the Babel Street persistent monitoring window
5. **No personal vehicle at the protest site** — prevents permanent ALPR record linking your plate to protest activity across events

---

**For questions and updates**: Contact your local NLG chapter or EFF digital rights helpline (eff.org/help).

**Version**: 1.1 (Q2 2026 patch — June 6, 2026; Chatrie and Flock litigation updates — June 27, 2026)
**Created**: May 7, 2026
**Last updated**: June 27, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Patch log**: v1.1 applies five Q2 2026 updates (UPDATE-ACT-01 through UPDATE-ACT-05 per PHASE_2_THREAT_INTEGRATION_CHECKLIST.md) plus Thomson Reuters LEIDS-5 expiration note. Source count: 17 (original) + 9 (v1.1 additions) = 26 total.
**Cross-references**: `activist-organizing-playbook.md` (extended companion document), `threat-model.md`, `opsec-playbook.md`, `implementation-guide.md`, `palantir-threat-model.md`, `phase-2-immigration-surveillance-evasion-playbook.md` (device hardening Sections 5–6 apply directly), `PHASE_2_THREAT_INTEGRATION_CHECKLIST.md` (patch reference document)

**Sources** (17 original + 9 Q2 2026 patch additions = 26 total):

*Original sources (v1.0)*:
- [LAPD drone surveillance No Kings protest — The Intercept](https://theintercept.com/2026/04/20/lapd-skydio-drone-surveillance-no-kings-protest-ice/)
- [LAPD Skydio drones orbited No Kings for seven hours — DroneXL](https://dronexl.co/2026/04/28/lapd-skydio-drone-surveillance-no-kings-protest/)
- [EFF — Flock Safety ALPR protest surveillance investigation](https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/)
- [DHS administrative subpoenas — TechCrunch](https://techcrunch.com/2026/02/14/homeland-security-reportedly-sent-hundreds-of-subpoenas-seeking-to-unmask-anti-ice-accounts/)
- [Reddit, Meta, Google voluntarily complied with DHS subpoenas — Gizmodo](https://gizmodo.com/reddit-meta-and-google-voluntarily-gave-dhs-info-of-anti-ice-users-report-says-2000722279)
- [DHS lawsuit — biometrics, domestic terrorism threats against Maine observers — NPR](https://www.npr.org/2026/02/23/nx-s1-5722988/dhs-lawsuit-biometrics-domestic-terrorism)
- [Class action challenges DHS use of facial recognition at protests — Biometric Update](https://www.biometricupdate.com/202602/class-action-challenges-dhs-use-of-facial-recognition-against-protesters)
- [ICE surveillance web — NPR](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify)
- [Mobile Fortify — Wikipedia](https://en.wikipedia.org/wiki/Mobile_Fortify)
- [EFF — rights organizations demand halt to Mobile Fortify](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition)
- [Babel Street and Catch and Revoke — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-state-department-plans-to-use-ai-to-revoke-visas-of-students-engaged-in-pro-hamas-activity/)
- [ICE surveillance shopping spree — EFF](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
- [Penlink geofencing — 404media.co](https://www.404media.co/inside-ices-tool-to-monitor-phones-in-entire-neighborhoods/)
- [ICE wants to monitor social media critics — The Intercept](https://theintercept.com/2025/02/11/ice-immigration-social-media-surveillance/)
- [Facial recognition targets international student protesters](https://www.lawfirm4immigrants.com/facial-recognition-technology-targets-international-student-protesters/)
- [DHS, ICE sued over immigration subpoenas — Military.com](https://www.military.com/daily-news/2026/04/22/lawsuit-dhs-ice-sued-over-immigration-subpoenas-id-social-media-users.html)
- [DeFlock.me — EFF-supported Flock Safety camera map](https://deflock.me)

*Added in v1.1 patch (June 6, 2026)*:
- [ICE awards Bi2 $25M contract for 1,570 biometric scanners — The Register](https://www.theregister.com/public-sector/2026/05/29/ice-awards-bi2-25m-contract-for-1570-biometric-scanners/5248733)
- [ICE iris scanners expanding arsenal of tech tools — NPR](https://www.npr.org/2026/05/27/nx-s1-5822429/ice-buys-iris-scanners-tech-tools)
- [ICE, FBI expand facial recognition use to protest investigations — Biometric Update](https://www.biometricupdate.com/202602/ice-fbi-expand-facial-recognition-use-to-protest-investigations)
- [ICE contracts with Clearview AI — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-ice-contracts-with-clearview-ai-for-facial-recognition-technology/)
- [ACLU moves to quash DHS subpoena targeting Philadelphia critic — ACLU](https://www.aclu.org/press-releases/aclu-moves-to-quash-abusive-subpoena-aimed-at-tracking-down-man-who-criticized-department-of-homeland-security)
- [DHS withdraws subpoena targeting man who criticized them — ACLU](https://www.aclu.org/press-releases/department-of-homeland-security-withdraws-subpoena-targeting-man-who-criticized-them)
- [DOGE SSA data and voter roll coordination — Democracy Forward](https://democracyforward.org/work/legal/stopping-doges-unlawful-seizure-of-americans-social-security-data/)
- [Trump administration admits DOGE accessed sensitive personal data — NPR](https://www.npr.org/2026/01/23/nx-s1-5684185/doge-data-social-security-privacy)
- [Thomson Reuters LEIDS-5 contract and employee pressure — LawNext](https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-2-the-pushback-employees-shareholders-lawyers-and-the-fight-over-may-31.html)
