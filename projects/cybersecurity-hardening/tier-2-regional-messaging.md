---
title: "Tier 2 Regional Messaging — Five Jurisdiction-Specific Variants"
project: cybersecurity-hardening
created: 2026-04-30
status: research-complete
item: 28 — Tier 2 Regional Adaptation Framework
depends-on: palantir-threat-model.md, TIER2_DISTRIBUTION_PREP.md, TIER2_MESSAGING_TEMPLATES.md
---

# Tier 2 Regional Messaging: Five Jurisdiction-Specific Variants

**Lead finding**: The core Tier 1 corpus was designed around the US domestic ICE/Palantir threat. Each of the five international and specialized audience contexts below has a structurally different threat model — different adversary, different legal framework, different data exposure surface. Messaging that leads with Palantir-specific countermeasures will fail to land in most of these contexts. What succeeds is threat-first framing that meets each audience at their actual risk environment before pivoting to the shared countermeasures that generalize across jurisdictions.

The five audiences treated here are not mutually exclusive. An Iranian exile in Germany faces state-actor surveillance from Tehran AND operates under GDPR protections — they fall across the EU/GDPR and Authoritarian Exile categories simultaneously. The appropriate messaging is the one that opens at their most acute risk, then layers in adjacent considerations.

---

## Audience 1: US Domestic Populations and Asylum Seekers

### Threat Context

This audience faces the most documented threat model in the existing corpus. ICE's ELITE system, Palantir ImmigrationOS, CBP's biometric expansion program, and the DOGE cross-agency master database project are the primary threat vectors. However, asylum seekers face threat elements that the core corpus does not fully address:

**Biometric capture at the border is now near-universal.** CBP finalized a rule in November 2025, effective December 2025, authorizing facial biometric data collection from all noncitizens at airports, land borders, seaports, and other points of departure — eliminating prior exemptions. The CBP One application required asylum seekers to submit facial images, geolocation data, passport numbers, and family member names before even reaching the border. This pre-arrival biometric capture means that the threat for asylum seekers begins before they enter US territory — the data exists in US government systems before any ELITE query is run. Biometric data collected by one agency is frequently shared across agencies through interagency systems.

**Metadata minimization is the relevant protection layer for this population.** Once biometric data is captured at a border crossing or through CBP One, it cannot be un-captured. The countermeasures that remain effective are forward-looking: preventing *new* commercial data from entering the broker ecosystem that ELITE queries, protecting associational networks from being mapped through phone contact and location co-presence, and limiting social media exposure that feeds ImmigrationOS's OSINT component.

**The commercial data pipeline is the most actionable gap.** An asylum seeker who has been through CBP processing cannot remove their biometrics from DHS systems. But they can remove themselves from commercial data broker databases that ELITE queries independently of biometric data — Medicaid records, utility bills, DMV records, and the commercial location data derived from smartphone apps. Part 0 of the core corpus (data broker opt-outs) is directly applicable and actionable without technical expertise.

### Messaging Framework

**Opening frame** (what they already know): ICE is using data from smartphones, Medicaid, and driver's licenses to find and deport people. This is documented and confirmed.

**Extension** (what they may not know): The same data pipeline also affects asylum seekers in the process of establishing legal status. CBP has already captured your biometrics if you crossed at an official port of entry. But your smartphone is still generating location data that commercial brokers are selling to ICE through systems separate from your biometric file. Stopping that flow is still possible.

