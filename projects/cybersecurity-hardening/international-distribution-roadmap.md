---
title: "International Distribution Roadmap — Secondary Language Priorities and Institutional Partners"
project: cybersecurity-hardening
created: 2026-04-30
status: research-complete
item: 28 — Tier 2 Regional Adaptation Framework
depends-on: tier-2-regional-messaging.md, regional-threat-model-analysis.md, regional-compliance-matrix.md
---

# International Distribution Roadmap: Secondary Language Priorities and Institutional Partners

**Lead finding**: The corpus as currently written is a US-domestic document in English. International distribution requires three distinct activities: translation (literal language conversion), localization (adapting threat examples, legal references, and institutional partners to the target jurisdiction), and routing (identifying the institutional partners in each region who can amplify to the target population). Of these three, routing to institutional partners is the highest-leverage activity — a single warm relationship with an organization like Access Now, UNHCR Digital Resilience, or a regional digital rights organization provides sustained reach that individual translation cannot replicate. Language translation should follow institutional partnerships, not precede them.

---

## I. Language Tier Framework

### Prioritization Criteria

Languages are prioritized by the intersection of:
1. **Speaker population at high threat urgency**: Communities actively facing the surveillance threats documented in the corpus
2. **Institutional coverage**: Whether organizations already exist to distribute content in the language to at-risk communities
3. **Translation and localization complexity**: Technical security content requires translators with both linguistic fluency and digital security familiarity
4. **Gap in existing resources**: Whether quality digital security content already exists in the language (if comprehensive resources exist, translation adds less marginal value)

### Tier 2a: Primary International Languages (>10M speakers, highest threat urgency)

**Spanish (Latin American asylum seekers and undocumented populations)**
- Estimated global speakers: 500+ million; approximately 55 million in the US
- Threat urgency: Highest — Latin American-origin communities are disproportionately represented in ICE enforcement populations; ELITE's address confidence scoring system was documented operating in neighborhoods with high concentrations of Spanish-speaking communities
- Existing resources: Partial. EFF publishes some Spanish-language digital security content; Access Now Helpline operates in Spanish; the Freedom of the Press Foundation's border journalist curriculum module includes Spanish-language material
- Gap: No Spanish-language document exists that specifically maps ELITE's data supply chain (Medicaid records, commercial broker location data, DMV records) to actionable countermeasures at the level of specificity in the corpus
- Translation complexity: Moderate. Technical terms (VPN, metadata, data broker) require consistent terminology decisions; legal references (CCPA DROP platform, California DELETE Act) need localization to explain state-specific context to a broader Latin American audience
- Estimated resource: 25-35 hours for skilled translator with digital security background

**Farsi/Persian (Iranian diaspora and Iran-based at-risk population)**
- Estimated global speakers: 70-80 million (Farsi, Dari, Tajik variants)
- Threat urgency: Critical — FBI March 2026 advisory documents active Iranian state actor operations targeting diaspora globally; Access Now reported 720% surge in digital security requests from Iranian communities in H1 2025
- Existing resources: Access Now Helpline does not currently list Farsi among its nine languages (Arabic is included; Farsi is not as of most recent documentation). This is a documented gap. Iran-focused digital rights organizations (Article 19, Center for Human Rights in Iran) publish some digital security content in Farsi
- Gap: FBI-documented Telegram malware operations specifically target the Iranian diaspora. A Farsi-language document mapping this threat (Telegram C2 malware, MOIS spear-phishing TTPs, sur-place surveillance risk for family back home) to Signal-based countermeasures fills a gap in currently available resources
- Translation complexity: High. Farsi script (right-to-left) requires technical accommodation; terminology decisions are politically significant in Iranian diaspora contexts (some terminology carries ideological weight); technical accuracy is critical because errors in security guidance could have life-safety consequences
- Estimated resource: 35-45 hours for skilled translator with digital security and Farsi-language journalism background

