---
title: "High-Risk Population Protection Protocols: Dissidents, Activists, and Asylum Seekers"
project: cybersecurity-hardening
created: 2026-04-27
status: complete
depends_on: threat-model.md, palantir-threat-model.md, opsec-playbook.md, device-hardening-guide.md
confidence: high — grounded in documented case law, confirmed investigative methods, EFF/ACLU/NLG guidance, UNHCR frameworks, and public court records
audience: activists, dissidents, asylum seekers, journalists facing government-level targeting
---

# High-Risk Population Protection Protocols

**Purpose**: This document extends the core `device-hardening-guide.md` and `opsec-playbook.md` into advanced territory — comprehensive protection for people facing sustained, targeted government action. Where those documents address device security and communications defense, this document addresses identity architecture, physical security, legal coordination, international sanctuary, and emergency protocols.

**Who this is for**: People who face potential arrest, deportation, or political persecution — including US-based activists facing federal prosecution, international students targeted for speech activity, asylum seekers and undocumented people subject to ICE enforcement, journalists with national-security-adjacent sources, and dissidents from other countries who fear transnational repression.

**What this is not**: This is not legal advice and does not substitute for a real attorney. Every case is different. This document provides frameworks grounded in established legal and technical practice — not individual guidance for your specific situation.

---

## Decision Tree: When to Activate These Protocols

Activate protocols incrementally based on assessed threat level. Activating everything simultaneously when not warranted creates its own operational security problems (changes in behavior patterns are detectable).

**Tier A — Precautionary (activate now if any apply)**:
- You organize, advocate, or publish on topics currently under federal scrutiny (immigration rights, Palestinian solidarity, environmental direct action, labor organizing)
- You are a non-citizen residing in the US, regardless of status
- You have previously been detained, arrested, or placed on a watchlist
- You work at an organization that has received government legal process (subpoena, FISA request, NSL)

**Tier B — Elevated (activate within 48 hours if any apply)**:
- You have received a grand jury subpoena, target letter, or formal legal process
- A colleague in your network has been arrested and possessed your contact information
- You have received credible intelligence that you are under active investigation
- ICE or federal law enforcement has contacted people in your network asking about you

**Tier C — Emergency (activate immediately)**:
- You are being followed by unknown vehicles or individuals across multiple days
- You have reason to believe law enforcement has your physical address and is preparing to act
- You are an international student or visa holder whose visa status has been revoked without notice (see *Mahmoud Khalil* and *Rümeysa Öztürk* cases below)
- You are ready to depart the US and need pre-departure procedures

---

## Part 1: Identity Compartmentalization

### The Core Principle

The `palantir-threat-model.md` established that Palantir's Gotham and Foundry platforms do not "have" your data — they *link* data from dozens of previously siloed government and commercial databases into a unified identity graph. The defense is not finding a single database to hide from; it is denying the system the *cross-reference points* it needs to resolve pseudonymous identities back to your legal name.

From Palantir's own whitepaper: "partial information from anonymised data, linked with insights from other data sources, can be used to reverse engineer aspects of the anonymisation process." The identifiers Palantir uses for entity resolution include SSN, name, date of birth, address (current and historical), phone number, email, vehicle VIN, license plate, biometrics, immigration number, IP address, and associated persons. Compartmentalization works by ensuring that your anonymous identity never shares two of these anchors with your legal identity simultaneously.

### 1.1 Burner Phone Architecture

A burner phone is not inherently anonymous. Its value depends on strict operational separation from everything linked to your legal identity. Partial separation is often worse than none — it creates a false sense of protection while still generating linkable metadata.

**SIM architecture options**:

*Single-SIM burner (minimum viable)*: One prepaid device, one prepaid SIM, purchased with cash at a store you do not routinely visit. The purchase location matters: stores with loyalty card infrastructure, high-density urban locations with CCTV, and carriers that sell online with credit cards all leave records. Purchase from a small convenience store or gas station in cash. In the United States, SIM registration is not currently mandatory (unlike in many European and Asian countries), but carries and law enforcement can correlate purchase-time CCTV with the IMEI of the SIM that was activated.

*Dual-SIM device (advanced)*: A device capable of running two SIMs simultaneously. Used carefully, this allows the same hardware to operate under two distinct operational identities — but this architecture is only safe if you never activate both SIMs in the same physical location. If you do, a cell tower will see both IMSIs at the same tower and at the same time, which is a linkage Palantir-class systems can resolve. Dual-SIM architecture is primarily useful for travel contexts where you need a local SIM in addition to your operations SIM.

**Payment discipline**: The single fastest way to burn a burner identity is to use it to conduct any transaction linkable to your real identity — including purchasing data from the same cell carrier, buying airtime with a card, or charging it through the same Wi-Fi router as your primary device. Recharge using cash purchased at in-person retail. Do not use a credit or debit card for any transaction associated with the burner identity, including food, transport, or accommodation near the time of burner-related activity.

**Carrier selection**: Major carriers (AT&T, T-Mobile, Verizon) retain metadata and respond to law enforcement process. MVNOs (Mobile Virtual Network Operators) resell the same towers but have varying data retention policies — they are not more private at the radio layer, but some retain less metadata. No US carrier is immune to a grand jury subpoena. The practical benefit of a burner is not carrier choice — it is that the number is not linked to your name, billing address, or credit history.

### 1.2 Device Layering

A mature compartmentalization architecture uses three distinct device layers:

**Layer 1 — Primary device (real identity)**: Your everyday phone in your real name, linked to your email, financial accounts, and healthcare. This device should follow the hardening protocols in `device-hardening-guide.md`. It should *not* run activist applications, store sensitive contacts, or be brought to sensitive meetings.

**Layer 2 — Secondary device (anonymous communications)**: A burner phone as described above. Used only for encrypted communications with people in your network. Never brought to Layer 1 locations. Never connected to your home Wi-Fi. Never present at a sensitive meeting alongside Layer 1. The Security in a Box guide maintained by Frontline Defenders and Tactical Tech recommends that this device run Signal with disappearing messages and no SMS/voice calls — calls generate carrier metadata regardless of encryption.

**Layer 3 — Courier/air-gap device (no communications)**: A device with no SIM card and no Wi-Fi connection used solely for handling sensitive documents, working on sensitive communications drafts, or storing encrypted records. Data transfers to/from this device via encrypted USB only. This device should be a dedicated purchase — never a device previously connected to any account. For most activists, this layer is relevant only when handling documents that would themselves constitute evidence if seized — legal declarations, source communications, organizational membership lists.

### 1.3 Number and Account Management

Phone numbers are identity anchors. The following practices reduce linkability:

- Register Signal on your Layer 2 device using a Google Voice number (reachable at voice.google.com and requiring only a Google account — create one under a pseudonym using Layer 2) or a MySudo number (a dedicated privacy-focused VOIP service). This separates your Signal identity from your carrier number. If law enforcement subpoenas Signal with your real number, they get nothing. If they subpoena with your Voice number, they reach a Google account with no real name.
- Enable Signal usernames and set phone number visibility to "Nobody" (Settings → Privacy → Phone Number). This prevents your phone number from being used to find your Signal account.
- Disable SMS fallback entirely on your Layer 2 device. SMS is unencrypted and generates carrier records.
- Account recovery for any sensitive account should not route through your primary phone number or email. Use offline TOTP codes (Aegis Authenticator on Android, Raivo OTP on iOS — both store codes locally without cloud sync).

**Fingerprinting risks**: Modern platforms including Google, Meta, and Apple correlate devices using non-obvious identifiers — not just account login, but device fingerprints (screen resolution, installed fonts, browser characteristics), IP address history, behavioral biometrics (typing patterns, swipe dynamics), and advertising identifiers (GAID on Android, IDFA on iOS). If your Layer 2 device ever shares a Google account, Apple ID, or Facebook login with Layer 1, the platforms will correlate them regardless of the SIM. Reset advertising IDs regularly (Settings → Privacy on both platforms), and never log into any Layer 1 account on Layer 2 hardware.

### 1.4 VPN and Tor Layering

VPNs and Tor address different threat vectors. Conflating them or using one where the other is needed reduces security.

**VPN**: A VPN replaces your ISP as the entity that can see your traffic. It does not provide anonymity — your VPN provider sees everything your ISP previously saw. For activists, a VPN is appropriate for: (a) hiding browsing content from ISP-level surveillance, (b) preventing IP-based geolocation from websites, (c) masking the fact that you use specific services (e.g., hiding that you connect to Signal servers from a corporate or institutional network). Use a VPN with a verified no-logs policy and a jurisdiction outside US legal process — Mullvad (Sweden) and ProtonVPN (Switzerland) have both had no-logs policies verified through law enforcement requests that returned nothing. Do not use free VPNs — they monetize your data and may cooperate with government requests.

**Tor**: Tor provides stronger anonymity than a VPN but at the cost of speed and compatibility. Tor routes your traffic through three relays, encrypting it at each layer. The entry relay knows your IP but not your destination; the exit relay knows your destination but not your IP. No single relay can correlate both. Tor is appropriate for: (a) high-sensitivity research where you need anonymity from the destination site, (b) communicating through services that require anonymity rather than just encryption, (c) accessing sites blocked by your ISP or network.

**Bridge selection**: In environments where Tor is monitored at the ISP level (which is relevant if you are in a country with active DPI censorship, or if you believe your ISP traffic is being monitored), plain Tor connections reveal that you are using Tor even if not their content. Use obfs4 bridges, which make Tor traffic appear as random bytes and resist active-probing attacks. Get bridges from bridges.torproject.org or by emailing bridges@torproject.org. Snowflake (a WebRTC-based transport) is now the recommended default for heavily censored environments — it mimics WebRTC traffic used by legitimate video calling applications.

**Guard node vetting**: Tor selects a guard node (the first relay) and keeps it for 2-3 months. If an adversary operates or has access to your guard node, they can correlate your Tor entry. For high-risk contexts: do not use Tor at all without at minimum running Tor Browser (which enforces a consistent security posture), and consider running Tor over VPN (VPN → Tor) so that the Tor guard node sees only the VPN exit IP rather than your real IP.

**Exit node jurisdiction**: Exit nodes are operated by volunteers worldwide. For connections that are not otherwise end-to-end encrypted (i.e., HTTP, not HTTPS), the exit node can see and modify the traffic. For all sensitive communications over Tor, ensure the destination uses HTTPS/TLS. Exit node jurisdiction matters primarily if you are concerned about nation-state-level Tor monitoring — adversaries who operate large numbers of exit nodes can perform statistical traffic analysis. For most US activists, the more immediate concern is simpler: never use Tor for any service where you also log in under your real name.

### 1.5 Case Study: Mahmoud Khalil and Rümeysa Öztürk (US, 2025)

