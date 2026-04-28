---
title: "Undocumented Immigrant Implementation Guide: Reducing ICE Detection Risk"
project: cybersecurity-hardening
created: 2026-04-28
status: complete
audience: undocumented immigrants, mixed-status families, support networks
tier: 2
depends_on: device-hardening-guide.md, opsec-playbook.md, palantir-threat-model.md
---

# Undocumented Immigrant Implementation Guide: Reducing ICE Detection Risk

## Your Threat Model

ICE uses Palantir's ELITE platform, which displays potential deportation targets as map pins with per-person address confidence scores (as precise as 98.95 out of 100). The score is calculated from IRS tax records, SSA records, DMV files, Medicaid enrollment, utility bills, and commercial location data purchased from smartphone app data brokers. ELITE also identifies "target-rich areas" — neighborhoods where the system detects concentrations of people with an "immigration nexus." You do not need to have done anything wrong to appear. You only need to have interacted with any of those data sources.

A separate Palantir system, ImmigrationOS, adds AI-assisted target prioritization and automated social media monitoring. ICE has also purchased commercial location data from brokers like Venntel, which harvests GPS coordinates from ordinary apps — weather apps, games, retail apps — via advertising code. No warrant is required for this purchase.

The goal of this guide is not invisibility but to reduce the density of your data profile, degrade ELITE's address confidence score for your current location, and remove the easiest detection signals. Even completing Week 1 provides meaningful protection.

---

## Week 1: Essential Baseline

**1. Submit data broker opt-out requests**
ELITE's address confidence scores pull from commercial data brokers — removing your data degrades those scores. Submit from a library computer, not your home Wi-Fi (submitting from home confirms your current address before the opt-out processes).

LexisNexis: [optout.lexisnexis.com](https://optout.lexisnexis.com) → "Opt out of LexisNexis risk solutions products" → fill in name, address, date of birth. May require a government-issued ID upload.

BeenVerified: [beenverified.com/app/optout/search](https://www.beenverified.com/app/optout/search) → search for your name → Opt Out → confirm via email. Allow 2–5 days.

Spokeo: [spokeo.com/optout](https://www.spokeo.com/optout) → find your profile → opt-out link. Allow up to 5 days.

Full broker list is in `implementation-guide.md` Part 0.

**2. California DROP platform (California residents only)**
Go to [privacy.ca.gov/drop](https://privacy.ca.gov/drop). One submission reaches all registered California data brokers — over 500 at once. California law (AB 60, AB 1766) allows undocumented residents to obtain a state driver's license or ID without immigration status proof; that ID satisfies DROP's verification requirement. Submit from a library computer, not your home Wi-Fi.

**3. Delete your advertising ID**
ICE purchases location data from brokers like Venntel that harvest GPS from app advertising SDKs. Deleting your advertising ID severs the persistent identifier that links your location history to a profile.

iPhone: Settings → Privacy & Security → Tracking → turn off "Allow Apps to Request to Track." Settings → Privacy & Security → Apple Advertising → turn off Personalized Ads.

Android: Settings → Privacy → Ads → Delete advertising ID (search Settings for "Advertising ID" if the path differs).

**4. Audit app location permissions**
iPhone: Settings → Privacy & Security → Location Services. Change any "Always" to "While Using." Change weather, retail, social media, and games to "Never." Turn off "Precise Location" for every app except navigation.

Android: Settings → Location → App permissions. Set every app to "Only while using" or "Denied" unless it is a navigation app.

**5. Install Signal for private communications**
Install Signal ([signal.org](https://signal.org)). Use it instead of text messages or phone calls for your attorney, family, and support contacts. Carrier records are accessible to law enforcement; Signal content is end-to-end encrypted and Signal stores nothing on its servers. Configure: Settings → Privacy → Disappearing Messages → Default Timer → 1 Week. For sensitive conversations, set 24 hours.

**6. Set a strong PIN and disable biometrics**
iPhone: Settings → Face ID & Passcode → Change Passcode → Passcode Options → Alphanumeric. Android: Settings → Security → Screen lock → Password. In many jurisdictions, law enforcement can compel a fingerprint or face scan but not a memorized PIN. Turn off Face ID unlock: Settings → Face ID & Passcode → iPhone Unlock → toggle off.

**7. Set maximum privacy on all social media**
ImmigrationOS includes automated social media monitoring — public posts are indexed and can reveal location, associations, and routine. For every account: set to private/friends-only, remove listed location/workplace/school, review past posts for address or neighborhood reveals, remove photos with visible street signs or house numbers.

---

## Month 1: Intermediate Hardening

**1. Understand what your phone reveals and when**
Your phone connects to cell towers continuously; carriers log those connections and can be compelled to provide historical location data. Two countermeasures: (1) Leave your phone at home for any activity — legal consultation, advocacy meetings — where your presence at that location could be used against you. (2) If you cannot leave it: a Faraday pouch (Mission Darkness or GoDark, ~$50–$80) blocks all cell, Wi-Fi, GPS, and Bluetooth. Test it: put your phone in and call it — if it rings, the pouch does not work. Note: the last location recorded before going in the pouch is already in carrier records.

**2. Separate phone identities if possible**
A second phone (used model, $30–$60) used only for attorney and advocacy communications provides meaningful identity separation. Purchase with cash, no real-name registration, activate with a MySudo number ([getsudo.com](https://getsudo.com)) not linked to your identity. Install only Signal.

Critical rule: never power on both phones in the same location. Cell towers log which phones are present; two phones always together will be correlated, defeating the separation.

**3. Reduce administrative data footprints**
ELITE's address confidence score updates near-real-time from administrative records. Minimize unnecessary address disclosures: when a service asks for your address and you do not need a physical delivery, use a friend's address or a PO box. Know that credit applications, utility account changes, and program enrollments update your address in broker databases. The highest-risk administrative actions are DMV transactions, utility connections, and tax filings — often unavoidable, but completing opt-outs first means your commercial broker profile is already thin when new records arrive.

**4. Enable VPN for browsing**
Install ProtonVPN's free tier ([proton.me/vpn](https://proton.me/vpn)) on your phone and computer. Enable by default. ISP browsing records are accessible via NSL — a VPN prevents your ISP from seeing which sites you visit. Use it especially when researching legal options or contacting advocacy organizations.

**5. Use ProtonMail for sensitive email**
Create a Proton account at [proton.me](https://proton.me) with a username not including your real name. Use for attorney and support organization communications. Proton cannot be compelled for email content without a Swiss court order. End-to-end encryption applies only Proton-to-Proton; email to Gmail/Yahoo recipients is not encrypted end-to-end.

**6. Review data from your car**
Modern vehicles with connected features (any infotainment with Wi-Fi or Bluetooth) log location data subpoena-accessible from the manufacturer. Insurance telematics devices (Progressive Snapshot) are also accessible. If your vehicle has a connected services subscription (OnStar, Ford Sync, Toyota Connected), submit a deletion request to the manufacturer and review what data is retained.

---

## Month 3: Advanced Mastery

**1. GrapheneOS or hardened iPhone**
GrapheneOS on a Google Pixel is confirmed resistant to the forensic extraction tools used by law enforcement (see `device-hardening-guide.md` Section 2.1) and blocks ad-SDK location harvesting at the network level — stronger than the advertising ID deletion done in Week 1. If GrapheneOS is not feasible, a hardened iPhone (Advanced Data Protection on, SIM PIN set, advertising ID deleted, location permissions audited) is meaningfully protective for most threat scenarios.

**2. Set up auto-reboot**
iOS 18 automatically reboots if your iPhone has not been unlocked in 72 hours, returning it to Before First Unlock (BFU) state where forensic extraction tools cannot access data. Verify: Settings → General → About → Software Version (must be 18.0+). GrapheneOS auto-reboot is configurable to 10 minutes: Settings → Security → Auto reboot.

**3. Establish an emergency contact protocol**
Identify two trusted contacts (attorney, family member, advocate) to notify if you are detained. Agree on a Signal code phrase for when you are being approached but not yet detained — something that activates your legal plan without signaling distress to an observer. Write your attorney's number on paper and keep it in your wallet. Your phone may be seized or out of battery.

**4. Complete the full data broker opt-out list**
Return to `implementation-guide.md` Part 0 and complete the full list systematically: LexisNexis (done), Spokeo, BeenVerified, WhitePages, MyLife, Intelius, Radaris. Set a calendar reminder every 6 months — brokers periodically re-add records from public sources.

**5. Understand the limits and plan around them**
Tax records, immigration filings, and court records are in government databases that no opt-out reaches. Assume ELITE already has your immigration history. Opt-outs degrade the commercial data that supplements government records — particularly your address confidence score. What reduces daily life risk: encrypted communications (Signal), deleted advertising ID, audited app permissions, data broker opt-outs, awareness of administrative data triggers, and a legal plan established before you need it.

---

## Common Mistakes and How to Avoid Them

**Deleting social media posts after a problem arises.** Palantir systems and OSINT tools archive public content. Setting accounts to private after you become aware of enforcement interest is too late — do it now.

**Using a second phone but turning both on at the same location.** If both phones are consistently co-located — home, work, your car — cell tower records will correlate them. The second phone only provides separation if it is powered off or in a Faraday pouch whenever your primary phone is on, and never at your home or workplace.

**Submitting data broker opt-outs from your home internet connection.** Your home IP confirms your current address to the broker's database before the opt-out processes. Submit from a library or school computer.

---

## Verification Checklist

- [ ] LexisNexis opt-out submitted (from a library computer)
- [ ] Advertising ID deleted: iPhone → Privacy & Security → Apple Advertising → Personalized Ads is off; Android → Settings → Privacy → Ads → "Advertising ID" has been deleted
- [ ] Location permissions audited: no apps set to "Always" except navigation
- [ ] Signal installed with disappearing messages configured
- [ ] Phone PIN is alphanumeric (not a 4–6 digit number)
- [ ] Face ID / fingerprint unlock disabled
- [ ] All social media accounts set to private
- [ ] ProtonVPN installed and enabled by default on your phone
- [ ] Attorney's phone number written on paper in your wallet
- [ ] Emergency contact protocol agreed with two trusted contacts

---

## References

This guide distills from the following documents in this repository:
- `device-hardening-guide.md` — complete iOS/Android hardening, including BFU/AFU explanation
- `opsec-playbook.md` — full countermeasures by tier, including metadata minimization
- `implementation-guide.md` — complete data broker opt-out procedures with exact URLs
- `palantir-threat-model.md` — confirmed ICE contracts, ELITE data sources, and ImmigrationOS

For legal support and advocacy: [ACLU](https://aclu.org), [National Immigration Law Center](https://nilc.org), [United We Dream](https://unitedwedream.org), [Immigrant Defense Project](https://www.immigrantdefenseproject.org), National Lawyers Guild ([nlg.org](https://nlg.org))
