---
title: "Domestic Violence Survivor Safety and Digital Security Playbook: Technology Safety Planning for Survivors, Advocates, and Service Providers"
project: cybersecurity-hardening
created: 2026-05-06
status: scenario-specific-guide
phase: Phase 2
session: 844
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — threat claims grounded in documented DV patterns (NNEDV 50% of victim service providers report offenders use cellphone apps to stalk survivors; Coalition Against Stalkerware documented behavioral escalation risk when stalkerware is removed without safety planning; Apple Safety Check confirmed; shared family plan abuse documented in NNEDV national survey); safety planning framework validated by NNEDV Safety Net project and the DV services community; this playbook does not substitute for a trained DV advocate who knows the survivor's specific risk context
audience: Domestic violence survivors (all genders, all relationship contexts), DV advocates and shelter staff, legal service providers working with DV survivors, law enforcement victim advocates, healthcare providers encountering DV disclosures
---

# Domestic Violence Survivor Safety and Digital Security Playbook

**This playbook is not a substitute for working with a trained domestic violence advocate. The safety considerations in DV contexts are highly individual. A technical step that is appropriate for one survivor may put another at risk. Before taking any action described in this playbook, survivors are strongly encouraged to contact the National Domestic Violence Hotline (1-800-799-7233 or text START to 88788) or a local DV organization to develop an individualized safety plan.**

**If you are reading this on a device that may be monitored, you can quickly exit your browser by pressing Alt+F4 (Windows/Linux) or Command+W (Mac), or closing the browser tab. Clear your browsing history after reading.**

---

**Executive Summary for Survivors, Advocates, Shelter Staff, and Legal Service Providers**: This guide addresses the specific digital security challenges facing domestic violence survivors. The threat model in DV contexts is fundamentally different from every other scenario in this corpus — and that difference requires a different approach throughout.

In every other playbook in this collection, the adversary is a government agency, an employer, or an institutional actor with limited prior access to the target's devices and accounts. In DV contexts, the adversary is an intimate partner who may have purchased the device, set up the accounts, enrolled in the family plan, enabled location sharing, and installed monitoring software — all before any conflict arose. The abuser does not need to hack into anything. They were there first.

This asymmetry means that the standard advice — change your password, factory reset your phone, enable two-factor authentication — is not only insufficient but potentially dangerous if applied at the wrong time. A stalkerware app that suddenly stops reporting can alert an abusive partner that something has changed. A password changed on a shared account can trigger escalation. An Apple Find My location that goes dark can provoke a dangerous response.

**Safety planning comes before technical changes. Every time. Without exception.**

The goal of this playbook is to provide technically accurate, safety-conscious guidance that survivors can use in coordination with trained advocates. It is organized to reflect the actual decision sequence a survivor faces: first, understand the safety risk; second, take stock of the technical threats; third, act at a time and in a manner that supports safety rather than undermining it.

Three primary resources anchor this playbook and should be treated as living authorities:
- **National Domestic Violence Hotline**: thehotline.org | 1-800-799-7233 | Text START to 88788
- **NNEDV Safety Net Project** (technology safety for DV survivors): techsafety.org
- **Coalition Against Stalkerware**: stopstalkerware.org

---

## Part 1: Why This Threat Model Is Different

### 1.1 The Intimate Partner Adversary

Every other playbook in this corpus addresses threats from actors who must work to obtain access: they must query databases, obtain warrants, deploy surveillance technology, or conduct active monitoring operations. The domestic violence adversary has a qualitatively different starting position.

An intimate partner abuser may have:

- **Physical access to devices** — they may have purchased the phone, set it up, and known the passcode before the relationship became abusive. Even if the passcode was changed, they may have enrolled a fingerprint or face ID.
- **Account administrator access** — they may have set up the email address, Apple ID, or Google account used on the device. They may be listed as the account owner or recovery contact.
- **Family plan control** — they may be the account holder on the cellular plan. Family plans include built-in location sharing, call log visibility, and data usage monitoring that is accessible to the account holder by default.
- **Legal ownership of shared accounts** — financial accounts, streaming services, cloud storage plans, and other shared subscriptions may be legally in the abuser's name, giving them legitimate access the survivor cannot simply revoke.
- **Installed monitoring software** — stalkerware (apps like FlexiSPY, Hoverwatch, mSpy, or CocoSpy) can be installed on a device in minutes with physical access. Stalkerware runs invisibly, reports device activity to the installer, and is designed to resist detection and removal.
- **Smart home and vehicle access** — connected home devices (smart speakers, security cameras, smart locks, connected vehicles) may be linked to accounts the abuser controls.

None of these access vectors require technical sophistication. They are features of mainstream consumer technology that function exactly as designed — but that can be weaponized in an abusive relationship.

### 1.2 How This Differs From Government Surveillance

The other playbooks in this corpus address adversaries who are surveilling from a distance, without pre-existing access. The countermeasures appropriate for that threat model — hardening your existing device, strengthening your existing accounts, compartmentalizing your existing identity — are insufficient for DV contexts because they assume you start with clean, uncompromised infrastructure.

You may not. Your device may be monitored at the operating system level. Your accounts may have recovery options that route to the abuser. Your location may be shared via the cellular carrier account. Hardening a compromised device does not remove the compromise.

This is why several countermeasures in this playbook are unique:

- **Device replacement, not just hardening** — because stalkerware installed with root access can survive a factory reset in some configurations
- **New account creation on new devices** — because resetting passwords on existing accounts may not remove an abuser who has account recovery access
- **Safety planning as a prerequisite** — because technical changes can trigger behavioral escalation from an abusive partner
- **Documentation for court** — because the digital record of abuse can be essential evidence in protective order proceedings

### 1.3 The Escalation Risk

