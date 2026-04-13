# Remote Electronic Voting: Deep Research Report

**Date**: 2026-04-10 (updated April 11, 2026 with Section 10: "Who Is a Voter?" analysis; Section 4 expanded April 11, 2026 with comprehensive cryptographic voting systems deep dive)
**Status**: Active — Section 4 expanded, Section 10 added April 11, 2026
**Topic**: Why fully remote electronic voting hasn't been implemented, what barriers exist, what it would take to make it work, and whether an open-source system could be both transparent and secure.

---

## Executive Summary

The consensus of computer scientists, cryptographers, and election security experts is unambiguous: **no currently deployed technology makes fully remote electronic voting secure enough for binding public elections**. But this isn't a simple gap — it's a cluster of deeply intertwined technical, political, legal, and human problems, each of which would need to be solved independently before the others matter. Several are genuinely hard unsolved problems in computer science. A few may be fundamentally unsolvable.

---

## 1. The Scientific Consensus

The National Academies of Sciences, Engineering and Medicine concluded in their 2018 report:

> *"The Internet should not be used for the return of marked ballots...no known technology guarantees the secrecy, security, and verifiability of a marked ballot transmitted over the Internet."*

As of January 2026, Princeton's Center for Information Technology Policy published a direct statement: **"Internet voting is insecure and should not be used in public elections."** More than 60 scientists and election security experts signed an open letter in 2020 to the same effect. The FBI, DHS/CISA, NIST, and the Election Assistance Commission jointly warned in 2020 that electronic ballot return was "high risk."

The US Senate Select Committee on Intelligence stated: *"States should resist pushes for online voting."*

This is not a fringe position — it is the dominant technical consensus and has held for over 25 years.

---

## 2. The Technical Barriers

### Problem 1: The Uncontrolled Device Problem

In a polling place, the voting machine is controlled, audited, and isolated. With remote voting, **the voter's device — phone, laptop, desktop — is unknown, untrusted, and potentially compromised**. Malware can silently alter a vote before it's even encrypted. The ballot can be changed *before* it leaves the device. There is no technical way to guarantee a device is malware-free. You can cryptographically verify what was *received*, but you can't verify it matches what the voter *intended* if the endpoint is hostile.

This is the **"last mile" problem** — one of the hardest. The security of the entire election becomes dependent on the security hygiene of every voter's personal device.

### Problem 2: Authentication Without Impersonation

How do you confirm the person voting is actually who they claim to be? Without a universal digital identity infrastructure (which the US, UK, and most democracies do not have), this is extremely hard.

Options:
- **Knowledge factors** (username/password/date of birth) — easily stolen, shared, or socially engineered
- **Possession factors** (hardware tokens, e-ID cards) — require expensive national infrastructure
- **Biometrics** (facial recognition) — severe privacy concerns, can be spoofed

Estonia has a national e-ID card program built over 20 years — that's why they can attempt it. The US has 50 independent state voter rolls, no national ID, and deeply divided politics on identity. Even with strong authentication, credentials can be handed over under coercion.

### Problem 3: The Coercion / Vote-Buying Problem (Possibly Fundamental)

This is arguably the **deepest and most philosophically interesting barrier**. The secret ballot was invented specifically to prevent employers, landlords, political machines, and criminal organisations from purchasing or coercing votes. It works because there is no way to prove to a third party how you voted — the voting booth guarantees deniability.

Remote voting **structurally eliminates this guarantee**. A coercer can sit next to you. An employer can require you to share your screen. A domestic abuser can control your vote entirely. Unlike in-person voting, there is no physical separation from those who would pressure you.

**Emerging countermeasure**: Fake credential systems, where voters can generate a second indistinguishable set of credentials to hand to a coercer; votes cast with fake credentials are silently discarded. EPFL researchers have demonstrated prototypes. But if the coercer controls the voter's environment entirely and can prevent them from ever accessing a private channel, even this fails.

### Problem 4: Scale and the Targeted Attack Problem

Physical election attacks require local, physical presence. A remote internet election creates a **single logical target** for nation-state actors. A successful attack on central infrastructure could alter millions of votes simultaneously and leave no detectable trace.

The 2014 independent security analysis of Estonia's system found that researchers could "breach the system, change votes and vote totals, and erase all evidence of their actions" via server-side malware — exactly the capabilities a sophisticated nation-state adversary has.

### Problem 5: Denial of Service and Availability

Elections have immovable deadlines. A DDoS attack doesn't need to change any votes — it just needs to prevent enough people from casting them in a swing district at the right time. This is far simpler than ballot manipulation and is within the capabilities of criminal groups, let alone nation-states.

### Problem 6: Auditability and the Absence of a Paper Trail

The US and most democracies have converged on **risk-limiting audits** as their best defence — a statistical process of hand-counting paper ballots that can detect and bound the probability of undetected fraud. Paper ballots are difficult to alter at scale because they're physical, distributed, and independently observable.

Internet voting systems have no equivalent. Cryptographic audit trails exist (see E2E-V below), but they require sophisticated verification infrastructure that doesn't exist and that voters cannot independently validate by holding a ballot in their hands.

---

## 3. Real-World Failures and Experiments

### Estonia

The most-cited real-world example. Estonia has offered internet voting since 2005; approximately 50% of votes are now cast online. Enabled by a mandatory national e-ID card system in a small (1.3M voter) country with a highly digitally literate population.

**Yet independent security researchers have repeatedly found serious flaws:**
- The 2014 international security audit found the system vulnerable to vote manipulation and erasure by server-side attackers
- Post-2023 elections, OSCE/ODIHR observers concluded the system **does not actually provide end-to-end verifiability** despite official claims
- The architecture is fundamentally dependent on trust in the Estonian state's own servers

Estonia is presented as a success story — and in some narrow ways it is. But it succeeds largely because Estonia has specific preconditions (national e-ID, small population, high trust in government) that don't generalise to the US, UK, or most democracies.

### Norway

Ran internet voting pilots in 2011 and 2013. **Discontinued** due to security concerns and insufficient evidence of increased turnout.

### Voatz (USA, 2018–2020)

US mobile voting startup used in West Virginia, Denver, Utah, and other jurisdictions, primarily for military/overseas UOCAVA voters.

MIT 2020 security analysis found:
- Vulnerable to **passive attacks** exposing a voter's ballot
- **API server attacks** could suppress or alter votes without detection
- Exploitation "well within the capacity of a nation-state actor"

