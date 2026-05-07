---
title: "DV Survivor Safety Playbook: Escaping Intimate Partner Surveillance, Device Security, and Building Long-Term Safety"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
version: 1.0
depends_on:
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — grounded in NNEDV Safety Net Project documentation (half of victim service providers report partner use of phone stalkerware), AV-Comparatives 2025 Stalkerware Test, Coalition Against Stalkerware reporting, FTC action against SpyFone, National DV Hotline technology safety resources, iMazing Spyware Analyzer, State of Surveillance stalkerware guide, and Congressional Tech Safety for DV Victims Act (2025-2026 session)
audience: Domestic violence survivors, DV advocates, shelter staff, safety planning counselors, hotline workers, legal advocates
word_count: ~3,800
safety_notice: This guide is designed for use by survivors and advocates together, not as a self-help document to be followed alone. The National Domestic Violence Hotline (1-800-799-7233 or text START to 88788) can connect you with a safety advocate before you take any steps described in this guide. Safety planning must come before technology safety. Changing device or account security without a safety plan can escalate danger if an abuser notices the changes.
---

# DV Survivor Safety Playbook

**CRITICAL SAFETY NOTE — READ BEFORE ANYTHING ELSE**: This guide must be used carefully. Changing your device security, deleting accounts, removing spyware, or making financial changes can trigger escalation from an abusive partner who notices the changes. **Do not take any action in this guide without first contacting a domestic violence advocate.** If you are in immediate danger, call 911. If you cannot safely call, text "START" to 88788 (National DV Hotline) or use the chat function at thehotline.org — both can be used silently. If you are concerned your device is being monitored, use a device your abuser does not know about (a library computer, a friend's device, a new phone purchased with cash).

The National Network to End Domestic Violence's Safety Net Project found that approximately half of victim service providers report that perpetrators use phone applications to stalk their partners. This is not an unusual or extreme situation — it is the norm. This guide is designed for that situation.

**For DV advocates and shelter staff**: This guide is designed to be worked through together with a survivor, not handed over as a self-help document. The safety planning framework must come first. Technology safety without a safety plan is incomplete and potentially dangerous.

---

## Section 1: How Intimate Partners Surveil — The Threat Model

The threat model for DV survivors is structurally different from every other playbook in this corpus. The primary threat is not a government agency or a corporation — it is a person with significant pre-existing access:

- Access to your devices before any stalkerware was installed (to install it)
- Knowledge of your passwords and PINs (from shared account access)
- Administrative access to your accounts through family plans, shared subscriptions, or account recovery options
- Potentially legal access to shared financial accounts, shared phone plans, and shared vehicle tracking systems
- Knowledge of your daily patterns, your social network, and your physical locations

The standard "device hardening" approach — which works well against government surveillance — is insufficient here, because the threat actor started inside the perimeter. The correct framing: you are not hardening a device against external intrusion. You are rebuilding a digital life in which an abuser has no access, from the ground up.

### 1.1 Stalkerware — The Primary Surveillance Tool

**What it is**: Stalkerware is commercial or custom software installed on a victim's device that secretly monitors activity and reports it to the abuser. Common commercial products include mSpy, FlexiSPY, Hoverwatch, and Cocospy. These products are commercially available, legally marketed as "parental monitoring" or "employee monitoring" software, and require physical access to the device for installation.

**What stalkerware can access** (varies by product and permissions granted):
- Real-time GPS location (often updating every 1–15 minutes)
- All incoming and outgoing calls (duration, caller ID, sometimes call recording)
- All text messages, including messages from encrypted apps if the stalkerware has screen-capture capability
- Camera and microphone (some products enable covert activation)
- All installed applications and their content
- Keystrokes (keylogging feature captures everything typed, including passwords)
- Browser history
- Photos and videos

**Android vs. iOS**: Android is the most common target because the operating system allows sideloading (installing apps from outside the Play Store). Most commercial stalkerware products are Android-only or Android-primary. On iPhone, stalkerware typically requires either: (a) the device to be jailbroken first, which creates visible symptoms; or (b) access to the victim's Apple ID and iCloud credentials (allowing the abuser to monitor iCloud backups remotely without touching the device); or (c) configuration profiles installed on the device.

**The detection challenge**: Commercial stalkerware is designed to be invisible. It does not appear in the normal app list on most Android configurations. It may masquerade as a system app (FlexiSpy, for example, can appear as "SyncManager" on Android). It consumes battery and data in ways that can be noticed but are often attributed to normal use.

### 1.2 Account Access — The Credential Problem

An abusive partner who knows your Apple ID password, your Google account password, or your iCloud credentials does not need to install stalkerware. They can:
- Access your iCloud photo library, contacts, calendar, and location history from any browser
- Use "Find My" (Apple) or "Find My Device" (Google) to see your real-time GPS location
- Read your iCloud-backed messages, including iMessage conversations
- Access your email and use account recovery to reset other passwords

**The family plan surveillance vector**: Shared family cellular plans give the account holder (typically the primary account holder) access to: call records for all lines on the plan, data usage patterns, location history if location sharing is enabled, and in some carrier apps, real-time location of all devices on the plan. Verizon, AT&T, and T-Mobile all provide this capability to family plan primary account holders.

**Financial account surveillance**: Access to shared bank accounts allows monitoring of all transactions — including grocery store locations (which reveal neighborhood), pharmacy names, gas station locations, and any purchase that reveals your whereabouts or plans.

### 1.3 The Safety Planning Requirement

No technology change is safe without a safety plan. An abuser who notices that their surveillance access has been cut off — the stalkerware stops reporting, the location sharing disappears, the bank account shows unusual activity — may escalate to physical violence. The sequence matters:

**Correct sequence**:
1. Contact a DV advocate (hotline, shelter, or local organization)
2. Work through safety planning with the advocate before making any technology changes
3. Identify a safe time and place to make changes (often after leaving the home, not before)
4. Make technology changes in the correct order (account separation before device changes)
5. Have a safety plan in place for the 72-hour window after changes, when escalation risk is highest

**Incorrect sequence**: Discovering stalkerware on your phone, removing it immediately, and then trying to figure out next steps. The abuser will notice within hours that the reports stopped, and will know you found it.

---

## Section 2: Threat Inventory — Mapping What Access Exists

Before making any changes, map the access. A DV advocate can help with this. The questions:

### 2.1 Device Access

| Device | Abuser has physical access? | Abuser knows PIN/password? | Stalkerware suspected? |
|---|---|---|---|
| Primary smartphone | Yes / No | Yes / No | Yes / No / Unknown |
| Laptop/computer | Yes / No | Yes / No | Yes / No / Unknown |
| Tablet | Yes / No | Yes / No | Yes / No / Unknown |
| Smart speaker (Alexa, Google Home) | Yes / No | N/A | Yes / No / Unknown |
| Smart TV | Yes / No | Yes / No | Yes / No / Unknown |

**Smart speakers and smart TVs**: Often overlooked. Smart speakers continuously listen for wake words and may be used by an abuser to monitor conversations in the home. Smart TVs with cameras can be used for visual monitoring in some configurations. If smart speakers are present in the home, assume conversations in those rooms are potentially monitored.

### 2.2 Account Access

| Account | Abuser has password? | Abuser has account recovery access (phone/email)? | Shared account? |
|---|---|---|---|
| Apple ID / Google Account | Yes / No | Yes / No | Yes / No |
| Email (primary) | Yes / No | Yes / No | Yes / No |
| Social media (each) | Yes / No | Yes / No | Yes / No |
| Bank accounts | Yes / No | N/A (online access) | Yes / No |
| Health insurance | Yes / No | N/A | Yes / No |
| Cell phone plan | — | — | Yes (family plan) / No |

### 2.3 Location Access

- Is "Find My" (Apple) or "Find My Device" (Google) enabled and shared with the abuser?
- Is there a shared location app (Life360, Google Maps location sharing, Snapchat location) enabled?
- Is there an AirTag, Tile, or other Bluetooth tracker on your vehicle, bag, or belongings?
- Is your vehicle on a shared insurance or GPS plan that allows the primary holder to see location?

**AirTag and Bluetooth tracker detection**: Apple devices running iOS 14.5 or later will receive an alert if an unknown AirTag has been traveling with you. Android devices can use Apple's "Tracker Detect" app or Google's "Unknown Tracker Alerts" to scan for AirTags. For Tile and other Bluetooth trackers: walk through your vehicle, bag, and belongings methodically. Common hiding places: wheel wells (magnetic), under seats, inside seat pockets, in jacket pockets or purse linings, inside children's items.

---

## Section 3: Stalkerware Detection

### 3.1 Warning Signs on Android

The following patterns are consistent with, but not conclusive of, stalkerware installation:

- **Unusual battery drain**: Stalkerware continuously uploads data (location, call records, messages) and consumes battery at a higher rate than normal
- **Unusual mobile data usage**: Check Settings > Network > Data Usage. An app you do not recognize consuming significant data in the background is a warning sign
- **Device warm without recent use**: Background data transmission generates heat
- **Accessibility Services**: Check Settings > Accessibility > Installed Services (or similar path depending on Android version). Any service you did not install that has broad permissions (read screen content, perform actions, observe touch) is likely stalkerware or stalkerware-adjacent. Approximately 90% of commercial stalkerware requires Accessibility Services permission for keylogging and screen content capture.
- **Device Administrator Apps**: Check Settings > Security > Device Admin Apps. An app listed as a device administrator that you did not install should be investigated.

### 3.2 Warning Signs on iPhone

iPhone stalkerware is less common but possible via:
- **Jailbreak**: Check for the presence of "Cydia" app or other jailbreak-related apps. If the phone is jailbroken and you did not jailbreak it, stalkerware may be installed. Note: jailbreaking is a visible, unusual action — if you did not do it, someone with physical access to the device did.
- **Configuration profiles**: Settings > General > VPN & Device Management. Any profile you did not install is suspicious. Configuration profiles can grant remote monitoring access and should be removed unless you can verify their legitimate source.
- **iCloud monitoring (no device required)**: If the abuser has your Apple ID and password, they do not need to touch your device. They can log into iCloud.com from any browser and see your photos, contacts, messages (if iCloud messages is enabled), and location. The sign: check Settings > [Your Name] > iCloud > Show All. See which apps sync to iCloud. Then check if anyone else has recently logged into your Apple ID at appleid.apple.com > Sign-in and Security > Active Sessions.

### 3.3 Professional Stalkerware Detection

For definitive stalkerware detection, professional help is available:
- **iMazing (iMazing.com)**: iMazing's Spyware Analyzer feature (updated 2024–2025) analyzes iPhone and iPad backups for known spyware indicators. Free with paid subscription.
- **Coalition Against Stalkerware**: stopstalkerware.org — provides a list of partner anti-stalkerware tools and victim resources
- **National Domestic Violence Hotline**: thehotline.org — can connect you with a technology safety advocate who can walk through detection with you
- **NNEDV Safety Net Project**: techsafety.org — maintains resources for stalkerware detection and provides technical assistance to victim service providers

**Caution**: Do not use stalkerware removal tools or antivirus scans on your device while the abuser still has access or is still monitoring. The removal of stalkerware is immediately visible to the abuser through the loss of reports. This step belongs in the post-safety-plan phase.

---

## Section 4: Device Safety — The Correct Response to Stalkerware

### 4.1 The Core Principle: Replace, Do Not Just Remove

If stalkerware has root access (common in some commercial products, especially on rooted/jailbroken devices), it can survive a factory reset. The correct response to a device confirmed to have stalkerware is replacement, not removal:

1. Purchase a new device with cash from a retail store (not online — no account or purchase record)
2. Do not link the new device to any account the abuser has access to
3. Do not restore from a backup of the old device — the backup may carry stalkerware
4. Set up the new device as a completely new device with new accounts (see Section 5)

**For iPhone**: If the abuser has your Apple ID credentials and iCloud access, a new iPhone linked to the same Apple ID gives the abuser continued access through iCloud. The new device must have a new Apple ID.

**For Android**: A new Android device linked to the same Google account gives the abuser continued access through Google account monitoring. The new device must have a new Google account.

### 4.2 Minimum Safety on the Old Device While Still in the Abusive Situation

If you cannot yet replace your device, the following reduces — but does not eliminate — ongoing surveillance:

- **Sensitive conversations only on a device the abuser does not know about** (a burner phone purchased with cash, a library computer, or a trusted friend's device)
- **Never disable or remove stalkerware from the compromised device** — this tips off the abuser
- **Assume everything on the compromised device is visible to the abuser** — do not use it for safety planning communications, shelter searches, legal consultations, or financial planning

### 4.3 The Burner Device

A prepaid smartphone purchased with cash from a retail store, not registered to your identity, with a prepaid SIM also purchased with cash, is the most practical interim safe device. Do not install any app that requires your real identity (Facebook, your primary Gmail, your Apple ID). Use it only for:
- Safety planning communications with your advocate
- Searching for shelters, legal aid, and resources
- Contacting family and friends who are safe to contact
- Accessing new accounts that the abuser does not know about

**Keep the burner device**: At a trusted friend's home, in your workplace locker, or in another location the abuser does not control. Do not bring it into your home until you are ready to leave.

---

## Section 5: Account Separation — Rebuilding a Digital Life

### 5.1 New Accounts, Not Password Resets

Resetting passwords on accounts the abuser has access to is not sufficient protection. If the abuser has account recovery access (the recovery phone number or recovery email is under their control), they can reset the password back. If they have installed a keylogger, they will see the new password as you type it. The correct approach is building new accounts, not changing passwords on compromised accounts.

**New account priority order**:

1. **New email address** — on a new provider (Proton Mail at proton.me provides encrypted email without the Google PRISM exposure; create it from a device and network the abuser does not know about). This is the anchor for all other new accounts.
2. **New Apple ID or Google account** — linked to the new email, not the old one
3. **New phone number** (the new prepaid SIM) — linked to the new accounts, not the old ones
4. **New banking/financial accounts** — see Section 7

**Accounts to NOT change on old devices or old email**: Social media accounts, shopping accounts, or any account that might tip off the abuser to what you are doing. Abusers monitor accounts for unusual activity. Changing passwords, changing email addresses, or unfriending on social media during the planning period can escalate danger.

### 5.2 Account Recovery — The Hidden Access Point

Even if you change a password, an abuser retains access if they control any account recovery channel:
- **Recovery phone number**: If the abuser's phone number is the recovery number for your email or bank account, they can reset your password at any time. Remove recovery phone numbers and add a new one (from your new SIM) as part of the new account setup.
- **Recovery email**: If the abuser controls the recovery email address (or has access to it), same issue. Anchor new accounts on the new email only.
- **Security questions**: If the abuser knows the answers to your security questions ("What city were you born in?"), those are not secure. Use a random string as the security question answer and store it in your advocate's records if needed.

### 5.3 Two-Factor Authentication — Set It Up on New Accounts

Enable two-factor authentication (2FA) on all new accounts, linked to your new phone number (new SIM). This prevents an abuser from accessing new accounts even if they somehow obtain the password.

**Do not use SMS 2FA on accounts linked to the old phone number**. The old SIM is on the abuser's family plan — they may have carrier access to intercept SMS codes through the plan's account management features.

---

## Section 6: Location Privacy — Cutting Off GPS and Tracking

### 6.1 Carrier Family Plan — The Invisible Surveillance

If your phone is on a shared family plan, the primary account holder may have real-time location access through the carrier's family tracking feature. This is the most commonly overlooked surveillance vector in DV situations.

**You cannot disable carrier-level family tracking on a plan you do not control**. The solution is to leave the family plan entirely and obtain an independent line — this requires either: (a) purchasing an outright phone and a prepaid SIM not on the family plan (the cash burner device in Section 4.3 accomplishes this), or (b) opening your own account with a carrier after leaving.

**Until you are on an independent line**: Assume your carrier-level location is visible to the abuser at all times while carrying the old device.

### 6.2 Location Apps — Find My, Life360, Google Maps Sharing

Check for and disable (carefully, after safety planning):
- **Apple Find My**: Settings > [Your Name] > Find My > Share My Location — check who it is shared with
- **Life360**: Requires leaving the "circle" — visible to all members
- **Google Maps location sharing**: Google Maps > Profile > Location Sharing

**The safety planning timing issue**: Removing yourself from location sharing is immediately visible to the abuser. This step must be timed as part of the exit or safety plan — not done while still in the dangerous situation without protection in place.

### 6.3 Vehicle Tracking

If your vehicle is on a shared insurance policy or has a family tracking system (OnStar, Tile, manufacturer app), the primary account holder may have vehicle GPS access. Check:
- Physically inspect the vehicle for AirTags and Bluetooth trackers (wheel wells, undercarriage, interior pockets, under seats)
- Review the vehicle's telematics app account access (log into the manufacturer's app and see what accounts have access)
- Check whether the vehicle's GPS reporting is enabled through insurance (Progressive Snapshot, State Farm Drive Safe, etc.)

After leaving: if possible, use a different vehicle for travel during the safety period, or have the vehicle swept professionally for trackers.

---

## Section 7: Financial Independence — Breaking Financial Surveillance

### 7.1 New Account Before Leaving

Open a new bank account in your name only at an institution the abuser does not use and has no relationship with. Do this before any other financial changes. This account is where you will deposit any funds you need to access independently and where any emergency financial assistance will be directed.

**Community credit unions** are recommended for their human relationship-based account management and their lower automated surveillance infrastructure. For DV survivors who need to open an account quickly, most credit unions accept initial account opening by walk-in.

**Required documents for bank account opening**: Most institutions require a government-issued ID and Social Security number. If you do not have access to your ID documents (a common situation when documents are controlled by an abusive partner), contact a DV advocate — advocates frequently assist survivors in obtaining replacement documents through emergency expedited processes.

### 7.2 Document Access — Social Security Card, Birth Certificate, Passport

If an abusive partner controls your identity documents, a DV advocate can help you navigate:
- Social Security card replacement: Free through SSA office; no fee; requires proof of identity (one document may be sufficient)
- Birth certificate: Through vital records in your state of birth; fee waived for DV survivors in many states
- State ID or driver's license: Through DMV; some states waive fees for DV survivors with advocate documentation
- Passport: Emergency passport for DV survivors fleeing internationally is available through State Department with advocate support

**The address concern**: If you are using a shelter or temporary address and need documents sent there, verify with your advocate that the shelter address is safe to use for document receipt. Many shelters have confidential address protections under state law.

### 7.3 Cash and Financial Independence During the Safety Period

Before leaving, accumulate a small cash reserve in a location the abuser does not control — a trusted friend's home, a secure locker, or a shelter safe. Even $200–$500 provides essential independence for transportation, food, and initial expenses.

Cash transactions leave no record in shared financial accounts. For purchases during the planning period that you do not want visible: pay in cash.

---

## Section 8: Legal Protective Orders and Technology

### 8.1 What a Protective Order Does and Does Not Do

A protective order (restraining order) legally prohibits the abuser from contacting you, approaching you, or being within a specified distance of you or your residence. Violation is a criminal offense. Protective orders are enforceable by calling 911.

**Technology-specific provisions available in most states**:
- Prohibition on electronic monitoring, including stalkerware installation
- Prohibition on accessing electronic accounts
- Prohibition on location tracking
- Prohibition on sharing intimate images

**How to request these provisions**: When filing for a protective order, specifically request technology-related provisions in your petition. DV advocates and legal aid attorneys can help you draft these provisions.

### 8.2 Protective Order Limitations

Protective orders are legal documents, not physical barriers. An abuser who violates a protective order may not be immediately stopped. The protective order creates legal accountability for violations — it does not create safety by itself. Technology safety combined with a protective order provides layered protection.

**Remote stalkerware**: An abuser who has already installed stalkerware before the protective order is issued may continue monitoring even while technically subject to the order. Removing the stalkerware (as part of device replacement) is the operational countermeasure; the protective order is the legal accountability mechanism for the installation and use.

### 8.3 State Specific Resources

- **thehotline.org**: National DV Hotline; can connect you with local legal advocates and protective order resources in any state
- **womenslaw.org**: State-by-state legal information on protective orders, custody, and DV law
- **techsafety.org/resources-survivors**: NNEDV Safety Net Project; technology safety resources by state
- **legalaid.org**: National directory of legal aid organizations; most provide DV representation without charge

---

## Section 9: Long-Term Identity Safety — After Leaving

### 9.1 Address Confidentiality Programs

Most states operate Address Confidentiality Programs (ACPs) that provide DV survivors, stalking victims, and sexual assault survivors with a substitute mailing address. Mail sent to the ACP address is forwarded by the state to your actual location without revealing it. ACP addresses can be used for:
- Voter registration
- Driver's license (in most participating states)
- Court documents
- Employment records in some states

**States with ACPs**: California (CalACS), Washington, Oregon, Illinois, Texas, New York, Florida, and approximately 35 additional states. Contact your state's ACP administrator through your local DV shelter or thehotline.org.

**Why ACPs matter in the data broker context**: ELITE and Thomson Reuters CLEAR aggregate DMV, voter registration, and court records to build address confidence scores. If your ACP address (not your real location) is the address in all official records, ELITE's score for your real location remains low — protecting you from address-based location in any government database that feeds Palantir.

### 9.2 Data Broker Opt-Outs for Your New Address

After establishing a new, safe address: complete data broker opt-outs to prevent your new address from being widely sold and accessible to the abuser who may search for you. The same opt-out process from the immigration playbook applies here:

- **LexisNexis Accurint**: https://optout.lexisnexis.com/ — this is the most important opt-out because LexisNexis is also used by skip tracers and private investigators, which abusers sometimes hire
- **BeenVerified**: https://www.beenverified.com/app/optout/search
- **Spokeo**: https://www.spokeo.com/optout
- **WhitePages**: https://www.whitepages.com/suppression-requests

**California residents**: DROP platform (https://privacy.ca.gov/drop/) provides one-stop opt-out from 100+ brokers including LexisNexis.

**Incogni** ($7.99/month) automates ongoing re-submission — particularly valuable for survivors who cannot allocate time to quarterly manual opt-outs.

### 9.3 Social Media and Online Presence

After leaving:
- Create new accounts with a new name variant if possible (many survivors use a middle name or nickname publicly)
- Set all profiles to private; do not accept connection requests from people who might know the abuser
- Disable location tagging on all platforms
- Do not tag your location in photos — even a background that shows a recognizable neighborhood can be used for location intelligence
- Consider running your own profile through a people-search site to see what is visible about your new location to someone searching for you

---

## Section 10: Implementation Checklists

### Checklist A: Before Leaving — Safety Planning Phase

**Complete with your DV advocate, not alone:**

- [ ] Contact DV advocate and complete safety planning (thehotline.org or 1-800-799-7233)
- [ ] Complete threat inventory (Section 2) with advocate
- [ ] Purchase cash burner phone and prepaid SIM; keep at safe location outside home
- [ ] Check for physical trackers in vehicle, bags, and clothing (Section 6.3)
- [ ] Create new email account (ProtonMail recommended) from safe device
- [ ] Open new bank account at institution abuser does not use
- [ ] Accumulate small cash reserve in secure location outside home
- [ ] Locate identity documents (SSN card, birth certificate, passport); if controlled by abuser, contact advocate for replacement assistance
- [ ] Identify ACP program in your state

### Checklist B: Day Of / Immediately After Leaving

- [ ] Bring identity documents, medications, and the cash reserve
- [ ] Leave old device at home OR keep it on your person but use only the burner phone for any sensitive communications
- [ ] Contact advocate to confirm safe arrival
- [ ] New accounts (new Apple/Google ID, new email) now accessible from new device
- [ ] Do NOT remove stalkerware from old device yet — discuss timing with advocate

### Checklist C: After You Are Safe

- [ ] Replace compromised device (not factory reset — full device replacement)
- [ ] Set up new accounts on new device; do not restore from old backups
- [ ] Remove yourself from shared carrier family plan (new independent line)
- [ ] Change all account recovery options on any accounts you want to keep (new phone, new email for recovery)
- [ ] Complete data broker opt-outs for new address (LexisNexis, Spokeo, BeenVerified, WhitePages)
- [ ] If California resident: DROP platform at privacy.ca.gov/drop/
- [ ] Apply for ACP program through state administrator
- [ ] If applicable: request protective order with technology-specific provisions from local court (advocate can assist)
- [ ] Enable 2FA on all new accounts using new phone number

### Checklist D: Ongoing Safety Maintenance

- [ ] Every 90 days: re-submit data broker opt-outs (or use Incogni for automation)
- [ ] Monthly: check new accounts for unfamiliar logins (Settings > Security > Active Sessions in most platforms)
- [ ] Periodically scan for AirTags and Bluetooth trackers if you have a shared vehicle or items that may have been left behind
- [ ] Maintain ACP enrollment; notify state of address changes

---

## Summary: Five Things That Matter Most

1. **Contact an advocate before making any changes** — the sequence matters more than any individual technical step. Changes that tip off an abuser before you are safe can escalate physical danger. Call 1-800-799-7233 or text START to 88788 first.

2. **Replace the compromised device, do not just reset it** — stalkerware can survive factory resets. New device, new accounts, new phone number is the correct architecture.

3. **New accounts, not password resets** — if an abuser has account recovery access, changing passwords does not break the access. New accounts anchored on a new email and new phone number that the abuser does not know about is the correct approach.

4. **Address Confidentiality Program enrollment** — an ACP address in official records (DMV, voter registration, court documents) keeps your real location out of the data broker pipelines that feed ELITE and commercial skip-trace services that abusers use to find survivors.

5. **Leave the family phone plan** — carrier-level family plan tracking is the most commonly overlooked surveillance vector. Until you are on an independent line, assume your location is known.

---

## Emergency Contact Numbers

- **National Domestic Violence Hotline**: 1-800-799-7233 | Text: START to 88788 | thehotline.org (chat)
- **National Sexual Assault Hotline**: 1-800-656-4673 | rainn.org
- **Crisis Text Line**: Text HOME to 741741

## Resources

### Technology Safety
- **NNEDV Safety Net Project**: techsafety.org — comprehensive technology safety resources, stalkerware information, state-specific resources
- **Coalition Against Stalkerware**: stopstalkerware.org — stalkerware detection resources and victim support
- **iMazing Spyware Analyzer**: imazing.com/blog/spyware-analyzer-redux — iPhone/iPad spyware analysis tool

### Legal Support
- **Women's Law**: womenslaw.org — state-by-state legal information
- **Legal Aid Society**: legalaid.org — national directory of free DV legal representation
- **Address Confidentiality Programs**: Find your state's program at techsafety.org

### Financial Independence
- **allotment.org**: Financial resources for DV survivors
- **National Network to End Domestic Violence**: nnedv.org — economic justice resources

### Shelter and Safety Planning
- **DomesticShelters.org**: domesticshelters.org — national shelter directory
- **National DV Hotline local resources**: thehotline.org/resources/

---

**Version**: 1.0
**Created**: May 7, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `phase-2-immigration-surveillance-evasion-playbook.md` (Section 2 data broker opt-outs directly applicable), `opsec-playbook.md`, `PHASE_2_SEQUENCING_STRATEGY.md` (Section 4.1 DV community)

---

## Sources

- [NNEDV Safety Net Project — Spyware and Stalkerware: Phone Surveillance](https://www.techsafety.org/spyware-and-stalkerware-phone-surveillance)
- [NNEDV Safety Net Project — Technology Safety Plan](https://www.techsafety.org/resources-survivors/technology-safety-plan)
- [NNEDV Safety Net Project — Resources for Survivors](https://www.techsafety.org/resources-survivors)
- [State of Surveillance — Stalkerware Detection and Removal Guide](https://stateofsurveillance.org/guides/basic/stalkerware-detection-removal-guide/)
- [AV-Comparatives — Stalkerware Test 2025](https://www.av-comparatives.org/tests/stalkerware-test-2025/)
- [Coalition Against Stalkerware — Media information](https://stopstalkerware.org/information-for-media/)
- [iMazing — Spyware Analyzer improvements](https://imazing.com/blog/spyware-analyzer-redux)
- [Harvard JOLT — Stalkerware: An Overlooked Harm Draws FTC Attention](https://jolt.law.harvard.edu/digest/stalkerware-an-overlooked-harm-draws-the-attention-of-the-ftc)
- [DomesticShelters.org — Technology Safety Resources](https://www.domesticshelters.org/domestic-violence-technology-safety-resources)
- [CASA Pinellas — Technology Safety: 9 Tips for DV Survivors](https://casapinellas.org/tech-safety/)
- [Congress.gov — Tech Safety for Victims of Domestic Violence Act, H.R.4127, 119th Congress](https://www.congress.gov/bill/119th-congress/house-bill/4127/text)
- [Protectstar — Detecting, Removing, and Preventing Spyware on Android Devices](https://www.protectstar.com/en/blog/detecting-removing-and-preventing-spyware-on-android-devices)
- [CPO Magazine — How to Detect and Remove Stalkerware](https://www.cpomagazine.com/data-privacy/how-to-detect-and-remove-stalkerware/)
- [MDPI Electronics — Review of Mobile Surveillanceware, 2025](https://www.mdpi.com/2079-9292/14/14/2763)
- [Operation Safe Escape — How Stalkerware Threatens Women's Privacy](https://safeescape.org/stalkerware-threatens-womens-privacy/)
- [PHASE_2_SEQUENCING_STRATEGY.md — Section 4.1 DV survivor audience](./PHASE_2_SEQUENCING_STRATEGY.md)
