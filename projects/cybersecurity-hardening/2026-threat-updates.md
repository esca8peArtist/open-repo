---
title: "2026 Threat Model Updates: April–May Developments"
project: cybersecurity-hardening
created: 2026-04-29
status: complete
purpose: Structured threat model update covering four new attack vectors, updated procurement guidance, and refreshed threat matrix for integration into Tier 1/2/3 distribution prep and Phase 2 guide updates
confidence: high — primary and near-primary sources throughout; FISA legislative status as of April 29 (vote scheduled May 1, outcome pending)
depends_on: threat-model.md, hardware-procurement-guide.md, opsec-playbook.md, 2026-threat-landscape-research.md
---

# 2026 Threat Model Updates: April–May Developments

**Bottom line up front**: Four new or materially changed threat vectors have emerged in April–May 2026 that require threat model updates before Tier 2 and Tier 3 distribution. The most operationally urgent is the software supply chain Shai-Hulud campaign (npm/PyPI/GitHub Actions), which directly affects recommended tools. The most structurally significant is the FISA 702 reauthorization fight, which is resolving — regardless of legislative outcome — in the direction that confirms warrantless backdoor searches remain operational through at least 2027. AI deepfake capabilities have crossed a threshold where voice-only verification is no longer reliable for high-risk individuals. And the DOJ voter database consolidation adds a new cross-reference vector that is specifically acute for election protection activists in compliant states.

---

## Part I: Four New Threat Vectors with April–May 2026 Sourcing

### Threat Vector 1: FISA Section 702 — Confirmed Warrantless Access Remains Operational

**What changed**: Section 702 expired April 20, 2026. Congress passed a 10-day stopgap to April 30 after two failed long-term reauthorization attempts (an 18-month and a 5-year extension both fell to a GOP revolt demanding warrant requirements). Speaker Johnson teed a three-year clean extension for a May 1 House floor vote via suspension of rules (requiring a two-thirds supermajority). As of April 29, Johnson did not have the votes. Separately, the Foreign Intelligence Surveillance Court extended operational authority for existing certifications through 2027 regardless of any legislative lapse.

**The critical detail**: All three legislative proposals in play — the 18-month extension (failed), the 5-year extension (failed), and the pending 3-year version — explicitly declined to add a warrant requirement for FBI "backdoor searches" of Americans' communications incidentally collected under 702. The reform coalition demanding a warrant requirement (Senators Wyden, Lee, and House members Davidson and Lofgren) lost. Whether 702 is extended for three years or lapses temporarily, the FISC extension means the surveillance apparatus continues operating, and when any extension passes, it will confirm warrantless database queries.

**Threat model implication**: This is not a change in adversary capability — it is a confirmation that no legislative check was added. The backdoor search authority documented in the existing threat-model.md under NSA/SIGINT remains fully operational. FBI can query the 702 database for Americans' communications using identifiers (email, phone, social media handle) without a warrant as long as there is any articulable "foreign intelligence purpose" — a very low bar confirmed by the FISC.

**Documented abuses now confirmed in the legislative record**: During the reauthorization debate, senators cited confirmed FBI warrantless queries of BLM protestors' communications, U.S. officials, journalists, and 19,000 donors to a congressional campaign. These abuses appeared in the Congressional Record in April 2026 without prompting any legislative correction.

**What this means for encrypted messaging users**: Signal remains the primary countermeasure. The Signal Foundation has produced message content in response to exactly zero government requests — because it cannot. End-to-end encryption defeats 702 legal process at the content layer. What 702 can still collect: the fact that you use Signal (carrier-visible), when you use it, and how often. Metadata is not protected by E2EE.

