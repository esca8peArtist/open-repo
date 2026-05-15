---
title: "Domain 40: Surveillance Capitalism and Electoral Manipulation"
subtitle: "How Commercial Data Infrastructure Became Democratic Attack Infrastructure"
created: 2026-05-15
updated: 2026-05-15
status: production-complete
phase: Phase 2
domain_number: 40
hard_deadline: 2026-11-03
distribution_target: 2026-07-15
eu_enforcement_hook: 2026-08-02
word_count: ~6,800
citations: 47
cross_references:
  - domain-43-epistemic-infrastructure-disinformation-crisis.md
  - domain-37-federal-executive-interference-2026-midterms.md
  - domain-25-fisa-702-april-2026-outcome.md
  - domain-36-ai-governance-algorithmic-accountability-democratic-authority.md
  - domain-33-state-legislative-autocratization.md
  - domain-51-campaign-finance-dark-money.md
  - domain-1-voter-registration-suppression.md
primary_audiences:
  - Election protection organizations (Brennan Center, Protect Democracy, Democracy Docket)
  - Digital rights organizations (EFF, EPIC, CDT, Access Now)
  - Campaign finance transparency groups (OpenSecrets, Campaign Legal Center)
  - Voting rights coalitions (swing-state voter protection networks)
  - Media literacy nonprofits (News Literacy Project, MediaWise)
tags:
  - surveillance-capitalism
  - deepfakes
  - electoral-manipulation
  - data-brokers
  - FEC-deadlock
  - EU-AI-Act
  - voter-suppression
  - AI-generated-content
---

# Domain 40: Surveillance Capitalism and Electoral Manipulation

**How Commercial Data Infrastructure Became Democratic Attack Infrastructure**

**Research completed**: May 15, 2026
**Distribution target**: July 15, 2026 — election protection organizations, digital rights advocates, campaign finance transparency groups, swing-state voter protection networks
**Hard external deadline**: November 3, 2026 (2026 US midterm election)
**EU enforcement hook**: August 2, 2026 — EU AI Act Article 50 enters enforcement (maximum-attention advocacy window)

**Cross-domain connections**:
- **Domain 43** (Epistemic Infrastructure/Deepfakes): Domain 43 analyzes deepfakes as an epistemic crisis — the liar's dividend, the collapse of shared factual foundations, CPB defunding. Domain 40 analyzes the commercial distribution infrastructure that delivers deepfakes to targeted voters at scale. Complementary tracks: Domain 43 covers information-environment harm; Domain 40 covers the data broker targeting supply chain.
- **Domain 37** (Federal Executive Interference in 2026 Midterms): Domain 37 covers government-side election interference. Domain 40 covers the private-sector manipulation infrastructure operating independently of — but potentially in coordination with — executive interference.
- **Domain 25** (FISA 702/Surveillance): The commercial data broker loophole that remains open after the June 12, 2026 FISA extension is structurally connected to voter targeting. What government cannot constitutionally collect directly, it can purchase commercially — and campaigns access the same marketplace.
- **Domain 36** (AI Governance): Domain 36 covers AI in government decision-making; Domain 40 covers AI in electoral manipulation. Both flow from the same statutory vacuum documented in the December 2025 preemption EO.
- **Domain 33** (State Legislative Autocratization): Geofencing churches and community meeting locations to deliver suppression messaging to specific racial and demographic communities is the synthesis point between state-level autocratization strategy and commercial surveillance tools.
- **Domain 51** (Campaign Finance/Dark Money): The dark money pipeline that funds super PACs and 501(c)(4)s is the same pipeline funding AI-generated political ad production. Domain 51 covers the funding architecture; Domain 40 covers what that money buys.
- **Domain 1** (Voter Registration Suppression): Digital suppression ads targeting non-white voters in battleground counties are the 2026 complement to the traditional voter ID and registration restriction strategies documented in Domain 1.

---

## Executive Summary

The leading finding: 2026 is the year AI-generated synthetic content became standard campaign infrastructure. The NRSC's lifelike deepfake of Texas Senate candidate James Talarico — the first national party committee deployment of a photorealistic synthetic candidate video — was released March 11, 2026. Multiple additional deepfake cases followed within weeks. None produced meaningful legal consequence. Each was technically compliant with existing disclosure requirements. The electoral manipulation apparatus documented in this domain is not a hypothetical future threat. It is the current operational reality of the 2026 election cycle.

The electoral manipulation threat of 2026 is not primarily from foreign interference or lone bad actors. It is from the systematic integration of commercial surveillance infrastructure — data brokers, social media platforms, AI generation tools — with political targeting operations, in an environment where no federal regulation governs the result.

Four components form the attack infrastructure. First, data brokers — Thomson Reuters CLEAR, LexisNexis Accurint, and hundreds of specialized political data companies — aggregate voter rolls, consumer behavior, location records, court filings, and social media into behavioral voter profiles usable for targeting at a specificity that no prior campaign technology achieved. Second, AI-generated synthetic content — deepfake videos, voice-cloned audio, synthetic text — is now deployed at industrial scale in the 2026 midterm cycle. Third, geofencing and microtargeting match these profiles to hyper-localized advertising systems, creating distinct information environments for different voter segments — with documented effects on turnout: a February 2026 PNAS study found targeted digital voter suppression ads reduced turnout 1.86 percent among exposed individuals, with non-white voters in minority-majority battleground counties receiving the ads at four times the rate of white voters in non-battleground counties and experiencing a 14.2 percent lower turnout than comparable non-exposed voters. Fourth, a regulatory vacuum: the FEC has lacked policymaking quorum since at least May 2025 and cannot issue AI deepfake guidance, the FCC's robocall prohibition does not extend to digital advertising, no federal law bans political deepfakes, and the December 2025 AI preemption executive order targets the 28-state disclosure patchwork that constitutes the only existing accountability layer.

The European Union has enacted substantive structural constraints. The DSA prohibits political microtargeting using sensitive personal data categories. EU Regulation 2024/900 (the Transparency and Targeted Political Advertising regulation) bans microtargeting using political opinions, religious beliefs, racial origin, sexual orientation, and political affiliations. EU AI Act Article 50 mandates machine-readable marking and user disclosure for AI-generated synthetic content — enforcement begins August 2, 2026, with fines up to €15 million or 3% of global annual turnover. Meta exited the EU political advertising market entirely rather than attempt compliance. The same companies deploy unregulated manipulation infrastructure in US elections.

This is regulatory arbitrage at democratic scale.

The domain proposes an integrated reform architecture: voter data broker regulation as election law, categorical prohibition on photorealistic AI-generated synthetic candidate content, congressional mandate for FEC binding rulemaking, and reversal of the December 2025 preemption order. The July 15 distribution target is not a preference — it is the last viable window before November 3 for any pre-election advocacy campaign, litigation filing, or congressional action to take effect.

---

## 1. The Data Broker Architecture: From Consumer Surveillance to Voter Targeting

### 1.1 The Commercial Data Pipeline

Every political campaign begins with a voter file — the list of registered voters purchased from state election authorities — providing names, addresses, party registration (in most states), and voting history. That file is the foundation. The manipulation infrastructure is what campaigns append to it.

Commercial data brokers transform a basic voter list into a psychographic targeting platform by matching voter records against their proprietary databases and appending hundreds of additional data points: purchase histories from loyalty programs, location histories from smartphone app data sold to aggregators, inferred religious and political beliefs from behavioral signals, financial stress indicators from credit bureau data, and social media activity scraped across platforms. In 2020, OpenSecrets documented that political groups paid 37 different data brokers at least $23 million for data services in a single cycle. The 2026 midterm advertising spend is projected at $10.8 billion, with an increasing share channeled through AI-enhanced precision targeting driven by these profiles.[^1]

The major players in this architecture operate across both commercial and government sectors without distinction. Thomson Reuters CLEAR — which holds six ICE contracts worth a total potential value of approximately $54 million[^2] — markets the same aggregated data products (license plate records, real estate transactions, court filings, professional licenses, arrest histories, organizational affiliations, Social Security and utility records) to law enforcement and to commercial clients.[^3] The same data infrastructure serving ICE deportation operations serves political campaign targeting. LexisNexis Accurint maintains records on over 276 million US residents;[^4] its PowerView Score incorporates Equifax credit data to generate consumer financial profiles that campaigns use for economic messaging targeting. Specialized political data firms — L2 (claiming data on 220 million voters), TargetSmart (claiming 171 million cell phone numbers matched to voter files), i360 — build partisan voter profiles using all of the above, enriched with dark web data, consumer transaction records, and social media scraping.[^5]

The data does not stay in separate silos. Thomson Reuters CLEAR is integrated in a system-to-system configuration with Palantir's analytical platform,[^6] allowing a single query to combine public record aggregations, commercial consumer data, and law enforcement investigative tools. The same query infrastructure used by ICE to identify deportation targets is available to political campaigns and PACs through commercial licensing arrangements. The commercial surveillance architecture does not discriminate between use cases.

### 1.2 The Government-Private Data Synthesis: DOJ Voter File Demands

The Trump administration's voter file collection campaign represents the most direct documented instance of government-private data broker synthesis in electoral management.

Beginning in May 2025, the Department of Justice demanded copies of complete voter registration databases from at least 33 states, seeking sensitive information including driver's license numbers, the last four digits of Social Security numbers, partisan affiliations, and voting histories. At least 27 of those states received demands for the voter files themselves.[^7] By May 2026, the DOJ had sued 30 states and the District of Columbia for refusing to provide their sensitive voter data.[^8]

The Brennan Center obtained and published confidential Memoranda of Understanding outlining the DOJ's plans for collected data. The MOU establishes that DOJ will "test, analyze, and assess states' voter rolls" and then instruct states to remove specific voters within 45 days — reversing the traditional state authority over voter roll maintenance. More critically for the surveillance capitalism nexus: the MOU permits voter files to be shared with contractors for "list maintenance verification" with minimal security safeguards — no binding encryption requirements, no audit logs, no restrictions on contractor data retention or resale.[^9]

Seven federal courts have dismissed the DOJ litigation, with one federal judge calling it a "fishing expedition." Rhode Island, California, Massachusetts, Michigan, Oregon, and Arizona courts have rejected the DOJ's legal theory.[^10] But at least twelve states have already complied voluntarily — Alaska, Arkansas, Indiana, Louisiana, Mississippi, Nebraska, Ohio, Oklahoma, South Dakota, Tennessee, Texas, and Wyoming — providing voter files with sensitive identifying information to federal contractors with no enforceable data security standards.[^11] The ACLU filed suit in federal court to block the national voter surveillance and purge database the DOJ MOU would create.[^12]

The structural significance: voter registration data combined with commercial data broker behavioral profiles creates targeting capability far beyond what state voter files alone provide. The government is constructing a centralized voter database that, under the current MOU framework, can be accessed by commercial contractors with no restriction on integration with the broader commercial data ecosystem.

### 1.3 Geofencing, Location Targeting, and Digital Suppression Infrastructure

The third component of the targeting architecture is location-based. Political campaigns have used geofencing — drawing a virtual perimeter around a physical location and capturing the device IDs of smartphones that enter it — since at least 2019, when NPR documented campaigns geofencing Catholic churches to target churchgoing voters with messaging calibrated to their inferred religious beliefs.[^13]

By 2026, the methodology is substantially more sophisticated. Campaigns can geofence community meeting locations, polling places, Black churches, immigrant service centers, and voter registration drives to capture the device IDs of attendees. Those device IDs are then matched against commercial data broker voter profiles, generating targeting lists that can be served microtargeted suppression messages on streaming video, social media, and connected television without the targets ever knowing they were identified.

The voter suppression effect is no longer theoretical. A January 2026 peer-reviewed PNAS study — the first empirical confirmation of digital voter suppression in an actual election — documented that participants exposed to digital voter suppression ads were 1.86 percent less likely to vote (nonexposure: 67.75% vs. exposure: 65.89%). Non-white voters in racial minority counties of battleground states received such ads at four times the rate of white voters in white-majority counties in non-battleground states; those non-white voters experienced a turnout rate 14.2 percent lower than comparable non-exposed white voters. Extrapolated to the 2016 election, the researchers estimated the ads may have prevented approximately 4.7 million people from voting.[^14] The study was led by researchers at the University of Wisconsin-Madison and analyzed the 2016 US presidential election using a real-time ad exposure tracking app installed by over 10,000 participants representative of the national voting population — matched against actual state voter records to confirm whether participants voted.

The critical democratic design problem: targeted digital voter suppression leaves no statutory footprint. It does not require passing a voter ID law. It does not require closing a polling location. It requires only a commercial data broker subscription, a geofencing platform, and AI-generated content — and there is currently no federal law requiring disclosure of suppression targeting, no requirement for campaigns to report what data they used, and no FEC or FTC enforcement mechanism with jurisdiction over this conduct.

---

## 2. AI-Generated Voter Manipulation: Industrial Scale in 2026

### 2.1 The Watershed Cases

The 2026 midterm cycle is the first US electoral cycle in which AI-generated political content operates as a documented standard tool of major party campaign operations. Five cases establish the arc from proof-of-concept to national party deployment.

**The Biden New Hampshire robocall (January 2024)**: A Democratic consultant hired a magician to use the AI voice-generation tool ElevenLabs to impersonate President Biden in robocalls sent to New Hampshire primary voters, instructing them not to vote in the primary. The operation cost approximately $500 for distribution; production took under 20 minutes using a commercially available tool.[^15] The FCC's subsequent ruling that AI-generated voices in robocalls violate the Telephone Consumer Protection Act closed the robocall channel while leaving all digital, social media, and television advertising channels unregulated. This case established the production cost floor: political-grade voice impersonation costs under $500.

**The Collins-Ossoff deepfake (November 2025)**: Rep. Mike Collins (R-GA), running against incumbent Democratic Sen. Jon Ossoff in Georgia's 2026 Senate race, released an AI-generated deepfake video depicting Ossoff mocking farmers and defending a government shutdown — statements Ossoff never made. The video included a small on-screen disclaimer satisfying Georgia's disclosure requirements while remaining an intentional deception. The Collins campaign confirmed it planned to continue using AI tools, stating it would "be at the forefront embracing new tactics."[^16]

**The NRSC-Talarico deepfake (March 11, 2026)**: The National Republican Senatorial Committee posted an attack ad depicting Texas Democratic Senate candidate James Talarico appearing to read excerpts from his past tweets on transgender issues, race, religion, and Planned Parenthood — with additional fabricated statements Talarico never made. This is the first deployment of a lifelike synthetic candidate video by a national party committee. The ad ran for over a minute. A digital forensics specialist at UC Berkeley assessed the synthetic video as "highly convincing" with only "a slight misalignment between audio and video," concluding: "this is hyper-realistic and I don't think that most people would immediately know it is fake." A small "AI GENERATED" label appeared in the corner for approximately three seconds at the start, then remained in fainter smaller text for the remainder — technically compliant with Texas disclosure law while remaining operationally deceptive.[^17] CNN characterized it as "the first featuring a phony version of a candidate talking in a lifelike manner for so long — an example of how far AI technology has come in a short time."[^18]

**The Virginia Spanberger deepfakes (February and April 2026)**: The Loudoun County Republican Committee released an AI-generated video on February 23, 2026 depicting Governor Abigail Spanberger with fabricated statements, including an animated sequence of the Spanberger figure setting fire to a religious painting. No disclaimer or "AI generated" label appeared in the post; the caption read simply "Thanks @GovernorVA !!!!!"[^19] In April 2026, a separate anti-redistricting group released a 30-second ad with an AI-generated fake Spanberger video claiming she "wants to burn Virginia's democracy to the ground."[^20] The February ad is significant as proof that even disclosure-only state laws produce no universal compliance — the Loudoun County case had zero disclosure.

**The Maine Platner deepfake (April 2026)**: A Republican ad deployed an AI deepfake of Maine Democratic candidate Graham Platner, extending the pattern beyond federal races to state legislative contests — confirming that national party normalization of deepfakes cascades downward through every level of electoral competition.[^21]

### 2.2 The Production Cost Threshold Has Collapsed

The democratic design implications of these cases cannot be understood without grasping the production cost collapse. The WEF's March 2026 analysis documents that deepfakes have "crossed a critical threshold in 2026, having improved and eliminated earlier tell-tale glitches and are now accessible to anyone with a smartphone."[^22] Generative AI video production tools available to individual users have reduced the cost of a photorealistic deepfake from tens of thousands of dollars in 2022 to approximately $8–50 in 2026, depending on length and fidelity requirements. Resemble AI recorded 482 politically motivated deepfake incidents in Q3 2025 alone, representing 23.7% of all deepfake cases tracked — a baseline that continues to accelerate.[^23]

The practical meaning: the production barriers that previously concentrated deepfake capability in well-resourced operations have collapsed. Any campaign, PAC, or political operative with $500 and 20 minutes can produce content sufficient to deceive voters. At the national party committee level, the NRSC's Talarico video demonstrates that sophisticated, extended lifelike deepfake videos are now standard-issue campaign tools. The 2026 midterm cycle is the first in which deepfake voter manipulation operates as normal campaign practice rather than exceptional bad behavior.

A 2025 peer-reviewed study in the Journal of Creative Communications found that people struggle to identify deepfake videos and that voters who see a fabricated video of a candidate making a controversial statement carry that impression measurably even after correction.[^24] The correction asymmetry — deception spreads at the speed of social media amplification; correction moves at the speed of journalism — means that even detected deepfakes produce lasting voter-impression effects before any corrective information reaches the same audience.

### 2.3 Disclosure Without Prohibition Is Compliance-as-Cover

All five major 2026 deepfake cases either operated within existing disclosure frameworks or violated them with no consequence. The NRSC's Talarico video displayed "AI GENERATED" in small text for three seconds. The Collins-Ossoff video included a disclaimer satisfying Georgia's requirements. The Virginia redistricting video deployed in April complied with Virginia's disclosure law. The February Spanberger video had no disclosure at all and produced no enforcement response.

This is the foundational problem with disclosure-only regulatory frameworks for AI-generated political content: a viewer who did not notice a small-text disclaimer in the corner of a video for three seconds has been deceived regardless of technical compliance. The disclosure architecture was designed for print advertising footnotes; it does not translate to video formats where the emotional impact of seeing a candidate "say" something they never said cannot be reversed by three seconds of small text.

The American Prospect analysis of the 2026 midterm deepfake landscape (April 17, 2026) documents that most state laws only require disclosure rather than prohibition. "Legislation is a noble effort, but the technology is moving so fast," the article quotes election law experts — capturing the fundamental asymmetry between the pace of AI development and the pace of legislative response.[^25]

---

## 3. The Regulatory Vacuum: Three Failure Modes and One Preemption

### 3.1 FEC Structural Paralysis

The Federal Election Commission has not had a policymaking quorum since at least May 1, 2025. As of October 2025, a fourth commissioner resigned, leaving only two of six seats occupied — the most severe quorum crisis in the FEC's history. On February 11, 2026, President Trump nominated Ashley Stow and Andrew Woodson to restore the quorum; as of May 2026, neither nominee has been confirmed by the Senate, no confirmation hearing has been scheduled, and the FEC remains unable to pass new election rules, conduct enforcement actions, or issue binding guidance.[^26]

This structural paralysis is the governing context for the FEC's AI response. On September 19, 2024 — before the quorum collapse — the FEC voted 3-3 not to open a rulemaking on AI in campaign ads. The Commission instead adopted a non-binding "Interpretive Rule" clarifying that existing fraudulent misrepresentation statutes apply regardless of technology used.[^27] The Interpretive Rule is not a regulation. It has no enforcement teeth beyond what the existing statute already provides. The existing statute — 52 U.S.C. § 30124, which prohibits fraudulent misrepresentation of a candidate — has never been successfully applied to a political deepfake case. There is no FEC definition of what constitutes AI-generated "fraudulent misrepresentation" as distinct from ordinary campaign attack rhetoric.

The quorum collapse means that even if the FEC Interpretive Rule were a binding regulation — it is not — the Commission cannot currently enforce it. A coalition of 50 Democratic congressional members formally urged FEC action; advocacy organizations including Public Citizen, Protect Democracy, and the Campaign Legal Center filed formal petitions.[^28] None has produced enforceable regulation. The FEC's structural incapacity is not a temporary gridlock. It is a design problem that will not resolve until at least late 2026 — after the midterm election.

### 3.2 FCC's Robocall Prohibition: Closing the Wrong Channel

The FCC's February 2024 ruling that AI-generated voices in robocalls violate the Telephone Consumer Protection Act was an enforcement action in response to the Biden NH robocall. The ruling was appropriate but largely irrelevant to the 2026 deepfake landscape.

The FCC's regulatory authority is limited to spectrum-based media — broadcast radio and television, cable, satellite TV and radio. Due to the FCC's lack of jurisdiction, its political advertising rules do not apply to social media platforms, video and audio streaming services, or connected television delivered via internet protocol.[^29] The 2026 deepfake cases — NRSC-Talarico, Collins-Ossoff, Virginia Spanberger, Maine Platner — were all distributed through social media and digital advertising channels the FCC cannot reach. The FCC's action in the robocall domain was appropriate; it addressed the channel with the narrowest reach while leaving the channels with the broadest reach — social media, connected television, digital advertising networks — completely unregulated.

### 3.3 The 28-State Patchwork: Disclosure Without Prohibition

As of February 2026, 30 states have enacted laws specifically addressing deepfakes in political communications.[^30] The Public Citizen tracker documents that most require small "AI Generated" disclaimers. State-level variation is significant:

**Texas**: The Responsible AI Governance Act (HB 149, effective January 1, 2026) prohibits intentionally developing or deploying AI systems to produce deepfakes for certain restricted purposes and criminalizes creating a deepfake video within 30 days of an election with intent to injure a candidate. The NRSC's Talarico video was released before the 30-day window and in compliance with the disclosure provision — demonstrating that the prohibition window is too narrow and the disclosure standard too weak to prevent deployment.

**California**: A federal court struck down California's AB 2655 — which required large online platforms to block materially deceptive content related to elections — on Section 230 grounds, holding that the law violated the Communications Decency Act's platform immunity provision.[^31] California's stronger prohibition approach was blocked by the very federal preemption architecture the December 2025 EO seeks to extend.

**New York**: The Synthetic Performer Disclosure Act (S.8420A), effective June 9, 2026, requires clear and conspicuous disclosure when an advertisement uses an AI-generated synthetic performer — a disclosure standard consistent with the broader patchwork, not a prohibition.

**Illinois**: Addresses AI in employment contexts (video interview analysis), not specifically in political advertising.

The patchwork's fundamental design problem: the best state approaches (California's prohibition) are being struck down by federal preemption; the surviving approaches (disclosure requirements) are being exploited as compliance-as-cover.

### 3.4 The December 2025 AI Preemption Executive Order

On December 11, 2025, President Trump signed "Ensuring a National Policy Framework for Artificial Intelligence," directing the DOJ to establish an AI Litigation Task Force to challenge state AI laws, directing the FTC to issue a policy statement identifying circumstances under which state AI laws are preempted, and directing the FCC to circumvent "onerous" state regulations.[^32]

The preemption theory is constitutionally contested. NPR's legal analysis reported the order "can easily be challenged and overturned in court unless Congress passes legislation" and that "state laws remain enforceable" while litigation is resolved.[^33] Goodwin Law found the order "unlikely to put a lid on state AI laws" given constitutional limits on executive preemption authority.[^34] But the order does not need to win in court to achieve its objective. The chilling effect on state legislative action is already operating: the 30-state patchwork has not meaningfully expanded since December 2025. States that planned to advance from disclosure requirements to prohibition requirements are now assessing litigation risk before proceeding.

The structural result is a three-layer accountability vacuum: the FEC is paralyzed by quorum collapse and cannot issue binding guidance; the FCC lacks jurisdiction over the distribution channels where deepfakes circulate; and state-level accountability — the only functioning layer — is targeted by a preemption theory designed to eliminate it before federal standards are established. This is the accountability vacuum by design.

---

## 4. The EU Accountability Divergence: Same Companies, Different Standards

### 4.1 DSA and the Political Advertising Regulation

The EU Digital Services Act (DSA) prohibits platforms from showing targeted advertising based on special categories of sensitive personal data, including political opinions, religious beliefs, racial or ethnic origin, and sexual orientation.[^35] DSA Article 25 prohibits deceptive and manipulative interface designs — "dark patterns" — that prevent users from making informed choices about political content.

EU Regulation 2024/900 — the Transparency and Targeting of Political Advertising (TTPA) regulation, which entered force in October 2025 — goes further: it bans microtargeting using political opinions, prohibits use of sensitive data categories for political targeting, requires explicit consent for all political data collection, mandates disclosure of who funded political advertising and what targeting criteria were used, and establishes safeguards against AI-driven microtargeting of sensitive categories.[^36]

The DSA enforcement record demonstrates these are not paper standards. On December 5, 2025, the European Commission issued its first non-compliance decision under the DSA, fining X (formerly Twitter) €120 million ($140 million) for breaches including ad transparency failures and deceptive design.[^37] In October 2025, Meta exited the political advertising market in Europe entirely rather than attempt compliance with the TTPA's targeting restrictions — removing the EU as a market for political microtargeting rather than adapting its tools to comply.[^38] This is not the behavior of a company that considers EU standards cosmetic.

### 4.2 EU AI Act Article 50: Deepfake Labeling Enforcement Begins August 2, 2026

EU AI Act Article 50 imposes transparency obligations on AI-generated synthetic content. Providers of AI systems that generate synthetic audio, image, video, or text content must ensure outputs are marked in a machine-readable format and detectable as artificially generated. Deployers must disclose to users when AI creates realistic synthetic content, including deepfakes. Violations of Article 50(4) transparency obligations carry fines of up to €15 million or 3% of global annual turnover, whichever is higher.[^39]

The European Commission published the first draft Code of Practice on Marking and Labelling of AI-Generated Content in December 2025, incorporating feedback from industry, civil society, and academia. A final code was anticipated in June 2026 ahead of the August 2, 2026 enforcement date.[^40]

The Article 50 framework is substantively different from US disclosure approaches in two critical ways. First, the machine-readable marking requirement means platforms — not just creators — have affirmative obligations to detect and label AI-generated content. A small on-screen text disclaimer that appears for three seconds does not satisfy Article 50. Second, Article 50 applies to platforms as well as content creators, closing the distribution-layer accountability gap that allows deepfake content to circulate on social media without platform-level intervention.

### 4.3 The Regulatory Arbitrage Problem

Meta, Google, and X — the three platforms through which 2026 US midterm deepfake content is primarily distributed — all comply with EU DSA and Article 50 standards for European political markets while applying only voluntary self-regulatory standards to US political markets.

Meta's European political advertising exit demonstrates the practical effect: rather than apply EU-compliant political advertising standards globally, Meta built a geographic carve-out. EU users are protected from political microtargeting using sensitive data categories; US users are not. The same targeting tools prohibited for use against European voters are available for deployment against American voters without any regulatory constraint.[^41]

TechPolicy.Press data on Meta and Google's political ad ban in EU markets documents that the political advertising revenue these platforms forfeited by complying with EU standards represents a fraction of their total revenue — meaning compliance is financially feasible. The question is not whether compliance is technically or economically possible; it is whether the US regulatory environment creates any obligation to extend EU-level protections to American voters. It does not.

The August 2, 2026 enforcement date for EU AI Act Article 50 creates a specific advocacy window. In the period between the July 2026 distribution of this document and August enforcement, the contrast between EU substantive protection and US regulatory vacuum will be at maximum visibility in tech policy, election law, and digital rights coverage. The argument — same companies, same technology, different accountability standards applied to US and European voters — is most powerful in that window.

### 4.4 The International IDEA Assessment

The International IDEA Navigating the EU's Digital Regulatory Framework analysis concludes that the combined DSA, TTPA, and AI Act framework represents the most comprehensive democratic safeguard for electoral integrity against digital manipulation in any major jurisdiction.[^42] The US-EU divergence is not a gap between a stricter and a more permissive approach to the same problem. It is a gap between an integrated structural accountability architecture and an accountability vacuum. EU citizens receive machine-readable content provenance markers, prohibition on sensitive-category political targeting, and platform-level deepfake detection obligations. US citizens receive a small-text disclaimer that appears for three seconds.

---

## 5. Reform Architecture: What Structural Regulation Would Require

The regulatory failures documented in Sections 3 and 4 are not accidents. They are the product of a commercial surveillance industry that has successfully prevented development of accountability frameworks covering its electoral use cases, a political regulatory body (the FEC) structurally unable to act, and a federal executive strategy actively dismantling the only accountability layer (state laws) that currently functions. The reform architecture required to address the threat has four structural components.

### 5.1 Voter Data as a Specially Protected Category

The current legal framework treats voter registration data as ordinary government records subject to standard public records access. In most states, voter files are purchasable by any party for any purpose. Data brokers can purchase voter files and append them to commercial behavioral profiles without restriction. The DOJ voter file collection campaign — operating under a confidential MOU framework with minimal security standards — represents the logical endpoint of treating voter data as undifferentiated government information.

The reform required is a federal Voter Data Protection framework: designation of voter registration data as a specially protected category under federal privacy law, prohibiting data brokers from incorporating voter file information into commercial behavioral profiles without explicit statutory authorization; requiring any contractor receiving voter data from a government source to comply with security standards equivalent to the Federal Information Security Management Act; and creating a private right of action for voters whose registration data is disclosed in violation of the protection framework.

