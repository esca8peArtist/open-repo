---
title: "High-Risk Population Protection Protocols: Dissidents, Activists, and Asylum Seekers"
project: cybersecurity-hardening
created: 2026-04-27
updated: 2026-04-28
status: complete — extended with HK 2019-2020 case study, geofence SCOTUS update, and Playbook B-2 (device seizure in 6 hours)
depends_on: threat-model.md, palantir-threat-model.md, opsec-playbook.md, device-hardening-guide.md
confidence: high — grounded in documented case law, confirmed investigative methods, EFF/ACLU/NLG guidance, UNHCR frameworks, public court records, and ABA litigation outcomes through April 2026
audience: activists, dissidents, asylum seekers, journalists, attorneys, and domestic violence survivors facing government-level or intimate-partner targeting
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

*April 2026 update*: On April 27, 2026, the Supreme Court heard oral arguments in *Chatrie v. United States*, a direct challenge to geofence warrant constitutionality under the Fourth Amendment. The case involves the FBI's demand that Google search its database of all location records for every user within a geofence perimeter at a specific time — a mechanism that produced the Jan. 6 identification list. A ruling narrowing geofence warrants would retroactively affect pending Jan. 6 cases and prospectively limit law enforcement's ability to perform mass-identification from cell-location data. No decision has been issued as of late April 2026; oral argument reporting indicates multiple justices were skeptical of the government's claim to unrestricted access. Defense attorneys representing clients in politically-sensitive cases should monitor the ruling closely — a favorable outcome creates suppression motion grounds in any case where geofence data was the primary identification mechanism.

**HK 47 prosecution (2021)**: In January 2021, 55 Hong Kong pro-democracy figures were arrested under the National Security Law for organizing and participating in an informal legislative primary. Thirty-five percent of all NSL arrests were predicated on online speech. The prosecution used defendants' own social media posts, Telegram messages, and public media appearances as primary evidence. The case illustrates: in political prosecutions, the prosecution's goal is often not to prove criminal intent but to establish factual predicate for legal theories (conspiracy, subversion) that are broadly written. Operational security for political defendants means minimizing the documentation of organizing activities that could be reframed by a hostile legal theory.

**Hong Kong protest network (2019-2020 adaptation)**: The 2019 Anti-Extradition Bill protests and the subsequent National Security Law (July 2020) produced one of the best-documented case studies in real-time activist operational security adaptation. The trajectory has direct lessons for US-based activists.

*Phase 1 — Pre-NSL (June-December 2019)*: Protesters coordinated using LIHKG (a Reddit-like forum), Telegram channels, and AirDrop. The "leaderless" model was deliberate — by decentralizing decision-making through open voting on LIHKG rather than through identified leaders, protesters reduced the value of any single arrest to law enforcement. AirDrop was used to distribute leaflets inside MTR trains and public spaces in ways that bypassed China's censorship because AirDrop operates peer-to-peer without network routing. Telegram was the primary organizing tool. However, Telegram's security architecture has a critical flaw: by default, it allows any user to match a phone number in their contacts to a Telegram username — meaning police who arrested protesters could potentially identify other protesters in the arrested person's contact list. Telegram was eventually pressured to disable this feature for Hong Kong users. Ivan Ip's arrest illustrates the risk: as administrator of a 20,000-person Telegram group, he was forced to provide device access, potentially exposing all 20,000 members.

*Phase 2 — Post-NSL (July 2020 onward)*: The National Security Law, enacted June 30, 2020, made "subversion," "secession," and "collusion" crimes punishable by life imprisonment. The response was immediate and documented: pro-democracy organizations disbanded; prominent figures including Nathan Law fled Hong Kong; activists deleted social media accounts and digital archives; diaspora networks established division of labor between public-facing members (willing to accept reputational exposure) and operational-support members (maintaining deep cover). The diaspora adaptation involved creating diaspora media outlets, shifting organizing to end-to-end encrypted platforms that Telegram is not by default, and compartmentalizing knowledge — supporters in Hong Kong who had no operational knowledge could not provide it under coercive questioning.

*Operational lessons for US activists*:
1. Platform security defaults matter at scale: Telegram's default contact-matching feature exposed entire networks in a single arrest. Always audit and harden platform privacy settings before a crisis, not during it.
2. Leaderless coordination is resilient to decapitation but requires shared decision-making infrastructure that is itself secure. LIHKG's open-access model worked because the forum was outside the PRC's technical reach; US equivalents (Signal groups, secure forums) require hardened access control.
3. The window for operational security adjustment is before legislative or enforcement escalation, not after. The NSL created a 48-72 hour window during which activists could assess their exposure and make departure or cover decisions. Most who waited beyond that window had fewer options.
4. Diaspora division of labor is a structural model worth adopting early: not all members of a network need the same exposure profile. Mapping who can operate publicly vs. operationally is a planning step, not an emergency response. In January 2021, 55 Hong Kong pro-democracy figures were arrested under the National Security Law for organizing and participating in an informal legislative primary. Thirty-five percent of all NSL arrests were predicated on online speech. The prosecution used defendants' own social media posts, Telegram messages, and public media appearances as primary evidence. The case illustrates: in political prosecutions, the prosecution's goal is often not to prove criminal intent but to establish factual predicate for legal theories (conspiracy, subversion) that are broadly written. Operational security for political defendants means minimizing the documentation of organizing activities that could be reframed by a hostile legal theory.

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

## Part 6: Scenario Playbooks

These playbooks are operationally sequenced for real situations. Each one identifies the threat context, time windows, step-by-step actions, specific tools, relevant contacts, and common failure modes. They are designed for people already in or entering a crisis — not for theoretical preparation that never gets tested.

Read the playbook for your situation *before* you need it. The middle of a crisis is not the time to learn a new protocol.

---

### Playbook A: Activist Arrested at a Protest

**Threat context**: You are arrested at a demonstration. Charges range from misdemeanor disorderly conduct to felony rioting or assault on a law enforcement officer. You may be held for hours or days. Law enforcement may attempt to gather intelligence during booking, transport, or holding.

**Pre-arrest baseline (should already be in place)**:

Before attending any demonstration with arrest risk:
- Write the NLG legal hotline number for your city in permanent marker on your arm. Do not rely on your phone — it may be seized. NLG hotline numbers vary by city; find yours at [nlg.org/chapters](https://www.nlg.org/chapters/) before the day of the action. The national Federal Defense Hotline is (212) 679-2811 for federal repression incidents.
- Leave your primary device at home or in a secure location not accessible to law enforcement at the scene. If you bring a phone, it should be your Layer 2 device with full-disk encryption enabled and a strong alphanumeric passcode. Power it off before any anticipated police contact — this puts it in BFU state, which maximizes extraction resistance.
- Do not bring: notebooks with contact lists, documents linking you to organizational roles, large amounts of cash, or anything that constitutes evidence of activity beyond your presence at the demonstration.
- Designate a jail support contact (someone not attending the demonstration) who will receive your call if arrested, knows your bail fund registration, and has your attorney's name and number.

**At the moment of arrest** (0-5 minutes):

1. Do not physically resist, regardless of whether you believe the arrest is lawful. Physical resistance creates additional charges and eliminates Fourth Amendment standing.
2. Say clearly: "I am invoking my right to remain silent and my right to an attorney." Do not qualify this statement or answer any follow-up questions, including "why won't you cooperate?" or "can you just tell me your name?" You are not required to answer questions. You are required to provide ID in states with "stop and identify" statutes (approximately 24 states), but not to answer substantive questions.
3. If police ask to search you or your belongings: say "I do not consent to this search." Even if they search anyway (which they may, and can in certain circumstances), your stated non-consent creates a record for a suppression motion.
4. Do not unlock your phone for any officer. Do not provide your passcode. If pressed, repeat: "I do not consent to searches of my device."
5. Observe and memorize: officer badge numbers, patrol car numbers, agency (city police vs. sheriff vs. federal), and the time and location of arrest.

**During transport and booking** (5 minutes — hours):

- You will likely be in a vehicle with officers who attempt conversation. This is an intelligence-gathering technique. Remain silent or make only social pleasantries unrelated to the action. Do not discuss charges, other participants, or your organizational role.
- Do not discuss the case with other arrestees in any shared space. Holding cells are audible to staff and in many jurisdictions have cameras with microphones.
- At booking, you will be asked basic identification questions. Provide your legal name, address, and date of birth if required (refusal can result in extended holding for identity verification). Do not provide anything beyond what is legally required for booking.
- When given the opportunity to make a phone call, call: (1) your pre-identified criminal defense attorney; (2) if no answer, the NLG hotline for your jurisdiction; (3) your designated jail support contact. Do not discuss facts of the case on this call — it is recorded.

**Call script for jail call** (use exactly):
> "My name is [name]. I was arrested at [location] at approximately [time] on [date]. I am invoking my right to remain silent and need an attorney. Please contact [attorney name] at [number] and my bail support contact at [number]. I am at [facility name if known]."

**Post-booking, pre-release** (hours — up to 72 hours):

- If bail is set and you are registered with your local bail fund, they will typically act within hours of being notified. The National Bail Fund Network directory is at [bailfundnetwork.org](https://bailfundnetwork.org) — pre-registration dramatically reduces response time.
- If you are held without charge for more than 48-72 hours (varies by jurisdiction), your attorney should file a writ of habeas corpus. This is urgent.
- If you are a non-citizen, immigration consequences can attach immediately upon arrest, before conviction. ICE has placed immigration holds (detainers) at local jails for protesters. Your attorney must address both criminal and immigration dimensions simultaneously — if they are not an immigration attorney, they need to coordinate with one immediately.

**After release**:

1. Document everything within one hour: officer descriptions, badge numbers, precise sequence of events, exact words spoken, any physical harm. Photograph injuries. Photograph damaged property.
2. Contact your attorney before speaking to anyone about the facts of the case, including media or your own organization. Anything you say publicly can be used against you and can affect co-defendants.
3. Review your bail conditions carefully. Typical conditions include restrictions on re-arrest, geographic limitations, and (for federal cases) monitoring. Violating bail conditions is a separate criminal offense.
4. Do not post on social media about the arrest, the demonstration, or what you observed. This is one of the primary ways protest defendants create new evidence against themselves and their co-defendants.
5. Activate Tier B digital protocols: transition organizing communications to your Layer 2 device, review what data was on any device that was seized, and inform your network (using pre-agreed code language) that you have been arrested.

**Common failure modes**:
- Talking to police in booking, believing you are "clearing things up." Everything said is recorded and may be used.
- Calling an unsecured contact who discusses the case over the phone.
- Posting bail fund contact information or jail location on public social media, which documents co-defendant networks.
- Failing to have a pre-identified attorney and assuming a public defender will be quickly available (public defenders are assigned at arraignment, which may be 24-72 hours after arrest).

**Sources**: [NLG Mass Defense Program](https://www.nlg.org/massdefenseprogram/), [NLG Hotline Manual (August 2025)](https://www.nlg.org/wp-content/uploads/2025/08/BW-NLG-Hotline-Manual-Guide.pdf), [ACLU Protesters' Rights](https://www.aclu.org/know-your-rights/protesters-rights), *Berghuis v. Thompkins* (2010) on right to silence invocation, *Riley v. California* (2014) on phone searches.

---

### Playbook B: Dissident or Asylum Seeker Preparing to Leave the United States

**Threat context**: You are a non-citizen (visa holder, lawful permanent resident, or undocumented person), or a US citizen with documented government persecution, and you have assessed that departure from the United States is necessary for your safety. This playbook covers the 72-hour pre-departure window and the asylum filing process in receiving countries.

**Who this applies to**: International students whose visas have been revoked (see Öztürk, Section 1.5 of this document), activists facing imminent federal prosecution, non-citizens with active removal orders who have credible fear claims, and US citizens who have experienced documented First Amendment retaliation and meet asylum eligibility criteria in receiving countries.

**Threat assessment before departure decision** (complete before acting):

Departure during pending removal proceedings is typically treated as voluntary departure and may bar re-entry for 3-10 years. Criminal charges survive departure — if a US arrest warrant exists, you will be arrested upon re-entry. Consult an attorney before departure if any of the following are true:
- Active federal criminal charges or arrest warrant
- Pending removal (deportation) proceedings
- Court-ordered restrictions on travel or surrender of passport
- Upcoming grand jury appearance (flight from a grand jury subpoena creates separate criminal exposure)

If none of the above apply: departure is legally permissible and the decision is yours.

**72-hour pre-departure protocol**:

**Device preparation** (do 48 hours before departure):
- Factory reset your primary phone. Reinstall only essential apps. Log out of all cloud accounts. This creates a clean device for travel that does not expose historical data at the border.
- Ensure your Layer 3 (air-gap) device is fully powered down and stored separately from your travel luggage.
- Export and encrypt any critical documents (personal records, legal filings, organizational evidence you may need for an asylum claim) to a ProtonDrive account under a pseudonymous email you created before this crisis. Store the access credentials physically in a sealed envelope, not on any device.
- Generate a Monero wallet if you have not already. Acquire a small amount via cash-to-crypto kiosk (Coinstar locations that accept cash to Bitcoin can be combined with a Monero swap; alternatively, LocalMonero.co accepts in-person cash trades). This provides purchasing power that does not require a US-linked bank account in the receiving country.

**Financial preparation** (do 48 hours before departure):
- Withdraw cash — enough for 30 days of basic expenses in the receiving country. Do not withdraw an unusual amount in a single transaction from your primary account (this flags bank monitoring systems). Spread withdrawals over 3-4 days if time permits.
- Notify your bank of international travel if you intend to continue using your primary card briefly. Do not notify them of your final destination if it would trigger account flags.
- Open a Wise (formerly TransferWise) account in advance if you have not done so. Wise allows international money transfers with relatively low documentation requirements and is accessible from most receiving countries. Note that Wise requires identity verification — it is not anonymous, but it is functional where US bank cards may be declined.

**Documentation preparation** (do 48 hours before departure):
- Gather originals: US passport, any immigration documents (I-551, I-797, I-589 receipt if applicable), court orders establishing your legal status, birth certificate, marriage certificate if relevant.
- Make physical copies and store them separately from the originals (give copies to a trusted contact who is not traveling with you).
- If your basis for asylum is political persecution, gather supporting documentation: social media posts documenting government action against you, news articles, organizational membership records, correspondence with attorneys, court filings. These will substantiate your asylum claim.

**Destination selection** (decide 48 hours before departure):

*Canada*: Most geographically accessible. File refugee protection claim immediately upon arrival. As of March 2026 (Bill C-12), new restrictions apply — **you must file within 14 days of entry** and avoid entry at land border crossings, which are subject to the Safe Third Country Agreement. **Fly to Toronto, Vancouver, or Montreal.** The STCA does not apply to air arrivals. Contact the Canadian Council for Refugees ([ccrweb.ca](https://ccrweb.ca)) for legal referral after arrival. Filing under the Convention Refugee or Protected Persons framework triggers access to the IRB (Immigration and Refugee Board of Canada).

*Ireland*: No visa required for US nationals. File the asylum application at the International Protection Office (IPO) in Dublin within 72 hours of arrival. Accessible via direct flights from many US cities. Initial decision timeline is approximately 13 weeks under normal circumstances. Contact the Irish Refugee Council ([irishrefugeecouncil.ie](https://www.irishrefugeecouncil.ie)) for legal referral upon arrival. The IPO address is 79-83 Lower Mount Street, Dublin 2.

*Germany*: File at a German Foreigners Office (Ausländerbehörde) or Federal Office for Migration and Refugees (BAMF) office. German asylum processing has well-developed infrastructure for political cases. Contact AWO (Workers' Welfare Association) or Diakonie for legal referral. Note: if you transit through a third country with your own asylum facilities before reaching Germany, this may affect eligibility under the Dublin Regulation (though this applies differently to US nationals than to those with EU entry stamps).

*Iceland*: File with the Directorate of Immigration (utl.is) upon arrival. Iceland is not part of the Schengen Dublin system in the same way; US nationals can file claims there. The UNHCR Iceland helpline is at [help.unhcr.org/iceland](https://help.unhcr.org/iceland/).

**Day-of departure protocol**:

1. Power off your primary phone before arriving at the airport — not at the gate, but before you enter the terminal.
2. Do not check in online using your home network in the hours before departure — this creates a record of your location and device.
3. Travel light. Bring only what you need for 2 weeks and can carry as cabin luggage. Checked luggage is subject to inspection and can be delayed.
4. At departure security: your phone in BFU state. If CBP or TSA asks about travel purpose, you may decline to answer beyond "personal travel." You are not required to disclose your destination reason.
5. Do not post travel plans or location on any social media, directly or by implication, until you have filed your asylum claim.

**Immediately after arrival in receiving country**:

1. Find a secure communications device (a local prepaid SIM, or a library computer) before contacting your network. Do not use your US-SIM phone for calls identifying your location until you have assessed local surveillance risk.
2. Contact the NGO or legal referral organization for the receiving country (listed above).
3. File your asylum or refugee protection claim as soon as legally possible — delays weaken claims procedurally.
4. Contact your US attorney by Signal or ProtonMail to notify them of your status and coordinate document transmission if needed.

**Common failure modes**:
- Departing with active criminal charges without consulting an attorney first — departure can waive certain legal rights and complicate criminal defense.
- Arriving in Canada at a land border crossing — this triggers STCA return to the US. Fly.
- Waiting to file the asylum claim, assuming you can settle in first. Filing delays can be used against you.
- Using your primary US-linked phone in the receiving country, which creates a location record linking your legal identity to the destination.

**Sources**: [Canada–US STCA](https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/agreements/safe-third-country-agreement.html), [Bill C-12 asylum changes (March 2026)](https://www.canada.ca/en/immigration-refugees-citizenship/news/2026/03/new-immigration-and-asylum-measures-from-bill-c-12-the-strengthening-canadas-immigration-system-and-borders-act-have-become-law.html), [UNHCR Iceland](https://help.unhcr.org/iceland/), [Irish Refugee Council](https://www.irishrefugeecouncil.ie), [Relocate.World US Asylum Abroad 2026](https://www.relocate.world/articles/us-citizens-seeking-asylum-abroad-2026), EFF Border Crossing Guide at [ssd.eff.org](https://ssd.eff.org).

---

### Playbook B-2: Device Will Be Seized in Six Hours — Emergency Evidence Preservation

**Threat context**: You have credible reason to believe your device will be seized by law enforcement within hours — a warrant is being executed, you are about to be arrested, law enforcement is en route, or you have been told to surrender a device. This playbook addresses the window between warning and seizure. It is the most time-compressed scenario in this document.

**The two competing priorities**: Evidence preservation (protecting data you want to keep accessible for your own defense) and evidence minimization (ensuring law enforcement cannot use your device as a source of evidence against you or your network) are in tension. Both are legitimate goals but they require different actions and must be prioritized by threat type.

- If you are primarily trying to **protect your own defense evidence** (documents, communications showing government misconduct, correspondence with your attorney): focus on secure backup before seizure.
- If you are primarily trying to **prevent your device from being used as a source of evidence against you or your network**: focus on minimization and BFU state.
- In most cases, both matter. The sequence below addresses both, in priority order given time constraints.

**Immediate assessment (do this first, takes 2 minutes)**:

1. How much time do you actually have? Be realistic — if you have 20 minutes, that changes what is achievable compared to 6 hours.
2. What is on this device that you most need to protect? Identify the three highest-priority categories: (a) material you need for your own defense, (b) contacts and network information that would expose others, (c) personal data with no legal relevance.
3. Is your attorney already aware of this situation? If not, contact them before anything else. Evidence preservation strategy should be directed by your attorney — what you preserve and how may affect privilege and admissibility.

**Hour 0-1: Contact attorney and begin secure backup**

Step 1 — Attorney contact (do this first): Signal your attorney or call on an encrypted line. Tell them what is happening and that a device seizure appears imminent. Ask whether they want you to preserve any specific materials. Their direction takes priority over this playbook — they know your legal situation.

Step 2 — Export critical legal defense documents: Any documents that support your legal position — attorney correspondence, court filings, documentary evidence of government misconduct, organizational records — should be uploaded to an end-to-end encrypted location your attorney can access. ProtonDrive (end-to-end encrypted) or a secured Backblaze B2 archive are appropriate. Do not upload to Google Drive, iCloud (without Advanced Data Protection enabled), or Dropbox — these respond to law enforcement process. Signal your attorney the access credentials via a message set to disappear in 24 hours.

Step 3 — Hash critical files immediately: For any file that you intend to use as evidence, compute a SHA-256 hash (on Mac: `shasum -a 256 filename`; on Linux: `sha256sum filename`; on Windows: `CertUtil -hashfile filename SHA256`). Store the hash value in a message to your attorney. This creates a cryptographic proof that the file has not been modified, which is essential for evidentiary admissibility if you later argue government tampering.

Step 4 — Screenshot and archive Signal conversations relevant to your defense: Signal's disappearing messages may destroy evidence you need before your attorney can review it. If conversations are directly relevant to your legal defense and have not been reviewed by your attorney, screenshot them and include them in your secure backup. Do this selectively — your attorney should know what you are preserving. Preserve only what has legal significance; preserving everything creates an unmanageable archive and may include material that harms your defense.

**Hour 1-3: Network notification and minimization**

Step 5 — Notify your network (using pre-agreed code language): Use your Layer 2 device (not the device about to be seized) to alert key contacts. Use a pre-agreed code signal — not explicit language — because even your Layer 2 communications may be monitored if law enforcement is executing a warrant against you. The goal is to let your network know to activate their own protocols without disclosing your specific situation over potentially monitored channels.

Step 6 — Review and reduce your network exposure on the device being seized: Do not delete communications in bulk — this may constitute obstruction of justice if you are under active investigation and the data is responsive to a warrant. However, if disappearing messages are already set on Signal conversations, let them run — you did not specifically delete them in response to legal process (they were already set to expire). The legal distinction matters: a pre-existing disappearing message timer is defensible; a bulk deletion after receiving a target letter is not.

Step 7 — Log out of cloud accounts: Log out of iCloud, Google, Dropbox, and any other cloud service from the device. CBP and law enforcement have argued that cloud data accessible from a device at the time of seizure is "on" the device for search purposes. Logging out means the data requires a separate warrant directed at the cloud provider — a higher legal bar. This is not obstruction; it is a recognized privacy protection step. (Note: this step is explicitly recommended in EFF's border crossing guide and applies equally to domestic device seizure contexts.)

Step 8 — Enable additional authentication on accounts: Enable a hardware key or additional authentication factor on any account that has not already been hardened. This prevents law enforcement from using password reset vectors to access accounts even after obtaining your device. If you use a TOTP authenticator, ensure the seeds are not stored on the device being seized.

**Hour 3-5: Device preparation**

Step 9 — Decide whether to factory reset: **This is a legally consequential decision that you must discuss with your attorney.** Factory resetting a device after receiving a target letter or grand jury subpoena that covers that device's contents can constitute obstruction of justice (18 U.S.C. § 1519, destruction of evidence). If no active legal process has been served requiring preservation of the device's contents, a factory reset is a legal act. If you have received any legal process requiring preservation, do not reset without attorney direction.

If your attorney advises that reset is legally permissible: A full factory reset returns the device to BFU state and destroys all user data. On iPhone, Settings → General → Transfer or Reset iPhone → Erase All Content and Settings. On Android, Settings → General Management → Reset → Factory Data Reset. A factory reset does not erase data from forensic recovery tools in all circumstances — it removes the file system pointers, but some data may be recoverable from flash storage by advanced forensics tools. However, it substantially reduces the evidentiary value of the device.

Step 10 — If you are not resetting: Power off the device fully. Do not leave it in airplane mode or screen-locked. A powered-off device is in BFU state; the encryption keys are not in memory. As documented in `device-hardening-guide.md`, a device in BFU state with a strong alphanumeric passcode and no unpatched extraction vulnerability is substantially resistant to Cellebrite extraction. The longer the device has been powered off, the lower the risk of memory-resident key extraction.

**Hour 5-6: Final actions**

Step 11 — Secure your Layer 2 device: Your Layer 2 (burner) device and your Layer 3 (air-gap) device should be in someone else's physical custody before any law enforcement contact. Do not have them in the same location as the device being seized. If law enforcement executes a search warrant on your home or person, all devices present are typically subject to seizure. Get your secondary devices out of the physical search radius.

Step 12 — Document what is on the device: Before seizure, create a written memo to your attorney (via secure channel) summarizing what the device contains — especially what categories of data are on it, what applications are installed, and what cloud accounts were linked. This helps your attorney assess what law enforcement has obtained and prepares them to file suppression motions if appropriate.

Step 13 — Do not consent to the search: When law enforcement arrives, state clearly: "I do not consent to searches." Even if they have a warrant and will execute the search regardless, your stated non-consent preserves your right to challenge the warrant's validity and scope in court. Request to see the warrant — you are entitled to inspect it. Note what it specifically covers, because a warrant for "electronic devices" may or may not legally cover specific cloud accounts, and over-execution of the warrant scope is grounds for suppression.

**After seizure**:

- Assume the device is permanently compromised. Do not use it for sensitive communications if it is returned.
- Request a Form 6051D (custody receipt) documenting what was seized — this creates a record for use in any suppression motion.
- Do not attempt to reconstruct destroyed or reset data — this may be inadvertent obstruction if the device is under active legal process.
- Your attorney should immediately request a copy of any search warrant affidavit that can be unsealed (some are sealed during investigation; unsealing can be sought once charges are filed or the investigation becomes public).

**Common failure modes**:
- Bulk-deleting communications after receiving legal process — this is obstruction regardless of the content. Let disappearing timers run; do not manually mass-delete.
- Logging out of cloud accounts but leaving the device unlocked at seizure — law enforcement can often still access cached data and session tokens even after logout. Power-off is the stronger posture.
- Notifying your network over the same device that is about to be seized — if that device is monitored, your warning reveals your network to investigators.
- Resetting the device without attorney direction when legal process requiring preservation has been served.
- Preserving evidence in a location law enforcement can also compel — such as an iCloud backup without Advanced Data Protection, which Apple will produce under a warrant.

**Sources**: [EFF Border Crossing Guide (which covers device seizure generally)](https://ssd.eff.org/module/things-consider-when-crossing-us-border), [Signal Secure Backups documentation](https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups), [Signal Disappearing Messages](https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages), [Activist Security Checklist — Signal](https://activistchecklist.org/signal/), [18 U.S.C. § 1519 (evidence tampering)](https://www.law.cornell.edu/uscode/text/18/1519), BFU/AFU forensic state analysis from `device-hardening-guide.md`.

---

### Playbook C: Attorney Targeted by Government Retaliation

**Threat context**: This playbook addresses attorneys facing government-initiated retaliatory action — including executive orders restricting law firm access to federal buildings or security clearances, DOJ investigations, security clearance revocations, bar disciplinary referrals initiated through political pressure, or surveillance of attorney-client communications. This has become a documented and ongoing threat category in 2025-2026: at least five executive orders targeted specific law firms, and the ABA filed suit in June 2025 to halt what it characterized as "a campaign to intimidate the entire legal profession." As of April 2026, the ABA's amicus brief supports ongoing DC Circuit challenges.

**Threat severity assessment**:

The threat to attorneys differs from the threat to activists in several important ways:
1. Attorneys retain professional obligations that cannot be abandoned under pressure — they cannot simply stop representing disfavored clients without ethical consequences to clients.
2. Attorney-client privilege is both a shield (communications are protected) and a target (government actors have attempted to pierce privilege through surveillance and disciplinary proceedings).
3. The chilling effect on the broader legal community means that even attorneys who are not targeted directly may face difficulty retaining clients or co-counsel for politically sensitive matters.
4. International Day of the Endangered Lawyer 2026 focused on the United States specifically — [The Fulcrum's coverage](https://thefulcrum.us/rule-of-law/endangered-lawyer-day-usa-rule-of-law-under-threat) documents the coordinated campaign.

**Immediate actions when you receive notice of adverse government action**:

*Security clearance revocation* (within 24 hours of notice):
1. Do not accept the revocation as final. In December 2025, a federal judge blocked the Trump administration from revoking the clearance of whistleblower attorney Mark Zaid, finding that "Zaid's representation of whistleblowers and other clients adverse to the government was the sole reason for summarily revoking his security clearance." Zaid's constitutional challenge succeeded on First Amendment retaliation grounds.
2. Immediately contact the ABA's litigation support infrastructure: the ABA filed suit in June 2025 and has maintained amicus support in ongoing appeals. Reaching out to the ABA's Center for Human Rights or Office of the President creates a record of your targeting and may connect you to ongoing litigation.
3. Retain a constitutional law attorney (separate from yourself) to file for injunctive relief. The firms that sued immediately after EO targeting (Perkins Coie, Paul Weiss, Jenner & Block, WilmerHale) prevailed on preliminary injunctions. Speed matters.
4. Document the nexus between the adverse action and your protected legal work. Courts have required the government to justify clearance revocations on non-retaliatory grounds; a documented connection between the revocation and your representation of disfavored clients is the core of a First Amendment retaliation claim.

*Executive order restricting federal access*:
- File for emergency injunctive relief in DC District Court. All firms that challenged EOs in court through June 2025 prevailed.
- Coordinate with your bar association. The State Bar of California ([calbar.ca.gov](https://www.calbar.ca.gov/news/state-bar-raises-concerns-over-federal-overreach-law-firm-executive-orders-and-doj-discipline-rule)), the New York City Bar Association, and the ABA have all filed formal statements or briefs against the EO targeting. Your state bar's formal position strengthens judicial challenges.
- Assess whether you need to notify clients. If an EO limits your ability to access federal courts or agencies on a client's behalf, you have an ethical obligation to inform them promptly so they can arrange alternative counsel if needed.

*DOJ bar disciplinary referral*:
- Contact the National Association of Criminal Defense Lawyers (NACDL) at [nacdl.org](https://www.nacdl.org). NACDL has been actively tracking politically-motivated disciplinary referrals and can provide referral to experienced disciplinary counsel.
- Do not respond to a disciplinary inquiry without a disciplinary defense attorney. The rules governing disciplinary proceedings differ from civil litigation — what you say in a disciplinary response can be used in subsequent criminal proceedings.

**Communications security for targeted attorneys**:

Attorney-client privilege does not physically prevent surveillance — it creates legal grounds for suppression after the fact. To minimize the risk of surveillance in the first place:
- All client communications: Signal with disappearing messages set to 1 week. ProtonMail for email with clients who can use it. Do not use your firm's standard email for any communication with clients you have reason to believe are under government surveillance.
- Legal strategy discussions with co-counsel: assume any non-E2E channel is potentially monitored. The Jan. 6 prosecutions included documented instances where prosecutors obtained attorney discussions that had been shared through non-privileged channels.
- Physical meetings with clients: if you have reason to believe your office is under surveillance, meet in a different location. A government building (a federal courthouse lobby, for example) is ironic but effective — government surveillance in those locations has legal exposure for the surveillance operators.
- Do not discuss case strategy on mobile calls. Calls generate carrier metadata and are subject to CALEA intercept capabilities. Use Signal calls if you must communicate by voice.

**Protecting your clients during your targeting**:

Your targeting is often specifically designed to harm your clients by disrupting their representation. Steps to minimize client harm:
1. Maintain meticulous documentation of all adverse government actions against you so that any eventual client prejudice is documentable.
2. Brief your clients clearly on what is happening and what it means for their representation. Clients have a right to seek alternative counsel; that right must not be impeded by your uncertainty about your own situation.
3. Identify backup counsel for each active matter — ideally someone who has already been briefed on the case and can step in without extensive onboarding.
4. If you are forced to withdraw from representation (e.g., because a security clearance revocation prevents you from accessing classified information needed for the case), provide a formal, documented withdrawal notice and sufficient notice for the client to obtain successor counsel.

**Personal security for the individual attorney**:

Security clearance revocations and EO targeting have been accompanied, in several documented instances, by increased personal surveillance, social media monitoring, and attempts to identify confidential sources through analysis of public filings. The physical and digital security protocols in Parts 1 and 2 of this document apply fully to targeted attorneys:
- Review your social media presence immediately. Any public post that could be characterized as indicative of political motivation for your legal work is a potential exhibit in a retaliation narrative.
- Enable Signal for all sensitive network contacts. The surveillance techniques documented in the `palantir-threat-model.md` — particularly social network mapping through communications metadata — apply to attorneys as readily as to activists.
- If you are a solo practitioner or small-firm attorney, your financial vulnerability is significantly higher than a large-firm attorney. The ABA's pro bono matching infrastructure and the NACDL's resources for targeted counsel include financial assistance components — contact them before your resources are depleted.

**Common failure modes**:
- Accepting adverse government action without legal challenge — every firm that challenged EO targeting in court prevailed, at least at the preliminary injunction stage.
- Failing to notify clients promptly, creating additional ethical exposure.
- Continuing to use standard firm email for privileged communications with high-risk clients.
- Conflating your personal legal defense with your clients' defense — these require separate counsel.

**Sources**: [ABA lawsuit (June 2025)](https://www.americanbar.org/news/abanews/aba-news-archives/2025/06/aba-files-suit-to-halt-govt-intimidation/), [ABA amicus brief (April 2026)](https://www.americanbar.org/news/abanews/aba-news-archives/2026/04/aba-amicus-brief-law-firms-executive-orders/), [Mark Zaid security clearance injunction (December 2025)](https://abcnews.go.com/US/wireStory/judge-blocks-trump-effort-strip-security-clearance-attorney-128680628), [International Day of the Endangered Lawyer 2026 US report (The Fulcrum)](https://thefulcrum.us/rule-of-law/endangered-lawyer-day-usa-rule-of-law-under-threat), [Law Society UK — Keep Your Hands Off the Lawyers](https://www.lawsociety.org.uk/Topics/Research/Keep-your-hands-off-the-lawyers), [NACDL](https://www.nacdl.org/Media/DefendingProtestersFacingCriminalCharges), [Wikipedia — Targeting of law firms and lawyers under the second Trump administration](https://en.wikipedia.org/wiki/Targeting_of_law_firms_and_lawyers_under_the_second_Trump_administration).

---

### Playbook D: Domestic Violence Survivor with Security Concerns Leaving an Abuser

**Threat context**: Survivors of intimate partner violence face a distinct and often under-recognized digital and physical threat model. The abuser's threat is not governmental but may in some respects exceed the government's technical capability — a cohabitating abuser has physical access to devices, accounts, vehicles, and social networks. Ninety-nine percent of intimate partner violence survivors also experience financial abuse, which compounds the surveillance problem: shared bank accounts, shared phone plans, and shared cloud accounts give abusers continuous visibility into location, communications, and activities.

This playbook treats the abuser as an adversary with high physical access and moderate technical sophistication, and applies the same layered security model used in the rest of this document to that specific threat.

**Critical distinction before any action**: The safety planning principle from the NNEDV Safety Net Project is foundational: **do not remove monitoring technology or change security practices without a comprehensive safety plan.** Abusers frequently escalate violence when they lose surveillance capability. Every step in this playbook should be preceded by a safety planning conversation with a domestic violence advocate. The National Domestic Violence Hotline is available 24/7: call 1-800-799-SAFE (7233), text START to 88788, or chat at [thehotline.org](https://www.thehotline.org). Use a device not connected to any shared account or the abuser's network for this contact.

**Threat assessment for your specific situation**:

Before implementing any counter-surveillance measures, assess which of the following monitoring vectors are active in your situation. The NNEDV Safety Net Project's stalkerware guide at [techsafety.org/spyware-and-stalkerware-phone-surveillance](https://www.techsafety.org/spyware-and-stalkerware-phone-surveillance) provides detailed technical indicators.

- **Device-level spyware**: Signs include unexpected battery drain, spikes in mobile data usage, the device appearing to operate independently (screen activating, apps opening), and the abuser appearing to know conversation content they should not know. The Coalition Against Stalkerware offers detection guidance at [stopstalkerware.org](https://stopstalkerware.org/information-for-survivors/).
- **Account-level monitoring**: Shared iCloud or Google accounts give the monitoring party access to photos, location history, contacts, messages, and browsing history. If your phone is on a shared Apple Family Sharing or Google Family plan, your location is shared continuously unless you have disabled it.
- **GPS tracking devices**: Physical trackers (AirTags, Tile, commercial GPS trackers) can be placed on vehicles, in bags, or in clothing. iPhones running iOS 14+ alert users to unknown AirTags traveling with them; Android devices require the AirTag Detector app or the Tracker Detect app from Apple. Commercial GPS trackers require RF scanning equipment to detect. Ask your local domestic violence shelter or a trusted mechanic to help inspect your vehicle.
- **Carrier-level monitoring**: Family plan administrators can access call records, text content (on most carriers), and real-time location through the carrier's family monitoring tools (AT&T FamilyMap, T-Mobile FamilyMode, etc.). Contact your carrier's domestic violence policy line — most major US carriers have DV-specific account separation processes that do not require notifying the account holder.
- **Financial monitoring**: Joint accounts, shared credit cards, and mutual financial advisors create continuous monitoring of spending patterns, locations, and activities.

**The safe device strategy** (do this first, before any other change):

1. Identify a device that the abuser does not have physical access to and that is not connected to any shared account. This may be a library computer, a friend's phone, or a new prepaid device purchased with cash. This is your secure communication device from this point forward.
2. From the secure device: create a new email account at ProtonMail or Gmail (a new account, not connected to your existing Google account) under a non-identifying username.
3. From the secure device: download Signal and register it using a Google Voice number created with the new email account. This is your new secure communications channel.
4. Contact your domestic violence advocate, attorney, and any shelter or housing resources from this secure device only. Do not conduct any safety planning from your primary device until you have assessed and mitigated its monitoring status.

**Safety planning timeline** (coordinate with DV advocate on specific timing):

*T-7 to T-14 days before planned departure*:
- Contact a domestic violence shelter or service organization for a safety planning conversation. Find shelters at [domesticshelters.org](https://www.domesticshelters.org) using a secure device.
- Open a personal bank account at a different bank than any shared account, using a branch physically removed from your usual location. Use a P.O. Box or a trusted friend's address as the mailing address if you do not yet have a secure residence.
- Gather important documents in a portable format (ID, passport, social security card, birth certificates for children, immigration documents, medical records, school records, financial records). If originals are not accessible, request replacement copies from the issuing agencies.
- If you have children, consult a family law attorney about custody implications before departure. Leaving the jurisdiction with children can create legal complications even when there is no custody order in place. Most domestic violence legal advocates can refer you to a family law attorney.

*T-48 hours before departure*:
- Notify your domestic violence advocate of your planned departure date and destination.
- Arrange transportation that does not use a vehicle known to the abuser and that does not rely on a ride-share app linked to your primary account (where ride history is visible).
- If you must use your primary phone before departure: know that it may be monitored. Use it only for normal-pattern activities. Do all planning and communication on your secure device.
- If you have workplace contacts who need to be aware (e.g., if you are changing your emergency contact or need FMLA leave): do not use work email or phone for this communication if the abuser knows your work contact. Use the secure channel.

*Day of departure*:
- Leave when the abuser is not present if at all possible.
- Take your document packet, the secure device, cash, and essential medications.
- Do not tell the abuser directly that you are leaving. This is the moment of maximum escalation risk.
- Go directly to a shelter, a trusted contact's home, or a hotel booked under a third party's name or with cash. Do not go to the first location the abuser would look for you (parents' home, close friend's home the abuser knows well).
- Inform the DV hotline or shelter of your location so that welfare checks are possible.

*After departure*:
- Within 48 hours: change passwords for all accounts the abuser may have access to — email, financial, social media, cloud storage, streaming services. Do this from a new device or after verifying that your device is free of stalkerware.
- Contact your carrier's DV policy line to separate your account from the shared plan. Most carriers have processes to do this without notifying the account holder.
- File for a protective order (restraining order) in the jurisdiction where you currently reside. Legal aid organizations can help at no cost — find your local legal aid at [lawhelp.org](https://lawhelp.org). A protective order creates a legal record of the threat and provides grounds for police response if violated.
- Inform your workplace HR and security team. This is uncomfortable but important — abusers frequently appear at workplaces, and your employer's security team needs to be aware in order to protect you. You control what level of detail you share.
- If you have children, consult a family law attorney about establishing a formal custody arrangement or emergency custody order as soon as possible.

**Digital hygiene after departure** (critical, often skipped):

- If you used your primary device during planning, assume it may have been compromised. Get a forensic evaluation (through your DV shelter's tech safety advocate, not a commercial phone repair shop) before using it for sensitive communications.
- Turn off location services on all apps on any device you continue using. Review app permissions thoroughly — many apps (including social media, weather apps, and games) share location data.
- Review your social media privacy settings. The abuser (and people they enlist) can use public posts to track your location, activities, and new network. Set all accounts to private and review your follower/friend lists.
- If you shared cloud photo libraries: create a new iCloud or Google Photos account and stop contributing to the shared library. Assume the abuser has already downloaded your previous photos.

**Supporting networks and organizations**:
- **National Domestic Violence Hotline**: 1-800-799-SAFE; chat at [thehotline.org](https://www.thehotline.org)
- **Safety Net Project (NNEDV)**: [techsafety.org](https://www.techsafety.org) — detailed tech safety guides
- **Coalition Against Stalkerware**: [stopstalkerware.org](https://stopstalkerware.org) — detection guides, partner with NNEDV
- **DomesticShelters.org**: shelter directory at [domesticshelters.org](https://www.domesticshelters.org)
- **LawHelp.org**: local legal aid referrals for protective orders

**Common failure modes**:
- Changing digital practices suddenly before safety planning is complete — this can trigger escalation before protective infrastructure is in place.
- Using a shared device for any safety planning communication.
- Assuming that the abuser "wouldn't know how to" use stalkerware — stalkerware apps are commercially available, legally purchasable, and do not require technical sophistication to install on a device the installer has physical access to.
- Not addressing the vehicle GPS question — location tracking via vehicle tracker has been used to find survivors after departure in documented cases.
- Using ride-share apps linked to the primary account, creating a record of departure route and destination.

**Sources**: [NNEDV Safety Net Project](https://www.techsafety.org/resources-survivors), [National DV Hotline internet safety](https://www.thehotline.org/plan-for-safety/internet-safety/), [Coalition Against Stalkerware](https://stopstalkerware.org/information-for-survivors/), [Safety Net Technology Safety Plan](https://www.techsafety.org/resources-survivors/technology-safety-plan), [Double Awareness Month 2025 (NNEDV/Safety Net)](https://www.techsafety.org/blog/2025/10/28/double-awareness-month-2025-domestic-violence-and-cybersecurity-1).

---

### Playbook E: Uyghur, Iranian, or Other Transnational Repression Target in the United States

**Threat context**: Transnational repression differs from domestic government targeting in a specific way: the threat originates from a foreign government, may involve both that government's intelligence apparatus and diaspora informants, and can use vectors that US law enforcement cannot (or will not) address quickly. The People's Republic of China's campaign against Uyghur activists is the most documented example: a 2025 investigation found that 60 of 105 interviewed Uyghur dissidents across 23 countries believed they had been surveilled by Chinese agents. Tactics include social media hacking (especially via spear-phishing to deliver malware through apparently legitimate tools — in March 2025, World Uyghur Congress leaders were targeted via a trojanized Uyghur-language text editor), family member coercion in the country of origin, and direct threats by WeChat or phone.

The Council on Foreign Relations documented that transnational repression grew in 2025 and is expected to continue expanding. The Freedom House Transnational Repression database identifies China, Russia, Iran, Saudi Arabia, Turkey, and Ethiopia as the six most prolific practitioners.

**Threat model for this population**:

*Primary vectors for Chinese state targeting*:
- Spear-phishing emails impersonating trusted NGO partners or community organizations, delivering malware via documents or installers
- Compromise of WeChat and WhatsApp accounts (Chinese authorities have direct access to WeChat; WhatsApp accounts can be compromised via malicious links)
- Infiltration of diaspora community organizations by agents posing as activists or community members
- Direct phone calls from Chinese police officers making threats (documented in the 2025 investigation cited above)
- Family coercion: relatives in China are interrogated or threatened as leverage

*Primary vectors for Iranian state targeting*:
- Phishing infrastructure impersonating Western human rights organizations
- Legal requests through international channels (Interpol red notices — though Freedom House research documents Germany's resistance to honoring politically-motivated notices against Iranian dissidents)
- Social engineering of diaspora community leaders

*Primary vectors for Turkish state targeting*:
- Interpol red notices for politically-motivated charges
- Cooperation requests to hosting countries' intelligence services
- Surveillance of Gülenist and Kurdish community networks in Europe and the US

**Immediate protective measures** (these are more device-intensive than for domestic threat actors):

*Device hygiene*:
- Do not install any application received through community channels, even if it appears to be from a trusted organization, without first verifying with the sending organization via a channel separate from the one through which you received the file. The World Uyghur Congress 2025 attack used a trojanized version of a legitimate Uyghur-language text editor — exactly the kind of tool that would be trusted by community members.
- Move all community communications off WeChat. For Uyghur community members, this is directly relevant: WeChat is operated by Tencent, which has near-total compliance with PRC government data requests. Signal or Briar are the appropriate replacements. If network members will not leave WeChat, treat everything on that platform as compromised.
- Enable Google Advanced Protection Program or Apple Lockdown Mode on all primary devices. Lockdown Mode (iOS 16+/macOS Ventura+) is specifically designed for high-risk users targeted by sophisticated attackers: it disables most zero-click attack surfaces including message link previews, complex WebKit features, and incoming FaceTime calls from unknown contacts. The tradeoff in usability is significant but appropriate for this threat level.
- For Android users in this threat tier: GrapheneOS provides the most robust security hardening currently available on Android hardware. It is available for Google Pixel devices at [grapheneos.org](https://grapheneos.org).

*Communications compartmentalization*:
- Do not discuss sensitive political activities on any platform linked to a real-name account that the home-country government can access. This includes Facebook (which has responded to Chinese and other government requests), Instagram, and TikTok (ByteDance).
- Verify the identity of new community members before including them in any organizing conversation. The HK 47 prosecution and documented Iranian exile network infiltrations both involved agents who had established community trust over months before providing information to authorities.

*Protecting family members in the country of origin*:
- Compartmentalize your advocacy activities from any communication with family members. If your relatives' communications are monitored, they cannot testify to what they do not know.
- Establish a safe signal with family — a regular check-in that, if interrupted or altered in character, indicates duress. This is the equivalent of the network check-in protocol in Section 2.2 of this document.
- Contact Freedom House's Transnational Repression documentation project and your local Human Rights Watch or Amnesty International office if you receive a threat. Documented threats create a record that strengthens asylum claims and may trigger international human rights mechanisms.

**If you receive a direct threat** (phone call from home-country police, WeChat message from government actor, in-person confrontation):

1. Do not comply with any demand in the threat before consulting an attorney and a human rights organization.
2. Document the threat immediately: date, time, platform, content of the message, any phone number or account identifier used.
3. Report to the FBI's transnational repression reporting line. The FBI has a specific program addressing foreign government harassment of persons in the United States — contact the local field office. Reporting does not resolve the threat but creates a US government record.
4. Contact Front Line Defenders at [frontlinedefenders.org](https://www.frontlinedefenders.org) via their emergency contact form. Front Line Defenders provides emergency grants, temporary relocation assistance, and case documentation for at-risk human rights defenders. They have processed cases from Uyghur, Iranian, and Tibetan activists in the United States.
5. Contact Access Now's Digital Security Helpline at [accessnow.org/help](https://www.accessnow.org/help) for a forensic assessment of your device if you have reason to believe you have been targeted with spyware. Access Now's team has experience specifically with state-sponsored spyware targeting diaspora communities.

**Interpol red notice and extradition risk**:

If your home country government has filed or threatens to file an Interpol red notice:
- Contact Fair Trials International ([fairtrials.org](https://www.fairtrials.org)) — an organization that specifically litigates against politically-motivated Interpol notices.
- Consult an immigration attorney about documenting the political basis of any charges that form the basis for an extradition request. Most US extradition treaties include a "political offense exception" that bars extradition for acts that are of a political character.
- Avoid travel to countries with poor track records of Interpol notice independence, particularly countries that have extradited nationals of your home country on politically-motivated charges.

**Common failure modes**:
- Continuing to use WeChat for any organizing communications
- Installing community-distributed software without verification from a separate channel
- Assuming that a new community member is trustworthy because they know other trusted people — infiltration typically builds on that assumption
- Not reporting direct threats to the FBI because of distrust of US authorities — in this specific context, a documented FBI report strengthens asylum claims and may result in investigation of the threatening actor

**Sources**: [CFR Transnational Repression 2025](https://www.cfr.org/expert-brief/transnational-repression-grew-2025-and-it-will-only-get-worse), [CSOHATE — Chinese Transnational Repression 2025](https://www.csohate.org/2025/09/02/chinese-transnational-repression/), [Citizen Lab — Uyghur Language Software Hijacked](https://citizenlab.ca/research/uyghur-language-software-hijacked-to-deliver-malware/), [Freedom House Transnational Repression](https://freedomhouse.org/report/transnational-repression), [Front Line Defenders Global Analysis 2025](https://frontlinedefenders.shorthandstories.com/frontline-defenders-global-analysis-2025/index.html), [Access Now Digital Security Helpline](https://www.accessnow.org/help), [Human Rights Foundation — Lasting Impacts of Transnational Repression](https://hrf.org/latest/the-lasting-impacts-of-transnational-repression/).

---

## Integration with Core Playbook

This document extends the following sections of the core playbooks:

- **`opsec-playbook.md` Part 1 (Communications Defense)**: The layered device architecture in Section 1.2 above provides the physical infrastructure for the Signal-based communications protocols there.
- **`device-hardening-guide.md` Part 2 (Airplane Mode vs. Power-Off)**: Section 2.4 above extends this into the specific border-crossing context, including the BFU/AFU distinction.
- **`threat-model.md` Section III (Commercial Data Brokers)**: Section 1.1 above on SIM/payment discipline directly counters Palantir's entity resolution capability, which relies heavily on commercial data broker feeds.
- **`palantir-threat-model.md` Section II.A (ICE Tools)**:  The Khalil/Öztürk case study in Section 1.5 above documents the live deployment of ImmigrationOS-style targeting against political speech actors.

---

## Key Resources

**Legal defense and arrest support**:
- **EFF Surveillance Self-Defense**: https://ssd.eff.org — maintained guides for journalists, activists, and at-risk populations
- **National Lawyers Guild Mass Defense Program**: https://www.nlg.org/massdefenseprogram — legal hotlines, jail support, and mass defense coordination. Federal Defense Hotline: (212) 679-2811
- **NLG Hotline Manual (August 2025)**: https://www.nlg.org/wp-content/uploads/2025/08/BW-NLG-Hotline-Manual-Guide.pdf — operational arrest support protocol
- **National Bail Fund Network**: https://bailfundnetwork.org — directory of local bail funds
- **ACLU Know Your Rights — Protesters**: https://www.aclu.org/know-your-rights/protesters-rights
- **NACDL (criminal defense attorneys)**: https://www.nacdl.org — referrals for criminal defense in protest and political cases

**Asylum and international sanctuary**:
- **UNHCR Asylum Process (Iceland)**: https://help.unhcr.org/iceland/
- **Irish Refugee Council**: https://www.irishrefugeecouncil.ie — legal referrals for Ireland asylum process
- **Canadian Council for Refugees**: https://ccrweb.ca — Canadian refugee protection legal referrals
- **Relocate.World — US Asylum Abroad 2026**: https://www.relocate.world/articles/us-citizens-seeking-asylum-abroad-2026

**Attorneys targeted by government**:
- **ABA Center for Human Rights**: https://www.americanbar.org/groups/human_rights/ — supports attorneys under government pressure
- **Law Society UK — Endangered Lawyers 2026 report**: https://www.lawsociety.org.uk/Topics/Research/Keep-your-hands-off-the-lawyers

**Transnational repression**:
- **Access Now Digital Security Helpline**: https://www.accessnow.org/help — 24/7 direct technical assistance in 9 languages; specializes in state-sponsored spyware
- **Freedom House Transnational Repression Research**: https://freedomhouse.org/report/transnational-repression
- **Front Line Defenders Emergency Contact**: https://www.frontlinedefenders.org/en/programme/emergency-contact — emergency grants and relocation for at-risk defenders
- **Fair Trials International (Interpol red notices)**: https://www.fairtrials.org

**Domestic violence and intimate partner tech safety**:
- **National Domestic Violence Hotline**: 1-800-799-SAFE; chat at https://www.thehotline.org; text START to 88788
- **Safety Net Project (NNEDV)**: https://www.techsafety.org — comprehensive tech safety guides for survivors
- **Coalition Against Stalkerware**: https://stopstalkerware.org — detection and removal guides
- **DomesticShelters.org**: https://www.domesticshelters.org — shelter directory
- **LawHelp.org**: https://lawhelp.org — local legal aid for protective orders

**Technical tools** (referenced throughout this document):
- **Tor Project Bridges**: https://bridges.torproject.org
- **Briar (mesh messenger)**: https://briarproject.org
- **GrapheneOS**: https://grapheneos.org
- **ProtonMail / ProtonDrive**: https://proton.me

---

## Confidence and Limitations

**High confidence**: The technical sections (device layering, Cellebrite capabilities, border search law, Signal configuration, Tor bridge architecture) are grounded in primary technical sources, court records, and EFF/Access Now documentation.

**High confidence**: The case studies (Khalil, Öztürk, Jan. 6 geofence prosecutions, HK 47) are drawn from public court records, Wikipedia's documented case lists, and mainstream press coverage with named parties.

**High confidence**: The scenario playbooks (Part 6) are grounded in confirmed organizational protocols (NLG Hotline Manual August 2025, Safety Net Project, Front Line Defenders), documented case outcomes (ABA/EO litigation, Mark Zaid injunction December 2025, World Uyghur Congress spear-phishing March 2025), and current statutes. They represent best-practice synthesis, not legal advice for individual cases.

**Moderate confidence**: The international sanctuary section reflects the legal framework and documented precedents as of early 2026, including Canada's Bill C-12 changes (effective March 26, 2026). Asylum processing timelines, Safe Third Country Agreement interpretations, and political will in receiving countries change rapidly. Consult an immigration attorney before making departure decisions.

**Moderate confidence**: The transnational repression sections describe threat patterns documented in Freedom House, Citizen Lab, and CFR research. The specific technical attack vectors used by Chinese, Iranian, and Turkish state actors evolve rapidly; check Citizen Lab ([citizenlab.ca](https://citizenlab.ca)) for current analysis.

**Gap**: This document does not cover Pegasus-class zero-click spyware attacks in detail, which represent a distinct threat tier requiring separate analysis (see EFF's Threat Lab reporting and Amnesty International's Security Lab forensic methodology). If you have reason to believe you are a Pegasus target, contact Access Now's Digital Security Helpline immediately — they have the forensic methodology to verify and document it.

**Gap**: Specific bail fund contacts, NLG chapter hotlines, and local criminal defense attorney referrals require local research — this document provides the framework and national resources but not city-specific contacts.

**Gap**: Playbook D (domestic violence) does not address the specific legal and safety challenges in rural areas, where shelter availability and law enforcement cooperation are substantially different from urban contexts. The Safety Net Project and National DV Hotline provide rural-specific guidance.