**Actionable steps specific to this population**:
1. Data broker opt-outs immediately — the California DELETE Act DROP platform is specifically documented in the corpus as accessible without government-issued ID, which matters for populations who may not have US identity documents
2. Compartmentalize smartphone location data: disable advertising identifier, limit app location permissions, avoid location-sharing apps
3. Signal for all sensitive communications — this is the one confirmed gap in Palantir's capability; Signal message content is inaccessible even under legal process
4. Avoid Telegram: FBI and IC3 advisories confirm Iranian and Russian state actors are using Telegram as a delivery vehicle for malware; the platform is also not end-to-end encrypted by default. This is less directly relevant to ICE/ELITE but matters for mixed-threat populations
5. For family members in countries of origin: family relationship data is stored in ICM (ICE's case management system); contacts between diaspora members and relatives in hostile states can expose both sides

**Institutional partners for this audience**:
- National Immigration Law Center (NILC) — litigation and policy on data sharing practices
- Immigrant Defense Project — represents people in deportation proceedings
- Access Now Digital Security Helpline — provides 24/7 technical support in Spanish, Arabic, Russian, French, Portuguese
- Just Futures Law — won EFF's 2025 Award for Leading Immigration and Surveillance Litigation; specializes in data broker liability for immigration enforcement purposes

### Confidence Level: High
This audience is directly addressed by the core corpus. Messaging extensions here are additions to an already-documented threat model, not new constructions.

---

## Audience 2: EU/GDPR Populations

### Threat Context

The EU threat model differs from the US model in two structural ways: the primary threat is commercial data aggregation rather than direct government surveillance, and GDPR enforcement functions as an asymmetric defensive weapon that does not exist in the US context.

**The commercial data broker ecosystem is the primary EU threat.** Privacy International's sustained campaigns against Acxiom, Criteo, Equifax, Experian, Oracle, Quantcast, and Tapad document a data broker ecosystem that operates across EU borders despite GDPR restrictions. A GDPR-era investigation revealed that data brokers were openly selling detailed location histories of European Commission staff despite Europe's privacy laws, demonstrating that GDPR compliance does not equal GDPR protection in practice. Experian received a €2.7 million Dutch DPA fine in 2025 for violations; Criteo received a €40 million CNIL fine in 2023. These fines are evidence of violations that had already occurred across millions of profiles.

**Clearview AI is the EU analog to the US biometric threat.** Clearview has been fined in France, Italy, the Netherlands, and Austria — totaling over €95 million in European fines — for building a biometric database by scraping billions of images without consent. The UK Upper Tribunal confirmed in October 2025 that Clearview's operations are subject to GDPR even for private companies processing EU resident data for foreign state clients. However, enforcement of these fines against a US-based company with no EU assets or offices remains a documented open problem: EU data protection authorities cannot seize US assets or compel payment.

**GDPR as asymmetric defensive weapon.** Unlike the US domestic context, EU populations have enforceable legal rights that create genuine operational friction for surveillance actors:
- Article 17 right to erasure ("right to be forgotten"): controllers must erase data without undue delay, typically within one month
- Article 20 data portability: individuals can obtain and transfer their data
- Article 15 subject access rights: individuals can demand disclosure of what data an organization holds
- Supervisory authority complaints: filing complaints with national DPAs (CNIL in France, BfDI in Germany, AEPD in Spain) creates documented compliance obligations
- These rights apply to data brokers operating in the EU regardless of their home country

**Chat Control and EU encryption tensions.** The EU's proposed CSAR regulation (colloquially "Chat Control") would, in its contested form, require client-side scanning of encrypted messages before encryption — which privacy experts and security researchers characterize as functionally creating a backdoor in end-to-end encryption. As of April 2026, the European Parliament voted to block the mandatory-scanning version; the compromise under negotiation extends a temporary voluntary scanning regime until 2028. This creates a live tension in messaging: the corpus recommends Signal and other E2EE tools as protective measures, and this recommendation is currently consistent with EU law — but the regulatory environment is actively contested and could change.

**The EU threat is NOT primarily from government bulk surveillance.** Unlike the US domestic context, EU populations do not face mass warrantless data purchase by law enforcement as the primary threat. The adversary is more often commercial — data brokers building behavioral profiles for advertising, insurance, and credit purposes, with the secondary risk that these profiles are accessible to law enforcement through legal process. The GDPR enforcement gap (brokers violate, regulators act slowly, brokers continue operating during enforcement) is the structural problem.

### Messaging Framework

**Opening frame**: Your data is being collected and sold commercially despite GDPR protections, and enforcement consistently lags collection. Clearview scraped billions of EU photos for a facial recognition database — the fines came years after the collection. Experian's violations took years to result in enforcement. Your legal rights are real but enforcement is slow; the most reliable protection is limiting data exposure in the first place.

**Extension**: The GDPR gives you weapons the US doesn't have. Use them proactively — file subject access requests with data brokers to discover what they hold, then file erasure requests. File DPA complaints against companies that can't justify their processing basis. These actions create documented compliance obligations that have legal force even when enforcement is slow.

**Actionable steps specific to this population**:
1. Subject access requests to major data brokers operating in your country — document what they hold, then file erasure requests under Article 17
2. Use the GDPR's legitimate interest balancing test as a litmus: if a broker cannot articulate a legitimate interest that overrides your right to erasure, file a DPA complaint
3. For device security: device fingerprinting by advertisers is regulated under the ePrivacy Directive; clear browser fingerprinting data, use privacy-respecting browsers (Firefox with uBlock Origin, Tor Browser)
4. Signal for communications — EU law currently supports E2EE; the Chat Control negotiations make this politically contentious but the recommendation is legally sound as of April 2026
5. Check national DPA enforcement history before choosing service providers — DPAs vary significantly in enforcement vigor (Irish DPC has drawn criticism for slow enforcement of Big Tech; CNIL and BfDI are more aggressive)

**EU-specific institutional partners**:
- Access Now (European offices in Brussels and other cities) — digital rights advocacy and technical support
- Privacy International — sustained campaigns against data broker ecosystem
- European Data Protection Board (EDPB) — guidance documents on individual rights
- noyb (None of Your Business, Max Schrems) — files GDPR complaints systematically; a natural partner for the right-to-erasure angle
- CNIL (France), BfDI (Germany), AEPD (Spain) — national DPAs with active enforcement programs

### Confidence Level: High
GDPR enforcement landscape is well-documented through enforcement decisions and academic analysis. Chat Control status is current through April 2026.

---

## Audience 3: Canada and Five Eyes Context

### Threat Context

Canada's threat model is structurally distinct because it combines a relatively strong domestic privacy law tradition with deep integration into the Five Eyes intelligence-sharing network (FVEY) — a combination that creates a gap between the protections that Canadian law appears to offer and the intelligence access that partners (primarily the US NSA and GCHQ) actually have.

**PIPEDA and its replacement are weaker than they appear.** The Personal Information Protection and Electronic Documents Act (PIPEDA) governs private-sector data handling federally. Bill C-27 (which would have replaced PIPEDA with the Consumer Privacy Protection Act and an AI governance framework) died when Parliament prorogued in January 2025. As of April 2026, Canada is developing replacement legislation under Prime Minister Carney's government, with data sovereignty framing from November 2025 shaping the policy direction. Proposed penalties under the contemplated CPPA would be up to C$25 million or 5% of global gross revenue — GDPR-scale enforcement. Provincial laws in Quebec, British Columbia, and Alberta have been deemed "substantially similar" to PIPEDA and apply instead of the federal law within those provinces.

**Quebec's Law 25 (Bill 64) is the strongest provincial privacy protection.** Quebec's amendments to its privacy law, fully in force since September 2023, created the most GDPR-like regime in Canada: mandatory privacy impact assessments, data minimization requirements, privacy by design requirements, and right to erasure provisions. Québec residents have stronger practical protections than residents of other provinces.

**The Five Eyes gap is the structural problem.** Canadian law constrains what Canadian government agencies can do with Canadian citizens' data. It does not constrain what the Communications Security Establishment (CSE) can share with NSA or GCHQ, and it does not prevent US law enforcement or intelligence from requesting data from US-based service providers about Canadian citizens through US legal process. Data about a Canadian citizen stored on US servers (Google, Apple, Meta, Microsoft) is accessible through FISA, National Security Letters, and other US legal instruments without Canadian court oversight. The Five Eyes "third-party rule" has historically limited sharing of intelligence about each other's citizens, but this rule is a policy constraint rather than a legal one, and its application has been contested in various intelligence contexts.

**CSE oversight gaps.** The Communications Security Establishment Act (2019) established the National Security and Intelligence Review Agency (NSIRA) and the Intelligence Commissioner — a significant improvement in oversight architecture. However, CSE's foreign intelligence mandate allows collection of communications that involve Canadians when the targets are foreign. The boundary between foreign collection that incidentally captures Canadian communications and targeted domestic surveillance is an ongoing legal and policy debate. The 2025 NSIRA annual report documented CSE compliance issues in data handling, suggesting that even the improved oversight architecture has gaps.

**International data sharing implications for the at-risk population.** For Canadians who are also members of communities targeted by US enforcement (Latin American immigrants with US ties, Iranian diaspora, Chinese diaspora communities under US-Canada Five Eyes surveillance coordination), Canadian residence does not provide protection from US data requests. US law enforcement can and does make Mutual Legal Assistance Treaty (MLAT) requests to Canada, and Five Eyes intelligence sharing creates back-channel information flows that do not require formal MLAT processes.

### Messaging Framework

**Opening frame**: Canadian privacy law provides real protections within Canada — but data about you on US servers, and intelligence collected by Five Eyes partners, operates under different rules. Your threat model depends on whether your adversary is a commercial entity (PIPEDA applies), a Canadian government agency (CSE Act and Charter apply), or a US government agency acting through US servers or Five Eyes channels (US law applies, not Canadian).

**Extension**: The most practical protective measure for Canadians in at-risk communities is data minimization from US-based service providers — not because Canadian law fails you, but because reducing data held on US servers limits what US legal instruments can reach.

**Actionable steps specific to this population**:
1. Assess which service providers hold your data and in which country: Canadian-domiciled data (Canadian government services, provincially regulated services) has stronger protection; US-company data (Google, Apple, Meta, Amazon) is accessible to US process
2. For sensitive communications: Signal (US-based company, but no content stored) is still the most protective option; ProtonMail (Switzerland-based) for email reduces US MLAT reach
3. Quebec residents: exercise Law 25 rights — request what data organizations hold, request erasure, file complaints with the Commission d'accès à l'information (CAI) when rights are violated
4. Federal PIPEDA rights (applicable everywhere): right to access personal information held by federally regulated companies and right to correct inaccurate information — use these for data brokers operating federally
5. Be aware of the provincial data localization gap: provincial laws like BC PIPA do not generally include US-style data residency requirements, meaning BC-headquartered companies can still store your data on US servers where it is accessible to US process

**Canada-specific institutional partners**:
- Citizen Lab (University of Toronto) — Canada's leading digital surveillance research lab; primary source on Five Eyes and CSE surveillance; publishes threat assessments on targeted community surveillance
- BC Freedom of Information and Privacy Association (FIPA)
- Canadian Civil Liberties Association (CCLA) — active on surveillance reform
- Office of the Privacy Commissioner of Canada (OPC) — federal DPA; accepts complaints against federally regulated organizations
- Commission d'accès à l'information (CAI) — Quebec's DPA; aggressive enforcement of Law 25

### Confidence Level: High for domestic law; Moderate for Five Eyes intelligence-sharing details
Domestic law status is documented through legislation and OPC guidance. FVEY operational details are inferred from publicly available reporting; specific CSEC/NSA data-sharing mechanisms on civil targets are not publicly documented.

---

## Audience 4: Refugee Camp and Humanitarian Contexts

### Threat Context

This is the most structurally distinct audience. The threat model for people in refugee camps or humanitarian settings is defined by three factors that do not apply to any other audience:

1. **Severely limited and monitored connectivity** — connectivity is provided by UNHCR, host governments, or commercial partners, all of whom have full visibility into network traffic
2. **Mandatory biometric registration** — UNHCR has collected biometric data from over 7 million refugees in 60 countries since 2019; this data is shared with host governments, creating direct surveillance risk where host governments are hostile
3. **Trust-based rather than technology-based OpSec** — in low-connectivity environments, the most reliable security is community-based information control rather than technical countermeasures

**UNHCR biometric sharing creates direct risk.** UNHCR was found to have shared Rohingya refugee biometric data with the Myanmar government — the same government from which Rohingya people were fleeing — without refugees' informed consent. A 2025 academic study documented that UNHCR data is "100% accessible to the Government of Jordan," which cross-references it with counter-terrorism data. The 2016 internal UNHCR audit found inadequate informed consent practices in four out of five countries reviewed, with some refugees reporting they were denied aid if they didn't provide data. This is not a historical problem — the structural dynamics that produced the Rohingya disclosure (UNHCR dependence on host government cooperation, funding pressure to demonstrate reach) remain in place.

**Connectivity is monitored infrastructure.** In most camp settings, internet access is provided through controlled infrastructure: UNHCR-contracted satellite uplinks, host government telecommunications networks, or commercial providers operating under host government licensing. Traffic analysis — determining who communicates with whom, when, and from where — is available to any party with access to the network infrastructure, regardless of whether message content is encrypted. This means:
- Tor usage patterns are detectable as Tor traffic even when content is hidden; in some camp jurisdictions, Tor usage itself is suspicious
- VPN traffic is similarly detectable by pattern analysis on monitored infrastructure
- The parties with network access are often the same parties from whom refugees need protection

**Offline security and community trust are the primary protective mechanisms.** The ITU and UNHCR "Connectivity for Refugees" initiative is attempting to scale meaningful connectivity to 20 million displaced people by 2030. Current coverage gaps mean that many people in camp settings have intermittent connectivity, shared devices, and limited ability to install or update security software. The Security in a Box toolkit (maintained by Front Line Defenders and Tactical Technology Collective) specifically addresses these constraints with offline-first tool recommendations and community-level operational security guidance.

**Digital onboarding creates lasting exposure.** Many humanitarian programs — cash assistance, food distribution, medical services — now require digital registration that captures biometric data, identity documents, and family relationships. This data, once captured, persists in systems that may be accessible to adversarial governments. The short-term benefit (receiving aid) creates a permanent data exposure that cannot be reversed.

### Messaging Framework

**Opening frame**: The tools that protect people in other contexts — encrypted apps, VPNs, Tor — are less useful in camp environments where the network infrastructure itself is controlled and monitored. The most effective security in your context is community-based: who knows what about whom, and what they know to say and not say.

**Extension**: Technology still matters, but the priority is different. Encryption protects content even on monitored networks. Offline storage protects sensitive documents without network exposure. Device compartmentalization prevents one seized device from exposing everything.

**Actionable steps specific to this audience**:
1. Community-level information compartmentalization: not everyone needs to know everything. Designate a small trusted group for sensitive information; others know only what they need to know
2. Signal for digital communications when connectivity permits: encrypted content is protected even on monitored networks, though traffic patterns (who you talk to) remain visible
3. Use disappearing messages (Signal's timed deletion): reduces the data available if a device is seized
4. Offline documentation: use VeraCrypt to encrypt sensitive documents stored on a USB drive that can be kept separate from the device; this prevents device seizure from exposing documents
5. Biometric registration awareness: understand what data UNHCR and host government programs collect, which governments have access to that data, and what the risks are before registering for any service that requires biometric capture. This is not an argument against registration (which is often required for aid) but an argument for informed consent
6. Shared device security: if devices are shared, use individual encrypted profiles rather than a single shared account; log out of all accounts before returning a shared device
7. Avoid cloud backup of sensitive content: device backups to Google, Apple, or commercial clouds are stored in jurisdictions that may honor host government legal process

**Humanitarian-context institutional partners**:
- UNHCR — for systemic advocacy on biometric data governance; also for direct service referral for individuals at risk
- International Committee of the Red Cross (ICRC) — ICRC has a distinct biometric data policy that emphasizes host-government data separation; relevant for populations in conflict zones with ICRC presence
- Tactical Technology Collective / Security in a Box — specifically designed for human rights defenders in low-resource environments
- Front Line Defenders — provides emergency digital security support for human rights defenders globally; active in refugee contexts
- Internews — media and communications organization active in humanitarian settings; has digital literacy programming

### Confidence Level: Moderate-High for structural threat model; Moderate for specific operational guidance
Biometric sharing risks are documented through multiple academic studies and UNHCR internal audits. Network monitoring in camp settings is inferred from infrastructure characteristics rather than direct documentation of specific surveillance incidents.

---

## Audience 5: Authoritarian Exile and Diaspora

### Threat Context

People in exile from China, Russia, Iran, and similar authoritarian states face a structurally different threat from all other audiences: state-level adversaries with sustained institutional investment in tracking, harassing, and silencing diaspora communities abroad. This is documented, not speculative.

**China: Uyghur diaspora as documented case study.** In March 2025, senior members of the World Uyghur Congress (WUC) living in exile received Google notifications warning of government-backed attacks. Citizen Lab documented a spearphishing campaign that delivered malware through a trojanized version of UyghurEdit++, a legitimate open-source word processing tool developed specifically for the Uyghur language. The attack surface was the community's own language tooling — attackers targeted software that diaspora members trusted because it served their cultural needs. This demonstrates a targeting methodology: state actors identify community-specific tools and weaponize them.

Additional documented Chinese state TTPs against diaspora:
- Physical surveillance and intimidation in host countries (documented in CEPA reporting)
- Pressure on family members remaining in China as a lever against diaspora activists
- "Super app" surveillance through WeChat: WeChat monitors content and communications, with data accessible to Chinese government authorities; diaspora members who communicate with family in China through WeChat expose both themselves and their family members
- APT41 and associated groups conduct targeted cyber operations against civil society and diaspora communities

**Iran: documented targeting with Telegram-based malware.** The FBI issued a warning (March 2026) that MOIS (Ministry of Intelligence and Security) cyber actors are using Telegram as command-and-control infrastructure for malware targeting Iranian dissidents, journalists, and opposition groups globally. The FBI attributed the campaign to actors linked to the Ministry of Intelligence and Security, with attacks stretching back to 2023. The UK government's April 2025 country policy note on Iran documented that Iranian intelligence monitors and targets high-profile Iranian dissidents living outside the country, including in the UK, France, Germany, and elsewhere. Access Now reported a 720% surge in individual requests for digital security assistance from Iranian communities in the first half of 2025.

Iran-specific threat profile:
- IRGC and MOIS conduct targeted spyware deployment using Pegasus and custom malware
- Social engineering through trusted community contacts (impersonation of journalists, activists, researchers)
- Sur-place surveillance: social media monitoring of diaspora posts that could be used to prosecute family members in Iran
- Coercion of family members remaining in Iran to surveil, report on, or communicate with targeted diaspora members

**Russia: diaspora under post-2022 enforcement pressure.** Russian diaspora in exile — particularly political activists, journalists, and civil society members who fled after the February 2022 invasion of Ukraine — face surveillance operations from FSB and GRU-linked groups. Russia's 2025 VPN restrictions (fines for using VPNs to access blocked content, fines for VPN providers) primarily affect people inside Russia, but intelligence operations against diaspora communities operate across borders. Russian state television and influence operations specifically target diaspora communities to monitor, harass, and discredit opposition voices.

**Family-in-hostile-state risk modeling.** This is the most under-addressed risk for diaspora populations. An exile who takes strong OpSec measures to protect themselves may still be accessible through their family members who remain in the authoritarian state:
- Family members can be pressured to surveil the exile's activities, provide contact information, or communicate surveillance-enabling information under duress
- Communications between an exile and their family, if conducted through monitored platforms (WeChat, Telegram, unencrypted SMS), expose both parties
- The exile's social media activity is visible to state intelligence monitoring even when the exile is physically outside the country; this visibility creates risk for family members identified through social graph analysis

### Messaging Framework

**Opening frame**: Your adversary is a government with significant intelligence resources and a documented interest in tracking, silencing, or coercing people like you, wherever you are in the world. The tools your community uses to stay connected — WeChat, Telegram, community WhatsApp groups — are also potential surveillance surfaces. This is not paranoia; Citizen Lab and the FBI have documented these operations in detail.

**Extension**: The goal is not to disappear digitally — maintaining community connections and diaspora organizing is itself a form of resistance. The goal is to protect the channels that carry your most sensitive communications, compartmentalize your digital identity, and reduce the exposure risk for family members who remain in the hostile state.

**Actionable steps specific to this audience**:

For Chinese diaspora:
1. Stop using WeChat for anything you wouldn't say to Chinese state security directly — it is a monitored platform. Migrate sensitive communications to Signal
2. Verify software before installing, particularly tools developed for your community's specific linguistic or cultural needs — state actors have targeted community-specific software (UyghurEdit++); treat downloads with scrutiny even from trusted sources
3. Compartmentalize: use a separate device or profile for any WeChat communication with family in China; do not mix this with your activist or political communications
4. For family back home: coach them on what not to say and what platforms are monitored; reduce the information they hold that could be extracted under pressure

For Iranian diaspora:
1. Do not use Telegram as your primary secure communications channel — the FBI advisory (March 2026) documents Iranian state actors using Telegram malware delivery. Telegram's default mode is not E2EE
2. Use Signal for secure communications; be aware that Signal's encryption is not effective if the device receiving the message is compromised by malware
3. Verify identity before sensitive conversations: Iranian intelligence uses impersonation of journalists, researchers, and other diaspora members as a social engineering vector
4. Sur-place risk: your social media posts are visible in Iran and can be used to target family members. Use geolocation blocking, audience restriction, and consider pseudonymous accounts for high-exposure advocacy activity
5. VPN for general browsing: reduces exposure to country-level traffic analysis, but does not protect against spyware on your device

For Russian diaspora:
1. Use Signal; be aware that Russian state actors can target the devices of people you communicate with even if you are careful
2. VPN status: VPNs are legally restricted inside Russia (July 2025 law imposes fines on providers who don't block banned content; individual fines for VPN use to access extremist content). If you have contacts inside Russia who use VPNs, be aware of their increased legal exposure
3. Operational separation between public advocacy activity and personal life reduces targeting surface
4. Proton Mail (Switzerland jurisdiction) for email — reduces exposure to MLAT requests from Russian authorities to US email providers

**Authoritarian-exile institutional partners**:
- Citizen Lab (University of Toronto) — primary research institution for state-actor surveillance of diaspora; publishes threat reports and provides direct assistance
- Access Now Digital Security Helpline — provides emergency support in nine languages including Russian and Arabic; specifically experienced with authoritarian-context threats
- Front Line Defenders — emergency support for human rights defenders under state threat
- Reporters Without Borders (RSF) — press freedom organization with diaspora journalist support programs
- Freedom House (Freedom on the Net report) — annual country-by-country internet freedom documentation; operational guidance implications

### Confidence Level: High
FBI advisories, Citizen Lab technical reports, and UK government country guidance provide strong primary-source documentation for these threat models. Specific TTPs are ongoing and current.

---

## Cross-Audience Notes: What Generalizes

Three countermeasures are sound across all five jurisdictions:

1. **Signal** — E2EE that has survived legal challenge in the US, complies with EU GDPR, is accessible in most jurisdictions (not blocked in most EU and Canadian contexts; blocked in some authoritarian contexts but accessible via bridges), and provides a confirmed gap in state adversary capability
2. **Data minimization** — reducing the volume of data generated by commercial apps (advertising ID, location permissions) reduces the data available to both commercial and government adversaries regardless of jurisdiction
3. **Disappearing messages** — reduces the data available if a device is seized, regardless of whether the adversary is a commercial data broker, a border agent, or a state intelligence service

One countermeasure that does NOT generalize is **Tor**:
- Legal and effective in most EU and Canadian contexts
- Legally available but detectably suspicious in refugee camp network contexts
- Blocked in China and Iran; use of circumvention tools carries criminal penalties in Iran; account termination in China
- Use in Russia exposes users to legal risk under 2025-2026 internet sovereignty laws
- Tor bridges mitigate blocking in China and Iran but do not eliminate legal risk

---

## Sources

- [404 Media: ELITE User Guide](https://www.404media.co/here-is-the-user-guide-for-elite-the-tool-palantir-made-for-ice/)
- [EFF: ICE Using Palantir Tool That Feeds on Medicaid Data](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data)
- [CBP Biometric Expansion Rule — Nextgov/FCW](https://www.nextgov.com/policy/2025/11/dhs-proposes-biometrics-expansion-immigrants-dropping-age-restrictions-and-requiring-biometrics-some-us-citizens/409274/)
- [Biometric Update: Data, quotas, and biometric surveillance reshape US immigration enforcement](https://www.biometricupdate.com/202601/data-quotas-and-biometric-surveillance-are-reshaping-us-immigration-enforcement)
- [Privacy International: Challenge Against Hidden Data Ecosystem](https://privacyinternational.org/legal-action/challenge-hidden-data-ecosystem)
- [Verfassungsblog: In the Shadows — Data Brokers and the Limits of the GDPR](https://verfassungsblog.de/datatrade-eu-gdpr-privacy/)
- [Solomon: How Clearview AI Dodged Fines Across Europe](https://wearesolomon.com/mag/format/investigation/clearview-how-a-shady-us-ai-company-dodged-fines-and-defied-regulators-across-europe/)
- [UK Upper Tribunal: Clearview AI GDPR Jurisdiction Confirmed, October 2025](https://www.faegredrinker.com/en/insights/publications/2025/10/decision-of-the-uk-information-commissioners-office-tribunal-on-clearview-ai)
- [EFF: EU Encryption Roadmap Makes Everyone Less Safe](https://www.eff.org/deeplinks/2025/06/eus-encryption-roadmap-makes-everyone-less-safe)
- [EFF: EU Parliament Blocks Mass-Scanning of Chats, April 2026](https://www.eff.org/deeplinks/2026/04/eu-parliament-blocks-mass-scanning-our-chats-whats-next)
- [IAPP: What 2026 May Bring for Canada's Privacy Reform Efforts](https://iapp.org/news/a/what-2026-may-bring-for-canadas-privacy-reform-efforts)
- [Osler: Canada's 2026 Privacy Priorities](https://www.osler.com/en/insights/reports/2025-legal-outlook/canadas-2026-privacy-priorities-data-sovereignty-open-banking-and-ai/)
- [Citizen Lab: Weaponized Words — Uyghur Language Software Hijacked](https://citizenlab.ca/research/uyghur-language-software-hijacked-to-deliver-malware/)
- [Citizen Lab: Digital Transnational Repression (UK Parliament submission)](https://committees.parliament.uk/writtenevidence/138042/pdf/)
- [IC3/FBI: Iranian MOIS Telegram C2 Malware Advisory, March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)
- [UK Gov: Iran Country Policy Note — Social Media Surveillance, April 2025](https://www.gov.uk/government/publications/iran-country-policy-and-information-notes/country-policy-and-information-note-social-media-surveillance-and-sur-place-activities-iran-april-2025-accessible)
- [Moscow Times: Russia's 2025 Internet Restrictions](https://www.themoscowtimes.com/2025/08/06/how-russias-new-internet-restrictions-work-and-how-to-get-around-them-a90117)
- [UNHCR: Connectivity for Refugees Initiative](https://www.unhcr.org/innovation/connectivity-for-refugees/)
- [ODI: Rohingya Biometrics Scandal](https://odi.org/en/insights/although-shocking-the-rohingya-biometrics-scandal-is-not-surprising-and-could-have-been-prevented/)
- [Access Now Digital Security Helpline](https://www.accessnow.org/help/)
- [Front Line Defenders: Security in a Box](https://www.frontlinedefenders.org/en/resource-publication/security-box)
- [CEPA: Super Apps — Surveillance in China and Russia](https://cepa.org/article/super-apps-a-path-to-surveillance-in-china-and-russia/)

---

*Created: 2026-04-30 | Item 28 — Tier 2 Regional Adaptation Framework*
