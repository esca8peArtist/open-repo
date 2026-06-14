---
title: "Phase 2 Readiness Checklist and Assessment"
project: cybersecurity-hardening
created: 2026-06-14
status: active
phase: 1-2-transition
---

# Phase 2 Readiness Checklist and Assessment

**Purpose**: Comprehensive assessment of whether you are ready to advance from Phase 1 (foundation) to Phase 2 (hardening). This document also clarifies your threat model maturity and system prerequisites before Phase 2 begins.

**Reading time**: 10 minutes. **Assessment time**: 20–30 minutes.

**When to use this**: After completing Phase 1 steps 1.3–1.7, and at least 1 week after starting disk encryption (to ensure encryption is stable).

---

## Part 1: Phase 1 Completion Verification

Before advancing to Phase 2, verify that Phase 1 is **fully complete and stable**.

### Disk Encryption Status

**BitLocker (Windows Pro/Enterprise)**

1. Open "Manage BitLocker" from Windows Start menu
2. Verify your C: drive shows **"BitLocker on"** with a green checkmark
3. Check encryption percentage:
   - **100% encrypted**: Encryption complete, safe to proceed to Phase 2
   - **1–99% encrypted**: Encryption still running. Wait until 100% before proceeding to Phase 2. Do not stress the drive with large operations (rendering, video encoding, large file transfers)
   - **0% encrypted** or **red X**: Encryption failed. See recovery procedures in PHASE_1_COMPLETION_WALKTHROUGH.md step 1.3

**VeraCrypt (Windows Home or Linux)**

1. Power on your computer
2. At the black screen before Windows boots, verify you see "VeraCrypt" pre-boot authentication
3. Enter your encryption password — you should be prompted before Windows loads
4. Once Windows loads, open VeraCrypt application
5. Verify "System encryption" shows as **Active**
6. Test by restarting your computer and confirming the pre-boot screen appears again

**Linux (LUKS encryption if applicable)**

1. Your system should boot normally — if encrypted during installation, you should have entered a passphrase during the installation process
2. Verify `/` (root) filesystem is encrypted: Open terminal and run `sudo cryptsetup status /dev/sda3` (adjust device name as needed) — should show "active"

**Status verification**: [ ] Disk encryption confirmed as active and 100% complete

---

### Authenticator App and Carrier Security

1. Open **Ente Auth** on your iPhone
2. Verify you see entries for:
   - Gmail / Google Account
   - Microsoft / Outlook Account
   - At least one financial account (bank, investment, etc.)
3. Tap each entry and confirm a 6-digit TOTP code appears (changes every 30 seconds)
4. Verify **backup codes** for each account are saved (screenshot, password manager, or physical location)

**Carrier account security**:
1. For your carrier (AT&T, T-Mobile, or Verizon), verify SIM protection / Number Lock is enabled
   - AT&T: Call 1-800-331-0500 and ask to verify "Extra Security" is enabled
   - T-Mobile: Open app → Profile → Security → SIM Protection should be ON
   - Verizon: Go to My Verizon and verify Number Lock is enabled

**Status verification**: [ ] Authenticator app working, [ ] Carrier SIM PIN/port-out PIN enabled

---

### Password Manager Active Use

1. Open **Bitwarden** on your Windows computer
2. Verify you can see at least 5 passwords stored
3. Open **Bitwarden browser extension** and verify it auto-fills a password on a test site (Gmail, bank, etc.)
4. On iPhone, open Bitwarden app and verify you can see the same passwords
5. Verify Bitwarden has 2FA enabled (check at bitwarden.com/account)

**Status verification**: [ ] Bitwarden has 5+ passwords, [ ] 2FA enabled on Bitwarden account, [ ] Browser extension and iPhone app working

---

### Data Broker Opt-Outs Submitted

1. Open a document or note where you tracked which brokers you opted out of
2. Verify all 10 brokers received opt-out requests:
   - [ ] LexisNexis
   - [ ] BeenVerified
   - [ ] Spokeo
   - [ ] WhitePages
   - [ ] Intelius
   - [ ] TruePeopleSearch
   - [ ] FastPeopleSearch
   - [ ] FamilyTreeNow
   - [ ] Radaris
   - [ ] Acxiom
3. Verify federal opt-outs:
   - [ ] OptOutPrescreen
   - [ ] Network Advertising Initiative
   - [ ] About Ads

**Status verification**: [ ] All 10 brokers opted out, [ ] All 3 federal opt-outs completed

---

### iPhone Passcode Configuration

1. Open **Settings → Face ID & Passcode** on your iPhone
2. Verify "Unlock iPhone" toggle is **OFF** (no checkmark)
3. Verify your passcode is 6+ digits (or alphanumeric custom)
4. Test unlock: lock your phone, then unlock with passcode only (no Face ID)
5. Practice Emergency SOS gesture: press side button + volume button simultaneously — should show "Emergency SOS" slider after 3 seconds

**Status verification**: [ ] Face ID disabled for unlock, [ ] Passcode tested, [ ] Emergency SOS gesture practiced

---

## Part 2: Hardware and Environment Prerequisites

Phase 2 requires certain minimum hardware and environment capabilities. Assess each area.

### Windows / Mac Encryption

**Requirement**: Full-disk encryption must be active on all computers you use.

| Device | Status | Phase 2 Ready? |
|--------|--------|---|
| Windows laptop | [ ] BitLocker active, [ ] VeraCrypt active, [ ] Not encrypted — BLOCK | Only if encrypted |
| Mac (if applicable) | [ ] FileVault 2 enabled, [ ] Not encrypted — BLOCK | Only if encrypted |
| Linux (if applicable) | [ ] LUKS encrypted, [ ] Not encrypted — BLOCK | Only if encrypted |

**If any computer is not encrypted**: You cannot proceed to Phase 2 until you enable full-disk encryption. Phase 2 work (ProtonMail, Tor Browser, sensitive research) requires that the underlying device is protected against physical seizure.

---

### iPhone Advanced Data Protection

**Requirement**: Advanced Data Protection must be enabled on iCloud for end-to-end encryption of backups.

1. Open **Settings → [Your Name] → iCloud** on your iPhone
2. Scroll to "Advanced Data Protection"
3. Tap "Advanced Data Protection"
4. Verify the status shows **"Advanced Data Protection is on"**
5. Verify you have saved the recovery key to a secure location (printed or in password manager, not in cloud)

**Status**: [ ] Advanced Data Protection enabled, [ ] Recovery key saved securely

**If not enabled**: Complete this before Phase 2. See PERSONAL_OPSEC_PLAN.md step 1.2 for details.

---

### Router Capabilities

**Phase 2 item 2.5** (Network Compartmentalization, in Phase 2 Execution Runbook) requires advanced router configuration. Assess your current router:

**Your router is Phase 2-ready if it supports**:
- [ ] Custom firmware (DD-WRT, OpenWrt, Tomato) **OR** native advanced settings (vlan, guest network, traffic monitoring)
- [ ] Guest network isolation (separate SSID that doesn't see your main network)
- [ ] Traffic filtering / firewall rules

**Typical modern routers** (WiFi 6, 2023+): Usually support all of these.

**Older routers** (2018 or earlier): May be limited. You may need to replace the router in Phase 2 (~$80–$150 for a capable model).

**Assessment**: Do you know your router model number? If not, see your router (usually on the bottom) or check your internet bill.

**Status**: [ ] Router model identified, [ ] Router appears Phase 2-compatible

---

### Physical Space for Faraday Testing

**Phase 2 item 3** (Physical Device Hardening) includes testing Faraday bags / RF shielding. This requires a way to test whether a Faraday bag actually blocks signals.

**You can test Faraday bags by**:
- [ ] Turning on Bluetooth on iPhone, putting it in the Faraday bag, and confirming nearby Bluetooth devices can't see it (test with your laptop or another iPhone)
- [ ] Having someone call your iPhone while it's in the bag — call should not go through
- [ ] Using a WiFi analyzer app to confirm WiFi networks disappear when phone is in the bag

**Assessment**: You don't need to own a Faraday bag yet (Phase 2 will cover purchasing), but you need a space where you can safely test RF blocking.

**Status**: [ ] Confirmed you can test Faraday bag (Bluetooth, WiFi, cellular signals)

---

## Part 3: Threat Model Maturity Assessment

Phase 2 involves spending time and money on security infrastructure. This is worthwhile only if your threat model is clear and matured. Complete this assessment honestly.

### Can You Articulate Your Threat Model?

Answer each question in 2–3 sentences:

**1. What data specifically needs protection?**

Write your answer:
> _____________________________________________________________
> _____________________________________________________________

Examples of clear answers:
- "My location data, so law enforcement can't trace my movements or presence at protests."
- "My email and financial accounts, so my identity can't be compromised if I'm a target of harassment."
- "My browser history and research, because I research topics that could be misinterpreted by my employer or government."

Examples of unclear answers:
- "Everything / my privacy"
- "I don't know, just in case something happens"

---

**2. From whom are you protecting this data?**

Write your answer:
> _____________________________________________________________
> _____________________________________________________________

Examples of clear answers:
- "Law enforcement and government data access via data brokers and surveillance."
- "Corporate tracking and behavioral profiling via ad networks and apps."
- "Harassment, doxxing, and OSINT from human adversaries (activists, competitors, former relationships)."
- "All three of the above."

---

**3. Under what specific scenarios would you actually be targeted?**

Write your answer:
> _____________________________________________________________
> _____________________________________________________________

Examples of clear answers:
- "If I attend protests or organize around a sensitive cause, law enforcement might query my location history."
- "If my email is compromised, an attacker could access my financial accounts."
- "If my home address is published online, I could be harassed or swatted."

Examples of unclear answers:
- "I might be targeted someday."
- "I want to be prepared for anything."

---

**4. If you're targeted, what level of effort is the adversary willing to expend?**

Write your answer:
> _____________________________________________________________
> _____________________________________________________________

Examples of clear answers:
- "Law enforcement with a warrant (moderate effort, legal compulsion)."
- "Casual OSINT doxxers (low effort, using publicly available tools)."
- "Targeted surveillance with commercial spyware (high effort, requires nation-state or well-funded criminal group)."

---

### Threat Model Maturity Scoring

Count how many of the 4 questions above you answered clearly and specifically:

- **4/4 clear answers**: Your threat model is **mature**. Proceed to Phase 2.
- **2–3 clear answers**: Your threat model is **partially mature**. Read the threat model section below, refine your answers, then proceed to Phase 2.
- **0–1 clear answers**: Your threat model is **underdeveloped**. Complete the "Threat Model Framing" section below before proceeding to Phase 2.

---

### Threat Model Framing (If Needed)

If your threat model is unclear, use this framework to develop one:

#### Simplified Threat Scenarios

**Scenario A: Law Enforcement and Palantir ELITE Data Access**

Palantir ELITE integrates:
- Your IRS records (income, filing status, financial info)
- Your SSA records (employment, benefits, name history)
- Your DMV records (license, vehicle info, address)
- Your bank statements and financial transactions (via DOGE cross-agency access)
- Your location history (purchased from data brokers like Venntel)
- Your social media presence and associates

**Question**: If law enforcement queried this integrated profile on you, would any of the following be problematic?
- Your location at a protest, demonstration, or sensitive location?
- Your associates or contacts (people you've been with, messaged with)?
- Your financial transactions (donations, purchases that reveal beliefs)?
- Your research activity or online searches?

If yes, **Scenario A applies to you**.

---

**Scenario B: Corporate Tracking and Behavioral Profiling**

Companies like:
- Google (via location services, search history, email, Chrome browser)
- Apple (via Siri, location, app behavior)
- Facebook/Meta (via ads, pixel tracking, device analytics)
- Data brokers (via ad networks, behavioral profiles, location aggregators)

...collect and sell your behavioral data, which:
- Enables targeted harassment (if your home address is published online, ads target that address)
- Feeds into law enforcement data pipelines (ICE purchases location data without warrants)
- Enables financial fraud (if your payment methods and addresses are exposed)
- Creates a detailed profile of your political beliefs, health information, and activities

**Question**: If your behavioral profile was purchased by law enforcement, a competitor, or a harasser, would any of the following be problematic?
- Your location history or patterns?
- Sites you've visited or things you've researched?
- Your financial transactions?
- Apps you've installed?

If yes, **Scenario B applies to you**.

---

**Scenario C: Targeted Harassment / Doxxing**

Humans (activists, competitors, former partners, internet strangers) use:
- Data broker sites (BeenVerified, Spokeo, WhitePages) to find your address, phone, and family info
- Social media OSINT to find your employer, relationships, and activities
- Public records (property records, voter registration, arrest records)
- Phone number lookup tools to find associated accounts

...to harass, threaten, or endanger you.

**Question**: If your address and phone number were published online by a hostile actor, would any of the following be problematic?
- Physical harassment, threats, or danger?
- Swatting or false police reports to your address?
- Contact to your employer or family?

If yes, **Scenario C applies to you**.

---

**Scenario D: Device Seizure and Physical Access**

Law enforcement conducts border searches, traffic stops, arrests, or civil asset forfeitures. Your device (laptop, iPhone) is seized while powered on or off.

**Question**: If your device was powered off and taken by law enforcement, would any of the following be problematic?
- They unlock it and read all your files, messages, photos, emails?
- They find evidence of activism, research, beliefs, or associations?
- They extract location history, contacts, or device metadata?

If yes, **Scenario D applies to you**.

---

### Applying Your Threat Model to Phase 2

Once you've identified which scenarios apply (A, B, C, D), Phase 2 should focus on those:

| Scenario | Applies to You? | Phase 2 Priority |
|----------|---|---|
| **A: Palantir ELITE / Law Enforcement Data Access** | [ ] Yes / [ ] No | VPN (2.1), Tor Browser (2.3), Windows telemetry (2.4), data broker automation (2.7) |
| **B: Corporate Tracking / Behavioral Profiling** | [ ] Yes / [ ] No | VPN (2.1), ProtonMail (2.2), Tor Browser (2.3), Windows telemetry (2.4), iPhone lockdown (2.6) |
| **C: Targeted Harassment / Doxxing** | [ ] Yes / [ ] No | Data broker automation (2.7), social media hygiene (3.5), financial compartmentalization (3.6) |
| **D: Device Seizure / Physical Access** | [ ] Yes / [ ] No | Disk encryption (1.3 — complete), Full-disk encryption is your protection here |

**If all four apply**: You need the full Phase 2 + Phase 3 roadmap. Estimated 2–3 months of work across June–August 2026.

**If scenarios A + B apply**: Focus on VPN, Tor Browser, email migration, and telemetry reduction. Estimated 1–2 months.

**If scenario C applies**: Focus on data broker automation and social media hygiene. Estimated 2–4 weeks.

**If scenario D only**: Your disk encryption (Phase 1 step 1.3) is your primary defense. Phase 2 is lower priority.

---

## Part 4: Financial and Time Commitment

Phase 2 requires both time and money. Assess whether you can commit.

### Time Commitment

Phase 2 items (from PERSONAL_OPSEC_PLAN.md):
- 2.1 Mullvad VPN: 1 hour setup
- 2.2 ProtonMail: 1 hour setup
- 2.3 Tor Browser: 30 minutes setup
- 2.4 Windows telemetry: 30 minutes
- 2.5 Linux encryption: 1–2 hours (if not already done)
- 2.6 iPhone Lockdown Mode: 5 minutes
- 2.7 Data broker automation: 15 minutes setup
- 2.8 Hardware security key (optional): 30 minutes setup
- 2.9 iPhone SIM PIN: 5 minutes

**Total time: 5–7 hours across 1–2 weeks** (can be spread across your schedule, 30–60 min per session)

**Do you have 5–7 hours available in the next 2 weeks?** [ ] Yes / [ ] No / [ ] Partially

---

### Financial Commitment

| Item | Cost | Required for Phase 2? |
|------|------|---|
| Mullvad VPN | ~$5/month (~$60/year) | Yes — core protection |
| Incogni data broker removal | ~$96/year | Optional but recommended |
| Prepaid gift cards (for anonymous payments) | ~$10–30 | Optional but useful |
| YubiKey 5 NFC (hardware security key) | ~$55 | Optional (high security) |
| Faraday bag (for Phase 3) | ~$50–80 | Optional (travel security) |

**Minimum Phase 2 cost**: ~$60/year (VPN only)  
**Comprehensive cost**: ~$250–300 first year

**Your budget for Phase 2**: __________ per month / __________ total

**Is this affordable for you?** [ ] Yes / [ ] No / [ ] Partially

---

## Part 5: System Prerequisites Check

Before starting Phase 2, verify you meet these minimum requirements.

### For Windows Users

- [ ] Windows 10 or 11 Pro/Enterprise (or Home with VeraCrypt alternative)
- [ ] 4+ GB RAM
- [ ] 50+ GB free disk space
- [ ] Admin access to install VPN and other software
- [ ] Modern browser (Chrome, Firefox, Edge, or Safari) with extension support

---

### For Mac Users

- [ ] macOS 10.15 or later
- [ ] FileVault 2 encryption enabled (check System Settings > Security & Privacy > FileVault)
- [ ] 4+ GB RAM
- [ ] Admin access to install VPN
- [ ] Modern browser with extension support

---

### For iPhone Users

- [ ] iOS 16 or later (recommended iOS 17+)
- [ ] 2+ GB free storage
- [ ] Active internet connection (WiFi or cellular)

---

### Internet and Network

- [ ] Stable internet connection at home (WiFi or cellular, ~5+ Mbps)
- [ ] Access to your router settings (admin credentials) — optional but useful for Phase 2 item 2.5
- [ ] Ability to pay for VPN subscription (credit card, prepaid card, or mail-in cash)

---

## Part 6: Final Phase 2 Readiness Decision

Based on Parts 1–5 above, assess your readiness:

### Phase 1 Completion Status

- **All 7 steps complete and stable?** [ ] Yes / [ ] No → If No, return to PHASE_1_COMPLETION_WALKTHROUGH.md

### Hardware and Environment

- **All devices encrypted?** [ ] Yes / [ ] No → If No, complete encryption before Phase 2
- **iPhone Advanced Data Protection enabled?** [ ] Yes / [ ] No → If No, enable before Phase 2
- **Router is Phase 2-compatible?** [ ] Yes / [ ] No / [ ] Unknown → Unknown is acceptable (can upgrade in Phase 2)

### Threat Model

- **Threat model is clear and specific?** [ ] Yes / [ ] Partially / [ ] No → Clarify using Part 3 before proceeding
- **Phase 2 spending is aligned with your threat level?** [ ] Yes / [ ] No → Reconsider if misaligned

### Resources

- **Time available for Phase 2 (5–7 hours)?** [ ] Yes / [ ] Partially / [ ] No → If No, delay Phase 2
- **Budget available (minimum $60/year)?** [ ] Yes / [ ] Partially / [ ] No → If No, Phase 2 can be delayed

---

### Phase 2 Readiness Verdict

| Condition | Status |
|-----------|--------|
| Phase 1 complete? | [ ] Yes / [ ] No |
| Disk encryption active? | [ ] Yes / [ ] No |
| Threat model clear? | [ ] Yes / [ ] No |
| Time available? | [ ] Yes / [ ] No |
| Budget available? | [ ] Yes / [ ] No |

**If all conditions are YES**: You are ready for Phase 2. Proceed to PHASE_2_EXECUTION_RUNBOOK.md.

**If any condition is NO**: You are not yet ready. Address the missing condition(s) before starting Phase 2:

1. **Phase 1 not complete**: Finish PHASE_1_COMPLETION_WALKTHROUGH.md steps 1.3–1.7
2. **Disk encryption not active**: Complete disk encryption for all devices
3. **Threat model not clear**: Revisit Part 3 (Threat Model Framing) in this document
4. **Time not available**: Schedule Phase 2 for when you have a free 1–2 week window
5. **Budget not available**: Start with minimum VPN setup (~$60/year) and add other items as budget allows

---

## Phase 2 Execution Timeline

Once you're ready, Phase 2 executes across roughly **4–8 weeks** depending on how you pace it:

| Week | Items | Hours |
|------|-------|-------|
| Week 1 | 2.1 Mullvad VPN + 2.2 ProtonMail | 2 hours |
| Week 1–2 | 2.3 Tor Browser + 2.4 Windows telemetry | 1.5 hours |
| Week 2–3 | 2.5 Linux encryption (if needed) | 1–2 hours |
| Week 3 | 2.6 iPhone Lockdown Mode + 2.7 Data broker automation | 0.5 hours |
| Week 4 | 2.8 Hardware security key (optional) + 2.9 iPhone SIM PIN | 0.5 hours |

**Phase 2 can overlap with Phase 1** if disk encryption is already running in the background.

---

## Next Steps

1. **Complete all checks in Part 1** — verify Phase 1 is stable
2. **Assess hardware prerequisites** (Part 2) — identify any gaps
3. **Clarify your threat model** (Part 3) — be specific about scenarios that apply
4. **Confirm time and budget** (Part 4) — set realistic expectations
5. **Make a readiness decision** (Part 6) — proceed to Phase 2 or address missing items

Once all sections are complete and you have a **"Phase 2 Readiness: YES"** verdict, proceed to **PHASE_2_EXECUTION_RUNBOOK.md**.

---

*Last updated: 2026-06-14*  
*Corresponds to PERSONAL_OPSEC_PLAN.md Phase 1→2 transition*