Independent audit by Trail of Bits upheld the key findings. The system was quietly discontinued in most jurisdictions.

### Blockchain Voting

Multiple startups have pitched blockchain as solving the trust problem. The academic consensus (Oxford Journal of Cybersecurity, 2021: *"Going from bad to worse: from Internet voting to blockchain voting"*) is that **blockchain solves none of the fundamental problems**:
- The uncontrolled endpoint problem is unchanged
- The coercion problem is unchanged
- The privacy model of most blockchains is antithetical to ballot secrecy
- Smart contract bugs are real and exploitable
- The "immutable ledger" means fraudulent votes can't even be removed after detection

---

## 4. Cryptographic Voting Systems: A Deep Dive

Despite the barriers documented in Sections 2-3, decades of cryptographic research have produced increasingly sophisticated approaches to verifiable, private, and coercion-resistant voting. This section maps the field: what exists, what works, what's deployed, and what remains theoretical. None of these systems solve all the problems simultaneously at national scale — but understanding them precisely is essential for knowing what's possible, what's close, and what's genuinely hard.

---

### 4.1 End-to-End Verifiable (E2E-V) Voting: The Core Framework

E2E-V is not a single system but a design philosophy: every voter can independently verify that the election outcome is correct, without trusting any single authority. An E2E-V system must provide three guarantees:

1. **Cast as intended** — the voter can verify that their device submitted the ballot they intended, not a modified version
2. **Recorded as cast** — the ballot appears on the public bulletin board (the election record) unchanged from what was submitted
3. **Tallied as recorded** — anyone can verify that the published tally correctly reflects all recorded ballots

The cryptographic building blocks that make this possible:

**Homomorphic encryption** allows mathematical operations on encrypted data. In voting, this means encrypted ballots can be *added together* without ever being decrypted individually. The election authority publishes the encrypted tally, then proves (via threshold decryption involving multiple independent trustees) that the decrypted total is correct. No individual ballot is ever exposed. The most commonly used schemes are exponential ElGamal (additively homomorphic, used in Helios and Belenios) and Paillier encryption. Fully homomorphic encryption (FHE) — which allows arbitrary computation on ciphertexts — exists theoretically (Gentry, 2009) but remains far too slow for real-time election use.

**Mix-networks (mix-nets)** provide an alternative anonymization pathway. Instead of adding encrypted ballots directly, each ballot passes through a chain of independent "mix servers." Each server cryptographically shuffles and re-encrypts the ballots it receives, then passes them to the next server. At the end of the chain, the ballots emerge in a random order with no link to the original voter. Each server publishes a zero-knowledge proof that its shuffle was performed correctly (no ballots added, removed, or altered). As long as *at least one* mix server is honest, voter privacy is preserved.

**Zero-knowledge proofs (ZKPs)** are the verification glue. A ZKP allows a party to prove a statement is true without revealing any information beyond the statement itself. In E2E-V systems, ZKPs prove that: (a) each encrypted ballot contains a valid vote (e.g., exactly one candidate selected, not two), (b) each mix-net shuffle was performed correctly, (c) the threshold decryption of the final tally was done honestly, and (d) the final count matches the recorded ballots. The most common ZKP constructions used in voting are Schnorr proofs, Chaum-Pedersen proofs, and more recently, Sigma protocols and SNARKs/STARKs for more complex statements.

**The verification model**: After the election, the entire cryptographic transcript — encrypted ballots, mix-net proofs, tally proofs — is published. Any technically capable observer (a university, a political party, a civic organization, a motivated individual with the right software) can independently re-verify every proof. This is the key insight: you don't need to trust the election authority because you can check their work. The election authority can cheat only by breaking the underlying cryptographic assumptions — which, for current schemes, would require solving problems believed to be computationally infeasible (discrete logarithm, factoring).

**What E2E-V does NOT solve**: Cast-as-intended verification in the remote setting remains the weakest link. In a polling place, techniques like Benaloh challenges (the voter can choose to "challenge" the encryption of their ballot, revealing it to verify correctness, then cast a fresh one) provide strong cast-as-intended guarantees. Remotely, the voter's device is untrusted — malware can display one thing and encrypt another. The "cast as intended" guarantee degrades to: you can verify *what was received by the server*, but not that your device sent what you told it to. This is the endpoint problem from Section 2, restated in cryptographic terms.

---

### 4.2 Deployed E2E-V Systems: What Actually Exists

**Helios** (2008, Ben Adida, Harvard/MIT). The first practical E2E-V system. Uses homomorphic tallying with exponential ElGamal encryption. Deployed for: IACR board elections (the International Association for Cryptologic Research — cryptographers voting with their own tools), Princeton University student government, Université Catholique de Louvain, and several other university elections. Helios is open-source, browser-based, and deliberately simple. Its threat model explicitly excludes coercion resistance — Helios provides a receipt that lets the voter verify their vote was counted, but that receipt could also be shown to a coercer. Helios also does not provide eligibility verifiability — a corrupt election authority could add fake voters. Despite these limitations, Helios demonstrated that E2E-V could work in practice with real voters, not just in papers. The IACR has used it for over 15 years without incident.

**Belenios** (INRIA, France, 2013-present). Extends Helios with eligibility verifiability: independent registrars issue credentials, and the published record allows anyone to verify that only credentialed voters' ballots are included. Uses a distributed trust model — the ballot box, credential authority, and decryption trustees are independent parties, and the system is secure as long as they don't all collude. Belenios has been used for: French CNRS committee elections, multiple French university elections, and various organizational votes. It is actively maintained, open-source, and has formal security proofs (Cortier, Galindo, et al., published in Journal of Computer Security and IEEE S&P). Belenios is currently the most rigorously analyzed deployed E2E-V system.

**Microsoft ElectionGuard** (2019-present). The most significant industry effort. ElectionGuard is an open-source SDK that adds E2E-V to existing in-person voting systems. It does not replace voting machines — it augments them. The voter uses a standard ballot-marking device; ElectionGuard encrypts a copy of the ballot and provides a verification code. After the election, an independent verifier (anyone with the software) can check the encrypted record against the published tally. Key deployments:
- Fulton, Wisconsin (February 2020): First binding public election using ElectionGuard, in a Spring primary. Voters received verification codes; independent verification confirmed the tally.
- Hart InterCivic partnership (2020-2022): Integration with a major commercial voting system vendor.
- Idaho (2022 pilot): ElectionGuard integrated with Hart Verity voting machines for a primary election.
- College Park, Maryland (2023): Municipal election pilot.