A finding consistent across DV advocacy literature and confirmed by the Coalition Against Stalkerware's guidance: **when an abuser detects that surveillance access has been disrupted, the risk of physical escalation increases.** A stalkerware app that stops reporting. A location that goes dark. A shared account that gets a password changed the abuser didn't authorize. These technical events can read to an abusive partner as the survivor "hiding something" or "planning to leave" — and the abuser's response may be physical.

This is not an argument against taking technical steps to protect yourself. It is an argument for timing those steps carefully, in coordination with a safety plan, at a moment when doing so creates maximum protection and minimum exposure to retaliatory violence. That timing decision belongs to you and your advocate — not to this playbook.

---

## Part 2: Safety Planning Before Technical Changes

**This section intentionally precedes the threat inventory. The safety planning framework establishes the context within which all technical decisions must be made.**

### 2.1 What Safety Planning Is

A safety plan is a personalized, practical plan developed with the help of a DV advocate that identifies the specific risks you face, the resources available to you, and the steps you can take — in the right sequence — to increase your safety. Safety planning is not a one-time event. It is an ongoing process that adjusts as your circumstances change.

Safety planning for DV technology safety specifically includes:
- Identifying which devices and accounts may be monitored
- Assessing the risk level of making specific technical changes at this time
- Determining what safe communication options are currently available to you
- Planning the timing of account separation and device transition
- Identifying a safe location and support network if you need to leave
- Documenting evidence of abuse in a way that doesn't alert the abuser

The NNEDV Safety Net project (techsafety.org) and its network of trained advocates are the authoritative resource for this process. Their technology safety planning framework has been developed specifically for DV contexts and is updated regularly. No playbook — including this one — can substitute for a trained advocate who understands your specific situation.

### 2.2 The Core Safety Planning Questions

