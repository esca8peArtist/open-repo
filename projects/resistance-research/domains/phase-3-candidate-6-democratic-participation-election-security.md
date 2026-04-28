# Phase 3 Candidate 6: Democratic Participation & Election Security
## Institutional Mechanisms for Simultaneously Secure and Participatory Elections

**Research completed**: April 28, 2026
**Status**: Phase 3 Exploration — Production-ready for institutional distribution
**Priority designation**: Phase 3 Expansion — Feeds Phase 1 distribution to election administrators, civil society organizations, policy influencers, law schools
**Cross-domain connections**: Domain 1 (Voting Rights and Elections), Domain 37 (Federal Executive Interference — 2026 Midterms), Domain 37b (State Election Security Coordination), Domain 6 (Judicial Independence), Domain 29 (DOJ Capture), Domain 35 (Supreme Court / Post-*Loper Bright* landscape), Domain 33 (State Legislative Autocratization), Domain 26 (Government Accountability and Institutional Resilience)

---

## Executive Summary

The central design challenge in democratic election reform is an apparent trilemma: election systems can be made more secure, more participatory, or more decentralized — but conventional wisdom treats these as tradeoffs. A system with rigorous identity verification is harder to fraudulently exploit but excludes eligible voters who lack required documents. Centralized administration can enforce consistent standards but creates a single point of partisan capture. Digital systems improve convenience but expand the attack surface for interference. Reform efforts that ignore the trilemma end up solving for one dimension at the expense of the others.

The international evidence, pilot program data, and US state-level experiments surveyed in this report resolve the trilemma on its empirical terms. The trilemma is a false constraint produced by treating security and participation as zero-sum. Paper ballot systems with rigorous post-election auditing are demonstrably more secure than paperless electronic systems AND are more accessible because they require no technical literacy. Automatic voter registration increases both the size of the electorate and the accuracy of voter rolls. Distributed administration combined with national coordination infrastructure is more robust against partisan capture than either fully centralized or fully atomized systems. Risk-limiting audits produce mathematically provable outcome verification at lower cost than the full hand counts that skeptics demand. These mechanisms do not trade participation for security — they reinforce each other.

The north star finding of this report: the optimal election system design combines (1) hand-marked paper ballots with optical scan tabulation, verified by (2) risk-limiting audits with publicly disclosed random seed generation, administered by (3) independent election management bodies insulated from partisan appointment, with voter access maximized through (4) automatic voter registration integrated with agency databases and (5) small-donor public financing that reduces the entry barrier for candidates representing low-income constituencies. Each mechanism is implementable within the US constitutional framework. Several are operating at the state level today. The reform pathway is policy, not constitutional amendment — with three exceptions discussed in Section 6.

The United States in 2025-2026 is experiencing a particularly acute version of the election security trilemma: a federal executive using the language of "election security" to systematically suppress participation (the SAVE Act, the March 2025 elections executive order, DOJ voter roll litigation), while simultaneously dismantling the actual technical security infrastructure (CISA defunding, EI-ISAC elimination, reduced HAVA funding from a pandemic-era high of $825 million to $15 million in FY2025). Understanding the difference between security theater — measures that impose participation costs while providing no genuine protection against actual threats — and authentic election security architecture is the organizing analytical task of this report.

---

## 1. Current Election Infrastructure Vulnerabilities

### 1.1 The Post-2020 Partisan Capture Crisis

The 2020 election produced a novel form of democratic threat that existing legal frameworks were not designed to handle: officials within the election administration system refusing, or threatening to refuse, to certify election results as a partisan intervention strategy. This was not election fraud in the traditional sense of vote manipulation; it was a downstream attack on the certification chain after the votes were correctly counted.

The mechanism worked as follows. Local canvassing boards and county-level election commissions in several states discovered that individual members could create significant disruption by threatening to withhold their signatures from certification documents, or by demanding extraordinary review periods that would delay or prevent certification within statutory deadlines. In Georgia, at least 19 election board members across nine counties objected to certifying elections during the 2020-2024 period. In Michigan, Republican canvassers explicitly stated they would not certify a 2024 election result they believed to be fraudulent — a circularity problem, since the canvasser's subjective belief about the legitimacy of the count has no statutory basis for certification refusal. Michigan's Proposal 2 (2022) — a constitutional-level voting access expansion approved by 60 percent of voters — partially addressed this by embedding certain certification timelines and requirements in the state constitution, which removed them from ordinary legislative modification.

Georgia's State Election Board became the most active laboratory for certification manipulation tactics in 2024. The board adopted two rules in advance of the November 2024 presidential election: one requiring election officials to certify only after "reasonable inquiry" (undefined), and another giving county election boards expanded authority to investigate elections if vote totals appeared anomalous. Democrats, joined by the Georgia Democratic Party, filed suit challenging both rules. The litigation established a critical legal record: courts found that the new rules violated Georgia's existing certification requirements, which are ministerial — meaning election officials have no discretion to withhold certification if the statutory count is correct.

CREW (Citizens for Responsibility and Ethics in Washington) identified 35 election officials across the country who had already refused to certify elections and were in a position to do so again heading into 2024. This is not a small-scale threat. It represents a systematic strategy, documented in litigation, of treating the certification step — which has historically been treated as ministerial — as a discretionary partisan intervention point.

The legal significance extends beyond individual cases. Courts have consistently held that certification is ministerial: once the count is correctly completed, certification must follow. The case law produced in 2020-2024 builds a record that future litigants can invoke against certification refusers. But the legal remedy (mandamus) requires filing, briefing, argument, and judicial action on an emergency basis at the most time-pressured moment in the electoral cycle — typically the days between Election Day and the state's certification deadline. The infrastructure to pursue mandamus relief at scale needs to be pre-positioned, not assembled after the fact.