ElectionGuard's approach is pragmatic: it doesn't attempt to solve the remote voting problem. It adds cryptographic verifiability to the existing in-person, paper-ballot ecosystem. The paper ballot remains the ground truth; ElectionGuard provides an additional, independent verification layer. This sidesteps the endpoint problem entirely (the "endpoint" is a controlled polling-place machine) and the coercion problem (the voter is in a booth). It is the most deployment-ready E2E-V technology and the most relevant to the near-term recommendations in this report.

**Scytl/PODEMOS (Spain)** and **SwissPost/CHVote (Switzerland)**. Scytl provided E2E-V internet voting for Swiss cantonal elections and Spanish political party primaries. The Swiss system (CHVote) was one of the most sophisticated deployed internet voting systems, using mix-nets and ZKPs. In 2019, independent researchers discovered a critical flaw in Scytl's cryptographic protocol: the shuffle proof could be manipulated to alter votes undetectably — exactly the scenario E2E-V is supposed to prevent. SwissPost suspended the system pending a complete rewrite. This is the most important cautionary tale in the E2E-V space: even systems designed by specialists, with formal security claims, can have implementation bugs that break the core guarantees. The CHVote rewrite (now in progress) uses formally verified code for the cryptographic core — a direct response to the lesson.

**Prêt à Voter and vVote (Australia)**. Prêt à Voter (2004, Peter Ryan, University of Luxembourg) uses a physical paper ballot with a randomized candidate order, printed in a polling place. The voter marks the ballot, tears off the candidate list, and feeds only the marked portion into a scanner. The randomization is generated and verified cryptographically. vVote was deployed for the 2014 Victorian state election in Australia — the only E2E-V system used in a state-level government election. It handled approximately 1,200 voters at supervised polling places. The system worked correctly but was expensive to operate and was not continued for subsequent elections.

---

### 4.3 Coercion Resistance: The Deepest Unsolved Problem

The secret ballot exists to prevent vote buying and coercion. In a polling place, no one can observe your vote — you have plausible deniability. Remote voting structurally breaks this. Cryptographic coercion resistance aims to restore it, and is the hardest open problem in the field.

**The JCJ/Civitas Protocol** (Juels, Catalano, Jakobsson, 2005; extended as Civitas by Clarkson, Chong, Myers, 2008). The foundational theoretical framework. Each voter receives a real credential and can also generate unlimited fake credentials that are cryptographically indistinguishable from real ones. A vote cast with a fake credential is silently discarded during tallying. If a coercer demands to watch you vote, you use a fake credential. The coercer sees what appears to be a valid vote submission and has no way to determine whether the credential was real.

**Why JCJ/Civitas hasn't been deployed:**
- **Computational cost**: The tallying phase requires comparing every submitted ballot against every credential to separate real from fake — this is quadratic in the number of voters. For a national election with 150 million potential voters, this is computationally prohibitive with current technology.
- **Credential distribution**: The voter must receive their real credential through a private, authenticated channel that the coercer cannot observe. If the coercer controls the voter's entire environment (domestic abuse, captive workforce), no such channel exists.
- **Usability**: The voter must understand and execute a fake-credential protocol under pressure. Behavioral studies suggest this is unreliable.
- **The "forced abstention" problem**: Even if the coercer can't determine how you voted, they can prevent you from reaching a private channel to vote with your real credential at all. JCJ addresses vote *manipulation* coercion but not vote *suppression* coercion.

**Selene** (2015, Peter Ryan). A different approach: instead of hiding the vote, Selene provides a "tracking number" that lets the voter verify their vote appeared correctly on the public bulletin board, but with a twist — the tracking number is computed in a way that a coercer cannot link the tracking number to the voter. The voter receives their tracking number through a private channel after the election. If a coercer forces the voter to reveal the tracking number, the voter can claim a different number (which will point to a different, random vote). The coercer cannot verify whether the number is real. This is weaker than JCJ (the voter can verify but the coercer might force the voter to check in their presence) but much more practical.

**zkVoting** (2024, IACR ePrint 2024/1003). The most recent significant proposal. Combines ZKPs with a JCJ-like credential scheme, using lattice-based cryptography (post-quantum secure). Key advance: uses zero-knowledge proofs to make the credential validation more efficient, reducing the quadratic tallying cost. Also integrates with mix-nets for privacy. Still a paper proposal — no deployment, no implementation performance data at scale.

**EPFL coercion-resistance research** (Hirt, Sako; Haenni, Dubuis, EPFL). Swiss researchers have been working on protocols that combine deniable encryption with fake-credential schemes. Their 2023 paper demonstrated a protocol that achieves both coercion resistance and cast-as-intended verifiability simultaneously — previously considered very difficult. Published in ScienceDirect with formal proofs. No deployment.

**The honest assessment**: After 20 years of research, coercion resistance remains theoretical for remote voting at scale. Every proposed protocol requires either a private channel between the voter and the system (which a determined coercer can eliminate), or computational costs that don't scale to national elections, or both. In-person voting solves coercion resistance trivially (the booth) and no cryptographic protocol has matched that simplicity. This is the strongest argument for the hybrid model: use cryptography for the counting and verification layers, but keep the casting layer physical.

---

### 4.4 Risk-Limiting Audits: The Statistical Bridge

Risk-limiting audits (RLAs) are not cryptographic, but they are the practical verification mechanism that complements E2E-V systems and provides the strongest current guarantee for in-person elections. Understanding them is essential because the cryptographic systems above are not yet ready for high-stakes elections — RLAs are the bridge.

**How they work**: After an election, a small, statistically determined random sample of paper ballots is hand-counted. If the sample confirms the electronic tally, the audit stops. If discrepancies appear, the sample is enlarged — up to a full hand count if necessary. The "risk limit" is the maximum probability that an incorrect outcome survives the audit (typically set at 5% or 10%). RLAs were developed by Philip Stark (UC Berkeley, 2008) and have rigorous statistical foundations.

**Current deployment**: Colorado became the first state to mandate RLAs statewide in 2017. As of 2025, approximately 12 states have adopted or piloted RLAs. The method has been endorsed by the American Statistical Association, the National Academies, and CISA.