Sources: [Spectrum News, April 27](https://spectrumlocalnews.com/us/snplus/politics/2026/04/27/fisa-section-702-house-vote); [American Prospect, April 28](https://prospect.org/2026/04/28/implausible-deniability-fisa-section-702-congress-himes/); [EFF, April 2026](https://www.eff.org/deeplinks/2026/04/congress-must-reject-new-insufficient-702-reauthorization-bill); [Brennan Center 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page); [Just Security analysis](https://www.justsecurity.org/137206/johnson-section-702-warrant/)

---

### Threat Vector 2: AI Deepfakes and Synthetic Identity — Voice Verification Is No Longer Reliable

**What changed**: Two threshold events occurred in early 2026. First, the World Economic Forum's Cybercrime Atlas (January 8, 2026) tested 17 face-swapping tools and eight camera injection tools against live KYC biometric verification systems and found that moderate-quality face swaps combined with camera injection defeat a wide range of active liveness implementations. Second, voice cloning quality crossed what researchers call the "indistinguishable threshold" — consumer tools can produce synthetic voices indistinguishable from real ones from a 30-second sample, and the perceptual tells that previously gave away synthetic audio have largely disappeared.

**The 2026 election deepfake escalation**: The 2026 U.S. midterm cycle is documented as the first electoral cycle where political deepfakes are deployed at industrial scale. Reporters Without Borders documented 100 journalists targeted by deepfakes in 27 countries between December 2023 and December 2025, with 74% of cases targeting women. Specific operational precedent: Cristina Caicedo Smit of Voice of America discovered fabricated videos in February 2025 replicating her voice and image to manufacture incriminating statements.

**Why this matters for activists**: Fabricated audio and video is now a documented harassment and discrediting tactic for activists and journalists. The threat is bidirectional:

- *Inbound*: A caller or video conference participant claiming to be a trusted contact, attorney, or colleague may not be that person. This is not a speculative risk — voice-cloning services are commercially available, require no special technical skill, and can be obtained for under $50/month.
- *Outbound*: Fabricated media purporting to show an activist making incriminating, damaging, or embarrassing statements can be created by adversaries and used for harassment campaigns, social pressure, government referrals, or evidence fabrication. This is a documented operational tactic of state-aligned threat actors and domestic right-wing harassment operations.

**What the WEF report found about authentication failure**: Passive liveness checks — the most common biometric verification layer — can only confirm a frame looks like a human face. They cannot separate real faces from realistic synthetic overlays. Camera injection (feeding a pre-recorded deepfake into the video stream rather than the actual camera) bypasses active liveness implementations in a wide range of tested systems. This means that even a "live" video call cannot be treated as reliable identity verification.

Sources: [WEF Cybercrime Atlas 2026 Report](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf); [Fortune: Deepfake outlook 2026](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/); [RSF deepfake journalist targeting analysis](https://rsf.org/en/rsf-analysis-100-deepfakes-shows-mounting-threat-journalists-especially-women); [CSIS: Crossing the Deepfake Rubicon](https://www.csis.org/analysis/crossing-deepfake-rubicon); [WEF: Cognitive manipulation and AI disinformation 2026](https://www.weforum.org/stories/2026/03/how-cognitive-manipulation-and-ai-will-shape-disinformation-in-2026/)

---

### Threat Vector 3: Software Supply Chain — The Shai-Hulud Campaign and the 48-Hour Package Ecosystem Collapse

**What changed**: The April 21–23, 2026 window saw three coordinated supply chain attacks across npm, PyPI, and Docker Hub — all targeting developer secrets. This was not opportunistic. It was systematic. The campaign is now attributed to a threat actor group (TeamPCP / "Shai-Hulud") operating across multiple ecosystems simultaneously.

**Confirmed April 2026 compromises**:

1. **Bitwarden CLI** (`@bitwarden/cli@2026.4.0`), April 22, 5:57–7:30 PM ET: Trojanized via compromise of Checkmarx GitHub Action in Bitwarden's CI/CD pipeline. The malicious version exfiltrated cloud credentials (AWS, Azure, GCP), GitHub PATs, npm publish tokens, SSH keys, and shell history. Attack vector: upstream dependency compromise, not a breach of Bitwarden itself. ~250,000 downloads/month means the 90-minute exposure window reached a significant install base.

2. **Checkmarx KICS Docker images and VS Code extensions**: Obfuscated payload harvested GitHub auth tokens, AWS credentials, Azure and Google Cloud tokens, npm config files, SSH keys, and environment variables.

3. **CanisterSprawl self-propagating worm** (npm, April 21): Started in `pgserve` (a PostgreSQL Node.js package). Installs a credential-harvesting script via `postinstall` hook, searches for npm publish tokens, then bumps patch version and self-publishes to every package the victim maintainer can publish. If a PyPI token is found, it jumps ecosystems. This is the first self-propagating npm supply chain worm documented at scale in 2026.

4. **xinference** (PyPI, April 22): Three consecutive releases carrying credential-stealing payloads.

5. **Axios HTTP client** (npm, March 31): The most-downloaded HTTP client library used as malware delivery vehicle for ~3 hours after maintainer account hijack. RAT inserted. Attributed to North Korean actor UNC1069.

6. **prt-scan GitHub Actions campaign** (March 11–ongoing): AI-powered campaign exploiting `pull_request_target` misconfiguration. As of disclosure in early April, over 500 malicious PRs opened across open source repositories. Verified credential theft of AWS keys, Cloudflare API tokens, and Netlify auth tokens. Notably, the attacker's payloads used AI to generate language-appropriate, idiomatic code — Go test files, pytest conftest patterns, npm script hooks — that match each target repository's conventions. This represents agentic attacker tooling operating at machine speed.

**The broader pattern**: These attacks share a structural feature: they don't breach Bitwarden, Trivy, or Axios directly. They compromise an upstream build tool, a CI/CD action, or a maintainer's credentials, and inject into a trusted artifact during the build pipeline. The resulting malicious package carries the original project's reputation and signing chain.

**What this means for guide populations**: Non-developers (Tier 1 and Tier 2 users installing Bitwarden via the official website, the macOS/Windows app installer, or app stores) were not affected by the CLI compromise. The CLI is installed exclusively via npm. This distinction matters and must appear in the guides.

Sources: [The Hacker News: Bitwarden CLI](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html); [Endor Labs analysis](https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack); [GitGuardian: 48-hour campaign](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/); [The Hacker News: CanisterSprawl worm](https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html); [Wiz: prt-scan campaign](https://www.wiz.io/blog/six-accounts-one-actor-inside-the-prt-scan-supply-chain-campaign); [The Register: Trivy and Axios](https://www.theregister.com/2026/04/11/trivy_axios_supply_chain_attacks/); [The Register: Ongoing Shai-Hulud campaign](https://www.theregister.com/2026/04/27/supply_chain_campaign_targets_security/)

---

### Threat Vector 4: Election Protection — DOJ Voter Database Cross-Reference and the CISA Coverage Gap

**What changed**: Two structural changes in April 2026 are directly relevant to election protection activists.

**Change A — DOJ Federal Voter Database**: For the first time in American history, the DOJ demanded non-public voter registration records from all 50 states and Washington D.C. to compile a single national record system, cross-referenced with DHS's SAVE citizenship verification database. The data includes driver's license numbers and partial Social Security numbers. At least 12 states have voluntarily complied. The DOJ's privacy officer resigned in protest. An ACLU coalition lawsuit is pending.

The threat model implication is specific: voter registration records in compliant states now flow into the same DHS/DOJ data integration environment as immigration enforcement databases. A person who is both registered to vote and appears in immigration records is now cross-referenceable by a single analyst query. For naturalized citizens, this creates false-positive risk in citizenship verification — the SAVE database has documented accuracy problems, and a mismatch can trigger an adverse action before any human review occurs.

**Change B — CISA Election Security Coverage Gap**: CISA lost 14 positions and $40 million in election security capacity in April 2026. The FY27 budget proposes eliminating the election security program entirely. The EI-ISAC (Elections Infrastructure Information Sharing and Analysis Center) — which provided threat intelligence and incident response to state and local election offices — has lost federal funding support. In a survey of election officials, 75% report insufficient resources to fill the gap, and 38% report having been personally harassed or threatened.

The practical implication for election protection activists: the coordinating infrastructure that previously provided rapid threat intelligence to election workers has been largely dismantled. Threats to digital election infrastructure (DDoS against county websites, disinformation about polling locations, targeted phishing of election officials) will now be responded to by state and local offices with reduced federal support. Election workers who previously relied on CISA advisories and EI-ISAC alerts now need alternative threat intelligence sources.

**Change C — ICE at Polling Places (legal confirmed, operational risk remains)**: DHS formally told state election chiefs that ICE will not be deployed to polling places in 2026. The Brennan Center's legal analysis confirms federal law prohibits this. However, the statement was carefully worded — ICE retains authority if there is an "active public safety threat" at a polling location, and Senate Republicans have stated deployment remains possible given sufficient predication. Arizona considered requiring counties to sign ICE cooperation agreements for polling place presence. The threat of ICE presence — whether or not it materializes — produces voter suppression effects through fear in immigrant communities.

Sources: [NPR: DOJ voter data](https://www.npr.org/2026/03/27/nx-s1-5764266/voter-data-trump-doj-dhs); [Protect Democracy: Voter database](https://protectdemocracy.org/work/voting-rights-doj-national-voter-database/); [ACLU lawsuit](https://www.aclu.org/press-releases/voting-rights-groups-sue-doj-to-block-national-voter-surveil-and-purge-database); [Nextgov: Federal election support drawdown](https://www.nextgov.com/cybersecurity/2026/04/federal-drawdown-election-support-destroyed-ongoing-relationships-experts-say/413181/); [Brennan Center: ICE at polls](https://www.brennancenter.org/our-work/research-reports/sending-ice-polling-places-illegal); [Stateline: Blue states ban ICE at polls](https://stateline.org/2026/03/05/blue-states-push-to-ban-ice-at-the-polls-amid-federal-voter-intimidation-fears/)

---

## Part II: Updated Threat Model Implications

### A. Encrypted Messaging

**No change to primary recommendation** (Signal with disappearing messages). The new FISA developments confirm, rather than expand, the existing threat model.

**What is now explicit that was implicit**:
- The FISC's 2027 extension means warrantless backdoor search authority persists regardless of legislative lapse. Even a formal expiration of Section 702 does not disable existing surveillance certifications. Users should not change their threat model based on any legislative news about 702.
- iCloud Advanced Data Protection is confirmed correct for Apple users: Apple cannot comply with 702 legal process targeting ADP-protected data because it holds no decryption keys.
- Gmail, Outlook, and WhatsApp (Meta infrastructure) remain unsuitable for sensitive communications. They are compelled cooperators under 702.

**New addition**: AI-generated spear-phishing now achieves click-through rates four times higher than human-crafted equivalents. A message appearing to come from a trusted contact, correctly referencing real case details, is no longer a signal of legitimate origin. The encrypted channel does not protect against a user being socially engineered into disclosing information or credentials outside of it.

### B. Device Hardening

**No change to hardware recommendations**. GrapheneOS, iOS with Lockdown Mode, and the hardened configurations in device-hardening-guide.md address the surveillance capabilities documented here.

**New supply chain addition**: The prt-scan and Shai-Hulud campaigns establish that software tools recommended in the guides (Bitwarden, security scanners, developer utilities) can be compromised via upstream CI/CD pipeline attacks that the end user cannot detect. This requires a new verification practice:

- Install Bitwarden via official website installers or app stores, never via `npm install`.
- For any security-critical software, verify cryptographic signatures before installation (the guides already recommend this for OS images; it now extends to all security tools).
- If a developer tool was updated on April 21–23, 2026, treat it as potentially compromised until independently verified. Rotate any credentials that may have been accessible to tools updated in that window.

### C. Operational Security

**AI social engineering additions required**:

1. **Out-of-band verification is mandatory for high-stakes requests.** Any unexpected request for credentials, location disclosure, fund transfer, or meeting — regardless of how convincingly it appears to originate from a trusted contact — must be verified via a pre-established second channel. If someone calls claiming to be your attorney, hang up and call the attorney's published number. If an email requests you log in anywhere, navigate directly to the site.

2. **Code words for unexpected voice and video contact.** For Tier 2 and Tier 3 individuals, establish a pre-agreed verification phrase with key trusted contacts (attorney, organizational security contact, emergency contact). Any unexpected call requesting sensitive action should trigger this challenge. This is a proportionate practice used by security professionals for exactly this threat.

3. **Video call identity verification is no longer reliable.** The WEF's January 2026 testing confirmed that camera injection attacks defeat liveness checks across a wide range of commercial systems. A video call from someone appearing to be a trusted colleague is not a verification method. For Tier 3, voice-only Signal calls on hardened devices remain the correct high-sensitivity communication channel.

4. **Synthetic evidence response protocol.** Activists should be prepared to receive fabricated audio or video purporting to show them making incriminating statements. Establish in advance: document (preserve the fabrication with metadata), do not respond publicly before legal consultation, report to EFF's digital security helpline or a trusted legal contact. Do not engage directly with harassment operations.

**Election-specific additions**:
- Any election worker or observer in a state that has provided voter data to the DOJ voter database project should consult an immigration attorney before any 2026 election activity that creates proximity to federal authorities, if they have any immigration status considerations.
- Know the Brennan Center's "Sending ICE to Polling Places Is Illegal" brief by title and have the URL available. ([Brennan Center](https://www.brennancenter.org/our-work/research-reports/sending-ice-polling-places-illegal))
- With CISA's EI-ISAC no longer providing threat intelligence to local election offices, election protection organizations should identify alternative threat intelligence resources: State Election Assistance Commission contacts, nonpartisan election security nonprofits (Defending Digital Democracy, Center for Democracy and Technology, Stanford Internet Observatory).

### D. Identity Compartmentalization

**DOJ voter database adds new cross-reference surface**: Voter registration in compliant states is now linked to the DHS/DOJ data environment. For individuals with immigration status considerations, voter registration is no longer a completely siloed data point — it is now a cross-reference into the same environment as immigration enforcement databases. Data minimization recommendation: individuals with status concerns should seek legal guidance before voter registration or registration updates in states that have complied with the DOJ demand.

**Deepfake threat to pseudonymous identities**: AI scraping of public content can construct voice profiles and potentially visual profiles from publicly available materials. For activists maintaining pseudonymous public identities, this means that any public audio or video appearance (podcast, livestream, video interview) provides raw material for voice cloning. Pseudonymous activists should assume their voice is clonable from any public content and should build verification practices accordingly (never rely on voice recognition alone for trusted-contact authentication).

---

## Part III: Hardware and Software Procurement Guidance — 2026 Status

### Hardware Tier Recommendations (No Material Changes)

The existing hardware-procurement-guide.md vendor assessment remains accurate as of April 2026. No critical supply chain compromises, firmware backdoor discoveries, or vendor security incidents affect the recommendations.

**Tier 1 (Threat: data pipelines, OSINT, low-probability targeted action)**
- Any modern laptop with full-disk encryption enabled and a non-default OS install
- Chromebook with verified boot is a reasonable choice for users who will not deviate from the guide setup
- Smartphone: iPhone with ADP enabled, or Pixel 8+ with GrapheneOS

**Tier 2 (Threat: IMSI catchers, device seizure, possible targeted firmware)**
- Framework Laptop 13/16: Best repairability, component verification, no known 2026 security incidents; strong choice
- System76: Coreboot on Intel hardware is mature; AMD Coreboot support still pending; no 2026 incidents
- Smartphone: Pixel 8 or newer with GrapheneOS — nonnegotiable for Tier 2+
- Avoid Lenovo hardware: UEFI backdoor history (SuperFish 2015, LSE 2015, UEFI driver 2022) makes it unsuitable even for Tier 2

**Tier 3 (Threat: Targeted supply chain interdiction, active investigation, confirmed intelligence interest)**
- Purism Librem 14: Open-source embedded controller (Librem-EC), Coreboot, Intel ME disabled, physical kill switches; automated firmware update delivery still incomplete as of April 2026 — verify manually
- Nitrokey-certified ThinkPads for Qubes OS: Best-validated compatibility combination as of 2026
- Procurement hygiene: Purchase from manufacturer directly or established domestic reseller; use a false delivery address or business address for high-risk procurement; inspect device for physical tampering before first use
- Smartphone: GrapheneOS on Pixel 8/9 with network hardening enabled

**Hardware status note (April 2026)**: No new security advisories for Purism, System76, or Framework as of the research date. The existing guide's analysis of Intel ME, AMD PSP, and UEFI risks remains current.

### Software Password Manager — Updated Guidance

**The Bitwarden April 22 incident changes the installation guidance, not the tool recommendation**:

- Bitwarden desktop application (downloaded from bitwarden.com) and browser extension (installed from official browser extension stores): NOT affected by the April 22 npm compromise
- Bitwarden iOS/Android apps (installed from App Store/Google Play): NOT affected
- Bitwarden CLI installed via `npm install @bitwarden/cli`: AFFECTED if installed/updated during 5:57–7:30 PM ET on April 22, 2026

**Action for affected users**: If you installed or updated `@bitwarden/cli` via npm during the window above, assume credentials may have been exfiltrated. Rotate: all cloud provider tokens (AWS, Azure, GCP), GitHub PATs, npm publish tokens, SSH keys, and any credentials accessible in shell history or environment variables.

**General principle added**: For any security-critical tool, prefer official website/app store installers over package manager installation unless you can verify the package against a cryptographic signature from a trusted key. Package managers (npm, pip, pip3, cargo) are now confirmed attack surfaces. This does not mean avoiding them for general use, but it means security tooling should be installed via verified channels.

**KeePassXC remains the Tier 3 alternative**: Local-only, no cloud sync, no npm delivery. For users who want zero cloud exposure for passwords, KeePassXC on an airgapped or heavily firewalled machine remains correct.

---

## Part IV: Updated Threat Matrix

The following matrix extends and updates the matrix in threat-model.md. New or materially changed entries are marked **[NEW 2026]** or **[UPDATED 2026]**.

| Threat Actor | Capability | Likelihood (for guide populations) | Impact | Countermeasure |
|---|---|---|---|---|
| NSA/FBI (702 backdoor search) | Warrantless query of 702 database for Americans' communications | High — confirmed authority, confirmed abuses | High — message content accessible if using Gmail/iCloud/Outlook | Signal E2EE; iCloud ADP; avoid cloud-provider email for sensitive comms |
| FBI (NSL) | Metadata subpoena, no judicial approval | Medium — low threshold, widely used | Medium — who you contact, when, carrier-level timing | Signal minimizes metadata retention; carrier-level metadata not addressable by apps |
| ICE/DHS (Palantir ELITE) | Address confidence scoring, database cross-reference | High for undocumented; Medium for advocates | High — location targeting, dossier construction | Device hardening; no personal apps on dedicated work devices; data broker opt-out |
| ICE (ad tech MAID procurement) | Location data from mobile advertising identifiers | High — ICE RFI issued Jan 2026 | High — precise location history without warrant | GrapheneOS/iOS hardening removes advertising identifier; guide already addresses this |
| DOJ (voter database) **[NEW 2026]** | Cross-reference voter registration with DHS/immigration databases | High in compliant states | High for naturalized citizens and anyone with status considerations | Legal consultation before registration; understand which states complied |
| AI-enabled social engineering (any actor) **[NEW 2026]** | Voice cloning, deepfake video, synthetic spear-phishing | High — commercially available tools, no technical barrier | High — credential theft, location disclosure, evidence fabrication | Out-of-band verification; code words; no video-call-only identity verification |
| Software supply chain (state + criminal actors) **[UPDATED 2026]** | CI/CD pipeline compromise, npm/PyPI package trojanization | High for developers; Medium for non-technical users of affected tools | High — credential exfiltration, persistent access | Official installer channels; signature verification; rotate credentials after exposure window |
| GitHub Actions campaigns (prt-scan) **[NEW 2026]** | AI-generated malicious PRs targeting repository secrets | High for open source maintainers; Low for end users | High for developers — AWS, Cloudflare, API token theft | Audit `pull_request_target` configurations; restrict fork execution scope |
| Clearview AI / ICE (facial recognition) | Biometric matching against ~billions of scraped images | High in urban areas with CCTV; high at public events | High — identity deanonymization at checkpoints, protests | Avoid photo exposure; protest-specific face coverage legal in some jurisdictions |
| Cell-site simulators (ICE, FBI, U.S. Marshals) | IMSI-based location tracking; forces device to connect | Medium for targeted individuals; elevated at protests | High — real-time location, IMSI harvested | Airplane mode or Faraday bag during high-risk in-person activities |
| CISA coverage gap **[NEW 2026]** | Threat intelligence gap for election infrastructure | High for local election offices | Medium — slower incident response, less proactive threat intel | Alternative resources: DDC, CDT, Stanford Internet Observatory, state-level coordination |
| Fabricated synthetic media targeting activists **[NEW 2026]** | Deepfake audio/video creating false evidence | Medium — documented state-aligned and domestic right-wing use | High — reputation, legal exposure, physical safety | Response protocol established in advance; do not engage before legal consultation |

---

## Part V: Integration Notes for Phase 2 Distribution

**For Tier 1 distribution (journalists, immigration advocates, labor organizers)**:
- Add Bitwarden installation guidance note (official website/app store only)
- Add a brief AI social engineering paragraph (out-of-band verification, do not trust voice alone)
- No hardware changes required

**For Tier 2 distribution (activists, civil rights litigants, protest organizers)**:
- Add full AI social engineering section including code word practice
- Add Bitwarden CLI remediation note
- Add DOJ voter database cross-reference note (state-specific where possible)
- Add CISA coverage gap context for election-affiliated Tier 2 users
- No hardware changes required; GrapheneOS remains nonnegotiable for Tier 2+

**For Tier 3 distribution (direct investigation targets, national security sources, confirmed legal process)**:
- All Tier 2 additions apply
- Add explicit treatment of fabricated synthetic evidence as a documented risk (not speculative)
- Add deepfake threat to pseudonymous identities section
- Add GitHub Actions / developer tool compromise note for any Tier 3 individuals who are developers
- Hardware and OS configurations in the existing guide remain correct; no changes needed

**For election worker / election protection audiences**:
- Add DOJ voter database cross-reference threat
- Add CISA coverage gap and alternative resources
- Add ICE legal status at polling places (Brennan Center cite)
- Add data broker opt-out as standard precaution for election workers (cross-reference osint-data-broker-deepening.md)
- Add AI deepfake / disinformation response protocol specific to election integrity context

---

## Sources

- [Brennan Center: FISA 702 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page)
- [EFF: Congress Must Reject Insufficient 702 Reauthorization Bill](https://www.eff.org/deeplinks/2026/04/congress-must-reject-new-insufficient-702-reauthorization-bill)
- [Just Security: Johnson 702 warrant analysis](https://www.justsecurity.org/137206/johnson-section-702-warrant/)
- [Spectrum News: House vote set on FISA 702](https://spectrumlocalnews.com/us/snplus/politics/2026/04/27/fisa-section-702-house-vote)
- [American Prospect: FISA 702 bill implodes](https://prospect.org/2026/04/28/implausible-deniability-fisa-section-702-congress-himes/)
- [Nextgov: House readies FISA 702 vote without warrant](https://www.nextgov.com/policy/2026/04/house-readies-vote-renew-fisa-702-without-warrant-amendment/412856/)
- [NPR: What to know about Section 702](https://www.npr.org/2026/04/14/nx-s1-5768270/what-to-know-about-section-702-surveillance)
- [WEF: Deepfake identity verification report (January 2026)](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf)
- [Fortune: 2026 deepfake outlook](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/)
- [RSF: 100 journalists targeted by deepfakes analysis](https://rsf.org/en/rsf-analysis-100-deepfakes-shows-mounting-threat-journalists-especially-women)
- [CSIS: Crossing the Deepfake Rubicon](https://www.csis.org/analysis/crossing-deepfake-rubicon)
- [WEF: Cognitive manipulation and AI in disinformation 2026](https://www.weforum.org/stories/2026/03/how-cognitive-manipulation-and-ai-will-shape-disinformation-in-2026/)
- [MSSP Alert: Deepfakes and AI agents in 2026](https://www.msspalert.com/news/deepfakes-ai-agents-will-expose-identities-to-more-threats-in-2026)
- [The Hacker News: Bitwarden CLI compromised](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html)
- [Endor Labs: Bitwarden CLI supply chain attack](https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack)
- [GitGuardian: 48-hour supply chain campaign](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/)
- [The Hacker News: CanisterSprawl self-propagating worm](https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html)
- [Wiz: prt-scan GitHub Actions campaign](https://www.wiz.io/blog/six-accounts-one-actor-inside-the-prt-scan-supply-chain-campaign)
- [SafeDep: prt-scan campaign analysis](https://safedep.io/prt-scan-github-actions-exfiltration-campaign/)
- [The Register: Trivy and Axios supply chain attacks](https://www.theregister.com/2026/04/11/trivy_axios_supply_chain_attacks/)
- [The Register: Ongoing Shai-Hulud supply chain campaign](https://www.theregister.com/2026/04/27/supply_chain_campaign_targets_security/)
- [Dark Reading: Supply chain worms 2026](https://www.darkreading.com/cyberattacks-data-breaches/supply-chain-worms-in-2026-what-shai-hulud-taught-attackers-and-how-to-prepare)
- [NPR: DOJ plans to share voter data with DHS](https://www.npr.org/2026/03/27/nx-s1-5764266/voter-data-trump-doj-dhs)
- [Protect Democracy: DOJ voter surveil-and-purge database](https://protectdemocracy.org/work/voting-rights-doj-national-voter-database/)
- [ACLU: Voting rights groups sue DOJ over voter database](https://www.aclu.org/press-releases/voting-rights-groups-sue-doj-to-block-national-voter-surveil-and-purge-database)
- [Nextgov: Federal drawdown of election support](https://www.nextgov.com/cybersecurity/2026/04/federal-drawdown-election-support-destroyed-ongoing-relationships-experts-say/413181/)
- [Brennan Center: Sending ICE to polling places is illegal](https://www.brennancenter.org/our-work/research-reports/sending-ice-polling-places-illegal)
- [Stateline: Blue states push to ban ICE at polls](https://stateline.org/2026/03/05/blue-states-push-to-ban-ice-at-the-polls-amid-federal-voter-intimidation-fears/)
