---
title: "Personal OpSec Implementation Plan"
project: cybersecurity-hardening
created: 2026-05-16
status: active
threat-model: full-spectrum — government/mass surveillance (Palantir-style identity linking, bulk data collection, law enforcement data broker access) + targeted harassment/doxxing + general corporate tracking
devices: Windows (primary), iPhone/iOS, Linux (also used)
starting-point: scratch — no security tooling currently in place
depends-on: threat-model.md, opsec-playbook.md, implementation-guide.md, device-hardening-guide.md
---

# Personal OpSec Implementation Plan

**Who this is for**: You, starting from zero, on Windows as primary computer, iPhone as your mobile device, and Linux for some tasks.

**Threat model in plain terms**: You face three overlapping threats:
1. **Government/mass surveillance** — Palantir's ELITE and ICM platforms link your IRS records, Medicaid data, SSA data, DMV records, and commercial broker data into a single addressable profile. ICE and law enforcement can purchase your location data from ad brokers without a warrant. NSA collects internet metadata from backbone infrastructure. The DOGE cross-agency fusion architecture is partially operational.
2. **Targeted harassment/doxxing** — Human adversaries actively querying data broker sites to build your real-world profile, find your address, employer, family members. Often combined with social media OSINT.
3. **Corporate tracking** — Pervasive ad-SDK location harvesting, behavioral profiling, and commercial data aggregation that feeds directly into the government surveillance pipeline via Venntel, Babel Street, and others.

**Why these phases are structured this way**: Phase 1 items give you the most protection per hour spent and require no new purchases. Phase 2 requires some spending and more time but closes the most serious remaining gaps. Phase 3 is behavioral and permanent — it never "ends" but becomes habit.

---

## Phase 1 — Week 1: Foundation (~2–3 hours total)

These are the highest-leverage, lowest-disruption steps. Each one closes a major attack surface immediately. Do them in order.

---

### 1.1 — Signal: Encrypted Messaging (30 minutes)
**Platform**: iPhone + any future Android/Linux devices
**Cost**: Free

**Why it matters for your threat model**: The IRS LCA platform explicitly maps "social networks among investigation targets" using "communications metadata: calls, texts, emails." iMessage content can be subpoenaed from Apple via standard search warrant. SMS is entirely unencrypted and trivially logged. Signal's end-to-end encryption means that even if Signal's servers are subpoenaed, the government receives only your account creation date and last connection time — not message content, not contact lists.

**Exact steps**:
1. Download Signal from signal.org (iOS: App Store, search "Signal Private Messenger" by Signal Messenger LLC — verify the developer name)
2. Open Signal, tap Continue, register with your phone number, set a 6+ digit PIN when prompted
3. **Settings > Profile** — tap the @ symbol field and create a username (e.g., a word + number, nothing tied to your real name)
4. **Settings > Privacy > Phone Number > Who can see my number** — set to **Nobody**
5. **Settings > Privacy > Phone Number > Who can find me by my number** — set to **Nobody**
6. **Settings > Privacy > Default Timer for New Chats** — set to **1 Week**

**Verify it worked**: Ask someone to search for you in Signal using your phone number — they should find nothing. Your @username is what you share with contacts instead.

**Do not**: Accept QR code invitations to Signal groups from links sent over other apps or email. This was the primary 2025 attack vector (NSA warning, February 2025) — attackers send fake group invite QR codes that add an adversary-controlled device to your conversation.

---

### 1.2 — iPhone: Disable Advertising ID and Lock Down Tracking (20 minutes)
**Platform**: iPhone
**Cost**: Free

**Why it matters for your threat model**: ICE filed a formal procurement request in January 2026 explicitly seeking ad-tech data — mobile advertising identifiers (MAIDs) harvested by app SDKs. Venntel collected location data from ~17 billion daily signals across ~1 billion devices via advertising SDKs and sold it to ICE without warrants. Your iPhone is broadcasting your location to data brokers through apps you've installed. This step partially severs that pipeline.

**Exact steps**:
1. **Settings > Privacy & Security > Tracking** — toggle **"Allow Apps to Request to Track"** to OFF. This prevents apps from asking permission to track you across other apps.
2. **Settings > Privacy & Security > Location Services** — audit every app:
   - Navigation apps (Maps, Google Maps): "While Using" is acceptable
   - Every other app: change to **Never** or **While Using** at most
   - **Settings > Privacy & Security > Location Services > System Services** — disable: "iPhone Analytics," "Routing & Traffic," "Improve Maps," "Product Improvement"
3. **Settings > Privacy & Security > Apple Advertising** — toggle **"Personalized Ads"** to OFF
4. **Settings > [your name] > iCloud > Advanced Data Protection** — enable this. It end-to-end encrypts your iCloud backups, photos, notes, and messages. Apple cannot decrypt them under a search warrant. Save the recovery key to a physical piece of paper stored somewhere secure (not your phone, not cloud).

**Estimated time**: 20 minutes.

**Important**: After enabling Advanced Data Protection, go to **Settings > [your name] > iCloud** and disable iCloud backup for these specific apps if ADP is not available or you want belt-and-suspenders protection: Messages, Health, and any app that holds sensitive information.

---

### 1.3 — Windows: Enable BitLocker Disk Encryption (15 minutes)
**Platform**: Windows
**Cost**: Free (included in Windows 10/11 Pro; Home may require upgrade — see note)

**Why it matters for your threat model**: FBI and law enforcement conduct device seizures. Full-disk encryption means a seized powered-off laptop yields nothing without your passphrase. Without encryption, any powered-off device is trivially readable.

**Exact steps**:
1. Search "Manage BitLocker" in the Windows Start menu and open it
2. Click "Turn on BitLocker" for your C: drive
3. **Critical**: When asked where to save your recovery key, choose **"Save to a file"** and save it to an external USB drive or print it. Do NOT save it to your Microsoft account — that defeats the purpose, since Microsoft can then be compelled to provide it.
4. Choose "Encrypt entire drive" (not just used space)
5. Choose "New encryption mode" for a fixed internal drive
6. Check "Run BitLocker system check" and click Continue
7. Restart when prompted. Encryption runs in the background — let it complete before using the laptop for anything sensitive.

**Verify it worked**: After restart, search "Manage BitLocker" again — the C: drive should show "BitLocker on."

**Note on Windows Home**: BitLocker is available on Windows 10/11 Pro but not Home. If you have Home edition, use VeraCrypt instead: download from veracrypt.fr, run the installer, and create a "system encryption" that encrypts your entire Windows drive. VeraCrypt is free and open source.

**After this step**: Your laptop is protected against physical seizure when powered off. Make sure you actually power it off (not just sleep) before leaving it anywhere.

---

### 1.4 — iPhone: Switch from SMS 2FA to Authenticator App (30 minutes)
**Platform**: iPhone
**Cost**: Free

**Why it matters for your threat model**: SIM swapping — where an attacker convinces your carrier to transfer your phone number — lets them intercept every SMS-based 2FA code, taking over every account that uses your phone number for recovery. This is how email, social media, and banking accounts get compromised. T-Mobile paid $33 million in arbitration in 2025 over a SIM swap.

**Exact steps**:
1. Download **Ente Auth** from the App Store (open source, encrypted, better than Google Authenticator)
2. For each important account (email, financial accounts, any social media), go into that account's security settings and find "Two-factor authentication" or "Two-step verification"
3. Switch from "SMS" to "Authenticator app" — scan the QR code with Ente Auth
4. Save the backup codes each service provides — put them in a document on your encrypted laptop or print and store physically

**Priority order for switching**: email accounts first (Gmail, Outlook, etc.), then financial accounts, then social media.

**Also do this on your carrier's account**:
- AT&T: Call customer service and ask to enable "Extra Security" (requires a passcode for any account changes)
- T-Mobile: In the T-Mobile app, go to Profile > Security > SIM Protection and enable it
- Verizon: Log into My Verizon > Security > Enable Number Lock
This prevents SIM swapping even if someone calls your carrier impersonating you.

---

### 1.5 — Password Manager Setup (30 minutes)
**Platform**: Windows (primary) + iPhone
**Cost**: Free (Bitwarden) or free self-hosted

**Why it matters for your threat model**: Account takeover is a documented law enforcement and harassment technique. A credential breach at one site exposing your reused password can cascade to every account. A password manager eliminates password reuse and lets you use truly random passwords.

**Exact steps**:
1. Download **Bitwarden** from bitwarden.com — install the desktop app on Windows and the iOS app on iPhone
2. Create an account with a strong master password (6+ random words — think of a nonsensical phrase like "trumpet-gallop-mountain-fern-47"). Write this down and store it physically.
3. Enable two-factor authentication on Bitwarden itself using Ente Auth (from step 1.4)
4. Install the Bitwarden browser extension in your browser
5. Start importing existing passwords or saving new ones as you log in to sites

**Alternative for higher security (no cloud)**: Use **KeePassXC** (keepassxc.org) instead — stores everything locally on your device, never in any cloud. Slightly more friction for accessing passwords across devices, but zero cloud exposure.

---

### 1.6 — Data Broker Opt-Outs: First Wave (45 minutes)
**Platform**: Any browser
**Cost**: Free (manual); ~$96/year for automated service

**Why it matters for your threat model**: Palantir's ELITE platform generates address confidence scores by pulling from LexisNexis, DMV records, and commercial data brokers. ICE's law enforcement data product pipeline purchases data from BeenVerified, Spokeo, and Intelius-type services without warrants. Doxxers use exactly these same sites to find your address, phone, and relatives. Removing yourself from them degrades both threat vectors simultaneously.

**Submit all of these in the same sitting. Open each in a separate tab:**

| Site | Opt-Out URL | Time |
|------|-------------|------|
| LexisNexis (highest priority — confirmed ICE contract) | https://optout.lexisnexis.com/ | 5 min (may require ID upload) |
| BeenVerified | https://www.beenverified.com/app/optout/search | 3 min |
| Spokeo | https://www.spokeo.com/optout | 3 min |
| WhitePages | https://www.whitepages.com/suppression-requests | 3 min |
| Intelius | https://www.intelius.com/opt-out/ | 3 min |
| TruePeopleSearch | https://www.truepeoplesearch.com/removal | 2 min |
| FastPeopleSearch | https://www.fastpeoplesearch.com/removal | 2 min |
| FamilyTreeNow | https://www.familytreenow.com/optout | 2 min |
| Radaris | https://radaris.com/page/how-to-remove | 3 min |
| Acxiom | https://isapps.acxiom.com/optout/optout.aspx | 3 min |

**Also submit these federal opt-outs while you're at it** (2 minutes total):
- https://www.optoutprescreen.com — removes you from pre-screened credit/insurance offer lists
- https://optout.networkadvertising.org — browser-based ad network opt-out (do in every browser you use)
- https://optout.aboutads.info — same as above, different member networks

**Verification** (2–4 weeks later): Search your name + city on BeenVerified and Spokeo in a private browser window. Re-submit for any that still show your record.

**Note**: These brokers re-add records from public sources every 3–6 months. You need to re-submit quarterly, or use an automated service. See Phase 2 for that.

---

### 1.7 — iPhone: Passcode Over Biometrics for Lock Screen (5 minutes)
**Platform**: iPhone
**Cost**: Free

**Why it matters for your threat model**: In most U.S. jurisdictions, law enforcement can compel you to use your fingerprint or face to unlock a phone by court order — but compelling you to reveal a PIN is contested as testimonial under the Fifth Amendment. A PIN you refuse to provide is more legally defensible than a face you can't hide.

**Exact steps**:
1. **Settings > Face ID & Passcode** — scroll down and under "Use Face ID For," disable **"iPhone Unlock"**
2. Confirm your passcode is 6+ digits (ideally a custom alphanumeric passcode — tap "Change Passcode" > "Passcode Options" > "Custom Alphanumeric Code")

**Quick-disable Face ID in an emergency**: Press the side button and one of the volume buttons simultaneously — this triggers the Emergency SOS screen and disables Face ID until you enter your passcode. Practice this gesture until it's muscle memory.

**iOS Inactivity Reboot**: iOS 18 automatically reboots your iPhone if it hasn't been unlocked for 72 hours, putting it into "Before First Unlock" (BFU) state where forensic tools can't extract data. This is enabled by default. Keep your iOS updated to maintain this protection.

---

## Phase 2 — Weeks 2–4: Hardening (~6–10 hours + some spending)

Phase 1 handled the broadest immediate exposures. Phase 2 closes the next tier of gaps — the ones that require either more setup time or some spending.

---

### 2.1 — Mullvad VPN: Always-On with Kill Switch (1 hour)
**Platform**: Windows + iPhone + Linux
**Cost**: ~$5/month (Mullvad) — **PAID**
**How to pay anonymously**: Mullvad accepts cash mailed to their office. Generate a Mullvad account number first (no email required), then mail physical cash in an envelope to their address at https://mullvad.net/help/sending-cash/. Alternatively, buy a prepaid Visa gift card with cash and use that.

**Why it matters for your threat model**: Your ISP can see every site you visit and can be compelled via NSL (no warrant required) to provide connection records. Commercial location data from ISP behavioral profiling feeds into data broker ecosystems. A VPN shifts that visibility to Mullvad, which is in Sweden (outside U.S. jurisdiction for routine legal process), operates with no-log architecture confirmed by Swedish law enforcement attempting to obtain data and finding nothing, and requires no identifying information to create an account.

**Why Mullvad specifically**: ProtonVPN is a good alternative, but Mullvad has the strongest court-verified no-log track record and the cleanest account anonymity model (no email, just a random account number).

**Exact steps — Windows**:
1. Go to mullvad.net, click "Get started" — a 16-digit account number is generated immediately. **Save this number in your password manager right now.** There is no email address, no password — this number is your entire account.
2. Add payment time via cash mail or prepaid card
3. Download the Mullvad app for Windows from mullvad.net/download
4. Install, enter your account number, click Connect
5. **Settings > VPN settings** — confirm Kill switch is ON (it is by default and cannot be turned off — this is correct)
6. Select a server in Sweden or Netherlands for GDPR jurisdiction protection

**Exact steps — iPhone**:
1. Download Mullvad from the App Store
2. Enter your account number
3. Enable the VPN and set it to always-on: **iOS Settings > General > VPN & Device Management > VPN > your Mullvad configuration > Connect On Demand** — enable this

**Verify no leaks**: With Mullvad connected, go to https://mullvad.net/check — it should show "You are connected to Mullvad" and your real IP should not appear.

**Linux**: Download the Mullvad app from mullvad.net/download/linux or install via the package manager instructions on their site.

---

### 2.2 — Email: Move Sensitive Communication to ProtonMail (1 hour)
**Platform**: Windows, iPhone, Linux
**Cost**: Free tier is sufficient to start

**Why it matters for your threat model**: NSA PRISM compels Google, Microsoft, and Yahoo to provide stored email content under Section 702. FBI can compel email content with a standard search warrant. ProtonMail is incorporated in Switzerland and uses zero-knowledge encryption — they cannot decrypt your emails even if subpoenaed. (Note: they have complied with Swiss court orders for IP addresses. Use a VPN when accessing ProtonMail to prevent IP logging.)

**Exact steps**:
1. Go to proton.me with Mullvad VPN connected (so Proton doesn't log your real IP)
2. Create an account with a username unconnected to your real identity — not your real name, not a name derived from your existing email address
3. Use this address for: Signal registration going forward, any service connected to sensitive activity, communications with lawyers or advocacy organizations
4. Continue using your existing email for: Amazon, bills, work, anything where your real identity is already established anyway
5. On iPhone: download the Proton Mail app; use it for the sensitive address

**Higher privacy**: When creating the account, access proton.me via Tor Browser (see 2.3 below) rather than just the VPN. This prevents Proton from logging any IP that could be traced to you.

---

### 2.3 — Tor Browser for Sensitive Research (30 minutes setup)
**Platform**: Windows + Linux
**Cost**: Free

**Why it matters for your threat model**: NSA backbone surveillance intercepts internet metadata. Browsing from your home IP creates a permanent record of what you've researched. Tor routes your traffic through three relays, so no single party can see both who you are and what you're visiting.

**Exact steps**:
1. Download Tor Browser ONLY from https://www.torproject.org/download — do not download from any other source
2. Install normally on Windows or Linux
3. Open Tor Browser, click the **shield icon** in the toolbar, set security level to **Safest** (this disables JavaScript, which is the primary category of browser exploit used to deanonymize Tor users)

**The VPN-then-Tor sequence** (always do this when using Tor):
1. Connect Mullvad first
2. Then open Tor Browser
This hides your Tor usage from your ISP. Without the VPN first, your ISP can see you're using Tor.

**Use Tor for**: Researching sensitive topics, creating accounts that shouldn't be linked to your identity, accessing .onion services (SecureDrop, ProtonMail's .onion address).

**Do not do in Tor Browser**: Log into any account linked to your real identity. Even one login destroys the anonymity for that session.

**Behavioral rules**:
- Don't resize the browser window (fingerprinting)
- Don't install extensions
- Don't open downloaded files outside Tor Browser

---

### 2.4 — Windows: Disable Telemetry and Data Collection (30 minutes)
**Platform**: Windows
**Cost**: Free

**Why it matters for your threat model**: Windows telemetry sends usage data to Microsoft by default, including app usage, browsing behavior, location data, and diagnostics. This data can be subpoenaed and feeds into commercial data broker ecosystems.

**Exact steps**:
1. **Settings > Privacy & security > Diagnostics & feedback** — set "Diagnostic data" to **Required diagnostic data only**, disable "Improve inking and typing," disable "Tailored experiences"
2. **Settings > Privacy & security > Activity history** — disable "Store my activity history on this device," clear activity history
3. **Settings > Privacy & security > Search permissions** — disable "Cloud content search," disable "Search history on this device"
4. **Settings > Privacy & security > App permissions** — go through each category (Location, Camera, Microphone, etc.) and disable access for any app that doesn't legitimately need it
5. **Settings > Privacy & security > Location** — disable "Location services" for the desktop (you can leave it on for iPhone; this is specifically for Windows)
6. Search for "Advertising ID" in Settings — **Settings > Privacy & security > General** — toggle "Let apps show me personalized ads by using my advertising ID" to OFF

**Also do**:
- **Settings > Windows Update > Advanced options > Optional updates** — leave security updates on but disable feature updates until you've reviewed what they add
- Consider using **O&O ShutUp10++** (free, from oo-software.com) — a dedicated Windows privacy tool that provides a single dashboard to disable telemetry settings. Run it after following the manual steps above.

---

### 2.5 — Linux: Full-Disk Encryption (if not already enabled)
**Platform**: Linux
**Cost**: Free

**Why it matters**: Same as Windows BitLocker — physical device seizure protection. On Linux the tool is LUKS.

**If you're setting up a new Linux installation**: During installation, select "Encrypt the installation" or "Use LUKS encryption" — this is a checkbox in most installers (Ubuntu, Fedora, Debian). Do this during installation; it's much harder to add afterward.

**If your Linux is already installed without encryption**: The cleanest path is to back up your data, reinstall with LUKS encryption enabled during setup, and restore. On a running system, `/home` encryption can be added separately, but it's complex. Reinstall is simpler.

**Passphrase choice**: Use a 6-word diceware passphrase for LUKS — longer and more memorable than a random character string. Generate one at https://thewordlist.net or roll dice with the EFF word list at https://eff.org/dice.

---

### 2.6 — iPhone: Enable Lockdown Mode (5 minutes, if warranted)
**Platform**: iPhone
**Cost**: Free

**Why it matters for your threat model**: Lockdown Mode (iOS 16+) is Apple's hardening mode against commercial spyware (Pegasus, Predator) and aggressive exploit delivery. It blocks most dangerous attachment types in Messages, restricts Safari's JavaScript JIT compiler (dramatically reduces browser attack surface), disables wired connections to accessories when locked, and blocks FaceTime from non-contacts.

**Trade-offs**: Some websites break. Some attachments won't open. Link previews are blocked in Messages. These are acceptable for someone in your threat model.

**Enable at**: Settings > Privacy & Security > Lockdown Mode > Turn On Lockdown Mode. Requires a device restart.

**When to enable**: Now if you attend protests, organize publicly, or have any elevated risk of being targeted. The usability cost is real but manageable.

---

### 2.7 — Data Broker Opt-Outs: Automation (15 minutes setup)
**Platform**: Any browser
**Cost**: ~$96/year (Incogni) or ~$20/year (EasyOptOuts) — **PAID**

**Why it matters**: Data brokers re-add your records from public sources every 3–6 months. Phase 1's manual opt-outs will expire. Automated services continuously re-submit removals.

**Recommended**:
- **Incogni** (incogni.com, ~$96/year): Covers 420+ brokers with 60-day re-submission cycles. Deloitte-verified process — the only service with independent third-party verification. Pay with a prepaid Visa gift card if you want to keep this account unlinkable to your identity.
- **EasyOptOuts** (~$20/year): Lower cost, good for maintaining the manual opt-outs from Phase 1. More limited coverage.

**To pay without identity linkage**: Buy a prepaid Visa or Mastercard gift card with cash at a gas station or drugstore. Use that card to pay for the service. Use a Proton Mail address (not your real email) to create the account.

---

### 2.8 — Second-Factor Hardening: Hardware Security Key (optional, 30 minutes)
**Platform**: Windows, iPhone (with adapter or NFC), Linux
**Cost**: ~$55 for a YubiKey 5 NFC — **PAID**

**Why it matters for your threat model**: Account takeover (getting into your email, cloud storage, or social media) is a documented harassment and investigation technique. Even with an authenticator app, phishing can capture TOTP codes. A hardware security key requires physical possession — a phishing page cannot extract it. It's immune to remote account takeover even if your password is known.

**Purchase**: From yubico.com directly — do not buy from third-party Amazon Marketplace sellers (supply chain risk). The YubiKey 5 NFC works with iPhone via NFC and with Windows/Linux via USB-A.

**Set up on**: Email (Gmail and Outlook both support it), Bitwarden (under Account > Security > Two-step Login), Proton Mail (Settings > Security > Two-factor authentication).

---

### 2.9 — iPhone: SIM PIN (5 minutes)
**Platform**: iPhone
**Cost**: Free

**Why it matters**: A SIM PIN prevents someone who physically has your iPhone from removing the SIM and using it in another device. It's a secondary layer after the port-out PIN from Phase 1.

**Exact steps**: Settings > Cellular > SIM PIN > Enable SIM PIN. Set a 6-digit PIN different from your phone passcode. You'll be prompted for this PIN each time you restart the phone.

---

## Phase 3 — Ongoing: Advanced Operational Security

Phase 3 items are not one-time setup tasks. They are habits and behavioral changes that become permanent parts of how you operate. Many of them will feel like significant friction at first and natural after a few months.

---

### 3.1 — Device Discipline: One Device, One Identity
**Platform**: All
**Effort**: High behavioral change required

**The rule**: Do not log into accounts associated with one purpose from a device or account associated with another purpose. "Separate browser profiles on the same device" does not count — that's trivially linkable by IP, timing, and browser fingerprint.

**What this means in practice**:
- Don't log into any activist-related accounts (Signal with sensitive contacts, Proton Mail, organizing platforms) from a device also signed into your personal Google/Apple account, work email, or anything tied to your real identity
- If you need true compartmentalization, it requires a separate device for sensitive activity — a used iPhone or Android purchased with cash, activated with a VoIP number, running no apps that link to your identity. See the next item.
- At minimum: don't mix sensitive Signal conversations with personal apps on the same device without understanding that all of that device's data is a single package if the device is seized

**Why this matters**: Palantir's entity resolution links identities across data points. A single shared data point — same IP, same payment method, same physical location when both devices are powered on — connects your identities.

---

### 3.2 — Leave Your Phone at Home for High-Stakes Situations
**Platform**: iPhone
**Effort**: Medium — requires planning ahead

**The rule**: When attending any protest, sensitive meeting, organizing session, or event you don't want permanently recorded in government databases, leave your phone at home or power it fully off and put it in a Faraday bag.

**Why this matters**: Every app with an advertising SDK (which is nearly every app) is logging your GPS location and broadcasting it to data brokers who sell it to law enforcement. ICE filed a formal market research request in January 2026 specifically for MAID-linked ad-tech location data. Venntel collected ~17 billion daily location signals and sold them to DHS without warrants. Your phone at a protest is a permanent, warrantless government record that you were there.

**The Faraday bag option**: A certified Faraday bag (Mission Darkness or GoDark, ~$50–$80) blocks all cellular, WiFi, Bluetooth, and GPS signals. Test it by calling the phone after putting it in the bag — if it rings, the bag doesn't work. A Faraday bag stops future tracking but does not erase data already collected.

**iOS-specific warning**: If "Find My" is enabled, your iPhone continues to broadcast a rotating Bluetooth beacon for up to 24 hours after being powered off (confirmed Apple feature, iPhone 11+). To stop this: Settings > [your name] > Find My > Find My iPhone — turn off before powering down, then power down.

**Pattern of life**: Vary your routes, times, and locations for routine activities. Palantir ELITE's address confidence scoring works by correlating your historical location patterns to predict where you currently are. Randomizing movement degrades that prediction significantly.

---

### 3.3 — Disable 2G on iPhone (Prevents IMSI Catchers)
**Platform**: iPhone
**Cost**: Free
**Effort**: 2 minutes, permanent

**Why it matters**: Cell-site simulators (Stingrays/IMSI catchers) impersonate cell towers, forcing nearby phones to reveal their location and identity. They work by forcing a downgrade to 2G, which is trivially interceptable. ICE, FBI, DEA, NSA, Secret Service, U.S. Marshals, and military all operate them. ICE and DHS have deployed them without following their own internal rules.

**Exact steps**: Settings > Cellular > Cellular Data Options > Voice & Data — select **LTE** or **5G** only (do not select "Enable 3G" or leave 2G available). On newer iPhones: Settings > Cellular > Cellular Data Options — ensure "Prefer 5G" or "LTE" is selected and 2G is not in the options chain.

---

### 3.4 — Physical Security Practices: Before Law Enforcement Encounters
**Platform**: iPhone + Linux/Windows
**Effort**: Habit change

**Power-off discipline**: Before any situation where device seizure is possible (border crossings, protests, traffic stops in high-risk contexts, any situation where you might be detained), **power the phone fully off**. Not sleep, not airplane mode — fully off.

**Why**: When your iPhone is powered on but locked, it is in "After First Unlock" (AFU) state — encryption keys are in memory. Cellebrite and similar tools can extract data from an AFU device. When powered off, the phone is in "Before First Unlock" (BFU) state — encryption keys are not in memory, and forensic tools cannot extract your data without your passcode. iOS 18 auto-reboots after 72 hours of inactivity for the same reason.

**The gesture to remember**: Side button + volume down simultaneously = Emergency SOS screen, which also disables Face ID. Memorize this. Practice it once.

**Border crossings specifically**: U.S. border agents have broader search authority than domestic law enforcement. Power off your phone before arriving at the checkpoint. If you are asked to unlock it, you have the right to decline — but agents can detain you and the device. Know this in advance so you can make an informed decision.

---

### 3.5 — Social Media Hygiene: Reduce OSINT Surface
**Platform**: All
**Effort**: Ongoing

**Why it matters**: Babel Street has confirmed FBI contracts up to $27 million for OSINT aggregation and social media monitoring. ImmigrationOS includes real-time social media monitoring with sentiment analysis. Palantir Gotham's OSINT capability is confirmed. Public social media posts are not just embarrassing — they are actively fed into the same systems generating address confidence scores and building social graphs.

**Exact actions**:
1. Audit all your public social media profiles: go through each one and look at what is visible to someone not following you. Remove or restrict: your location (especially city/neighborhood), your employer, family member names and relationships, and photos that show the exterior of where you live
2. On any platform with public posts: review the last 6 months of posts with the question "could this be used to identify my political views, religious beliefs, associations, or location patterns?" Flag anything you'd be uncomfortable with an ICE investigator reading
3. For Twitter/X, Instagram, Facebook: set accounts to private or remove them if you don't need them for anything specific
4. Never post real-time location ("at the march right now," "at this restaurant"). Post after you've left, if at all
5. Google your own name quarterly and look at what appears. Submit removal requests for anything you can opt out of

---

### 3.6 — Financial Compartmentalization
**Platform**: All
**Effort**: Medium — requires setting up separate payment methods

**Why it matters**: The IRS LCA platform ingests bank statements and financial transactions. Palantir's data integration connects financial records to identity via the DOGE-era cross-agency fusion architecture. Shared payment methods between your personal and any sensitive activity create a direct graph edge in Palantir's ontology.

**Practical steps**:
1. For any activity you want separated from your primary identity: use prepaid Visa or Mastercard gift cards purchased with cash. These are available at pharmacies and grocery stores. Use them for: VPN subscriptions, data broker removal services, any service connected to sensitive activity
2. Do not use Venmo, Cash App, or Zelle for sensitive transactions — these services are subpoena-able and maintain permanent transaction records
3. For ongoing recurring payments connected to sensitive activity (VPN, encrypted email): get a single prepaid card and reload it with cash as needed, rather than using a reloadable card linked to your bank

---

### 3.7 — Document Metadata Stripping Before Sharing
**Platform**: Windows + Linux
**Effort**: Low — becomes habit
**Cost**: Free

**Why it matters**: Every Word document, PDF, and photo you create and share may contain your name, GPS coordinates, the name of your machine, edit history, and creation timestamps. This metadata is embedded in the file and travels with it. A document shared with a journalist, lawyer, or advocacy organization could expose your identity through metadata even if the content is anonymized.

**Exact steps (Windows)**:
1. Download ExifTool from exiftool.org — install the Windows executable
2. Before sharing any document: right-click the file, run ExifTool to strip metadata
   - From command prompt: `exiftool -all= -overwrite_original document.docx`
3. For photos: always strip GPS data before sharing — `exiftool -gps:all= photo.jpg`

**For Word documents specifically**: File > Info > Check for Issues > Inspect Document — this shows you exactly what metadata is embedded and lets you remove it from within Word before saving.

**Also**: Configure your camera to not save GPS location. iPhone: Settings > Privacy & Security > Location Services > Camera > **Never**.

---

### 3.8 — Quarterly Maintenance Schedule
**Platform**: All
**Effort**: Low — ~1 hour per quarter

**Why maintenance matters**: Data brokers re-add your records quarterly. Tools have vulnerabilities patched in updates. The threat landscape changes — new Palantir contracts, new surveillance capabilities, new legal rulings.

**Each quarter, do**:
1. Re-submit data broker opt-outs for the top 5 priority sites (BeenVerified, Spokeo, WhitePages, Intelius, Radaris) in a 15-minute batch
2. Update all software: iOS (Settings > General > Software Update), Windows (Settings > Windows Update), any security tools
3. Verify Mullvad is still working: connect VPN, go to https://mullvad.net/check, confirm no leaks
4. Review Signal: update the app, verify Safety Numbers with your highest-trust contacts if you haven't done so recently
5. Check EFF Deeplinks (eff.org/deeplinks) and 404media.co for new surveillance tool reporting that might affect your setup

**Each year**:
1. Rotate your Mullvad account number (create new, transfer payment, discard old — limits accumulated metadata)
2. Reassess your threat level: has your public profile changed? Have you attended events or engaged with organizations that raise your exposure?
3. Review the threat-model.md in this directory for updates to Palantir's confirmed capabilities

---

### 3.9 — Know Your Legal Resources Before You Need Them
**Platform**: N/A — preparation
**Effort**: 30 minutes to bookmark and identify

**Why it matters**: Technical measures protect you against passive surveillance. But if you receive a subpoena, a knock-and-talk from law enforcement, or a National Security Letter, you need legal support immediately. NSLs carry gag orders — you may not be able to tell anyone you received one. FBI NSLs require no judicial approval. By the time you're looking for a lawyer under pressure, it's too late to research.

**Bookmark these now**:
- **Electronic Frontier Foundation**: eff.org — legal defense fund, digital rights litigation
- **National Lawyers Guild**: nlg.org — legal support for activists, protest observers, people facing political prosecution
- **ACLU Digital Rights**: aclu.org/privacy-technology — surveillance law, compelled decryption litigation

**If approached by law enforcement**: You have the right to remain silent and the right to an attorney. "I want a lawyer and I'm exercising my right to remain silent" is a complete sentence. Do not explain yourself, do not answer questions, do not consent to searches. This applies even if you've done nothing wrong.

---

## Summary: What Each Phase Gives You

| After Phase 1 | After Phase 2 | After Phase 3 |
|---|---|---|
| Signal-encrypted communications | VPN shields ISP from your browsing | Compartmentalized identities across devices |
| iPhone tracking SDKs partially severed | ProtonMail for sensitive email (outside U.S. legal compulsion) | Social media OSINT surface reduced |
| iCloud data end-to-end encrypted | Tor Browser for sensitive research | Document metadata stripped before sharing |
| Laptop encrypted against physical seizure | Data broker removal automated | Financial separation for sensitive activity |
| SMS 2FA replaced (SIM swap resistance) | Windows telemetry reduced | Behavioral patterns randomized (ELITE scoring degraded) |
| Password manager eliminates credential reuse | Carrier port-out PIN set | Quarterly maintenance keeps tools current |
| First-wave data broker opt-outs submitted | Hardware key for highest-value accounts (optional) | Legal resources pre-identified |

---

## Spending Summary

| Item | Cost | When |
|------|------|------|
| Mullvad VPN | ~$5/month (~$60/year) | Phase 2 |
| Incogni data broker removal | ~$96/year | Phase 2 (optional but recommended) |
| Prepaid gift cards for anonymous payments | ~$10–$30 one-time | Phase 2 |
| YubiKey 5 NFC | ~$55 one-time | Phase 2 (optional) |
| Faraday bag (Mission Darkness or GoDark) | ~$50–$80 | Phase 3 (if high-risk situations apply) |
| **Total minimum (VPN only)** | **~$60/year** | |
| **Total comprehensive** | **~$250–$300 first year** | |

Everything in Phase 1 is free. The only required spending for meaningful protection is the VPN.

---

## What This Plan Does Not Cover

**What remains exposed after completing all three phases**:

1. **Your existing data broker profile**: Opt-outs are not retroactive. Law enforcement that has already purchased a copy of your data retains it. Opt-outs prevent future sales.

2. **Carrier metadata**: Your phone carrier always sees what towers your phone connects to, even with a VPN. This is the cell tower location record. A VPN does not prevent this.

3. **Vehicles**: Your car's license plate is read by ALPR networks feeding into Palantir ELITE. If you drive to locations you don't want in government databases, the car itself is a data source.

4. **Facial recognition in public spaces**: Clearview AI has a confirmed $9.2M ICE contract. There is no consumer opt-out for federal law enforcement queries. Physical countermeasures (N95 mask, full-brim hat, wraparound sunglasses) are the only available real-time mitigation in public spaces.

5. **Already-compiled SSA/IRS data**: The DOGE cross-agency fusion architecture has accessed SSA records with SCOTUS approval. Your SSN, employment history, and tax records are already in a system queryable by DHS. Technical measures cannot retroactively prevent this, but they can prevent new data points from being added to your profile.

6. **Targeted spyware**: If you believe you may be a target of commercial spyware (Pegasus, Predator) — which requires nation-state-level resources and intent — this plan's mobile security model is insufficient. You would need GrapheneOS (Android), device replacement, and security audit from a trusted organization.

---

*This plan is based on the confirmed threat capabilities documented in threat-model.md, opsec-playbook.md, implementation-guide.md, and device-hardening-guide.md as of May 2026. Reassess quarterly — the surveillance landscape and available tools both evolve. The goal is not perfect security; it is meaningful friction against the specific threat vectors that are actively and operationally deployed against people like you.*