**The connection to E2E-V**: RLAs verify the *paper record* against the *electronic count*. E2E-V verifies the *electronic record* against the *cryptographic transcript*. Together, they create a two-layer verification system: the cryptography guarantees the electronic layer is honest, the RLA guarantees the paper layer matches. This is why ElectionGuard's approach — adding E2E-V on top of existing paper-ballot systems that already support RLAs — is the most deployable near-term path. The voter doesn't need to understand the cryptography. The paper ballot remains the primary evidence. The cryptography provides an additional, independent check.

**Limitation**: RLAs require paper ballots. They cannot be applied to fully electronic or internet voting systems where no physical artifact exists. This is a fundamental reason why the in-person, paper-ballot model remains the most auditable.

---

### 4.5 Post-Quantum Cryptography: The Looming Transition

Every deployed E2E-V system relies on the hardness of the discrete logarithm or factoring problem. A sufficiently powerful quantum computer could break these in polynomial time (Shor's algorithm). This is not yet a practical threat — the largest quantum computers as of early 2026 have approximately 1,000-1,200 qubits, while breaking the cryptography used in voting systems would require millions of error-corrected qubits. But election records are public and persistent: encrypted ballots published today could be stored by an adversary and decrypted decades later when quantum computers mature ("harvest now, decrypt later"). For elections, this means:

- **Voter privacy has a time horizon.** An encrypted ballot published in 2026 could be decrypted in 2040 or 2050. Whether this matters depends on the election — a 2026 House race decrypted in 2050 has limited coercive or blackmail value, but the principle matters for institutional trust.
- **The transition to post-quantum cryptography is underway.** NIST finalized its first post-quantum cryptographic standards in August 2024: ML-KEM (Kyber) for key encapsulation and ML-DSA (Dilithium) for digital signatures, both lattice-based. These are being integrated into TLS, SSH, and other protocols. Voting systems will need to migrate — but the timeline is not urgent. The most prudent approach is to use hybrid encryption (classical + post-quantum) for new deployments, ensuring security against both classical and quantum adversaries.
- **Lattice-based ZKPs** are being developed specifically for voting applications. The 2024 Journal of Cryptology paper on lattice-based ZKPs for electronic voting (Springer) demonstrates that the core verification machinery of E2E-V systems can be rebuilt on post-quantum foundations. Performance is worse than classical ZKPs (proofs are larger, verification is slower) but within feasibility for election-scale applications.
- **zkVoting's lattice-based approach** (Section 4.3) is explicitly designed to be post-quantum secure, combining lattice-based ZKPs with coercion-resistant credential schemes.

The practical implication: post-quantum cryptography is a migration challenge, not a fundamental threat. The voting research community is already building the necessary tools. Any new E2E-V deployment should plan for the transition, but existing systems are not immediately vulnerable.

---

### 4.6 Formally Verified Implementations: Closing the Gap Between Theory and Code

The SwissPost/CHVote debacle (Section 4.2) demonstrated that a cryptographic protocol can be correct on paper and broken in implementation. The response has been a push toward formally verified voting software — code that is mathematically proven to implement the protocol correctly.

**CHVote 2.0** (SwissPost, in development). The rewrite of the Swiss internet voting system uses formally verified cryptographic components. The shuffle proofs — exactly where the 2019 bug was found — are implemented with machine-checked proofs of correctness.

**Belenios formal verification** (INRIA). The Belenios team has published machine-checked proofs (using the Coq proof assistant) that the core protocol provides ballot privacy and verifiability under stated assumptions. This is among the strongest formal guarantees in any deployed voting system.

**EasyVote/Verificatum** (Douglas Wikström, KTH Stockholm). Verificatum is a mix-net library with a formally specified interface, designed specifically for voting. It has been used in Norwegian and Estonian election infrastructure. While not fully formally verified at the implementation level, it has undergone extensive independent security review.

**The gap**: Formal verification proves that code correctly implements a protocol. It does not prove that the protocol itself captures all real-world threats. The endpoint problem, coercion, and institutional trust are outside the formal model. Formal verification eliminates implementation bugs — a real and serious source of failures — but does not substitute for the governance and institutional analysis in Section 10 of this report.

---

### 4.7 The Maturity Spectrum: What's Deployable and What's Not

| Technology | Maturity | Deployed At | Solves |
|---|---|---|---|
| **Risk-limiting audits** | Production-ready | 12+ US states | Paper-electronic consistency |
| **ElectionGuard (in-person E2E-V)** | Pilot-ready | Fulton WI, Idaho, College Park MD | Verifiable in-person tallying |
| **Belenios (online E2E-V)** | Operational for low-stakes | CNRS, universities | Verifiable online tallying + eligibility |
| **Helios (online E2E-V)** | Operational for low-stakes | IACR, universities | Verifiable online tallying (no eligibility) |
| **Prêt à Voter / vVote** | Demonstrated | Victorian state election 2014 | In-person E2E-V with paper |
| **Mix-net libraries (Verificatum)** | Production component | Norwegian/Estonian infra | Anonymization layer |
| **JCJ/Civitas coercion resistance** | Theoretical | None at scale | Coercion resistance (quadratic cost) |
| **Selene (post-election verification)** | Prototype | Small-scale demos | Voter-verifiable, partial coercion resistance |
| **zkVoting (lattice-based)** | Paper only | None | Post-quantum coercion resistance |
| **Fully remote E2E-V + coercion-resistant** | Theoretical | None | Everything (nothing deployable) |

**The honest summary**: The cryptographic counting layer is solved and deployable. E2E-V for in-person voting is ready for wider adoption — ElectionGuard demonstrates this. E2E-V for online voting works for low-stakes elections where coercion resistance is less critical (organizational elections, union votes). Coercion resistance at scale remains unsolved. The endpoint problem (trusted device) remains unsolved. Post-quantum migration is underway and manageable.

The practical path is not to wait for the complete solution. It is to deploy what works now — RLAs and in-person E2E-V — while continuing research on the harder problems. Each layer of cryptographic verification added to the existing system makes it harder to cheat undetectably, even if no single layer provides a complete solution.

---

### 4.8 Hybrid Models: The Most Pragmatic Near-Term Path

Given the maturity spectrum above, the most viable near-term architecture combines:

1. **Paper ballots** for the casting layer — preserving the physical audit trail and coercion resistance of the voting booth
2. **E2E-V encryption** (ElectionGuard or similar) for the counting layer — adding cryptographic verifiability on top of paper
3. **Risk-limiting audits** for the statistical verification layer — confirming paper and electronic records agree
4. **Remote ballot *marking*** (not casting) for accessibility — voters with disabilities or overseas voters mark a ballot electronically, print it, and submit it physically

This three-layer model — paper + cryptography + statistical audit — provides stronger guarantees than any single method alone. It doesn't solve remote casting, but it makes in-person and mail voting significantly more trustworthy and transparent. It is deployable today with existing technology, does not require new infrastructure, and can be incrementally adopted jurisdiction by jurisdiction.

For full remote casting to become viable, the field needs breakthroughs in:
- **Coercion resistance at scale** — bringing JCJ-class protocols to practical performance
- **Trusted endpoints** — hardware attestation, trusted execution environments, or government-issued voting devices
- **Digital identity infrastructure** — a prerequisite analyzed in Sections 8 and 10 of this report

Until those breakthroughs arrive, the hybrid model is the strongest achievable posture.

---

## 5. Can It Be Open Source and Secure?

**Yes — and in fact, for any system to be trustworthy, open source is a prerequisite, not a risk.**

The security community is unambiguous: security through obscurity is not security. You cannot have credible independent verification of a system whose source code is hidden.

**VotingWorks** is the leading US example — a nonprofit building open-source election software, currently deployed in several states. Their code is publicly auditable, and their bids come in at roughly 50% of proprietary vendor prices.

**Nuances:**

| Concern | Reality |
|---|---|
| Supply chain risk | Open source reduces but doesn't eliminate it. Requires reproducible builds and independent build verification. Same problem exists (hidden) in proprietary systems. |
| Vulnerability disclosure | Bugs visible to adversaries during patch window. Mitigant: bug bounty, rapid response, transparent disclosure — same model that secures TLS, SSH, etc. |
| Transparency vs. legitimacy | The current system (proprietary, trade-secret-shielded) *actively generates* the information environment that conspiracy theories require. Open source removes that oxygen. |

The NIST/EAC certification process would need to adapt to properly validate open-source deployments rather than treating open code as a liability.

**Open source is necessary but not sufficient.** It is the floor, not the ceiling.

---

## 6. Political, Legal, and Organisational Barriers

**Fragmented jurisdiction**: In the US, elections are run by approximately 10,000 independent jurisdictions. There is no federal election administration. Any national solution requires either federal mandate (politically fraught) or 50-state adoption (practically impossible). Estonia has one national system run by one national body.

**Incumbent protection dynamics**: Higher-turnout systems tend to disfavour incumbents and established parties. Internet voting, by lowering participation costs, would likely increase turnout among younger, more mobile, and more disadvantaged voters. There is no lobbying constituency pushing for this change from within power structures.

**Proprietary vendor lock-in**: The existing election technology industry (Dominion, ES&S, Hart InterCivic) sells proprietary, certified equipment on long contracts. The VSTL certification pipeline is slow and expensive — VotingWorks has been working for years to navigate it. Structural inertia is substantial.

**Legal frameworks lag technology**: UOCAVA (1986) was written before the internet. HAVA (2002) created certification processes designed for physical machines. Amending these requires Congressional action in a deeply polarised environment.

**Trust deficit cuts both ways**: In the current US political environment, any new voting technology will be immediately attacked as fraudulent by the losing side. This creates a perverse incentive to keep systems as simple and paper-based as possible — a technically correct but politically motivated position.

**Countries that pulled back**: The Netherlands, Ireland, Germany, and the United Kingdom have all cancelled e-voting systems or decided against large-scale rollout due to reliability or transparency concerns.

---

## 7. The Legitimate Pressure for Remote Voting

The argument isn't purely theoretical — there are real constituencies for whom current systems fail:

- **Military/overseas voters (UOCAVA)**: Voters in combat zones or with poor mail service may have no realistic alternative. 31 states and DC already allow select electronic return for UOCAVA voters and voters with disabilities.
- **Voters with disabilities**: Current in-person accessibility solutions are inconsistent; remote accessible ballot marking could enable independent private voting for voters who currently need assistance.
- **Young and mobile voters**: Geographic mobility, lack of established residency, and lower civic integration all correlate with lower turnout. Lower participation friction could counteract this.

These are real democratic access problems. The answer isn't to dismiss them — it's to solve them with the least security cost, which currently means accessible ballot *marking* systems paired with mail or in-person *casting*, not full remote casting.

---

## 8. What Would Actually Be Required

For fully remote electronic voting to be deployable at national scale with acceptable security, the following conditions would need to be met **simultaneously**:

1. **Solved endpoint problem**: Trusted execution environments, hardware attestation, or universally available secure voting devices. Likely requires government-issued voting hardware or a radically different device security model.

2. **Universal digital identity infrastructure**: A national, privacy-preserving digital identity system. Estonia spent 20 years building this. The US has not started.

3. **Mature E2E-V deployment**: Battle-tested, independently audited, open-source E2E-V systems deployed in progressively higher-stakes elections over a decade. Currently viable only for institutional/union elections.

4. **Coercion resistance at scale**: Fake credential systems or equivalent, proven effective against state-level coercive actors. Currently theoretical/prototype.

5. **Redundant, DDoS-resistant infrastructure**: Election-specific, geographically distributed, hardened infrastructure with verifiable availability guarantees. Does not currently exist.

6. **Legislative and regulatory framework**: Modernised UOCAVA and HAVA, updated VVSG standards incorporating E2E-V requirements, reformed certification pipeline.

7. **Long-term public trust building**: Gradual rollout in low-stakes elections (union elections, party primaries, institutional governance) with independent audits and transparent results, building a decade-long evidentiary record.

---

## 9. A Realistic Path Forward

The barriers to remote electronic voting are **not primarily political** — they are deeply technical, and the hardest ones (coercion resistance, endpoint trust) may be fundamentally unsolvable without infrastructure that doesn't exist and will take decades to build.

A realistic path:

1. **Open-source the existing in-person system** — VotingWorks / TrustTheVote model. Do this now.
2. **Expand E2E-V cryptographic techniques to in-person and mail voting systems** — verifiability without full internet exposure.
3. **Build national digital identity infrastructure** for other purposes; voting can piggyback once it exists.
4. **Deploy internet voting only for specific narrow use cases** (UOCAVA overseas military, severe disability) where the participation stakes outweigh the security tradeoffs — with full public transparency about those tradeoffs.
5. **Fund 10–20 years of graduated deployment** in progressively higher-stakes institutional elections to build an evidence base.

---

## 10. The "Who Is a Voter?" Problem: How the April 2026 Legal Environment Changes Everything

*Added April 11, 2026. This section connects the voting technology analysis above with the constitutional litigation documented in `litigation-tracker-2026.md` and the crisis assessment in `us-democracy-crisis-analysis-2026.md`.*

---

Sections 1–9 of this report treat voter eligibility as a stable predicate — a known, settled input to the voting system design problem. The technical question has been: given a defined set of eligible voters, how do you build a system that authenticates them, records their votes, and counts them securely?

As of April 2026, this assumption is breaking down. The legal definition of "who is a voter" is itself under active litigation, and the institutional mechanisms for enforcing voting rights are degrading faster than any voting technology can compensate for. This section analyzes why this matters for the entire e-voting research program.

### 10.1 Trump v. Barbara: The Citizenship Predicate Under Attack

The Fourteenth Amendment's Citizenship Clause — "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States" — has been understood since United States v. Wong Kim Ark (1898) to guarantee birthright citizenship to virtually everyone born on U.S. soil, regardless of their parents' immigration status.

Trump's January 20, 2025 executive order directly challenged this, purporting to strip citizenship from children born to parents present unlawfully or temporarily. Every federal court that ruled on the merits blocked the order. The Supreme Court heard oral argument on April 1, 2026 (Trump v. Barbara, No. 25-365), with a decision expected by late June or early July 2026.

**Why this matters for voting technology:**

Every voting system — paper, electronic, or hybrid — depends on a voter roll: a list of eligible voters. That list is compiled from citizenship records, which are themselves derived from birth certificates, naturalization records, and the legal rules governing who counts as a citizen. If the Supreme Court narrows the meaning of "subject to the jurisdiction thereof," several consequences follow:

1. **Retroactive eligibility uncertainty.** A ruling that some classes of U.S.-born persons are not citizens would create an unknown population of people who were on voter rolls, may have voted in prior elections, and whose eligibility is now contested. No voting system — electronic or otherwise — can handle a retroactive redefinition of its own eligibility database. The technical problem is not authentication (proving you are who you claim to be) but authorization (proving you are entitled to vote at all), and the authorization rules would have just changed under the feet of every existing system.

2. **Verification infrastructure doesn't exist.** The U.S. has no national citizenship registry. Citizenship is currently inferred from birth certificates (for native-born citizens) or naturalization records (for naturalized citizens). A narrowed birthright citizenship rule would require determining, at the point of voter registration or voting, whether each voter's parents were citizens, lawful permanent residents, or otherwise "subject to the jurisdiction" of the United States at the time of the voter's birth. This requires accessing parental immigration status records — records that may not exist, may be in DHS databases that state election officials cannot access, or may be decades old. The authentication infrastructure gap identified in Section 2 (Problem 2) of this report would expand dramatically: you would need not just a digital identity system for voters, but a linked parental immigration status verification system reaching back to the voter's date of birth.

3. **Contested eligibility becomes a vector for suppression.** Even a partial ruling — say, one that technically narrows birthright citizenship only for children of parents with no lawful status — would create a chilling effect. Voters who are in fact citizens but whose parents' immigration history is complex, undocumented, or ambiguous would face challenges at the registration stage. In an electronic voting system, this challenge would need to be adjudicated before a ballot is issued — and the adjudication mechanism does not exist. In a paper system with provisional ballots, the voter at least gets a provisional ballot that can be counted later; in a remote electronic system, the equivalent would require a real-time eligibility determination pipeline that connects voting infrastructure to immigration databases. This is the exact kind of large-scale identity infrastructure that Section 8 (Condition 2) of this report identified as a 20-year project. A narrowed citizenship ruling would make it not just desirable but legally necessary — and would make it a tool of exclusion rather than inclusion.

4. **The "who decides" problem.** Currently, voter eligibility challenges in most states are handled by county election officials with appeal to state courts. A contested citizenship definition would federalize the eligibility question — only federal courts can interpret the Fourteenth Amendment. Any electronic voting system that needs to authenticate voters against a citizenship standard would need to integrate with a federal eligibility determination pipeline that does not exist and would require federal legislation, interagency data sharing agreements, and a judicial adjudication framework for real-time disputes. The governance complexity alone makes this a decade-long project.

**Bottom line:** The entire e-voting research program — from Section 2's authentication analysis through Section 8's deployment prerequisites — implicitly assumes that voter eligibility is defined, stable, and knowable. Trump v. Barbara threatens all three of those assumptions. A ruling in the administration's favor would not merely add a new authentication requirement; it would destabilize the foundational layer beneath every other technical problem this report identifies.

### 10.2 The Compliance Crisis and Institutional Trust

The April 2026 litigation environment reveals a second problem that compounds the first: the institutions responsible for administering elections and enforcing voting rights are themselves in crisis.

**Compliance litigation as a category.** The litigation tracker documents a new pattern as of April 2026: courts issuing orders that the executive branch does not fully obey. Ramirez Ovando v. Noem required evidentiary hearings about whether ICE was complying with a federal injunction. Judge Jackson heard testimony from ICE officers about internal compliance (or non-compliance) with court orders. This is not an isolated incident — it is becoming a recognized pattern across multiple federal agencies.

For voting infrastructure, this matters because:

- Any electronic voting system is, at bottom, a compliance system. It enforces rules: who can vote, where they can vote, how many times, whether their ballot counts. If the institutions responsible for defining and administering those rules are themselves in a compliance crisis — if federal agencies are not reliably obeying court orders about who is entitled to what — then the rules the voting system enforces may not be the rules the courts have actually set.

- The voting system cannot be more trustworthy than the institutional environment it operates within. Estonia's i-voting works (to the extent it does) because Estonian citizens have high trust in their government and a national identity infrastructure maintained by a reliable state. The April 2026 U.S. environment is one where federal agencies have been caught providing "patently false information" to courts (the Fourth Circuit's characterization in the AFSCME v. SSA proceedings), where DOGE shared federal data with unnamed political advocacy groups, and where the administration's stated position in multiple cases is that executive actions are unreviewable. In this environment, deploying an electronic voting system that depends on federal databases for authentication is not a technical risk — it is a governance risk. The database you are authenticating against may have been compromised or politically manipulated.

