---
title: "Electoral Interference Detection and Documentation Framework"
created: 2026-04-29
session: 627
status: production-ready
phase: "Phase 2 expansion — Domain 37 post-distribution"
related_domains:
  - "Domain 37 (Federal Executive Interference in 2026 Midterms)"
  - "Domain 37a (Post-Election Section 3 Litigation and Certification Recovery)"
  - "Domain 37b (State Election Security Coordination — Post-CISA Architecture)"
  - "Domain 21 (Data Privacy and Digital Surveillance)"
word_count: ~3200
---

# Electoral Interference Detection and Documentation Framework

*Session 627 — April 29, 2026*

*Production-ready guide for movement organizations, election protection practitioners, and legal teams preparing for the 2026 midterm cycle. Feeds Phase 2 Domain 37 post-distribution coordination with election-protection organizations.*

---

## Lead Finding

The most important development for 2026 is not a new adversary capability. It is the collapse of the domestic institutional infrastructure that was doing the detection. The FBI dissolved its Foreign Influence Task Force. CISA dismantled EI-ISAC, the national threat-sharing network for election security. The Office of the Director of National Intelligence is downsizing the Foreign Malign Influence Center. At the same time, the same federal apparatus is running what amounts to a domestic interference operation through the DOJ voter data aggregation initiative — 27 state voter files demanded, a centralized purge database under construction, and two DOGE staffers already referred to an inspector general for matching Social Security data with voter rolls for political advocacy purposes. The framework below covers detection, documentation, legal liability, and coordination architecture — but the 2026 context requires practitioners to keep that inversion clearly in view: the domestic threat now partially wears a federal badge, and the international threat-detection institutions have been deliberately degraded.

---

## Part 1: Detection Methodologies

### 1.1 Network Analysis: Coordinated Inauthentic Behavior

Coordinated inauthentic behavior (CIB) is the use of multiple accounts acting in coordination, without disclosing that coordination, to manipulate public discourse. The core detection signal is behavioral synchrony that would not occur by chance among genuinely independent accounts.

**Primary detection signals (applicable across platforms):**

*Temporal synchrony.* Accounts posting the same or similar content within narrow time windows — minutes or hours — across a large volume of posts. The IRA's 2016 operations were identifiable in part because account posting patterns dropped on weekends and Russian holidays, consistent with a structured work schedule. Bot networks show even tighter temporal clustering, often posting within seconds of a trigger event.

*Content replication.* Identical or near-identical text, images, or hashtag sequences across accounts that have no obvious legitimate reason to share the same content verbatim. This is distinguishable from organic sharing because organic amplification involves visible engagement chains (quote tweets, replies, reshares), while coordinated amplification often involves fresh posts of identical content from disconnected accounts.

*Account provenance patterns.* Mass account creation within a narrow window, purchased follower networks (detectable through sudden follower count spikes on young accounts), and common infrastructure signals (shared IP registration, domain registration patterns, profile image reverse-image matching). The Social Design Agency operation in Poland's 2024 elections was traced in part because approximately 400 accounts linked to the Moscow-funded NGO showed clustered creation dates and overlapping infrastructure.

*Behavioral fingerprints.* For video platforms like TikTok, detection requires adapted methods: synchronized amplification of identical audio tracks, semi-automated content replication using AI-generated voiceovers, and Duet/Stitch patterns that function as coordinated narrative boosters. Research on the 2024 U.S. presidential election found 793,000 TikTok videos related to the election, with a subset showing clear coordination through these video-specific signals.

**Tools and infrastructure:**
- Graphika's network mapping methodology (used in Election Integrity Partnership 2020 report)
- DFRLab's URL Similarity Networks and Text Similarity Networks methodology
- CrowdTangle API (note: Meta has degraded access; archive what you can before further restriction)
- Botometer (Indiana University) for Twitter/X account scoring
- OSoMe (Observatory on Social Media) tools for network visualization

### 1.2 State-Sponsored Disinformation: Signature Characteristics by Actor

Each state actor runs recognizable operational patterns. These signatures are not perfectly reliable — actors update tradecraft — but they remain the primary starting point for attribution analysis.

**Russia (IRA and successor operations):**
The IRA, funded through the Concord Management structure and linked to the GRU after 2016, has the most sophisticated understanding of American domestic politics of any foreign actor. Signature characteristics: amplification of existing domestic divisions rather than injection of purely foreign narratives; investment in building audience credibility over time before pivoting to influence operations ("follower fishing" followed by "narrative switching"); targeting of swing-state audiences with platform-specific content; use of sock puppet networks that pose as authentic American community voices (Black American, evangelical, gun rights, immigration restrictionist personas); coordination with RT and Sputnik narrative themes; posting patterns consistent with structured work schedules in Moscow time zones. The 2024 cycle saw Russia pay a Tennessee media company nine million euros to produce pro-Russian content — a shift toward using genuinely American-facing companies as proxies rather than purely synthetic accounts.

**China (Spamouflage and related):**
China's operations are more focused on specific policy outcomes (Taiwan, trade, critics in Congress) than on broad social division. Signature characteristics: targeting of specific down-ballot candidates who are Beijing critics; use of hacked or purchased dormant accounts (higher credibility than freshly created accounts); the Spamouflage campaign, which uses accounts posing as American citizens to spread anti-Western sentiment with low engagement patterns that suggest artificial amplification; content themes centering on undermining U.S. democratic credibility globally rather than influencing specific votes. China's operations in Taiwan's 2024 election showed an evolution toward more decentralized, less traceable approaches — individual domestic proxies amplifying Beijing-aligned narratives rather than easily-attributed state media accounts.

**Iran (Storm-2035 and related):**
Iran's 2024 operations were characterized by fake news site networks posing as American news outlets catering to both left and right audiences, a tactic designed to launder credibility through fake domestic sources before amplifying polarizing content. Storm-2035 created sites that published content on hot-button issues (immigration, Gaza, abortion) tailored to each audience segment. Iranian operations also targeted the Harris campaign directly with a hack-and-leak operation. Signature characteristics: bilingual (English and Spanish) content; heavy use of Gaza-related narratives as a wedge issue; shorter operational timelines than Russian operations (less investment in long-term audience building); willingness to engage in direct cyber intrusion alongside information operations.

### 1.3 Deepfake Detection: Technical and Forensic Approaches

Deepfakes require layered detection because no single method is fully reliable as the technology improves.

**Tier 1 — Visual and audio forensics.** Frame-level analysis for unnatural blinking, facial movement boundaries, and lighting inconsistencies (synthetic faces often have lighting that does not match the ambient environment). Audio deepfakes — which were the dominant format in the 2024 election cycle, including a fake Biden robocall urging Democrats not to vote in the New Hampshire primary — show compression artifacts distinct from genuine recordings, and waveform analysis can reveal synthesis signatures. The FakeCatcher algorithm (Intel) analyzes photoplethysmographic signals — the subtle color changes in skin pixels caused by blood flow — and returns results in milliseconds with reported 96% accuracy on trained datasets.

**Tier 2 — Metadata forensics.** Authentic media carries creation metadata (device signatures, GPS data where applicable, timestamp consistency) that is typically absent or inconsistent in generated media. The C2PA (Coalition for Content Provenance and Authenticity) standard creates cryptographically signed Content Credentials attached to media files that establish provenance — who created it, with what tool, when, and whether it has been modified. The Carter Center piloted C2PA credentials in election observation missions in 2024. The limitation: most social media platforms strip metadata on upload, and only LinkedIn and TikTok preserved C2PA credentials in limited deployment. This is a critical gap for 2026.

**Tier 3 — Cross-reference and provenance tracing.** Before-and-after search: does the claimed event have any corroborating evidence from independent sources? Does the audio or visual match any known authentic recording the deepfake may have been trained on? Reverse image and audio search can identify source material used in synthesis. This is where journalistic verification skills overlap directly with forensic methods.

**Practical threshold for practitioners:** Deepfakes are not primarily a technical challenge for local movement organizations — they are an institutional challenge. The detection infrastructure requires tools and trained personnel. The practical role for election protection organizations is: (a) flag suspicious content quickly to organizations with detection capacity (DFRLab, First Draft, Graphika); (b) do not republish; (c) document the original distribution context before platforms remove it.

### 1.4 Cross-Platform Amplification Tracing

Election disinformation does not respect platform boundaries. The Springfield, Ohio, Haitian immigrants rumor in 2024 followed a documented cross-platform trajectory: local Facebook groups > far-right networks on Gab and Telegram > X/Twitter amplification > debate stage. Research frameworks have now demonstrated that narratives on fringe platforms (Telegram, Gab) predict mainstream amplification on X/Twitter within days, with prediction accuracy exceeding 94% AUC in trained models.

**Tracing methodology:**

1. *Origin identification.* Where did the narrative first appear? Fringe platform monitoring (Telegram channels, Gab, Truth Social) using keyword and entity tracking catches narratives before they reach mainstream platforms. The DFRLab and Graphika both maintain monitoring infrastructure for this purpose.

2. *Amplification pathway mapping.* Track the same narrative as it moves across platforms by searching for identical or near-identical claim language (not just hashtags, which change as narratives migrate). URL Similarity Networks can identify when the same URLs are being shared across platforms by disconnected account clusters — a signature of coordinated cross-platform amplification.

3. *Platform-specific documentation.* Each platform requires different capture methods because content is removed or modified. For Telegram: channel archival tools before channels are deleted. For Twitter/X: real-time archival because post deletion is fast. For TikTok: screen recording plus metadata capture because TikTok's API access for researchers is severely restricted.

4. *Timing correlation.* Cross-platform operations often show a "seed and amplify" pattern: content seeded on lower-scrutiny platforms first (Telegram, Gab), then selectively amplified to higher-visibility platforms once an organic-looking amplification chain is established.

---

## Part 2: Documentation Standards for Evidence Preservation

### 2.1 Core Evidentiary Standards

Digital evidence is admissible in court when it satisfies four conditions under the Federal Rules of Evidence (Rules 901 and 902) and ISO/IEC 27037:

1. **Authenticated origin** — the file can be linked to a verified source with a timestamp
2. **Proven integrity** — no alteration occurred after capture
3. **Documented chain of custody** — every access event is logged (who touched it, when, from where)
4. **Compliance with applicable legal frameworks** — collection method must not violate the Fourth Amendment, Computer Fraud and Abuse Act, or applicable wiretapping statutes

For election interference documentation, practitioners should apply evidentiary standards from the outset, even if litigation is not yet contemplated. Evidence gathered without chain-of-custody documentation loses much of its value if legal proceedings later become relevant.

### 2.2 Social Media Archival Protocol

The fundamental problem: platforms remove content, and removal is often fastest precisely when content is most consequential (coordinated takedowns during breaking events, platform moderation of flagged interference content).

**Capture protocol for each piece of social media evidence:**

- *Screenshot with full browser context:* Include the URL bar, timestamp visible in the browser, and the platform's own timestamp on the post. Use a browser extension that date-stamps the screenshot (e.g., GoFullPage with timestamp overlay).
- *Full URL capture:* Record the exact URL including post ID. For tweets/posts, this is the permanent link to the individual post, not just the account page.
- *Account metadata snapshot:* Capture the account's profile page at time of documentation — follower count, account creation date, bio, and any available engagement metrics. This contextualizes the post's reach and the account's history.
- *HTML/JSON source:* For higher-stakes documentation, use browser developer tools to save the raw HTML or, where API access exists, the JSON response. This preserves metadata that screenshots cannot capture.
- *Video and audio downloads:* Use tools like yt-dlp for video preservation before platform removal. Archive to local storage with creation timestamp.
- *Wayback Machine submission:* Submit URLs to archive.org/save for independent third-party archival with its own timestamp. This provides an independent verification of content at a specific time.

**Chain of custody log format (minimum):**

```
Item ID | Content Type | Source URL | Capture Timestamp (UTC) | Captured By | 
Storage Location | Hash (SHA-256) | Subsequent Access Events
```

The SHA-256 hash of the captured file establishes that the file has not been modified since capture. Generate the hash immediately upon capture and record it in the log. Any subsequent access that produces the same hash proves the file is unmodified.

### 2.3 Cryptographic Verification

For the highest-stakes evidence (documented foreign interference operations, documented domestic interference by federal actors), cryptographic timestamping provides an additional layer of authenticity verification that goes beyond organizational chain of custody.

**Trusted Timestamping (RFC 3161):** A recognized timestamping authority issues a cryptographic token linked to the hash of your document, proving it existed in its current form at the stamped time. Free RFC 3161 services are available; the DFRLab and several academic institutions offer this as part of their investigator tool kits. The timestamp is verifiable by any third party with the RFC 3161 token and is not dependent on the original archiving organization's credibility.

**Content Credentials (C2PA standard):** For media you create as part of documentation (photographs of physical evidence, video of in-person events related to interference), use C2PA-compliant tools at capture to embed cryptographically signed provenance. The Adobe Content Authenticity Initiative provides free tools for this.

### 2.4 Institutional Archive Models

The Stanford Internet Observatory (now closed, but its archive methodology survives in successor institutions), Graphika, and the DFRLab have established the institutional standard for election interference documentation:

- **Systematic collection before events:** Building baseline datasets of accounts, narratives, and network structure before an election, so that post-election analysis can identify what changed. This is the key lesson from the 2016 analysis failures — the IRA data existed in real time but was not systematically archived.
- **Platform-coordinated takedown data:** When platforms conduct coordinated inauthentic behavior takedowns (as Twitter/X, Meta, and YouTube have done since 2018), they release datasets of removed accounts. These datasets are the most valuable primary sources for CIB research. The DFRLab has archived and analyzed hundreds of these takedown datasets. Access them at: dfrlab.org/research and the Stanford Internet Observatory's GitHub repository (archived materials remain public).
- **Freedom House Election Vulnerability Index:** Freedom House's Election Watch for the Digital Age methodology uses three categories — digital sphere, electoral system, and human rights — to produce pre-election assessments. Their finding that 88% of examined elections showed digital interference provides the baseline for U.S. expectations in 2026.

---

## Part 3: Legal Liability Frameworks

### 3.1 Defamation Risks When Accusing Specific Actors

Publicly naming a specific person or organization as an election interference actor creates defamation exposure unless the accusation is either (a) true, (b) protected as opinion based on disclosed facts, or (c) made by a government official in an official capacity.

**Practical standard for public accusation:**

Before publicly naming an actor, the documentation should support:
1. A specific, documented action (not inference about intent)
2. Attribution that is more than circumstantial (ideally corroborated by independent investigation or official government findings)
3. Clear framing as investigative finding rather than verified fact, unless you have reached a verified-fact threshold

The Georgia election officials case is instructive in the positive direction: systematic false accusations of election fraud by identified actors created $148 million in defamation damages. Dominion Voting Systems' litigation against Powell, Giuliani, and Fox News established that reckless disregard for truth in election fraud accusations is actionable. Both cases establish that false election-related accusations carry real legal consequences — but also that the legal standard applies symmetrically to accusations against interference actors.

**Safe harbor framing:** "DFRLab analysis documents that accounts exhibiting these behavioral characteristics amplified this narrative" is very different from "Russian intelligence is responsible for this influence operation." The former is a documented finding; the latter is an attribution conclusion that requires intelligence-level evidence to support.

### 3.2 Election Law Standing for Legal Challenges

The 2024 Supreme Court decision in *Trump v. Anderson* significantly narrowed Section 3 enforcement standing, holding that states cannot enforce Section 3 against federal officeholders and that congressional action under Section 5 is the required mechanism. This creates a structural gap for the most aggressive use of documented interference evidence in litigation.

**What documentation can directly support:**

- **52 U.S.C. § 30121 (Foreign Contributions):** Evidence of a foreign national providing "anything of value" to a campaign — including opposition research, polling data, or strategic consulting — is directly actionable. The "anything of value" standard is broad and has been interpreted to include information with tactical value. Documented evidence meeting this standard can support DOJ referrals, FEC complaints, or private civil actions where standing can be established.

- **18 U.S.C. § 241 (Conspiracy Against Rights):** Evidence of coordinated voter intimidation, voter suppression, or interference with the right to vote supports criminal referrals to the FBI and DOJ. Given that the FBI has dissolved its Foreign Influence Task Force and the DOJ is itself a source of documented domestic interference vectors (see Part 5), the practical enforcement pathway for these referrals in 2026 runs through state attorneys general and the remaining Career DOJ election crimes staff, not political appointees.

- **18 U.S.C. § 594 (Voter Intimidation):** Direct threats or intimidation directed at voters or election workers. Documentation standards are the same as above.

- **Computer Fraud and Abuse Act (18 U.S.C. § 1030):** Unauthorized access to election infrastructure (voter registration databases, voting machine networks) carries federal penalties. State-level versions of the CFAA provide additional jurisdiction.

- **State election interference statutes:** Approximately 30 states have their own election interference statutes that cover conduct not captured by federal law. State AG offices are the primary enforcement venue when federal enforcement is compromised.

### 3.3 International Legal Frameworks

The OSCE's Office for Democratic Institutions and Human Rights (ODIHR) published its final report on the 2024 U.S. elections in April 2025, containing 31 recommendations for alignment with OSCE democratic commitments. ODIHR election observation reports create a public international record of election conduct, including interference patterns observed by international monitors.

**UN Electoral Assistance Division:** Provides technical assistance to member states on election security and documentation standards. For U.S. purposes, the most relevant function is the international normative framework: the UN General Assembly's Declaration on Criteria for Free and Fair Elections (1994) establishes baseline standards that can be referenced in advocacy and litigation contexts, though they are not directly enforceable in U.S. courts.

**Council of Europe Venice Commission:** Has developed standards on election observation and interference documentation that are relevant as persuasive authority in U.S. courts and directly applicable in OSCE member state contexts.

---

## Part 4: Institutional Coordination Architecture

### 4.1 The Pre-2025 Model (Now Degraded)

Understanding what has been lost requires understanding what existed. The federal election security coordination architecture through 2024 included:

- **CISA Election Infrastructure ISAC (EI-ISAC):** Real-time threat sharing between federal and state/local election officials — 1,300 physical security assessments, 700 cybersecurity assessments, and 500 training sessions since 2023. Terminated.
- **FBI Foreign Influence Task Force:** Coordinated foreign interference threat intelligence with state and local law enforcement. Dissolved.
- **ODNI Foreign Malign Influence Center:** Tracked cross-agency intelligence on foreign interference. Being downsized and "refocused."
- **Multi-State ISAC (MS-ISAC):** State-level threat sharing, previously federally funded. Now forced into paid membership model, creating capability gaps in lower-resource states.

What replaced these institutions is, in the words of state officials, "a patchwork of informal phone calls, email lists, and association meetings."

### 4.2 Estonia's Model: Distributed Resilience

Estonia's election security architecture is the most relevant international model for a decentralized, adversary-hardened approach. Key elements:

**Information System Authority (RIA):** Coordinates development and administration of state information systems and handles security incident response. Functions as an independent technical agency with clear statutory authority, not subject to political interference through the election cycle.

**Estonian Defence League Cyber Unit:** A volunteer militia with cybersecurity expertise, deployable for election infrastructure defense. This hybrid civil-military model creates surge capacity without requiring permanent staffing.

**i-Voting security model:** Estonia has used online voting since 2005. The security architecture assumes a compromised internet and builds in multiple verification layers: national ID card cryptographic signatures, independent audit systems, and public verifiability of the cryptographic process. The key lesson is not that i-voting is inherently secure — it is that security-by-design from the ground up, with independent auditing, is achievable.

**Critical distinction for U.S. application:** Estonia's model works partly because it is a unitary state with centralized election administration. U.S. decentralization (approximately 8,000 county election jurisdictions) is simultaneously a security strength (no single point of failure) and a coordination weakness (no mechanism for rapid national threat response).

### 4.3 Taiwan's 2024 Election Defense: Civil Society Coordination

Taiwan's defense against China's 2024 interference campaign is the most recent and complete case study of successful multi-sector coordination.

**Government layer:** The Anti-Infiltration Act (2020) criminalized acting as an agent of a "hostile foreign force" in elections, with the Supreme Prosecutors Office reporting 117 cases involving 287 individuals investigated under the Act by January 2024.

**Platform layer:** Government-platform collaboration with Meta, Google, LINE, X, and TikTok for monitoring and coordinated content action. The collaboration was established in 2019 and deepened for 2024 — giving it five years of institutional relationship-building before the election. This lead time is important: similar collaboration for 2026 U.S. midterms should be in active development now.

**Civil society layer:** Fact-checking organizations including Taiwan FactCheck Center deployed chatbots for real-time verification of suspicious viral content. "Prebunking" — preemptive public education about expected disinformation tactics before they are deployed — proved more effective than reactive debunking.

**Media layer:** Local media institutions, with institutional trust built over decades, were the most effective vector for rapid correction of disinformation. This points to the importance of local news infrastructure as election security infrastructure.

**Result:** Taiwan's election proceeded despite documented PRC interference, including AI-generated audio deepfakes targeting candidates. The coordination architecture held.

### 4.4 U.S. Residual Institutional Actors

With federal coordination degraded, the operational architecture for 2026 runs through:

**State Secretaries of State offices:** The primary state-level election security authority. NASS (National Association of Secretaries of State) wrote to DHS Secretary Kristi Noem in February 2026 warning that CISA's changes "could endanger future elections." NASS has become the primary national coordination mechanism by default.

**State National Guard cyber units:** High-capacity states (California, Texas, New York) have National Guard cyber units that can provide election security support. Low-capacity states (Wyoming, Vermont, New Mexico) have minimal surge capacity. This is the primary 2026 equity gap.

**CISA residual (Career staff):** Career staff at CISA retain technical expertise even as political leadership has been replaced. The relationship between career staff and election officials is damaged but not fully severed.

**FBI Cyber Division field offices:** The Foreign Influence Task Force is dissolved, but FBI Cyber Division field offices retain election infrastructure jurisdiction. Reporting pathway: Election Crime Coordinators via FBI field offices, or cyber incidents to CISA at report@cisa.dhs.gov.

**Election Assistance Commission (EAC):** Provides voluntary voting system guidelines (VVSG 2.0) and grant coordination. Under institutional capture pressure (Domain 37), but career staff functions continue.

**NGO coordination infrastructure:**
- **Democracy Docket** (Marc Elias): Litigation tracking and strategic election law coordination. Primary platform for tracking 2026 election law challenges.
- **Common Cause / Election Protection Coalition:** Deploys thousands of poll monitors, staffs the 866-OUR-VOTE hotline, and monitors social media for disinformation. Currently litigating against Trump's DOJ voter data aggregation initiative.
- **Protect Democracy:** Strategic litigation and documentation. Currently litigating the DOJ national voter database initiative.
- **Brennan Center for Justice:** Research and litigation on election security and voting rights. Published "How the Federal Government Is Undermining Election Security" (2026) — essential reading for the 2026 context.

---

## Part 5: U.S. Applicability Analysis — 2026 Midterm Frame

### 5.1 The Domestic-Foreign Inversion

The 2026 election interference landscape requires distinguishing three categories that prior frameworks treated as two:

1. **Foreign interference** (Russia, China, Iran, others): Adversary states using disinformation, cyber operations, and covert influence to manipulate U.S. elections without U.S. governmental participation

2. **Domestic interference by non-governmental actors**: Private actors using disinformation, voter suppression, voter intimidation, or fraud — historically the primary focus of election protection litigation

3. **Domestic interference by federal actors**: Executive branch agencies using their official powers to manipulate election outcomes — the new category that emerged clearly in 2025-2026

Category 3 is the most legally complex and the most operationally significant for 2026. The documented mechanisms include:
- DOJ national voter database aggregation with 81%+ error rates in documented state testing (Missouri SAVE data), targeted toward purging eligible voters
- Executive Order 14,399 directing DHS to compile citizenship verification lists from data systems not designed for that purpose
- DOGE staff referrals for Hatch Act violations in matching Social Security data with voter rolls for political advocacy
- CISA dismantlement that creates a detection gap specifically for foreign interference — the destruction of the detection capacity is itself an interference mechanism

### 5.2 Section 3 Post-Trump v. Anderson Landscape

*Trump v. Anderson* (2024) established that Section 3 of the 14th Amendment cannot be enforced against federal officeholders by state action; enforcement requires Congress. This limits the direct litigation pathway using documented interference as grounds for disqualification. However, documented interference evidence remains relevant to:

- **Congressional proceedings:** Documentation supporting challenges to seating of elected officials under the House Contestation mechanism (FCEA, 3 U.S.C. § 17) — covered in Domain 37a
- **Criminal referrals:** Building the evidentiary record for future prosecution of documented interference actors under 18 U.S.C. § 241, § 594, and 52 U.S.C. § 30121
- **Congressional certification challenges:** The certification process runs on a tight timeline (January 6, 2027 for 2026 midterms); documented interference establishes the grounds for specific objections that must be disposed of procedurally

### 5.3 Actionable Vectors vs. Reform-Dependent Vectors

**Currently actionable through existing law:**

- Foreign national contributions (52 U.S.C. § 30121): Strong statute with broad "anything of value" scope; limited only by enforcement will at DOJ
- Voter intimidation (18 U.S.C. § 594): Direct threats documented through witnesses and digital evidence; enforcement pathway through state AGs and remaining career DOJ staff
- CFAA violations against election infrastructure: Documented cyberattacks on voting systems, registration databases; enforcement through FBI Cyber Division
- Defamation by documented false election fraud accusers: Precedent established by Georgia officials, Dominion cases
- Wrongful voter purge challenges: Well-developed litigation doctrine; Common Cause and Protect Democracy cases in active development for 2026

**Requiring statutory reform to be fully actionable:**

- FISA Section 702 without warrant requirement: Post-April 30, 2026 reauthorization (outcome unknown as of this writing) — mass surveillance of election organizers remains lawful if reauthorized without warrant protections (see surveillance-tracking.md)
- National voter database without legal authority: Current legal challenges focus on Executive Order authority rather than a specific prohibitory statute; a clear statutory prohibition would close the loophole
- AI deepfake disclosure in elections: No federal statute requires disclosure that political advertising uses AI-generated content; approximately 20 states have enacted such laws; federal standard needed
- Platform liability reform: Section 230 provides platforms near-complete immunity for hosting interference content; reform is contested and unlikely before 2026

### 5.4 Detection and Response Timeline: 2026 Midterm Calendar

**Now through June 2026 — Pre-election interference window:**
Detection focus: Foreign state actor operation seeding (operations begin 6-12 months before election day); domestic voter roll challenge filing patterns; disinformation infrastructure building. Documentation priority: Archive baseline social media account networks and narrative landscapes now, so post-election analysis has a comparison point.

**July-September 2026 — Primary and run-off period:**
Detection focus: Amplified coordinated inauthentic behavior targeting competitive primaries; voter suppression messaging targeting likely Democratic turnout demographics; deepfake deployment targeting specific candidates. Documentation priority: Real-time evidence capture with cryptographic timestamping. Legal response: Emergency TRO applications for documented voter suppression operations.

**October 2026 — Final push:**
Detection focus: "October surprise" hack-and-leak operations (Iran's 2024 model); last-minute disinformation about voting procedures (polling location changes, date confusion). This is the period with the shortest correction window — prebunking in September is the most effective countermeasure. Documentation priority: Preserve everything; deletion rates spike in this period as actors cover tracks.

**November 2026 — Election day and count:**
Detection focus: Real-time voter intimidation documentation; anomalous voting system incidents; social media false reporting of results before official counts. Response infrastructure: Election Protection Coalition 866-OUR-VOTE hotline; legal rapid-response teams deployed to competitive jurisdictions; litigation teams on standby for emergency injunctions.

**Post-election — Certification window (November-January 2027):**
Documentation focus: Build the complete evidentiary record for any certification challenge, congressional contestation, or criminal referral. The January 6, 2027 certification date is the hard deadline for any proceeding under the FCEA contestation mechanism.

---

## Integration Note: Phase 2 Domain 37 Post-Distribution

This framework is designed for deployment to election-protection organizations in the Phase 2 Domain 37 distribution sequence (Week 6-8 post-Phase A launch, per DOMAIN_37_SEQUENCING_PLAN.md). When transmitting to election-protection practitioners:

1. **Lead with Part 5** (U.S. Applicability) for organizations focused on 2026 advocacy
2. **Lead with Part 2** (Documentation Standards) for organizations building evidence preservation capacity
3. **Lead with Part 1** (Detection Methodologies) for research-oriented partners (DFRLab contacts, university election security programs)
4. The domestic-foreign inversion finding in Part 5.1 is the most novel analytical contribution — it reframes the threat landscape in a way that organizations working from prior-cycle playbooks may not have internalized

**Coordination targets for this framework:**
- Democracy Docket (litigation coordination)
- Common Cause / Election Protection Coalition (field documentation)
- Brennan Center (policy and advocacy)
- State secretaries of state offices in competitive states (AZ, GA, MI, PA, WI — per Domain 37b vulnerability matrix)
- University election security programs (supply trained researchers for detection work)

---

*Sources: Stanford Internet Observatory / Election Integrity Partnership archive; Atlantic Council DFRLab research and Digital Sherlocks methodology; Freedom House Election Watch for the Digital Age; OSCE/ODIHR 2024 USA Final Report; Brookings analysis of Taiwan 2024 election defense; Center for American Progress Taiwan election analysis; Foreign Policy deepfake and election interference analysis; Recorded Future 2024 Deepfake and Election Disinformation Report; DFRLab Poland 2024 analysis; CEPA Serbia elections analysis; Nextgov/FCW CISA drawdown reporting; Votebeat CISA trust reporting; Brennan Center "How the Federal Government Is Undermining Election Security"; CDT "Countdown to the Midterms"; Democracy Docket DOJ election machinery analysis; Brennan Center voter data reporting; Protect Democracy DOJ voter database analysis; ACLU voter data litigation; Popular.info SAVE database analysis; Congress.gov CRS overview of federal election interference statutes; ACM Web Conference 2025 CIB cross-platform study; arXiv coordinated inauthentic behavior survey (2408.01257); USC Viterbi 2024 information operation research; C2PA Coalition content credentials documentation; Electoral Integrity Project C2PA pilot report; MDPI blockchain deepfake verification study; The Conversation IRA/China/Iran comparative analysis; NBC News AI election interference reporting; Heinrich Böll Stiftung Hungary 2026 analysis; France 24 Hungary Orbán disinformation reporting; ISD Global Western Balkans monitoring report; USIP Taiwan democratic resilience analysis; GIJN Taiwan disinformation lessons; HKS Misinformation Review Taiwan 2024; Cyber Defense Review GenAI in Taiwan election.*