**What happened**: Mahmoud Khalil, a Columbia University graduate student and lead negotiator of the 2024 Gaza Solidarity Encampment, was arrested by ICE on March 8, 2025. When agents learned he was a lawful permanent resident (not a visa holder), they stated they would revoke his green card instead. He was transported to a detention facility in Louisiana. Rümeysa Öztürk, a Tufts doctoral student, was arrested on March 25 by plainclothes ICE agents near her Massachusetts home — four days after the State Department quietly revoked her student visa. Both cases were predicated on op-ed articles and protest participation, not any criminal conduct.

**The surveillance mechanism**: In both cases, law enforcement used public social media posts, university disciplinary records, and known associational data (who attended which protest) as the primary evidence base. Neither case required device seizure to establish the factual predicate for arrest. This is consistent with the threat model established in `palantir-threat-model.md`: ImmigrationOS and ELITE aggregate social media activity alongside immigration status data, enabling targeting without traditional criminal investigation techniques.

**What worked in Öztürk's defense**: Her attorneys immediately filed in federal court challenging the constitutional basis of the arrest. A federal judge ruled in February 2026 that there were no grounds for deportation. She completed her PhD and returned to Turkey. Key elements: pre-existing attorney contact (her institution's legal counsel was immediately reachable), documented evidence that the arrest was based solely on protected speech, and a federal court challenge filed before administrative proceedings could conclude.

**Operational lessons**:
1. Social media is the primary surveillance surface for immigration-based political targeting. Public posts on institutional accounts and under real names are immediately accessible without legal process.
2. The window between visa revocation and arrest may be days or even hours — as short as four days in Öztürk's case. Legal counsel must be pre-identified, not identified at the moment of arrest.
3. Physical location discipline matters: Öztürk was arrested near her home, on a route officers had apparently mapped in advance. Predictable movement patterns are a targeting vulnerability.
4. Attorney-client privilege must be established before the crisis, not during it.

---

## Part 2: Physical Security and Movement

### 2.1 Surveillance Detection

Surveillance detection is the practice of confirming whether you are under active physical surveillance. The goal is not to evade surveillance (which may not be possible once established) but to *know* whether it exists, so that operational decisions can be made with accurate information.

**The TEDD framework**: US government surveillance training uses TEDD — Time, Environment, Distance, Demeanor — as indicators that a person may be following you. You should use the same framework in reverse. A surveillance team will typically:
- Appear in more than one environment (at your workplace *and* your transit stop)
- Be seen across more than one time period (morning departure *and* evening return)
- Maintain a consistent distance, neither closing rapidly nor falling too far back
- Display behavioral indicators: loitering without apparent purpose, using phones extensively, wearing the same distinctive clothing across sightings, or making sudden movements when you change direction

**Surveillance Detection Routes (SDRs)**: An SDR is a planned route designed to expose surveillance by forcing any following party to make choices that reveal themselves. An effective SDR incorporates:
- Multiple direction changes (an observer following you through three unrelated turns in different directions is almost certainly following you)
- Speed changes (walk faster, then stop; enter a store, wait, observe who enters after you)
- Mode changes (walk to transit, take transit, walk again — surveillance vehicles must adapt)
- Natural checkpoints (a cafe or shop with a window where you can observe the street behind you)

The four-consecutive-right-turns vehicle technique is a simple confirmation test: no civilian driver follows that route accidentally. On foot, the equivalent is entering a store, waiting 60-90 seconds near the window, and watching who enters or lingers outside.

**Detection indicators**: Specific behaviors suggesting active surveillance include: vehicles parked in the same location across multiple days (note plate numbers and vehicle descriptions); individuals who appear at multiple distinct locations in your routine; a noticeable increase in service vehicles (utilities, delivery) in your immediate area; unusual interest in your neighbors; and changes in how delivery or mail services treat your address.

**Response protocols**:
- *If you detect possible surveillance*: Do not change your behavior dramatically. Sudden changes confirm that you noticed. Complete your planned activity at a reduced sensitivity level. Activate your legal contact protocol (see Part 3). Do not contact sensitive network members from your primary device.
- *If surveillance is confirmed*: Assume that anything you have done in the recent period was observed. Do not attempt to "clean up" digital traces urgently — rapid changes in digital behavior are themselves evidence. Contact your attorney. Do not discuss the case with anyone other than your attorney.
- *Safe house activation trigger*: Physical surveillance confirmed over two or more days is a Tier C emergency trigger.

### 2.2 Safe House Networks

A safe house is not a specific physical location — it is a *network relationship* that provides a place to stay, communicate, or recover outside your normal residential and professional environments. Most activists do not need a dedicated safe house; they need a vetted network of people who can provide temporary residence if needed.