The April 2026 SECURE Data Act — the House Republican comprehensive privacy bill, released April 22, 2026 — establishes data broker registration requirements and a federal privacy floor.[^43] It does not contain voter-specific protections. The gap between a general privacy framework and a voter data protection framework is the gap between treating voter data as consumer information and treating it as a component of democratic infrastructure.

### 5.2 AI-Generated Synthetic Candidate Content: Beyond Disclosure

The documented failure of disclosure-only frameworks establishes that disclosure requirements do not prevent voter manipulation. The NRSC-Talarico complied with Texas disclosure law while remaining an intentional deception; the Virginia Spanberger video of February 2026 deployed with no disclosure at all and produced no enforcement response; the Collins-Ossoff ad satisfied Georgia law. The reform architecture must go beyond disclosure.

The legislative spectrum runs from disclosure reinforcement to categorical prohibition. The NO FAKES Act of 2025 (S.1367, H.R.2794, reintroduced April 2025, referred to Senate Judiciary Committee) establishes a federal right of publicity against unauthorized digital replicas — but focuses on the content creator and production side rather than the electoral distribution context.[^44] The Protecting Consumers from Deceptive AI Act (introduced April 24, 2026) establishes technical standards for AI content disclosure — stronger than existing state frameworks but still disclosure-based.[^45]

The reform that matches the scale of the documented harm is a categorical prohibition on photorealistic AI-generated video and audio depicting real federal candidates in paid political advertising, with a safe harbor for clearly satirical content. This approach — prohibition rather than disclosure — aligns with how the EU has structured its protections (DSA prohibition on sensitive data targeting rather than disclosure of targeting) and addresses the mechanism the documented 2026 cases demonstrate: disclosure does not prevent deception.

State prohibition models are the correct federal template. Texas SB753 prohibits election-related deepfake videos within 30 days of elections. Maryland SB0141 criminalizes election-related deepfakes. The federal approach should extend the prohibition window to 90 days, cover all paid political advertising regardless of medium, and include a platform liability provision modeled on the Deepfake Liability Act (H.R.6334) requiring platforms to respond to verified complaints about digital forgeries as a condition of Section 230 immunity.[^46]

### 5.3 FEC Mandatory AI Rulemaking: Breaking the Deadlock

The FEC's quorum collapse and partisan deadlock on AI regulation is not resolvable through FEC internal process. The Commission has demonstrated it cannot reach consensus on AI rulemaking. The reform required is a congressional mandate specifying: (a) the FEC must complete a rulemaking on AI-generated political content within 180 days of enactment; (b) the rulemaking must establish specific requirements for machine-readable content provenance disclosure and platform-level detection obligations (parallel to EU AI Act Article 50); (c) in the event of continued commission deadlock, a specified tie-breaking mechanism applies.

Senator Warner's March 2026 call for congressional action in response to the NRSC-Talarico video provides the legislative hook.[^47] A targeted FEC rulemaking mandate — modeled on congressional mandates that have resolved prior FEC deadlocks — is the most direct path to enforceable federal standards before the November 2026 election. The interim action available before legislation is enacted: the FTC has existing Section 5 authority over unfair and deceptive practices that may extend to AI-generated voter manipulation; an FTC policy statement could establish interim standards while FEC rulemaking proceeds.

### 5.4 Federal Floor and State Authority Preservation

The December 2025 AI preemption executive order is premised on a regulatory vision in which a permissive federal standard preempts more protective state standards. The democratic design logic runs in the opposite direction. State experimentation — the 30-state patchwork that includes both disclosure and prohibition frameworks — represents the only functioning accountability layer currently operating over AI-generated political content.

The reform architecture must reverse the preemption logic: federal law should establish a minimum floor that the 30 states with AI disclosure requirements already exceed, while explicitly preserving state authority to enact more protective standards. This anti-preemption model — federal floor plus state authority — mirrors the NVRA's structure on voter registration and the Clean Air Act's structure on environmental standards. It preserves the laboratory function of state innovation while establishing a federal baseline that prevents the most egregious uses of AI-generated manipulation in elections that lack any state law.

The December 2025 EO should be rescinded or overridden by Congress for the electoral manipulation domain. The legal analysis from Goodwin Law and NPR confirms that state laws remain enforceable during litigation — but the chilling effect on state legislative expansion requires a congressional signal that state authority in the electoral context is affirmatively protected.

---

## 6. Movement Leverage: Coalition Architecture for November 3

Achieving any regulatory response before November 3 requires multi-sector coalition mobilization starting at the July 2026 distribution window. The movement organizations with highest leverage in this domain span four sectors with distinct but complementary advocacy capacities.

### 6.1 Election Protection Organizations

**Brennan Center for Justice (Elections Program)**: Has published the definitive analyses of digital voter suppression, data broker threats, and AI deepfake regulation in the electoral context. The Brennan Center's "Preparing to Fight AI-Backed Voter Suppression" and "Gauging the AI Threat to Free and Fair Elections" provide the foundation for coalition advocacy. The Brennan Center has specifically urged policies expanding voter intimidation laws to cover AI-generated content, regulating deepfakes used to suppress votes, and establishing new guidance for election officials on AI in election administration.

**Protect Democracy**: Focused on systemic democratic threats; has documented the nexus between commercial surveillance and election manipulation as a democratic design failure. Litigation capacity for state-level and federal challenges.

**Democracy Docket (Marc Elias Foundation)**: 24 lawsuits active related to voter purge and suppression mechanisms in 2026; the DOJ voter file demand campaign is directly in Democracy Docket's operational scope.

**Campaign Legal Center**: Campaign finance law expertise; the data broker purchase of voter targeting information is a campaign finance disclosure gap that Campaign Legal Center has documented.

### 6.2 Digital Rights Organizations

**EFF (Electronic Frontier Foundation)**: Has published critical analysis of the political campaign data use ecosystem and the specific threat to political organizing posed by commercial surveillance infrastructure. The EFF's analysis of the takedown provision in deepfake legislation provides the First Amendment guardrail framework that any prohibition legislation must satisfy.

**EPIC (Electronic Privacy Information Center)**: Has published "Generative AI and Elections: The Approaching Train Wreck" and has formally petitioned the FEC for AI guidance. EPIC's FTC Section 5 argument for interim regulation is the most immediately actionable regulatory leverage point.

**CDT (Center for Democracy and Technology)**: Tech policy expertise and Congressional relationships; has documented the platform-level accountability gap that Section 230 creates for AI-generated political content.

**Access Now**: International digital rights network with EU regulatory expertise — best positioned to operationalize the US-EU comparison argument for advocacy purposes.

### 6.3 Voting Rights and Voter Protection Coalitions

**Lawyers' Committee for Civil Rights Under Law (Election Protection hotline)**: Operates the 1-866-OUR-VOTE election protection hotline network. Digital suppression ad targeting of non-white voters in battleground counties is directly within Election Protection's operational scope; the PNAS study's findings on racial targeting should be core advocacy material distributed through the Election Protection network.

**NAACP Legal Defense Fund**: Voting rights litigation expertise; the PNAS study's racial targeting findings (non-white voters in minority-majority battleground counties receiving ads at 4x the rate of white voters) are actionable under the Voting Rights Act's discriminatory effect framework.

**League of Women Voters**: Mass membership voter advocacy; voter data protection and deepfake threats are issues that activate the League's membership in swing states.

**Common Cause**: State-level chapters with legislative advocacy capacity in all 50 states; the 30-state patchwork maintenance and expansion is Common Cause terrain.

### 6.4 Media Literacy and Academic Partners

**Stanford Internet Observatory**: Deepfake detection research and platform policy documentation. The SIO's partnerships with platforms are the leverage point for platform-level deepfake detection implementation ahead of EU AI Act enforcement.

