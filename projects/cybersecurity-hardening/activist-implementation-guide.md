---
title: "Activist Implementation Guide: Secure Organizing, Protests, and Group Communications"
project: cybersecurity-hardening
created: 2026-04-28
status: complete
audience: activists, protest organizers, civil rights litigants, labor organizers
tier: 2
depends_on: device-hardening-guide.md, opsec-playbook.md, palantir-threat-model.md
---

# Activist Implementation Guide: Secure Organizing, Protests, and Group Communications

## Your Threat Model

You face a layered surveillance environment. At the infrastructure level, Palantir Gotham is deployed by NYPD, LAPD, and dozens of other major departments. It maps "family relationships," "all known associates," and constructs pattern-of-life analyses from arrest records, field contact cards, license plate reader data, and social media. A field contact card from a stop — even without charges — may already link someone in your organization to your group.

At the network level, Babel Street holds FBI contracts worth up to $27 million for OSINT aggregation; ImmigrationOS adds automated social media monitoring. Assume every public post connected to activism is indexed and searchable by law enforcement.

At the device level, ICE has purchased location data from Venntel — harvested from advertising SDKs in ordinary smartphone apps. EFF's Rayhunter confirmed cell-site simulator (IMSI catcher/StingRay) detection events in proximity to law enforcement in 2025. At protests, your phone may be subject to IMSI catcher collection even with no police contact.

NSA contact chaining extends two to three hops from a target: one arrested or compromised group member can expose your entire network in the absence of operational discipline. The goal of this guide is not invisibility — it is making each step of targeting more difficult and more legally contested.

---

## Week 1: Essential Baseline

**1. Install and configure Signal**
Install Signal ([signal.org](https://signal.org)). A subpoena returns only account creation date and last connection time. Configure:
- Settings → Privacy → Disappearing Messages → Default Timer → 1 Week (24 hours for operational conversations)
- Settings → Profile → @ field → set a username not linked to your real name
- Settings → Privacy → Phone Number → "Who can find me by my number" → Nobody
- Settings → Notifications → Show → No Name or Message (prevents Signal messages on lock screen)
- Settings → Privacy → Screen Lock → enable

Never scan QR codes to join Signal groups from untrusted sources — the NSA warned in February 2025 that this was the primary active attack vector against Signal users.

**2. Delete your advertising ID**
iPhone: Settings → Privacy & Security → Tracking → off. Settings → Privacy & Security → Apple Advertising → Personalized Ads off.
Android: Settings → Privacy → Ads → Delete advertising ID.

This severs the cross-app identifier that allows data brokers to build a historical location profile and sell it to law enforcement without a warrant.

**3. Audit app location permissions**
iPhone: Settings → Privacy & Security → Location Services → change any "Always" to "While Using"; change social media, retail, games to "Never."
Android: Settings → Location → App permissions → same audit.

**4. Set alphanumeric PIN and disable biometrics**
iPhone: Settings → Face ID & Passcode → Change Passcode → Passcode Options → Alphanumeric. Then: Face ID & Passcode → iPhone Unlock → toggle off Face ID. Android: Settings → Security → Screen lock → Password. Emergency shortcut: hold side + volume down to disable Face ID immediately. Practice this until it is automatic.

**5. Lock down all public social media**
Set every account to maximum privacy. Remove location from profiles. Set posts to friends-only. Remove unknown followers on organizing accounts. Anything posted publicly is already indexed by Babel Street and available to law enforcement — you cannot delete what is archived, but you can stop creating new data for public monitoring systems.

**6. Mullvad VPN**
[mullvad.net](https://mullvad.net) ($5/month, accepts cash by mail, no identifying information required). Enable before any online organizing research or platform access. ISP records are accessible via NSL without a warrant.

**7. Password manager and 2FA cleanup**
Install KeePassXC ([keepassxc.org](https://keepassxc.org)) and generate unique strong passwords for every account. Replace every SMS-based 2FA with an authenticator app (Ente Auth or Raivo OTP). SMS 2FA is vulnerable to SIM swapping — a transferred number lets an attacker intercept your 2FA codes for every SMS-protected account.

---

## Month 1: Intermediate Hardening

**1. Establish a dedicated secondary device**
Purchase a used Pixel phone with cash ($60–$120 at electronics resellers). No real-name accounts, no social media, Signal only, activated with a MySudo number ([getsudo.com](https://getsudo.com)) not linked to your carrier. Critical rule: never co-locate it with your primary phone while both are powered on. Cell towers log co-located phones; consistent co-location defeats identity separation. When your primary is on, the secondary lives in a Faraday pouch.

**2. Purchase and use a Faraday pouch**
Mission Darkness or GoDark (~$50–$80). Test: put your phone in, call it from another phone — if it rings, the pouch does not work. Use it for: secondary phone when not in use; primary phone at sensitive meetings; border crossings (combined with power-off). The last location recorded before entering the pouch is already in carrier records — the pouch only stops future tracking.

**3. Power-off protocol for protests**
Leave your phone at home if possible — its last recorded location before you left creates a verifiable record you were not at the protest. If you must bring it: power off completely (not just airplane mode). Full power-off before arriving provides BFU protection and prevents IMSI catcher collection. Airplane mode alone prevents IMSI catcher and carrier location data but recent iPhones continue Bluetooth beaconing if Find My is enabled (see `device-hardening-guide.md` Section 1.4). Best option: power off + Faraday pouch.

**4. Register secondary Signal with a VoIP number**
Register Signal on your secondary device using a MySudo or Google Voice number not linked to your identity. Configure identically to your primary: disappearing messages, username, phone number visibility to Nobody. Verify Safety Numbers with key contacts in person: open their conversation → tap name → Safety Number → read aloud together. Marks no-one has been inserted between you.

**5. Organizational Signal communications hygiene**
Each person in a Signal group is a potential weak link. Rules: (1) Separate groups by sensitivity — general coordination (assume membership list could be exposed) versus operational planning (in-person-verified members only, 24-hour disappearing messages mandatory). (2) Keep sensitive groups small. (3) Never discuss tactics in groups with unvette members. (4) If any member is arrested: assume the group is compromised, remove them, archive it, and restart with re-verified members.

**6. OnionShare for document distribution**
Install OnionShare ([onionshare.org](https://onionshare.org)). Creates a temporary .onion address for file transfer through Tor — no central server, no provider to subpoena. Use for meeting notes, action plans, any document that should not exist in a third-party cloud service.

**7. Pattern-of-life disruption**
Palantir Gotham constructs pattern-of-life analyses from your recurring locations and timing. Disrupt: vary routes and departure times. Do not conduct sensitive activity from home or workplace — use locations you visit only occasionally. Keep your activism phone off during all travel to and from sensitive locations; turn it on only at the destination. The carrier sees the phone appear and disappear at a location without seeing the travel pattern that connects it to you.

---

## Month 3: Advanced Mastery

**1. Install GrapheneOS on your activism device**
GrapheneOS ([grapheneos.org](https://grapheneos.org)) provides the strongest available Android hardening: auto-reboot at 18 hours (configurable to 10 minutes, returning the device to BFU state even if seized overnight), per-app network access controls that block ad-SDK harvesting at the OS level, and USB restrictions that block new connections when locked (the primary Cellebrite vector). A leaked Cellebrite support matrix flagged GrapheneOS Pixel devices as inaccessible for most extraction scenarios. Runs on Google Pixel only — a used Pixel 8 is the correct choice.

**2. Tor Browser for sensitive research**
Download from [torproject.org](https://www.torproject.org). For best anonymity: connect Mullvad VPN first, then use Tor Browser — this hides Tor usage from your ISP while preserving Tor's anonymity. Set security level to "Safest" via the shield icon in the toolbar.

**3. Deploy Rayhunter for IMSI catcher detection**
EFF's Rayhunter ([github.com/EFForg/rayhunter](https://github.com/EFForg/rayhunter)) runs on an Orbic hotspot (~$20) and detects cell-site simulator indicators in real time: 2G downgrade attacks, unusual IMSI requests, suspicious base station behavior. Rayhunter detects, does not block — response to a trigger is to power off and leave. Its primary value is documenting patterns for legal challenges. One person in your organization running it provides detection for everyone present.

**4. Incident response plan**
Before anyone is arrested: document who has access to what and which Signal groups they are members of. When someone is arrested: (1) assume their device is accessible to law enforcement within hours; (2) remove them from all sensitive Signal groups immediately; (3) assess operational information they had access to and notify affected members; (4) discuss nothing digital — in person only; (5) activate legal support. Know your NLG chapter's protest hotline number before any demonstration.

**5. Financial compartmentalization**
The IRS LCA platform maps social networks through financial transactions. Use a prepaid Visa/Mastercard gift card purchased with cash for all activist-related purchases (VPN, cloud storage, any service linked to your activist identity). For digital payments requiring genuine anonymity, Monero is documented in `opsec-playbook.md` Section 5.2 — ring signatures make transaction tracing computationally infeasible, unlike Bitcoin which the IRS LCA platform explicitly analyzes.

---

## Common Mistakes and How to Avoid Them

**Keeping both phones on at the same location.** Cell tower records showing two phones at the same location every night and morning will be correlated by any competent analyst. The second phone lives in a Faraday pouch when your primary is on.

**Adding people to Signal groups without in-person vetting.** An infiltrator does not need to break Signal's encryption — they just need to read the group. Keep sensitive groups small, require in-person verification for operational membership, and rotate groups after any member's device is seized.

**Relying on post-protest social media cleanup.** Babel Street archives public posts in real time. Setting accounts to private after a protest does not remove what was already collected. Set everything to private before any action — not afterward.

---

## Verification Checklist

- [ ] Signal disappearing messages: open a conversation → tap name at top → Disappearing Messages → confirm timer is set
- [ ] Signal username: Settings → Profile → confirms @ username field is set
- [ ] Signal phone number visibility: Settings → Privacy → Phone Number → "Who can find me by my number" → Nobody
- [ ] Advertising ID deleted: iPhone → Privacy & Security → Apple Advertising → Personalized Ads off; Android → Settings → Privacy → Ads → confirmed deleted
- [ ] Location permissions: no apps set to "Always" except navigation apps
- [ ] Faraday pouch test: phone in pouch, called from another phone — did not ring
- [ ] VPN active: Mullvad → mullvad.net/check confirms connected
- [ ] 2FA audit: three most sensitive accounts — 2FA via authenticator app, not SMS
- [ ] Social media: all accounts set to private, location removed from profile
- [ ] Emergency legal number: NLG number written down or memorized
- [ ] Secondary device: Signal registered, never co-located with primary phone while both are on

---

## References

This guide distills from the following documents in this repository:
- `device-hardening-guide.md` — complete iOS/Android hardening, IMSI catcher context, BFU/AFU states
- `opsec-playbook.md` — full countermeasures by tier, organizational OpSec, Signal configuration
- `implementation-guide.md` — step-by-step setup, financial compartmentalization, data broker opt-outs
- `palantir-threat-model.md` — confirmed police Gotham deployments, ImmigrationOS, Babel Street capabilities

For legal support at protests: [National Lawyers Guild](https://nlg.org) (know your NLG chapter's phone number before arriving at any demonstration). For digital rights and civil rights: [EFF](https://eff.org), [ACLU](https://aclu.org).