**Mandarin Chinese (Chinese diaspora)**
- Estimated global speakers: 1+ billion; Chinese diaspora in US, Canada, Europe estimated at 5-6 million
- Threat urgency: Critical — Citizen Lab March 2025 documentation of trojanized Uyghur-language software targeting World Uyghur Congress; documented WeChat surveillance infrastructure; Chinese police stations in foreign countries; family-leverage operations
- Existing resources: EFF has some Chinese-language content; Citizen Lab publishes research in English with Chinese-language summaries for some reports; Great Fire is a China-focused censorship circumvention project with Chinese-language resources
- Gap: A Mandarin-language document specifically addressing WeChat surveillance risk, the family-back-home communication dilemma, and Signal migration for a diaspora audience is not comprehensively available from major digital rights organizations. Distinction between Simplified (PRC-origin diaspora) and Traditional (Taiwan, HK diaspora) script matters for audience targeting
- Translation complexity: High. Simplified vs. Traditional script is a meaningful choice (Traditional Chinese is appropriate for Taiwanese and Hong Kong diaspora; Simplified for mainland China-origin diaspora — these communities have different threat models and should receive different versions). Technical terminology in Chinese security discourse is not standardized; Wikipedia Chinese versions of technical terms vary in quality
- Estimated resource: 35-45 hours per version (Simplified and Traditional are different localization projects)

---

### Tier 2b: Secondary International Languages (strategic value, specialized audiences)

**Arabic (refugee contexts, MENA authoritarian state diaspora)**
- Estimated global speakers: 300+ million
- Threat urgency: High for multiple distinct populations: Syrian refugees in camps (Jordan, Turkey, Lebanon), Sudanese refugees, Palestinian diaspora, Yemeni diaspora; additionally Gulf state diaspora facing authoritarian surveillance
- Existing resources: Access Now Helpline operates in Arabic; Front Line Defenders has Arabic-language digital security resources; Committee to Protect Journalists publishes some Arabic-language journalist security content. Coverage is better for Arabic than for Farsi or some other target languages
- Gap: The refugee camp specific threat model (UNHCR biometric data sharing risk, monitored network environments, offline-first security for limited connectivity) is not well-covered in existing Arabic-language resources, which tend to address more tech-literate urban activist audiences rather than camp-based populations with limited device access
- Translation complexity: High. Modern Standard Arabic vs. specific national dialects (Egyptian Arabic, Levantine Arabic, Gulf Arabic) — corpus should target Modern Standard Arabic for broadest reach while acknowledging that spoken dialect varies; humanitarian workers reading the Arabic version may have different technical backgrounds than diaspora activists
- Estimated resource: 30-40 hours for skilled translator with digital security background; additional 10-15 hours for humanitarian-context localization

**Russian (diaspora in exile)**
- Estimated global speakers: 150+ million; Russian diaspora in Germany, Baltic states, US, Israel, and other countries following 2022 exodus
- Threat urgency: High for Russian political opposition, journalists, and civil society in exile; documented FSB and GRU operations against opposition diaspora
- Existing resources: Access Now Helpline operates in Russian; Meduza (Russian independent journalism) and iStories publish some digital security guidance; FBK has published internet sovereignty documentation. Russian-language digital security resources exist but are fragmented across sources with varying quality
- Gap: Russian dissident communities in exile need content specifically addressing the communication security problem created by Russian internet sovereignty measures — how to communicate securely with contacts inside Russia who face VPN restrictions and content blocking, how to navigate the information environment where Telegram is both widely used and partly compromised
- Translation complexity: Moderate. Russian technical security vocabulary is well-developed (the Russian security research community is large); political framing choices matter for reception in diaspora communities
- Estimated resource: 25-35 hours for skilled translator; lower complexity than Farsi or Chinese because Russian technical security vocabulary is more standardized

---

## II. Institutional Partners by Region

### US/North American Partners

| Organization | Role | Relevant Capability | Contact |
|-------------|------|--------------------|---------| 
| National Immigration Law Center (NILC) | Litigation and policy on immigrant data rights | Network reaches Spanish-speaking legal services providers nationally | info@nilc.org |
| Immigrant Defense Project | Legal defense in deportation proceedings | Direct contact with at-risk population | info@immigrantdefenseproject.org |
| Just Futures Law | Data broker liability for immigration enforcement | Won EFF's 2025 Award for Leading Immigration Surveillance Litigation | contact@justfutureslaw.org |
| Mijente | Latinx social justice organization | Spanish-language community organizing infrastructure; has published ICE data surveillance guides | info@mijente.net |
| National Day Laborer Organizing Network (NDLON) | Worker centers serving undocumented workers | Distribution infrastructure to Spanish-speaking at-risk population | info@ndlon.org |

### EU Partners