**Harvard Shorenstein Center**: Election media research and journalism training; the PNAS study's implications for political journalism (how to cover synthetic content, how to document targeting campaigns) is core Shorenstein curriculum.

**News Literacy Project**: Media literacy training for educators; voter-facing media literacy tools are the supply-side response to the demand-side regulatory failures.

**Columbia Tow Center for Digital Journalism**: Platform policy research; the EU-US regulatory divergence documentation is Tow Center research infrastructure.

---

## 7. The November 3 Constraint: Why This Window Is Closing

The 2026 midterm election — November 3, 2026 — is the structural constraint on reform timeline. The documented developments in this domain are not preliminary indicators. They are the current operational reality of the 2026 election cycle.

The NRSC deployed a national party deepfake in March 2026. Collins deployed a Georgia Senate deepfake in November 2025. The Loudoun County Republican Committee deployed a deepfake of a sitting governor with no disclosure in February 2026. A Maine Republican operation deployed a deepfake against a state legislative candidate in April 2026. These are not isolated incidents. They are documented proof that AI-generated voter manipulation is now standard campaign practice at every level of the electoral system.

The advocacy timeline required to achieve any regulatory response before November 3:

**July 15, 2026 — Hard distribution deadline**: Domain 40 reaches election protection organizations (Brennan Center Elections Program, Protect Democracy, Democracy Docket), digital rights organizations (EFF, EPIC, CDT), campaign finance transparency organizations (OpenSecrets, Campaign Legal Center), and swing-state voter protection networks. Congressional testimony preparation and coalition letter campaigns launch.

**August 2, 2026 — EU AI Act Article 50 enforcement begins**: Maximum media window for the US-EU comparison argument. The argument — same companies, EU compliance, US deregulation — is most powerful in this window. Op-ed and media placement campaign.

**August-September 2026 — Congressional floor window**: Congressional recess ends in early September; any floor action on deepfake legislation must occur in this window to have effect before the November election. Senate votes on FEC nominees may occur in this window — a bipartisan FEC quorum restoration is the minimum prerequisite for any FEC enforcement response.

**October 2026 — Final pre-election window**: Platform-level advocacy (coordinated pressure through Stanford Internet Observatory, Harvard Shorenstein Center, and Columbia Tow Center) to implement voluntary deepfake detection and labeling standards that go beyond EU-minimum standards and apply globally.

**November 3, 2026 — Hard deadline**: No regulatory response enacted after this date can address the 2026 election cycle.

The interim actions available before legislation is enacted: (1) FEC commissioners can individually request reconsideration of the September 2024 Interpretive Rule, triggering a new commission vote if quorum is restored; (2) the FTC has existing Section 5 authority over unfair and deceptive practices — an FTC policy statement on AI-generated voter manipulation could establish interim standards while FEC rulemaking is pending; (3) state AGs with authority over deceptive practices can investigate deepfake campaigns using state consumer protection law as an alternative to FEC enforcement.

---

## 8. Unique Contribution and Cross-Domain Synthesis

Domain 40 provides the framework's first systematic analysis of commercial surveillance infrastructure as electoral attack infrastructure. Domain 43 (Epistemic Infrastructure) covers the epistemic harm — what deepfakes do to the information environment, the liar's dividend, the collapse of shared factual foundations. Domain 37 (Federal Executive Interference) covers the government side of election manipulation. Neither covers the commercial data broker industry as the supply chain that makes targeted voter manipulation possible at scale.

This domain also provides the first cross-domain synthesis connecting the data broker problem — which appears in Domain 25 as the FISA loophole, in Domain 36 as ImmigrationOS inputs, in the ICE contractor research as a government surveillance pipeline — to the electoral democracy problem specifically. The synthesis is the framework's unique contribution to the election protection movement: connecting commercial surveillance infrastructure to voting rights advocacy in a single democratic-design argument.

The regulatory arbitrage finding — same companies, EU compliance, US deregulation — is the advocacy handle most likely to generate media coverage, congressional attention, and platform pressure in the August 2026 window.

**Confidence assessment**: The core factual claims in this domain are high-confidence. The PNAS study findings (1.86% turnout suppression, 4x racial targeting disparity) are peer-reviewed and confirmed by the study text. The deepfake cases (NRSC-Talarico, Collins-Ossoff, Spanberger, Platner) are documented by multiple news sources. The FEC quorum collapse and the DOJ voter file demands are confirmed by court records and the Brennan Center tracker. The EU regulatory architecture (DSA, TTPA, AI Act Article 50, fines) is confirmed from primary EU sources. One area of lower confidence: the specific "50% voter influence" figure cited in some secondary sources regarding the NRSC-Talarico polling impact — this figure could not be independently verified from a named primary survey (CBS/WaPo or otherwise) during research; the confirmed figure from the OECD AI incident tracker and multiple secondary sources is "nearly 50%" or "approximately 50%", sourced to general 2026 cycle polling rather than a named single survey. This domain uses the formulation "nearly 50%" consistent with verified sources.

---

## Source Notes

[^1]: EFF — How Political Campaigns Use Your Data to Target You (April 2024): https://www.eff.org/deeplinks/2024/04/how-political-campaigns-use-your-data-target-you; OpenSecrets — Third-Party Brokers Selling Data to Political Groups: https://www.opensecrets.org/news/2022/04/the-third-party-brokers-who-make-millions-selling-your-data-to-political-groups/

[^2]: AFSC Investigate — Thomson Reuters: https://investigate.afsc.org/company/thomson-reuters; State of Surveillance — Data Brokers Selling to ICE: https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/

[^3]: LawNext — The Legal Tech Giants Powering ICE, Part 1 (April 2026): https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-1-how-thomson-reuters-and-lexisnexis-helped-support-americas-immigration-surveillance-machine.html; In These Times — Data Brokers Fueling ICE's Deportation Machine: https://inthesetimes.com/article/ice-deportation-machine-surveillance-artificial-intelligence-thomson-reuters-clear-trump

[^4]: LawNext — The Legal Tech Giants Powering ICE, Part 1 (April 2026), op. cit. LexisNexis Accurint holds records on over 276 million US residents.

[^5]: GhostVault — Data Broker List 2026 (500+ sites): https://www.ghostvault.live/data-brokers; State of Surveillance — Data Brokers and Political Campaigns: https://stateofsurveillance.org/articles/surveillance/data-brokers-political-campaigns-voter-targeting/; Privacy International — Data and Elections: https://privacyinternational.org/learn/data-and-elections

[^6]: AFSC Investigate — Thomson Reuters, op. cit.: "CLEAR integrates with Palantir's analytical platform in a system-to-system configuration."

[^7]: Brennan Center — Justice Department Has Demanded Voter Files from at Least 27 States: https://www.brennancenter.org/our-work/analysis-opinion/justice-department-has-demanded-voter-files-least-21-states; Brennan Center Tracker of Justice Department Requests for Voter Information: https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information; USAFacts — Voter Lists: What Are They and Why Is the DOJ Asking for Them: https://usafacts.org/articles/voter-lists-what-are-they-and-why-is-the-doj-asking-for-them

[^8]: NBC News — Tracking the DOJ's Effort to Get US Voter Registration Data: https://www.nbcnews.com/politics/justice-department/tracking-dojs-effort-get-us-voter-registration-data-rcna331509; US News — DOJ Drafts Legal Opinion Backing Demands for State Voter Rolls (May 13, 2026): https://www.usnews.com/news/politics/articles/2026-05-13/us-justice-department-drafts-legal-opinion-backing-demands-for-state-voter-rolls