Sources: [Just Security: Election Certification Refusers Are a Movement](https://www.justsecurity.org/100005/election-certification-refusers/); [Votebeat: Georgia election rule changes raise concerns about certification fights](https://www.votebeat.org/2024/10/10/presidential-election-certification-delays-trump-republicans-disputes-georgia-board-rule/); [Protect Democracy: Election certification, explained](https://protectdemocracy.org/work/election-certification-explained/); [Brookings: The counties that may try not to certify the 2024 election](https://www.brookings.edu/articles/the-counties-that-may-try-not-to-certify-the-2024-election/)

### 1.2 The March 2025 Executive Order and EAC Capture Attempt

On March 25, 2025, President Trump issued Executive Order 14248, "Preserving and Protecting the Integrity of American Elections," which targeted five areas: the Election Assistance Commission (EAC), the national voter registration form, mail ballot administration, state voter roll access by federal agencies, and election security funding conditionality. The order is the clearest single statement of the administration's strategy for using the federal executive apparatus to reshape election administration — and it was blocked in court on constitutional grounds.

The order's most significant provision attempted to require proof of citizenship for voter registration on the federal form, accepting only passports or equivalent documents. Only approximately 50 percent of Americans hold a valid passport; the uninsured rate is much higher among young, low-income, and minority voters. The EAC — an independent bipartisan agency created by HAVA — refused to comply. A federal court permanently blocked the provision, finding that the president has no authority over the EAC, which reports to Congress, not the executive branch. The legal framework is settled: the Elections Clause (Article I, Section 4) assigns election administration authority to states and Congress, not the president. But the attempt demonstrated the administration's theory of executive authority over elections — and the theory will return in different statutory clothing regardless of this specific court loss.

The EAC's institutional independence proved structurally important in a way that is not always understood: unlike many independent agencies, the EAC has explicit bipartisan commission structure, requiring equal numbers of Democratic and Republican commissioners, with no single-party majority. This design makes it harder for a president to achieve functional control through appointment pressure. The FEC became inoperative from May 2025 forward due to a lack of quorum — an administration strategy of declining to nominate commissioners rather than capturing the agency directly. The EAC has thus far resisted equivalent disruption, but its $15-per-state effective budget (the FY2025 HAVA security grant totaling $15 million nationally) means it is operationally limited regardless of its institutional independence.

Sources: [Brennan Center: The President's March 2025 Executive Order on Elections](https://www.brennancenter.org/our-work/research-reports/presidents-executive-order-elections-explained); [Brennan Center: Status of Trump's Anti-Voting Executive Order](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order); [Campaign Legal Center: Victory! Anti-Voter Executive Order Halted in Court](https://campaignlegal.org/update/victory-anti-voter-executive-order-halted-court)

### 1.3 The CISA Dismantlement and the $45 Million Adequacy Problem

The Cybersecurity and Infrastructure Security Agency's election security program was the primary federal technical backstop for state-level election administration. CISA had, since 2018, provided 1,300 physical security assessments, 700 cybersecurity assessments, and 500 training sessions to local election offices. It funded the Election Infrastructure Information Sharing and Analysis Center (EI-ISAC), which was the national incident-coordination network when any state identified a threat to voting systems. The administration cut CISA's budget by $700 million, eliminated EI-ISAC, and terminated the cooperative agreement with the Multi-State ISAC (MS-ISAC).

HAVA election security grants now total $45 million nationally for FY2026 — approximately $900,000 per state — compared with $825 million in FY2020. A coalition of more than 50 civil rights and election protection organizations has asked Congress to restore $825 million in FY2026 funding; the coalition letter has not produced legislative action. The contrast with other infrastructure security investments is instructive: the federal government spends approximately $28 billion annually on nuclear security and $8.5 billion on aviation security. The election security investment at $45 million covers the infrastructure on which all those other investments depend for democratic legitimacy.

Sources: [EAC: Election Security Grant](https://www.eac.gov/grants/election-security-funds); [Issue One: Federal Funding for American Elections](https://issueone.org/articles/federal-funding-for-american-elections-hava-grants/); [Leadership Conference: Coalition Letter Supporting Federal Funding for Election Administration in FY26](https://civilrights.org/resource/coalition-letter-supporting-federal-funding-for-election-administration-in-fy26/)

---

## 2. Voting Systems and Ballot Integrity Mechanisms

### 2.1 The Paper Ballot Consensus and What It Actually Requires

There is a strong professional and academic consensus, supported by NIST, the Verified Voting Foundation, the MIT Election Lab, and the National Academies, that election security requires a voter-verified paper record. The MIT Election Lab's 2024 Survey of the Performance of American Elections found that 74 percent of respondents identified "securing paper ballots" and "logic-and-accuracy testing" as the measures providing the greatest assurance of election integrity — the same percentage as the most trusted measure on the survey. Computerized voting systems without paper records are, by definition, unauditable: there is no independent record to compare against the electronic tally.

The distinction between hand-marked paper ballots (HMPBs) and ballot marking devices (BMDs) is a genuine and underappreciated security debate. BMDs are electronic devices that print a marked ballot, which the voter can then review before submitting. The theoretical security advantage of HMPBs is that the voter's intent is directly expressed in ink, without any intervening software. The theoretical security concern with BMDs is that if the BMD software is compromised, it could print a ballot that differs from the voter's selections in ways the voter might not notice — particularly in down-ballot races where attention drops. The security community (led by the Georgia Tech Election Cybersecurity Initiative and the Verified Voting Foundation) has documented this as a non-theoretical risk: the human verification rate for BMD-printed ballots has been measured at approximately 7 percent in some studies, meaning that a compromised BMD could affect 93 percent of printed ballots without detection.

For high-volume jurisdictions with significant populations of voters with disabilities — for whom BMDs provide essential accessibility — the security-and-access tension is real. The resolution is not to mandate one over the other universally, but to require independent verification. The VVSG 2.0 (approved by the EAC in 2021, the first major revision in 15 years) includes cryptographic protection requirements, risk assessment mandates, and supply chain risk management standards. The 2024 VVSG Review Report found implementation progress but noted that the majority of voting systems deployed in November 2024 were certified under earlier standards; VVSG 2.0-compliant systems will not be universal until after 2026.

### 2.2 Risk-Limiting Audits: The Mathematics of Election Verification

Risk-limiting audits (RLAs) are the most important technical development in election verification of the past two decades. An RLA is a statistical procedure that examines a randomly selected sample of ballots and provides a mathematical guarantee — at a specified confidence level — that the reported outcome is correct. If the reported outcome is wrong, the RLA will detect the error with probability equal to (1 - risk limit). A 5 percent risk limit means a 95 percent probability that a wrong outcome would be detected and corrected; a 3 percent risk limit means a 97 percent probability.

Colorado became the first state to implement RLAs statewide in 2017, following a 2009 legislative mandate. It currently uses a 3 percent risk limit — among the strictest in the nation. The procedure uses a publicly generated random seed (produced by rolling 20 ten-sided dice in a public meeting) to select specific ballots for examination, ensuring that ballot selection cannot be predicted or manipulated in advance. Auditors then compare the paper ballot to the corresponding electronic record, and a comparison audit algorithm determines when sufficient evidence exists to confirm the reported outcome without examining every ballot.

Colorado's implementation has produced several findings relevant to national replication. First, the audit has produced no evidence of systemic tabulation error across eight election cycles. This is not null evidence — it is affirmative evidence that Colorado's optical scan tabulators are operating correctly. Second, the public random seed generation has become a civic accountability mechanism: the dice-rolling ceremony is a public event, which creates a record that the selection process was not manipulated. Third, the cost of compliance has declined as county staff have internalized the process; the initial learning-curve investment in 2017 is no longer a significant operational barrier.

The contrasting cases are instructive. Georgia's 2020 hand recount — not an RLA — examined 100 percent of ballots and confirmed Biden's victory; the political outcome was to generate new attacks on the counting process rather than accept the mathematical result. An RLA with a published risk limit and random seed provides a cleaner evidentiary record for court challenges, because the statistical guarantees are mathematically precise and publicly verifiable. A hand count's result, by contrast, is dependent on the accuracy of the counting teams — an infinite regress that election deniers can exploit. States that implement RLAs before the next contested election are better positioned to defend their results in court and in public.

As of 2026, states with RLA requirements include Colorado, Rhode Island, Virginia, Nevada, Michigan, Pennsylvania (partial), and Georgia (for certain contests). Verified Voting's implementation database documents significant variation in audit type, risk limits, and scope. Fourteen states still use no meaningful post-election audit; eleven use fixed-percentage audits (examining a preset percentage of ballots regardless of margin) rather than RLAs, which provide weaker statistical guarantees.

Sources: [Colorado Secretary of State: Risk-Limiting Audit FAQs](https://www.coloradosos.gov/pubs/elections/RLA/faqs.html); [Colorado Politics: Colorado's election audits are built on math, not politics](http://www.coloradopolitics.com/2026/03/12/colorados-election-audits-are-built-on-math-not-politics-in-response/); [MIT Election Lab: Election Auditing](https://electionlab.mit.edu/research/projects/mapping-election-science/white-papers/election-auditing); [NIST: Security of Ballot Marking](https://www.nist.gov/itl/voting/security-ballot-marking); [Verified Voting: Comments on VVSG 2.0](https://verifiedvoting.org/verified-voting-comments-on-vvsg-2-0-v3/)

### 2.3 Chain of Custody and the Decentralized Administration Tradeoff

The United States has an unusual election administration structure by international standards: responsibility is distributed across approximately 10,000 local and state jurisdictions, nearly all administered by elected officials. This decentralization has a genuine security benefit: there is no single central point that a sophisticated adversary can attack to affect the national election simultaneously. A cybersecurity breach of one county's tabulation system cannot automatically propagate to other counties using different systems, vendors, and network configurations.

But decentralization also creates vulnerabilities. Election officials in rural counties frequently have no dedicated cybersecurity staff; they may be single-person offices managing elections on general-purpose computers. Before CISA's dismantlement, federal technical assistance bridged this capacity gap. Now, the 2,000+ county election offices with fewer than five staff members face a threat environment that national security agencies assess as more sophisticated in 2025-2026 than in 2020, with no equivalent federal backstop.

Chain of custody — the documented, auditable record of ballot handling from the moment of casting through tabulation and storage — is the procedural mechanism that makes decentralized administration compatible with verification. Colorado's RLA framework depends on an intact chain of custody; if a ballot cannot be located, the audit cannot confirm the outcome. Sealed, numbered ballot containers with documented transfer records create a forensic record. Several states have reduced chain-of-custody documentation requirements in recent cycles, creating audit gaps that post-election review cannot close.

---

## 3. Participation Mechanisms

### 3.1 Automatic Voter Registration: What the Evidence Shows

Automatic voter registration (AVR) moves voter registration from an opt-in to an opt-out model, typically through integration with DMV or other government agency databases. Oregon adopted the first state AVR system in 2016; California followed in 2017. As of 2026, 23 states and the District of Columbia have enacted AVR.

The evidence on AVR's effects divides into two distinct findings that are frequently conflated. AVR substantially increases registration rates: the Center for American Progress projected that nationwide AVR adoption would add more than 22 million voters in the first year. Oregon's implementation added substantial numbers to the rolls, though registration increases varied widely across states, from 9 to 94 percent depending on implementation model and baseline conditions. This is not in dispute.

The evidence on turnout effects from those newly registered voters is more complicated. Only 42 percent of automatically registered Oregonians turned out in the 2018 election, well below the 70 percent turnout rate for voters who registered through traditional channels. The turnout gap reflects a genuine behavioral dynamic: voters who affirmatively choose to register are, on average, more politically engaged than voters who are registered passively. AVR registration does not automatically create election participation.

However, the policy-relevant calculation is net turnout, not per-registrant turnout. Even if automatically registered voters turn out at lower rates than traditionally registered voters, adding large numbers of additional voters to the rolls increases net participation if even a fraction of new registrants vote who would not have done so under the opt-in system. The evidence supports this: research published in 2024 found that AVR increases young voter turnout by 3.2 percentage points on average, with front-end opt-out policies increasing youth turnout by 2.8 points and back-end opt-out policies producing a 3.9-point effect. For a demographic with historically low turnout (18-24 year olds), these are significant margins.

AVR also improves roll accuracy. The most common source of voter roll errors is outdated registration information — voters who have moved and failed to update their registration. AVR systems integrated with DMV records automatically update address information when voters change their driver's license, which reduces both roll maintenance costs and the error rate that produces mismatched registrations. This is an underappreciated argument for AVR: it is not only a participation tool but a data hygiene tool that reduces the size of the voter roll error problems that partisan actors exploit to challenge legitimate registrations.

Sources: [MIT Election Lab: Automatic Voter Registration](https://electionlab.mit.edu/research/automatic-voter-registration); [Center for American Progress: Who Votes With Automatic Voter Registration?](https://www.americanprogress.org/article/votes-automatic-voter-registration/); [FiveThirtyEight: What Happened When 2.2 Million People Were Automatically Registered To Vote](https://fivethirtyeight.com/features/what-happened-when-2-2-million-people-were-automatically-registered-to-vote/); [Berkeley Initiative for Young Americans: Easy as Clicking 'Yes'](https://youngamericans.berkeley.edu/2024/09/easy-as-clicking-yes-how-automatic-voter-registration-is-powering-up-youth-votes/)

### 3.2 Ranked Choice Voting: Implementation Evidence and Political Environment

Ranked choice voting (RCV) — also called instant-runoff voting or alternative vote — allows voters to rank candidates in order of preference. If no candidate receives a majority of first-choice votes, the last-place candidate is eliminated and their supporters' second-choice votes are redistributed, until a candidate achieves a majority. The mechanism was designed to solve two problems: it eliminates the "spoiler effect" that discourages third-party candidacies under plurality voting, and it produces majority winners in single-round elections without the cost and participation drop-off of a separate runoff.

Maine adopted RCV for federal and statewide elections beginning in 2018, following a citizen initiative. Maine's model covers all federal elections (House, Senate) and statewide primaries. Alaska adopted a more ambitious system in 2020 — a top-four nonpartisan primary with RCV in the general election — designed to reduce the power of partisan primaries in producing extreme nominees. Alaska's system produced the most closely watched RCV general election contest of the modern era: the 2022 House special election in which Democrat Mary Peltola defeated Sarah Palin (and a second Republican) on the second round of tabulation.

Alaska's experience through 2024 provides the clearest evidence on RCV's effects in a competitive multi-candidate environment. A 2024 study in Social Science Quarterly found that Alaska's system affected campaign finance spending patterns — specifically, that cross-cutting appeals to second-choice voters in ranked-choice contests altered fundraising strategies compared with the winner-take-all primary model. Research on polarization effects, while not definitive, documents that RCV primary systems tend to reduce the advantage of extreme candidates over moderate ones, because a candidate who wins 35 percent of a plurality primary may lose in an RCV field where moderate voters collectively rank a centrist higher.

The 2024 electoral environment was unfavorable for RCV expansion. Ballot measures to establish or maintain RCV failed in six states; Nevada reversed its 2022 approval. Alaska's repeal measure was defeated by the narrowest margin in state history — 50.1 percent to 49.9 percent — and a new repeal measure is on the ballot for 2026. Seventeen states have enacted legislative bans on RCV since 2022, with the partisan divide nearly complete: Republican legislators vote nearly unanimously to ban RCV, Democratic legislators nearly unanimously to preserve it. This partisan polarization of the mechanism itself undermines its appeal as a depolarizing tool, since polarized debates about voting methods tend to entrench partisan identities rather than bridge them.

For implementation advocates, the most important technical finding from Maine and Alaska is that RCV is tabulation-auditable: the round-by-round counting process produces a complete paper trail of how votes transferred, and an RLA can verify the outcome of any particular round. The claim that RCV is "too complicated to audit" is technically incorrect; it is more complicated to tabulate than plurality voting, but the complication is in the counting software, not in the underlying paper records. FairVote's 2026 primary tracker documents RCV in use for multiple states' gubernatorial and congressional primaries, suggesting that implementation capacity exists at scale.

Sources: [FairVote: Fact Sheet — Ranked Choice Voting & 2026 Primaries](https://fairvote.org/press/fact-sheet-ranked-choice-voting-2026-primaries/); [Alaska Ballot Measure 2 — Repeal Top-Four Ranked-Choice Voting (2024)](https://ballotpedia.org/Alaska_Ballot_Measure_2,_Repeal_Top-Four_Ranked-Choice_Voting_Initiative_(2024)); [Bipartisan Policy Center: Reform Meets Reality — How Ranked Choice Voting Impacts Election Administration](https://bipartisanpolicy.org/report/reform-meets-reality-how-ranked-choice-voting-impacts-election-administration/); [Social Science Quarterly: Election reform and campaign finance — Did Alaska's top-4 nonpartisan primaries affect political spending?](https://onlinelibrary.wiley.com/doi/full/10.1111/ssqu.13422)

### 3.3 Ballot Access Reform and Fusion Voting

Third-party ballot access in the United States is structurally hostile compared with virtually any other established democracy. The mechanics vary by state but generally involve: (1) petition signature thresholds requiring a percentage of registered voters or previous election votes to qualify for the ballot, often set at levels that require professional signature-gathering campaigns costing hundreds of thousands of dollars; (2) filing deadlines set months before primary season, before candidates or issues have achieved public salience; (3) sore-loser laws in many states that prevent candidates who lose a primary from appearing on the general election ballot as independents; and (4) the interaction of these requirements with winner-take-all plurality voting, which structurally penalizes votes for third-party candidates as "wasted" votes.

Fusion voting — permitting a candidate to appear on the ballot under multiple party lines, with votes on each line counted separately but totaled — is the most structurally significant ballot access reform available within the existing constitutional framework. Fusion allows minor parties to cross-endorse major-party candidates while maintaining their independent ballot line and ideological brand. A voter who ranks healthcare or climate above partisan identity can vote the Working Families Party line for a Democrat who holds those positions, sending both a vote and a signal about why they voted.

As of 2026, functional fusion voting operates in New York and Connecticut. New York's model — in which the Working Families Party, Conservative Party, and other minor parties each maintain independent ballot lines — has produced measurable effects on political mobilization: the Working Families Party's ballot line, by making the cost of cross-endorsement refusal explicit (WFP can and does run independent candidates against unresponsive Democrats), creates accountability pressure on the Democratic Party that the Vermont model of single-ticket cross-endorsement does not. Vermont uses dual-labeling rather than separate line fusion, which facilitates Progressive-Democrat coordination without giving the Vermont Progressive Party an independent credible threat mechanism.

Efforts to restore fusion voting through litigation are active in New Jersey, Michigan, and Kansas, coordinated primarily by the Center for Ballot Freedom. The constitutional path is complicated by *Timmons v. Twin Cities Area New Party* (1997), in which the Supreme Court upheld Minnesota's anti-fusion law 6-3, finding that states have legitimate interests in maintaining stable political structures that can justify fusion restrictions. *Timmons* does not bar fusion voting — it bars federal constitutional mandates for it — leaving the question to state law, where both legislative and ballot initiative pathways are available.

The sore-loser law problem is separate and directly relevant to the 2026 environment. Independent and third-party candidates face state laws in 44 states that prevent a candidate who runs in and loses a primary from appearing on the general election ballot. These laws were primarily designed to prevent primary losers from attempting end-runs around their party's selection decision, but their effect in the current environment is to close the general election ballot to moderate candidates who lose partisan primaries to extreme opponents. The proliferation of these laws has created a structural obstacle to the kind of independent center candidacies that electoral reform advocates hope RCV and top-two primary systems would enable.

Sources: [Electoral Fusion in the United States — Wikipedia](https://en.wikipedia.org/wiki/Electoral_fusion_in_the_United_States); [Protect Democracy: Fusion voting, explained](https://protectdemocracy.org/work/fusion-voting-explained/); [Center for Ballot Freedom: What They're Saying About Fusion](https://centerforballotfreedom.org/what-theyre-saying-about-fusion/)

### 3.4 Small-Donor Matching and Public Campaign Financing

The relationship between *Citizens United v. FEC* (2010) and election participation is direct but frequently mischaracterized. *Citizens United* did not affect contribution limits to candidate campaigns (individual contribution limits are set by FECA and remain in place); it prohibited limits on independent expenditures by corporations and nonprofits. The practical effect has been to create an independent-expenditure ecosystem — super PACs and dark money 501(c)(4) organizations — that operates parallel to and dramatically exceeds candidate fundraising in competitive races.

The regulatory fix for *Citizens United* requires constitutional amendment or a Supreme Court reversal, neither of which is near-term achievable. The policy fix that does not require constitutional action is structural: public financing mechanisms that amplify small donor contributions create a competitive funding environment in which candidates who rely on small donors can match the scale of those relying on large donors, reducing the electoral relevance of the independent-expenditure gap.

New York City's small-donor matching program, operating since 1988 and currently providing 8-to-1 matching on contributions from city residents (a $10 contribution becomes $90 for the candidate), is the most-studied municipal public financing program in the country. The Brennan Center's documented outcomes include: more competitive primary elections, more first-time candidates, a donor base that more closely matches the city's demographic composition, and no documented reduction in campaign quality. New York State extended a similar program to state legislative and statewide races beginning in 2022, providing a larger-scale test. The first cycle demonstrated that publicly financed candidates could run competitive campaigns even in districts where independent expenditures opposed them heavily.

Three Maryland counties (Anne Arundel, Baltimore, and Prince George's) will implement new small-donor matching programs for the 2026 election cycle, expanding the evidence base beyond the New York model. Three states considered expansion programs in 2026 legislative sessions (OpenSecrets documented the activity as of April 2026). Connecticut's statewide program, enacted in 2005, has operated through 21 years of elections under both Democratic and Republican governors, establishing that public financing programs can survive political transitions — a critical durability question.

The *Loper Bright* implication for campaign finance is specific: FEC regulations implementing FECA's coordination limits, contribution source restrictions, and disclosure requirements are now subject to de novo judicial review. In May 2025, the FEC became inoperative due to a quorum vacancy strategy — the administration declined to nominate commissioners, reducing the body below the four-commissioner threshold required for enforcement actions. This means that coordination limits and disclosure requirements are currently unenforceable at the federal level regardless of their statutory authority. The *Loper Bright* implication for state programs is less severe, since state campaign finance commissions are not subject to the same quorum constraints, but it creates a federal-state asymmetry in which state programs are the primary functioning public financing infrastructure.

Sources: [NYC Campaign Finance Board: Matching Funds Program](https://www.nyccfb.info/program); [Brennan Center: Small Donor Public Financing, Explained](https://www.brennancenter.org/our-work/research-reports/small-donor-public-financing-explained); [Brennan Center: New York State's Public Campaign Financing Program Empowers Constituent Small Donors](https://www.brennancenter.org/our-work/research-reports/new-york-states-public-campaign-financing-program-empowers-constituent); [OpenSecrets: Three states considering expansions of public campaign financing programs](https://www.opensecrets.org/news/2026/04/three-states-considering-expansions-of-public-campaign-financing-programs)

---

## 4. Institutional Resilience and Capture-Resistance

### 4.1 International Models: What Independent Administration Looks Like

The United States' unusual approach to election administration — nearly all election officials are elected partisans, rather than professional civil servants — is an international outlier. International Institute for Democracy and Electoral Assistance (International IDEA) taxonomy identifies three models of election management: independent bodies (chaired by judges or nonpartisan professionals), governmental bodies (administered by Interior or Justice ministries), and mixed models. Most established democracies with high election integrity scores use independent or mixed models.

**Australia (AEC model)**: The Australian Electoral Commission has been chaired by a judge or former judge since its establishment, reinforcing non-partisanship through the symbolic authority of the judiciary. Automatic enrollment (compulsory) combined with compulsory voting produces turnout that has not fallen below 90 percent since 1924. The 2025 federal election participation data published by the AEC confirms sustained >90 percent participation at the most recent cycle. The AEC's operational consequence of mandatory voting deserves specific attention: when 90 percent of the eligible population votes, no party can win by suppressing turnout among the opposition's base. Voter suppression tactics — whether through polling place consolidation, identification requirements, or registration purges — are ineffective against a system that fines nonvoters. The structural alignment between mandatory voting and election administration quality is not coincidental: mandatory voting creates a political incentive to make the voting process as simple as possible for everyone, since making it complicated affects everyone's base voters equally.

**Canada (Elections Canada model)**: Canada's Chief Electoral Officer (CEO) has been appointed by resolution of the House of Commons — not by the government — since 1920. This is a constitutional distinction: the CEO reports to Parliament, not to the cabinet, and cannot be removed except by joint address of both chambers. Elections Canada administers federal elections as a non-partisan independent agency with a permanent professional civil service. Canada's voter turnout has declined over the past two decades (from approximately 75 percent in the 1990s to 62 percent in 2021) — evidence that independent administration is necessary but not sufficient for participation. However, Canada has not experienced systematic partisan manipulation of the election administration apparatus itself, which is the specific threat the independent model addresses.

**Germany (Länder model)**: Germany's federal election administration is distributed to state-level (Länder) authorities, with a Federal Returning Officer (Bundeswahlleiter) who provides coordination and legal interpretation but cannot direct state electoral officials. The Federal Ministry of the Interior has authority to enact certain regulations for federal election procedures but has no directive authority over the management bodies themselves. This produces a genuine federalism-independence hybrid: decentralized enough to prevent national-level capture, but with sufficient coordination through the independent Federal Returning Officer to ensure consistency in election law application. The German model is the international precedent most directly applicable to the US federal structure, since Germany faces the same constitutional division between federal and state authority.

**Taiwan (citizen observer model)**: Taiwan's election integrity architecture deserves specific attention given its adversarial context — Taiwan conducts elections while facing sophisticated Chinese disinformation operations targeting its democratic institutions. Taiwan uses hand-marked paper ballots counted publicly and immediately after polls close. Counting is performed by poll workers who announce each ballot aloud while displaying it; party representatives and citizen observers are present and authorized to challenge individual ballot interpretations. The 2024 Taiwanese elections — 42 million votes across presidential and legislative contests — were conducted with this manual transparency system. Taiwan's paper ballot and public counting model has essentially eliminated the credibility of systemic fraud allegations: when any citizen can observe the count, the claim that counts are being manipulated requires claiming the fraud is visible to every observer present.

Sources: [International IDEA: Independence in Electoral Management](https://www.idea.int/sites/default/files/publications/independence-in-electoral-management.pdf); [Elections Canada: Comparative Assessment of Central Electoral Agencies](https://www.elections.ca/content.aspx?section=res&dir=rec/tech/comp&document=p4&lang=e); [AEC: Participation in the 2025 federal election](https://www.aec.gov.au/election/fe25/participation-rates.htm); [The Hill: What Taiwan can teach the US about how to run an election](https://thehill.com/opinion/international/4413389-what-taiwan-can-teach-the-u-s-about-how-to-run-an-election/); [WBEZ: What the US can learn from how Australia votes](https://www.wbez.org/democracy-solutions-project/2024/australia-electoral-innovation-preferential-ranked-choice-voting-proportional-representation-aec)

### 4.2 Capture-Resistance: Adversarial Stress Testing

The question of what would be required to rig elections under each mechanism is analytically important because it identifies the specific vulnerabilities that a sophisticated actor would target and the procedural requirements that make those attacks either implausible or detectable.

**Hand-marked paper ballots with RLA**: Rigging a paper ballot election with RLA verification requires either (a) physically substituting fraudulent ballots in the chain of custody — requiring access to sealed, numbered ballot containers with documented physical seals, which creates a forensic record — or (b) compromising the random seed generation to enable predictable ballot selection, which Colorado prevents by using physical dice in a public ceremony. The scale of paper substitution required to change a competitive statewide outcome would involve tens or hundreds of thousands of individual ballots, with physical evidence at every step. This is not impossible, but it is orders of magnitude harder than compromising the tabulation software of an internet-connected voting machine.

**Paperless electronic systems**: The attack surface for paperless systems is both larger and harder to detect. Software compromise, supply chain infiltration, or network intrusion can alter tallies without any physical evidence. The most important finding from the Cybersecurity and Infrastructure Security Agency's (now defunded) election security assessments was that electronic poll book vulnerabilities — the systems used to check in voters on Election Day — are more significant than tabulation vulnerabilities, because poll book compromise can prevent legitimate voters from casting ballots at a scale and speed that tabulation manipulation cannot. In a close election, suppressing 5,000 legitimate voters in a targeted precinct is functionally equivalent to adding 5,000 fraudulent votes.

**Decentralized administration**: Decentralization's capture-resistance profile is well-understood: no single adversary can simultaneously compromise 10,000 election offices. The failure mode is instead quality degradation at the margins — the county offices with no cybersecurity staff, obsolete equipment, and no federal technical support are the vulnerable nodes. Before CISA's dismantlement, federal vulnerability assessments identified the most at-risk counties. That information now belongs to no functioning federal agency. The minimum viable solution — a national RLA requirement with NIST-specified risk limits — creates a verification layer that can detect systemic compromise even in low-capacity counties, because the paper record exists independent of the electronic system.

**Certification as a capture mechanism**: As documented in Section 1.1, the certification refusal strategy exploits the gap between the count and the legal ratification of the count. The capture-resistance mechanism is judicial (mandamus to compel certification) and legislative (defining certification as ministerial with no discretion). Michigan's constitutional amendment embedding certification requirements is the model: if certification conditions are in the state constitution, legislative modification by a hostile state legislature requires a supermajority or constitutional referendum, which raises the capture cost substantially.

### 4.3 The Self-Enforcing Mechanism Standard

Applying the same analytical framework developed in Phase 3 Candidate 5 (fiscal architecture) to election security: which mechanisms are self-enforcing versus dependent on good-faith administration?

Self-enforcing mechanisms in the election context are those where the mechanism's operation does not require the cooperation of the official who might benefit from non-compliance. An RLA with a public random seed and publicly available ballot image records is self-enforcing: any independent party can verify the audit by selecting the same ballots using the same random seed and comparing results. A paper ballot requirement enforced by an elected secretary of state who opposes paper ballots is not self-enforcing.

The design principle that follows: election security mechanisms should minimize the number of steps that require the active cooperation of elected officials with partisan interests in the outcome. This is the structural argument for:

- Mandatory RLA requirements in statute or constitution (rather than voluntary guidelines)
- Automatic voter registration through agency integration (rather than agency-discretion implementation)
- Independent election commissions with cause-only removal (rather than elected secretaries of state)
- Bipartisan canvassing boards with mandated certification timelines (rather than discretionary review periods)
- Federal minimum floor standards for ballot chain of custody (rather than county-level variation)

---

## 5. Demographic Dimensions and the Turnout Feedback Loop

The relationship between registration access, ballot access, and participation is not demographically neutral. The MIT Election Lab's voting technology research documents systematic variation in ballot rejection rates by jurisdiction: rural counties using older equipment have higher ballot spoilage rates than urban counties with newer systems. Language access provisions — required under Section 203 of the Voting Rights Act for jurisdictions with specified minority language populations — are inconsistently implemented, with some jurisdictions providing minimal-quality translations that fail the substantive accessibility standard. Disability access under the Americans with Disabilities Act creates requirements for polling place physical accessibility and accessible ballot format that are also inconsistently implemented.

The demographic analysis of automatic voter registration is particularly important in the current context. Young voters (18-29) are the demographic most likely to be unregistered despite eligibility, and AVR's measured 3.2-point turnout increase for young voters represents one of the largest single-mechanism turnout effects documented for that demographic. Black, Hispanic, and Native American voters are registered at lower rates than white voters; AVR integration with DMV records systematically closes this gap, because DMV enrollment rates are higher and more demographically uniform than voluntary registration rates.

The disability access dimension of ballot marking devices connects to the broader participation-security tension. BMDs were initially adopted specifically to comply with HAVA's disability access requirements — they allow voters with motor or visual impairments to cast ballots independently. The security community's concerns about BMD software integrity are legitimate and documented. But any policy response that reduces BMD availability reduces accessibility. The resolution — mandatory voter verification of BMD output, random post-election comparison audits of BMD-printed ballots against BMD electronic records, and accessible HMPB alternatives for voters who can use them — addresses the security concern without sacrificing accessibility.

---

## 6. US Statutory Reform Pathways: Five Concrete Mechanisms with Post-*Loper Bright* Enforceability

### 6.1 The Post-*Loper Bright* Enforceability Framework

*Loper Bright Enterprises v. Raimondo* (2024) overruled *Chevron* deference and requires courts to exercise independent judgment on agency statutory interpretations. For election law, the specific implication is that EAC guidance, FEC regulations, and agency interpretations of HAVA, NVRA, and FECA are now subject to de novo review. Regulations that relied on broad delegations from Congress — the standard pre-*Loper Bright* pattern — are the most vulnerable to challenge.

The *Loper Bright* enforceability principle for election statutes is: the more specifically Congress defines the required conduct, the less vulnerable the statute is to post-*Loper Bright* deregulatory litigation. A statute that says "states must implement risk-limiting audits with a risk limit not to exceed 5 percent using the ballot comparison or ballot-polling method" is far less vulnerable to agency-override than a statute that says "states must conduct appropriate post-election audits as defined by the EAC." Congress can write the standard; it need not delegate it.

The second *Loper Bright* implication is private right of action. If Congress creates a private right of action directly in statute — allowing individual voters or civil rights organizations to sue to enforce election security or access requirements — the enforcement mechanism does not run through the same executive branch agencies that may be captured or inoperative. Private enforcement of NVRA has produced most of the significant voter registration jurisprudence; private enforcement of a paper ballot or RLA requirement would provide an enforcement mechanism independent of DOJ or the EAC.

The third *Loper Bright* implication is clarity of congressional intent for *Shelby County* reconstruction. The Supreme Court's 2013 *Shelby County v. Holder* ruling struck down the VRA's coverage formula as outdated. The John R. Lewis Voting Rights Advancement Act (S.2523, 119th Congress, introduced July 2025) proposes new coverage criteria based on documented recent violations rather than historical patterns. Under *Loper Bright*, the new coverage formula must be precise enough that courts can apply it without deference to DOJ interpretation — meaning Congress must define each trigger criteria in measurable, verifiable terms rather than delegating definitional authority to the agency.

### 6.2 Five Reform Mechanisms

**Mechanism 1: National Risk-Limiting Audit Act**

Content: Amend HAVA to require all states to conduct ballot comparison or ballot-polling RLAs with a risk limit of 5 percent or less for all federal offices. Require public random seed generation through a specified protocol (physical dice or cryptographic alternative with verifiable public inputs). Require complete ballot image publication within 72 hours of election certification. Create a private right of action for any voter in the relevant jurisdiction to enforce the audit requirement.

Post-*Loper Bright* design: The act specifies the risk limit, audit method, and seed generation protocol in statutory text. No agency discretion; no delegation to EAC guidance. Courts applying the statute need not defer to any agency interpretation.

Legal basis: Article I, Section 4 grants Congress authority to "make or alter" state regulations on the "Times, Places and Manner" of congressional elections. The Supreme Court has consistently upheld congressional time-place-manner regulation of federal elections.

State-level precedent: Colorado (3% risk limit, public seed, 64-county implementation since 2017), Rhode Island, Virginia. Eight state implementations demonstrate feasibility.

**Mechanism 2: Automatic Voter Registration Integration Act**

Content: Amend NVRA to require states to establish automatic voter registration at DMV, Social Security Administration, SNAP, Medicaid, and public college/university agencies, with opt-out capability. Require interoperability with state voter registration databases. Prohibit removal of voters automatically registered under the Act except through the full NVRA notice-and-response process. Create a private right of action for NVRA violations, explicitly including automated registration failures.

Post-*Loper Bright* design: Specifies the agencies, integration requirements, and opt-out procedures in statutory text. Removes EAC's discretion over which agencies qualify; Congress lists them. The NVRA private right of action — which predates *Loper Bright* and is well-established — provides enforcement without relying on DOJ.

State precedent: Oregon (2016), California (2017), 21 additional states. The existing NVRA private right of action has produced extensive enforcement litigation (Indiana's Acts 442 and 334 were struck down by the Seventh Circuit in 2025 for NVRA violations under the existing private right of action).

Interplay with Trump EO: The March 2025 executive order's passport-citizenship requirement for federal registration form was permanently blocked as exceeding presidential authority over the EAC. The Automatic Voter Registration Integration Act would embed registration policy in statute — making future executive order interference legally implausible regardless of the specific administration.

**Mechanism 3: Election Administration Independence Act**

Content: Establish a permanent, non-partisan Federal Election Administration (FEA) as an independent agency analogous to the AEC (Australia) or Elections Canada. The FEA is governed by a five-member board appointed by staggered terms: two members appointed by the Senate Majority Leader, two by the Minority Leader, one by joint recommendation of the four. Members serve eight-year terms, removable only for cause defined in statute (incapacitation, proven corruption, or material breach of independence requirements). The FEA administers the federal voter registration form, HAVA compliance assessments, federal election security grants, and RLA certification. States retain primary administration of their own elections; the FEA provides minimum federal floor standards.

Post-*Loper Bright* design: Staggered terms with cause-only removal are the structural self-enforcement mechanism. FEA members cannot be removed by a president who disagrees with their administration decisions. This mirrors the Brazil central bank model documented in Phase 3 Candidate 5: the structural protection outlasts any particular administration's pressure. Congressional appointment of majority of members protects against executive capture analogous to the Canadian model.

Constitutional basis: *Morrison v. Olson* (1988) and *Seila Law v. CFPB* (2020) together establish that independent agencies with for-cause removal protections are constitutionally permissible when they do not exercise exclusively executive functions. Election administration — which Congress is constitutionally authorized to regulate — can be delegated to an independent agency. The FEC's bipartisan structure, operating since 1974, is the existing statutory model.

**Mechanism 4: Bright Lines for Certification Act**

Content: Amend federal law to specify that certification of federal election results by state and county canvassing authorities is ministerial: once the statutory count is complete, certification must be issued within five business days of canvass completion without discretion. Create a private right of action to seek mandamus in federal court against any official who fails to certify within the statutory period. Create federal civil and criminal penalties for willful certification delay.

Post-*Loper Bright* design: No agency interpretation required; the standard (certification is mandatory, no discretion) is in statutory text. Federal court mandamus enforces ministerial duties directly.

Legal basis: The Elections Clause allows Congress to specify the "Times" and "Manner" of elections, which includes the certification process. Federal criminal penalties (18 U.S.C. § 594 and related provisions) already exist for voter intimidation; extending equivalent penalties to certification manipulation is within Congress's existing election law authority.

Existing case law: Courts have consistently held that certification is ministerial in post-2020 litigation in Georgia, Michigan, Arizona, and Nevada. The Bright Lines for Certification Act codifies what courts have held while providing a federal enforcement mechanism that does not require state prosecutors (who may be aligned with certification refusers) to act.

**Mechanism 5: Federal Small-Donor Matching Act for Congressional Elections**

Content: Establish a voluntary small-donor matching program for federal congressional elections providing 6-to-1 match on contributions of $200 or less from in-district residents. Fund the program through a reallocation of tax benefits on large contributions (requiring legislation, not constitutional amendment). Participating candidates accept matching funds in exchange for contribution limits lower than FECA maxima. The program is administered by the FEC or FEA.

Post-*Loper Bright* design: Congress sets the match ratio, income cap, in-district residency definition, and contribution limits in statutory text. No agency discretion on core program parameters; agency discretion limited to ministerial processing functions.

Constitutional basis: *Buckley v. Valeo* (1976) upheld the voluntary public financing system for presidential elections. The Court distinguished voluntary programs (which it upheld) from contribution and expenditure limits (which it treated differently). A voluntary matching program for congressional elections is squarely within *Buckley*'s framework. *Citizens United* did not address voluntary public financing.

State precedent: NYC (8:1 match, 35+ years), New York State (2022-present), Connecticut (since 2005), Maryland (three counties beginning 2026). Multiple cycles of state data available.

### 6.3 What Cannot Be Achieved Without Constitutional Amendment

Three reforms require either constitutional amendment or Supreme Court reversal and are therefore not achievable on a legislative-only pathway:

*Citizens United* reversal through constitutional amendment: Requires two-thirds supermajority in both chambers plus ratification by three-fourths of states. No mechanism by which this is achievable in the current political environment. State-level experimentation with public financing is the actionable alternative.

Mandatory voting: Article II, Section 1's voter qualification provisions — which reserve voting qualification primarily to state law — and First Amendment concerns about compelled political participation make a federal mandatory voting requirement constitutionally contested. Australia's compulsory voting operates entirely within a parliamentary system that does not face equivalent constitutional constraints. Robust AVR combined with Election Day as a federal holiday and expanded early voting are achievable statutory alternatives.

National popular vote for president: Requires either a constitutional amendment (changing the Electoral College) or sufficient state adoption of the National Popular Vote Interstate Compact to achieve the 270 electoral vote threshold. The NPVIC has been enacted by 17 states and DC totaling 209 electoral votes as of 2026; it requires an additional 61 electoral votes to take effect.

---

## 7. Implementation Dependencies and Timeline

### 7.1 What Is Achievable Before November 2026

The six-month window before November 2026 defines what is and is not achievable at the legislative level. Congressional action on any of the five reform mechanisms is not achievable in this window: none will advance through the current 53-47 Republican Senate majority with the filibuster intact, and even if Democrats retake one or both chambers in November 2026, legislative action before the election is impossible.

What is achievable before November 2026 is state-level implementation and litigation infrastructure:

- States that do not have RLA requirements can enact them through state legislative action or, where available, ballot initiative. Colorado and other model states can provide technical assistance.
- AVR expansion in states where legislative routes are available. As of 2026, seven states have pending AVR legislation that could be enacted within the relevant timeframe.
- Certification protection through the existing mandamus framework: the legal infrastructure for emergency court action against certification refusers can be pre-positioned in all contested states before Election Day.
- HAVA security grant applications: states should maximize applications against the $45 million FY2026 pool, even at reduced funding levels, to maintain federal security relationships.
- State small-donor matching program adoption: any state can enact a state-level program without federal action; the model statutes from New York and Connecticut are available.

### 7.2 The Two-Cycle Reform Window

The strategically realistic window for the five federal reforms proposed in Section 6 is a congressional majority willing to prioritize electoral reform — potentially arising from a 2026 Democratic midterm wave or a 2028 election cycle. The reform window requires not only a majority but a majority willing to use the nuclear option for voting rights (a 51-vote threshold for electoral reform legislation), since all five reforms could be filibustered by a Republican minority even in a Democratic majority Senate.

The filibuster dynamic is the central variable. As documented in Domain 1, the SAVE Act coalition fracture (Collins, Murkowski, Tillis, McConnell defecting on the 48-50 vote) demonstrates that the institutionalist faction within the Republican caucus protects the filibuster on procedural grounds regardless of legislative content. That same institutionalist logic, if applied symmetrically, should protect a Democratic majority's electoral reform legislation from filibuster — the question is whether Democratic leadership in a hypothetical future majority would invoke the argument. There is no guarantee they would. But the political dynamics are more favorable than they appear: a Democratic majority that fails to pass basic election security legislation when it has the votes will face electoral accountability from the same coalition that produced the majority.

### 7.3 Sequencing Priority

If only one reform is achievable, the National Risk-Limiting Audit Act should take priority. It is the mechanism with the most direct impact on election security (verified outcome), the broadest bipartisan appeal (audit requirements are nominally consistent with "election integrity" framing from both parties), and the strongest existing state implementation record. Colorado's system is a working model that requires federal legislation only to make it a national floor, not to prove it is operationally feasible.

If two reforms are achievable, add the Automatic Voter Registration Integration Act. Its interaction effect with RLAs is significant: AVR produces more accurate rolls (reducing the erroneous purge problem) while RLAs produce more verifiable outcomes (reducing the counting-challenge problem). Together they address both the participation suppression attack and the tabulation integrity attack that currently define the election security threat environment.

The Election Administration Independence Act, Bright Lines for Certification Act, and Federal Small-Donor Matching Act each require broader legislative coalitions and longer implementation timelines. They are appropriate Phase 2 and Phase 3 priorities after the foundational integrity and participation mechanisms are established.

---

## 8. Bibliography

### Primary Legal Sources

1. Help America Vote Act of 2002 (HAVA), 52 U.S.C. §§ 20901–21145. [Congress.gov](https://www.congress.gov/bill/107th-congress/house-bill/3295)
2. National Voter Registration Act of 1993 (NVRA), 52 U.S.C. §§ 20501–20511. [DOJ Civil Rights Division](https://www.justice.gov/crt/national-voter-registration-act-1993-nvra)
3. John R. Lewis Voting Rights Advancement Act of 2025 (H.R. 14 / S.2523, 119th Congress). [Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/2523)
4. Executive Order 14248, "Preserving and Protecting the Integrity of American Elections," March 25, 2025. [White House](https://www.whitehouse.gov/presidential-actions/2025/03/preserving-and-protecting-the-integrity-of-american-elections/)
5. *Loper Bright Enterprises v. Raimondo*, 603 U.S. 369 (2024). (Overruling *Chevron U.S.A., Inc. v. Natural Resources Defense Council*)
6. *Citizens United v. Federal Election Commission*, 558 U.S. 310 (2010).
7. *Shelby County v. Holder*, 570 U.S. 529 (2013).
8. *Timmons v. Twin Cities Area New Party*, 520 U.S. 351 (1997).
9. *Buckley v. Valeo*, 424 U.S. 1 (1976).

### US Government Sources

10. Election Assistance Commission (EAC). Voluntary Voting System Guidelines (VVSG) 2.0 (2021). [EAC.gov](https://www.eac.gov/sites/default/files/TestingCertification/Voluntary_Voting_System_Guidelines_Version_2_0.pdf)
11. EAC. 2024 VVSG Review Report (January 2025). [EAC.gov](https://www.eac.gov/sites/default/files/2025-01/2024%20VVSG%20Review%20Report.pdf)
12. EAC. HAVA Election Security Grant Programs (FY2026). [EAC.gov](https://www.eac.gov/grants/hava-grant-programs)
13. NIST. Election Security Research and Projects. [NIST.gov](https://www.nist.gov/itl/voting/research-and-projects/election-security)
14. NIST. Security of Ballot Marking. [NIST.gov](https://www.nist.gov/itl/voting/security-ballot-marking)
15. Colorado Secretary of State. Risk-Limiting Audit FAQs. [ColoradoSOS.gov](https://www.coloradosos.gov/pubs/elections/RLA/faqs.html)

### Academic and Research Sources

16. MIT Election Lab. "How We Voted in 2024." (2025). [ElectionLab.MIT.edu](https://electionlab.mit.edu/articles/new-report-how-we-voted-2024)
17. MIT Election Lab. Automatic Voter Registration research. [ElectionLab.MIT.edu](https://electionlab.mit.edu/research/automatic-voter-registration)
18. MIT Election Lab. Election Auditing white paper. [ElectionLab.MIT.edu](https://electionlab.mit.edu/research/projects/mapping-election-science/white-papers/election-auditing)
19. Albert, Zachary. "Election reform and campaign finance: Did Alaska's top-4 nonpartisan primaries and ranked-choice general elections affect political spending?" *Social Science Quarterly* (2024). [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/ssqu.13422)
20. International IDEA. "Independence in Electoral Management: Electoral Processes Primer 1." [IDEA.int](https://www.idea.int/sites/default/files/publications/independence-in-electoral-management.pdf)
21. Elections Canada. "Comparative Assessment of Central Electoral Agencies." [Elections.ca](https://www.elections.ca/content.aspx?section=res&dir=rec/tech/comp&document=p4&lang=e)
22. Bipartisan Policy Center. "Measuring the Impact of Recent Grants to Election Administrators Under HAVA." (January 2025). [BipartisanPolicy.org](https://bipartisanpolicy.org/report/impact-recent-grants-help-america-vote-act/)
23. Bipartisan Policy Center. "Reform Meets Reality: How Ranked Choice Voting Impacts Election Administration." [BipartisanPolicy.org](https://bipartisanpolicy.org/report/reform-meets-reality-how-ranked-choice-voting-impacts-election-administration/)

### Brennan Center for Justice Sources

24. Brennan Center. "Small Donor Public Financing, Explained." [BrennanCenter.org](https://www.brennancenter.org/our-work/research-reports/small-donor-public-financing-explained)
25. Brennan Center. "New York State's Public Campaign Financing Program Empowers Constituent Small Donors." [BrennanCenter.org](https://www.brennancenter.org/our-work/research-reports/new-york-states-public-campaign-financing-program-empowers-constituent)
26. Brennan Center. "The President's March 2025 Executive Order on Elections." [BrennanCenter.org](https://www.brennancenter.org/our-work/research-reports/presidents-executive-order-elections-explained)
27. Brennan Center. "Status of Trump's Anti-Voting Executive Order." [BrennanCenter.org](https://www.brennancenter.org/our-work/research-reports/status-trumps-anti-voting-executive-order)
28. Brennan Center. "Small Donor Matching Funds: The NYC Experience." (2019). [BrennanCenter.org](https://www.brennancenter.org/sites/default/files/2019-08/Report_Small-Donor-Matching-Funds-NYC-Experience.pdf)
29. Brennan Center. "John R. Lewis Voting Rights Advancement Act Reintroduced in Senate." (2025). [BrennanCenter.org](https://www.brennancenter.org/our-work/analysis-opinion/john-r-lewis-voting-rights-advancement-act-reintroduced-senate-brennan)
30. Brennan Center. "Citizens United, Explained." [BrennanCenter.org](https://www.brennancenter.org/our-work/research-reports/citizens-united-explained)

### Civil Society and Advocacy Sources

31. Verified Voting. Comments on VVSG 2.0 v3. [VerifiedVoting.org](https://verifiedvoting.org/verified-voting-comments-on-vvsg-2-0-v3/)
32. FairVote. "Fact Sheet: Ranked Choice Voting & 2026 Primaries." [FairVote.org](https://fairvote.org/press/fact-sheet-ranked-choice-voting-2026-primaries/)
33. Center for American Progress. "Who Votes With Automatic Voter Registration?" [AmericanProgress.org](https://www.americanprogress.org/article/votes-automatic-voter-registration/)
34. Protect Democracy. "Fusion voting, explained." [ProtectDemocracy.org](https://protectdemocracy.org/work/fusion-voting-explained/)
35. Protect Democracy. "Election certification, explained." [ProtectDemocracy.org](https://protectdemocracy.org/work/election-certification-explained/)
36. Just Security. "Election Certification Refusers Are a Movement." [JustSecurity.org](https://www.justsecurity.org/100005/election-certification-refusers/)
37. Issue One. "Federal Funding for American Elections — HAVA Grants." [IssueOne.org](https://issueone.org/articles/federal-funding-for-american-elections-hava-grants/)
38. Leadership Conference on Civil and Human Rights. "Coalition Letter Supporting Federal Funding for Election Administration in FY26." [CivilRights.org](https://civilrights.org/resource/coalition-letter-supporting-federal-funding-for-election-administration-in-fy26/)
39. Campaign Legal Center. "Victory! Anti-Voter Executive Order Halted in Court." [CampaignLegal.org](https://campaignlegal.org/update/victory-anti-voter-executive-order-halted-court)
40. Lawfare Media. "The Trump Administration Comes for State Voter Rolls." [LawfarMedia.org](https://www.lawfaremedia.org/article/the-trump-administration-comes-for-state-voter-rolls)

### Media and Monitoring Sources

41. OpenSecrets. "Three states considering expansions of public campaign financing programs." (April 2026). [OpenSecrets.org](https://www.opensecrets.org/news/2026/04/three-states-considering-expansions-of-public-campaign-financing-programs)
42. Votebeat. "Georgia election rule changes raise concerns about certification fights." (October 2024). [Votebeat.org](https://www.votebeat.org/2024/10/10/presidential-election-certification-delays-trump-republicans-disputes-georgia-board-rule/)
43. The Hill. "What Taiwan can teach the US about how to run an election." [TheHill.com](https://thehill.com/opinion/international/4413389-what-taiwan-can-teach-the-u-s-about-how-to-run-an-election/)
44. WBEZ Chicago Democracy Solutions Project. "What the US can learn from how Australia votes." [WBEZ.org](https://www.wbez.org/democracy-solutions-project/2024/australia-electoral-innovation-preferential-ranked-choice-voting-proportional-representation-aec)
45. Colorado Politics. "Colorado's election audits are built on math, not politics." (March 2026). [ColoradoPolitics.com](http://www.coloradopolitics.com/2026/03/12/colorados-election-audits-are-built-on-math-not-politics-in-response/)

---

*Research completed April 28, 2026. Production-ready for Phase 1 institutional distribution. Cross-reference: Domain 1 (Voting Rights), Domain 37 (Federal Executive Interference — 2026 Midterms), Domain 37b (State Election Security Coordination), Domain 35 (Post-Loper Bright Landscape).*
