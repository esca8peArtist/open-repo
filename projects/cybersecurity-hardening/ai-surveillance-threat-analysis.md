---
title: "AI-Powered Surveillance and Synthetic Identity Threats: 2025-2026 Analysis"
project: cybersecurity-hardening
created: 2026-05-04
status: complete
confidence: high — primary and near-primary sources throughout; research current as of May 2026
depends_on: threat-model.md, 2026-threat-updates.md, device-hardening-guide.md
---

# AI-Powered Surveillance and Synthetic Identity Threats: 2025-2026 Analysis

**Bottom line up front**: The AI surveillance threat landscape in 2025-2026 is defined by three convergences. First, federal facial recognition is now deployed at street level with a 200-million-image database accessible via mobile phone — and documented cases show ICE treating false matches as "definitive." Second, voice cloning crossed the indistinguishable threshold in late 2025; any phone call or video conference from an unverified source is now an unverified identity. Third, LLMs have removed the cost barrier to mass deanonymization — work that previously required expert analysts can now be performed for cents per target. The existing threat model's countermeasures remain valid; this document deepens the analysis and adds operational guidance not yet present in the project.

---

## Part I: AI-Powered Facial Recognition — Federal Deployment and Failure Rates

### What Is Confirmed Operational (2025-2026)

**ICE Mobile Fortify** is the most significant new operational development in federal facial recognition. As of early 2025, ICE and CBP field agents have the app installed directly on government-issued phones. The workflow: point the phone camera at a person in public, upload their face and optional fingerprint scan, and within seconds receive a dossier including name, date of birth, and other data drawn from databases containing **200 million stored images**. The system has been used in the field more than 100,000 times as of January 2026, per a lawsuit filed by the State of Illinois and City of Chicago.

The databases Mobile Fortify queries include federal identity records, DHS biometric holdings, and state DMV photo repositories. The system connects directly into the Palantir ELITE and ICM data environment described in threat-model.md. ICE has confirmed the agency treats Mobile Fortify outputs as a "definitive" determination of immigration status — meaning an officer may continue detaining a U.S. citizen even when presented with a birth certificate if the app returned a result contradicting it.

**CBP biometric entry-exit system** is operational at all major airports and most land ports of entry. TSA's pilot programs for facial recognition boarding verification expanded to over 25 airports in 2025. The FBI's **Next Generation Identification (NGI) Interstate Photo System (IPS)** is the backend repository for criminal investigation use — the FBI completed an upgrade in 2018 achieving 99.12% Rank-1 accuracy on its test dataset with a selected vendor's algorithm, though as detailed below, test-dataset accuracy diverges substantially from real-world performance on certain demographics.

**Clearview AI** holds a $9.2 million contract with ICE (September 2025, described in threat-model.md) and claims a database of tens of billions of images scraped from the public internet — an order of magnitude larger than any government repository. Any public photo (social media profile, news article, organizational website) is in this database.

