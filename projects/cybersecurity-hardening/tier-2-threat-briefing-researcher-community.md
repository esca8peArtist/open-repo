---
title: "Tier 2 Threat Briefing: Researcher Communities"
project: cybersecurity-hardening
created: 2026-05-06
status: ready-for-distribution
audience: Researcher communities — Citizen Lab, Stanford Internet Observatory, Johns Hopkins CISA, MIT Media Lab, UC Berkeley School of Information
distribution-tier: Tier 2 — Researcher Sector
depends-on: may-2026-advanced-threats.md, may-2026-threat-update.md, ITEM14_TIER2_MESSAGING_ANALYSIS.md
---

# Technical Briefing: May 2026 Threat Landscape — Dataset and Analysis Opportunities

**For**: Research communities at Citizen Lab, Stanford Internet Observatory, Johns Hopkins Security Institute, MIT Media Lab, and UC Berkeley School of Information

**Date**: May 2026

**Prepared by**: Cybersecurity Hardening Project (public-source research corpus)

**Format**: Peer-oriented technical briefing. All claims sourced to primary or near-primary sources. Confidence gaps flagged per section. Framed as research invitation, not threat advisory.

---

## Opening Orientation

This briefing covers four threat areas that emerged or materially developed in Q1–Q2 2026 and present tractable research problems with publicly available datasets, open-source tooling, and near-term publication opportunities. Each section closes with dataset pointers, analytical entry points, and relevant conference submission angles.

The four areas are structurally connected: synthetic identity fraud, supply chain attacks, election infrastructure degradation, and government surveillance expansion all converge on a common problem — the verification and trust infrastructure on which digital society runs is being attacked from multiple angles simultaneously, by actors ranging from a $629/year subscription service to nation-state firmware developers to a federal agency with a $1B blanket purchasing agreement.

---

## Part I: Synthetic Identity Detection — Datasets, Benchmarks, and the ProKYC Problem

### The Technical Landscape

The ProKYC platform (documented by Cato CTRL researchers) executes a complete synthetic identity attack chain as a commercial subscription:

1. Generates fraudulent identity documents from real breach-sourced SSN fragments + fabricated biometrics
2. Produces a matching deepfake video persona
3. Injects the deepfake as a real-time webcam feed into identity verification liveness checks
4. Supplements with voice synthesis using 3 seconds of audio from any public source

The liveness bypass has been confirmed against Binance, Bybit, and OKX. The voice cloning component uses APIs from ElevenLabs, xAI, OpenAI, and Microsoft with synthesis latency below 500ms — enabling real-time conversation, not playback of pre-recorded audio.

**The detection failure numbers**: Human detection of high-quality video deepfakes is below 30% accuracy. AI classifiers lose up to 50% accuracy under adversarial real-world conditions. Voice biometric systems are defeated by Time-domain Voice Identity Morphing (TD-VIM), which blends voice characteristics at the signal level without requiring access to the target's biometric embedding — defeating closed biometric verification systems.

### Publicly Available Datasets

| Dataset | Contents | Access | Relevance |
|---------|----------|--------|-----------|
| FaceForensics++ | 1,000 original videos + manipulated versions (DeepFakes, Face2Face, FaceSwap, NeuralTextures) | https://github.com/ondyari/FaceForensics | Foundational deepfake detection benchmark |
| DFDC (DeepFake Detection Challenge) | 128,154 video clips, 5,639 subjects (Facebook/Meta, 2020) | https://ai.meta.com/datasets/dfdc/ | Large-scale, diverse; generalization benchmark |
| WildDeepfake | 7,314 face sequences extracted from internet-sourced deepfake videos | https://github.com/deepfakeinthewild/deepfakeinthewild | In-the-wild distribution, higher adversarial realism |
| ASVspoof 2019 / 2021 | Voice spoofing and anti-spoofing challenge data (logical access + physical access) | https://datasharing.spsc.tugraz.at/dataset/asvspoof-2019 | Standard voice anti-spoofing benchmark |
| ADD 2022 (Audio Deep Synthesis Detection) | 1.4M utterances including partially fake audio | https://github.com/audio-deepfake-detection | Partially-fake audio (mixing real and synthetic segments) |
| VoxCeleb 1/2 | 7,000+ celebrity speakers, YouTube-sourced | https://www.robots.ox.ac.uk/~vgg/data/voxceleb/ | Speaker verification baseline; voice clone source material |

