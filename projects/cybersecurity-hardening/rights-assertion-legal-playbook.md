---
title: "Rights-Assertion Legal Playbook: Fifth, Fourth, and First Amendment Frameworks for Surveillance Resistance"
project: cybersecurity-hardening
created: 2026-06-22
status: complete
priority: P1 (F-03)
depends_on:
  - emergency-protocols-playbook.md (F-01 — scenario protocols; this document deepens the legal analysis)
  - opsec-playbook.md (Part 11 — legal resources)
  - immigration-surveillance-evasion-playbook.md (field encounter protocols)
  - whistleblower-playbook.md (legal framework for government employees)
confidence: high — grounded in primary case citations and current circuit-level analysis; Fifth Amendment compelled decryption section notes areas of genuine legal uncertainty
audience: anyone who may face law enforcement contact, border crossings, or legal process demanding access to devices or identity — especially activists, organizers, journalists, immigrants, and whistleblowers
---

# Rights-Assertion Legal Playbook

> **Lead finding**: The most important legal preparation you can do is not knowing the doctrine — it is storing your lawyer's number somewhere you can access without your phone, and practicing the five words until they are automatic: "I want a lawyer."

---

## Table of Contents

1. [How to Use This Playbook](#1-how-to-use-this-playbook)
2. [Fifth Amendment: Compelled Decryption](#2-fifth-amendment-compelled-decryption)
3. [Fourth Amendment: Searches and Digital Devices](#3-fourth-amendment-searches-and-digital-devices)
4. [First Amendment: Anonymous Speech and Association](#4-first-amendment-anonymous-speech-and-association)
5. [Legal Status of Privacy Tools in the US](#5-legal-status-of-privacy-tools-in-the-us)
6. [Scripted Law Enforcement Encounter Protocol](#6-scripted-law-enforcement-encounter-protocol)
7. [Legal Resources and Support Organizations](#7-legal-resources-and-support-organizations)

---

## 1. How to Use This Playbook

### This Is an Operational Legal Reference

The Emergency Protocols Playbook (F-01) gives you scenario-by-scenario action sequences. This document goes deeper into the constitutional frameworks so you understand why those actions are correct and can apply the reasoning in situations the scenario guide does not explicitly cover.

This is not legal advice for your specific case. If you are facing actual legal process — a warrant, a subpoena, a formal demand to decrypt — you need a lawyer, not a reference document. The value of this playbook is the preparation it enables before any encounter.

### Jurisdiction Matters

Some of the rights discussed here — particularly Fifth Amendment protection against compelled decryption — vary by federal circuit. The document flags where the law is settled and where it is contested. If you are in a jurisdiction where the law is less protective, the practical implication is that preparation (powering off your device, using alphanumeric passcodes, having a lawyer's number memorized) becomes more important, not less.

### Pre-Crisis Action: Do This Now

> [!important]
> Store your lawyer's phone number somewhere other than your phone — memorized, written in your wallet, or given to a trusted contact. If your phone is seized, you need to reach counsel without it.

If you do not yet have a specific lawyer, identify the National Lawyers Guild legal support line for your area (nlg.org) and the local ACLU before any high-risk situation. Many civil rights organizations have rapid-response legal support available by phone.

---

## 2. Fifth Amendment: Compelled Decryption

### The Core Doctrine

The Fifth Amendment protects against compelled self-incrimination: the government cannot force you to be a witness against yourself. The question courts have grappled with is whether providing your phone's passcode or biometric authentication is "testimonial" — a communicative act protected by the Fifth Amendment — or merely physical, like a blood draw or handwriting sample, which courts have held is not testimonial.

The foundational case is **Fisher v. United States, 425 U.S. 391 (1976)**, which established the "foregone conclusion" doctrine: the act of producing evidence is not testimonial if the government already knows the evidence exists, knows it is in your possession, and knows the specific content well enough that compelling you to produce it reveals nothing new. Under Fisher, if the government can independently establish all three of these things, it can compel production without running afoul of the Fifth Amendment.

The dispute in compelled decryption cases is whether the government can meet the foregone conclusion standard — and what "reasonable particularity" actually requires.

### Passcodes: The Current Circuit Landscape

As of mid-2026, the federal circuit law on compelling passcode disclosure is genuinely unsettled, with different courts applying different standards.

**Eleventh Circuit — most willing to compel:**
The Eleventh Circuit addressed compelled decryption in *In re Grand Jury Subpoena Duces Tecum* (11th Cir. 2012). The court adopted the foregone conclusion doctrine and held that if the government can show with "reasonable particularity" that specific incriminating files exist on the encrypted device, compelling decryption is not testimonial. However, the court ruled for the defendant in that specific case because the government could not meet that standard.

The practical implication: in the Eleventh Circuit, the government has a workable legal path to compel decryption. If you are in a federal case with Eleventh Circuit jurisdiction (Florida, Georgia, Alabama), the Fifth Amendment protection for your passcode is more vulnerable than in other circuits.

**Third Circuit — unresolved:**
The Third Circuit in *In re Grand Jury* (3d Cir. 2012) punted on the merits of the foregone conclusion standard, finding the case moot without ruling on the constitutional question. Courts in the Third Circuit are not bound by a settled standard.

**State courts — split on passcodes:**
State courts have ruled in multiple directions. The Pennsylvania Supreme Court (*Commonwealth v. Davis*) ruled that compelled passcode production violates the Fifth Amendment. The New Jersey Supreme Court (*State v. Andrews*) held the opposite — if the government can prove you know the passcode, you can be compelled to produce it. Massachusetts (*Commonwealth v. Jones*) also allows compelled passcode production if the government proves knowledge of the password beyond a reasonable doubt.

> [!warning]
> If your case proceeds in state court — which many device-search cases do — the applicable law is your state's constitution and case law, not just federal constitutional doctrine. Know your state's position.

**The Supreme Court has not ruled:** As of mid-2026, the U.S. Supreme Court has not resolved the circuit split on compelled passcode production. Until it does, the outcome depends heavily on jurisdiction and specific facts.

### Biometrics: A Different and Evolving Analysis

Most courts have historically treated biometric unlocking (fingerprint, face) as non-testimonial — a physical act like providing a blood sample or a voice exemplar — because it does not communicate the contents of your knowledge. That consensus is now fracturing.

**Ninth Circuit (2024) — biometrics not testimonial:**
In *United States v. Payne*, 99 F.4th 495 (9th Cir. 2024), the Ninth Circuit held that law enforcement physically grabbing the defendant's thumb and pressing it to the phone did not violate the Fifth Amendment. The court reasoned that using the fingerprint required "no cognitive exertion" and was analogous to a compelled fingerprinting.

**D.C. Circuit (2025) — biometric unlock can be testimonial:**
In *United States v. Brown*, 125 F.4th 1186 (D.C. Cir. 2025), the D.C. Circuit reached the opposite conclusion: compelling a person to unlock their phone with a fingerprint is testimonial because the instruction to unlock communicates control and ownership of the device and implies knowledge of its contents. The court distinguished *Payne*: what matters is whether law enforcement instructs the person to perform an act (testimonial) vs. physically seizing and using their body part without instruction (not testimonial — the person performs no act).

The distinction is narrow and the law is moving. The key practical implications:

> [!important]
> **Passcodes provide stronger Fifth Amendment protection than biometrics in most jurisdictions.** The D.C. Circuit's 2025 ruling has made biometric compulsion more legally contested, but the safest posture is:
> 1. Use an alphanumeric passcode as your primary authentication
> 2. Disable biometrics before any law enforcement encounter using the emergency gesture (iPhone: side button + volume button; this disables Face ID and requires passcode entry)
> 3. If ordered to use biometrics to unlock your device, state clearly that you are declining on Fifth Amendment grounds and request a lawyer

### What to Say

> [!quote]
> **Script — compelled decryption refusal:**
> "I am invoking my Fifth Amendment right against self-incrimination. I will not provide any password, passphrase, or biometric authentication. I want to speak with a lawyer."

Do not add explanation. "I have nothing to hide" is not helpful. "I'd prefer not to" is not an invocation. State it once, clearly, and stop.

If law enforcement has a court order specifically compelling production of a password, do not comply without a lawyer present. A court order changes the calculus — refusing a lawful court order can constitute contempt — but the scope of the order, its legal validity, and your appeal options all require legal counsel to navigate.

### Practical Takeaway

The most durable protection is not legal doctrine — it is not having the passcode on your person at all. A powered-off device in BFU state cannot be accessed by forensic tools without the passcode. The legal question of whether you can be compelled to provide the passcode is important, but it is secondary to the technical question of whether they can access the device without it. See `device-hardening-guide.md` Section 2.3 for the BFU/AFU technical analysis.

---

## 3. Fourth Amendment: Searches and Digital Devices

### The Settled Rule: Riley v. California (2014)

**Riley v. California, 573 U.S. 373 (2014)** is the most important Fourth Amendment case for cell phone searches and it is settled law. The Supreme Court held unanimously that law enforcement cannot search the digital contents of a cell phone incident to a lawful arrest without a warrant. The "search incident to arrest" exception — which allows warrantless searches of a person and the area within their immediate reach at arrest — does not extend to the data on a cell phone. A warrant is required.

> [!important]
> **If you are arrested and law enforcement searches your phone's contents without a warrant, that search is unconstitutional under settled Supreme Court precedent.** The evidence obtained may be subject to suppression via a motion to suppress. Document everything and notify your lawyer immediately.

What *Riley* does not protect: the physical device itself can be seized. Seizing the device to prevent destruction of evidence is different from searching its contents. They take the phone; they need a warrant to read it.

### Warrant Execution: Know the Scope

If law enforcement presents a warrant authorizing a search of your device:

1. **Read the warrant.** You have the right to read it before any search begins. Look at: (a) what specific devices are described, (b) what specific evidence they are authorized to search for, (c) what accounts or data types the warrant covers, and (d) the time period covered.

2. **State your objection to scope overreach on the record.** If officers attempt to search content that is not described in the warrant, say clearly and calmly: "I do not consent to any search beyond what is authorized by the warrant." This is not physical resistance — you do not obstruct, you object verbally and let them proceed while preserving your right to challenge later.

3. **Do not provide your password unless the warrant specifically compels it.** A warrant to seize and search a device is not automatically a warrant compelling you to decrypt it. Some warrants include specific language compelling password production; most do not. If the warrant does not specifically compel your password, the compelled decryption analysis in Section 2 applies.

4. **Call a lawyer immediately.** While officers are present if possible; as soon as you can otherwise.

5. **Get a receipt for anything taken.** Document make, model, and approximate contents of each device taken.

### The Border Exception

The border search exception to the Fourth Amendment is one of the most significant legal carve-outs you need to understand. **At international borders and ports of entry, the government has broad search authority that does not require a warrant and in many cases requires no individualized suspicion at all.**

Courts have sustained this authority based on the government's interest in controlling what enters and leaves the country. The exception covers:

**"Basic" or "manual" searches** — manual review of what is visible on an unlocked device, by an officer without forensic tools. CBP policy allows this without any suspicion.

**"Advanced" or "forensic" searches** — connecting the device to Cellebrite or similar extraction tools. CBP's internal policy (Directive 3340-049A) states this requires reasonable suspicion of illegal activity or a national security concern. However, this is an internal policy, not a constitutional requirement — courts have not uniformly required reasonable suspicion for forensic border searches. CBP does not always follow its own policy, and the legal remedy is after-the-fact challenge, not pre-search protection.

**Compelled unlocking at the border** is contested. CBP claims authority to compel you to unlock your device. You can refuse. If you refuse:
- CBP can detain you for additional questioning
- CBP can seize your device (they must provide a Form 6051D receipt)
- If you are a foreign national (not a U.S. citizen), CBP can deny entry
- They cannot criminally charge you solely for refusing to unlock

> [!warning]
> The outcome of refusing to unlock at the border is different from refusing in a domestic encounter. A U.S. citizen cannot be denied entry to the country, but can face extended detention and device seizure. **The practical protection against border searches is crossing with a factory-reset device — see emergency-protocols-playbook.md Scenario 5.**

### The 100-Mile Border Zone

CBP has claimed authority to conduct searches not just at ports of entry but anywhere within 100 miles of any external U.S. border. This zone encompasses approximately two-thirds of the U.S. population, including most major coastal metropolitan areas. Courts have not resolved the full scope of this authority. Internal highway checkpoints have more limited authority than ports of entry, and courts have struck down some checkpoint practices. But the authority is real, the zone is vast, and the legal landscape is not protective enough to rely on.

### The Plain View Doctrine

If you voluntarily show officers your phone and they observe something incriminating in plain view, they can seize it and use it. Do not unlock your phone for an officer for any reason — not to demonstrate you have nothing to hide, not to show them something specific, not because they ask nicely.

**Never consent to a search.** This is not suspicion-raising behavior; it is the legally correct response to a request that has no legal obligation behind it (absent a warrant or court order). "I do not consent to searches" is a complete sentence and the correct answer every time.

---

## 4. First Amendment: Anonymous Speech and Association

### The Foundational Cases

**NAACP v. Alabama ex rel. Patterson, 357 U.S. 449 (1958)** is the bedrock. The Supreme Court unanimously held that Alabama could not compel the NAACP to produce its membership lists, because forced disclosure would substantially restrain members' freedom of association by deterring membership. The Court found that the freedom of association is a form of speech protected by the First Amendment, and that compelled disclosure of membership can chill the exercise of that right. This is the founding precedent for First Amendment protection against compelled identification.

**McIntyre v. Ohio Elections Commission, 514 U.S. 334 (1995)**: The Supreme Court held that anonymous political pamphlets are constitutionally protected. The First Amendment protects the right not to identify yourself as the author of political speech.

**Reno v. ACLU, 521 U.S. 844 (1997)**: The Supreme Court held that internet speech receives the full First Amendment protection applied to print media — not the diminished protection that applies to broadcast. This established the baseline for online speech protection.

**Talley v. California, 362 U.S. 60 (1960)**: The Supreme Court struck down a Los Angeles ordinance requiring handbills to identify their author and distributor. The Court recognized, for the first time, a right to speak anonymously.

### Current Application: Anonymous Online Speech and Subpoenas

When someone is subpoenaed to reveal the identity of an anonymous online speaker, courts apply a balancing test derived from the *NAACP* line of cases: the need for disclosure must outweigh the chilling effect on protected anonymous speech. Factors courts consider include whether the speech at issue is on a matter of public concern, the magnitude of the claimed injury to the subpoenaing party, and whether the subpoena is the only means of obtaining the information.

Courts have been fairly protective of anonymous online speech on matters of public concern. But this protection is not absolute, and the test is applied case-by-case. If you receive a subpoena seeking your identity as an anonymous online speaker — served to an online platform, email provider, or similar — you (or more precisely, a lawyer you retain) can file a motion to quash the subpoena on First Amendment grounds. This requires legal counsel.

### How to Assert First Amendment Anonymous Speech Rights

If you receive notice that a subpoena has been served on a platform for your account information:

1. **Retain a lawyer immediately.** The filing deadline to quash a subpoena is short. EFF, ACLU, and the First Amendment Coalition can provide referrals to attorneys who handle these cases.

2. **File a motion to quash** citing the First Amendment right to anonymous speech and the *NAACP v. Alabama* line of cases, and arguing that the government's interest in disclosure does not outweigh the chilling effect on protected speech.

3. **Do not contact the subpoenaing party directly.** Your lawyer handles all communication.

> [!note]
> The First Amendment protection for anonymous speech is strongest when: the speech is political, the speaker is engaging in advocacy or organizing, disclosure would chill the speech, and the person seeking disclosure cannot articulate a compelling need that outweighs that chilling effect. It is weakest when the speech is defamatory, harassing, or directly connected to a crime — then other considerations override the anonymity interest.

### Encryption and Anonymity Tools as First Amendment Expression

There is a growing body of argument — though no settled Supreme Court doctrine — that the use of encryption and anonymity tools is itself protected expression under the First Amendment. The argument is that code is speech (*Bernstein v. DOJ*, 9th Cir. 1999, establishing that source code has First Amendment protection) and that the decision to communicate privately is itself a communicative act about the importance of privacy in a democratic society. This argument has not been tested in the compelled decryption context at the circuit level.

For practical purposes: using encryption and anonymity tools is legal. It does not create probable cause. It is not suspicious. The section below addresses this directly.

---

## 5. Legal Status of Privacy Tools in the US

This section states clearly what many people incorrectly assume about the legal status of privacy tools.

> [!important]
> **Encryption tools, anonymity networks, and surveillance countermeasures are entirely legal in the United States for personal use. Their use does not create probable cause for a search or investigation. There is no law criminalizing Tor, VPN use, Signal, VeraCrypt, or Faraday bags.**

Specifically:

**Encryption software** — Signal, WhatsApp end-to-end encryption, ProtonMail, VeraCrypt, PGP/GPG, FileVault, BitLocker, LUKS, GrapheneOS: legal for personal use. The U.S. government has pursued mandatory encryption backdoors in legislation (the EARN IT Act and predecessors), but as of mid-2026, no such law has passed. There are no legal encryption backdoors in U.S. law.

**Anonymity networks** — Tor Browser, I2P: legal for personal use. Tor is used by journalists, human rights workers, researchers, businesses protecting trade secrets, and ordinary privacy-conscious individuals. The Tor Project is a 501(c)(3) nonprofit. Using Tor does not by itself create probable cause.

**VPNs** — Mullvad, ProtonVPN, IVPN, and similar: legal for personal use. Purchasing a VPN subscription does not require identification. Using a VPN does not by itself create probable cause.

**Anonymous communications** — prepaid phones, SIM cards: legal. As noted in the IMSI catcher guide (F-04), the U.S. does not have mandatory prepaid SIM registration laws at the federal level.

**Physical countermeasures** — Faraday bags (Mission Darkness, GoDark), RF shielding wallets, camera covers, microphone blockers: legal.

**What IS illegal** (to be clear about the actual legal lines):

- Using these tools to commit crimes (drug trafficking, fraud, child exploitation) — the tool is legal; the underlying crime is not
- Wiretapping: intercepting communications of others without their consent is illegal under the Electronic Communications Privacy Act (18 U.S.C. § 2511) — even if you are using legal encryption tools to do it
- Signal jammers: radio jammers that block cellular or Wi-Fi signals are prohibited by the FCC regardless of purpose (47 U.S.C. § 333). This includes Stingray-blocking "cell-jammers" — even possessing one is a federal violation.
- Export of certain cryptographic technology: the Export Administration Regulations have historically controlled export of strong encryption products to certain countries. This is not a concern for domestic personal use.

> [!note]
> **A law enforcement officer telling you that using Tor or a VPN is suspicious is not a legal basis for a search.** Using legal privacy tools does not create reasonable suspicion. If you are told otherwise and your device is searched on that basis, document it and contact a lawyer — it may be the basis for a suppression motion.

---

## 6. Scripted Law Enforcement Encounter Protocol

The following scripts are designed to be memorized and used verbatim. They are not combative — they are calm, factual assertions of rights. The goal is to create a clear record while not escalating the encounter.

### At the Door (Law Enforcement Knocking)

**Before opening** (if you have time to think): Do not open the door unless you confirm they have a warrant and you can see it slid under the door or held to a window. You are generally not legally required to open your door to law enforcement unless they have a warrant.

**If you open the door:**

> "Am I free to go, or am I being detained?"

If free to go: "Thank you." Close the door (politely) and contact a lawyer.

If detained or arrested: "I am invoking my Fifth Amendment right against self-incrimination and my right to an attorney. I will not answer questions without a lawyer present."

**If they say they have a warrant:** "I'd like to read the warrant before anything proceeds." You have the right to read it. Review scope carefully. "I do not consent to any search beyond what is specified in this warrant." Then cooperate physically with what the warrant authorizes while continuing to assert your rights verbally.

### At a Traffic Stop or Street Encounter

**Basic assertion:**

> "I am exercising my right to remain silent and my right to an attorney. I do not consent to any search of my person, my vehicle, or my belongings."

If they ask for ID: in a Terry stop (reasonable suspicion) or traffic stop, you may be legally required to identify yourself in many states. Identify yourself if legally required. "Stop and identify" laws vary by state — know your state's requirement. Identification does not waive your other rights.

After providing ID: return to silence. Any further questions: "I'd like to speak with an attorney before answering any questions."

### At Arrest

**The five words:**

> "I want a lawyer."

Nothing else. Not "I want a lawyer, but I should tell you that..." Just "I want a lawyer." These words, clearly stated, legally require all questioning to stop under *Miranda v. Arizona, 384 U.S. 436 (1966)* and its progeny. Continuing to answer questions after invoking this right can be treated as a waiver.

Do not say "I think maybe I should talk to a lawyer" or "I might want a lawyer." Ambiguous invocations may not trigger the protection under *Berghuis v. Thompkins, 560 U.S. 370 (2010)*.

> [!important]
> **Be completely unambiguous:** "I want a lawyer." Then do not answer any further questions, no matter what officers say, until counsel is present.

If your phone is with you when arrested:

- **Before they approach** (if you have a moment): press side button + volume button simultaneously (iPhone). This triggers the Emergency SOS screen and disables Face ID. The phone is now passcode-only. If possible, power off completely.
- **After approached**: do not attempt to delete, wipe, or lock anything. Obstruction charges are real and separate from the underlying matter.

### At the Border (CBP Encounter)

**For U.S. citizens:**

> "I am a United States citizen. I am asserting my Fifth Amendment right against self-incrimination. I do not consent to a search of my electronic devices."

State it once, calmly. They can still detain you and seize your device. If they seize the device, request a Form 6051D receipt, note the officer's name and badge number, and call a lawyer immediately after clearing the checkpoint.

**For non-citizens:**

Non-citizens have fewer protections at the border. CBP can deny entry to a non-citizen who refuses to comply with a border search demand. If you are a non-citizen facing a device search at a port of entry, the practical calculus is different — refusal risks denial of entry; compliance creates a forensic record. Consult an immigration attorney before international travel if this is a concern for you.

**For everyone:**

Do not lie to CBP. Providing false information to CBP is a federal crime (18 U.S.C. § 1001). Refusing to answer is not lying. "I am exercising my right not to answer that question" is available to you. "No, there's nothing on this phone" when there is something is not.

### Document Everything Immediately After

As soon as the encounter is over and you are in a safe place:

1. Write down: officer name(s) and badge number(s), date, time, location, what was said verbatim (to the extent you can recall), what was searched, what was taken
2. Do not call or text about what happened from a device that may have been compromised during the encounter
3. Contact your lawyer or a civil rights organization within 24 hours

---

## 7. Legal Resources and Support Organizations

### Emergency and Rapid-Response Legal Support

**National Lawyers Guild (NLG)**
- nlg.org | nlg.org/find-an-attorney
- Mass defense and rapid-response legal support for activists, protesters, and individuals facing political prosecution
- NLG legal observers are present at many protests and demonstrations
- Know Your Rights resources at nlg.org/know-your-rights
- **If you are at a protest or demonstration**: write the NLG legal support line number on your arm in permanent marker before going. Search "NLG legal support [your city]" to find the local number.

**ACLU Digital Rights**
- aclu.org/privacy-technology
- Fourth Amendment, Fifth Amendment compelled decryption litigation
- Know Your Rights guides at aclu.org/know-your-rights
- State ACLU chapters have local resources and rapid-response support

**Electronic Frontier Foundation (EFF)**
- eff.org | ssd.eff.org
- Digital rights litigation, surveillance legal resources, Know Your Rights guides
- Border search resources at eff.org/issues/searches-and-seizures-phones-and-computers-border
- Border search reporting form at eff.org/document/border-search-report (document your CBP encounter to help EFF's legal challenges)

### Digital Security-Specific Legal Support

**Access Now Digital Security Helpline**
- accessnow.org/help
- Free technical digital security assistance for journalists, activists, civil society organizations, and at-risk individuals globally
- Available in multiple languages; not a legal service — a technical security resource
- Can connect you with legal resources appropriate to your situation

**Freedom of the Press Foundation**
- freedom.press
- Digital security and legal support specifically for journalists and publishers
- Source protection guidance; SecureDrop infrastructure
- Digital security training for newsrooms

### For Compelled Decryption or Device Seizure Issues

If your device has been seized or you have been asked to provide a password by court order:

- **EFF**: Has litigated compelled decryption cases and files amicus briefs in major cases. Can provide attorney referrals.
- **ACLU**: Runs a Digital Fourth Amendment project that takes cases involving digital privacy and compelled disclosure.
- **National Association of Criminal Defense Lawyers (NACDL)**: Compelled Decryption Primer at nacdl.org — also provides attorney referrals.

### For First Amendment / Anonymous Speech Issues

If you are served with a subpoena seeking to identify you as an anonymous online speaker:

- **Electronic Frontier Foundation**: Has filed amicus briefs in John Doe subpoena cases; can provide attorney referrals.
- **First Amendment Coalition**: firstamendmentcoalition.org — free legal hotline for First Amendment issues.
- **ACLU**: Has litigated anonymous speech cases at the circuit level.

### For Whistleblowers

See `whistleblower-playbook.md` for the full legal framework. For immediate legal support:

- **Government Accountability Project (GAP)**: whistleblower.org — primary support organization for federal whistleblowers; actively representing DOGE-era whistleblowers as of 2026
- **National Whistleblower Center**: whistleblowers.org

---

## Confidence Assessment and Known Gaps

**High confidence — settled law:**
- *Riley v. California* (2014): warrant required for phone content search incident to arrest. Unanimous Supreme Court. This is not contested.
- *Miranda v. Arizona*: right to remain silent and to counsel upon arrest. Unambiguous.
- *NAACP v. Alabama* (1958): First Amendment protects freedom of association against compelled membership disclosure. Foundational and uncontested.
- Tor, VPN, Signal, VeraCrypt: legal for personal use. No U.S. law criminalizes these tools.

**Medium confidence — evolving law:**
- Fifth Amendment protection for passcode production: circuit courts are split; the Supreme Court has not ruled. The outcome in any specific case depends on jurisdiction, the specific facts, and how the court reads "reasonable particularity" under the foregone conclusion doctrine.
- Biometric compulsion: the *United States v. Brown* (D.C. Cir. 2025) ruling has made the law more contested than it was in 2023. The Ninth and D.C. Circuits are now in tension. Supreme Court resolution is possible in the next 2-3 terms but has not been granted.
- CBP authority for forensic device searches: the border exception is broad and courts have been reluctant to limit it. The legal trajectory is not protective, and CBP's own policy is unevenly followed.

**Known gaps:**
- State-specific variation in stop-and-identify requirements, compelled decryption doctrine, and police conduct regulations. This playbook addresses federal constitutional law; know your state's law.
- Immigration status substantially complicates border encounters, device searches, and silence rights at enforcement encounters. See `immigration-surveillance-evasion-playbook.md` for the immigration-specific analysis.
- National Security Letter context: NSLs bypass most of the Fourth Amendment protections described here. They carry gag orders and require no judicial approval. If you have reason to believe you may be subject to national security process, consult a lawyer specializing in national security law; the frameworks described here do not fully apply.

---

## Sources

- [Fisher v. United States, 425 U.S. 391 (1976)](https://supreme.justia.com/cases/federal/us/425/391/) — foregone conclusion doctrine
- [Riley v. California, 573 U.S. 373 (2014)](https://www.supremecourt.gov/opinions/13pdf/13-132_8l9c.pdf) — phone content search incident to arrest requires warrant
- [Miranda v. Arizona, 384 U.S. 436 (1966)](https://supreme.justia.com/cases/federal/us/384/436/) — right to remain silent and to counsel
- [Berghuis v. Thompkins, 560 U.S. 370 (2010)](https://supreme.justia.com/cases/federal/us/560/370/) — invocation of silence must be unambiguous
- [NAACP v. Alabama ex rel. Patterson, 357 U.S. 449 (1958)](https://supreme.justia.com/cases/federal/us/357/449/) — First Amendment freedom of association; compelled membership disclosure
- [McIntyre v. Ohio Elections Commission, 514 U.S. 334 (1995)](https://supreme.justia.com/cases/federal/us/514/334/) — anonymous political speech is constitutionally protected
- [Reno v. ACLU, 521 U.S. 844 (1997)](https://supreme.justia.com/cases/federal/us/521/844/) — internet speech receives full First Amendment protection
- [Talley v. California, 362 U.S. 60 (1960)](https://supreme.justia.com/cases/federal/us/362/60/) — right to distribute anonymous handbills
- [United States v. Payne, 99 F.4th 495 (9th Cir. 2024)](https://www.techdirt.com/2024/04/25/ninth-circuit-5th-amendment-doesnt-cover-compelled-production-of-fingerprints-to-unlock-a-phone/) — Ninth Circuit: compelled fingerprint use not testimonial
- [United States v. Brown, 125 F.4th 1186 (D.C. Cir. 2025)](https://www.arnoldporter.com/en/perspectives/advisories/2025/03/when-your-fingers-do-the-talking) — D.C. Circuit: compelled biometric unlock is testimonial
- [Cell Phone Passcode Ruling Deepens Fifth Amendment Rift — American Bar Association (2024)](https://www.americanbar.org/groups/litigation/resources/litigation-news/2024/cell-phone-passcode-ruling-deepens-fifth-amendment-rift/)
- [NACDL Compelled Decryption Primer](https://www.nacdl.org/Content/Compelled-Decryption-Primer)
- [EFF: The Fifth Amendment, Encryption, and the Forgotten Doctrine of Foregone Conclusion](https://www.eff.org/deeplinks/2020/01/fifth-amendment-encryption-and-forgotten-doctrine-foregone-conclusion)
- [EFF: Know Your Rights — Devices at the US Border](https://www.eff.org/document/know-your-rights-devices-us-border)
- [CBP Border Search Policy — Directive No. 3340-049A](https://www.cbp.gov/sites/default/files/assets/documents/2018-Jan/CBP-Directive-3340-049A-Border-Search-Electronic-Media.pdf)
- [ACLU: Digital Fourth Amendment](https://www.aclu.org/cases/digital-fourth-amendment)
- [National Lawyers Guild: Know Your Rights](https://www.nlg.org/know-your-rights/)
- [Access Now Digital Security Helpline](https://www.accessnow.org/help/)
- [Freedom of the Press Foundation: Digital Security for Journalists](https://freedom.press/digisec/)
- [EFF Surveillance Self-Defense](https://ssd.eff.org/)
- [Bernstein v. U.S. Dep't of Justice, 176 F.3d 1132 (9th Cir. 1999)](https://www.eff.org/cases/bernstein-v-us-dept-justice) — source code as First Amendment protected speech