Sources: [404 Media: Mobile Fortify](https://www.404media.co/inside-ices-supercharged-facial-recognition-app-of-200-million-images/); [ACLU: Face Recognition and the Trump Terror](https://www.aclu.org/news/privacy-technology/ice-face-recognition); [Illinois/Chicago lawsuit via Democracy Now](https://www.democracynow.org/2026/1/29/ice_cbp_facial_recognition_technology_app); [Biometric Update: Clearview ICE contract](https://www.biometricupdate.com/202509/ice-awards-clearview-ai-9-2m-facial-recognition-contract)

---

### Accuracy Disparities by Demographic — Documented Research

The demographic accuracy problem in facial recognition is settled science, but its operational implications are routinely ignored in deployment decisions.

**NIST's foundational FRVT (Facial Recognition Vendor Test) Part 3** (2019) is still the reference standard for demographic effects. Key findings: false positive rates for African American and Asian faces were **up to 100 times higher** than for white faces, depending on the algorithm. False positive rates were highest for West and East African and East Asian subjects. In one-to-many matching scenarios (searching a database for a match — the exact use case in Mobile Fortify), the disparity is acute for African American females.

**2025 research on degraded image quality** — the normal condition for law enforcement surveillance footage — found error rates consistently higher for women and Black individuals, with Black females most affected. This is operationally significant: surveillance images captured at protests, from body cameras, or from street CCTV rarely match the controlled conditions of accuracy testing.

The **oversight gap created in February 2026**: DHS removed from its website the Biden-era directive governing face recognition use. No replacement policy was announced. There is currently no public federal standard for acceptable false positive rates in immigration enforcement facial recognition contexts, no mandatory human review requirement, and no mechanism for an incorrectly matched individual to challenge the result before detention.

Sources: [NIST FRVT Demographic Effects (NISTIR 8280)](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf); [2025 accuracy research on degraded images via ArXiv](https://arxiv.org/html/2505.14320v1); [Senator Kelly letter to DOJ on demographic disparities](https://www.kelly.senate.gov/wp-content/uploads/2024/01/Sen.-Kelly_Letter-to-DOJ-on-Facial-Recognition-and-Title-VI.pdf)

---

### Wrongful Arrests and Immigration Enforcement Use Cases

The ACLU has documented **more than a dozen wrongful arrests** caused by police reliance on facial recognition false positives. The first publicly documented case was Robert Williams, a Black man in Detroit, arrested in 2020 for a watch theft based on a match against his nine-year-old expired driver's license photo. He was held overnight before the false match was acknowledged. The ACLU's count stood at fourteen as of mid-2025.

For immigration enforcement, documented incidents include ICE agents in Chicago using Mobile Fortify on young people riding bikes and on an adult driver who explicitly declared U.S. citizenship. Under ICE's operational practice of treating Mobile Fortify as definitive, that declaration was apparently insufficient. IBTimes UK documented a U.S. citizen wrongfully detained by ICE in 2025 in circumstances consistent with facial recognition error.

The Illinois/Chicago lawsuit filed January 2026 argues that Mobile Fortify violates the Illinois Biometric Information Privacy Act (BIPA) — the strongest state biometric privacy law in the country — because the app collects, stores, and shares biometric identifiers without informed written consent. The plaintiffs also allege Fourth and First Amendment violations: indiscriminate scanning at protests and on public streets constitutes a suspicionless search.

Sources: [ACLU: More Than a Dozen Wrongful Arrests](https://www.aclu.org/news/privacy-technology/more-than-a-dozen-wrongful-arrests-due-to-police-reliance-on-facial-recognition-technology); [IBTimes UK: US citizen wrongfully detained](https://www.ibtimes.co.uk/us-citizen-wrongfully-detained-ice-facial-recognition-1792001); [MSNBC Op-Ed: ICE CBP guardrails needed](https://www.ms.now/opinion/msnbc-opinion/ice-cbp-border-patrol-facial-recognition-tech-immigrants-rcna241020); [EPIC coalition letter on Mobile Fortify (November 2025)](https://epic.org/wp-content/uploads/2025/11/Coalition-Letter-on-ICE-Mobile-Fortify-FRT-Nov2025.pdf)

---

### Evasion: What Works, What Does Not

**Physical obstruction remains the most reliable countermeasure.** Covering key identification landmarks — eyes, nose, mouth, jawline — prevents facial recognition algorithms from building a usable template. A mask plus sunglasses worn together provides substantial protection against camera-based recognition at distance. This is the baseline.

**Adversarial makeup research** has advanced significantly. The 2010-era CV Dazzle approach (high-contrast geometric patterns) is largely obsolete against modern deep learning systems, which learned to work around it. Current research published in 2025 shows that subtle darkening of high-density facial keypoint regions — the areas algorithms prioritize for landmark detection — can disrupt recognition without requiring dramatic visual changes. The approach is closer to strategic contouring than costume makeup. However, this is laboratory research; real-world effectiveness against deployed systems (which use proprietary models) is not confirmed.

**Adversarial patches and glasses** with infrared-reflective or optically confusing patterns have shown effectiveness in controlled research settings. The CVPR 2025 paper ProjAttacker demonstrated configurable physical projection attacks against face recognition systems. In practice, wearing purpose-built adversarial eyewear at a protest is conspicuous and legally distinguishable from ordinary protest participation.

**What does not help against facial recognition but is often misunderstood**: hoodies and hats provide limited protection unless they fully obstruct the face from camera angles. They may help in some camera placements but not others. Turning your back to cameras only works if you know camera locations in advance.

**The gait recognition caveat**: Physical facial countermeasures have no effect on gait recognition, which identifies individuals by their walking pattern from up to 50 meters away, even with back turned and face covered. China has deployed this operationally on city streets. U.S. deployment is not confirmed at scale, but the technology exists and is mature. For Tier 3 individuals, physical countermeasures should account for gait as well as face: altering gait deliberately and consistently is difficult to sustain, but footwear changes and bulky layered clothing can degrade gait recognition accuracy.

**The legal picture on face covering**: In a significant number of U.S. states, anti-mask laws restrict face covering at protests except for health or religious reasons. Legal status varies by jurisdiction. Know your state law before deploying physical facial countermeasures at a public event.

Sources: [State of Surveillance: How to Defeat Facial Recognition (2025)](https://stateofsurveillance.org/news/how-to-defeat-facial-recognition/); [ProjAttacker CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ProjAttacker_A_Configurable_Physical_Adversarial_Attack_for_Face_Recognition_via_CVPR_2025_paper.pdf); [ScienceDirect: Physical adversarial attacks survey 2025](https://www.sciencedirect.com/science/article/abs/pii/S0925231225031571)

---

## Part II: Deepfakes and Synthetic Identity Attacks

### Voice Cloning: Current Capability

Voice cloning technology as of late 2025 requires as little as **3 seconds of audio** to produce a functional clone. For high-fidelity, indistinguishable output, 30-60 seconds is sufficient. The Fortune/researcher assessment published December 2025 characterized 2026 as the year voice cloning crosses "the indistinguishable threshold" — meaning consumer tools now produce synthetic voices that most people cannot distinguish from real ones.

Real-time voice cloning is now commercially available. During a live call, a voice cloning pipeline can process incoming audio and generate output voice in near-real-time, transforming one speaker's voice to sound like the target. The FBI issued a formal warning in May 2025 that malicious actors were using AI-generated voice messages to impersonate **senior U.S. government officials**. Documented 2025 attack: fraudsters cloned the voice of Italian Defense Minister Guido Crosetto and used it to call high-profile business leaders soliciting ransom payments for a fabricated kidnapping scenario.

Vishing (voice phishing) attacks surged 442% in 2025 attributable to AI-driven techniques. Microsoft's 2025 Digital Defense Report measured AI-generated phishing messages achieving a **54% click-through rate** versus 12% for manually crafted messages — a 4.5x improvement. Applied to voice: AI-generated voice social engineering is measurably more convincing than human-executed attacks.

Sources: [Fortune: Voice cloning indistinguishable threshold (December 2025)](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/); [SQ Magazine: AI Voice Cloning Statistics 2026](https://sqmagazine.co.uk/ai-voice-cloning-fraud-statistics/); [TechNewsWorld: Real-time voice cloning vishing](https://www.technewsworld.com/story/researchers-mount-vishing-attacks-with-real-time-voice-cloning-179945.html); [Microsoft 2025 Digital Defense Report via Paubox](https://www.paubox.com/blog/microsoft-ai-makes-phishing-4.5x-more-effective-and-far-more-profitable)

---

### Deepfake Video: Detection Thresholds

The WEF Cybercrime Atlas report (January 2026) tested 17 face-swapping tools and eight camera injection tools against live KYC (Know Your Customer) biometric verification systems. The finding: **moderate-quality face swaps combined with camera injection defeat a wide range of active liveness implementations.** Camera injection means feeding a pre-recorded deepfake video into the video stream rather than using the actual camera — bypassing even systems designed to detect static image substitution.

In controlled laboratory conditions, state-of-the-art detection algorithms achieve 94% accuracy. In real-world deployment, effectiveness drops by **45-50%** against manipulations outside the training dataset. Human detection rates are far worse: a 2025 iProov study found that only **0.1% of participants** correctly identified all fake and real media presented to them, and human detection rates for high-quality deepfakes are just 24.5%.

The practical operational implication: no commonly available video call platform (Zoom, Signal video, FaceTime, Teams) provides reliable protection against a determined adversary injecting a deepfake. A video call showing a person's face is not identity verification. This was previously noted in 2026-threat-updates.md under Threat Vector 2 and is confirmed by additional sourcing here.

The Arup case remains the clearest documented large-scale consequence: a finance employee transferred $25.6 million after a video conference in which every participant — including the apparent CFO — was a deepfake. This was not a nation-state operation. It was a criminal fraud using commercially available tooling.

Sources: [WEF Unmasking Cybercrime Report 2026](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf); [Deepstrike.io: Deepfake Statistics 2025](https://deepstrike.io/blog/deepfake-statistics-2025); [The Hacker News: Purdue deepfake benchmark](https://thehackernews.com/expert-insights/2025/12/purdue-universitys-real-world-deepfake.html); [6G-AI: Deepfake detection arms race 2026](https://6g-ai.com/news/deepfake-detection-2026-arms-race)

---

### Social Engineering Amplification

AI enables targeted social engineering at a scale and precision previously achievable only by well-resourced intelligence agencies. The key capability is context injection: AI tools can scrape publicly available information about a target (social media, professional profiles, news mentions, organizational affiliations), synthesize a personalized narrative, and generate a convincing communication — all in under a minute, for under a dollar per target.

Documented 2025 example: Brightside AI documented a campaign targeting 800 accounting firms with AI-generated emails referencing **specific state registration details** for each firm — details a human attacker would spend hours researching per target. The campaign achieved a 27% click rate.

For activists and journalists, the threat model includes both inbound and outbound synthetic content:

**Inbound**: A call, email, or message appearing to come from a trusted source (attorney, organizational contact, colleague) may be AI-synthesized. The message will correctly reference real details from your public presence. The goal may be to extract credentials, physical location, schedule, or legal strategy.

**Outbound fabrication**: Fabricated audio and video purporting to show you making damaging statements is now a documented harassment tactic used by state-aligned actors and domestic right-wing operations against activists. Reporters Without Borders documented 100 journalists targeted by deepfakes in 27 countries between December 2023 and December 2025, with 74% of cases targeting women.

**Defense against voice authentication specifically**: A journalist demonstrated in a Business Insider test that a deepfake voice generated with an inexpensive tool passed both a bank's IVR system and a five-minute live agent call, reciting account and Social Security details (purchasable on dark web markets). Voice biometrics as a 2FA mechanism is now functionally compromised for any individual whose voice is publicly accessible.

Sources: [Group-IB: Voice of Fraud deepfake vishing](https://www.group-ib.com/resources/research-hub/voice-of-fraud/); [Brightside AI: AI phishing click rates](https://www.brside.com/blog/ai-generated-phishing-vs-human-attacks-2025-risk-analysis); [RSF: 100 journalists targeted by deepfakes](https://rsf.org/en/rsf-analysis-100-deepfakes-shows-mounting-threat-journalists-especially-women); [ABA Banking Journal: Voice biometric vulnerabilities](https://bankingjournal.aba.com/2024/02/challenges-in-voice-biometrics-vulnerabilities-in-the-age-of-deepfakes/)

---

## Part III: AI-Assisted Mass Surveillance (LLM-Based)

### How LLMs Are Being Used to Analyze Social Media at Scale

The MIT Technology Review published a detailed analysis in April 2026 specifically examining how LLMs could enable mass surveillance using commercially purchased bulk datasets. The core finding is structural: **privacy has historically depended on the inefficiency of analysis, not on legal protection.** LLMs remove this friction.

Research demonstrates the capability:

- An LLM agent identified individuals from **redacted interviews** in approximately four minutes for under fifty cents per subject.
- LLM tools can match anonymous forum accounts to LinkedIn profiles with high accuracy.
- LLMs can infer native language, psychological traits, demographic information, and political orientation from writing samples.
- Cross-platform account correlation — linking a pseudonymous Twitter account to a Reddit account to a GitHub profile — is now automatable.

The government surveillance application: federal agencies that purchase commercial data (social media posts, browsing records, purchase histories, location data — as documented in threat-model.md) now have LLM tooling to analyze these datasets at analyst-scale cost. The ImmigrationOS system's confirmed OSINT and social media monitoring capabilities, combined with Palantir's AIP platform (which deploys LLMs on top of existing government data pipelines), represent a deployed version of this capability.

Palantir's AIP platform is explicitly confirmed in the Army's $10 billion ESA contract and is the integration layer that connects bulk data to AI analysis. The "what can they see" threat matrix in threat-model.md understates the analytical capability by describing raw data access. The more accurate framing: not only can they see the data, they can now process it with LLM agents at the cost of running a query.

Sources: [MIT Technology Review: How LLMs could supercharge mass surveillance (April 2026)](https://www.technologyreview.com/2026/04/21/1135919/ai-surveillance-privacy-llms-bulk-data/); [Palantir AIP platform](https://www.palantir.com/platforms/aip/); [International Journal of Cyber Criminology: LLMs in OSINT cyberterrorism detection](https://cybercrimejournal.com/menuscript/index.php/cybercrimejournal/article/view/389)

---

### OSINT Amplification: What AI Can Infer That Humans Cannot Manually

Roughly 57-64% of OSINT tools now incorporate AI or machine learning components. The operational capability expansion over manual OSINT is qualitative, not just quantitative:

**Image-based inference**: AI-powered OSINT tools automatically extract identities from photos and videos even without text association. A photo posted without a name can be matched against facial recognition databases. EXIF metadata in photos contains geolocation, device model, and timestamp data — AI tools flag inconsistencies automatically.

**Cross-platform entity resolution**: Modern OSINT platforms perform automated entity resolution — linking the same individual's presence across multiple platforms even under different usernames, through linguistic fingerprinting, behavioral pattern matching, and network analysis.

**Relationship graph construction from public data**: An AI OSINT agent scanning the social media of an activist can automatically construct their social graph — identifying associates, mapping organizational affiliations, inferring physical location patterns from check-ins and tagged photos — without any database access beyond what is publicly visible. The OWASP SocialOSINTAgent does this autonomously across Twitter/X, Reddit, Hacker News, Bluesky, GitHub, and Mastodon.

**What can be inferred that individuals do not intend to disclose**: political orientation, physical location home/work patterns, health conditions (from following medical accounts), relationships (from interaction patterns and photo co-occurrence), financial stress indicators, travel patterns, and organizational membership — all from public post metadata and content.

### Practical OpSec Implications

The inference capabilities above translate into specific behavioral patterns to avoid:

1. **Consistent usernames across platforms** enable automated cross-platform deanonymization. Different usernames per platform, with no behavioral links between them, is the baseline compartmentalization.

2. **Posting photos from identifiable locations** allows geolocation inference even without EXIF data. Background elements in photos (buildings, street signs, store fronts) are resolved by AI image analysis to specific geographic coordinates.

3. **Following and liking patterns** are public metadata on most platforms and reveal organizational affiliations and political orientation without any post content. An activist who never posts but follows 200 protest organizations has disclosed their affiliation through follows alone.

4. **Timing patterns in posts** disclose active hours and time zone with high accuracy, narrowing physical location. Consistent posting times correlate with work schedules and domestic patterns.

5. **Language and writing style** is a biometric. LLM tools can match anonymous writing to identified writing samples with increasing accuracy. Activists maintaining pseudonymous blogs should use stylometric countermeasures (varied sentence length, deliberate avoidance of distinctive phrasing patterns) or accept that the pseudonym provides limited protection against sophisticated actors.

Sources: [MIT Technology Review: LLMs and mass surveillance](https://www.technologyreview.com/2026/04/21/1135919/ai-surveillance-privacy-llms-bulk-data/); [Web Asha Technologies: AI-powered OSINT 2026](https://www.webasha.com/blog/blog/ai-powered-osint-tools-in-2025-how-artificial-intelligence-is-transforming-open-source-intelligence-gathering); [OWASP SocialOSINTAgent](https://owasp.org/www-project-social-osint-agent/); [Reuters Institute: AI undermining OSINT assumptions](https://reutersinstitute.politics.ox.ac.uk/news/ai-undermining-osints-core-assumptions-heres-how-journalists-should-adapt)

---

## Part IV: Predictive Policing and Pre-Crime Tools (2026 State)

### Systems Currently in Use

**SoundThinking (ShotSpotter / CrimeTracer)**: SoundThinking is now the dominant vendor in the predictive policing space after acquiring Geolitica (formerly PredPol) in late 2023. The consolidated product combines gunshot detection (acoustic sensor networks) with location-based crime prediction. As of early 2026, ShotSpotter acoustic sensors remain deployed in over 100 U.S. law enforcement agencies. SoundThinking's CrimeTracer product — the former PredPol — generates geographic hotspot predictions based on historical crime data, weather, temporal patterns, and other inputs.

Chicago's experience is instructive: the city ended its ShotSpotter contract in February 2024. A December 2025 analysis found that homicides in the 12 South and West Side neighborhoods where ShotSpotter sensors had operated dropped steeply and continued declining for the full year after removal — contradicting the vendor's claimed crime reduction effects. However, Cambridge, Massachusetts was still facing active pressure from civil liberties advocates in April 2026 to end its contract, and four Greater Los Angeles cities signed new deployments in March 2025.

**Palantir Gotham predictive features**: Gotham's law enforcement deployment (used by FBI, CBP, ICE, and hundreds of state/local agencies) includes geospatial analysis and prediction, alerts, hotspot mapping, and what the company describes as risk scoring. The system ingests arrest records, license plate data, social media, financial and medical data "where permitted," and constructs searchable networks and risk assessments. The Danish POL-INTEL project has been operational since 2017 using Gotham; German state police and Europol also use it. For U.S. domestic use, Gotham's inputs are the same data ecosystem described throughout threat-model.md — ALPR data, CLEAR, commercial data broker feeds — plus direct agency database access.

**Person-based risk scoring (successor to "chronic offender" programs)**: The LAPD's Operation LASER (Location-based Deterrence program) — which assigned numerical scores to individuals — was shut down in 2019 after the inspector general found it impossible to isolate the program's impact. However, person-based scoring remains embedded in the Gotham platform and successor products. These scores are not public, not auditable, and not subject to challenge by the scored individual.

Sources: [WTTW Chicago homicide analysis](https://news.wttw.com/2025/12/29/steep-drop-homicides-continued-full-year-after-shotspotter-was-removed-analysis); [TechPolicy.Press: Politicians move to limit predictive policing](https://www.techpolicy.press/politicians-move-to-limit-predictive-policing-after-years-of-controversial-failures/); [Globe Newswire: LA cities ShotSpotter deployments March 2025](https://www.globenewswire.com/news-release/2025/03/27/3050551/0/en/Four-Greater-Los-Angeles-Cities-Lead-the-Way-with-ShotSpotter-Deployments-to-Protect-Neighborhoods.html); [Harvard Crimson: Cambridge ShotSpotter April 2026](https://www.thecrimson.com/article/2026/4/30/shotspotter-city-council/); [EFF Street Level Surveillance: Predictive Policing](https://sls.eff.org/technologies/predictive-policing)

---

### What Data Feeds Predictive Systems and How to Minimize Your Footprint

Predictive policing systems draw from several data streams that individuals can partially influence:

**Arrest and contact records**: Any police stop, field interview card, or arrest creates a record that feeds predictive systems. Legal counsel strongly advises against engaging with police beyond legally required identification. Every voluntary conversation creates a data record.

**License plate readers (ALPR)**: Already documented in threat-model.md. Palantir ELITE and Gotham ingest ALPR data continuously. Driving patterns, frequented locations, and vehicle associations are automatically logged. Countermeasure: where legal, ALPR camera avoidance routing (apps like DriveSafe can show sensor locations). Rental cars and shared vehicles reduce the direct association between a license plate and a specific individual.

**Location data from mobile advertising identifiers**: As documented in threat-model.md under the ICE MAID procurement RFI, ad-tech location data flows into law enforcement data pipelines. This data feeds predictive systems as a proxy for pattern-of-life analysis. Countermeasure: GrapheneOS or hardened iOS removes advertising identifiers from the data collection pipeline.

**Social media monitoring feeds**: Babel Street, ImmigrationOS, and Gotham all ingest social media monitoring. The predictive inference is behavioral: posts expressing political views, organizational affiliations, or attendance at monitored events create records in these systems.

**Financial transaction data**: Through FinCEN Suspicious Activity Reports, IRS/Palantir LCA, and commercial data broker feeds, financial patterns are visible to predictive systems. Cash for politically sensitive activities reduces this footprint.

---

### Legal Status: Which Jurisdictions Have Banned or Restricted These Tools

**Definitive bans (as of May 2026)**:
- Santa Cruz, California: First U.S. city to ban both predictive policing and facial recognition (June 2020, still in effect)
- Oakland, California: Banned person-based predictive policing; facial recognition ban also in effect
- San Francisco, California: Banned city agency use of facial recognition (2019); predictive policing heavily restricted
- Chicago: Allowed ShotSpotter contract to expire (February 2024); Operation LASER ended 2019

**Active legislative restriction efforts (2026)**:
- Cambridge, Massachusetts: Civil liberties advocates renewing calls to end ShotSpotter contract (April 2026)
- Seven members of Congress (2024 letter) called on DOJ to end funding of predictive policing
- Illinois and Chicago filed a federal lawsuit in January 2026 against Mobile Fortify that, if successful, would establish a legal precedent restricting biometric collection in law enforcement field operations

**Significant gap**: No federal law restricts predictive policing. Most U.S. cities and states have no restriction on these tools. The absence of federal oversight means that a tool banned in San Francisco is in active use by federal agencies (ICE, CBP, FBI) operating in San Francisco.

Sources: [Courthouse News: California city bans predictive policing](https://www.courthousenews.com/california-city-bans-predictive-policing/); [EFF: Cities should ban predictive policing and ShotSpotter](https://www.eff.org/deeplinks/2023/10/cities-should-act-now-ban-predictive-policingand-stop-using-shotspotter-too); [Minnesota Journal of Law & Inequality: AI and predictive policing 2026](https://lawandinequality.org/2026/01/27/fighting-pre-crime-law-enforcement-artificial-intelligence-and-predictive-policing-technology/)

---

## Part V: Defensive Recommendations

Recommendations are graded by threat tier consistent with the rest of this project. Tier 1 = general privacy hygiene for anyone. Tier 2 = elevated risk (activists, immigrant community members, journalists, lawyers). Tier 3 = confirmed investigation targets, high-visibility organizers, individuals in active immigration enforcement proceedings.

---

### Tier 1 (Everyone): Browser Fingerprinting Countermeasures and Social Media Hygiene

**Browser fingerprinting countermeasures**

Traditional incognito mode and cookie clearing do not protect against fingerprinting, which cannot be deleted and persists across sessions. Fingerprinting collects hardware characteristics, screen resolution, installed fonts, GPU rendering signatures, and behavioral micro-patterns — none of which are addressed by clearing browsing data.

Effective countermeasures in order of increasing effectiveness:
- **Firefox with Strict Mode Enhanced Tracking Protection**: Now blocks canvas probes, WebGL fingerprinting, and cross-site tracking scripts. Mozilla completed the second phase of anti-fingerprinting defenses in 2025, reducing the trackable Firefox user population by half.
- **Mullvad Browser**: Built with Tor's anti-fingerprinting technology. Standardizes the observable fingerprint and makes the browser appearance identical across thousands of users — providing anonymity-in-a-crowd rather than uniqueness.
- **Tor Browser**: The strongest anti-fingerprinting protection available. Applies letterboxing, user-agent spoofing, and first-party isolation. Appropriate for high-sensitivity browsing. Slow; not appropriate as primary daily browser.
- Pair any privacy browser with **uBlock Origin** (blocks tracking scripts at the source) and a reputable no-logging VPN to remove IP address as a fallback identifier.

**Social media hygiene**

The inference capabilities described in Part III translate into specific hygiene practices:

- **Disable geotagging** on all devices before taking photos. Strip EXIF metadata before posting any image using a tool like ExifTool or a privacy-focused image sharing service.
- **Separate accounts for separate contexts**. A professional identity and an activist identity should never be linked — different usernames, different devices or browsers, different email accounts, no mutual followers or crossposted content.
- **Assume follows/likes are analyzed**. Following an organization is a disclosed affiliation even with zero posts. Use private lists, RSS feeds, or browser bookmarks for monitoring organizations you do not want associated with your public identity.
- **Minimize event attendance disclosure**. Posting about attending a protest, meeting, or event creates a record of presence at that event in ImmigrationOS, Babel Street, and Gotham pipelines. If attendance could create risk, do not post it.
- **Delete old accounts and posts**. AI OSINT tools analyze historical data. Posts from years ago are still in scope. Use account deletion tools to reduce the historical footprint on platforms that support it.

---

### Tier 2 (Elevated Risk): AI-Resistant Communication Patterns and Synthetic Presence Minimization

**Out-of-band verification is mandatory for all sensitive requests**

Any unexpected request for credentials, location disclosure, meeting, legal strategy discussion, or fund transfer — regardless of how convincingly it appears to come from a trusted contact — must be verified through a pre-established second channel.

Specific protocols:
- If someone calls claiming to be your attorney or organizational security contact, hang up and call their published number independently. Do not call back a number provided in the message.
- If an email requests you click any link, navigate directly to the site by typing the address. AI-generated phishing correctly references real details about the target — authentic-looking context is no longer a signal of legitimacy.
- **Pre-establish code words with key contacts** (attorney, organizational security contact, emergency contact). Any unexpected call requesting sensitive action should trigger the challenge. The code word system is the only reliable voice identity verification method when calls cannot be made through confirmed-secure channels.

**Synthetic presence minimization**

Activists who maintain a public presence (podcast appearances, video interviews, published writing) are providing raw material for voice cloning and stylometric analysis. This cannot be fully eliminated for public-facing organizers, but it can be managed:

- **Assume your voice is clonable** from any public audio. Build verification practices that do not rely on voice recognition — the code word system above is the correct solution.
- **Pseudonymous public identities**: Any public audio or video appearance by a pseudonymous activist provides voice and potentially face data that can defeat the pseudonym. If a pseudonymous identity must remain secure against nation-state actors, no public audio or video appearances under that identity.
- **Compartmentalize writing style**: For pseudonymous written material, use deliberate stylometric countermeasures — vary sentence length, avoid distinctive phrases and idioms present in your identified writing, use a second reader to flag unconscious stylistic signatures.

**Deepfake social engineering response protocol**

Activists should establish this protocol before it is needed:

1. If you receive fabricated audio or video claiming to show you making damaging statements: do not engage publicly before legal consultation.
2. Preserve the fabrication with metadata intact (do not screenshot; preserve the original URL and access log if possible).
3. Report to EFF's digital security helpline or a trusted legal contact.
4. Notify your organization's security contact — fabricated material targeting one member is often part of a broader harassment operation.

**Data broker opt-out as baseline**

The data broker opt-out process documented in osint-data-broker-deepening.md reduces the inputs available to predictive systems and identity resolution tools. For Tier 2 individuals, completing the major data broker opt-outs (Spokeo, WhitePages, Intelius, BeenVerified, MyLife) removes the most accessible commercial data layer before it can be purchased by agencies without a warrant.

---

### Tier 3 (High Risk): Physical Countermeasures and Air-Gapped Device Protocols

**Physical countermeasures at public events**

For individuals at confirmed elevated risk of Mobile Fortify or Clearview AI scanning at public events:

- Wear a mask (N95 or cloth) and sunglasses together as a baseline. This combination obstructs the facial landmarks required for recognition template construction.
- Know your state's anti-mask law status before attending a protest. States with anti-mask laws typically include exceptions for health-related masking, but enforcement is discretionary.
- Wear clothing that provides consistent, unremarkable appearance without distinctive identifying features (logos, distinctive colors). This counters both human identification and AI-assisted identification from footage review.
- **Gait countermeasures**: Alter footwear from your daily baseline (different shoe type or heel height changes gait signature). Bulky layered clothing degrades gait recognition accuracy. These measures are imperfect but add friction.
- **Electronic device protocol at high-risk events**: Follow the existing device-hardening-guide.md protocol — leave primary phone at home or in a Faraday bag, bring a secondary hardened device with no account logins, airplane mode when not actively needed. This addresses IMSI catcher capture, ALPR correlation, and ad-tech MAID location data collection simultaneously.

**Air-gapped device protocols for sensitive communications**

For individuals managing information whose exposure would create direct physical risk:

- Use a dedicated air-gapped device (never connected to any network) for drafting, storing, and processing the most sensitive materials. Transfer via USB is the only data movement method; the USB device itself should be dedicated and never connected to a networked machine.
- For communication with legal counsel in active proceedings: Signal on a dedicated device (secondary SIM or Wi-Fi only) used only for that relationship. Do not mix communications from this device with any other personal or organizational communications.
- The Qubes OS installation on Nitrokey-certified ThinkPad hardware (documented in hardware-procurement-guide.md) provides compartmentalized computing environments for Tier 3 use cases. Application compromise in one compartment cannot access data in another.

**Facial recognition avoidance in travel contexts**

CBP and TSA facial recognition systems at airports are actively expanding. For individuals who wish to avoid enrollment in the biometric exit-entry database:

- CBP's facial recognition system at airports is currently voluntary for U.S. citizens (you may opt out and use standard document inspection instead). Assert this right — agents may not proactively inform you of it.
- Keep a record of any facial recognition match that appears incorrect or that results in additional screening. Document the agency, location, date, and time. This data is relevant if you later need to challenge a record.
- For Tier 3 individuals traveling internationally, be aware that facial recognition data collected at border crossings is retained and accessible to the Palantir Gotham/ELITE system and to CBP's biometric database for at least 75 years (standard biometric retention policy).

---

## Confidence Assessment and Gaps

**High confidence** (primary source documentation): All federal deployment details, contract values, the NIST demographic accuracy research, the WEF deepfake KYC testing findings, the MIT Technology Review LLM surveillance analysis, and the wrongful arrest documentation.

**Medium confidence** (research-consistent but limited deployment documentation): The real-world operational effectiveness of adversarial makeup against current deployed systems. Laboratory results are documented; field effectiveness against specific vendor implementations is not confirmed.

**Confirmed gap**: The specific AI/ML models underlying Palantir's address confidence scores and ImmigrationOS targeting priorities have not been independently audited or publicly disclosed. The false positive rates of these systems for specific demographics are unknown.

**Confirmed gap**: The extent to which gait recognition is currently deployed by U.S. federal agencies at domestic public events is not confirmed. Chinese deployment is confirmed and documented; U.S. federal deployment at scale is not.

**Confirmed gap**: The specific technical architecture connecting Palantir AIP to the social media monitoring feeds (Babel Street, ImmigrationOS) is not publicly documented. The existence of these connections is confirmed; the data flow architecture is not.

---

## Key Sources

- [404 Media: Inside ICE's Supercharged Facial Recognition App of 200 Million Images](https://www.404media.co/inside-ices-supercharged-facial-recognition-app-of-200-million-images/)
- [ACLU: Face Recognition and the Trump Terror](https://www.aclu.org/news/privacy-technology/ice-face-recognition)
- [ACLU: More Than a Dozen Wrongful Arrests Due to Facial Recognition](https://www.aclu.org/news/privacy-technology/more-than-a-dozen-wrongful-arrests-due-to-police-reliance-on-facial-recognition-technology)
- [EPIC Coalition Letter on ICE Mobile Fortify (November 2025)](https://epic.org/wp-content/uploads/2025/11/Coalition-Letter-on-ICE-Mobile-Fortify-FRT-Nov2025.pdf)
- [NIST FRVT Part 3: Demographic Effects (NISTIR 8280)](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf)
- [ArXiv: Facial recognition accuracy in low-quality police images (2025)](https://arxiv.org/html/2505.14320v1)
- [WEF: Unmasking Cybercrime — Deepfakes and KYC Testing (January 2026)](https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf)
- [MIT Technology Review: How LLMs could supercharge mass surveillance (April 2026)](https://www.technologyreview.com/2026/04/21/1135919/ai-surveillance-privacy-llms-bulk-data/)
- [Fortune: 2026 voice cloning indistinguishable threshold](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/)
- [RSF: 100 deepfakes targeting journalists (2023-2025)](https://rsf.org/en/rsf-analysis-100-deepfakes-shows-mounting-threat-journalists-especially-women)
- [Microsoft 2025 Digital Defense Report: AI phishing 4.5x more effective (via Paubox)](https://www.paubox.com/blog/microsoft-ai-makes-phishing-4.5x-more-effective-and-far-more-profitable)
- [ABA Banking Journal: Voice biometric vulnerabilities in the age of deepfakes](https://bankingjournal.aba.com/2024/02/challenges-in-voice-biometrics-vulnerabilities-in-the-age-of-deepfakes/)
- [WTTW Chicago: Homicides continued to drop after ShotSpotter removal (December 2025)](https://news.wttw.com/2025/12/29/steep-drop-homicides-continued-full-year-after-shotspotter-was-removed-analysis)
- [TechPolicy.Press: Politicians move to limit predictive policing](https://www.techpolicy.press/politicians-move-to-limit-predictive-policing-after-years-of-controversial-failures/)
- [EFF: Cities should ban predictive policing and ShotSpotter](https://www.eff.org/deeplinks/2023/10/cities-should-act-now-ban-predictive-policingand-stop-using-shotspotter-too)
- [Mozilla Blog: Firefox fingerprinting protections](https://blog.mozilla.org/en/firefox/fingerprinting-protections/)
- [American Immigration Council: ICE AI surveillance tracking Americans](https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/)
- [Minnesota Journal of Law & Inequality: AI in predictive policing (January 2026)](https://lawandinequality.org/2026/01/27/fighting-pre-crime-law-enforcement-artificial-intelligence-and-predictive-policing-technology/)
- [Democracy Now: ICE agents film protesters with Mobile Fortify (January 2026)](https://www.democracynow.org/2026/1/29/ice_cbp_facial_recognition_technology_app)
