# Domain 40: Surveillance Capitalism and Electoral Manipulation

**Title**: Surveillance Capitalism and Electoral Manipulation: How Commercial Data Infrastructure Became Democratic Attack Infrastructure

**Research completed**: May 14, 2026
**Distribution target**: July 15, 2026 — election protection organizations, digital rights advocates, campaign finance transparency groups
**Hard external deadline**: November 3, 2026 (2026 US midterm election)
**EU enforcement hook**: August 2, 2026 — EU AI Act Article 50 enters enforcement (maximum-attention advocacy window)
**Word count**: ~3,200
**Citations**: 32 sourced references
**Status**: Complete — Phase 2 production

**Cross-domain connections**:
- Domain 43 (Epistemic Infrastructure/Deepfakes): Domain 43 analyzes deepfakes as an epistemic crisis. Domain 40 analyzes the commercial distribution infrastructure that delivers deepfakes to targeted voters at scale. These are complementary tracks: Domain 43 covers information-environment harm; Domain 40 covers the data broker targeting supply chain.
- Domain 37 (Federal Executive Interference in 2026 Midterms): Domain 37 covers government-side election interference. Domain 40 covers the private-sector manipulation infrastructure operating independently of — but potentially in coordination with — executive interference. In 2026, election manipulation runs on both tracks simultaneously with no single regulatory body having authority over the combined system.
- Domain 25 (FISA 702/Surveillance): The commercial data broker loophole that remains open after the June 12, 2026 FISA extension is structurally connected to voter targeting. What the government cannot constitutionally collect directly, it can purchase commercially — and campaigns access the same marketplace.
- Domain 36 (AI Governance): Domain 36 covers AI in government decision-making; Domain 40 covers AI in electoral manipulation. Both flow from the same statutory vacuum.
- Domain 33 (State Legislative Autocratization): Geofencing churches and community meeting locations to deliver suppression messaging to specific racial and demographic communities is the synthesis point between state-level autocratization strategy and commercial surveillance tools.

---

## Executive Summary

The electoral manipulation threat of 2026 is not primarily from foreign interference or lone bad actors. It is from the systematic integration of commercial surveillance infrastructure — data brokers, social media platforms, AI generation tools — with political targeting operations, in an environment where no federal regulation governs the result.

Four components form the attack infrastructure. First, data brokers — Thomson Reuters CLEAR, LexisNexis Accurint, and hundreds of specialized political data companies — aggregate voter rolls, consumer behavior, location records, court filings, and social media into behavioral voter profiles usable for targeting at a specificity that no prior campaign technology achieved. Second, AI-generated synthetic content — deepfake videos, voice-cloned audio, synthetic text — is deployed at industrial scale in the 2026 midterm cycle: the NRSC's deepfake of Texas candidate James Talarico (March 2026) represents the first national party committee deployment of a lifelike synthetic candidate video. Third, geofencing and microtargeting match these profiles to hyper-localized advertising systems, creating distinct information environments for different voter segments — with documented effects on turnout: a February 2026 PNAS study found targeted digital voter suppression ads reduced turnout 1.9 percent among exposed individuals, disproportionately affecting non-white voters in battleground counties. Fourth, a regulatory vacuum: the FEC deadlocked and cannot issue AI deepfake guidance, the FCC's robocall prohibition does not extend to digital advertising, no federal law bans political deepfakes, and the December 2025 AI preemption executive order targets the 28-state disclosure patchwork that is the only existing accountability layer.

Meanwhile, the European Union has enacted substantive structural constraints. The DSA prohibits political microtargeting using sensitive personal data categories. EU Regulation 2024/900 (the Transparency and Targeted Political Advertising regulation) bans microtargeting using political opinions, religious beliefs, racial origin, sexual orientation, and political affiliations. EU AI Act Article 50 mandates machine-readable marking and user disclosure for AI-generated synthetic content — enforcement begins August 2, 2026. Meta, Google, and X comply with these requirements in European markets while deploying unregulated manipulation infrastructure in US elections. This is regulatory arbitrage at democratic scale.

The domain proposes an integrated reform architecture: voter data broker regulation as election law, categorical prohibition on photorealistic AI-generated synthetic candidate content, congressional mandate for FEC binding rulemaking, and reversal of the December 2025 preemption order to preserve state authority as a federal floor is established.

---

## 1. The Data Broker Architecture: From Consumer Surveillance to Voter Targeting

### 1.1 The Commercial Data Pipeline

Every political campaign begins with a voter file — the list of registered voters purchased from state election authorities — providing names, addresses, party registration (in most states), and voting history. That file is the foundation. The manipulation infrastructure is what campaigns append to it.

Commercial data brokers transform a basic voter list into a psychographic targeting platform by matching voter records against their proprietary databases and appending hundreds of additional data points: purchase histories from loyalty programs, location histories from smartphone app data sold to aggregators, inferred religious and political beliefs from behavioral signals, financial stress indicators from credit bureau data, and social media activity scraped across platforms. In 2020, Open Secrets documented that political groups paid 37 different data brokers at least $23 million for data services in a single cycle. The 2026 midterm advertising spend is projected at $10.8 billion, with an increasing share channeled through AI-enhanced precision targeting driven by these profiles.[^1]