**Gap**: No public dataset specifically modeling the ProKYC attack chain as an end-to-end workflow — synthetic document generation + face synthesis + real-time injection into a verification pipeline. The adversarial realism of commercially-deployed tools ($629/year, trained on production bypass data) likely exceeds benchmarks trained on earlier-generation synthetic tools.

### Model Benchmarks and Key Prior Work

- **FaceSwap-KoDF** (Kim et al., 2021): Korean deepfake dataset, important for non-English-face generalization
- **Detecting Deep-Fake Videos from Appearance and Behavior** (Agarwal et al., IEEE CVPR 2020): behavior-based approach (blink rate, head pose) that is now defeated by ProKYC-class tools
- **Lips Don't Lie: A Generalisable and Robust Approach to Face Forgery Detection** (Haliassos et al., CVPR 2021): lip-sync consistency detection — relevant to real-time injection defenses
- **The WEF Cybercrime Atlas (2026)**: Documents camera injection defeating commercial liveness systems — the best current synthesis of deployed capability vs. deployed defense

**Critical gap in current benchmarks**: TD-VIM (Time-domain Voice Identity Morphing) is documented in the Biometric Update literature but does not yet appear as an adversarial attack variant in standard anti-spoofing challenge datasets. This is an accessible research contribution: generate TD-VIM variants against ASVspoof baselines and document the detection failure rate.

### Code Repository Pointers

- Deepfake detection baseline implementations: https://github.com/ondyari/FaceForensics (authors' baseline models)
- AASIST anti-spoofing: https://github.com/clovaai/aasist (current SOTA on ASVspoof 2019)
- RawBoost anti-spoofing data augmentation: https://github.com/TakHemlata/RawBoost
- WEF Cybercrime Atlas tools: https://www.weforum.org/projects/cybercrime-atlas (research consortium, not public code repo — contact point for data access)

### Conference CFP Angles

**IEEE S&P 2027 (deadlines typically November–December 2026)**: "Adversarial robustness of multimodal deepfake detectors under commercial attack toolchain" — framing the ProKYC chain as a structured adversarial attack against multimodal systems fits S&P's systems security framing.

**USENIX Security 2027 (summer 2026 deadline)**: "End-to-end synthetic identity fraud: Threat modeling the ProKYC attack surface against deployed verification systems" — USENIX security has published identity verification research extensively; a threat model grounded in a commercially deployed adversarial tool is within scope.

**ACM CCS 2026 (deadline typically May 2026 — check current CFP)**: "Voice identity morphing at test time: Defeating speaker verification without enrolled biometric access" — specifically addresses the TD-VIM gap in ASVspoof benchmarks.

---

## Part II: Supply Chain Attack Forensics — Malware Signatures and Analysis Playbooks

### The Shai-Hulud Campaign: What Forensic Evidence Is Public

The Shai-Hulud campaign (TeamPCP threat actor) executed three waves across September 2025, November 2025, and April–May 2026. The publicly documented forensic artifacts:

**Wave 1 npm tradecraft** (documented by Microsoft Security Blog):
- Install-time execution via `preinstall` and `postinstall` hooks
- Bun-based payload launcher (Bun runtime included in package to avoid Node.js dependency)
- Heavily obfuscated JavaScript with string manipulation designed to evade static analysis
- Credential harvesting scope: environment variables, `~/.aws/`, `~/.npmrc`, `~/.ssh/`, browser storage, cryptocurrency wallets
- Exfiltration endpoint: attacker-controlled GitHub repository (authenticated via stolen token — traffic indistinguishable from legitimate GitHub API calls)

**Wave 3 / Mini Shai-Hulud PHP tradecraft** (documented by Sophos):
- Identical architecture to npm Wave 1 (install-time execution, obfuscated payload, GitHub exfiltration)
- PHP-specific targets: composer.json-defined install hooks, PSR-4 autoloaded malicious classes
- SAP CAP targets: @sap/cds package ecosystem — enterprise-specific credential scope (SAP HANA credentials, BTP service keys)

