---
title: "Activist Organizing and Counter-Surveillance Playbook: Digital and Physical Defense for Protest Organizers"
project: cybersecurity-hardening
created: 2026-05-06
status: scenario-specific-guide
phase: Phase 2
session: 844
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — grounded in documented government capabilities (Babel Street DHS contracts, LAPD/NYPD drone flight records, Flock Safety EFF investigation, Mobile Fortify Minneapolis deployment, DHS administrative subpoenas), Amnesty International and EFF primary source reporting, and court filings
audience: Protest organizers, political activists, community defense networks, legal support organizations, security teams advising activist groups
---

# Activist Organizing and Counter-Surveillance Playbook

**Executive Summary for Organizers and Legal Support Networks**: This guide maps the specific surveillance stack deployed against protest participants and political activists in the United States as of 2026, and provides actionable countermeasures organized by implementation priority. The threat is documented and operational: Babel Street's persistent OSINT monitoring runs continuously against public social media profiles; Flock Safety's ALPR network was used by 50+ agencies to track vehicles at No Kings, Hands Off, and 50501 protest sites; LAPD deployed drones 31 times against a single downtown Los Angeles protest; ICE agents photographed protesters using Mobile Fortify in Minneapolis; and DHS issued hundreds of administrative subpoenas to unmask anonymous anti-ICE social media accounts. These are not emerging risks — they are in-use capabilities with documented deployment records. The countermeasures below address each layer.

This playbook is a companion to the Immigration + Surveillance Evasion Playbook and the broader corpus (`threat-model.md`, `opsec-playbook.md`). Cross-references are provided. Do not duplicate work: if you have already hardened your device per the immigration playbook or `implementation-guide.md`, those measures apply directly here.

---

## Part 1: Threat Model Specific to Activist Organizing

### 1.1 The Five-Layer Surveillance Stack Deployed Against Activists

The government surveillance infrastructure targeting activists operates across five distinct layers that compound each other. Defeating one layer while ignoring others provides false security.

**Layer 1: Social Media OSINT — Babel Street Persistent Monitoring**

Babel Street is a commercial OSINT platform with confirmed DHS, ICE, CBP, and State Department contracts. It is not merely a search tool: Babel Street's "persistent search" feature continuously monitors any new content appearing online that matches flagged individuals, keywords, or geographies — without a new query being initiated. The system automates scraping and flagging at scale.

Amnesty International's 2025 investigation documented Babel Street being used specifically against pro-Palestine student protesters, with DHS's Senior Vice President of Risk publicly promoting keyword searches to identify "radicalized groups" and flag individuals for visa revocation, detention, and deportation. The mechanism converts organizers into permanent investigation subjects from the moment their name or handle appears in a relevant context — even if that content is constitutionally protected.

The "Catch and Revoke" initiative, operated by the State Department in coordination with DHS and DOJ, uses AI to review visa holders' social media for protest-related content and revoke visas accordingly. As of 2026, Babel Street is feeding directly into this pipeline. [State Department Catch and Revoke — immpolicytracking.org](https://immpolicytracking.org/policies/reported-state-department-plans-to-use-ai-to-revoke-visas-of-students-engaged-in-pro-hamas-activity/)

**Layer 2: Aerial Surveillance — Drone Deployment at Protests**

This is the layer most inadequately addressed in generic security guides. LAPD deployed Skydio X10 drones at least 31 times to surveil a single anti-ICE protest in downtown Los Angeles on January 31, 2026, and again at least 32 times at the March 28 No Kings protest. The Skydio X10 detects people from 8,000 feet and identifies individuals from 2,500 feet. It reads license plates from 800 feet.

NYPD's drone program conducted 6,546 flights in the first six months of 2025, a 3,200% increase since 2022, with deployment confirmed at No Kings demonstrations. CBP flew a military-grade MQ-9 Predator drone over anti-ICE protests in Los Angeles. The FAA rule of January 16, 2026 banned third parties from flying drones within 3,000 feet of active ICE operations, creating aerial exclusion zones that grant ICE sole surveillance authority during its own enforcement actions.