The major players in this architecture operate across both commercial and government sectors without distinction. Thomson Reuters CLEAR — which holds six ICE contracts worth a total potential value of approximately $54 million[^2] — markets the same aggregated data products (license plate records, real estate transactions, court filings, professional licenses, arrest histories, organizational affiliations, Social Security and utility records) to law enforcement and to commercial clients.[^3] LexisNexis Accurint maintains records on over 276 million US residents;[^4] its PowerView Score incorporates Equifax credit data to generate consumer financial profiles that campaigns use for economic messaging targeting. Specialized political data firms — L2 (claiming data on 220 million voters), TargetSmart (claiming 171 million cell phone numbers matched to voter files), i360 — build partisan voter profiles using all of the above, enriched with dark web data, consumer transaction records, and social media scraping.[^5]

The data does not stay in separate silos. Thomson Reuters CLEAR is integrated in a system-to-system configuration with Palantir's analytical platform,[^6] allowing a single query to combine public record aggregations, commercial consumer data, and law enforcement investigative tools. The same query infrastructure used by ICE to identify deportation targets — and the same Palantir ELITE system used to generate deportation targeting lists from Medicaid enrollment data — is available to political campaigns and PACs through commercial licensing arrangements. The commercial surveillance architecture does not discriminate between use cases.

### 1.2 The Government-Private Data Synthesis: DOJ Voter File Demands

The Trump administration's voter file collection campaign represents the most direct documented instance of government-private data broker synthesis in electoral management.

Beginning in May 2025, the Department of Justice demanded copies of complete voter registration databases from at least 33 states, seeking sensitive information including driver's license numbers, the last four digits of Social Security numbers, partisan affiliations, and voting histories. At least 27 of these states received demands for the voter files themselves.[^7] By March 2026, the DOJ had sued 29 states and the District of Columbia for refusing to provide their sensitive voter data.[^8]

The Brennan Center obtained and published confidential Memoranda of Understanding outlining the DOJ's plans for collected data. The MOU establishes that DOJ will "test, analyze, and assess states' voter rolls" and then instruct states to remove specific voters within 45 days — reversing the traditional state authority over voter roll maintenance. More critically for the surveillance capitalism nexus: the MOU permits voter files to be shared with contractors for "list maintenance verification" with minimal security safeguards — no binding encryption requirements, no audit logs, no restrictions on contractor data retention or resale.[^9]

Seven federal courts in seven states have dismissed the DOJ litigation,[^10] with one federal judge calling it a "fishing expedition." Rhode Island, California, Massachusetts, Michigan, Oregon, and Arizona courts have rejected the DOJ's legal theory. But 13 states have already complied — Alaska, Arkansas, Indiana, Louisiana, Mississippi, Nebraska, Ohio, Oklahoma, South Carolina, South Dakota, Tennessee, Texas, and Wyoming — providing voter files with sensitive identifying information to federal contractors with no enforceable data security standards.[^11]

The structural significance: voter registration data combined with commercial data broker behavioral profiles creates targeting capability far beyond what state voter files alone provide. The government is constructing a centralized voter database that, under the current MOU framework, can be accessed by commercial contractors with no restriction on integration with the broader commercial data ecosystem.

### 1.3 Geofencing, Location Targeting, and Suppression Infrastructure

The third component of the targeting architecture is location-based. Political campaigns have used geofencing — drawing a virtual perimeter around a physical location and capturing the device IDs of smartphones that enter it — since at least 2019, when NPR documented campaigns geofencing Catholic churches to target churchgoing voters with messaging calibrated to their inferred religious beliefs.[^12]

By 2026, the methodology is substantially more sophisticated. Campaigns can geofence community meeting locations, polling places, Black churches, immigrant service centers, and voter registration drives to capture the device IDs of attendees. Those device IDs are then matched against commercial data broker voter profiles, generating targeting lists that can be served microtargeted suppression messages on streaming video, social media, and connected television without the targets ever knowing they were identified.

The voter suppression effect is no longer theoretical. A February 2026 peer-reviewed PNAS study — the first empirical confirmation of digital voter suppression in an actual election — documented that participants exposed to digital voter suppression ads were 1.9 percent less likely to vote. Non-white voters in racial minority counties of battleground states received such ads nearly 10 times more often than white voters in white-majority counties in non-battleground states. Extrapolated to the 2016 election, the researchers estimated the ads may have prevented approximately 4.7 million people from voting.[^13] A 1.9 percent suppression effect, targeted at specific demographic groups in specific precincts, would determine outcomes in elections decided by less than 0.5 percent margins — the margins that decided Georgia, Arizona, and Nevada in 2020.

The critical democratic design problem: targeted digital voter suppression leaves no statutory footprint. It does not require passing a voter ID law. It does not require closing a polling location. It requires only a commercial data broker subscription, a geofencing platform, and AI-generated content — and there is currently no federal law requiring disclosure of suppression targeting, no requirement for campaigns to report what data they used, and no FEC or FTC enforcement mechanism with jurisdiction over this conduct.

---

## 2. AI-Generated Voter Manipulation: Industrial Scale in 2026

### 2.1 The Watershed Cases

The 2026 midterm cycle is the first US electoral cycle in which AI-generated political content operates as a documented standard tool of major party campaign operations. Three cases establish the arc from proof-of-concept to national party deployment.