Before taking any technical action described in this playbook, work through these questions with an advocate or on a device you know is safe (a shelter computer, a public library terminal, a trusted friend's phone):

**About your current situation**:
- Is it currently safe for you to make changes to devices or accounts?
- Does the abuser monitor your activity closely enough that a change would be immediately noticed?
- Are there children in the household whose devices or accounts may also be monitored?
- Does the abuser have a pattern of checking your phone, email, or account activity?

**About your exit planning**:
- Are you planning to leave, and if so, when?
- Do you have a safe place to go?
- Are the timing of your technical changes coordinated with your exit plan?
- Who else needs to be informed — children's school, workplace, healthcare providers?

**About evidence preservation**:
- Do you need to preserve digital evidence of abuse for a protective order or criminal proceeding?
- Is there evidence currently on your device or accounts that would be lost if you replace the device?
- Have you documented the evidence in a form that could be used in court?

**About your support network**:
- Who in your life knows about the situation and can be trusted with your safety plan?
- Does the abuser have access to the accounts of people in your support network?
- Is there a DV organization or shelter you have contacted or plan to contact?

### 2.3 Apple Safety Check: An Emergency Option for iPhone Users

Apple has built a safety-specific tool into iOS 16 and later called Safety Check (Settings > Privacy & Security > Safety Check). Safety Check has two modes:

**Emergency Reset**: Stops sharing everything immediately — location data, app permissions, iCloud access, shared AirDrop — with all people and all apps at once. Use this if you need to act immediately and cannot go through a step-by-step review.

**Manage Sharing & Access**: A guided review of what you are currently sharing and with whom, allowing you to make selective changes at your own pace.

Safety Check also includes a Quick Exit button that returns you immediately to the home screen if you need to hide that you are using it.

**Safety caveat**: Using Emergency Reset will immediately stop all location sharing. If an abuser is monitoring your location and it suddenly goes dark, this may trigger a response. Assess this risk with your advocate before using Emergency Reset. In some situations, a gradual transition (replacing the device, then disabling location sharing on the old device after you are in a safe location) is safer than an immediate shutdown.

### 2.4 Using a Safe Device for Safety Planning

Safety planning itself — including reading this guide, contacting the hotline, or communicating with an advocate — should be done on a device the abuser does not have access to. Options:

- A public computer at a library (use private/incognito browsing; clear history before leaving)
- A shelter computer
- A trusted friend's or family member's phone
- A prepaid phone purchased with cash (a new SIM and phone with no connection to shared accounts)

Do not use your primary phone or your home Wi-Fi connection for safety planning research if you have reason to believe either is monitored.

---

## Part 3: Threat Inventory — What May Be Compromised

After completing the safety planning conversation with an advocate, this section helps you take stock of what may be accessible to the abuser.

### 3.1 Stalkerware: The Primary Technical Threat

Stalkerware refers to software installed on a device — usually a smartphone — that runs invisibly in the background and reports the device's activity to the installer. Common capabilities include:

- Real-time GPS location reporting
- Text message and call log copies
- Email content access
- Social media message interception
- Screenshots at regular intervals
- Recording of calls and ambient audio
- Browser history
- Keylogging (recording everything typed)

**Common stalkerware products**: FlexiSPY, Hoverwatch, mSpy, CocoSpy, SpyBubble, KidsGuard Pro. Many are marketed as "parental monitoring" or "employee monitoring" tools and are commercially available.

**Installation requirements**: Most stalkerware requires a few minutes of physical access to an unlocked device. Some versions require "rooting" or "jailbreaking" the device (removing its software protections), which gives the stalkerware deep system-level access that survives factory resets. Other versions operate at a less privileged level and can be removed by a factory reset — but even then, restoring from a backup may reinstall the stalkerware if the backup contains it.

**Why factory reset alone is insufficient**: If stalkerware was installed after the device was rooted (and the abuser may have rooted it before giving you the phone), a factory reset may not remove it. The safest response to suspected stalkerware is device replacement, not remediation of the existing device.

**Stalkerware indicators**:
- **Battery drain**: Stalkerware that continuously transmits location and logs data uses battery power. Significant unexplained battery drain (especially when the phone appears idle) is a warning sign.
- **Unusual data usage**: Stalkerware transmits data to a remote server. Unexplained spikes in cellular data usage may indicate background reporting.
- **Device warmth**: A device that stays warm when idle may have background processes running.
- **Unfamiliar apps in device storage**: Some stalkerware is visible in the apps list under an innocuous name (like "Sync Manager" or "System Service"). Settings > Apps (Android) or Settings > Privacy > App Privacy Report (iOS) may reveal unexpected apps with access to location, microphone, or contacts.
- **The abuser's behavioral signal**: The most reliable indicator is not technical — it is behavioral. If the abuser consistently demonstrates knowledge of things they could only know from monitoring your device (where you went, who you called, what you texted), that is the strongest evidence of stalkerware, regardless of whether you can identify the app.

**Before attempting to remove stalkerware**: The Coalition Against Stalkerware explicitly recommends consulting with a DV advocate before removing stalkerware. Removal may alert the abuser. Evidence of stalkerware may also be needed for legal proceedings. The decision to remove, document, or leave in place pending a planned device transition should be made as part of your safety plan.

### 3.2 Location Tracking Vectors

Location tracking in DV contexts operates through multiple simultaneous channels, and addressing one without addressing the others leaves the survivor visible.

**Apple Find My / Family Sharing**: If you and the abuser are in the same Apple Family Sharing group, they may be able to see your location through Find My. Family Sharing is set up intentionally, often early in a relationship, and persists until explicitly removed. The account holder for the family group may also have administrative access to devices purchased through that account.

Removing yourself from Apple Family Sharing (Settings > [Your Name] > Family Sharing > tap your name > Stop Using Family Sharing) will stop location sharing through that channel — but see the safety caveat about sudden location disappearance above.

**Google Location Sharing**: Google Maps allows explicit location sharing between accounts. If location sharing was set up on your account, the abuser can see your location in Google Maps. Check: Google Maps > tap your profile photo > Location Sharing to see who you are currently sharing with.

**Google Timeline**: Google accounts with location history enabled record everywhere you have been. If the abuser has access to your Google account (via shared credentials, a recovery address, or a device logged into your account), they can review this history. Turn off location history: myaccount.google.com/data-and-privacy > Location history.

**Carrier family plan tracking**: Most major U.S. carriers offer family plan location sharing features (T-Mobile Scam Shield, AT&T FamilyMap, Verizon Smart Family). If the abuser is the account holder on your shared family plan, they may have access to carrier-level location tracking even if you have disabled all device-level location sharing. The only reliable countermeasure is leaving the shared plan and establishing an independent account with a new number.

**Connected vehicles**: Many modern vehicles have built-in GPS and remote access features accessible through a manufacturer app. If the vehicle account is in the abuser's name, or if they have credentials for the manufacturer's app, they may be able to track vehicle location, review trip history, or remotely lock/unlock the vehicle. This is documented in DV advocacy literature as an increasingly common control vector. Check your vehicle manufacturer's app/account settings with your advocate's assistance.

**AirTags and other tracking devices**: Small Bluetooth tracking devices (Apple AirTags, Tile trackers, Samsung SmartTags) can be hidden in bags, vehicles, or clothing. Apple devices running iOS 14.5+ will alert you to an unknown AirTag traveling with you (Settings > Privacy > Location Services > check for AirTag alerts; also check the Find My app). Android users can install the Tracker Detect app. Physically inspect your vehicle (wheel wells, bumper cavities, under seats), bags, and luggage if you suspect physical tracking.

### 3.3 Account Access Vectors

**Shared email accounts**: If the abuser has access to your primary email account — whether through shared credentials, a family plan email setup, or account recovery routing to their device — they can read incoming messages, intercept two-factor authentication codes sent to that address, and monitor your contacts and communications. This is a particularly dangerous single point of access because email is the recovery mechanism for most other accounts.

**Password manager access**: If you share a password manager account (or use one the abuser set up), they may have access to all stored credentials. This applies to built-in password managers in browsers (Chrome, Safari, Edge) as well as dedicated tools.

**Shared cloud storage**: A shared Google Drive, iCloud Drive, Dropbox, or OneDrive account gives the abuser access to files, photos, and documents. Auto-backup features may be sending photos and files from your device to a shared account automatically.

**Financial account visibility**: Shared bank accounts, credit cards, and payment apps (Venmo, CashApp, PayPal, Zelle) give the abuser real-time visibility into your transactions. Venmo transaction history is public by default unless explicitly set to private. Even a private Venmo account in a shared relationship may reveal transaction patterns (when you spend money, with whom, on what) that expose your activities or plans.

**Credit report access**: Credit monitoring services or identity protection services set up under a shared account may give the abuser access to your credit inquiries, new account openings, and address changes — which can reveal new housing arrangements.

**Two-factor authentication routing**: If 2FA codes for your accounts are sent to a phone number on the abuser's carrier account, or to an email address they can access, your 2FA provides no protection — they receive the codes.

---

## Part 4: Device Replacement Strategy

**Recommendation: In most DV situations where device compromise is suspected, device replacement is more reliable than device remediation.** This section explains why and how to execute a device transition safely.

### 4.1 Why Factory Reset Is Often Insufficient

A factory reset wipes the device's user-accessible storage and reinstalls the base operating system. In most cases, a factory reset will remove stalkerware installed at the app level. However:

- Stalkerware installed after the device was rooted (Android) or jailbroken (iOS) has system-level access that a standard factory reset may not fully remove. The tool may reinstall itself from a hidden partition.
- Restoring the device from a backup (iCloud backup, Google account restore) may reinstall the stalkerware if the backup was made after installation.
- A device that has been rooted or jailbroken has had its security protections permanently weakened, even after a factory reset.

The Coalition Against Stalkerware recommends: "It might be safest to get a new phone with an account the abuser doesn't have access to." For survivors who can access device assistance through a DV organization or shelter, this is the recommended path.

### 4.2 New Device Procurement

**Where to get a new device**:
- Many DV shelters and organizations maintain device donation programs or can assist with emergency device procurement
- The National Domestic Violence Hotline can connect you with local resources: 1-800-799-7233
- A basic Android phone (under $100 new, often available for less through donation programs) running a recent version of Android is sufficient for the account setup and communication security described in this playbook
- Prepaid phones purchased with cash at a retail store (Walmart, Target, Best Buy) have no carrier registration requirement that connects them to your identity through the shared plan

**Do not**:
- Restore a new device from an iCloud or Google account backup that was created while you were in the abusive relationship (the backup may contain the stalkerware or compromised account credentials)
- Use the new device on the same Wi-Fi network as the old device until the safety plan is fully executed (Wi-Fi network presence may be visible to the router's account holder)
- Sign into any account on the new device that the abuser has access to

### 4.3 New Carrier Account

If the abuser is the account holder on your current cellular plan, your new device should use a new, independent carrier account. This is how to break the carrier-level location sharing and call log access that family plan account holders have by default.

Options for a new independent account:
- A prepaid SIM from a carrier different from the shared plan carrier (T-Mobile, AT&T, Verizon, or prepaid options like Mint Mobile, Visible, TracFone)
- A prepaid phone with its own number, purchased at retail with cash, requires no credit check and no identity link to your abuser's account

**Important**: Porting your current phone number to a new carrier is possible but may generate account activity notifications visible to the abuser if the number is on their account. Getting a new number on the new device avoids this. Inform your support network and essential contacts of the new number using a safe communication channel.

### 4.4 What to Leave Behind

When transitioning to a new device, the following should not be transferred:
- Contacts from the compromised device (re-enter them manually from memory or a paper list, not from a sync)
- App data restored from backup (install apps fresh, do not restore from a cloud backup associated with compromised accounts)
- Accounts linked to the abuser or to shared infrastructure

What to bring:
- Evidence of abuse (photos, screenshots, messages) — but export these to a secure location before transitioning, not from within the compromised account ecosystem. See Part 8 on evidence documentation.
- Contacts you need that are not in your memory — write them down on paper before transitioning

### 4.5 Transition Timing

The timing of device replacement should be coordinated with your safety plan. Options include:

- **Before leaving**: Replace the device before the exit, using the new device as your primary communication tool for exit planning while continuing to use the old device for normal interactions that would appear monitored. This requires two devices simultaneously and requires discipline about which device is used for what.
- **During exit**: Replace the device as part of the exit, so the transition to new infrastructure happens at the same time you move to a safe location.
- **After leaving**: Replace the device once you are in a safe location, with advocate support.

Your advocate can help you assess which timing makes the most sense for your specific situation.

---

## Part 5: Account Separation and Access Control

Once you have a new device on an independent carrier account, this section walks through establishing clean digital infrastructure that the abuser cannot access.

### 5.1 New Email Account

The email account is the foundation of all other account security, because it is the recovery mechanism for everything else. Your new email must be:

- Created on your new device
- Not listed as a recovery option in any account the abuser has access to
- Not shared with the abuser under any circumstances

**Recommended**: Create a new ProtonMail account (proton.me — end-to-end encrypted, Swiss jurisdiction) or a new Gmail account that the abuser has never seen and that uses your new phone number (not your old number or any shared number) for 2FA.

**Do not** use your existing email account as the recovery mechanism for any new accounts. The point of the new email is clean separation.

### 5.2 Password Manager

A password manager stores and generates unique, strong passwords for all your accounts. The goal is to have no password that the abuser knows or could guess.

**Bitwarden** (bitwarden.com) is recommended for DV contexts:
- Free tier is sufficient for personal use
- Open-source and independently audited
- Cross-platform (works on any new phone)
- Self-hostable for high-security needs, but cloud-hosted for most users is appropriate

When setting up Bitwarden (or any password manager) on your new device:
- Use your new email address as the account email
- Use a strong master password the abuser would not know or guess (not a birthday, not a pet's name, not any shared password pattern)
- Do not install Bitwarden on the compromised device

### 5.3 Two-Factor Authentication Strategy

Two-factor authentication adds a second verification step when logging in. For DV survivors, the specific concern is that 2FA codes routed to a compromised phone number or email are accessible to the abuser.

**Use an authenticator app, not SMS, where possible**: Apps like Aegis Authenticator (Android, open-source) or Raivo OTP (iOS) store 2FA codes on the device and are not routable to anyone else. Unlike SMS codes, they cannot be intercepted through the carrier account.

**For accounts that require SMS 2FA**: Use your new phone number (on the new independent carrier account). The abuser's access to your old number does not give them access to codes sent to your new number.

**Recovery codes**: When setting up 2FA on any account, you will typically be offered one-time recovery codes. Print these or write them down and store them in a physically secure location (a DV shelter safe, with a trusted advocate). Do not store them in the cloud using a compromised account.

**Trusted recovery contacts**: Do not list the abuser or anyone the abuser controls as a trusted recovery contact for any account.

### 5.4 Shared Account Audit

Work through this list of accounts that may give the abuser visibility or access. For each, determine whether to close, separate, or change credentials. Your advocate can help with timing and safety considerations for each:

| Account Type | What the Abuser May Access | Action |
|---|---|---|
| Shared bank accounts | All transactions, balance, account statements | Open individual account at a different bank; consult with DV advocate re: legal rights to shared funds |
| Venmo / CashApp / Zelle | Transaction history, contacts, amounts | Create new account under new email; set Venmo transactions to private |
| Shared streaming services | Viewing history (minor); may reveal new address if billing updated | Separate billing; create new profile |
| Shared iCloud / Google account | Photos, location, messages, backups, Find My | New accounts on new device only; do not sign into old accounts on new device |
| Credit monitoring / identity protection | Address changes, new accounts, credit inquiries | Do not share this service; close or separate |
| Amazon / online retail | Shipping address (reveals new location) | Create new account; use shelter or trusted address for shipping |
| Social media | Can be monitored; new contacts may be visible | Review privacy settings; consider new accounts with new email |
| Email | All messages; 2FA codes | New account is the primary step; do not forward from old account |

### 5.5 Credit Freeze

A credit freeze (also called a security freeze) prevents new credit accounts from being opened in your name without your authorization. In a DV context, this prevents the abuser from:
- Opening new credit accounts in your name (financial abuse)
- Monitoring credit inquiries if they have access to a joint credit monitoring service

Place a credit freeze at all three bureaus:
- **Equifax**: equifax.com/personal/credit-report-services/ or 1-800-349-9960
- **Experian**: experian.com/freeze/center.html or 1-888-397-3742
- **TransUnion**: transunion.com/credit-freeze or 1-888-909-8872

A credit freeze is free and does not affect your existing accounts or credit score. It does not affect your ability to use existing credit cards. If you need to apply for new credit (for housing, employment), you can temporarily lift the freeze.

---

## Part 6: Location and Network Privacy

This section addresses the multiple channels through which your location may be visible to an abusive partner and the steps to close each one. Complete these steps in the order appropriate to your safety plan — not necessarily the order listed here.

### 6.1 Disabling Location Sharing — Comprehensive Checklist

**Apple Find My**: Settings > [Your Name] > Find My > check "Share My Location" and who it is shared with. Turn off sharing with the abuser directly. If you are in a Family Sharing group with the abuser, removing yourself from the group will stop Find My sharing for that group.

**Google Location Sharing**: In Google Maps, tap your profile photo > Location Sharing. Review who can see your location. Select any entry for the abuser and stop sharing.

**Google Maps Timeline / Location History**: myaccount.google.com/data-and-privacy > Location History. Turn off. Consider deleting past location history as well.

**Carrier family plan tracking**: Log into your carrier account (or have your advocate assist) and check for any family location sharing features. If you are on someone else's account as a dependent, the account holder retains visibility. The only reliable solution is leaving the shared plan.

**Connected vehicle**: Check the manufacturer's connected vehicle app (Honda Link, Toyota Connected, Ford Pass, OnStar, BMW ConnectedDrive, Tesla app, etc.). If the vehicle is registered in the abuser's name or their account, they may retain GPS access. Discuss with your advocate. If the vehicle is yours, change the app account credentials and remove any connected devices or authorized users.

**Social media location tagging**: Disable location access for Facebook, Instagram, TikTok, Twitter/X, and any other social apps in your phone's app permissions. Review past posts for location tags. Settings > Privacy > Location Services (iOS) or Settings > Apps > [App] > Permissions > Location (Android).

**Photos EXIF data**: Photos taken on your phone contain GPS coordinates in the EXIF metadata by default on most devices. This means a photo shared publicly (or sent to someone) reveals where it was taken. Disable location access for the camera app: Settings > Privacy & Security > Location Services > Camera > Never (iOS) or Settings > Apps > Camera > Permissions > Location > Deny (Android).

### 6.2 Wi-Fi Network Considerations

If you continue to use the same home Wi-Fi network as the abuser (during a period before leaving), the router logs can reveal which devices are connected, when, and in some cases, which websites were visited. This is another reason to conduct safety planning on a device not connected to the shared network.

If you are in a new location (shelter, friend's home), use that location's Wi-Fi normally — it is not connected to the abuser's network.

### 6.3 New SIM and Carrier Account

As noted in Part 4, a new independent carrier account eliminates the carrier-level location tracking and call log visibility that family plan account holders have. This is one of the most effective single steps for location privacy. Prepaid SIM cards are available at major retailers without identity verification in most states.

---

## Part 7: Communication Privacy

Establishing secure, private communication channels is essential both for safety planning and for maintaining contact with your support network after separation.

### 7.1 Signal on a New Device with a New Number

Signal (signal.org) provides end-to-end encrypted messaging and calls. For DV contexts, Signal's value is:
- Messages are encrypted end-to-end; even Signal cannot read them
- You can set messages to automatically delete after a specified period (disappearing messages), reducing the evidence available if your device is ever compromised
- Signal requires a phone number to register — use your new number from the new independent carrier account

**Setup on new device**:
1. Install Signal from the official app store (Google Play, Apple App Store)
2. Register with your new phone number
3. Turn on disappearing messages: a chat with a contact > tap the contact name > Disappearing Messages > set to 1 week or less for regular contacts, 1 day for anything sensitive
4. Do not link Signal to your old number or old device

**Who can find you**: Signal allows contacts to find you if they have your phone number. Since you are using a new number, contacts who only have your old number will not see you on Signal unless you share the new number with them through a safe channel.

**Safety number verification**: When using Signal with trusted contacts, you can verify the "safety number" — a unique code that confirms you are communicating with the right person and that no one has intercepted the connection. This is an optional step appropriate for communications with advocates or attorneys.

### 7.2 Trusted Contacts List

Maintain a short list of people you trust completely with knowledge of your situation and your new contact information. This list should be:
- Written on paper or stored in a secure location, not in the contacts of a compromised device
- Limited to people you are confident the abuser cannot pressure, access, or manipulate
- Informed of your situation and your safety plan at a level appropriate to their role

For each person on the list, establish: (1) how they can reach you (new number or Signal); (2) what they should do if they cannot reach you (who to contact, what to say); (3) what information they should not share with the abuser under any circumstances.

### 7.3 Communication Patterns to Avoid

- Do not communicate with the abuser from your new device unless absolutely necessary and after consulting with your advocate about the risks. Every communication from the new device can potentially reveal its number, carrier, or location.
- Do not use the new device to log into any account the abuser knows about. Even a brief login can create a session record linking the new device to the old account.
- Avoid establishing new accounts at services where you used your real name previously — if the abuser searches for you, avoid accounts that create a findable trail.

---

## Part 8: Documentation and Legal Support

### 8.1 Evidence Preservation for Protective Orders

Digital evidence of abuse — threatening messages, controlling communications, documentation of stalkerware installation — can be essential in protective order proceedings, criminal complaints, and custody matters. This section describes how to preserve that evidence in a form that will be useful in court.

**What constitutes valuable digital evidence in DV cases**:
- Text messages, voicemails, or social media messages containing threats, controlling behavior, or evidence of harassment
- Screenshots of location tracking apps showing surveillance
- Evidence of financial control or coercion (transaction records, messages about financial access)
- Photos or videos documenting physical abuse or property damage
- Evidence of stalkerware installation (app presence in settings, data usage anomalies)
- Documented patterns of behavior over time (dates, times, what was said or done)

**How to preserve digital evidence**:

The key principle is preserving both the content and the metadata that establishes authenticity. A screenshot alone is less useful in court than a screenshot that includes timestamps, sender information, and platform context visible in the image.

1. **Screenshot methodology**: Take screenshots that show the full message thread context (including the sender's name/number, the date and time of messages, and the platform). Do not crop out the context information.

2. **Video screen recording**: For dynamic content (a video threat, a location tracking screen), a screen recording captures more context than a static screenshot. Both iOS and Android have built-in screen recording.

3. **Multiple copies, separate storage**: Save copies to at least two separate locations, neither of which the abuser controls. Options: a trusted friend's device (sent via Signal or a secure channel), an email to your new email account, a cloud storage account the abuser does not know about, a USB drive kept at a shelter or advocate's office.

4. **Written contemporaneous log**: In addition to digital evidence, maintain a written log (paper or secure digital document) recording each incident: date, time, what happened, what was said, what evidence was preserved and where. A consistent written log is powerful corroboration in court.

5. **Do not delete the original**: Do not delete the original messages from the device after copying them. Preserve originals where possible.

**Important limitation**: Evidence you intend to use in legal proceedings may need to meet admissibility standards your jurisdiction's courts apply to digital evidence. Work with a DV legal advocate or attorney to ensure your preservation approach will produce admissible evidence. WomensLaw.org (womenslaw.org/about-abuse/abuse-using-technology) maintains a resource on digital evidence in technology abuse cases.

### 8.2 Legal Aid and Protective Orders

Many DV legal organizations provide free legal assistance for protective orders, divorce proceedings involving documented digital abuse, and custody matters where technology-facilitated abuse is relevant.

- **WomensLaw.org**: Free legal information for survivors of abuse in all 50 states, including state-specific restraining order information. Staffed email hotline for survivors without internet access.
- **National Domestic Violence Hotline**: thehotline.org | 1-800-799-7233 | Can connect you with local legal aid
- **Law Help Interactive** (lawhelp.org): Free legal forms and state-specific guidance
- **Local legal aid**: Search "[your state] domestic violence legal aid" for bar association DV programs, law school clinics, and legal aid organizations in your area
- **VAWA (Violence Against Women Act) programs**: VAWA-funded programs provide free legal services to DV survivors in most states; the hotline can identify local VAWA-funded providers

### 8.3 Law Enforcement Reporting — Your Decision

Reporting to law enforcement is a decision that belongs entirely to the survivor. There are legitimate reasons to report and legitimate reasons not to, and both can be the right choice depending on your circumstances. A DV advocate can help you think through the considerations without judgment.

Factors that may affect the decision:
- Whether you need law enforcement involvement to obtain a protective order (in some jurisdictions, criminal reporting is not required; civil protective orders are available independently)
- Whether police-based escalation may put you at greater risk
- Immigration status considerations (for undocumented survivors — the U visa program provides immigration relief for DV survivors who cooperate with law enforcement investigation; consult with an immigration attorney)
- Whether the abuser has law enforcement connections
- The specific laws in your jurisdiction regarding digital stalking, stalkerware use, and harassment

Law enforcement reporting is not required to access DV services, shelter, or legal aid. The hotline and local DV organizations serve survivors regardless of their reporting decisions.

---

## Part 9: Implementation Paths with Safety Considerations

Unlike other playbooks in this corpus, the tiers here are not primarily organized by technical sophistication. They are organized by safety context — specifically, how much the abuser knows about your plans and how much control they currently exert over your digital infrastructure. A survivor in Tier 3 may need to take actions in a different order than a survivor in Tier 1.

**In all cases: contact the National Domestic Violence Hotline (1-800-799-7233) or a local DV organization before beginning any of these steps. The hotline is free, confidential, and available 24/7 by phone and text.**

### Tier 1: Active Safety Planning — High-Control Situation

For survivors who are currently in or recently left an abusive relationship where the abuser exercises significant control, monitors closely, and is likely to notice changes.

The priority here is **not** technical action — it is safety planning and exit infrastructure. Technical steps follow from and support that plan.

**Before any technical action**:
1. Contact the National Domestic Violence Hotline or a local DV organization on a safe device. Develop a safety plan.
2. Identify a safe location for exit (shelter, trusted family/friend, DV organization).
3. Prepare a go-bag with essential documents (ID, Social Security card, children's documents, financial records, medications, evidence you have preserved). Store it at a location the abuser does not know about.

**Simultaneous to safety planning** (on a safe device only):
4. Document digital evidence of abuse using the methodology in Part 8. Store it outside compromised infrastructure.
5. Write down important phone numbers (advocate, attorney, trusted contacts) on paper. Do not rely on the compromised device.

**Coordinate timing of technical steps with your advocate.** Do not begin account separation or device replacement until your safety plan addresses the timing.

**Time to implement**: Safety planning itself can begin immediately on a safe device. Technical steps: timeline set by the safety plan, not by this playbook.

### Tier 2: Transition Phase — Safety Plan in Place

For survivors who have a safety plan, are executing an exit or have recently left, and are now building independent digital infrastructure.

All of Tier 1, plus:

1. **New device on independent carrier**: Procure a new device (see Part 4). Get a new number on an independent carrier account.
2. **New email account**: Create on new device, with new carrier number as 2FA. See Part 5.1.
3. **Signal setup**: Install Signal on new device with new number. Share new number with trusted contacts only. Enable disappearing messages.
4. **Location sharing audit**: Work through the checklist in Part 6.1. Prioritize carrier plan separation and Apple/Google location sharing.
5. **Evidence documentation**: If not already done, preserve digital evidence of abuse using the methodology in Part 8.1.
6. **Credit freeze**: Place credit freezes at all three bureaus (Part 5.5).

**Safety caveat for each step**: For each technical step above, assess whether completing it will alert the abuser before you are in a safe situation. Your advocate is the right person to help with this assessment.

**Time to implement**: 2–4 hours for device and account setup once the new device is in hand. Credit freeze: 30 minutes. Evidence documentation: variable.

### Tier 3: Stabilization Phase — Established in Safe Location

For survivors who are now in a stable, safe location and are building longer-term digital privacy.

All of Tier 2, plus:

1. **Password manager**: Set up Bitwarden (Part 5.2) and systematically update credentials for all accounts on the audit list (Part 5.4). Use unique, strong passwords for each.
2. **Authenticator app**: Install Aegis (Android) or Raivo OTP (iOS) and migrate 2FA from SMS to TOTP wherever possible.
3. **Shared account separation**: Work through the full account audit table in Part 5.4. Close or separate each shared account at a pace your advocate confirms is safe.
4. **Data broker opt-outs**: Your personal information — home address, phone number, relatives, email — may be available on data broker sites that the abuser can use to locate you. Priority opt-outs:
   - Spokeo: spokeo.com/optout
   - WhitePages: whitepages.com/suppression-requests
   - BeenVerified: beenverified.com/app/optout/search
   - Radaris: radaris.com/page/how-to-remove
   - TruePeopleSearch: truepeoplesearch.com/removal
   For ongoing maintenance, consider Incogni ($7.99/month via Surfshark) which automates quarterly opt-out submissions to 420+ brokers.
5. **Social media privacy audit**: Review all social media accounts for location tags, identifiable background details in photos, and information that could help the abuser locate you. Consider new accounts under a different name for public-facing social media.
6. **Address confidentiality programs**: Many states offer formal Address Confidentiality Programs (ACPs) that provide a substitute mailing address for DV survivors, protecting their physical address from public records. Search "[your state] address confidentiality program" or ask your DV advocate. These programs are free and can be invaluable for preventing address disclosure in court documents, voter rolls, and government records.

**Time to implement**: 4–8 hours for the full account separation and data broker opt-out process.

---

## Part 10: FAQ for Survivors and Advocates

**Q: If I use Signal, will the abuser know I'm using it?**

On a compromised device with stalkerware installed, the abuser may be able to see that you opened Signal, see screenshots of your messages, or detect that you installed it. On a new, clean device on a new carrier account, Signal's communications are end-to-end encrypted and the abuser would have no access. The distinction that matters is: new device, new number, clean infrastructure. Signal on an old compromised device does not provide meaningful protection from a stalkerware installation.

**Q: Can I use a factory reset on my current phone to remove stalkerware?**

A factory reset removes most stalkerware. However, if the device was rooted and stalkerware was installed at root level, a factory reset may not remove it. Additionally, restoring from a backup made during the abusive relationship may reinstall the stalkerware from the backup. The safest approach for a device you suspect is heavily compromised is replacement, not reset. If device replacement is not immediately possible, a factory reset with no backup restore (set up the phone entirely fresh) removes most non-root stalkerware. Consult with a DV advocate or a tech safety organization before resetting if you need to preserve evidence on the device.

**Q: I need to keep the same phone number for work or family. What can I do?**

You can port your number to a new, independent carrier account, away from the shared family plan. This removes the abuser's carrier-level access (call logs, location sharing features on the plan) while preserving your number. Contact a new carrier (one different from your current shared plan carrier) and request a port-in. Be aware: if the number is currently on the abuser's account, they may receive a notification about the port-out request. Coordinate the timing with your safety plan. Once ported, your old number on the abuser's plan becomes inactive — the abuser can no longer receive your calls or texts through the carrier account.

**Q: The abuser purchased my phone. Do they legally own it?**

This is a legal question that depends on your state and the specifics of the purchase. In general, a gift (even from an abusive partner) transfers ownership, but a device provided as part of a carrier plan contract may have more complex ownership implications. More practically: even if the abuser legally owns the device, your safety interests take precedence. DV organizations, shelters, and legal advocates are experienced with helping survivors navigate the practical and legal dimensions of property in abusive relationships. The National Domestic Violence Hotline can connect you with local legal resources.

**Q: My abuser works in technology and is much more sophisticated than average. Does this change anything?**

The core recommendations in this playbook — new device, new carrier, new accounts, no restores from old backups — protect against technically sophisticated monitoring as well as commodity stalkerware. A technically sophisticated abuser may have installed more persistent monitoring tools, may have compromised router-level infrastructure in your home, or may be able to identify your new number or device through social engineering (contacting mutual contacts or carrier stores). Work with a DV advocate who has technology safety expertise. The NNEDV Safety Net project (techsafety.org) can provide or connect you with advocates who have specific experience with technology-facilitated abuse by technically sophisticated abusers.

**Q: I'm an advocate, not a survivor. What's the most important thing I can help survivors do?**

The highest-impact action is completing safety planning that explicitly includes technology — not as an afterthought, but as a central component. Before advising any technical step, ensure the survivor has thought through: (1) whether the abuser will notice the change; (2) what the abuser's likely response is; and (3) whether the survivor is in a position to be safe before, during, and immediately after that response. Technology safety planning templates and training are available from the NNEDV Safety Net project's training programs and the Tech Safety Tech Summit. Ongoing technical assistance for advocates is available at techsafety.org.

**Q: What if the abuser monitors me through the shelter's shared computer or Wi-Fi?**

Shelter computers and shelter Wi-Fi are generally safer than the survivor's compromised device or home network, but they are shared environments. Use private/incognito browsing mode on shelter computers and clear the browsing history after each session. Do not save passwords in a shared browser. For sensitive communications (with your attorney, your support network, about your safety plan), Signal on your new personal device is more private than a shared shelter computer. Shelters vary in their IT practices; your shelter can advise on their specific setup.

**Q: Can digital evidence of stalkerware be used in a restraining order application?**

Yes, in most jurisdictions. Documentation of stalkerware — screenshots showing the app in device settings, records of unusual data usage, the abuser's demonstrated knowledge of information they could only have through monitoring — can support a protective order application. Some jurisdictions have specific stalking statutes that cover digital monitoring tools. Work with a DV legal advocate or attorney who knows your jurisdiction's law on digital evidence and stalking. WomensLaw.org (womenslaw.org) has state-by-state information on relevant laws.

---

## Resource Directory

### Immediate Help and Crisis Support

- **National Domestic Violence Hotline**: thehotline.org | 1-800-799-7233 (TTY: 1-800-787-3224) | Text START to 88788 | Available 24/7; confidential; can connect to local resources and safety planning advocates
- **Crisis Text Line**: Text HOME to 741741 | 24/7 crisis support via text
- **LGBTQ+ DV resources**: avp.org (National Coalition of Anti-Violence Programs) | National Hotline also serves LGBTQ+ survivors

### Technology Safety Specialists

- **NNEDV Safety Net Project**: techsafety.org | Resources on stalkerware, location tracking, account security, and technology safety planning; training for advocates; technical assistance for DV organizations
- **Coalition Against Stalkerware**: stopstalkerware.org | Information on stalkerware identification and removal with safety guidance; links to local support
- **Apple Safety Check guide** (iPhone iOS 16+): support.apple.com/guide/personal-safety/safety-check-iphone-ios-16-ips2aad835e1/web

### Legal Resources

- **WomensLaw.org**: Free legal information for survivors in all 50 states, including state-specific restraining order information and digital evidence guidance; staffed email hotline
- **National Domestic Violence Hotline legal referrals**: thehotline.org — can connect to VAWA-funded local legal aid providers
- **LawHelp.org**: Free legal forms and state-specific guidance for protective orders and related matters

### Tools Referenced in This Playbook

- **Signal**: signal.org — end-to-end encrypted messaging; configure disappearing messages
- **Bitwarden**: bitwarden.com — free, open-source password manager; use new email to register
- **Aegis Authenticator** (Android): getaegis.app — free, open-source TOTP authenticator app
- **Raivo OTP** (iOS): raivoapp.com — open-source TOTP authenticator app for iPhone
- **Proton Mail**: proton.me — end-to-end encrypted email for your new account
- **Incogni**: incogni.com — automated data broker opt-out service ($7.99/month) for address removal from people-finder sites

### Address Confidentiality Programs

Address Confidentiality Programs (ACPs) are available in most states and provide DV survivors a substitute mailing address for public records. Search "[your state] address confidentiality program" or contact your local DV organization. The National Center for Victims of Crime maintains a state-by-state ACP list.

---

## Summary Checklist

**Immediate priority (do on a safe device before any other steps)**:
- [ ] Contact National Domestic Violence Hotline (1-800-799-7233) or local DV organization
- [ ] Develop a safety plan that includes technology — timing of technical steps is part of the plan
- [ ] Identify a safe device for safety planning research (shelter computer, trusted friend's phone, library terminal)
- [ ] Document evidence of abuse on a safe device using the methodology in Part 8.1
- [ ] Write down essential phone numbers on paper (advocate, attorney, trusted contacts)

**Transition phase (with safety plan in place)**:
- [ ] New device on an independent carrier account (new number)
- [ ] New email account on new device (not linked to any shared account)
- [ ] Signal installed with new number; disappearing messages enabled
- [ ] Location sharing audit completed (Find My, Google Maps, carrier plan)
- [ ] Credit freeze placed at all three bureaus
- [ ] Apple Safety Check reviewed (iPhone users)

**Stabilization phase (in safe location)**:
- [ ] Bitwarden password manager set up; unique passwords for all accounts
- [ ] Authenticator app (Aegis or Raivo) replacing SMS 2FA where possible
- [ ] Shared account audit completed (bank, Venmo/CashApp, iCloud/Google, social media, streaming)
- [ ] Data broker opt-outs submitted for Spokeo, WhitePages, BeenVerified, Radaris, TruePeopleSearch
- [ ] State Address Confidentiality Program application filed if available
- [ ] Social media accounts reviewed; location tags removed; privacy settings confirmed

---

**If this playbook is found on a shared or monitored device**: The existence of this document does not constitute evidence of any illegal activity. This is a publicly available safety resource published by an open-source digital rights project. It is distributed to DV organizations, advocates, healthcare providers, and legal service providers as professional reference material.

**Version**: 1.0
**Last updated**: May 6, 2026
**Next review**: July 26, 2026 (aligned with corpus quarterly review)
**Cross-references**: threat-model.md, opsec-playbook.md, implementation-guide.md, device-hardening-guide.md, PHASE_2_SEQUENCING_STRATEGY.md Section 4.1
**Primary external resources**: techsafety.org (NNEDV Safety Net), stopstalkerware.org (Coalition Against Stalkerware), thehotline.org (National Domestic Violence Hotline)