Ground-level countermeasures (face masks, hats) are partially effective against aerial platforms. Overhead and oblique angles used by drones require additional countermeasures described in Part 4. [The Intercept — LAPD drone surveillance No Kings protest](https://theintercept.com/2026/04/20/lapd-skydio-drone-surveillance-no-kings-protest-ice/)

**Layer 3: Vehicle Tracking — ALPR at Protest Sites**

Flock Safety's ALPR network operates across 5,000+ communities. EFF's November 2025 investigation documented more than 50 federal, state, and local agencies running hundreds of ALPR searches in connection with protest activity specifically — the 50501 protests in February, Hands Off in April, and No Kings in June and October 2025. Flock was simultaneously developing "Nova," a product that supplements ALPR data with information from data breaches and commercially available data to track specific individuals without a warrant. [EFF — How cops are using Flock Safety to surveil protesters](https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/)

If your vehicle's license plate appears in ALPR data at a known protest site, that record is stored and queryable. If your vehicle appears at multiple protest sites across weeks or months, the pattern maps your organizing activity regardless of any digital privacy measures you take online.

**Layer 4: Field Biometric ID — Mobile Fortify at Protest Perimeters**

ICE agents photographed protesters using Mobile Fortify during protests in Minneapolis — photographs from the scene show agents in tactical gear using phones to scan faces. The device transmits the photograph against DHS's HART biometric database (150M+ records) and returns identity matches. As documented in the immigration playbook and `PHASE_2_SEQUENCING_STRATEGY.md` Section 1.2, ICE has used Mobile Fortify more than 100,000 times since launch.

The activist-specific threat this creates is distinct from the immigration context: even US citizens with no immigration vulnerability can be enrolled in a protest-related biometric database and subsequently monitored. ICE and FBI agents have explicitly described using facial recognition data from protests to add individuals to databases of "domestic terrorists," with direct First Amendment implications. [NBC News — ICE agents using facial recognition at protests](https://www.nbcnews.com/tech/security/ice-agent-facial-recognition-video-protest-movile-fortify-photo-rcna257331)

**Layer 5: Account Unmasking — DHS Administrative Subpoenas**

DHS issued hundreds of administrative subpoenas to Google, Reddit, Discord, and Meta between late 2025 and early 2026, seeking to unmask the identities behind anonymous anti-ICE accounts. Targets included accounts that posted bilingual ICE raid alerts in Montgomery County, PA, and accounts that tracked ICE agent locations. Unlike traditional warrants, administrative subpoenas require no judicial authorization before issuance. Google, Meta, and Reddit complied in at least some cases; others notified account holders with a 10–14 day window to challenge.

The critical implication for organizers: anonymity on major commercial platforms cannot be assumed. If your account has ever been linked to your real identity through any data point (registration email, phone verification, IP address, payment method), DHS can reach that link through a subpoena to the platform. [TechCrunch — DHS subpoenas to unmask anti-ICE accounts](https://techcrunch.com/2026/02/14/homeland-security-reportedly-sent-hundreds-of-subpoenas-seeking-to-unmask-anti-ice-accounts/)

---

### 1.2 AI/ML Threats Specific to Activist Contexts

Three AI/ML patterns documented in `PHASE_2_SEQUENCING_STRATEGY.md` Section 1.3 have specific implications for activists that differ from the general population.

**Behavioral pattern-of-life flagging (Palantir AIP)**: Palantir's AIP agents can autonomously monitor data streams and flag individuals when pattern thresholds are crossed. For activists, the relevant threshold is not just identity — it is behavioral. Regular attendance at protest locations, social media posts correlating with known organizing timelines, and financial transactions at activist-affiliated organizations all generate behavioral signals. An AIP agent can surface you as a person of interest based solely on behavioral correlation with known organizing activity, without any individual analyst initiating a query.

**Deepfake content fabrication against activists**: In January 2026, a White House account posted a photograph of an African American protester in Minnesota that had been altered to darken her skin and depict her in tears — documented AI manipulation of protest imagery for political purposes. Beyond government manipulation, deepfake technology is now accessible to any actor with a smartphone. For activist organizers with a public video presence (speaking at rallies, interviews, recorded meetings), fabricated video depicting them saying things they never said is a realistic harassment and delegitimization threat. The same ProKYC-type tools documented in the advanced threats analysis can generate synthetic video that passes basic authenticity checks. Countermeasures: establish provenance for important public statements (record on multiple devices with timestamp, share original files with trusted legal contacts immediately), and pre-brief your legal team and community that fabricated content targeting you is a known threat.

**Social graph expansion**: ImmigrationOS stores social relationships. Babel Street maps social connections through communication pattern analysis. If a known organizing target's profile has connections to your account, username, or contact information — even through indirect association — you enter the social graph of that investigation. This is documented in `palantir-threat-model.md` as the entity resolution mechanism: the system creates ontological links between associated persons, and those links are persistent.

---

## Part 2: Social Media Hygiene and Digital Footprint

*Expands PHASE_2_SEQUENCING_STRATEGY.md Section 3.3.1*

### 2.1 The 72-Hour Pre-Action Protocol

Babel Street's persistent monitoring collects public content continuously. Content posted in the period immediately before and during a public action is the highest-risk window because it is temporally correlated with the action and provides real-time context to analysts monitoring for that event.

**72 hours before any public action**:
1. Set all social media accounts to maximum privacy. On Instagram and Facebook: Settings > Privacy > Account Privacy > Private. On X/Twitter: Settings > Privacy and Safety > Audience and Tagging > Protect posts. On TikTok: Settings > Privacy > Private Account.
2. Review your last 30 days of posts. Archive or delete anything that identifies your regular locations, travel patterns, home neighborhood, vehicle, or event planning details. Babel Street retrospective searches can pull this content even after the action is over.
3. Remove location tagging from all future posts. Settings vary by platform — disable it globally, not per-post.
4. Do not post event logistics (time, route, staging location, legal contact numbers) in public-facing formats. Use closed Signal groups with disappearing messages enabled (24-hour default) for operational coordination.

**During the action**: Do not post from the protest site with location services enabled. If you post at all, post after leaving the area. Photos you take with geotagging enabled embed GPS coordinates in the file's EXIF data — disable camera location access in your phone's app permissions before leaving home.

**After the action**: Wait 48 hours before posting any documentation of the action from your personal accounts. If your organization maintains a public documentation account, that account should have no connection to your personal identity (separate device, separate email, separate IP — see Section 2.3 on organizational account separation).

### 2.2 Account Architecture: Personal vs. Organizing vs. Public

The central principle is context separation. Your personal account (connected to your real identity), your organizing coordination account (used within your group), and any public-facing organizational account are three different threat surfaces with three different countermeasures.

**Personal accounts**: Apply the 72-hour pre-action protocol above. The goal is not to hide that you organize — it is to prevent Babel Street from building a behavioral profile by correlating your posts with known protest timelines.

**Organizing coordination accounts** (Signal groups, private Discord, closed Signal channels): These should never be used for public-facing communications. Membership should be limited to vetted participants. New member vetting matters: in documented cases, law enforcement has placed informants in activist organizing groups. The digital equivalent is an account that appears to be a known organizer but is actually managed by law enforcement. Vet new members through in-person contact whenever possible. Enable disappearing messages.

**Public-facing organizational accounts**: These accounts are, by design, public and persistent. Assume everything posted here is monitored. Babel Street will flag it. The countermeasure is not secrecy — it is separation. Ensure the operator of the public account is not personally identified on that account (separate email registered through Tor or a VoIP service, separate device, no recovery phone number linked to the operator's identity).

### 2.3 Babel Street Countermeasures: What Actually Works

- **Remove public posts that identify your organizing role**: Babel Street requires public content to scrape. Content that is not public is not accessible to it.
- **Use usernames not connected to your legal name**: This does not stop subpoenas to platforms (see Part 1.1, Layer 5), but it stops passive OSINT correlation. Pseudonymous accounts on separate devices provide meaningful protection against automated surveillance; they provide only time-delay protection against a targeted subpoena.
- **Avoid cross-posting between personal and organizing accounts**: Any cross-post that appears on both accounts provides an entity-resolution anchor linking the two identities.
- **For visa holders and international students specifically**: The Catch and Revoke pipeline specifically targets public social media for protest-related content. The operational countermeasure is maximum privacy settings and no public posts about protest participation. This is a genuine harm-benefit tradeoff: advocacy is valuable and protected, but documented Catch and Revoke enforcement demonstrates that public expression carries visa revocation risk for non-citizens that US citizens do not face. Consult with immigration counsel about your specific visa status before making public protest-related statements.

---

## Part 3: Vehicle and Transit Security

*Expands PHASE_2_SEQUENCING_STRATEGY.md Section 3.3.2*

### 3.1 Understanding the ALPR Protest Tracking Problem

The Flock Safety evidence is specific: 50+ agencies ran ALPR searches against protest-correlated license plates for the 50501 protests, Hands Off, and No Kings. This is not a theoretical capability — it is a documented operational practice. ALPR data is stored, queryable, and shareable across the Flock national network.

The structural problem for activists is temporal correlation: if your vehicle's license plate appears in ALPR data near protest sites across multiple events, that correlation is stored permanently and can be used to establish that you were present at those events regardless of any other security measures you took.

### 3.2 Vehicle Choice Strategy

**First choice: Use transit or walk when possible.** Transit leaves no vehicle record in ALPR data. If you take public transit to a protest and pay with cash (not a transit card linked to your identity), there is no vehicle-based location record for that event.

**Second choice: Use a vehicle not associated with your identity.** Options:
- Carpool with a friend in their vehicle (plates are not yours)
- Use a cash-purchased rental from an agency that does not require an identity-linked credit card (increasingly difficult but possible at some independent agencies; requires advance research)
- Request a rideshare pickup several blocks from your departure point, and request a dropoff several blocks from the protest site. The pickup and dropoff points are linked to your account, but they are not directly in the ALPR field of view near the protest.

**If driving your own vehicle is unavoidable**:
- Park at least 4–6 blocks from the protest site perimeter. Flock cameras are concentrated near the entry points that agencies anticipate protesters will use. Distance from the core ALPR coverage area reduces (but does not eliminate) detection probability.
- Vary your arrival and departure times. Do not arrive at the same time you typically arrive at other events. ALPR pattern-of-life analysis correlates not just location but time.
- Do not park in the same block or structure you have used at previous protests. Pattern repetition across events is the data point that maps organizing activity.

### 3.3 Temporal De-Correlation

Temporal correlation is the analytical technique that links your vehicle (via ALPR), your phone (via cell tower data), and your social media posts to the same event timeline. Even if each data point is individually weak, temporal co-occurrence at the same location strengthens the inference that the same person is connected to all of them.

De-correlation means introducing randomness into the timing signature:
- If you always arrive at protests 30 minutes early and depart immediately after, that timing signature is a behavioral fingerprint. Vary it deliberately.
- Do not use your phone near the protest site. Leave it powered off or in a Faraday bag from the moment you leave your vehicle until you have departed the area and are in a different location from where you parked. Your phone's cell tower check-ins create a location timeline that corresponds to the ALPR data.
- If your phone must be on (emergency contact role, legal observer support), use airplane mode except when actively needed. Airplane mode stops active cell tower communication; it does not stop passive baseband firmware responses on all devices. Full power-off is the only guarantee.

---

## Part 4: Physical Countermeasures Against Aerial and Ground Surveillance

*Expands PHASE_2_SEQUENCING_STRATEGY.md Section 3.3.3*

### 4.1 Layered Countermeasures for Ground-Level Surveillance

**Face + hat + sunglasses combination**: This remains the most effective accessible countermeasure against ground-level facial recognition.
- Medical-grade mask (N95 or FFP2, not cloth) covers the lower 40% of facial geometry that most algorithms rely on. A cloth mask provides visual obstruction but is more permeable to infrared cameras in low-light conditions.
- Hat with a full brim (baseball cap works; wide brim is better) reduces overhead and oblique-angle acquisition from fixed elevated cameras and from drone-mounted cameras at moderate altitudes.
- Sunglasses defeat periorbital feature extraction and reduce iris recognition capability. Wraparound or large-frame sunglasses provide greater coverage against wide-angle optics.
- Combined, this reduces recognizable features to approximately 20%, which drops recognition accuracy from 99%+ to 40–60% depending on the algorithm. Not zero — but meaningful degradation against automated systems with large queues.

**Limitation that matters for activism specifically**: Mobile Fortify used at close range by an ICE agent who is actively trying to photograph you is a different threat than a CCTV camera at 20 meters. At close range, the agent can position the camera to capture an uncovered angle. Physical distance from ICE agents at protest perimeters is a more effective countermeasure than mask-alone when agents are actively scanning faces.

### 4.2 Aerial Drone Countermeasures

Ground-level facial coverage that is effective against static CCTV cameras breaks down under aerial surveillance for two reasons: overhead angle exposure (face visible from directly above when looking up, which is uncommon) and clothing-based re-identification (drones track individuals who lose facial recognition coverage by continuing to track their distinctive clothing).

**Overhead angle**: At Skydio X10's operational altitude, the primary identification method shifts from facial feature matching to movement patterns and clothing signatures when face masks are worn. An overhead angle sees the top of a hat, not a face. The most effective aerial countermeasure against identification-at-altitude is generic, non-distinctive clothing — dark or neutral tones (gray, black, navy, dark olive), no logos, no distinctive patterns, no bright colors. If everyone in a crowd wears generic dark clothing, aerial re-identification becomes computationally expensive.

**Clothing change protocol**: Change at least one major outer layer (jacket, top layer, hat color) before leaving the protest area. This breaks the visual continuity chain that aerial and perimeter CCTV systems use to track individuals from inside a crowd to individual vehicle or transit connections. The handoff moment — from protest crowd to transit or parking area — is where individual tracking reconnects dispersed protesters to identity anchors. Breaking the clothing signature at that transition point degrades this handoff.

**Umbrellas**: An open umbrella directly defeats overhead drone camera acquisition for the individual directly below it. This is a high-friction countermeasure (requires carrying and deploying an umbrella) but effective. In wet-weather protests or protests where drone presence is confirmed, umbrella protocols for key organizers have functional value.

**Building cover**: Overhangs, scaffolding, tree canopy, and building awnings all block aerial line of sight. When drone presence is suspected or confirmed (use ADS-B Exchange — adsbexchange.com — on a separate device to check active drone flights in the area), route movement under available cover wherever possible. This is easier for organizers coordinating movement than for individual protesters.

**Crowd distribution**: Dense concentrated crowds make individual aerial tracking harder by increasing the computational cost of maintaining distinct identity tracks for each person. Dispersed small-group movement (protesters spreading across a wide area in groups of 2–5) is easier to track individually than a dense march. This is a tactical consideration for organizers, not individual protesters: concentrated mass presence provides better aerial cover but different ground-level risks.

### 4.3 IMSI Catchers and Device Detection at Protests

IMSI catchers (cell-site simulators, Stingrays) are deployed by law enforcement to collect IMEI numbers and cell tower connection data from all phones in an area. They cannot (in most configurations) intercept encrypted communications — but they can establish that your device was present at a specific location at a specific time.

The countermeasure is the same as the temporal de-correlation guidance in Part 3.3: power off your phone before entering the protest perimeter. Airplane mode is insufficient on most devices — baseband firmware can still respond to cell tower authentication requests while the OS shows airplane mode enabled. Full power-off eliminates this. Store the powered-off phone in a Faraday bag (Mission Darkness, Silent Pocket, or equivalent — $20–$80) for additional security against any residual baseband vulnerability.

If you need a phone for the action (emergency communication, legal observer documentation), use a dedicated burner device — a prepaid phone purchased with cash, with no connection to your identity — and keep your primary phone powered off and bagged.

---

## Part 5: Emergency Communication and Legal Support

*Expands PHASE_2_SEQUENCING_STRATEGY.md Section 3.3.4*

### 5.1 Pre-Action Legal Preparation

This section addresses the single most underprepared element of activist security: legal support infrastructure must be established before the action, not during it.

**Before the action, every participant should have**:
1. The National Lawyers Guild mass defense hotline number written in permanent marker on their forearm or upper arm (not stored in a phone that may be seized): NLG National Mass Defense Hotline — (212) 679-2811. Local NLG chapter numbers should be used where available (list at nlg.org/chapters/). Writing the number on skin means you have it even if your phone is seized, dead, or destroyed.
2. A designated "outside contact" — a trusted person who is NOT at the action — informed of your plans. This person's role is to receive check-ins and contact legal support if check-in is missed.
3. A pre-written legal statement — a card or note in a wallet pocket stating: "I am exercising my right to remain silent. I request an attorney immediately." You do not have to say anything else.

**Pre-action legal brief**: Organizers should conduct a 5-minute legal brief at the start of every public action covering: the right to remain silent, the right to refuse consent to search, the process for requesting an attorney, and the check-in protocol. The NLG Legal Observer program (nlg.org/massdefenseprogram/los/) can provide trained legal observers who document police interactions. Contact your local NLG chapter to request legal observers for planned actions.

### 5.2 Check-In Protocol

The check-in protocol is the operational mechanism that connects you to legal support if something goes wrong. It requires minimal technology and works even if your phone is seized.

**Establish before the action**:
- A specific check-in time (e.g., "I will check in by 4:00 PM")
- A communication method (Signal message to outside contact)
- A trigger for escalation ("If I haven't checked in by 4:30 PM, contact [NLG hotline number] and tell them my last known location was [location]")

**What outside contact does if check-in is missed**:
1. Call the NLG mass defense hotline or local chapter hotline
2. Provide: your name, physical description, last known location, the time you were last in contact, and whether you were with others
3. Contact trusted family members or other support contacts
4. Monitor the jail lookup system for the local jurisdiction (most jurisdictions have online systems; NLG can guide this)

**Signal group configuration for check-in coordination**:
- Create a dedicated Signal group for the action's legal support contacts — outside contacts and any NLG-affiliated support
- Enable disappearing messages (24 hours)
- Pre-distribute the group ID to participants before the action
- This group should have no operational planning content — only the check-in function

### 5.3 If You Are Detained or Arrested

The principles from the immigration playbook apply directly and are not repeated here. The activist-specific additions:

**Do not consent to device search**: This is especially important at protests. Law enforcement may claim that your phone photos or messages constitute evidence relevant to the action. You are not required to consent to device search without a warrant. Say: "I do not consent to a search of my device." A warrant can compel production, but consent produces it immediately without judicial oversight.

**Do not identify other participants**: You are not required to identify other protesters, describe who organized the action, or provide names of contacts. Anything you say about other participants can be used to expand an investigation beyond you. Say only your name (if legally required to identify yourself in your state) and then: "I am exercising my right to remain silent."

**Document before powering off**: If you have photos or video documenting police violence or misconduct, upload them to a trusted cloud service (a privacy-preserving service or a trusted contact's secure account) before powering off your device at the moment of anticipated detention. Once your phone is off and in BFU state (see `implementation-guide.md` and immigration playbook Part 4), that data is encrypted and Cellebrite cannot access it without your passphrase.

### 5.4 National Lawyers Guild Integration

The NLG is the primary legal support infrastructure for political activists in the United States. Its resources are specifically designed for protest and activist legal defense.

- **National Mass Defense Hotline**: (212) 679-2811 (for mass arrest situations)
- **Local chapters**: nlg.org/chapters/ — find your local chapter hotline before attending any action
- **Legal Observer request**: Contact your local chapter to request trained legal observers for planned actions. Legal observers wear distinctive green hats and are trained to document police-protester interactions without participating in the action.
- **Mass defense fund**: For large-scale arrests, NLG coordinates mass defense with legal representation and bail support
- **Know Your Rights training**: NLG chapters conduct training specifically for protest contexts — strongly recommended for organizers and first-time participants

Additional legal support resources:
- **ACLU**: aclu.org — The ACLU has filed suits challenging DHS subpoenas targeting anti-ICE accounts and provides know-your-rights resources
- **Electronic Frontier Foundation**: eff.org/know-your-rights — EFF's protest-specific know-your-rights guide
- **National Police Accountability Project**: nlg-npap.org — for civil rights claims arising from protest-related police misconduct

---

## Part 6: Implementation Path

### Tier 1: Essential (all participants in any public action — no exceptions)

These measures apply to any person attending a protest or public political action, regardless of how minimal their organizing role.

1. **Write the NLG hotline on your arm** (not your phone): Local chapter number or national: (212) 679-2811. This takes 30 seconds and costs nothing.
2. **Disable phone location services** for all apps before leaving home. iOS: Settings > Privacy > Location Services > Off. Android: Settings > Location > Off. Do this the night before the action.
3. **Set social media to private** at least 72 hours before the action. Review and archive recent posts identifying location or organizing activity.
4. **Designate an outside contact** and confirm the check-in time and escalation protocol before leaving home.
5. **Know your rights**: Read EFF's protest rights guide (eff.org/know-your-rights) before attending. The 5 minutes is worth it.
6. **Wear generic, non-distinctive outer clothing**: Dark or neutral tones, no logos, no bright colors. This is the single most effective aerial surveillance countermeasure available to an individual at no cost.

**Time to implement**: 2 hours (social media audit + know-your-rights reading + outside contact setup)

### Tier 2: Intermediate (regular protest participants, event coordinators, anyone with a public organizing role)

All of Tier 1, plus:

7. **Face + hat + sunglasses**: Carry an N95 or FFP2 mask, a brimmed hat, and sunglasses to every action. Wearing them together is the relevant countermeasure — any single element alone is significantly less effective.
8. **Power off your phone before entering the protest perimeter**: Leave it powered off and in a Faraday bag. Use a dedicated burner device if you need a phone for the action (prepaid, cash-purchased, no identity link).
9. **Vehicle de-correlation**: Do not drive your own vehicle to protest sites. Use transit, carpool in a friend's vehicle, or use a rideshare with pickup/dropoff at least 4–6 blocks away.
10. **Clothing change protocol**: Bring a change of at least one outer layer (a packable layer, hat swap) to change before leaving the protest area.
11. **Signal hygiene for organizing groups**: Enable disappearing messages (24 hours) in all organizing Signal groups. Do not use public platforms for operational coordination.
12. **Data broker opt-outs**: If you have not already: complete LexisNexis Accurint opt-out (optout.lexisnexis.com). If California resident, complete the DROP platform (privacy.ca.gov/drop). Details in immigration playbook Part 2.

**Time to implement**: 6–8 hours (Signal configuration, data broker opt-outs, purchasing burner device and Faraday bag)

**Equipment cost**: N95 masks ($15–$25 for a box of 20), Faraday bag ($20–$80), prepaid phone ($25–$50 for a basic burner). Total Tier 2 equipment: under $150.

### Tier 3: Advanced (lead organizers, people with public profiles, those who have received DHS administrative subpoenas or believe they are active investigation targets)

All of Tier 2, plus:

13. **GrapheneOS on a dedicated protest device**: The device used for communication during actions should run GrapheneOS (grapheneos.org) with auto-reboot set to 18 hours and the wipe passphrase configured. Details in `implementation-guide.md` and immigration playbook Part 4.
14. **Account separation architecture**: Organizational public accounts should be operated from a device with no connection to your personal identity. Separate email (registered through Tor), separate phone number (VoIP service registered through Tor), separate IP (Mullvad VPN or Tor). Instructions in `opsec-playbook.md` Part 1.
15. **Legal consultation before public-facing activity**: If you are a visa holder, DACA recipient, or non-citizen in any immigration status, consult with immigration counsel before making public statements at protests or posting protest-related content. Catch and Revoke enforcement is documented.
16. **Provenance documentation for public statements**: For lead organizers who speak at events or appear in media: establish a documentation practice for recorded public statements. Keep original video files with timestamp metadata and share them with legal contacts immediately after recording. This creates an authentic record against which deepfake fabrications can be compared.
17. **Incogni subscription**: $7.99/month (via Surfshark) for automated quarterly data broker re-submissions, covering 420+ brokers. This automates the ongoing maintenance work from Step 12.

**Time to implement**: 20–30 hours (GrapheneOS installation is the time-intensive step; legal consultation scheduling varies)

---

## Part 7: FAQ for Organizers and Legal Advocates

**Q: If I use Signal for organizing, is that enough to protect my communications?**

No, for two reasons. First, Signal's end-to-end encryption protects message content in transit, but messages stored on a device are accessible via Cellebrite forensic extraction if the device is in AFU (After First Unlock) state. If your phone is seized at a protest, power it off before surrendering it — BFU state significantly limits what Cellebrite can extract. Second, Signal does not protect metadata: your carrier can confirm when you sent data to Signal's servers, and that data is accessible via NSL. Signal protects what you say, not when or how often you communicate.

**Q: Is it legal to wear a mask at a protest?**

In most US jurisdictions, yes. "Anti-mask" laws historically applied to Ku Klux Klan-type activities and were narrow in scope; wearing an N95 for health or privacy reasons at a protest is generally protected expression. However, laws vary by state and municipality. Check your local jurisdiction before the action. This is also something your NLG chapter or a legal observer briefing can address.

**Q: The protest I'm planning is entirely lawful. Do I really need these countermeasures?**

The documented surveillance deployments (LAPD drones, Flock Safety ALPR queries, Babel Street monitoring) were applied to entirely lawful protests — No Kings, Hands Off, 50501. The surveillance does not require illegal activity to be deployed; it is routinely applied to constitutionally protected assembly. Whether the information collected is subsequently used depends on enforcement priorities that can change. Countermeasures applied now create a baseline of privacy that does not depend on correctly predicting future enforcement priorities.

**Q: As a legal observer, what do I need to do differently?**

Legal observers who document police-protester interactions are themselves documented by the same surveillance systems. Apply Tier 2 measures for your own protection. Additionally: all documentation you collect (photos, video, notes) should be transmitted to secure NLG storage as quickly as possible after the action, before your phone could be seized. NLG can advise on their current preferred secure transmission method. Do not store documentation only on your primary device.

**Q: What should I tell a non-technical organizer who won't read a long guide?**

Five things: write the NLG number on your arm, wear a mask and hat, turn off your phone before the protest, don't drive your own car, and check in with someone after. These five measures address the four highest-impact surveillance layers at near-zero cost and require no technical knowledge to implement.

**Q: Our organization has a public social media presence we need for organizing. How do we protect the people who run it?**

Separate the operator's identity from the account. The account-running device should have no personal identity link to the person operating it: a dedicated email registered through Tor, a VoIP phone number not linked to their carrier account, a device that has never been signed into personal accounts. The person's legal name should never appear in account recovery options, billing records, or two-factor authentication setup for that account. This does not defeat a subpoena to the platform (platforms hold IP records and account metadata that can narrow identity), but it defeats passive OSINT and substantially raises the barrier for targeted account unmasking.

---

## Resource Directory

### Legal Support
- **National Lawyers Guild — Mass Defense Hotline**: (212) 679-2811 | nlg.org/massdefenseprogram/
- **NLG Legal Observer Program**: nlg.org/massdefenseprogram/los/ (request observers for your action)
- **NLG Chapter Hotlines**: nlg.org/chapters/ (find local hotline before the action)
- **ACLU Know Your Rights at Protests**: aclu.org/know-your-rights/protesters-rights
- **EFF Protest Guide**: eff.org/know-your-rights
- **National Police Accountability Project**: nlg-npap.org

### Security Tools
- **Signal**: signal.org (encrypted messaging — configure disappearing messages)
- **GrapheneOS**: grapheneos.org (hardened mobile OS for dedicated protest device)
- **Mullvad VPN**: mullvad.net (no-logs VPN for account separation architecture)
- **Tor Browser**: torproject.org (for registering separated accounts, anonymous browsing)
- **Briar**: briarproject.org (Tor-routed mesh messenger, no phone number required)
- **Faraday bags**: Mission Darkness (mosequipment.com) or Silent Pocket (silentpocket.com)

### Surveillance Monitoring
- **ADS-B Exchange**: adsbexchange.com (track active drone/aircraft flights over protest areas)
- **DeFlock.me**: deflock.me (map of known Flock Safety ALPR camera locations — EFF-supported)

### Research and Reporting
- **EFF — Flock Safety protest surveillance investigation**: eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/
- **Amnesty International — Babel Street protest surveillance**: amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/
- **The Intercept — LAPD drone surveillance No Kings**: theintercept.com/2026/04/20/lapd-skydio-drone-surveillance-no-kings-protest-ice/
- **Biometric Update — ICE FBI facial recognition at protests**: biometricupdate.com/202602/ice-fbi-expand-facial-recognition-use-to-protest-investigations

---

## Summary Checklist

**Tier 1 — Everyone at any action**:
- [ ] NLG hotline written on arm (not stored in phone)
- [ ] Phone location services off
- [ ] Social media set to private 72 hours before action
- [ ] Outside contact designated with check-in time
- [ ] EFF protest rights guide read
- [ ] Generic, non-distinctive clothing (dark/neutral, no logos)

**Tier 2 — Regular participants and event coordinators**:
- [ ] N95/FFP2 mask, brimmed hat, sunglasses — brought to every action
- [ ] Phone powered off and in Faraday bag at protest perimeter
- [ ] Burner device purchased for in-action communication if needed
- [ ] No personal vehicle at protest site (transit, carpool, or rideshare 4–6 blocks away)
- [ ] Change of outer layer to switch before leaving protest area
- [ ] Disappearing messages enabled in all organizing Signal groups
- [ ] LexisNexis Accurint opt-out completed

**Tier 3 — Lead organizers and active investigation targets**:
- [ ] GrapheneOS on dedicated protest device with auto-reboot configured
- [ ] Organizational public accounts separated from personal identity
- [ ] Immigration counsel consulted (if applicable)
- [ ] Provenance documentation practice established for public statements
- [ ] Incogni subscription active for automated data broker maintenance

---

**For questions or updates**: Contact your local NLG chapter or the EFF digital rights helpline (eff.org/help).

**Version**: 1.0
**Last updated**: May 6, 2026
**Next review**: July 26, 2026 (aligned with corpus quarterly review)
**Cross-references**: threat-model.md, opsec-playbook.md, implementation-guide.md, palantir-threat-model.md, immigration-surveillance-evasion-playbook.md, PHASE_2_SEQUENCING_STRATEGY.md Sections 1.2, 1.3, 3.3