**The shadow docket and voting rights.** Justice Sotomayor flagged in April 2026 that the Supreme Court had issued approximately 25 emergency-docket rulings since January 2025, approximately 20 of which favored the administration. The shadow docket — emergency orders issued without full briefing, oral argument, or written opinions — has become the primary mechanism for resolving contested legal questions, including voting rights questions. The Texas redistricting stay (LULAC v. Abbott) is a direct example: the Supreme Court stayed a lower court ruling that found a congressional map was an illegal racial gerrymander, ensuring that the contested map would be used for the 2026 midterms. The stay was issued without a merits opinion.

For the e-voting research program, this means:

- **Voting rules are changing faster than systems can adapt.** A shadow-docket stay can change the effective legal status of a congressional map, voter ID requirement, or eligibility standard overnight. An electronic voting system needs stable rules to implement. When the rules themselves are unstable — subject to emergency-docket modification weeks before an election — no system, electronic or paper, can guarantee that voters are voting under the rules they were told applied.

- **Auditability requires stable law.** Section 6 of this report discusses the auditability problem for electronic voting. But auditability assumes you know what the correct outcome should be — which requires stable, agreed-upon rules for who voted, where, and whether their ballot counted. When the legal environment is in flux, the audit standard itself is contested. A risk-limiting audit can tell you whether the paper count matches the electronic count, but it cannot tell you whether the rules applied to determine eligibility were the rules the courts intended, if those rules changed between the start and end of voting.