[^9]: Brennan Center — Confidential Agreements Show Trump Administration's Plans for States' Voter Data: https://www.brennancenter.org/our-work/analysis-opinion/confidential-agreements-show-trump-administrations-plans-states-voter; Brennan Center — Justice Department Security Measures Are Inadequate: https://www.brennancenter.org/our-work/analysis-opinion/justice-departments-security-measures-collecting-voter-rolls-are

[^10]: NBC News — Judge Dismisses DOJ Lawsuit Seeking Arizona Voter Data: https://www.nbcnews.com/politics/justice-department/judge-dismisses-doj-lawsuit-seeking-arizona-voter-data-rcna342613; US News — Federal Judge Dismisses DOJ Lawsuit in Massachusetts (April 9, 2026): https://www.usnews.com/news/politics/articles/2026-04-09/a-federal-judge-dismisses-another-doj-lawsuit-seeking-voter-data-this-time-in-massachusetts; PBS — Federal Judge Dismisses DOJ Lawsuit in Rhode Island: https://www.pbs.org/newshour/politics/federal-judge-dismisses-doj-lawsuit-seeking-personal-details-about-rhode-island-voters

[^11]: Stateline — Trump's DOJ Wants States to Turn Over Voter Lists, Election Info (July 16, 2025): https://stateline.org/2025/07/16/trumps-doj-wants-states-to-turn-over-voter-lists-election-info/; University of Wisconsin Law School — Tracker: DOJ Lawsuits Seeking States' Sensitive Voter Data: https://statedemocracy.law.wisc.edu/our-work/tracker-doj-lawsuits-seeking-states-sensitive-voter-data

[^12]: ACLU — Voting Rights Groups Sue DOJ to Block National Voter Surveil-and-Purge Database: https://www.aclu.org/press-releases/voting-rights-groups-sue-doj-to-block-national-voter-surveil-and-purge-database

[^13]: NPR — How Political Campaigns Are Using Geofencing to Target Catholics at Mass (February 2020): https://www.npr.org/2020/02/06/803508851/how-political-campaigns-are-using-geofencing-technology-to-target-catholics-at-m; The Markup — How Political Campaigns Use Your Phone's Location (November 2022): https://themarkup.org/privacy/2022/11/08/how-political-campaigns-use-your-phones-location-to-target-you

[^14]: PNAS — Targeted digital voter suppression efforts likely decrease voter turnout (January 26, 2026): https://www.pnas.org/doi/10.1073/pnas.2519944123; PMC — Targeted digital voter suppression efforts likely decrease voter turnout: https://pmc.ncbi.nlm.nih.gov/articles/PMC12867748/; University of Wisconsin news release: https://news.wisc.edu/research-shows-social-media-advertising-suppresses-voting-in-targeted-communities/

[^15]: NBC News — A magician says a Democratic operative paid him to make the fake Biden New Hampshire robocall: https://www.nbcnews.com/politics/2024-election/biden-robocall-new-hampshire-strategist-rcna139760; NPR — What a robocall of Biden's AI-generated voice could mean for the 2024 election: https://www.npr.org/2024/02/07/1229856682/what-a-robocall-of-bidens-ai-generated-voice-could-mean-for-the-2024-election

[^16]: CBS Atlanta — Georgia Rep. Mike Collins' campaign uses AI-generated deepfake of Senator Jon Ossoff: https://www.cbsnews.com/atlanta/news/georgia-rep-mike-collins-campaign-uses-ai-generated-deepfake-of-senator-jon-ossoff-in-tight-senate-showdown/; AJC — Jon Ossoff warned about deepfakes. Now, an opponent has made him one: https://www.ajc.com/politics/2025/11/jon-ossoff-warned-about-deepfakes-now-he-is-one/

[^17]: IBTimes — Republicans Release AI Deepfake of James Talarico — Is Voter Manipulation Crossing the Line? (March 2026): https://www.ibtimes.com/republicans-release-ai-deepfake-james-talarico-voter-manipulation-crossing-line-3799291; RoboRhythms — AI Deepfakes Are Official Campaign Strategy. The 2026 Midterms Proved It.: https://www.roborhythms.com/ai-deepfakes-midterm-elections-2026/

[^18]: CNN — Republicans release AI deepfake of James Talarico (March 13, 2026): https://www.cnn.com/2026/03/13/politics/james-talarico-ai-deepfake-republicans-midterms; OECD AI — AI Deepfakes Used to Mislead Voters in 2026 US Midterm Campaigns: https://oecd.ai/en/incidents/2026-03-28-b14f

[^19]: Lead Stories — Fact Check: Republican Committee Published Fake AI Campaign Video of Virginia Governor Spanberger (February 2026): https://leadstories.com/hoax-alert/2026/02/fact-check-republican-committee-published-fake-ai-campaign-video-of-virginia-governor-spanberger.html

[^20]: Virginia Independent — Anti-redistricting group uses fake AI-generated video of Spanberger in ad: https://virginiaindependentnews.com/elections/anti-redistricting-group-uses-fake-ai-generated-video-of-spanberger-in-ad/

[^21]: Bangor Daily News — Republican ad uses an AI deepfake of Graham Platner (April 16, 2026): https://www.bangordailynews.com/2026/04/16/politics/elections/maine-senate-election-republican-ai-deepfake-ad-graham-platner/

[^22]: WEF — How cognitive manipulation and AI will shape disinformation in 2026 (March 2026): https://www.weforum.org/stories/2026/03/how-cognitive-manipulation-and-ai-will-shape-disinformation-in-2026/

[^23]: Bright Defense — 150+ Deepfake Statistics (March 2026): https://www.brightdefense.com/resources/deepfake-statistics/; Resemble AI — Q3 2025 Deepfake Incident Report.

[^24]: AI CERTs — How Political Misinformation Deepfakes Threaten 2026 Elections: https://www.aicerts.ai/news/how-political-misinformation-deepfakes-threaten-2026-elections/; Science Survey — When Seeing Is No Longer Believing: Deepfake Media in Elections (March 2026): https://thesciencesurvey.com/news/2026/03/16/when-seeing-is-no-longer-believing-deepfake-media-in-elections/

[^25]: American Prospect — American Politics Is Already Inundated With AI Deepfakes. It's Only Getting Worse (April 17, 2026): https://prospect.org/2026/04/17/american-politics-inundated-with-ai-deepfakes/

[^26]: NOTUS — 'Hobbled' Campaign Finance Regulator Cancels Public Meetings Until 2026: https://www.notus.org/2026-election/federal-election-commission-fec-quorum-shut-down-trump-nominees; NOTUS — Trump Finally Nominated New FEC Commissioners. But Their Confirmations Could Languish: https://www.notus.org/money/federal-election-commission-nominees-shutdown-trump; Perkins Coie — Federal Election Commission Poised to Regain Quorum: https://perkinscoie.com/insights/update/federal-election-commission-poised-regain-quorum; NPR — The FEC hasn't had a quorum for months, halting its work (October 2025): https://www.npr.org/2025/10/04/nx-s1-5559763/fec-no-quorum-campaign-finance; Brennan Center — As of Thursday, the FEC Can't Enforce Campaign Finance Laws: https://www.brennancenter.org/our-work/analysis-opinion/today-fec-cant-enforce-campaign-finance-laws-and-thats-only-one-its