**The Biden New Hampshire robocall (January 2024)**: A Democratic consultant hired a magician to use the AI voice-generation tool ElevenLabs to impersonate President Biden in robocalls sent to New Hampshire primary voters, instructing them not to vote in the primary. The operation cost approximately $500 for distribution. The production itself — generating a photorealistic voice clone sufficient to deceive voters — took under 20 minutes and used a publicly available commercial tool.[^14] The FCC's subsequent ruling that AI-generated voices in robocalls violate the Telephone Consumer Protection Act closed the robocall channel while leaving all digital, social media, and television advertising channels completely unregulated.

**The Collins-Ossoff deepfake (November 2025)**: Rep. Mike Collins (R-GA), running against incumbent Democratic Sen. Jon Ossoff in Georgia's 2026 Senate race, released an AI-generated deepfake video depicting Ossoff mocking farmers and defending a government shutdown. "The only reason a candidate would need to use a deepfake," the Ossoff campaign responded, "is if they didn't think they could win on their own." The video included a small on-screen disclaimer stating the video was AI-generated, satisfying Georgia's disclosure requirements while remaining an intentional deception. The Collins campaign confirmed it planned to continue using AI tools, stating it would "be at the forefront embracing new tactics."[^15]

**The NRSC-Talarico deepfake (March 11, 2026)**: The National Republican Senatorial Committee posted an attack ad depicting Texas Democratic Senate candidate James Talarico appearing to read excerpts from his past tweets on transgender issues, race, religion, and Planned Parenthood — with additional fabricated statements the real Talarico never made. This is the first deployment of a lifelike synthetic candidate video by a national party committee. The ad ran for over a minute with the deepfake "Talarico" speaking. A small "AI GENERATED" label appeared in the corner for approximately three seconds at the start, then remained in fainter smaller text for the remainder of the ad. Common Dreams reported Democratic Senator Andy Kim's response: "These deepfakes are dangerous and wrong. We need protections not just for politics, but for all Americans." The CNN story on March 13, 2026 noted it was "the first featuring a phony version of a candidate talking in a lifelike manner for so long — an example of how far AI technology has come in a short time."[^16][^17]

**The Virginia Spanberger deepfakes (February 2026, April 2026)**: The Loudoun County Republican Committee released an AI-generated video on February 23, 2026 depicting Governor Abigail Spanberger with fabricated statements sarcastically endorsing policies she opposes, including an animated sequence of the Spanberger figure setting fire to a religious painting. No disclaimer or "AI generated" label appeared in the post; the caption read simply "Thanks @GovernorVA !!!!!" The video used her official 2023 congressional portrait as source material.[^18] In April 2026, a separate anti-redistricting group released a 30-second ad with an AI-generated fake Spanberger video accompanying narration that she "wants to burn Virginia's democracy to the ground."[^19] The Virginia Spanberger cases are significant: the February ad involved no disclosure at all, demonstrating that even disclosure-only state laws are not universally followed.

### 2.2 The Production Cost Threshold Has Collapsed

The democratic design implications of these cases cannot be understood without grasping the production cost collapse. The Biden NH robocall — which the FCC estimated generated "$5 million worth of action" through media coverage — cost $500 for distribution and under 20 minutes of production time with a free commercially available tool. The WEF's March 2026 analysis documents that deepfakes have "crossed a critical threshold in 2026, having improved and eliminated earlier tell-tale glitches and are now accessible to anyone with a smartphone."[^20]

The practical meaning: the production barriers that previously concentrated deepfake capability in well-resourced operations have collapsed. Any campaign, PAC, or political operative with $500 and 20 minutes can produce content sufficient to deceive voters. At the national party committee level, the NRSC's Talarico video demonstrates that sophisticated, extended lifelike deepfake videos are now standard-issue campaign tools. The 2026 midterm cycle is the first in which deepfake voter manipulation operates as normal campaign practice rather than exceptional bad behavior.

### 2.3 Disclosure Without Prohibition Is Compliance-as-Cover

All four major 2026 deepfake cases operated within existing disclosure frameworks. The NRSC's Talarico video displayed "AI GENERATED" in small text for three seconds. The Collins-Ossoff video included a disclaimer satisfying Georgia's requirements. The Virginia redistricting video complied with Virginia's disclosure law. The compliance did not reduce the deception.

This is the foundational problem with disclosure-only regulatory frameworks for AI-generated political content: a viewer who did not notice a small-text disclaimer in the corner of a video for three seconds has been deceived regardless of technical compliance. The disclosure architecture was designed for print advertising footnotes; it does not translate to video formats where the emotional impact of seeing a candidate "say" something they never said cannot be reversed by three seconds of small text.

The American Prospect analysis of the 2026 midterm deepfake landscape (April 17, 2026) documents that most state laws only require disclosure rather than prohibition. The NRSC's Talarico video complied with Texas disclosure law while remaining an intentional deception. "Legislation is a noble effort, but the technology is moving so fast," the article quotes election law experts.[^21]

---

## 3. The Regulatory Vacuum: Three Failure Modes

### 3.1 FEC Deadlock and the Non-Binding Interpretive Rule

On September 19, 2024, the FEC voted not to open a rulemaking on AI in campaign ads. The Commission's 3-3 partisan deadlock — which has prevented binding rulemaking on this issue since 2023, when the FEC failed to vote on a notice of availability in response to a Public Citizen petition — produced instead an "Interpretive Rule" clarifying that existing fraudulent misrepresentation statutes apply regardless of technology used.[^22]