**Cell structure**: Safe house networks are most resilient when organized in cells — small groups (3-5 people) with knowledge of other cells limited to one or two designated liaisons. If one cell is compromised, the liaison can warn adjacent cells without exposing the entire network. This is the model used by the Hong Kong 2019-2021 resistance networks, Iranian and Turkish dissident communities in Berlin (documented by Freedom House's transnational repression research), and US mutual aid networks during the 2020-2021 protest period.

**Vetting**: Anyone who will have access to safe house information should be vetted through existing trusted relationships, not through new contacts developed under stress. Common law enforcement infiltration techniques include: offering to help during a crisis (becoming trusted quickly), providing resources (establishing reciprocal obligation), and positioning near leadership. Vetting protocol: new contacts require vouching by at least two existing trusted members before receiving operational information.

**Physical specifications**: A functional safe house location should have: a rear exit or secondary egress; a location that does not share a physical address with any member's known residence, employer, or regular location; neighbors who are unlikely to notice or report unusual visitors; and clean communications infrastructure (no devices that have been at your primary residence). Short-term rental properties (Airbnb paid with prepaid cards) can serve this function but leave a commercial record. Private hosting by trusted contacts leaves no commercial record.

**Emergency communication**: Designate a check-in protocol with your network — a regular signal (a brief message to a specific Signal group at a specific time) whose absence triggers a welfare check. The absence of a check-in message is more secure than a specific "emergency" message, because it does not require you to send anything when under duress.

### 2.3 Movement Patterns

Routine is a targeting vulnerability. If you leave home at the same time, take the same route, and arrive at the same location every day, any surveillance team can establish your pattern in 48-72 hours and position accordingly.

**Counter-routine practices**:
- Vary departure times by 30-60 minutes
- Use at least two different routes for any regular commute
- Vary transportation mode (transit vs. walk vs. ride-share) across the week
- Do not conduct sensitive activities (calls, meetings) at the same location repeatedly

**Travel security for multi-state or international trips**:

Before departure: assume that your device will be seized at a border crossing. See section 2.4. Activate Tier B protocols if you have not already. Leave sensitive devices at home or perform a clean-device trip (a secondary device with only essential apps, no historical communications).

During travel: avoid discussing sensitive topics using devices that use your real identity. If traveling domestically to attend demonstrations or organize, use your Layer 2 device for all organizing communications. Assume that hotel rooms in the US can be legally searched under certain circumstances without notice (sneak-and-peek warrants under FISA and PATRIOT Act provisions). Do not leave devices unattended in hotel rooms during sensitive trips.

Crossing state lines: federal law applies equally in all states, but state-level law enforcement cooperation with federal agencies varies significantly. States that have enacted non-cooperation policies (California, Illinois, New York, and several others) have documented refusals to share information with ICE absent federal court orders. This provides marginal additional protection but is not a guarantee — federal agencies can and do conduct operations in non-cooperative states.

### 2.4 Device Security in Transit

**The border search legal context**: CBP claims authority to conduct "basic" searches of electronic devices at the border without any individualized suspicion — a policy upheld by most (though not all) federal circuits under the "border search exception" to the Fourth Amendment. A 2025 Pacific Legal Foundation lawsuit challenges a CBP practice of holding a US citizen for four hours until he agreed to unlock his phone. The legal landscape is unsettled: the First, Fourth, Ninth, and Eleventh Circuits have reached different conclusions on whether "advanced forensic searches" require reasonable suspicion. The Supreme Court accepted *Chatrie v. United States* (geofence warrant case) in 2025, which may clarify the framework.

**Practical posture for border crossings**:

- Power off the device before reaching the CBP inspection point. A device that has been powered off since boot requires entry of a passcode before full-disk encryption keys are loaded into memory — this is the "Before First Unlock" (BFU) state, which dramatically reduces what Cellebrite can extract. A device that has been unlocked since boot (the "After First Unlock"/AFU state) has encryption keys in memory and can be extracted even without the passcode on many device models.
- Understand your rights: you may refuse to provide a passcode, but CBP may detain you or seize the device. US citizens cannot be denied re-entry for refusing a search; non-citizens risk being turned away. Weigh this against the sensitivity of what is on the device.
- The cleanest approach for high-risk international travel: travel with a clean device. Back up your primary phone, factory reset it, install only essential apps, and travel with that. Restore from backup after re-entry. This approach is documented in EFF's border crossing guide and is now standard practice for journalists covering sensitive topics internationally.
- Log out of all cloud accounts before reaching the border. CBP can compel access to locally stored data; cloud data requires a separate legal process. If you are logged into iCloud, Google Drive, or Dropbox at the border, CBP has argued it can access that data as "accessible" from the device.

**Cellebrite capability awareness**: Cellebrite's UFED Premium tool can extract data from many locked iPhones running iOS 16 and earlier, and from many Android devices in AFU state. iOS 17+ and recent GrapheneOS builds have meaningfully raised the bar. A device in BFU state with a strong alphanumeric passcode is substantially more resistant. The `device-hardening-guide.md` covers this in detail; the key border-crossing-specific action is ensuring BFU state before any checkpoint.

### 2.5 Documentation: What to Carry

**Safe to carry**: Government-issued ID (required for domestic flight boarding), any court documents establishing your legal status, emergency contact cards (physical, not digital), legal aid organization contact numbers (written, not stored on phone), health insurance cards.

**Avoid carrying**: Organizational membership lists, physical notebooks with activist contact information, devices with unencrypted sensitive data, large amounts of cash (subject to civil asset forfeiture without criminal charge), any documentation that establishes affiliation with organizations currently under federal scrutiny.

**Legal safe harbor documentation**: If you have attorney-client relationship documentation or legal process (a court order establishing your rights in a specific case), carry copies. If you are an asylum seeker with pending status, carry your I-589 receipt notice and any court order establishing status quo. These documents do not guarantee respectful treatment but create a paper record of government knowledge of your status.

---

## Part 3: Legal Defense Coordination

### 3.1 Pre-Crisis Attorney Infrastructure

The single most impactful step available to anyone in Tiers A or B is establishing an attorney-client relationship *before* a crisis occurs. In both the Khalil and Öztürk cases, swift legal response was possible because institutional infrastructure (university legal counsel, ACLU contacts) existed. Individuals without institutional backing need to build equivalent infrastructure personally.

**Attorney network structure**:

A robust pre-crisis legal network includes:
- One criminal defense attorney in your jurisdiction who has agreed to be your first call if arrested. This attorney should have your name, basic background, and a small retainer that establishes the relationship. Public defenders cannot be pre-retained (they are appointed by courts); private criminal defense counsel can.
- One immigration attorney if you are a non-citizen. This is distinct from the criminal defense attorney. Immigration proceedings and criminal proceedings are parallel systems — ICE can move to deport you while criminal charges are pending, and the two processes can interact in ways that require specialized expertise.
- Contact information for the National Lawyers Guild Mass Defense program in your city. NLG operates a legal hotline (a single number, distributed before actions) that connects arrested people to volunteer attorneys and coordinates jail support. Find your local chapter at nlg.org/chapters.
- Contact information for the ACLU National Security Project or your state ACLU if you face surveillance-related legal issues.

**Attorney-client privilege architecture**: Communications with your attorney are privileged only if: (a) they relate to seeking or receiving legal advice, (b) they are kept confidential. The privilege can be waived if you discuss the substance of your attorney communications with third parties, if you use a shared device or account to communicate, or if your attorney uses a platform that logs communications server-side.

For privileged communications, both you and your attorney should use end-to-end encrypted channels — Signal or ProtonMail. The Access Now organization published analysis confirming that encryption is essential to protecting attorney-client communications in digital form: "unencrypted attorney-client communications transmitted digitally are not categorically protected from interception." If your attorney insists on email-only communications, request that they use ProtonMail-to-ProtonMail messaging (end-to-end encrypted within the ProtonMail ecosystem).

**Geographic diversity**: If you operate in a city where federal operations are concentrated, ensure at least one attorney contact is in a different jurisdiction and reachable by phone. If you are arrested and transported (as Khalil was, to Louisiana) your primary local attorney may not be licensed to appear in the jurisdiction of detention. Federal habeas corpus filings can be made by any licensed attorney, but immigration court appearances typically require an attorney licensed in that jurisdiction or admitted pro hac vice.

### 3.2 Bail Funds and Legal Support Networks

Community bail funds provide immediate financial infrastructure when bail is set after arrest. They are not primarily about the legal strategy — they address the practical problem that most people cannot post substantial bail from personal resources, and pre-trial detention dramatically weakens defense options.

**How funds are organized**: Most effective funds operate as separate 501(c)(3) or fiscal-sponsored organizations, not as line items of advocacy groups (which creates legal and financial entanglement). Funds accept donations, hold resources in escrow, and disburse on a first-come basis or through a triage committee. The National Lawyers Guild and National Bail Fund Network jointly publish guidance on fund structure.

**Pre-registration**: Most bail funds require a brief registration (name, contact, organization) before they can rapidly respond. If you are in Tier A, register with your local fund now. The process takes 10 minutes and dramatically reduces response time if arrest occurs.

**Contact procedures under stress**: After arrest, you have the right to make a phone call. This call should go, in order: (1) your pre-identified criminal defense attorney; (2) if no answer, the NLG legal hotline for your jurisdiction; (3) if neither, a trusted person who knows your attorney contact and bail fund registration. Do not use this call to discuss the substance of what happened — assume the call is recorded (it almost always is in US facilities).

### 3.3 Criminal Defense Playbook

**At the moment of arrest**:
- State clearly: "I am invoking my right to remain silent and my right to an attorney." Repeat this if questioned further. Do not qualify it ("I'll talk after...") or answer clarifying questions. Under *Berghuis v. Thompkins* (2010), simply not talking is not enough to invoke the right to silence — you must affirmatively invoke it.
- Do not physically resist. Physical resistance creates additional charges and eliminates Fourth Amendment standing to challenge the legality of the arrest in court.
- Do not consent to searches. Clearly state: "I do not consent to searches." This creates a legal record for suppression motions.
- Do not lie. Lying to federal agents is itself a crime under 18 U.S.C. § 1001 (the Martha Stewart statute). Silence cannot be used as evidence; false statements can.
- Memorize (do not save digitally) your attorney's phone number and the NLG legal hotline for your jurisdiction.

**Evidence preservation**: Before any arrest becomes likely, ensure that your attorney has copies of any documentation that establishes your conduct was lawful — correspondence, organizational records, documentation of protest activity, legal advice you received. This creates a pre-crisis record that cannot be characterized as post-hoc fabrication.

**Family notification**: Designate one person (not another activist who may themselves be arrested) as your family notification contact — someone who will call your family if you are arrested and who knows your attorney's name. This person should *not* have sensitive operational information. Their role is purely communicative.

### 3.4 Post-Arrest Communication

After release on bail or following charges being dropped, assume that your communications may remain under surveillance — bail conditions frequently include monitoring, and investigation may continue even if initial charges were dropped or reduced.

**Legal privilege over eavesdropped communications**: If law enforcement records your attorney communications without authorization (which the Sixth Amendment prohibits), those recordings may be suppressed. Document any evidence that attorney communications were intercepted — your attorney should file a motion for inquiry. The ACLU has litigated cases where prison telecom providers recorded attorney-client calls.

**Civil litigation documentation**: If your arrest involved constitutional violations (improper Fourth Amendment search, First Amendment retaliation), document everything immediately after release: officer names, badge numbers, patrol car numbers, precise sequence of events, physical injuries. Get witness contact information. This documentation is time-sensitive — memories fade and physical evidence disappears.

### 3.5 Case Studies in Legal Defense

**US protest defense (2020-2021)**: During the 2020 Black Lives Matter protests, the NLG's mass defense infrastructure processed thousands of arrest cases. Key lesson: pre-positioning worked. Cities where NLG had pre-distributed legal hotline numbers and established bail funds had dramatically faster release times and better legal outcomes than cities without that infrastructure. Cities without it saw protesters held for days on misdemeanor charges because no one could coordinate counsel.

**Jan. 6 prosecutions (digital evidence lessons)**: The FBI issued geofence warrants to Google that captured location data on 5,723 devices present at the Capitol. Of those, 1,535 names were identified and turned over to investigators. Google Location History data was cited in 128 prosecutions. Social media posts — posted publicly and voluntarily — formed the factual basis for the majority of charges. The lesson is direct: **the FBI did not need to break any encryption to charge most January 6 defendants**. The evidence was already public. Operational security failure was not technical — it was behavioral.

**HK 47 prosecution (2021)**: In January 2021, 55 Hong Kong pro-democracy figures were arrested under the National Security Law for organizing and participating in an informal legislative primary. Thirty-five percent of all NSL arrests were predicated on online speech. The prosecution used defendants' own social media posts, Telegram messages, and public media appearances as primary evidence. The case illustrates: in political prosecutions, the prosecution's goal is often not to prove criminal intent but to establish factual predicate for legal theories (conspiracy, subversion) that are broadly written. Operational security for political defendants means minimizing the documentation of organizing activities that could be reframed by a hostile legal theory.

**Asylum seeker defense (ongoing)**: For asylum seekers facing deportation, the legal defense framework is distinct — it runs through immigration court, not criminal court. The key pre-crisis steps are: filing an I-589 (Asylum Application) as early as possible (this establishes a legal record and triggers certain due process protections), obtaining legal representation before any removal proceedings are initiated, and documenting the basis for fear of persecution with as much corroborating evidence as possible (country condition reports, organizational membership documentation, news articles, medical records if persecution involved physical harm).

---

## Part 4: International Sanctuary Options

### 4.1 The Legal Framework for Asylum

The 1951 Refugee Convention defines a refugee as someone with "well-founded fear of being persecuted for reasons of race, religion, nationality, membership of a particular social group or political opinion" who is outside their country of nationality. The United States is a signatory to the 1967 Protocol, which incorporates these definitions. The key term is "political opinion" — persecution based on your political views or organizing activities qualifies.

The practical difficulty for US citizens or residents seeking asylum abroad is establishing that the US government does not provide adequate legal protection against the persecution they fear. Most receiving countries will scrutinize this carefully — asylum is designed for people fleeing states that lack effective legal systems, and courts in Germany, Ireland, and Canada will typically start from the presumption that the US provides due process.

**The narrow path**: Claims that have a realistic chance of success in receiving countries share several characteristics: (a) the applicant has already experienced concrete adverse action (arrest, detention, deportation proceedings, documented surveillance) rather than general political fear; (b) the action is documented (court records, government communications, news coverage); (c) the action was taken based on protected grounds (political opinion, not criminal conduct); (d) the applicant's continued presence in the US poses a documented risk (ongoing prosecution, active deportation proceedings).

LGBTQ+ Americans face a somewhat different calculus — Germany, Ireland, and Canada have all processed claims from LGBTQ+ Americans based on US state-level policies, though success rates vary and the legal framework continues to evolve.

### 4.2 Country Assessment

**Canada**: Canada is the most accessible option for US nationals due to geographic proximity and no visa requirement for short stays. In the first half of 2025, more Americans applied for Canadian refugee protection than in all of 2024 combined. However, the US-Canada Safe Third Country Agreement creates procedural barriers at land border crossings — claimants arriving at a land crossing are often turned back. **Air travel to Canada bypasses the land-border Safe Third Country Agreement.** File the refugee protection claim immediately upon arrival. Processing timelines vary but have historically been 12-24 months. Critical note: Canada has agreed under certain conditions to accept US deportees, which means its asylum system is under political pressure from both sides.

**Germany**: Germany processes substantial numbers of Iranian and Turkish dissident cases and has infrastructure for political asylum processing. Freedom House's transnational repression research documents that German authorities have actively protected Iranian and Turkish dissidents from their governments' cooperation requests — refusing to share asylum seeker information with Turkish intelligence affiliates even when political pressure was applied. German claims require a German attorney (who can be found through UNHCR Germany or the Federal Office for Migration and Refugees / BAMF). Timeline: 12-24 months for initial decision.

**Ireland**: Ireland recorded 76 US asylum applications in the first nine months of 2025, up from 22 in all of 2024. Ireland is a common-law jurisdiction that shares legal heritage with US courts, which makes US attorneys (with Irish co-counsel) effective in navigating claims. Ireland is not part of the Dublin Regulation for US nationals, which means it does not automatically defer to another EU country. Irish law provides 13 weeks for initial decision; complex claims take longer.

**Iceland**: Iceland is a party to the 1951 Convention. You must be physically present in Iceland to apply. Iceland processes claims with relatively short timelines by European standards, and the country has an established record of independence from US political pressure (the Snowden-era WikiLeaks mirror case is the most public example, though it did not result in formal asylum). The UNHCR maintains a helpline at help.unhcr.org/iceland for assistance with the process.

### 4.3 Travel Security and Pre-Departure Protocol

**Visa requirements**: US citizens do not require advance visas for Canada, Ireland, Germany (up to 90 days under Visa Waiver), or Iceland. File the asylum claim within the lawful visa-free period — overstaying a visa weakens the claim procedurally.

**Identity documentation**: Carry your US passport. If your passport is about to be confiscated by government order (a possibility in some federal cases), be aware that confiscation of a US passport by court order is a significant escalation requiring immediate legal counsel. Do not surrender your passport without an explicit court order.

**Transit routing**: Countries that have signed extradition treaties with the United States (which includes most Western nations) can potentially detain you if a US warrant exists. However, extradition is typically not pursued for purely political cases, and extradition for offenses that are considered political crimes (as opposed to violent crimes) is traditionally excluded from most treaties. Consult an attorney before transit if you have active federal criminal charges — not all charges are extraditable, and some transiting countries will not detain you absent a formal Interpol notice.

**Intermediate destinations** that have been used historically as low-friction transit points: Iceland (no Interpol presence for most political cases, accessible from the US without a long flight), Mexico City (accessible, large exile community, no US extradition for political cases in practice), and Panama City (flight hub with relatively neutral status for most political cases). These are patterns documented in journalism about dissident networks, not formal recommendations — individual circumstances vary substantially.

### 4.4 Re-Entry Risks

Returning to the US after seeking asylum abroad carries significant legal risk if any of the following are true:
- Active federal criminal charges or arrest warrant exist
- Civil deportation proceedings are pending (for non-citizens)
- You have been designated as a "threat to national security" under INA § 237(a)(4)

For US citizens, criminal charges survive departure and re-entry will result in arrest at the port of entry if a warrant exists. For non-citizens, departure during pending removal proceedings is typically treated as voluntary departure and may bar re-entry.

**Civil vs. criminal jeopardy**: Most political prosecution cases in the US involve civil and criminal exposure simultaneously. A criminal conviction is typically required for incarceration; deportation (for non-citizens) can occur on a civil standard. This distinction matters for legal strategy — criminal defense counsel and immigration counsel should coordinate from the outset.

---

## Part 5: Emergency Protocols

### 5.1 Pre-Positioned Resources

An emergency that requires rapid departure does not allow time for normal financial logistics. Pre-positioning resources is not paranoid — it is the same logic as a home emergency kit.

**Cash**: Maintain an emergency cash reserve of at least $500 in small bills (nothing larger than $20) in a location other than your primary residence. Cash is accessible when accounts are frozen, when you cannot use a traceable payment method, or when you need to move without creating a financial record. Amounts over $10,000 in cash are reportable under federal law; amounts over $10,000 in cash in a vehicle are subject to civil asset forfeiture without criminal charge in many jurisdictions.

**Crypto**: A small amount (equivalent to $200-500) in Monero (XMR) — a privacy-preserving cryptocurrency — provides an additional untraceable payment option. Monero uses ring signatures and stealth addresses that make transaction tracing substantially more difficult than Bitcoin. Store the wallet seed phrase (not the wallet file) in a physically secure location separate from your devices.

**Documents**: Maintain a small sealed envelope (in a trusted person's custody, not your own home) containing: a photocopy of your passport or government ID, your attorney's contact information, the phone numbers of your legal support network, your bail fund registration confirmation, and a brief statement of your legal status and current legal proceedings. Update this envelope annually.

**Dead-drop protocol**: If you need to pass resources or documents to a network member under surveillance conditions, use a dead-drop: a pre-agreed physical location where items are left for retrieval, without the giver and receiver meeting. Designate at least one dead-drop location with each of your closest network contacts. The location should be accessible without triggering surveillance (not a home address), not monitored by commercial cameras, and memorable without being written down.

### 5.2 Family Safety

Family members of activists and dissidents are frequently targeted as pressure vectors — not because they have done anything, but because their vulnerability can be used to compel behavior or gather information. Prepare your family accordingly.

**Communication compartmentalization for family**: Family members should know: (a) your attorney's name and contact number; (b) the NLG hotline number; (c) what to say if law enforcement contacts them (they have the right to decline to answer questions and to contact an attorney; they should do so). They should *not* know: operational security details, the identities of network members, or anything that would make them a meaningful intelligence source.

**Custody scenarios**: If you are arrested and have minor children, designate a trusted adult in advance who has legal authority to care for them temporarily. If you are a non-citizen at risk of deportation, consult an attorney about whether your children (if US citizens) have independent legal recourse to remain in the US. The ACLU has documented cases where US-citizen children were deported with their parents under administrative confusion — having documentation of their citizenship status available to a trusted third party is essential.

**Protecting family from targeting**: Federal law enforcement has, in documented cases, served subpoenas on family members, contacted employers, and conducted surveillance on homes of political targets. Alert family members that they may receive law enforcement contact and that they should respond only through an attorney. The NLG "Know Your Risks" booklet specifically addresses what to say when the FBI contacts you and includes guidance for non-citizens and family members.

### 5.3 Evidence Preservation

If you anticipate legal proceedings — either as a defendant or a civil plaintiff documenting government misconduct — preserving evidence correctly from the outset determines what is available later.

**What to document immediately after any incident involving law enforcement**: Date, time, and precise location. Full description of all officers present (agency, badge number, uniform, physical description). Exact words spoken (write this down as soon as possible — within an hour if possible). Witnesses' names and contact information. Physical evidence of any harm (photographs of injuries, torn clothing, damaged property). Any video recorded by you or bystanders.

**Secure backup**: Sensitive documents and records should be backed up in two locations: one encrypted cloud backup (end-to-end encrypted, e.g., Proton Drive or an encrypted Backblaze archive) and one physical backup (an encrypted USB drive held by your attorney or a trusted person outside your immediate network). This redundancy ensures that device seizure does not destroy the evidentiary record.

**Chain of custody**: For any evidence you intend to use in litigation, maintain chain of custody documentation — a record of who has had access to the evidence and when. Legal admissibility of digital evidence requires that it has not been tampered with. Hash files immediately upon creation (SHA-256 hash stored separately) and do not modify originals.

**Legal admissibility of encrypted communications**: US courts have admitted end-to-end encrypted communications as evidence when a party with access to the device produces them. The encryption itself does not make them inadmissible; it makes them inaccessible to parties who do not have device access. Preserve screenshots of relevant Signal conversations if they document government misconduct, but do so through your attorney to maintain privilege over the disclosure strategy.

### 5.4 Escalation Procedures

The following trigger conditions should result in immediate escalation to the next protocol tier:

**Tier A → Tier B triggers**:
- Any member of your immediate network is arrested
- You receive any form of law enforcement contact (call, email, in-person visit) — even if it seems benign
- Your organization receives legal process of any kind
- You notice any of the surveillance detection indicators described in Part 2.1 on two or more consecutive days

**Tier B → Tier C triggers**:
- Physical surveillance confirmed (SDR test confirms following across multiple environments)
- You receive a target letter, grand jury subpoena, or FISA notification
- Your visa status is affected or you receive any communication from USCIS suggesting adverse action
- A network member with your contact information is arrested and you have reason to believe devices were seized

**Tier C execution steps**:
1. Immediately contact your pre-identified criminal defense attorney (or immigration attorney if applicable)
2. Do not use your primary device for any further organizational communications
3. Activate your Layer 2 device and inform your network via a pre-agreed signal
4. Transfer custody of your evidence preservation envelope to your attorney
5. Assess whether physical departure is warranted (see Part 4)
6. If departure is warranted, execute pre-departure protocol before any law enforcement contact

**Network notification discipline**: When activating network protocols, use a pre-agreed code rather than explicit language. "I'm taking some time away from the project" as a coded message to key contacts is preferable to "I'm activating emergency protocols" — the latter is self-explanatory to anyone monitoring your communications. Establish these codes with key network contacts in person, not over any digital channel.

---

## Integration with Core Playbook

This document extends the following sections of the core playbooks:

- **`opsec-playbook.md` Part 1 (Communications Defense)**: The layered device architecture in Section 1.2 above provides the physical infrastructure for the Signal-based communications protocols there.
- **`device-hardening-guide.md` Part 2 (Airplane Mode vs. Power-Off)**: Section 2.4 above extends this into the specific border-crossing context, including the BFU/AFU distinction.
- **`threat-model.md` Section III (Commercial Data Brokers)**: Section 1.1 above on SIM/payment discipline directly counters Palantir's entity resolution capability, which relies heavily on commercial data broker feeds.
- **`palantir-threat-model.md` Section II.A (ICE Tools)**:  The Khalil/Öztürk case study in Section 1.5 above documents the live deployment of ImmigrationOS-style targeting against political speech actors.

---

## Key Resources

- **EFF Surveillance Self-Defense**: https://ssd.eff.org — maintained guides for journalists, activists, and at-risk populations
- **Access Now Digital Security Helpline**: https://www.accessnow.org/help — 24/7 direct technical assistance in 9 languages
- **National Lawyers Guild Mass Defense Program**: https://www.nlg.org/massdefenseprogram — legal hotlines, jail support, and mass defense coordination
- **National Bail Fund Network**: https://www.bailfunds.github.io — directory of local bail funds
- **ACLU Know Your Rights — Protesters**: https://www.aclu.org/know-your-rights/protesters-rights
- **UNHCR Asylum Process (Iceland)**: https://help.unhcr.org/iceland/
- **Tor Project Bridges**: https://bridges.torproject.org
- **Freedom House Transnational Repression Research**: https://freedomhouse.org/report/transnational-repression

---

## Confidence and Limitations

**High confidence**: The technical sections (device layering, Cellebrite capabilities, border search law, Signal configuration, Tor bridge architecture) are grounded in primary technical sources, court records, and EFF/Access Now documentation.

**High confidence**: The case studies (Khalil, Öztürk, Jan. 6 geofence prosecutions, HK 47) are drawn from public court records, Wikipedia's documented case lists, and mainstream press coverage with named parties.

**Moderate confidence**: The international sanctuary section reflects the legal framework and documented precedents as of early 2026. Asylum processing timelines, Safe Third Country Agreement interpretations, and political will in receiving countries change rapidly. Consult an immigration attorney before making departure decisions.

**Gap**: This document does not cover Pegasus-class zero-click spyware attacks, which represent a distinct threat tier requiring separate analysis (see EFF's Threat Lab reporting and Amnesty International's Security Lab forensic methodology). If you have reason to believe you are a Pegasus target, contact Access Now's Digital Security Helpline immediately.

**Gap**: Specific bail fund contacts, NLG chapter hotlines, and local criminal defense attorney referrals require local research — this document provides the framework and national resources but not city-specific contacts.