[^27]: FEC — Commission approves Notification of Disposition, Interpretive Rule on Artificial Intelligence in Campaign Ads (September 19, 2024): https://www.fec.gov/updates/commission-approves-notification-of-disposition-interpretive-rule-on-artificial-intelligence-in-campaign-ads/; Federal Register — Artificial Intelligence in Campaign Ads (2024-21979): https://www.federalregister.gov/documents/2024/09/26/2024-21979/artificial-intelligence-in-campaign-ads

[^28]: CampaignNow — Regulators Scramble as AI Deepfakes Flood the 2026 Midterms: https://www.campaignnow.com/blog/regulators-scramble-as-ai-deepfakes-flood-the-2026-midterms; EPIC — Generative AI and Elections: The Approaching Train Wreck: https://epic.org/generative-ai-and-elections-the-approaching-train-wreck/

[^29]: AdWave — FCC Political Advertising Rules: 2026 Compliance Guide: https://adwave.com/resources/fcc-political-advertising-rules-2026; FCC — Political Programming: https://www.fcc.gov/media/policy/political-programming; CRS — Identifying TV Political and Issue Ad Sponsors in the Digital Age (R46516): https://www.congress.gov/crs-product/R46516

[^30]: Public Citizen — 30 States Now Have Laws to Regulate Election Deepfakes: https://www.citizen.org/news/30-states-now-have-laws-to-regulate-election-deepfakes/; Public Citizen — Tracker: Legislation on Deepfakes in Elections: https://www.citizen.org/article/tracker-legislation-on-deepfakes-in-elections/

[^31]: Conference Board — Federal Judge Strikes Down California Deepfake Law: https://www.conference-board.org/research/CED-Newsletters-Alerts/federal-judge-strikes-down-california-deepfake-law; TechPolicy.Press — Regulating Election Deepfakes: A Comparison of State Laws: https://www.techpolicy.press/regulating-election-deepfakes-a-comparison-of-state-laws/

[^32]: White House — Ensuring a National Policy Framework for Artificial Intelligence (December 11, 2025): https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/; Sidley — Unpacking the December 11, 2025 Executive Order (December 23, 2025): https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/

[^33]: NPR — Trump is trying to preempt state AI laws via an executive order. It may not be legal (December 2025): https://www.npr.org/2025/12/11/nx-s1-5638562/trump-ai-david-sacks-executive-order

[^34]: Goodwin Law — Trump's AI Preemption Executive Order Unlikely to Put a Lid on State AI Laws (December 2025): https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-otherindustries-trumps-ai-preemption-executive-order

[^35]: Digital Services Act — Wikipedia: https://en.wikipedia.org/wiki/Digital_Services_Act; AlgorithmWatch — A guide to the Digital Services Act, the EU's law to rein in Big Tech: https://algorithmwatch.org/en/dsa-explained/; EU Digital Services Act official page: https://digital-strategy.ec.europa.eu/en/policies/digital-services-act

[^36]: IAPP — New rules regulate data-use in EU political campaigns: https://iapp.org/news/a/personal-data-in-political-campaigns; Qomon — What Is Regulation (EU) 2024/900 and TTPA: https://qomon.com/blog/gdpr-900-a-new-era-for-political-and-advocacy-data-in-europe

[^37]: European Business Magazine — EU Prepares Tougher Tech Enforcement in 2026 as Trump Warns of Retaliation: https://europeanbusinessmagazine.com/european-news/eu-prepares-tougher-tech-enforcement-in-2026-as-trump-warns-of-retaliation/; Euronews — EU Takes on Big Tech: Top Actions Regulators Have Taken in 2025: https://www.euronews.com/next/2025/12/17/eu-takes-on-big-tech-here-are-the-top-actions-regulators-have-taken-in-2025

[^38]: TechPolicy.Press — Meta and Google's Ad Ban Upends Political Campaigning in Europe: https://www.techpolicy.press/meta-and-googles-ad-ban-upends-political-campaigning-in-europe/; TechPolicy.Press — What Data Reveals About Meta and Google's Political Ad Ban in the EU: https://www.techpolicy.press/what-data-reveals-about-meta-and-googles-political-ad-ban-in-the-eu/

[^39]: EU AI Act Article 50 text: https://artificialintelligenceact.eu/article/50/; Resemble.ai — The EU AI Act: What Generative AI Companies Need to Know in 2026: https://www.resemble.ai/resources/the-eu-ai-act-what-generative-ai-companies-need-to-know-in-2026; Blackbird.AI — Deepfake Detection Now Required Under EU AI Act Rules: https://blackbird.ai/blog/deepfake-detection-required-eu-ai-act-blackbird-ai-compass/

[^40]: European Commission — Code of Practice on Marking and Labelling of AI-Generated Content: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content; Jones Day — European Commission Publishes Draft Code of Practice on AI Labelling and Transparency (January 2026): https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency; Ashurst — Transparency of AI-generated content: the EU's first draft Code of Practice: https://www.ashurst.com/en/insights/transparency-of-ai-generated-content-the-eu-first-draft-code-of-practice/

[^41]: Audit Socials — Meta AI Chat Ad Targeting 2026: Disclosure and EU Carve-Out: https://www.auditsocials.com/blog/meta-ai-chat-data-ad-targeting-2026-disclosure-opt-out-eu-carve-out-advertiser-implications

[^42]: International IDEA — Navigating the European Union's Digital Regulatory Framework: Part 1 (Compact Overview of Impact on Electoral Processes): https://www.idea.int/publications/catalogue/html/navigating-european-unions-digital-regulatory-framework-part-1-compact

[^43]: Consumer Finance Monitor — House Committee Releases SECURE Data Act (May 12, 2026): https://www.consumerfinancemonitor.com/2026/05/12/u-s-house-committee-releases-secure-data-act-to-establish-new-federal-privacy-framework/; IAPP — SECURE Data Act Analysis: https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill

[^44]: Congress.gov — NO FAKES Act of 2025 (S.1367): https://www.congress.gov/bill/119th-congress/senate-bill/1367; Congress.gov — NO FAKES Act of 2025 (H.R.2794): https://www.congress.gov/bill/119th-congress/house-bill/2794/text

[^45]: Rep. Foushee — Protecting Consumers from Deceptive AI Act (April 24, 2026): https://foushee.house.gov/media/press-releases/reps-foushee-beyer-and-moylan-introduce-the-protecting-consumers-from-deceptive-ai-act-to-establish-accountability-and-transparency-standards-for-generative-ai

[^46]: Brennan Center — States Take the Lead in Regulating AI in Elections — Within Limits: https://www.brennancenter.org/our-work/research-reports/states-take-lead-regulating-ai-elections-within-limits; Brennan Center — Preparing to Fight AI-Backed Voter Suppression: https://www.brennancenter.org/our-work/research-reports/preparing-fight-ai-backed-voter-suppression; Brennan Center — Gauging the AI Threat to Free and Fair Elections: https://www.brennancenter.org/our-work/analysis-opinion/gauging-ai-threat-free-and-fair-elections; Brookings — Policy Framework for Generative AI in Political Ads: https://www.brookings.edu/articles/a-policy-framework-to-govern-the-use-of-generative-ai-in-political-ads/

[^47]: Senator Warner — Pushing Tech Companies to Take Action Against Deepfakes (March 2026): https://www.warner.senate.gov/public/index.cfm/2026/3/warner-pushes-tech-companies-to-take-action-against-deepfakes-maliciously-manipulated-media

---

*Domain 40 — Phase 2 Research — Resistance Research Framework*
*Produced May 15, 2026 | Distribution target July 15, 2026 | Hard constraint November 3, 2026*
*Research agent: General Research Agent (Claude Sonnet 4.6) | Session: Phase 2 Domain 40 initiation*