The Interpretive Rule is not a regulation. It has no enforcement teeth beyond what the existing statute already provides. The existing statute — 52 U.S.C. § 30124, which prohibits fraudulent misrepresentation of a candidate — has never been successfully applied to a political deepfake case. There is no definition in FEC regulations of what constitutes AI-generated "fraudulent misrepresentation" as distinct from ordinary campaign attack rhetoric. The FEC's interpretive position is that deepfakes are covered by existing law; the practical result is that no deepfake creator has faced FEC enforcement.

The FEC's structural incapacity is not a temporary gridlock. It is a design problem: the six-commissioner structure with equal partisan representation was built on the assumption that partisan commissioners would cooperate on process even when disagreeing on policy. The AI regulatory environment has broken that assumption. Without a congressional mandate specifying what the FEC must regulate and how to break ties, the FEC cannot produce binding guidance in this area.

### 3.2 FCC's Robocall Prohibition: Closing the Wrong Channel

The FCC's February 2024 ruling that AI-generated voices in robocalls violate the Telephone Consumer Protection Act was an enforcement action in response to the Biden NH robocall. The ruling was appropriate. It was also largely irrelevant to the 2026 deepfake landscape: the robocall channel is the one channel where AI-generated content was already reaching voters in ways that existing law could clearly address.

The 2026 deepfake cases — NRSC-Talarico, Collins-Ossoff, Virginia Spanberger — were all distributed through social media and digital advertising channels. The TCPA does not apply to digital advertising. The FCC has no jurisdiction over political advertising on social media platforms. The FCC's action in the robocall domain was appropriate, but it addressed the channel with the narrowest reach while leaving the channels with the broadest reach — social media, connected television, digital advertising networks — completely unregulated.[^23]

### 3.3 The December 2025 AI Preemption Executive Order

On December 11, 2025, President Trump signed an executive order titled "Ensuring a National Policy Framework for Artificial Intelligence," directing the Department of Justice to establish an AI Litigation Task Force to challenge state AI laws, directing the FTC to issue a policy statement identifying circumstances under which state AI laws requiring alterations to AI outputs are preempted by federal law, and directing the FCC to follow the White House AI action plan to circumvent "onerous" state regulations.[^24]

The executive order targets the only existing accountability layer over AI-generated political content: the 28-state patchwork of disclosure requirements. As of January 2026, 28 states had enacted laws specifically addressing AI deepfakes in political communications — predominantly disclosure requirements with smaller prohibitory elements.[^25] State-level disclosure legislation is the only mechanism that has produced any accountability response to documented deepfake deployment in the 2026 cycle.

The preemption theory in the order is constitutionally contested. NPR's legal analysis reported that "Trump's executive order can easily be challenged and overturned in court unless Congress passes legislation to restrict states from passing AI laws" — and that "until relevant legal challenges are resolved, state laws remain enforceable."[^26] Goodwin Law's analysis found the order "unlikely to put a lid on state AI laws" given constitutional limits on executive preemption authority.[^27] But the order does not need to win in court to achieve its objective. Its chilling effect on state legislative action — states that planned to expand disclosure requirements to prohibition requirements are now assessing litigation risk before proceeding — is already operating. The 28-state patchwork has not expanded since December 2025.

---

## 4. The EU Accountability Divergence: Same Companies, Different Standards

### 4.1 DSA and the Political Advertising Regulation

The EU Digital Services Act prohibits platforms from showing targeted advertising based on special categories of sensitive personal data, including political opinions, religious beliefs, racial or ethnic origin, and sexual orientation.[^28] EU Regulation 2024/900 — the Transparency and Targeting of Political Advertising regulation, which entered force in October 2025 — goes further: it bans microtargeting using political opinions, prohibits the use of sensitive data categories for political targeting purposes, requires explicit consent for all political data collection, mandates disclosure of who funded political advertising and what targeting criteria were used, and establishes safeguards against AI-driven microtargeting of sensitive categories.[^29]

The DSA enforcement record demonstrates these are not paper standards. On December 5, 2025, the European Commission issued its first non-compliance decision under the DSA, fining X €120 million ($140 million) for breaches including ad transparency failures and deceptive design.[^30] In October 2025, Meta exited the political advertising market in Europe entirely rather than attempt compliance with the TTPA's targeting restrictions — removing the EU as a market for political microtargeting rather than adapting its tools to comply.[^31] This is not the behavior of a company that considers EU standards cosmetic.

### 4.2 EU AI Act Article 50: Deepfake Labeling Enforcement Begins August 2, 2026

EU AI Act Article 50 imposes transparency obligations on AI-generated synthetic content. Deployers must disclose when AI creates realistic synthetic content, including deepfakes, through machine-readable marking and clear user notification. The European Commission published the first draft Code of Practice on Marking and Labelling of AI-Generated Content in December 2025, incorporating feedback from industry, civil society, and academia. A final code was anticipated in June 2026 ahead of the Article 50 enforcement date of August 2, 2026.[^32]

The Article 50 framework is substantively different from US disclosure approaches in two ways. First, the machine-readable marking requirement means platforms — not just creators — have affirmative obligations to detect and label AI-generated content. A small on-screen text disclaimer that appears for three seconds does not satisfy Article 50. Second, Article 50 applies to platforms as well as to content creators, closing the distribution-layer accountability gap that allows deepfake content to circulate on social media without platform-level intervention.

### 4.3 The Regulatory Arbitrage Problem

Meta, Google, and X — the three platforms through which 2026 US midterm deepfake content is primarily distributed — all comply with EU DSA and Article 50 standards for European political markets while applying only voluntary self-regulatory standards to US political markets.

Meta's European political advertising exit demonstrates the practical effect: rather than apply EU-compliant political advertising standards globally, Meta built a geographic carve-out. EU users are protected from political microtargeting using sensitive data categories; US users are not. The same targeting tools that are prohibited for use against European voters are available for deployment against American voters with no regulatory constraint.[^33]

This is regulatory arbitrage at democratic scale. The companies have demonstrated they possess the technical capability to comply with the EU's substantive requirements — they already do so in European markets. The question is not whether compliance is technically possible but whether the US regulatory environment creates any obligation to extend those protections to American voters. It does not.

The August 2, 2026 enforcement date for EU AI Act Article 50 creates a specific advocacy window: in the period between the July 2026 distribution of this document and August enforcement, the contrast between EU substantive protection and US regulatory vacuum will be at maximum visibility in tech policy, election law, and digital rights coverage. The argument — same companies, same technology, different accountability standards applied to US and European voters — is most powerful in that window.

---

## 5. Reform Architecture: What Structural Regulation Would Require

The regulatory failures documented in Sections 3 and 4 are not accidents. They are the product of a commercial surveillance industry that has successfully prevented the development of accountability frameworks covering its electoral use cases. The reform architecture required to address the threat documented in this domain has four structural components.

### 5.1 Voter Data as a Specially Protected Category

The current legal framework treats voter registration data as ordinary government records subject to standard public records access. In most states, voter files are purchasable by any party for any purpose. Data brokers can purchase voter files and append them to commercial behavioral profiles without restriction. The DOJ voter file collection campaign — operating under a confidential MOU framework with minimal security standards — represents the logical endpoint of treating voter data as undifferentiated government information.

The reform required is a federal Voter Data Protection framework: designation of voter registration data as a specially protected category under federal privacy law, prohibiting data brokers from incorporating voter file information into commercial behavioral profiles without explicit statutory authorization; requiring any contractor receiving voter data from a government source to comply with security standards equivalent to the Federal Information Security Management Act; and creating a private right of action for voters whose registration data is disclosed in violation of the protection framework.

The April 2026 SECURE Data Act — the House Republican comprehensive privacy bill — establishes data broker registration requirements and a federal privacy floor.[^34] It does not contain voter-specific protections. The gap between a general privacy framework and a voter data protection framework is the gap between treating voter data as consumer information and treating it as a component of democratic infrastructure.

### 5.2 AI-Generated Synthetic Candidate Content: Beyond Disclosure

The documented failure of disclosure-only frameworks — NRSC-Talarico complied with Texas disclosure law while remaining an intentional deception; the Virginia Spanberger video deployed with no disclosure at all; the Collins-Ossoff ad satisfied Georgia law — establishes that disclosure requirements do not prevent voter manipulation. The reform architecture must go beyond disclosure.

The legislative options span a spectrum. The NO FAKES Act of 2025 (S.1367, H.R. 2794, reintroduced April 2025 and referred to Senate Judiciary Committee) establishes a federal right of publicity against unauthorized digital replicas — but focuses on the content creator and production side rather than the electoral distribution context.[^35] The Protecting Consumers from Deceptive AI Act (introduced April 24, 2026) would establish technical standards for AI content disclosure — stronger than existing state frameworks but still disclosure-based.[^36]

The reform that matches the scale of the documented harm is a categorical prohibition on photorealistic AI-generated video and audio depicting real federal candidates in paid political advertising, with a safe harbor for clearly satirical content. This approach — prohibition rather than disclosure — aligns with how the EU has structured its protections (DSA prohibition on sensitive data targeting rather than disclosure of targeting) and addresses the mechanism the documented 2026 cases demonstrate: disclosure does not prevent deception.

Several state-level prohibition bills provide legislative models. Texas SB753 prohibits election-related deepfake videos within 30 days of elections. Maryland SB0141 criminalizes election-related deepfakes. These state prohibition models — not Texas's disclosure approach, which the NRSC's Talarico video exploited — are the correct federal template.

### 5.3 FEC Mandatory AI Rulemaking: Breaking the Deadlock

The FEC's 3-3 partisan deadlock on AI regulation is not resolvable through FEC internal process. The Commission has demonstrated it cannot reach consensus on rulemaking. The reform required is a congressional mandate specifying: (a) the FEC must complete a rulemaking on AI-generated political content within 180 days of enactment; (b) the rulemaking must establish specific requirements for machine-readable content provenance disclosure and platform-level detection obligations (parallel to EU AI Act Article 50); (c) in the event of continued commission deadlock, a specified tie-breaking mechanism (chair vote, NAB/FTC determination, or expedited OIRA review) applies.

Senator Warner's March 2026 call for congressional action in response to the NRSC-Talarico video provides the legislative hook.[^37] The Protecting Consumers from Deceptive AI Act introduced April 2026 establishes some content standards but does not resolve the FEC enforcement vacuum. A targeted FEC rulemaking mandate — modeled on the congressional mandates that have resolved prior FEC deadlocks — is the most direct path to enforceable federal standards before the November 2026 election.

### 5.4 Federal Floor and State Authority Preservation

The December 2025 AI preemption executive order is premised on a regulatory vision in which a permissive federal standard preempts more protective state standards. The democratic design logic runs in the opposite direction: state experimentation — the 28-state patchwork that includes both disclosure and prohibition frameworks — represents the only functioning accountability layer currently operating over AI-generated political content.