### 10.3 Implications for the Realistic Path Forward

Section 9 of this report laid out a five-step realistic path for remote electronic voting. The April 2026 developments require amending that path:

**Step 1 (open-source the existing system) becomes more urgent, not less.** When institutional trust is low and the legal environment is contested, transparency is the only credible substitute. VotingWorks and TrustTheVote's open-source model is more important in April 2026 than it was in April 2025 — not because the technology changed, but because the trust environment degraded. Open source doesn't solve the "who is a voter" problem, but it at least ensures that the rules the system is implementing are publicly verifiable.

**Step 2 (E2E-V for in-person and mail voting) is unchanged.** Cryptographic verifiability is orthogonal to the eligibility question — it proves the count is honest, regardless of how eligibility is defined.

**Step 3 (national digital identity infrastructure) is now politicized beyond the technical analysis.** In April 2025, a national digital identity system was a 20-year infrastructure project. In April 2026, it is also a political flashpoint. Any identity system that connects to immigration databases — which a post-Barbara citizenship verification system would require — becomes a tool of the administration's immigration enforcement agenda. Estonia's e-ID works because it serves all citizens equally and is not entangled with enforcement. A U.S. digital identity system built in the current environment would inherit the political toxicity of immigration enforcement, voter ID laws, and the citizenship question itself. This doesn't make it technically impossible, but it makes the governance design vastly harder. The identity system would need to be constitutionally firewalled from enforcement agencies, operated by an independent body with protected tenure, and subject to judicial review at every data-sharing point. None of this exists or has been proposed.