**Bitwarden CLI (April 22) GitHub Action vector** (documented by Endor Labs):
- Compromised `tj-actions/changed-files@v46` GitHub Action
- Malicious code appended to the Action's entrypoint script
- Triggered on all repositories using the Action in any workflow
- Payload exfiltrated repository secrets to the Action's run logs — then accessible to the attacker via the GitHub API

**BootKitty UEFI forensics** (documented by Binarly and BleepingComputer):
- Malicious UEFI application targeting `shim` bootloader (UEFI Secure Boot chain)
- Exploits CVE-2023-40238 (Logofail variant in Insyde firmware's BmpDecoderDxe module)
- Injects rogue certificates into UEFI variables: `MokList`, `SBAT` entries
- Kernel modification: patches `integrity_validate_mok_list()` to accept unsigned modules
- Persistence: survives OS reinstall, disk encryption, Secure Boot re-enrollment without firmware update
- Scope: specific Ubuntu kernel versions at discovery (likely broader with production-grade implementation)

### Analysis Playbooks

**For npm/PyPI package compromise detection**:

1. Extract all packages installed in the April 21–May 31 window from `package-lock.json` or `yarn.lock` diffs
2. Cross-reference against Socket.dev's package health scores (https://socket.dev) — Socket integrates with GitHub and flags malicious packages at PR review time
3. For each flagged package: extract install scripts (`preinstall`, `postinstall`, `install`) and scan for Bun runtime inclusion, string obfuscation patterns (`charCodeAt`, `fromCharCode` chains), and environment variable enumeration
4. Check GitGuardian's dataset of exposed secrets (https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/) for any leaked credentials matching your organization's patterns

**For BootKitty / LogoFAIL detection**:

1. Binarly's UEFI firmware analysis tool (https://fwcheck.binarly.io) scans UEFI firmware images for LogoFAIL-vulnerable components — free for individual device analysis
2. Check for unexpected UEFI variable modifications: `mokutil --list-enrolled-keys` and compare against known-good state
3. Kernel module signature verification: `modinfo <module>` for unexpected unsigned modules; `dmesg | grep "module verification failed"` for recent load attempts
4. UEFI event log analysis: `journalctl -b 0 -k | grep -i uefi` for anomalous boot sequence events

**For CI/CD pipeline credential assessment**:

1. Audit GitHub Action references in all workflow files — any action pinned to a tag (v46) rather than a commit SHA is vulnerable to tag-moved compromise (the Bitwarden attack vector)
2. Enumerate all repository secrets and environment variables accessible from workflow runs — these are in scope for exfiltration if any workflow step is compromised
3. OIDC token assessment: workflows using long-lived `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` patterns should migrate to OIDC-based short-lived token generation

### Open Research Questions in Supply Chain Forensics

1. **Supply chain worm propagation modeling**: The CanisterSprawl npm worm (Shai-Hulud Wave 3) self-publishes to every package a compromised maintainer controls, using their existing signing credentials. Epidemic modeling of worm spread through package maintainer networks — using the documented npm dependency graph — would produce actionable data about containment strategies.

2. **GitHub exfiltration detection**: Shai-Hulud exfiltrates credentials to attacker-controlled GitHub repositories, bypassing enterprise egress monitoring that blocks traditional C2 domains. A detection research contribution: characterize the traffic patterns of legitimate GitHub API calls vs. credential exfiltration API calls. GitHub's API rate limits, repository creation patterns, and commit timing distributions may distinguish the two.

3. **UEFI patch deployment rates**: The LogoFAIL vulnerability scope (95% of x86 devices potentially affected) and the BootKitty exploitation confirm that UEFI patch deployment is a public health problem, not just an individual security hygiene problem. A measurement study of UEFI firmware version distributions across internet-connected devices would quantify the unpatched attack surface.

---

## Part III: Election Infrastructure Vulnerability — CISA Capability Loss as Research Opportunity

### The Defense Vacuum

CISA has lost approximately one-third of its workforce (3,400 → 2,400). The EI-ISAC — which provided threat intelligence to election offices — was defunded. The NSA/Cyber Command Election Security Group has not been reconvened for the 2026 midterm cycle. The IC annual threat assessment did not mention foreign election threats for the first time since 2016.

The external threat environment has not diminished:

- Russia's information operations budget increased 54% ($458M additional)
- China's AI-enabled "Cognitive Domain" campaign projected above $10B annually
- The NRSC deployed sustained deepfake political video in at least five 2026 Senate races — establishing domestic political actor precedent for synthetic content deployment

For research institutions: this gap creates both a research obligation and a research opportunity. Academic institutions are now among the best-positioned external actors to do the threat modeling that federal agencies are no longer doing.

### Research Opportunities

**Black-box threat modeling from external vantage point**:

The absence of classified intelligence access does not preclude rigorous threat modeling. Several data sources remain available:

- **Open-source foreign influence operation detection**: Twitter/X's published state-linked information operations datasets (https://transparency.twitter.com/en/reports/information-operations.html) include content from Russian, Chinese, and Iranian operations — analyzable for 2026 midterm targeting patterns
- **Voting infrastructure vulnerability disclosure**: CVE database entries for election management systems; vendor security advisories; state incident reports (where available from states that do report to alternative channels)
- **Precinct-level election results anomaly detection**: Historical precinct-level data from MIT Election Data and Science Lab (https://electionlab.mit.edu/data) enables baseline modeling; anomalies in 2026 results would be detectable against historical patterns

**Trust architecture research**:

The Votebeat reporting documenting the collapse of CISA-state election official trust is the entry point for a research design question: what alternative federal-state coordination architectures would function without routing through a single federal agency? Graph-theoretic models of information sharing networks in a multi-hub configuration, with empirical grounding in how peer information sharing (state-to-state, through organizations like NASS and NACO) has functioned historically, would contribute to policy design.

**Deepfake political content detection, calibrated for political distribution**:

Standard deepfake detection benchmarks use entertainment content (celebrity face swaps). Politically deployed synthetic content differs in distribution: it is targeted at specific geographic audiences, deployed on specific platforms (Twitter, Facebook, local news embeds), and formatted for political advertising rather than entertainment. A detection system calibrated for political deployment patterns — platform-specific compression artifacts, geo-targeted delivery metadata, political ad disclosure format (the three-second "AI GENERATED" text) — is both technically novel and policy-relevant.

---

## Part IV: Palantir Surveillance Capabilities — Publicly Documented Contracts and Accountability Framework

### The Public Record

Palantir's government surveillance capabilities are documented more extensively in public records than is commonly acknowledged in the research literature. The primary source categories:

**FOIA-obtained contracts and procurement documents**:
- ICE ELITE contract ($29.9M): Available via government contracting databases (USASpending.gov, FPDS)
- ICE ImmigrationOS ($30M): immpolicytracking.org tracks procurement documentation
- USDA $300M BPA: CNBC (April 22, 2026) reports; USASpending.gov for procurement details
- Maven Smart System Enterprise Agreement ($10B Army): DefenseScoop (April 2026) documentation of program-of-record designation

**Court filings**:
- IRS–ICE data sharing injunction (U.S. District Judge Talwani, February 5, 2026): Available via PACER for the D.C. District Court filing
- D.C. Circuit appeal declining to maintain injunction (February 24, 2026): Circuit court docket
- ACLU v. DOJ voter database: ACLU case filing page

**Government contract database queries**:

```
# USASpending.gov queries for documented Palantir contracts
Recipient: Palantir Technologies
Agency: Department of Homeland Security → $1B BPA
Agency: Department of the Army → Maven EA ($10B)
Agency: USDA → $300M BPA
Agency: IRS Criminal Investigation → LCA contract ($130M+)
Agency: ICE → ELITE, ImmigrationOS, ICM sole-source (pending)

Note: Solo-source ICM contract is pending award; track via FPDS.gov for award date
```

**Published vendor documentation and press releases**:
- Palantir's "Correcting the Record" blog post (response to EFF January 2026 report): https://blog.palantir.com/correcting-the-record-response-to-the-eff-january-15-2026-report-on-palantir-4b3a12536cd2
- Palantir investor materials describing Maven capabilities: SEC filings (10-K, 10-Q) available at sec.gov
- Feinberg memorandum designating Maven as program-of-record: DefenseScoop coverage with document excerpts

### Academic Accountability Measurement Framework

Measuring government contractor adherence to self-stated human rights policies against public contract documentation is a tractable research design:

**Palantir as primary test case**:
- Palantir's published Human Rights Policy (https://www.palantir.com/human-rights-policy/) commits to "respect for the laws of war," "avoiding complicity in human rights abuses," and regular human rights impact assessments
- EFF's April 2026 letter to Palantir asking how the human rights policy applies to its ICE work received no substantive response
- House Democrats' April 2026 letter to DHS demanding explanation of Palantir surveillance tool deployment received no substantive response

**Measurement approach**: Document the gap between self-stated policy and publicly documented contract behavior. Compare against other contractor human rights policies (Microsoft, Amazon, Google all have published policies). Develop a rubric for measuring policy-practice gaps that could generalize to other contractor accountability research.

**Data sources for the measurement study**:
1. Contractor human rights policies (public, on corporate websites)
2. Contract specifications from USASpending.gov / FPDS.gov
3. Court filings describing system capabilities (IRS, ICE dockets)
4. FOIA-obtained procurement documents (EFF, ACLU, STOP have obtained and published significant documentation)
5. Congressional testimony (accessible via congress.gov for hearings where Palantir or its contractors have testified)

### Publication Strategy for Sensitive Findings

Research on active government surveillance systems raises several publication ethics considerations that the field has engaged with since USENIX Security introduced mandatory ethics review sections in 2025:

**Defensible ethics posture**: Research that documents publicly available information about government surveillance capabilities for the purpose of enabling accurate threat modeling by civil society organizations is defensible under information asymmetry principles — the government agency has substantial information about its own capabilities; the public does not; reducing that asymmetry serves public accountability.

**Sensitive data handling**: Research that involves real data about surveillance targets (rather than documentation of surveillance system capabilities) requires IRB review and careful handling. Capability documentation from public sources does not.

**Coordinated disclosure with civil society**: Research findings with immediate operational implications for at-risk populations (e.g., a newly discovered capability that invalidates an existing countermeasure) should be shared with civil society organizations (EFF, Access Now Digital Security Helpline) concurrently with or before public publication, allowing time for countermeasure updates.

**Venue selection for politically sensitive work**: IEEE S&P has published election security research with immediate policy implications (Defcon Voting Village research, EAC technical standards work). ACM CCS has published government surveillance documentation research. USENIX Security's ethics section is the most developed in the field and provides guidance language for navigating the policy implications of surveillance research.

---

## Data Sharing Protocols and Collaboration Opportunities

The research areas above would benefit from collaboration across institutions with complementary expertise:

**Citizen Lab**: Leads on government surveillance technical documentation, particularly attribution and capability characterization of state-linked surveillance tools. Citizen Lab's existing relationships with EFF and Access Now Digital Security Helpline create a civil society integration pathway for research findings.

**Stanford Internet Observatory (SIO)**: Foreign influence operation detection research and deepfake political content analysis are SIO's core research areas. Cross-institutional collaboration on 2026 midterm influence operation detection — sharing open-source data against Stanford's classification frameworks — is a natural extension of existing SIO work.

**Johns Hopkins CISA**: Election security technical analysis, including infrastructure vulnerability research, aligns with JHCISA's applied security mission. The CISA capability loss creates an opening for academic external vantage point threat modeling that JHCISA is well-positioned to lead.

**MIT Media Lab**: Deepfake detection, synthetic media attribution, and the intersection of AI-generated content with political behavior research has deep lineage at the Media Lab. The ProKYC attack chain's multimodal architecture is a direct research target for Media Lab's synthetic media detection work.

**UC Berkeley School of Information**: Privacy policy research, commercial data broker ecosystem documentation, and the intersection of surveillance technology with marginalized populations are I School research areas. The Palantir accountability measurement framework described above maps directly onto I School faculty interests (notably Deirdre Mulligan, who testified at California's March 2026 Privacy in the Age of Mass Surveillance hearing).

**Conference submission coordination**: IEEE S&P, USENIX Security, and ACM CCS all have double-blind review processes that permit simultaneous submission to one venue at a time. For research with both technical and policy dimensions, consider parallel or sequential submission to a technical venue and a policy venue (e.g., WPES — Workshop on Privacy in the Electronic Society, co-located with CCS; USENIX HotSec for early-stage ideas).

---

## Upcoming Deadlines

| Conference | Submission Deadline | Notification | Venue |
|-----------|--------------------|-----------|----|
| ACM CCS 2026 | May 14, 2026 (paper) / June 18 (second cycle) | Check CFP | Salt Lake City, UT |
| USENIX Security 2027 | Summer 2026 (check usenix.org/conference/usenixsecurity27) | — | — |
| IEEE S&P 2027 | November–December 2026 (typically) | — | San Francisco, CA |
| NDSS 2027 | September 2026 (typically) | — | San Diego, CA |
| CCC 40C3 (Chaos Communication Congress) | Summer 2026 (talk submissions) | — | Hamburg, Germany |
| DEF CON 34 | CFP opens late 2025 / closes spring 2026 | — | Las Vegas, NV |

*Note: Check current CFP pages directly — deadlines shift. CCC 40C3 is December 2026; DEF CON 34 is August 2026.*

---

## Sources

1. Cato Networks: ProKYC — Selling Deepfake Tool for Account Fraud Attacks — https://www.catonetworks.com/blog/prokyc-selling-deepfake-tool-for-account-fraud-attacks/
2. Biometric Update: Voice Morphing Attack Blends Identities to Bypass Voice Biometrics (April 2026) — https://www.biometricupdate.com/202604/voice-morphing-attack-blends-identities-to-bypass-voice-biometrics-study
3. WEF: Unmasking Cybercrime (January 2026) — https://reports.weforum.org/docs/WEF_Unmasking_Cybercrime_Strengthening_Digital_Identity_Verification_against_Deepfakes_2026.pdf
4. Microsoft Security Blog: Shai-Hulud 2.0 — https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/
5. Endor Labs: Bitwarden CLI Supply Chain Attack — https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack
6. Sophos: Mini Shai-Hulud SAP npm Packages — https://www.sophos.com/en-us/blog/-mini-shai-hulud-supply-chain-attack-targets-sap-npm-packages
7. Binarly: LogoFAIL Exploited to Deploy Bootkitty — https://www.binarly.io/blog/logofail-exploited-to-deploy-bootkitty-the-first-uefi-bootkit-for-linux
8. BleepingComputer: BootKitty UEFI Malware Exploits LogoFAIL — https://www.bleepingcomputer.com/news/security/bootkitty-uefi-malware-exploits-logofail-to-infect-linux-systems/
9. Group-IB: Six Supply Chain Attack Groups 2026 — https://www.group-ib.com/blog/supply-chain-attack-groups-2026/
10. Votebeat: CISA Election Security Trust Is Broken (January 2026) — https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/
11. CNN: US Cyber Team Not Yet Activated (April 2026) — https://www.cnn.com/2026/04/30/politics/cyber-team-midterm-elections-foreign-meddling
12. The Hill: China, Russia, Iran Investing Billions to Influence US Midterms — https://thehill.com/opinion/cybersecurity/5713097-china-russia-iran-influence/
13. EFF: Palantir Has a Human Rights Policy — Its ICE Work Tells a Different Story (April 2026) — https://www.eff.org/deeplinks/2026/04/palantir-has-human-rights-policy-its-ice-work-tells-different-story
14. The Intercept: Palantir Helping Trump IRS Conduct Massive-Scale Data Mining (April 2026) — https://theintercept.com/2026/04/24/palantir-irs-contract-data/
15. DefenseScoop: Maven Smart System Pentagon Program Transition (April 2026) — https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/
16. CNBC: Palantir $300M USDA Deal (April 2026) — https://www.cnbc.com/2026/04/22/palantir-inks-300-million-deal-with-usda-to-safeguard-food-supply.html
17. Palantir: Correcting the Record (January 2026) — https://blog.palantir.com/correcting-the-record-response-to-the-eff-january-15-2026-report-on-palantir-4b3a12536cd2
18. Help Net Security: Cybersecurity Research Ethics Rules (September 2025) — https://www.helpnetsecurity.com/2025/09/08/cybersecurity-research-ethics/
19. CDT: Countdown to the Midterms (2026) — https://cdt.org/insights/countdown-to-the-midterms-mapping-the-rapid-evolution-of-election-security/
20. ACLU: All the Ways Palantir Is Assisting Trump's Abusive Removal Campaign — https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup
