# Flock Safety & License Plate Reader Surveillance
## Research Domain: Mass Surveillance Infrastructure, Civil Liberties, and Resistance Pathways

**Last updated:** 2026-07-04
**Status:** Active research — Houston/Harris County focus
**Priority:** High — direct ICE/immigration enforcement nexus; abortion surveillance documented; civic resistance active

---

## Executive Summary

Flock Safety has built the largest private automated license plate reader (ALPR) network in the United States — 100,000+ cameras as of June 2026, deployed across more than 6,000 communities in 49 states, generating over 20 billion vehicle scans per month. The company has admitted to running undisclosed pilot programs granting U.S. Customs and Border Protection direct access to the network. Audit logs obtained by EFF and journalists document: ICE-related queries across the network, use of the system to track a Texas woman who obtained an abortion across state lines, and surveillance of protest activity by 50+ agencies. Texas has virtually no state-level ALPR regulation. Houston has a $6.4M contract for 318 city cameras and access to the national network; Harris County renewed its own contract in May 2026 over resident objections. The legal landscape is shifting — the Supreme Court's June 2026 Chatrie ruling on geofence warrants creates new Fourth Amendment arguments, and the Institute for Justice appeal of the Norfolk ruling is pending. The resistance toolkit is well-developed: TPIA request templates, model ordinance language, and a national organizing infrastructure exist and are actionable today.

---

## 1. What Flock Safety Is: The Network, the Technology, and Who Controls It

### Corporate Structure and Scale

Flock Group Inc. (operating as Flock Safety) was founded in Atlanta in 2017 by CEO Garrett Langley and co-founders Matt Feury (CTO) and Paige Todd, following Langley's personal experience as a crime victim in a DeKalb County neighborhood where legacy plate readers were too expensive for widespread deployment.[^1] The company went through Y Combinator and grew explosively through the pandemic years.

As of June 2026, Flock has crossed **100,000 cameras** deployed across more than 6,000 communities in 49 states. The company processes **over 20 billion vehicle scans per month** and claims involvement in 10% of all successful U.S. crime investigations.[^2][^3] The network is the largest privately operated ALPR infrastructure in the country.

Flock's financial position is significant to understanding its political power:
- Total funding: approximately $950 million across eight rounds from 28 investors
- Key investors: Andreessen Horowitz (lead Series F), Founders Fund, Kleiner Perkins, Tiger Global, Y Combinator, Matrix Partners, Bedrock Capital, Meritech Capital, Greenoaks Capital, Sands Capital[^4]
- Series F (March 2025): $275 million, valuing the company at **$7.5 billion** (some sources report $8.4 billion by April 2026)[^5]
- 2024 annual recurring revenue: $300 million, a 70% year-over-year increase
- Anticipated IPO: 2026–2027, based on funding structure designed as "runway to liquidity"[^6]

The company employs over 900 people and has made two critical acquisitions: **Aerodome** (October 2024, drone manufacturer for law enforcement) and **Lucidus** (February 2025, Nashville AI startup), which Flock rebuilt into a platform called **Nova**.[^7]

### How the Network Works

Flock's hardware consists primarily of the **Sparrow** and **Falcon Flex** cameras — solar-powered, pole-mounted units that connect to Flock's central servers via LTE cellular network. Each camera runs a modified version of Android and processes captured images using computer vision at capture speeds of up to 100 mph.[^8]

The system does not merely read license plate numbers. It generates a **"vehicle fingerprint"** comprising:
- License plate number and state
- Vehicle make, model, color, and body style
- Bumper stickers, roof racks, visible damage
- Trailer hitches, missing plates, paper plates

This fingerprinting capability means Flock can track a vehicle even if its plate is obscured or missing. Officers can search the resulting database using **FreeForm**, a natural language AI query system — entering queries such as "blue pickup truck with a kayak in the bed" and receiving matching footage from across the network.[^9]

Data uploads via cellular network to Flock's cloud servers, where it is logged with timestamp and GPS coordinates and compared against the National Crime Information Center (NCIC) and agency watchlists ("Hot Lists"). A Hot List entry flags any captured plate matching a vehicle of interest; officers receive an alert in real time.

### Data Retention and Access Architecture

Flock's **default data retention period is 30 days** — data is "hard deleted" on a rolling basis. This can be increased or decreased on a per-customer basis if required by local law or policy. Hot List entries expire after 30 days unless renewed.[^10]

Access tiers:
- **Local users**: authorized officers within the contracting agency, with role-based permissions
- **National Lookup / Statewide Lookup**: a feature embedded in most Flock contracts allowing any participating law enforcement agency to query data from any other participating agency's cameras. This feature was enabled by default in many contracts, or activated without local government knowledge. Over 75% of police departments using Flock opted into national data sharing.[^11]
- **Flock employees**: access only in tightly controlled, audited circumstances; employees require CJIS training and background checks

The national lookup feature is the most consequential aspect of the architecture for civil liberties purposes. It means that a camera in a Houston HOA can be queried by a sheriff's office in Georgia, a Border Patrol agent through a local intermediary, or a federal agency conducting immigration enforcement.

### The Nova Platform: From Plate Readers to Comprehensive Surveillance

In February 2025, Flock acquired Lucidus and rebuilt it into **Nova**, which it describes as "the most expansive AI and data analysis toolset for law enforcement." Nova combines:
- Flock ALPR data
- Computer-Aided Dispatch (CAD) records
- Records Management System (RMS) data
- Open-source intelligence
- Public records including **property and occupancy data, Social Security numbers, and personal credit bureau histories**

All of this is made granularly searchable by AI.[^12] The ACLU's Senior Policy Analyst Jay Stanley called Nova "an end run around privacy laws and the Constitution."[^13] After reporting by 404 Media, Flock backed away from including data breach records in Nova — but retained all other data sources.

### The Raven System: Audio Surveillance

Flock's **Raven** device, launched in 2021, adds acoustic surveillance to the ALPR network. Raven records audio in 5-second increments and uses AI to identify gunfire, alerting police with location estimates. In October 2025, Flock announced Raven would expand to detect **"human distress"** including screaming. After EFF exposed this capability, Flock amended its marketing to remove the explicit reference to screaming — but continued development and deployment.[^14] The company also announced an **Amazon Ring partnership** in October 2025, allowing Ring camera owners to voluntarily share video to the Flock network.[^15]

### Federal Data Sharing: The Documented Record

Flock's official position is that it has no contract with ICE. The reality is more complex:

1. **CBP/HSI pilot programs**: Flock admitted to 9News Denver that it ran an undisclosed pilot program with U.S. Customs and Border Protection, granting direct access to cameras in multiple states. In Colorado, Border Patrol obtained an account, signed an MOU with Flock, and then requested access from local agencies — 25 Colorado departments agreed. An Illinois state audit triggered by the abortion-tracking case confirmed Flock had granted CBP access to Illinois cameras without adequate safeguards or disclosure.[^16][^17]

2. **Indirect ICE access**: Even where direct access was halted, ICE officials requested that state and local law enforcement search Flock cameras on their behalf. More than 4,000 lookups were documented as conducted at the behest of federal immigration agencies.[^18]

3. **Dayton audit**: Data from Dayton's cameras was searched more than 7,100 times for immigration enforcement purposes — explicitly prohibited under the city's policy.[^19]

4. **Mountain View unauthorized access**: Over 12 months ending December 2025, more than 250 agencies that had never signed a data-sharing agreement with Mountain View conducted an estimated 600,000 unauthorized searches of the city's plate data.[^20]

5. **San Francisco**: The Northern California Regional Intelligence Center queried San Francisco's Flock network on behalf of federal and out-of-state agencies — 299 improper inquiries over approximately one year. A February 2026 class action alleges ICE, CBP, FBI, and ATF queried SF cameras more than 1.6 million times in seven months.[^21]

In January 2026, Flock introduced a toggle in Admin Settings allowing agencies to disable all Federal Sharing. Critics note this puts the burden on local governments to discover and activate a previously hidden control.

---

## 2. Federal Legal Landscape: Fourth Amendment Case Law on ALPR

### The Controlling Precedent: Carpenter v. United States (2018)

*Carpenter v. United States*, 585 U.S. 296 (2018), is the lodestar for ALPR Fourth Amendment analysis. The Supreme Court held 5-4 that accessing seven days or more of historical cell-site location information (CSLI) requires a warrant under the Fourth Amendment, reasoning that CSLI creates an "all-encompassing" log of a person's movements — roughly 101 data points per day — that cannot be characterized as information voluntarily shared under the third-party doctrine.

Chief Justice Roberts' majority explicitly cabined the holding: it did not "call into question conventional surveillance techniques and tools, such as security cameras." This carve-out is the basis for law enforcement arguments that ALPR data requires no warrant. The court also noted the "seismic shifts in digital technology" that alter the relationship between privacy and data aggregation.

The central legal question post-*Carpenter* is: at what scale of ALPR deployment does the "seismic shift" reasoning apply?

### The Institute for Justice Norfolk Litigation (2024–Present)

The most significant constitutional challenge to Flock was filed in October 2024 by Norfolk residents Lee Schmidt and Crystal Arrington, represented by the **Institute for Justice**, challenging the constitutionality of Norfolk's 176 Flock cameras.[^22]

Key procedural history:
- **February 2025**: Chief Judge Mark Davis (E.D. Va.) **denied the motion to dismiss**, citing *Carpenter* and holding that "a reasonable person could believe that society's expectations, as laid out by the Court in *Carpenter*, are being violated by the Norfolk Flock system." This was a significant early victory — the case was allowed to proceed to discovery and trial.[^23]
- Flock Safety attempted to intervene as a party; Judge Davis rejected the attempt as "untimely" and said it would "throw this case off the rails."[^24]
- **January 27, 2026**: Judge Davis ruled that Norfolk's network **does not violate the Fourth Amendment**, finding the 176 cameras (75 clusters, 21-day rolling retention) insufficiently pervasive to trigger *Carpenter* protections. The opinion expressly warned that expanding the network could change the calculus.[^25]
- **Appeal**: IJ announced plans to appeal to the Fourth Circuit Court of Appeals. The ACLU filed an amicus brief in the Fourth Circuit in April 2026 arguing that ALPR systems give the government "unprecedented powers of surveillance that upset traditional expectations of privacy."[^26]

### The Chatrie Geofence Ruling: New Fourth Amendment Ground (June 2026)

On June 29, 2026, the Supreme Court decided *United States v. Chatrie*, 6-3, holding that **geofence warrants require probable cause** under the Fourth Amendment. The case involved police pulling Google location data from every device near a Virginia bank during a 2019 robbery. The Court held that this kind of bulk retrospective location sweep, without individualized probable cause, is unconstitutional.

Legal analysts immediately flagged the direct application to Flock: **bulk ALPR queries work the same backward-sweep logic** — logging every vehicle at a location over time regardless of whether the owner is suspected of anything, then searching that stored data retroactively. The Chatrie reasoning, if applied, would require individualized probable cause before police run location-based ALPR queries. As of this writing (July 2026), no court has yet applied Chatrie to an ALPR case, but the IJ Fourth Circuit appeal is now positioned to be the leading vehicle for that argument.[^27]

### The Commonwealth v. Church State Case (Virginia)

In *Commonwealth v. Church*, a Norfolk police officer searched Flock ALPR data without a warrant — not to place the defendant at a crime scene, but to establish "guilty mind." The circuit court suppressed the ALPR evidence as an unconstitutional warrantless search. The **Virginia Court of Appeals reversed in October 2025**, holding no warrant was required. EFF and the ACLU of Virginia filed a brief urging the Court of Appeals to require warrants; they lost. This case remains significant because it shows a state appellate court split from the circuit court's privacy-protective ruling.[^28]

### The San Jose ALPR Lawsuit (November 2025)

The EFF and ACLU jointly filed suit in November 2025 challenging San Jose's warrantless ALPR mass surveillance under the **California Constitution** — which has an explicit right to privacy stronger than the federal Fourth Amendment. The plaintiffs include the Services, Immigrant Rights and Education Network (SIREN) and CAIR-California. This case, filed in California state court, could establish that California's state constitutional right to privacy requires warrants for ALPR database access — a ruling that would be binding on all California agencies.[^29]

### The California Class Action (April 2026)

Gibbs Mura filed an amended class action complaint in April 2026 alleging Flock used its ALPR cameras to track millions of Californians and illegally share information with out-of-state law enforcement agencies, violating California privacy laws.[^30]

### Court Landscape Summary

As of July 2026, courts have **uniformly rejected** constitutional challenges to ALPR systems as currently deployed — two federal circuit courts, twenty federal district courts, and four state appellate courts have upheld ALPR constitutionality. The central legal theory — that limited camera networks are not pervasive enough to trigger *Carpenter* — remains the prevailing rule. The IJ Fourth Circuit appeal, armed with the *Chatrie* precedent, is the most promising vehicle to change this. The San Jose California case is the strongest immediate threat to Flock's model because California's right to privacy is textually explicit.[^31]

**Texas legal note**: The Texas Constitution, Article I, Section 9 mirrors the federal Fourth Amendment but does not contain an explicit privacy provision stronger than federal law. Texas courts follow federal Fourth Amendment jurisprudence closely. A state constitutional challenge in Texas faces the same uphill battle as the federal cases.

---

## 3. State-by-State Law: The Regulatory Patchwork

### States With ALPR Statutes (NCSL as of 2025)

As of late 2025, **16 states** have enacted ALPR-specific statutes[^32]:

| State | Key Provisions |
|-------|---------------|
| **New Hampshire** | Strictest: data deleted within **3 minutes** unless linked to arrest/citation; government use restricted to law enforcement |
| **Maine** | Restricts to public safety purposes; max **21-day** retention; data confidential |
| **Montana** | Prohibits ALPR on public highways with limited exceptions; max **90-day** retention |
| **Vermont** | Requires operator certification; access limited to law enforcement; independent audits |
| **Utah** | Specified government uses only; warrant required for private data access |
| **Minnesota** | Classifies ALPR data; requires written access procedures; mandates public use logs |
| **California** | CHP: 60-day retention (felony cases excepted); prohibits sale to non-law enforcement |
| **Colorado** | Requires destruction of passive surveillance images within 3 years |
| **Maryland** | Requires access procedures, training, and audits |
| **North Carolina** | Written policies required; max **90-day** retention; data confidential |
| **Tennessee** | Max **90-day** retention unless ongoing investigation; data confidential |
| **Nebraska** | Requires written policies; annual reporting |
| **Arkansas** | Bans individual/private use; law enforcement exemptions; max 150-day retention |
| **Georgia** | Collection/access for law enforcement only; max 30 months unless toll violation |
| **Florida** | Public records exemption; data confidential; criminal justice agencies only |
| **Oklahoma** | Limited to insurance law enforcement; other uses prohibited |

### 2025–2026 Legislative Wave

Three states passed new ALPR laws in 2025. **Oregon** enacted rules requiring 30-day data retention and mandating compliance with the state's sanctuary laws — effectively prohibiting data sharing with immigration enforcement. **Washington** passed SB 6002 (Driver Privacy Act) in early 2026: bans ICE from accessing plate data, limits retention to 21 days, prohibits cameras near schools and churches, and makes violations a gross misdemeanor; the attorney general must develop model policies by July 2027.[^33][^34] Conservative-led states — **Arkansas, Idaho, and Montana** — also enacted data protection measures in 2025, joining blue states in bipartisan concern about surveillance overreach.[^35]

At least 10 states, including Texas, introduced ALPR legislation in 2025 that **did not advance**.

### Texas: Virtually No State Regulation

Texas has **no meaningful state-level ALPR regulation**. Key facts:

- **No statewide retention mandate**: Agencies set their own policies. Some departments store LPR data for up to 191 days; others less.
- **No data sharing prohibition**: Texas law does not restrict sharing ALPR data with federal agencies, including ICE.
- **No warrant requirement**: Texas courts follow federal precedent, which does not require warrants.
- **Texas DPS regulation**: Flock was found to be operating cameras at private homes and HOAs **without a required private security license** from 2019 to 2024. Texas DPS sent a cease-and-desist letter in 2024 and assessed a **$500 fine** — the statutory maximum for first-time offenders. Flock subsequently obtained the required certification. The cease-and-desist did not affect law enforcement or government-operated cameras.[^36][^37]
- **Texas DPS expansion**: The Texas Department of Public Safety has been expanding its own ALPR program, drawing privacy concerns from advocates. Texas law enforcement agencies conducted at least **180 ALPR searches related to immigration enforcement** from January to May 2025.[^38]
- **Legislative failure**: Bills filed to regulate police ALPR use in Texas did not gain traction in the 2025 session.
- **The abortion precedent**: A Texas DPS investigation into the use of Illinois ALPR data to track a woman who received abortion care — by a Texas sheriff using Washington State's camera network — triggered the Illinois state audit that confirmed Flock's CBP pilot. The tool is actively being used in Texas for reproductive surveillance.

### States That Have Banned or Substantially Restricted LPR Use

The most protective states for ALPR-related privacy:
- **New Hampshire**: Three-minute deletion model is the most protective in the nation; effectively makes long-term ALPR surveillance impossible
- **Maine**: 21-day cap and public safety purpose limitation
- **Montana**: Prohibition on public highway use, with exceptions
- **Oregon**: 30-day cap + sanctuary law compliance requirement (prohibits ICE data sharing)
- **Washington**: 21-day cap + explicit ICE prohibition + school/church buffer zones (2026)

---

## 4. Houston Specifically: Contracts, Oversight, and Community Resistance

### Houston Police Department (HPD)

The Houston City Council **unanimously approved** a five-year contract with Flock Safety for 318 cameras at a total cost of **$6.4 million** — voted on in fall 2025 (the Public Safety Committee reviewed the proposal on October 14, 2025).[^39] The cameras are described as deployed "in neighborhoods across town and on city properties." Specific locations are not publicly disclosed.

The new HPD cameras augment an existing network. Through the national lookup feature, **HPD officers can access approximately 88,000 cameras from agencies nationwide**. HPD Assistant Chief Martin confirmed that police departments in Katy, Sugar Land, Pearland, and other Houston-area cities share camera data with HPD.[^40]

The Houston Chronicle and Texas Standard conducted a joint investigation into HPD's use of the Flock database, analyzing approximately **500,000 searches**. Key findings[^41][^42]:
- Many officers do not enter a purpose for their searches, or enter meaningless text such as "ASDF," "donut," or undetailed "investigation"
- The system is being used "like a search engine" rather than a formal law enforcement tool
- HPD's governing policy on surveillance technology dates to 2015 — before Flock existed — and does not require documented justification for individual searches
- No regulation mandates that officers explain their searches on paper
- HPD has not published evidence that the cameras reduce crime

The Flock CEO responded to scrutiny by announcing a new "drop-down menu" of reasons that officers would be required to select before searching. This is a cosmetic fix: drop-down options are not verified against the actual investigation, and "investigation" or "suspect" with no further detail remains permissible.

**No local ordinance** in Houston restricts ALPR use, requires oversight, limits data sharing, or mandates audit disclosure. The City Council's April 2026 immigration ordinance (limiting when HPD can call ICE, passed 13-4 after amendment) does not address Flock camera data sharing.[^43]

### Harris County

The Harris County Commissioners Court **renewed the county's Flock contract** on May 28, 2026, through June 5, 2027, at a cost of **$868,975**, approved on a **4-0 vote** with County Judge Lina Hidalgo abstaining.[^44]

Key facts from the renewal proceeding:
- Many county cameras are not tax-funded but financed by **homeowners associations and Municipal Utility Districts (MUDs)**, with the Sheriff's Office administering them
- The County Attorney's Office, Sheriff's Office, and purchasing department tightened data privacy language in the renewed contract
- Commissioner Adrian Garcia championed renewal, citing stolen vehicle recovery and crime-solving successes
- Judge Hidalgo criticized the process: "If we are really open to accountability, then we would not be trying to ram this through"
- Community members stated: "stop investing in technology that monitors our neighbors" and "there are not and can't be enough guardrails around unauthorized use of electronic surveillance"[^45]

The political split is significant: Hidalgo's abstention signals that the county's progressive wing is not unified behind the contract. This creates an opening for 2027 renewal opposition if organized early.

### The Woodlands and Conroe (Montgomery County)

**The Woodlands Township** approved 30 additional Flock cameras for summer 2026, at $109,500 in the first year and $90,000 annually thereafter. Montgomery County Sheriff's Office briefed the Woodlands Township board on Flock usage in May 2026. One community member argued the deployment "infringes on constitutional rights and should be decided by public vote."[^46]

**Conroe** presents the clearest documented case of **obstruction of public records access** in the Houston area. A resident filed a TPIA request for basic information about Flock cameras (how many, how they work, where the data goes, who can access it). The city charged **$1,200** to process the request. After the community funded the request and paid the city, the city slow-walked release: by May 2026, the resident had received nothing and stated "they were quick to take the money and very slow to provide the documents." The Conroe Police Chief subsequently addressed concerns at a June 11, 2026 council meeting, confirming cameras are not used for facial recognition or traffic enforcement — but this verbal assurance is not a binding policy.[^47]

### The Abortion Surveillance Case: A Texas Origination Story

In May 2025, the **Johnson County Sheriff's Office** (Texas) used Flock's national ALPR network to search for a woman suspected of self-managing an abortion. The search record explicitly stated: "had an abortion, search for female." Officers searched **6,809 different camera networks** across the country — including in abortion-protective states like Washington and Illinois. Newly obtained court records (via EFF) showed that police had opened a "death investigation" into the fetus and consulted the District Attorney about charging the woman with a crime — contradicting the Sheriff's and Flock's public claims that the search was a "missing person" welfare check.[^48]

This case is determinative for how Houston-area advocates should frame the Flock fight: the threat is not hypothetical. A Texas law enforcement agency used the same national lookup network that HPD accesses to conduct reproductive surveillance across state lines. The same infrastructure tracks immigrants. The same infrastructure surveilled protesters.

### Protest Surveillance

EFF analyzed 10 months of Flock audit logs and found that **more than 50 federal, state, and local agencies** conducted hundreds of searches tied to protest activity. Searches were linked to the 50501 protests (February 2026), Hands Off protests (April 2026), No Kings protests (June and October 2026), and Direct Action Everywhere (animal rights group) actions.[^49] Nineteen agencies conducted searches specifically tied to No Kings protests. There is no indication Houston-area agencies are exempt from this pattern.

---

## 5. What Can Be Done: Legal Challenges, Legislative Routes, Organizing, and Countermeasures

### Legal Challenges: Pathways and Standing

**Standing requirements**: To challenge ALPR use in court, plaintiffs must show (1) concrete injury in fact, (2) causation, and (3) redressability. The strongest standing arguments come from:
- Individuals documented to have been subjected to an ALPR search unrelated to a crime (e.g., protesters, immigrants, abortion patients)
- Organizations whose members are regularly tracked (immigrant rights groups, reproductive rights groups, political organizations)
- Individuals who can show their movements were logged across time and location

**Litigation pathways in Texas**:
1. **Fourth Amendment challenge**: Difficult in current climate but the IJ Norfolk appeal + *Chatrie* creates new momentum. A Harris County or Houston plaintiff who can show bulk surveillance of protected activity (political protest, medical care) has the strongest factual posture.
2. **Texas Constitution, Article I, Section 9**: Tracks federal Fourth Amendment closely; modest independent protection, but state courts may be more receptive.
3. **Texas Privacy Act / TPIA enforcement**: If an agency violates its own data sharing policy (as Dayton and San Francisco documented), Texas Government Code remedies and injunctive relief are available.
4. **Breach of contract**: If Flock violated its data sharing commitments to a Texas city (sharing with federal agencies without authorization, as documented in Illinois), the city has contract remedies — and a citizen may have standing to enforce sanctuary protections through declaratory judgment.
5. **Reproductive rights nexus**: Post-*Dobbs*, Texas law criminalizes abortion provision. The Johnson County case shows this infrastructure is live for abortion surveillance. Civil liberties organizations representing abortion providers or patients have a direct injury argument.
6. **First Amendment**: Surveillance of protest activity chills protected speech and assembly. An organizational plaintiff whose members' vehicles were tracked at protests has a concrete First Amendment injury.

**Organizations providing legal support**:
- Institute for Justice (IJ): actively litigating the Norfolk case; contact through ij.org
- Electronic Frontier Foundation: counsel in San Jose case; ALPR research and advocacy at eff.org/cases/automated-license-plate-readers
- ACLU of Texas: policy engagement; aclutx.org; Nick Hudson, policy and advocacy strategist
- ACLU national: has filed amicus briefs; aclu.org/campaigns-initiatives/get-the-flock-out
- Gibbs Mura (class action): California-based, filed amended complaint April 2026; classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit

### Legislative Routes: State and Local

**State level — Texas**:

Bills to regulate ALPR in Texas have repeatedly failed. The 2025 legislative session produced no ALPR-specific law. The 2027 Texas legislative session is the next opportunity. Key model provisions to advocate for:

- **Data retention cap**: 30 days maximum (matching Oregon); 21 days preferred (matching Maine, Washington)
- **ICE data sharing prohibition**: explicit ban on providing ALPR data to immigration enforcement agencies without a warrant, matching Oregon's sanctuary law integration
- **Warrant requirement**: require a judicially authorized warrant before any retrospective location search of ALPR data
- **Mandatory audit logs**: require agencies to log all searches with reason, retain logs for public inspection
- **Private camera registration**: require all HOA and private cameras sharing data with law enforcement to be publicly registered

Use **Washington SB 6002** as the model bill template. It is the most comprehensive recent statute and its provisions are specific and enforceable.[^50]

**Local ordinance — Houston and Harris County**:

Houston City Council can adopt a surveillance ordinance without state authorization. Model provisions:
- **Purpose limitation**: ALPR searches permitted only for active criminal investigations with documented case number
- **Mandatory search justification**: officers must enter a verified case number and crime category before accessing ALPR data
- **Federal agency prohibition**: no sharing of ALPR data with federal immigration agencies without a judicial warrant
- **Audit disclosure**: monthly public release of aggregate search statistics (number of searches, stated purpose categories)
- **Data retention**: reduce to 21 days from Flock's 30-day default
- **Community oversight board**: independent civilian review of ALPR use policies

**Durango, Colorado model** provides the most developed local ordinance template: warrant requirement for data access, 72-hour baseline retention (extendable for active investigations), and a community oversight board.[^51] Seattle's ordinance requires the police department to transmit the ALPR vendor contract to Council and mandates annual reporting.[^52]

**Harris County**: The May 2026 contract renewal runs through June 5, 2027. This provides a defined window to organize before the next renewal. Judge Hidalgo's abstention signals potential for a different outcome in 2027 if advocacy begins now. The goal is not just a "no" vote but a contract with binding data sharing prohibitions and audit requirements.

### Public Records Requests: TPIA Strategy for Houston and Harris County

Texas uses the **Texas Public Information Act (TPIA)**, not FOIA. Agencies must respond within **10 business days** — providing records, seeking an Attorney General opinion, or claiming a statutory exception. The Texas AG's office reviews claimed exceptions and frequently orders disclosure.

**Key note on Flock's data deletion**: Flock deletes ALPR scan data after 30 days. Any TPIA request for scan records must be submitted promptly; records of specific queries may have longer retention. **Request audit logs and access records immediately** — these are more durable than raw scan data.

**Substantive requests to file**:

Flock contracts, MOUs, and data agreements are clearly public under TPIA — they are government contracts. Flock has attempted to claim trade secret exemptions on pricing; fight these at the AG level as the public interest in knowing contract terms outweighs vendor business interests (a Washington state court ruled similarly in November 2025 that Flock camera data are public records).[^53]

**Request categories**:

1. All contracts, licenses, MOUs, data sharing agreements, and scope of work documents between [Agency] and Flock Group Inc. / Flock Safety, including all amendments
2. All audit logs, access logs, or query records showing who accessed the ALPR database, when, and for what stated purpose — for the past 12 months
3. All communications between [Agency] and Flock Safety regarding data sharing with federal agencies including CBP, DHS, ICE, FBI, and ATF
4. All policies governing ALPR data access, retention, and sharing
5. The number and location of all Flock cameras operating under [Agency] contracts or accessible by [Agency] officers
6. All records of complaints or internal reviews related to ALPR data access

**Submission contacts**:

- **HPD**: Houston Police Department Public Information, houstontx.gov/police/public_information.htm; or through the City of Houston GovQA portal at houstontx.gov/pia.html
- **City of Houston (non-HPD)**: GovQA portal at houstontx.gov/pia.html
- **Harris County Clerk**: Mail to Teneshia Hudspeth, Harris County Clerk, PIA Request, P.O. Box 1525, Houston, TX 77251-1525
- **Harris County Sheriff**: Harris County Sheriff's Office, PIA Unit (use HCSO website submission form)
- **Conroe**: City of Conroe, City Secretary's Office (in person or mail to 300 W Davis St, Conroe, TX 77301)

**Cost management**: Request a fee waiver on grounds of public interest. Under TPIA, agencies may reduce or waive fees if disclosure is in the public interest and primarily benefits the general public rather than the requestor. Frame the request as research serving the public's right to know about surveillance infrastructure.

**If records are withheld**: File for AG review within 10 days. The Texas AG has consistently ruled that vendor contracts are public. Cite *City of Garland v. Dallas Morning News* for the principle that vendor pricing in government contracts is public.

**Existing toolkit**: The GitHub repository `rpriven/flock-public-records-toolkit` provides state-specific public records request templates for 20+ states including Texas, with TPIA-specific citation language and expedited processing requests.[^54]

### Community Organizing Tactics

**What has worked elsewhere**:

- **Cambridge, MA**: Two unauthorized Flock cameras installed without city knowledge after a deactivation order — documented through public records requests — gave advocates a "material breach" argument. The city terminated the contract.[^55]
- **Eugene, OR**: Community tipster discovered a reactivated camera after deactivation orders. The tip came from a local organizer who monitored camera locations. Local vigilance plus records requests created the evidentiary record.
- **Oak Park, IL**: Village board voted to cancel because the cameras violated the sanctuary ordinance. The key move: connecting ALPR to the existing sanctuary policy framework, not starting a new fight.
- **Evanston, IL**: Followed Oak Park within three weeks. Peer-city dynamics accelerated cancellation after the first domino fell.

**Tactics**:

1. **Map the cameras**: Use DeFlock (deflock.org / maps.deflock.org) to locate all Flock cameras in your jurisdiction. Photograph and GPS-tag cameras you find; contribute to the OpenStreetMap database. This creates a public record of surveillance infrastructure and reveals discrepancies with official counts.[^56]

2. **File serial TPIA requests**: Start with contracts and audit logs. If the city stonewalls (as Conroe did), publicize the non-response. Consider crowdfunding record fees as a community accountability action; the public attention on the funding/payment creates political pressure.

3. **Connect to the immigration ordinance**: Houston passed an ordinance in April 2026 limiting HPD-ICE cooperation. Flock data sharing with federal agencies is in direct tension with this ordinance. Frame ALPR reform as enforcement of the existing immigration policy.

4. **Appear at Commissioners Court before the 2027 renewal**: The Harris County contract runs through June 5, 2027. Organized public testimony at the renewal hearing creates a record. Judge Hidalgo's abstention shows there is political space. Organize a coalition of immigration, reproductive rights, civil liberties, and community groups to testify.

5. **Use the abortion surveillance story**: The Johnson County case is a Texas origination story that connects Flock surveillance directly to reproductive rights — a live issue in Houston's immigrant and progressive communities.

6. **Engage HOAs and MUDs**: A significant portion of the Houston-area Flock network is financed by HOAs and MUDs. Engage HOA boards directly. Many homeowners are unaware their dues are funding a surveillance network accessible by federal immigration agents. HOA board members can vote to opt out.

### Technical Countermeasures (Legal)

**No general opt-out exists**: There is no mechanism to opt out of being tracked by Flock cameras. Anyone who drives past a camera has their plate logged.

**Flock SafeList**: Flock offers a "SafeList" feature for HOA deployments allowing residents to register their vehicle as a neighborhood resident. This does not prevent data from being captured, queried by law enforcement, or shared with federal agencies. It simply marks images as "resident." It is not a meaningful privacy protection.

**Route planning**: DeFlock Maps (maps.deflock.org) provides **privacy-optimized routing** that treats camera locations as hazards to avoid — analogous to routing around toll plazas. This is a legal way to reduce capture frequency. It is most useful for people with specific, documented reasons to avoid surveillance (journalists, activists, abortion patients, immigrants in removal proceedings).

**Legal plate alternatives**: License plate covers that obstruct cameras are **illegal in Texas** and most other states. Do not recommend or use plate-obscuring devices.

**Camera documentation**: Photographing publicly visible Flock cameras is fully legal. Camera documentation contributes to the DeFlock map and can reveal discrepancies between official camera counts and actual deployments — as occurred in Cambridge, MA, where unauthorized cameras were discovered by community members.[^57]

---

## 6. Actionable Toolkit

### TPIA Request Templates

**Template A — HPD Flock Contract and Audit Logs**

```
TO: Houston Police Department, Office of the Chief of Police, Public Information Unit
Houston, TX 77002
Via: houstontx.gov/police/public_information.htm

DATE: [DATE]

This is a request under the Texas Public Information Act, Texas Government Code Chapter 552.

I request the following records:

1. All contracts, agreements, memoranda of understanding, memoranda of agreement, 
   licenses, data sharing agreements, and amendments between the Houston Police Department 
   (HPD) or the City of Houston and Flock Group Inc. (also known as Flock Safety), 
   from 2015 to present.

2. All policies, procedures, directives, and general orders governing the use of 
   Automated License Plate Reader (ALPR) technology, including Flock Safety cameras, 
   from 2015 to present.

3. All audit logs, query records, or access logs documenting searches of the Flock Safety 
   database by HPD officers, including the date, time, stated purpose, and user identifier 
   (may be redacted to badge number) for each query — for the period [12 months prior to 
   this request].

4. All records of requests by federal agencies — including U.S. Immigration and Customs 
   Enforcement (ICE), U.S. Customs and Border Protection (CBP), the Department of Homeland 
   Security (DHS), the Federal Bureau of Investigation (FBI), and the Bureau of Alcohol, 
   Tobacco, Firearms and Explosives (ATF) — to access, query, or receive data from HPD's 
   ALPR systems, from 2020 to present.

5. All communications (emails, letters, texts, records of meetings) between HPD and 
   Flock Group Inc. regarding data sharing with any federal agency, from 2020 to present.

6. The number and addresses of all Flock Safety cameras currently operating under HPD 
   contracts or accessible by HPD officers.

I request a fee waiver on grounds of public interest. This information is sought to inform 
the public about surveillance infrastructure affecting all Houston residents, and release will 
primarily benefit the general public. 

If any records are withheld, please provide a specific written statement of the legal basis 
for each withholding, as required by Tex. Gov't Code § 552.301.

[Signature / Contact information]
```

**Template B — Harris County Sheriff Flock Contract**

```
TO: Harris County Sheriff's Office, Public Information Unit
Via: [HCSO website submission or mail to 1200 Baker St, Houston, TX 77002]

DATE: [DATE]

This is a request under the Texas Public Information Act, Texas Government Code Chapter 552.

I request the following records concerning Automated License Plate Reader (ALPR) 
technology and Flock Group Inc. (Flock Safety):

1. The current contract and all prior contracts, amendments, and renewals between the 
   Harris County Sheriff's Office and/or Harris County and Flock Group Inc., including 
   the contract renewed on or about May 28, 2026.

2. All data sharing agreements, memoranda of understanding, or other agreements between 
   the Harris County Sheriff's Office and any federal law enforcement agency regarding 
   access to ALPR data, from 2019 to present.

3. All audit logs or query records documenting access to Flock Safety camera data by 
   Harris County Sheriff's Office personnel, for the past 12 months, including stated 
   purpose for each query.

4. The number and street addresses of all Flock Safety cameras operating under agreements 
   with the Harris County Sheriff's Office, including cameras financed by HOAs or MUDs 
   that share data with the Sheriff's Office.

5. Any records reflecting whether Harris County ALPR data has been accessed by or 
   shared with U.S. Immigration and Customs Enforcement, CBP, DHS, FBI, or ATF, 
   from 2019 to present.

I request a fee waiver on public interest grounds. [Signature / Contact information]
```

### Model Ordinance Language (Houston City Council)

Based on the Durango, CO model and Washington SB 6002, the following provisions are recommended for a Houston ALPR Use Ordinance:

**Core provisions**:

> **Sec. [X].1 — Purpose limitation**: HPD officers may access ALPR data only in connection with an active, documented criminal investigation. Each query must be associated with a verified case number and documented offense category.
>
> **Sec. [X].2 — Federal sharing prohibition**: No ALPR data collected by or accessible to HPD shall be shared with, disclosed to, or queried on behalf of any federal immigration enforcement agency, including ICE and CBP, without a judicially authorized warrant.
>
> **Sec. [X].3 — Data retention**: ALPR scan data shall be deleted after 21 days unless specifically preserved in connection with an active criminal case, in which case retention is permissible for the duration of the investigation and associated legal proceedings.
>
> **Sec. [X].4 — Audit and transparency**: HPD shall publish a monthly report disclosing: total number of ALPR queries, breakdown by stated purpose category, number of queries resulting in an arrest, and any federal agency requests for data. Individual query records shall be available by TPIA request.
>
> **Sec. [X].5 — Oversight**: An independent ALPR oversight committee, including civil liberties representatives and community members from impacted neighborhoods, shall review HPD's ALPR program annually and report to City Council.
>
> **Sec. [X].6 — Penalties**: Willful violation of this ordinance by a city employee is a Class A misdemeanor. Affected individuals may bring a civil action for injunctive relief.

### Organizations Working on This Issue — Contact Information

| Organization | Role | Contact |
|---|---|---|
| **ACLU of Texas** | State-level advocacy; surveillance policy | aclutx.org; Nick Hudson, policy/advocacy strategist |
| **ACLU National — Get the Flock Out** | Campaign toolkit, model legislation | aclu.org/campaigns-initiatives/get-the-flock-out; aclu.org/get-the-flock-out-toolkit |
| **Electronic Frontier Foundation (EFF)** | Litigation support, audit log analysis, technical guidance | eff.org/cases/automated-license-plate-readers; ALPR tags at eff.org |
| **Institute for Justice** | Active litigation (Norfolk appeal); Fourth Amendment theory | ij.org; Fourth Circuit case pending |
| **Fight for the Future** | FLOCK Out campaign; activist resources | fightforthefuture.org/actions/flockout/; team@fightforthefuture.org |
| **DeFlock** | Camera mapping; privacy-route navigation | deflock.org; maps.deflock.org; OpenStreetMap-based |
| **Eyes On Flock** | Aggregates Flock transparency portal data | eyesonflock.com |
| **Rural Privacy Coalition** | Flock camera locator; rural context | ruralprivacy.org/find-flock-alprs-in-your-area |
| **Gibbs Mura** | California class action; data sharing claims | classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit |
| **MuckRock** | FOIA/TPIA request facilitation and tracking | muckrock.com (search "Flock Safety" for precedent requests) |

---

## 7. Open Threads and Research Gaps

- **HPD camera locations**: The city has not published a map of the 318 new cameras. A TPIA request for camera addresses is the fastest way to get this; follow up on submission.
- **Flock-Ring partnership in Houston**: The October 2025 Amazon Ring partnership may be creating additional camera coverage in Houston neighborhoods. Track whether HPD is accessing Ring data through Flock's integration.
- **Nova platform in Texas**: No reporting yet documents whether Texas agencies are using Flock Nova's Social Security and credit bureau search capabilities. This warrants a direct TPIA request for Nova-related contracts.
- **Raven audio deployment in Harris County**: The Harris County contract renewal (approx. $868,975) covers "license plate reader and sound detection technology" — confirming Raven audio sensors are included. The scope of audio capture is not publicly documented.
- **MUD/HOA camera inventory**: Major MUDs in Harris County (Barker Cypress, Katy, Friendswood) may have separate Flock contracts not covered by the county contract. Research and TPIA requests to individual MUDs warranted.
- **IJ Fourth Circuit appeal**: Monitor for briefing schedule and argument dates. The *Chatrie* ruling will likely be a centerpiece of IJ's brief. An amicus opportunity exists for Texas civil liberties organizations.
- **2027 Harris County contract renewal**: Calendar June 5, 2027 as the critical date. Begin organizing testimony by Q1 2027.

---

## Source Notes

[^1]: [Flock Safety - Wikipedia](https://en.wikipedia.org/wiki/Flock_Safety)
[^2]: [Flock Safety Crosses 100,000 Cameras as 53 Cities Cancel — TechTimes, June 29, 2026](https://www.techtimes.com/articles/319317/20260629/flock-safety-crosses-100000-cameras-53-cities-cancel-over-unauthorized-federal-data-access.htm)
[^3]: [Flock Safety: 2025 CNBC Disruptor 50](https://www.cnbc.com/2025/06/10/flock-safety-cnbc-disruptor-50.html)
[^4]: [Flock Safety Secures $275 Million to Advance Crime-Solving Technology](https://www.flocksafety.com/blog/flock-safety-secures-major-funding)
[^5]: [Flock Safety 2026 Company Profile — PitchBook](https://pitchbook.com/profiles/company/185188-06)
[^6]: [AI Startup Flock Thinks It Can Eliminate All Crime In America — Forbes, September 2025](https://www.forbes.com/sites/thomasbrewster/2025/09/03/ai-startup-flock-thinks-it-can-eliminate-all-crime-in-america/)
[^7]: [Flock Safety Reveals Flock Nova Platform — Yahoo Finance](https://finance.yahoo.com/news/flock-safety-reveals-most-expansive-130000761.html)
[^8]: [Flock Safety: The $7.5 Billion Surveillance Network Tracking Your Car — State of Surveillance](https://stateofsurveillance.org/articles/surveillance/flock-safety-surveillance-network/)
[^9]: [Flock cameras track more than your license plate — Engadget](https://www.engadget.com/2203000/flock-cameras-recording-license-plate/)
[^10]: [Flock Safety Data Privacy & Retention Policies](https://www.flocksafety.com/trust/data-privacy)
[^11]: [Flock Gives Law Enforcement All Over the Country Access to Your Location — ACLU of Massachusetts](https://data.aclum.org/2025/10/07/flock-gives-law-enforcement-all-over-the-country-access-to-your-location/)
[^12]: [Flock Safety reveals the most expansive AI toolset — Police1](https://www.police1.com/police-products/police-technology/publicsafetysoftware/flock-safety-reveals-the-most-expansive-ai-and-data-analysis-toolset-for-law-enforcement-including-flock-nova-a-new-platform-to-transform-investigations)
[^13]: [Flock's AI Cameras Are Watching Cars. They're About to Get a Lot More Powerful — Forbes, June 2025](https://www.forbes.com/sites/thomasbrewster/2025/06/04/flocks-ai-cameras-are-watching-cars-all-over-america-theyre-about-to-get-a-lot-more-powerful/)
[^14]: [Flock's Gunshot Detection Microphones Will Start Listening for Human Voices — EFF, October 2025](https://www.eff.org/deeplinks/2025/10/flocks-gunshot-detection-microphones-will-start-listening-human-voices)
[^15]: [Flock Safety - Wikipedia](https://en.wikipedia.org/wiki/Flock_Safety)
[^16]: [Flock admits federal immigration agents have direct access to tracking data — 9News](https://www.9news.com/article/news/local/flock-federal-immigration-agents-access-tracking-data/73-a8aee742-56d4-4a57-b5bb-0373286dfef8)
[^17]: [Flock Safety halts federal pilot programs with Homeland Security agencies — KEZI](https://www.kezi.com/news/local/flock-safety-halts-federal-pilot-programs-with-homeland-security-agencies/article_5e3709e2-d9f9-49e8-b885-23f6cdb8ca6f.html)
[^18]: [Reported: ICE using ALPR cameras via state/local police — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-ice-accessing-flock-automated-license-plate-reader-cameras-via-local-law-enforcement/)
[^19]: [Flock Safety Crosses 100,000 Cameras — TechTimes, June 29, 2026](https://www.techtimes.com/articles/319317/20260629/flock-safety-crosses-100000-cameras-53-cities-cancel-over-unauthorized-federal-data-access.htm)
[^20]: [Flock Can Share Driver-Surveillance Data Even When Police Departments Opt Out — ACLU](https://www.aclu.org/news/privacy-technology/flock-massachusetts-and-updates)
[^21]: [California drivers accuse Flock Safety of sharing data with federal agencies — Courthouse News](https://courthousenews.com/california-drivers-accuse-flock-safety-of-sharing-data-with-federal-and-out-of-state-agencies/)
[^22]: [New lawsuit challenges whether Flock cameras in Norfolk are constitutional — WTKR](https://www.wtkr.com/news/in-the-community/norfolk/new-lawsuit-challenges-whether-flock-cameras-in-norfolk-are-constitutional)
[^23]: [Judge Rules Lawsuit Challenging Norfolk's Use of Flock Cameras Can Proceed — Institute for Justice](https://ij.org/press-release/judge-rules-lawsuit-challenging-norfolks-use-of-flock-cameras-can-proceed/)
[^24]: [Federal Court Rejects Flock Safety's Late Bid to Join IJ's Lawsuit — Institute for Justice](https://ij.org/press-release/federal-court-rejects-flock-safetys-late-bid-to-join-and-block-ijs-lawsuit-challenging-norfolks-mass-surveillance-cameras/)
[^25]: [Judge holds Norfolk's license plate reader use constitutional — Courthouse News, 2026](https://courthousenews.com/judge-holds-norfolks-license-plate-reader-use-constitutional/)
[^26]: [As Abuses Mount Nationwide, Administration Calls on Court to Reject Lawsuit — IJ](https://ij.org/press-release/as-abuses-mount-nationwide-federal-government-calls-on-court-to-reject-lawsuit-challenging-constitutionality-of-license-plate-readers/)
[^27]: [SCOTUS Geofence Ruling Challenges Flock Safety ALPR Data in 2026 — Utica Phoenix](https://uticaphoenix.net/scotus-geofence-ruling-challenges-flock-safetys-alpr-data-practices-in-july-2026/)
[^28]: [EFF Urges Virginia Court of Appeals to Require Search Warrants to Access ALPR Databases — EFF, September 2025](https://www.eff.org/deeplinks/2025/09/eff-urges-virgina-court-appeals-require-search-warrants-access-alpr-databases)
[^29]: [Lawsuit Challenges San Jose's Warrantless ALPR Mass Surveillance — EFF, November 2025](https://www.eff.org/press/releases/lawsuit-challenges-san-joses-warrantless-alpr-mass-surveillance)
[^30]: [California drivers accuse Flock Safety of sharing data — Courthouse News](https://courthousenews.com/california-drivers-accuse-flock-safety-of-sharing-data-with-federal-and-out-of-state-agencies/)
[^31]: [Vehicle Fingerprinting Through Pervasive Camera Surveillance Likely Violates Fourth Amendment — EPIC](https://epic.org/vehicle-fingerprinting-through-pervasive-camera-surveillance-likely-violates-fourth-amendment-court-finds/)
[^32]: [Automated License Plate Readers: State Statutes — NCSL](https://www.ncsl.org/technology-and-communication/automated-license-plate-readers-state-statutes)
[^33]: [This New Oregon Law Regulates Use of License Plate Readers — GovTech](https://www.govtech.com/policy/this-new-oregon-law-regulates-use-of-license-plate-readers)
[^34]: [Bill introduced to regulate Flock automatic license plate reader cameras — Washington Senate Democrats](https://senatedemocrats.wa.gov/blog/2026/01/06/bill-introduced-to-regulate-flock-automatic-license-plate-reader-cameras/)
[^35]: [Worried about surveillance, states enact privacy laws and restrict license plate readers — Stateline, January 2026](https://stateline.org/2026/01/08/worried-about-surveillance-states-enact-privacy-laws-and-restrict-license-plate-readers/)
[^36]: [Texas DPS sends cease and desist to Flock Safety — Fox 26 Houston](https://www.fox26.com/news/texas-dps-send-cease-desist-flock-safety-camera-private-homes-businesess)
[^37]: [Exclusive: Texas DPS finds Flock surveillance violated state law — Yahoo News](https://www.yahoo.com/news/articles/exclusive-texas-dps-finds-flock-223019946.html)
[^38]: [License to scan: Plate readers found across Texas are mostly unregulated — KVUE](https://www.kvue.com/article/news/investigations/defenders/texas-license-plate-readers-widely-unregulated/269-d32a0ea0-edb6-4ce4-a25b-61c135c581a6)
[^39]: [More than 300 new automatic license plate reader cameras are coming to Houston — KHOU](https://www.khou.com/article/news/local/automatic-license-plate-reader-cameras-houston-texas/285-7632b4af-7156-4457-87f8-77510b748680)
[^40]: [Houston's ALPRs Help Solve Crimes, but Not Everyone Is a Fan — GovTech](https://www.govtech.com/public-safety/houstons-alprs-help-solve-crimes-but-not-everyone-is-a-fan)
[^41]: [Probe finds Houston police using surveillance tool, meant to deter crime, like a search engine — Texas Standard](https://texasstandard.org/stories/flock-safety-cameras-houston-police-texas-investigation-crime-use/)
[^42]: [Flock CEO Responds to Scrutiny of Houston Police's Surveillance Tech Use — GovTech Insider](https://insider.govtech.com/texas/news/flock-ceo-responds-to-scrutiny-of-houston-polices-surveillance-tech-use)
[^43]: [Houston City Council passes ordinance limiting when HPD can call ICE — Click2Houston](https://www.click2houston.com/news/local/2026/04/08/houston-city-council-to-vote-on-immigration-ordinance-defining-hpd-ice-roles/)
[^44]: [Harris County Renews Flock Camera Contract — My Neighborhood News](https://myneighborhoodnews.com/harris-county-renews-flock-camera-contract-after-lengthy-debate-over-privacy-and-public-safety)
[^45]: ['Y'all are playing games': Harris County's Flock camera contract renewal turns tense — Click2Houston, May 2026](https://www.click2houston.com/news/local/2026/05/29/%27y%27all-are-playing-games%27:-discussion-over-harris-county%27s-flock-camera-contract-renewal-turns-tense/)
[^46]: [The Woodlands Approves Installation of 30 New Flock Cameras — Conroe News](https://www.conroenews.org/article/the-woodlands-approves-expansion-of-flock-safety-system-amid-privacy-concerns)
[^47]: [Conroe residents say city is stonewalling their requests for information on Flock Safety cameras — ABC13 Houston](https://abc13.com/post/conroe-residents-say-city-is-stonewalling-requests-information-flock-safety-cameras/18953584/)
[^48]: [Flock Safety and Texas Sheriff Claimed License Plate Search Was for a Missing Person. It Was an Abortion Investigation. — EFF, October 2025](https://www.eff.org/deeplinks/2025/10/flock-safety-and-texas-sheriff-claimed-license-plate-search-was-missing-person-it)
[^49]: [How Cops Are Using Flock Safety's ALPR Network to Surveil Protesters and Activists — EFF, November 2025](https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists)
[^50]: [Washington Driver Privacy Act Could Ban Flock Data Sharing With ICE — State of Surveillance](https://stateofsurveillance.org/news/washington-sb6002-driver-privacy-act-alpr-flock-2026/)
[^51]: [New Proposed Ordinance Aims to Regulate ALPR Technology in Durango — ACLU of Colorado](https://www.aclu-co.org/press-releases/new-proposed-ordinance-aims-to-regulate-automated-license-plate-reader-alpr-technology-in-durango/)
[^52]: [City of Seattle ALPR Ordinance](https://clerk.seattle.gov/~archives/Ordinances/Ord_127044.pdf)
[^53]: [Washington Court Rules That Data Captured on Flock Safety Cameras Are Public Records — EFF, November 2025](https://www.eff.org/deeplinks/2025/11/washington-court-rules-data-captured-flock-safety-cameras-are-public-records)
[^54]: [GitHub — flock-public-records-toolkit (rpriven)](https://github.com/rpriven/flock-public-records-toolkit)
[^55]: [Cambridge ends contract for license plate cameras after 'breach of trust' — Boston.com, December 2025](https://www.boston.com/news/local-news/2025/12/11/cambridge-ends-contract-for-license-plate-cameras-after-breach-of-trust/)
[^56]: [DeFlock Maps | ALPR Camera Map & Privacy Routes](https://maps.deflock.org/)
[^57]: [DeFlock: How One Guy Mapped 90,000 Cameras and Sparked a Revolt — State of Surveillance](https://stateofsurveillance.org/news/deflock-flock-safety-revolt-90000-cameras-cities-cancel-2026/)

**Additional sources consulted**:
- [Flock's Aggressive Expansions Go Far Beyond Simple Driver Surveillance — ACLU](https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/flock-roundup)
- [Why some cities are canceling Flock license plate reader contracts — NPR, February 2026](https://www.npr.org/2026/02/17/nx-s1-5612825/flock-contracts-canceled-immigration-survillance-concerns)
- [Flock Safety Credibility Lost as it Repeatedly Lies to City Councils — ACLU](https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/flock-safety-credibility-lost-as-it-repeatedly-lies-to-city-councils-police-departments-and-public-across-the-country)
- [How to Fight Deployment of Flock and Other Mass Surveillance License Plate Readers — ACLU](https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/how-to-fight-deployment-of-flock-and-other-mass-surveillance-license-plate-readers-in-your-community)
- [Get The Flock Out Campaign — ACLU](https://www.aclu.org/campaigns-initiatives/get-the-flock-out)
- [Fight Creepy ALPR Cameras — ACLU](https://www.aclu.org/campaigns-initiatives/get-the-flock-out)
- [After Oak Park cut ties, state says Flock Safety broke the law — Wednesday Journal, August 2025](https://www.oakpark.com/2025/08/28/state-says-flock-safety-broke-the-law/)
- [Victory! Supreme Court Says Constitution Protects People's Location Data (Chatrie) — EFF](https://www.eff.org/deeplinks/2026/06/victory-supreme-court-says-constitution-protects-peoples-location-data)
- [EFF's Investigations Expose Flock Safety's Surveillance Abuses: 2025 in Review — EFF](https://www.eff.org/deeplinks/2025/12/effs-investigations-expose-flock-safetys-surveillance-abuses-2025-review)
- [She Got an Abortion. So A Texas Cop Used 83,000 Cameras to Track Her Down — EFF, May 2025](https://www.eff.org/deeplinks/2025/05/she-got-abortion-so-texas-cop-used-83000-cameras-track-her-down)
- [Are Your Local Police Using Flock Safety ALPRs to Scan for Immigrants? — EFF, June 2026](https://www.eff.org/deeplinks/2026/06/are-your-local-police-using-flock-safety-alprs-scan-immigrants)
- [Open Records Laws Reveal ALPRs' Sprawling Surveillance — EFF, April 2026](https://www.eff.org/deeplinks/2026/04/open-records-laws-reveal-alprs-sprawling-surveillance-now-states-want-block-what-public-sees)
- [Mass Surveillance in Texas: The Hidden Dangers of License Plate Tracking — Texas Policy Research](https://www.texaspolicyresearch.com/mass-surveillance-in-texas-the-hidden-dangers-of-license-plate-tracking/)
- [As License Plate Readers Expand in Texas, Privacy Advocates Are Fighting Back — Texas Observer](https://www.texasobserver.org/license-plate-readers-texas-privacy-advocates/)
- [Harris County renews contract for law enforcement license plate cameras — Community Impact, May 2026](https://communityimpact.com/houston/spring-klein/government/2026/05/28/harris-county-renews-contract-for-law-enforcement-license-plate-cameras-despite-resident-pushback/)
- [Flock Safety FOIA Data — ALPRWatch](https://alprwatch.org/news/2025-07-28_flock_foia/)
- [Eyes On Flock](https://eyesonflock.com/)
- [FLOCK Out — Fight for the Future](https://www.fightforthefuture.org/actions/flockout/)
- [Surveillance company skirted regulations as it expanded across north Fort Worth HOAs — KERA News, 2024](https://www.keranews.org/government/2024-10-09/surveillance-company-skirted-regulations-as-it-expanded-across-north-fort-worth-hoas)
- [Despite widespread interest, only 3 states passed license plate reader laws this year — Stateline, October 2025](https://stateline.org/2025/10/10/despite-widespread-interest-only-3-states-passed-license-plate-reader-laws-this-year/)
- [Automatic License Plate Recognition Systems: Summary of State Laws — Legislative Analysis, September 2025](https://legislativeanalysis.org/wp-content/uploads/2025/09/Automatic-License-Plate-Recognition-Systems-Summary-of-State-Laws.pdf)
- [Flock Safety and Texas Sheriff: It Was an Abortion Investigation — Techdirt](https://www.techdirt.com/2025/10/17/flock-safety-texas-sheriff-claimed-license-plate-search-was-for-a-missing-person-it-was-an-abortion-investigation/)
- [Flock Safety & Texas Sheriff Claimed License Plate Search Was For A Missing Person — Krishnamoorthi House letter, August 2025](https://krishnamoorthi.house.gov/sites/evo-subsites/krishnamoorthi.house.gov/files/evo-media-document/2025-08-06.garcia-krishnamoorthi-to-flock-re-lpr-tech-and-tracking.pdf)
- [Under Surveillance: Constitutional Concerns Surrounding Flock Cameras — NC Journal of Law & Technology](https://journals.law.unc.edu/ncjolt/blogs/under-surveillance-constitutional-concerns-surrounding-flock-cameras/)
- [Flock's data sharing policy — Does Flock Share Data With ICE?](https://www.flocksafety.com/blog/does-flock-share-data-with-ice)
- [A federal judge ruled Norfolk's Flock surveillance cameras don't invade people's privacy – yet — WHRO, February 2026](https://www.whro.org/business-growth/2026-02-11/a-federal-judge-ruled-norfolks-flock-surveillance-cameras-dont-invade-peoples-privacy-yet)
- [The Nationwide Revolt Against Flock Safety Cameras — The New Republic](https://newrepublic.com/article/206992/flock-safety-cameras-alpr-deflock-resistance-nationwide)
- [We're Fighting Mass Surveillance Tech—and Winning — EFF, June 2026](https://www.eff.org/deeplinks/2026/06/get-flock-out-here)