| Organization | Role | Relevant Capability | Contact |
|-------------|------|--------------------|---------| 
| Access Now (Brussels + regional offices) | Digital rights advocacy + Direct technical support helpline | Operates in 9 languages; EU policy advocacy; Digital Security Helpline for at-risk populations | security@accessnow.org; press@accessnow.org |
| noyb (Max Schrems, Vienna) | GDPR enforcement through systematic complaints | Industrialized complaint filing; EU legal enforcement expertise | office@noyb.eu |
| Privacy International | Commercial surveillance advocacy | Commercial data broker research; cross-EU coverage | contact@privacyinternational.org |
| Digitalcourage (Germany) | German-language digital rights | German-language content; German data protection focus | info@digitalcourage.de |
| La Quadrature du Net (France) | French digital rights | GDPR litigation; French-language content; EU policy advocacy | contact@laquadrature.net |
| CNIL (France) | French national DPA | Formal regulatory channel for GDPR complaints | https://www.cnil.fr/fr/plaintes |
| Article 19 | Freedom of expression globally | Arabic and other language content; MENA coverage | info@article19.org |

### Canadian Partners

| Organization | Role | Relevant Capability | Contact |
|-------------|------|--------------------|---------| 
| Citizen Lab (University of Toronto) | Research on state-actor surveillance | Primary research source on Five Eyes and diaspora targeting; institutional credibility | citizenlab@citizenlab.ca |
| BC Freedom of Information and Privacy Association (FIPA) | BC privacy rights | Provincial expertise; PIPA rights guidance | info@fipa.bc.ca |
| Canadian Civil Liberties Association (CCLA) | Surveillance reform litigation | Active on national security surveillance law | mail@ccla.org |
| Office of the Privacy Commissioner of Canada (OPC) | Federal privacy regulator | Accepts PIPEDA complaints; issues guidance | info@priv.gc.ca |
| Commission d'accès à l'information (CAI) | Quebec DPA | Quebec Law 25 enforcement; Quebec-specific rights | https://www.cai.gouv.qc.ca |

### Refugee and Humanitarian Partners

| Organization | Role | Relevant Capability | Contact |
|-------------|------|--------------------|---------| 
| UNHCR Digital Inclusion team | Connectivity for Refugees initiative | Direct infrastructure reach into camp populations; formal mandate for data protection | unhcr.org/innovation |
| International Committee of the Red Cross (ICRC) | Humanitarian law; separate biometric data policy | ICRC has adopted a stricter data-sharing policy than UNHCR; relevant for conflict-zone populations | icrc.org/en/contact |
| Internews | Media and communications in humanitarian settings | Digital literacy programming in camps; Arabic, French, Swahili coverage | info@internews.org |
| Tactical Technology Collective / Security in a Box | Human rights defender security tools | Offline-first toolkit specifically designed for limited-connectivity environments | tacticaltech.org |
| Front Line Defenders | Emergency security support for HRDs | 24/7 emergency support; camp-context digital security experience | digital@frontlinedefenders.org |
| NetHope | Technology for humanitarian organizations | Technology infrastructure for NGOs in crisis contexts | info@nethope.org |

### Authoritarian Exile Partners

| Organization | Role | Relevant Capability | Contact |
|-------------|------|--------------------|---------| 
| Citizen Lab | Research + direct assistance for diaspora under state attack | Primary documentation of Chinese, Iranian, and other state surveillance of diaspora | citizenlab@citizenlab.ca |
| Access Now Digital Security Helpline | 24/7 emergency technical support | Nine languages; experienced with authoritarian-context threats; directly serves diaspora populations | security@accessnow.org |
| Reporters Without Borders (RSF) | Press freedom; journalist safety | Diaspora journalist support programs; Arabic, Chinese, Russian, Farsi coverage | info@rsf.org |
| Freedom House | Internet freedom research | Country-by-country threat assessment; operational guidance implications | info@freedomhouse.org |
| World Uyghur Congress (WUC) | Uyghur diaspora organization | Direct distribution channel to Uyghur diaspora; trusted community institution | uyghurcongress@uyghur.org |
| Persian-language media in exile (IranWire, Manoto, VOA Persian) | Diaspora journalism | Distribution to Iranian diaspora; Farsi-language content infrastructure | (contact via publication) |
| Meduza, iStories (Russian independent media in exile) | Russian diaspora journalism | Distribution to Russian opposition diaspora; Russian-language content infrastructure | (contact via publication) |

---

## III. Translation and Localization Resource Requirements

### Technical Translation Standards for Security Content

Security content translation has unique requirements beyond standard professional translation:

**1. Technical vocabulary consistency**: Terms like "end-to-end encryption," "metadata," "advertising identifier," "data broker," "entity resolution" must be translated consistently throughout the document and consistently with terms used in the target-language security community. Using inconsistent terminology confuses readers and potentially directs them to incorrect tools.

**2. Security-competent translator**: A translator who is linguistically fluent but lacks digital security background will translate terms incorrectly or use locally deprecated vocabulary. The ideal translator has both language proficiency and digital security training — a profile that commands significant premium over standard translation rates.

**3. Operational accuracy is a safety issue**: For populations facing government-level surveillance, an incorrect recommendation (e.g., describing Telegram as end-to-end encrypted by default, which it is not) could have life-safety consequences. Translation quality review by a second security-competent reviewer is appropriate for high-threat contexts.

**4. Localization beyond translation**: Legal references (California CCPA, GDPR Article 17, PIPEDA) must be adapted for target audiences. A Spanish-language version for Latin American asylum seekers needs to explain California DELETE Act as a California-specific resource, not a national one. An Arabic version for Syrian refugees in Jordan needs to reference Jordanian data protection context, not EU law.

**5. Cultural framing**: Security guidance framing that works in a US context ("call the EFF hotline") may not translate to jurisdictions where no equivalent organization exists. The institutional partner map above should be integrated into localized versions so that each version points readers to regionally appropriate resources.

### Per-Language Resource Estimates

| Language | Script complexity | Translator profile needed | Estimated hours (translation) | Estimated hours (localization) | Total estimate |
|----------|------------------|--------------------------|-------------------------------|--------------------------------|----------------|
| Spanish (Latin American) | Latin script | Bilingual + digital security background | 20-25h | 10-15h | 30-40h |
| Farsi | Right-to-left Perso-Arabic script | Native Farsi + digital security + journalism background | 25-30h | 12-18h | 37-48h |
| Mandarin Simplified | Chinese character; significant | Digital security Mandarin-English bilingual | 25-30h | 15-20h | 40-50h |
| Mandarin Traditional | Separate version required | Same profile; Traditional script preference | 20-25h (from Simplified) | 10-15h (Taiwan/HK localization) | 30-40h |
| Arabic (MSA) | Right-to-left; significant typographic requirements | Arabic-English bilingual + digital security | 25-30h | 15-20h + humanitarian localization | 40-50h |
| Russian | Cyrillic script | Russian digital security community background | 20-25h | 8-12h | 28-37h |

**Total estimated resource for all six language versions**: 205-265 translator-hours, exclusive of project management, review, and technical formatting.

### Funding and Partnership Pathways

Security translation at these quality standards costs $75-150/hour for qualified translators, yielding a total project estimate of $15,000-40,000 depending on scope and language.

Institutional partnership provides the most efficient pathway to funded translation:
- **Access Now** has translation infrastructure and a multilingual team; partnership with Access Now could yield Spanish, Russian, Arabic, and French translations at lower cost than open-market translation
- **Internews** has humanitarian-context translation capacity for Arabic and regional languages
- **Freedom of the Press Foundation** has some translation capacity for journalist-security content
- Open-source community translation (volunteer translators with security background) is an option for Mandarin Chinese, where large diaspora communities include technology professionals; this requires careful quality review

---

## IV. Distribution Sequencing for International Expansion

### Phase 1 (Concurrent with Tier 2 domestic outreach, or immediately after)

**Target**: Institutional partner outreach — no translation required

1. Contact Access Now (security@accessnow.org) specifically requesting the Digital Security Helpline team review the corpus; note the Spanish and Arabic application
2. Contact Front Line Defenders (digital@frontlinedefenders.org) with the humanitarian-context framing from the refugee camp messaging variant
3. Contact Citizen Lab (citizenlab@citizenlab.ca) with the authoritarian-exile research alignment framing
4. Contact Privacy International regarding the EU data broker documentation

**Goal**: Establish at least one institutional partner in each regional category (EU, refugee, authoritarian exile) before beginning translation investment.

### Phase 2 (Following institutional partner engagement, 4-8 weeks after Phase 1)

**Target**: Spanish translation, leveraging NILC and Mijente networks

1. Engage NILC and Mijente to identify whether they can provide translation support or funding
2. Commission Spanish translation with localization for California DELETE Act context and Latin American asylum seeker threat model
3. Publish Spanish version to the Gist (or separate Gist) and notify Spanish-language distribution partners

**Rationale**: Spanish has the largest target population for the ELITE/US domestic threat model; institutional partners exist; distribution infrastructure (NDLON, Mijente worker centers) can reach the population without cold outreach.

### Phase 3 (Following Phase 2, 2-3 months after Phase 2)

**Target**: Farsi and Mandarin translations for authoritarian-exile populations

1. Farsi: partner with Access Now and Article 19 for quality review; identify Farsi-language translator through Iranian diaspora journalist community (IranWire editorial team is a potential referral source)
2. Mandarin: partner with Citizen Lab for Chinese security terminology review; identify translators through Chinese diaspora technology communities; produce Simplified and Traditional versions

**Rationale**: These are higher complexity translations with higher per-translation safety stakes; they should follow validation of the institutional partner relationships that enable quality review.

### Phase 4 (Ongoing)

**Target**: Arabic and Russian versions; humanitarian localization

1. Arabic: coordinate with Internews for humanitarian-context localization; integrate UNHCR digital resilience framing
2. Russian: coordinate with Meduza or iStories for distribution to Russian opposition diaspora
3. Develop refugee-context supplement that addresses UNHCR biometric data governance concerns — this may require separate UNHCR internal advocacy rather than a translated external document

---

## V. Metrics for International Distribution Success

**Phase 1 indicators (institutional partner engagement)**:
- At least two institutional partners in different regions agree to review and share the corpus within their networks
- Access Now Helpline confirms the corpus is relevant to their client population in at least one language they operate in
- Citizen Lab engages with the authoritarian-exile threat model research documentation

**Phase 2 indicators (Spanish translation)**:
- Spanish version published and distributed through at least one community organization with direct access to Spanish-speaking at-risk population
- Downloads/views of Spanish version measured through link tracking on published version

**Phase 3 indicators (Farsi and Mandarin)**:
- Quality review completed by a security-competent reviewer with native language proficiency before publication
- At least one diaspora media outlet (IranWire for Farsi; a Mandarin diaspora publication for Chinese) refers to or republishes the translated version

**Phase 4 indicators (Arabic and Russian)**:
- Arabic version reaches a humanitarian partner organization with camp-based distribution capacity
- Russian version reaches at least one Russian opposition diaspora outlet

---

## Sources

- [Access Now Digital Security Helpline](https://www.accessnow.org/help/)
- [Access Now: Guides for At-Risk Users](https://guides.accessnow.org/)
- [Front Line Defenders: Security in a Box](https://www.frontlinedefenders.org/en/resource-publication/security-box)
- [Citizen Lab: Digital Transnational Repression Research](https://citizenlab.ca/research/)
- [UNHCR: Connectivity for Refugees Initiative](https://www.unhcr.org/innovation/connectivity-for-refugees/)
- [ITU: Connectivity for Refugees — Digital Access for Displaced People, December 2025](https://www.itu.int/hub/2025/12/connectivity-for-refugees-digital-access-for-displaced-people-and-communities/)
- [Privacy International: Campaign Against Hidden Data Ecosystem](https://privacyinternational.org/campaigns/data-brokers)
- [IC3/FBI: Iranian MOIS Operations Advisory, March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)
- [Citizen Lab: Weaponized Words — Uyghur Language Software](https://citizenlab.ca/research/uyghur-language-software-hijacked-to-deliver-malware/)
- [Freedom of the Press Foundation: Border Journalist Digital Security Curriculum](https://freedom.press/digisec/blog/new-journalism-curriculum-module-teaches-digital-security-for-border-journalists/)
- [EFF: 2025 Award for Leading Immigration and Surveillance Litigation — Just Futures Law](https://www.eff.org/)
- [CPJ: Journalist Assistance Network Launch, May 2025](https://cpj.org/2025/05/us-press-freedom-groups-launch-journalist-assistance-network-to-address-growing-need-for-legal-safety-immigration-resources/)
- [Internews: Digital Literacy in Humanitarian Contexts](https://internews.org)
- [La Quadrature du Net](https://www.laquadrature.net/)
- [noyb — None of Your Business (Max Schrems)](https://noyb.eu)
- [FBK: Access Denied — How the Kremlin Controls the Internet, March 2026](https://fbk.info/files/acf-internet-report-EN.pdf)

---

*Created: 2026-04-30 | Item 28 — Tier 2 Regional Adaptation Framework*