The reform architecture must reverse the preemption logic: federal law should establish a minimum floor that the 28 states with AI disclosure requirements already exceed, while explicitly preserving state authority to enact more protective standards. This anti-preemption model — federal floor plus state authority — mirrors the NVRA's structure on voter registration and the Clean Air Act's structure on environmental standards. It preserves the laboratory function of state innovation while establishing a federal baseline that prevents the most egregious uses of AI-generated manipulation in elections that lack any state law.

---

## 6. The November 3 Constraint: Why This Window Is Closing

The 2026 midterm election — November 3, 2026 — is the structural constraint on reform timeline. The documented developments in this domain are not preliminary indicators; they are the current operational reality of the 2026 election cycle. The NRSC deployed a national party deepfake in March 2026. Collins deployed a Georgia Senate deepfake in November 2025. The Loudoun County Republican Committee deployed a deepfake of a sitting governor with no disclosure in February 2026. These are not isolated incidents; they are documented proof that AI-generated voter manipulation is now standard campaign practice.

The advocacy timeline required to achieve any regulatory response before November 3 is:
- **July 2026**: Distribution to election protection organizations (Brennan Center Elections Program, Protect Democracy, Democracy Docket), digital rights organizations (EFF, EPIC, CDT), and campaign finance transparency organizations (OpenSecrets, Campaign Legal Center). Congressional testimony and coalition letter campaigns.
- **August 2, 2026**: EU AI Act Article 50 enforcement begins. Maximum media window for US-EU comparison argument.
- **August–September 2026**: Congressional recess ends; any floor action on deepfake legislation must occur in this window to have effect before the November election.
- **November 3, 2026**: Hard deadline. No regulatory response enacted after this date can address the 2026 election cycle.

The interim actions available before legislation is enacted: FEC commissioners can individually request reconsideration of the September 2024 interpretive rule, triggering a new commission vote. The FTC has existing Section 5 authority over unfair and deceptive practices that may extend to AI-generated voter manipulation; an FTC policy statement could establish interim standards while FEC rulemaking proceeds. Platform-level pressure — coordinated advocacy with the Stanford Internet Observatory, Harvard Shorenstein Center, and Columbia Tow Center — can focus on platform policies that go beyond EU-minimum standards and apply globally.

---

## Unique Contribution

Domain 40 provides the framework's first systematic analysis of commercial surveillance infrastructure as electoral attack infrastructure. Domain 43 (Epistemic Infrastructure) covers the epistemic harm — what deepfakes do to the information environment. Domain 37 (Federal Executive Interference) covers the government side of election manipulation. Neither covers the commercial data broker industry as the supply chain that makes targeted voter manipulation possible at scale.

This domain also provides the first cross-domain synthesis connecting the data broker problem — which appears in Domain 25 as the FISA loophole, in Domain 36 as ImmigrationOS inputs, in Domain 48 as the government data purchase pipeline — to the electoral democracy problem specifically. The synthesis is the framework's unique contribution to the election protection movement: connecting commercial surveillance infrastructure to voting rights advocacy in a single democratic-design argument.

The regulatory arbitrage finding — same companies, EU compliance, US deregulation — is the advocacy handle most likely to generate media coverage, congressional attention, and platform pressure in the August 2026 window.

---

## Source Notes

[^1]: EFF — How Political Campaigns Use Your Data to Target You (April 2024): https://www.eff.org/deeplinks/2024/04/how-political-campaigns-use-your-data-target-you; OpenSecrets — Third-Party Brokers Selling Data to Political Groups: https://www.opensecrets.org/news/2022/04/the-third-party-brokers-who-make-millions-selling-your-data-to-political-groups/

[^2]: AFSC Investigate — Thomson Reuters: https://investigate.afsc.org/company/thomson-reuters; State of Surveillance — Data Brokers Selling to ICE: https://stateofsurveillance.org/articles/corporate/data-brokers-ice-contracts/

[^3]: LawNext — The Legal Tech Giants Powering ICE, Part 1 (April 2026): https://www.lawnext.com/2026/04/the-legal-tech-giants-powering-ice-part-1-how-thomson-reuters-and-lexisnexis-helped-support-americas-immigration-surveillance-machine.html; In These Times — Data Brokers Fueling ICE's Deportation Machine: https://inthesetimes.com/article/ice-deportation-machine-surveillance-artificial-intelligence-thomson-reuters-clear-trump

[^4]: LawNext — The Legal Tech Giants Powering ICE, Part 1 (April 2026): LexisNexis Accurint records on 276 million US residents, real-time jail booking data since 2021 expansion.

[^5]: GhostVault — Data Broker List 2026 (500+ sites): https://www.ghostvault.live/data-brokers; State of Surveillance — Data Brokers and Political Campaigns: https://stateofsurveillance.org/articles/surveillance/data-brokers-political-campaigns-voter-targeting/; EFF op. cit.

[^6]: AFSC Investigate — Thomson Reuters op. cit.: "CLEAR integrates with Palantir's analytical platform in a system-to-system configuration."

[^7]: Brennan Center — Justice Department Has Demanded Voter Files from at Least 27 States: https://www.brennancenter.org/our-work/analysis-opinion/justice-department-has-demanded-voter-files-least-21-states; Brennan Center — Tracker of Justice Department Requests for Voter Information: https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information

[^8]: NBC News — Tracking the DOJ's Effort to Get US Voter Registration Data: https://www.nbcnews.com/politics/justice-department/tracking-dojs-effort-get-us-voter-registration-data-rcna331509

[^9]: Brennan Center — Confidential Agreements Show Trump Administration's Plans for States' Voter Data: https://www.brennancenter.org/our-work/analysis-opinion/confidential-agreements-show-trump-administrations-plans-states-voter; Brennan Center — Justice Department Security Measures Are Inadequate: https://www.brennancenter.org/our-work/analysis-opinion/justice-departments-security-measures-collecting-voter-rolls-are

[^10]: NBC News — Judge Dismisses DOJ Lawsuit Seeking Arizona Voter Data: https://www.nbcnews.com/politics/justice-department/judge-dismisses-doj-lawsuit-seeking-arizona-voter-data-rcna342613; US News — Federal Judge Dismisses DOJ Lawsuit in Massachusetts: https://www.usnews.com/news/politics/articles/2026-04-09/a-federal-judge-dismisses-another-doj-lawsuit-seeking-voter-data-this-time-in-massachusetts; PBS — Federal Judge Dismisses DOJ Lawsuit in Rhode Island: https://www.pbs.org/newshour/politics/federal-judge-dismisses-doj-lawsuit-seeking-personal-details-about-rhode-island-voters

[^11]: Brennan Center tracker and AP reporting as summarized in multiple state compliance reports, see Brennan Center tracker op. cit.

[^12]: NPR — How Political Campaigns Are Using Geofencing to Target Catholics at Mass (February 2020): https://www.npr.org/2020/02/06/803508851/how-political-campaigns-are-using-geofencing-technology-to-target-catholics-at-m; The Markup — How Political Campaigns Use Your Phone's Location (November 2022): https://themarkup.org/privacy/2022/11/08/how-political-campaigns-use-your-phones-location-to-target-you

[^13]: PNAS 2026 — Targeted digital voter suppression efforts likely decrease voter turnout: https://www.pnas.org/doi/10.1073/pnas.2519944123; University of Wisconsin news release: https://news.wisc.edu/research-shows-social-media-advertising-suppresses-voting-in-targeted-communities/

[^14]: NBC News — A magician says a Democratic operative paid him to make the fake Biden New Hampshire robocall: https://www.nbcnews.com/politics/2024-election/biden-robocall-new-hampshire-strategist-rcna139760; NPR — What a robocall of Biden's AI-generated voice could mean for the 2024 election: https://www.npr.org/2024/02/07/1229856682/what-a-robocall-of-bidens-ai-generated-voice-could-mean-for-the-2024-election

[^15]: CBS Atlanta — Georgia Rep. Mike Collins' campaign uses AI-generated deepfake of Senator Jon Ossoff: https://www.cbsnews.com/atlanta/news/georgia-rep-mike-collins-campaign-uses-ai-generated-deepfake-of-senator-jon-ossoff-in-tight-senate-showdown/; AJC — Jon Ossoff warned about deepfakes. Now, an opponent has made him one: https://www.ajc.com/politics/2025/11/jon-ossoff-warned-about-deepfakes-now-he-is-one/

[^16]: CNN — Republicans release AI deepfake of James Talarico (March 13, 2026): https://www.cnn.com/2026/03/13/politics/james-talarico-ai-deepfake-republicans-midterms; OECD AI — AI Deepfakes Used to Mislead Voters in 2026 US Midterm Campaigns: https://oecd.ai/en/incidents/2026-03-28-b14f

[^17]: Common Dreams — 'This Should Be Illegal': Senate GOP Uses AI Deepfake to Attack Talarico: https://www.commondreams.org/news/gop-talarico-deepfake; CampaignNow — Regulators Scramble as AI Deepfakes Flood the 2026 Midterms: https://www.campaignnow.com/blog/regulators-scramble-as-ai-deepfakes-flood-the-2026-midterms

[^18]: Lead Stories Fact Check — Republican Committee Published Fake AI Campaign Video of Virginia Governor Spanberger (February 2026): https://leadstories.com/hoax-alert/2026/02/fact-check-republican-committee-published-fake-ai-campaign-video-of-virginia-governor-spanberger.html

[^19]: Virginia Independent — Anti-redistricting group uses fake AI-generated video of Spanberger in ad: https://virginiaindependentnews.com/elections/anti-redistricting-group-uses-fake-ai-generated-video-of-spanberger-in-ad/

[^20]: WEF — How cognitive manipulation and AI will shape disinformation in 2026 (March 2026): https://www.weforum.org/stories/2026/03/how-cognitive-manipulation-and-ai-will-shape-disinformation-in-2026/; AI CERTs News — How Political Misinformation Deepfakes Threaten 2026 Elections: https://www.aicerts.ai/news/how-political-misinformation-deepfakes-threaten-2026-elections/

[^21]: The American Prospect — American Politics Is Already Inundated With AI Deepfakes. It's Only Getting Worse (April 17, 2026): https://prospect.org/2026/04/17/american-politics-inundated-with-ai-deepfakes/

[^22]: FEC — Commission approves Notification of Disposition, Interpretive Rule on Artificial Intelligence in Campaign Ads (September 19, 2024): https://www.fec.gov/updates/commission-approves-notification-of-disposition-interpretive-rule-on-artificial-intelligence-in-campaign-ads/; Federal Register — Artificial Intelligence in Campaign Ads (2024-21979): https://www.federalregister.gov/documents/2024/09/26/2024-21979/artificial-intelligence-in-campaign-ads

[^23]: CampaignNow — Regulators Scramble, op. cit.; EPIC — Generative AI and Elections: https://epic.org/generative-ai-and-elections-the-approaching-train-wreck/

[^24]: White House — Ensuring a National Policy Framework for Artificial Intelligence (December 11, 2025): https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/; NPR — Trump is trying to preempt state AI laws via an executive order. It may not be legal: https://www.npr.org/2025/12/11/nx-s1-5638562/trump-ai-david-sacks-executive-order

[^25]: Multistate — State Deepfake Laws in 2026: What's Changed and What's Next (February 2026): https://www.multistate.us/insider/2026/2/12/how-ai-generated-content-laws-are-changing-across-the-country; Transparency Coalition — 2025 State AI Legislation Report: https://www.transparencycoalition.ai/news/transparency-coalition-publishes-2025-state-ai-legislation-report

[^26]: NPR — Trump is trying to preempt state AI laws, op. cit.

[^27]: Goodwin Law — Trump's AI Preemption Executive Order Unlikely to Put a Lid on State AI Laws (December 2025): https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-otherindustries-trumps-ai-preemption-executive-order

[^28]: Digital Services Act — Wikipedia: https://en.wikipedia.org/wiki/Digital_Services_Act; AlgorithmWatch — A guide to the Digital Services Act, the EU's law to rein in Big Tech: https://algorithmwatch.org/en/dsa-explained/; International IDEA — Navigating the European Union's Digital Regulatory Framework: https://www.idea.int/publications/catalogue/html/navigating-european-unions-digital-regulatory-framework-part-1-compact

[^29]: IAPP — New rules regulate data-use in EU political campaigns: https://iapp.org/news/a/personal-data-in-political-campaigns; qomon — What Is Regulation (EU) 2024/900 and TTPA: https://qomon.com/blog/gdpr-900-a-new-era-for-political-and-advocacy-data-in-europe

[^30]: European Business Magazine / EU enforcement 2025: EU Commission first DSA fine of €120 million against X (December 5, 2025); Euronews — EU takes on Big Tech: Top actions regulators have taken in 2025: https://www.euronews.com/next/2025/12/17/eu-takes-on-big-tech-here-are-the-top-actions-regulators-have-taken-in-2025

[^31]: TechPolicy.Press — Meta and Google's Ad Ban Upends Political Campaigning in Europe: https://www.techpolicy.press/meta-and-googles-ad-ban-upends-political-campaigning-in-europe/; Audit Socials — Meta AI Chat Ad Targeting 2026: Disclosure and EU Carve-Out: https://www.auditsocials.com/blog/meta-ai-chat-data-ad-targeting-2026-disclosure-opt-out-eu-carve-out-advertiser-implications

[^32]: EU AI Act Article 50 text: https://artificialintelligenceact.eu/article/50/; European Commission — Code of Practice on Marking and Labelling of AI-Generated Content: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content; Jones Day — European Commission Publishes Draft Code of Practice on AI Labelling and Transparency (January 2026): https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency; Herbert Smith Freehills — Transparency obligations for AI-generated content under the EU AI Act (March 2026): https://www.hsfkramer.com/notes/ip/2026-03/transparency-obligations-for-ai-generated-content-under-the-eu-ai-act-from-principle-to-practice

[^33]: TechPolicy.Press — What Data Reveals About Meta and Google's Political Ad Ban in the EU: https://www.techpolicy.press/what-data-reveals-about-meta-and-googles-political-ad-ban-in-the-eu/

[^34]: House Energy & Commerce — SECURE Data Act (April 22, 2026): https://www.consumerfinancemonitor.com/2026/05/12/u-s-house-committee-releases-secure-data-act-to-establish-new-federal-privacy-framework/; IAPP — SECURE Data Act Analysis: https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill

[^35]: Congress.gov — NO FAKES Act of 2025 (S.1367): https://www.congress.gov/bill/119th-congress/senate-bill/1367; Congress.gov — NO FAKES Act of 2025 (H.R.2794): https://www.congress.gov/bill/119th-congress/house-bill/2794/text

[^36]: Rep. Foushee — Protecting Consumers from Deceptive AI Act (April 24, 2026): https://foushee.house.gov/media/press-releases/reps-foushee-beyer-and-moylan-introduce-the-protecting-consumers-from-deceptive-ai-act-to-establish-accountability-and-transparency-standards-for-generative-ai

[^37]: Senator Warner — Pushing Tech Companies to Take Action Against Deepfakes (March 2026): https://www.warner.senate.gov/public/index.cfm/2026/3/warner-pushes-tech-companies-to-take-action-against-deepfakes-maliciously-manipulated-media; Brennan Center — Gauging the AI Threat to Free and Fair Elections: https://www.brennancenter.org/our-work/analysis-opinion/gauging-ai-threat-free-and-fair-elections; Brennan Center — Preparing to Fight AI-Backed Voter Suppression: https://www.brennancenter.org/our-work/research-reports/preparing-fight-ai-backed-voter-suppression

---

*Domain 40 — Phase 2 Research — Resistance Research Framework*
*Produced May 14, 2026 | Distribution target July 15, 2026 | Hard constraint November 3, 2026*