**Step 4 (narrow remote voting for UOCAVA/disability) may need to be paused.** The 31 states that currently allow some form of electronic ballot return for overseas military voters are operating on the assumption that citizenship verification for military personnel is straightforward (it is — military service records establish citizenship). But if Trump v. Barbara is decided broadly, even military voter eligibility could become contested for service members born in the U.S. to noncitizen parents. This is a small population, but it illustrates how a citizenship definition change radiates into every subsystem.

**Step 5 (graduated deployment over 10-20 years) needs a prerequisite that didn't exist before: legal stability.** The original analysis assumed that the legal framework would evolve slowly and predictably. The April 2026 environment shows the opposite: legal rules governing voting are changing rapidly, unpredictably, and through procedural mechanisms (shadow docket, emergency stays) that bypass the deliberative process. Deploying e-voting infrastructure in this environment is like building on a fault line. The technology may work perfectly and still fail because the legal ground shifted beneath it.

### 10.4 The Deeper Lesson: Voting Technology Cannot Outrun Institutional Decay

The original report (Sections 1-9) framed remote electronic voting as primarily a technical problem with political complications. The April 2026 analysis inverts that framing: **remote electronic voting is primarily a governance problem that happens to have technical components.**

The technical barriers identified in Section 2 — endpoint trust, authentication, coercion resistance, scale, availability, auditability — are all real and all unsolved. But even if every one of them were solved tomorrow, deploying e-voting in April 2026 America would fail, because:

- The definition of "eligible voter" is under active Supreme Court challenge
- The federal agencies responsible for citizenship and immigration records have been caught lying to courts
- Voting rights protections are being modified via emergency orders without full legal process
- The executive branch has demonstrated willingness to defy court orders
- Federal data has been shared with political advocacy groups without authorization

No cryptographic protocol can compensate for an institutional environment where the entities responsible for defining and enforcing eligibility rules are themselves compromised. E2E-V can guarantee that a ballot was counted as cast, but it cannot guarantee that the voter should have been allowed to cast it, or that the rules determining who can vote are the rules the courts intended, or that the database used for authentication has not been politically manipulated.

This is not an argument against the e-voting research program. It is an argument that the research program must be embedded within the broader democratic renewal framework (`democratic-renewal-proposal.md`). Electoral reform (Domain 1), institutional integrity (Domain 2), and digital government infrastructure (Domain 4) are prerequisites, not parallel tracks. You cannot build trustworthy voting technology on top of untrustworthy institutions.

The practical implication: the "realistic path forward" from Section 9 should be understood as contingent on the broader institutional repair agenda. If institutional integrity is restored — civil service independence, judicial compliance, data protection, stable legal frameworks — then the 15-20 year e-voting roadmap is plausible. If it is not, the roadmap is irrelevant, because the governance preconditions for any voting system, paper or electronic, will have been undermined.

---

## Key Actors & Resources

| Organisation | Role |
|---|---|
| [VotingWorks](https://www.votingworks.org/) | Leading US open-source election software nonprofit |
| [TrustTheVote](https://trustthevote.org/) | Open-source election infrastructure initiative |
| [Verified Voting](https://verifiedvoting.org/) | Advocacy for paper-backed, auditable election systems |
| [CITP Princeton](https://citp.princeton.edu/) | Leading academic election security research |
| [INRIA / Belenios](https://www.belenios.org/) | Leading E2E-V cryptographic voting research (France) |
| [IACR](https://iacr.org/) | International cryptography research; runs its own E2E-V elections |
| [EAC](https://www.eac.gov/) | US Election Assistance Commission (certification body) |
| [Brennan Center](https://www.brennancenter.org/election-security) | Election security policy and legal advocacy |
| [EPIC](https://epic.org/issues/cybersecurity/election-security/) | Digital rights and election security advocacy |

---

## Sources

- [Internet voting is insecure and should not be used in public elections — CITP Princeton (Jan 2026)](https://blog.citp.princeton.edu/2026/01/16/internet-voting-is-insecure-and-should-not-be-used-in-public-elections/)
- [Internet or Online Voting Remains Insecure — AAAS](https://www.aaas.org/epi-center/internet-online-voting)
- [Internet Voting FAQ — Verified Voting](https://verifiedvoting.org/internet-voting-faq/)
- [Going from bad to worse: from Internet voting to blockchain voting — Oxford Journal of Cybersecurity](https://academic.oup.com/cybersecurity/article/7/1/tyaa025/6137886)
- [Security Analysis of the Estonian Internet Voting System — ACM CCS 2014](https://dl.acm.org/doi/10.1145/2660267.2660315)
- [Independent Report on E-voting in Estonia](https://estoniaevoting.org/)
- [Electronic voting in Estonia — Wikipedia](https://en.wikipedia.org/wiki/Electronic_voting_in_Estonia)
- [A Security Analysis of Voatz — MIT Internet Policy Research Initiative](https://internetpolicy.mit.edu/wp-content/uploads/2020/02/SecurityAnalysisOfVoatz_Public.pdf)
- [MIT researchers identify security vulnerabilities in Voatz — MIT News](https://news.mit.edu/2020/voting-voatz-app-hack-issues-0213)
- [Making e-voting safer from coercion and vote buying — EPFL](https://actu.epfl.ch/news/making-e-voting-safer-from-coercion-and-vote-buyin/)
- [On remote electronic voting with both coercion resistance and cast-as-intended verifiability — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2214212623001382)
- [zkVoting: ZKP-based coercion-resistant and E2E verifiable — IACR ePrint 2024](https://eprint.iacr.org/2024/1003.pdf)
- [End-to-end auditable voting — Wikipedia](https://en.wikipedia.org/wiki/End-to-end_auditable_voting)
- [Belenios: Verifiable Online Voting System — INRIA](https://www.belenios.org/)
- [Helios Voting — Wikipedia](https://en.wikipedia.org/wiki/Helios_Voting)
- [How open source voting machines could boost trust in US elections — MIT Technology Review (2024)](https://www.technologyreview.com/2024/03/07/1089524/open-source-voting-machines-us-elections/)
- [Open-Source Software Won't Ensure Election Security — Lawfare](https://www.lawfaremedia.org/article/open-source-software-wont-ensure-election-security)
- [A Transparent, Open-Source Vision for U.S. Elections — Undark (2024)](https://undark.org/2024/02/28/open-source-voting/)
- [Voter Authentication in Remote Electronic Voting — Springer](https://link.springer.com/chapter/10.1007/978-3-031-23213-8_1)
- [Accessibility and Usability Considerations for UOCAVA Remote Electronic Voting — EAC](https://www.eac.gov/documents/2017/03/17/accessibility-and-usability-considerations-uocava-remote-electronic-voting)
- [Proving vote correctness in the IVXV internet voting system — Nature Scientific Reports (2025)](https://www.nature.com/articles/s41598-025-16764-1)
- [Risks of E-voting — David Wagner, UC Berkeley / CACM 2007](https://people.eecs.berkeley.edu/~daw/papers/risks-cacm07.pdf)
- [Lattice-Based Zero-Knowledge Proofs in Electronic Voting — Springer Journal of Cryptology (2024)](https://link.springer.com/article/10.1007/s00145-024-09530-5)
- [Internet Voting — LWVMD Issue Paper](https://www.lwvmd.org/internet_voting_issue_paper)
- [Online Voting Isn't as Flawed as You Think — Just Ask Estonia — IEEE Spectrum](https://spectrum.ieee.org/online-voting-isnt-as-flawed-as-you-thinkjust-ask-estonia)

### Section 10 Sources (April 2026 Update)

- Trump v. Barbara, No. 25-365, oral argument April 1, 2026 — [SCOTUSblog case page](https://www.scotusblog.com/2026/01/supreme-court-will-hear-birthright-citizenship-case-on-april-1/)
- [Constitutional Accountability Center — Trump v. Barbara analysis](https://www.theusconstitution.org/litigation/trump-v-barbara/)
- [ACLU — Trump's birthright citizenship executive order: what happens next](https://www.aclu.org/news/immigrants-rights/trumps-birthright-citizenship-executive-order-what-happens-next)
- United States v. Wong Kim Ark, 169 U.S. 649 (1898) — the foundational birthright citizenship case
- LULAC v. Abbott — SCOTUS stay of Texas redistricting ruling, late 2025 — [MALDEF statement](https://www.maldef.org/2025/12/maldef-statement-on-supreme-court-order-allowing-new-texas-redistricting-maps-to-be-used-for-2026/)
- AFSCME v. SSA — Fourth Circuit reversal of preliminary injunction, April 2026 — [Government Executive reporting](https://www.govexec.com/)
- Gibson v. ICE/DHS — filed April 2, 2026, challenging secret Lyons memo — [ACLU-MN press release](https://www.aclu-mn.org/)
- Ramirez Ovando v. Noem — compliance evidentiary hearing, March 10-11, 2026 — [Colorado Politics](https://www.coloradopolitics.com/)
- Justice Sotomayor remarks on emergency-docket volume, April 9, 2026 — [Just Security reporting](https://www.justsecurity.org/)
- Cross-reference: `litigation-tracker-2026.md` (April 11, 2026 update) for full case details and sourcing
- Cross-reference: `us-democracy-crisis-analysis-2026.md` (April 11, 2026 update) for institutional crisis data
- Cross-reference: `democratic-renewal-proposal.md` for the broader governance reform framework
