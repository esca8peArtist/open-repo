---
title: "Phase 2 Execution Runbook: Hardening (2.1–2.9)"
project: cybersecurity-hardening
created: 2026-06-14
status: active
phase: 2
timeline: "4–8 weeks (June–August 2026)"
---

# Phase 2 Execution Runbook: Hardening

**Purpose**: Week-by-week implementation guide for Phase 2 of your personal OPSEC plan. This runbook parallels PERSONAL_OPSEC_PLAN.md Phase 2 (steps 2.1–2.9) with additional contingency procedures, success metrics, and integration with Phase 1.

**Prerequisites**: Phase 1 complete (steps 1.3–1.7). See PHASE_2_READINESS_CHECKLIST.md before starting.

**Total time commitment**: 5–7 hours across 4–8 weeks.  
**Total cost**: $60–250/year (VPN minimum, comprehensive with optional hardware key).

---

## Phase 2 Overview: Six Hardening Domains

Phase 2 closes the next tier of attack surfaces. Unlike Phase 1 (one-time setup), Phase 2 items involve recurring work and some spending.

| Domain | Items | Goal | Effort |
|--------|-------|------|--------|
| **Signal Isolation** | 2.1 Mullvad VPN | Hide ISP visibility of browsing | 1 hour |
| **Email & Communication** | 2.2 ProtonMail, 2.3 Tor Browser | End-to-end encrypted comms, anonymous research | 1.5 hours |
| **System Telemetry** | 2.4 Windows privacy, 2.5 Linux encryption | Stop OS data collection | 1–2 hours |
| **Device Hardening** | 2.6 iPhone Lockdown Mode, 2.9 SIM PIN | Advanced mobile protections | 0.5 hours |
| **Data Broker Management** | 2.7 Automated opt-outs | Quarterly removal re-submissions | 0.25 hours setup, recurring |
| **Account Resilience** | 2.8 Hardware security key (optional) | Phishing-resistant 2FA | 0.5 hours (optional) |

---

## Timeline: Week-by-Week Execution

### Week 1 (Weeks 1–2 of Phase 2): Signal Isolation

**Focus**: VPN setup + initial ProtonMail account creation  
**Time**: 1–2 hours  
**Can overlap with Phase 1** if disk encryption is running in background

#### 2.1 — Mullvad VPN: Always-On Connection

**Why now**: Your ISP can see every site you visit (even encrypted HTTPS requests show destination domain). This is NSL-subpoena-able (no warrant required). Mullvad shifts this visibility to a Swedish company outside U.S. legal jurisdiction.

**Prerequisites**:
- [ ] You can access mullvad.net
- [ ] You have payment method (credit card, prepaid card, or mailing address for cash)
- [ ] Admin access to install software on Windows/Mac/Linux

##### Windows Desktop Setup

1. **Generate Mullvad account**
   - Go to mullvad.net
   - Look for "Get started" or "Create account"
   - A 16-digit account number is generated
   - **SAVE THIS NUMBER IMMEDIATELY**
   - Paste it into Bitwarden (from Phase 1.5): entry "Mullvad Account," username: "account-number," password: the 16 digits
   - No email, no traditional password — this account number IS your entire account

2. **Add payment**
   - **Option A (cash by mail, most anonymous)**:
     - Note your 16-digit account number
     - Go to mullvad.net/help/sending-cash
     - Mail physical cash in an envelope to the Mullvad address in Sweden
     - Include a note with your 16-digit account number
     - Payment takes 1–3 weeks to process
   
   - **Option B (prepaid card, faster)**:
     - Buy a prepaid Visa or Mastercard gift card with cash at a pharmacy/grocery store
     - Go to mullvad.net and log in with your account number
     - Add the prepaid card to your account
     - Payment is immediate

3. **Download and install Mullvad**
   - Go to mullvad.net/download
   - Click "Windows"
   - Download the executable
   - Run the installer and follow prompts
   - Open Mullvad once installed

4. **Configure Mullvad**
   - You'll see a login screen
   - Enter your 16-digit account number
   - Click "Connect"
   - A popup message should say "Mullvad is connected"

5. **Verify VPN is working**
   - Open a browser
   - Go to https://mullvad.net/check
   - You should see a green checkmark and "You are connected to Mullvad"
   - Your real IP should NOT appear
   - Note the Mullvad IP shown — this is your exit node

6. **Verify kill switch is ON**
   - In Mullvad, click the hamburger menu (three lines)
   - Go to Settings → VPN settings
   - Confirm "Kill switch" is ON (enabled)
   - Kill switch is critical — it blocks ALL traffic if the VPN disconnects, preventing IP leaks

7. **Choose server location (optional)**
   - In Mullvad, click "Select location"
   - Choose a server in Sweden or Netherlands (GDPR jurisdiction protection)
   - Or choose based on speed — Mullvad shows latency for each server

8. **Test kill switch**
   - In Mullvad settings, toggle "Kill switch" OFF temporarily
   - Go to mullvad.net/check — you should see your real IP (kill switch OFF)
   - Toggle kill switch back ON
   - Refresh mullvad.net/check — your real IP should disappear
   - This confirms kill switch works

9. **Set to auto-connect on startup**
   - Mullvad should auto-connect by default, but verify
   - In Settings, ensure "Auto-connect on startup" is enabled
   - Restart your computer — Mullvad should connect automatically before Windows fully loads

##### iPhone Setup

1. **Download Mullvad from App Store**
   - Search "Mullvad"
   - Verify developer is "Mullvad VPN AB"
   - Tap "Get" → "Install"

2. **Sign in**
   - Open Mullvad
   - Enter your 16-digit account number
   - Tap "Connect"

3. **Enable always-on VPN**
   - Go to iPhone Settings → General → VPN & Device Management
   - Tap the Mullvad configuration
   - Toggle "Connect On Demand" to ON
   - This makes the VPN auto-connect whenever WiFi or cellular is used

4. **Verify connection**
   - Open Mullvad app
   - Confirm "Connected" is shown
   - Open a browser and go to mullvad.net/check
   - Verify "You are connected to Mullvad"

##### Linux Setup (if applicable)

1. **Download from mullvad.net/download** — select Linux
2. **Follow package manager instructions** (varies by distro: Ubuntu, Fedora, Debian)
3. **Install and log in** with your account number
4. **Verify**: `curl https://am.i.mullvad.net/` should show Mullvad IP, not your real IP

---

#### 2.2 — ProtonMail: Encrypted Email Account

**Why now**: NSA PRISM compels Google/Microsoft to provide stored email content. FBI compels email with a search warrant. ProtonMail is incorporated in Switzerland and uses zero-knowledge encryption — ProtonMail cannot decrypt your emails even if subpoenaed.

**Prerequisites**:
- [ ] Mullvad VPN is installed and connected
- [ ] You can access proton.me
- [ ] You have your primary email for recovery

##### Create ProtonMail Account

1. **Access proton.me via Mullvad**
   - Confirm Mullvad is connected to your VPN
   - Open a private/incognito browser window (additional privacy)
   - Go to https://proton.me
   - Click "Create account" or "Sign up"

2. **Choose username**
   - This is your new email address: `username@proton.me`
   - **Use a username NOT connected to your real identity**
   - Examples of good usernames:
     - `bluemoon47` (unrelated words + numbers)
     - `silverfish92` (unrelated to your real name)
   - Examples of bad usernames:
     - Your real name
     - A nickname that appears on your social media
     - Something derived from your existing email

3. **Create password**
   - Strong passphrase (6+ random words, or 20+ random characters)
   - **Store in Bitwarden**: Create entry "ProtonMail" with username: `username@proton.me`, password: your new password

4. **Set recovery email**
   - Use your Gmail or primary email (the one you secured in Phase 1.4)
   - This is the recovery method if you lose access to ProtonMail
   - ProtonMail will send a verification email — open it and click verify link

5. **Enable 2FA on ProtonMail (using Ente Auth)**
   - Once signed in, click your profile icon (top right)
   - Go to Account → Security → Two-step Login
   - Select "Authenticator app"
   - Scan the QR code with Ente Auth on iPhone
   - Confirm the 6-digit code
   - Save backup codes to Bitwarden or printed location

6. **Download ProtonMail Bridge (optional, for desktop email client)**
   - ProtonMail works via web browser, but you can also use a desktop email client (Outlook, Thunderbird)
   - Go to proton.me/download → ProtonMail Bridge
   - This is optional — the web interface is sufficient for Phase 2

##### iPhone Setup

1. **Download Proton Mail from App Store**
   - Verify developer is "Proton AG"
   - Tap "Get" → "Install"

2. **Sign in**
   - Enter your ProtonMail email and password
   - Confirm 2FA code from Ente Auth
   - You're signed in

3. **Set as default (optional)**
   - You now have both Gmail and ProtonMail on iPhone
   - Use Gmail for routine things
   - Use ProtonMail for sensitive communications (Signal contacts, lawyers, advocacy organizations)

---

### Week 2 (Weeks 2–3 of Phase 2): Anonymous Research & Telemetry

**Focus**: Tor Browser setup + Windows privacy hardening  
**Time**: 1.5–2 hours  
**Can overlap with VPN setup from Week 1**

#### 2.3 — Tor Browser: Anonymized Web Research

**Why now**: NSA backbone surveillance intercepts internet metadata. Browsing from your home IP creates a permanent record of what you've researched (topics, timing, frequency). Tor routes traffic through 3 relays so no single party sees both your identity and your destination.

**Prerequisites**:
- [ ] Mullvad VPN is working
- [ ] You have Windows or Linux
- [ ] You can access torproject.org

##### Download and Install Tor Browser

1. **Download ONLY from torproject.org**
   - Do NOT download Tor Browser from any other source (supply chain risk)
   - Go to https://www.torproject.org/download
   - Click "Download for Windows" or "Download for Linux"
   - Verify the file hash on the download page (advanced users) — this confirms you downloaded the legitimate version

2. **Install normally**
   - Run the installer
   - Choose installation location (default is fine)
   - Open Tor Browser once installed

3. **Wait for connection**
   - On first launch, Tor Browser will take 10–30 seconds to connect to the Tor network
   - You'll see progress: "Connecting to Tor..."
   - Once connected, the browser window opens

---

##### Configure Tor Browser Security

1. **Set security level to "Safest"**
   - Click the shield icon in the Tor Browser toolbar (top right)
   - Scroll to "Security" → "Security level"
   - Select **"Safest"** (this disables JavaScript, the primary browser exploit category)
   - You may see some websites not render properly — this is expected and safe

2. **Disable extensions**
   - Tor Browser comes with no extensions by default — do not install any
   - Extensions are a deanonymization risk

3. **Do not resize the window**
   - Keep Tor Browser at default size — resizing the window is browser fingerprinting

---

##### Use Tor Browser Safely

1. **The VPN-then-Tor sequence**:
   - Connect Mullvad first
   - Then open Tor Browser
   - This hides your Tor usage from your ISP

2. **Use Tor for**:
   - Researching sensitive topics (political movements, health conditions, legal issues)
   - Creating accounts that shouldn't be linked to your identity
   - Accessing .onion services (SecureDrop, ProtonMail's .onion address)

3. **Do NOT use Tor for**:
   - Logging into any account connected to your real identity
   - One login destroys anonymity for that session
   - Example: Don't log into your Gmail from Tor Browser

4. **Do NOT**:
   - Resize the Tor Browser window (fingerprinting)
   - Install extensions (deanonymization risk)
   - Open downloaded files outside Tor Browser (IP leak risk)

---

##### Verify Tor is Working

1. **Check your Tor exit node**
   - With Tor connected, go to https://check.torproject.org
   - You should see "Congratulations! You are using Tor"
   - Your IP shown is a Tor exit node, not your real IP

2. **Verify your real IP is hidden**
   - The page should NOT show your ISP name or real IP

---

#### 2.4 — Windows: Disable Telemetry and Data Collection

**Why now**: Windows telemetry sends usage data to Microsoft: app behavior, browsing activity, location, and diagnostics. This data can be subpoenaed and feeds into commercial data broker ecosystems.

**Prerequisites**:
- [ ] Windows 10 or 11 Pro/Enterprise (Home can do manual steps only)
- [ ] Admin access
- [ ] 30 minutes uninterrupted time

##### Manual Telemetry Disabling

1. **Diagnostic data setting**
   - Open Settings (Windows key + I)
   - Go to Privacy & security → Diagnostics & feedback
   - Under "Diagnostic data," select **"Required diagnostic data only"**
   - This is the minimum Microsoft requires for OS function

2. **Disable experience improvement**
   - On the same page, toggle OFF:
     - "Improve inking & typing"
     - "Tailored experiences"
     - "Advertising ID"

3. **Disable activity history**
   - Privacy & security → Activity history
   - Uncheck "Store my activity history on this device"
   - Click "Clear" to delete existing activity data

4. **Disable search history**
   - Privacy & security → Search permissions
   - Toggle OFF "Cloud content search"
   - Toggle OFF "Search history on this device"

5. **Disable location services**
   - Privacy & security → Location
   - Toggle OFF "Location services"
   - (Leave it on for iPhone, but disable for Windows)

6. **App permissions audit**
   - Privacy & security → App permissions
   - Go through each category (Camera, Microphone, Location, Calendar, Contacts, etc.)
   - For each app listed, toggle OFF access for apps that don't legitimately need it
   - Example: Disable Camera for Notepad, disable Location for Calculator

7. **Disable advertising ID**
   - Privacy & security → General
   - Toggle OFF "Let apps show me personalized ads"

---

##### (Optional) Advanced: O&O ShutUp10++

For more granular control:

1. **Download O&O ShutUp10++**
   - Go to oo-software.com → select ShutUp10++
   - Download (free version is sufficient)
   - Run the installer

2. **Apply recommended settings**
   - The interface shows hundreds of privacy settings
   - Click "Recommended" button to apply pre-vetted privacy-hardening settings
   - Restart your computer

3. **Verify changes**
   - Reopen Manage BitLocker, Bitwarden, and Mullvad to confirm they still work normally
   - O&O can sometimes break features — test your critical apps

---

### Week 3 (Weeks 3–4 of Phase 2): Mobile Hardening & Data Cleanup

**Focus**: iPhone Lockdown Mode + Linux encryption (if needed)  
**Time**: 0.5–2 hours (most time if Linux encryption needed)

#### 2.5 — Linux: Full-Disk Encryption (if not completed in Phase 1)

**Prerequisites**:
- [ ] You have a Linux system installed
- [ ] You have backup of critical data

**If you already enabled LUKS during installation**: Skip this section — you're done.

**If Linux was installed without encryption**: You have two options:

##### Option A: Encrypt /home Directory Only (Faster, Less Disruptive)

This encrypts only your user files, not the OS itself:

1. Open terminal
2. Encrypt your home directory:
   ```bash
   sudo ecryptfs-migrate-home -u $USER
   ```
3. Follow the prompts — this will take 30–60 minutes depending on data size
4. Restart your computer

##### Option B: Full System Reinstall with Encryption (Slower, More Complete)

1. Back up all your data to external drive
2. Download your Linux installer (Ubuntu, Fedora, Debian, etc.)
3. During installation, when prompted for "Encryption," select "Use LUKS" or "Encrypt the installation"
4. Choose a passphrase (6-word diceware phrase recommended)
5. Complete installation
6. Restore your backed-up data

Option B is recommended for Phase 2-level security, but Option A is acceptable if you have limited time.

---

#### 2.6 — iPhone: Enable Lockdown Mode

**Why now**: Lockdown Mode (iOS 16+) hardens iPhone against commercial spyware (Pegasus, Predator). It blocks dangerous attachment types, restricts JavaScript, disables wired connections when locked, and blocks FaceTime from non-contacts.

**Prerequisites**:
- [ ] iPhone with iOS 16 or later (check Settings → General → Software Update)
- [ ] You've completed Phase 1 (passcode, Face ID disabled, etc.)

##### Enable Lockdown Mode

1. Open Settings
2. Go to Privacy & Security → Lockdown Mode
3. Tap "Turn On Lockdown Mode"
4. Read the summary of what Lockdown Mode changes
5. Tap "Turn On Lockdown Mode" to confirm
6. Your iPhone will restart

##### Verify Lockdown Mode is Active

- Go back to Settings → Privacy & Security → Lockdown Mode
- You should see "Lockdown Mode is on" with a blue toggle

##### What Changes in Lockdown Mode

**Video calls**: FaceTime calls from non-contacts are blocked
- You'll see a notification if someone not in your contacts tries to call
- Any contact can call you normally

**Attachments in Messages**: Certain file types are blocked
- PDFs, Office documents, etc. will not open from Messages
- This is intentional — many exploits use document metadata

**Websites**: Some websites may break or render incorrectly
- This is because JavaScript is restricted
- You can temporarily disable Lockdown Mode if you need to access a problematic site

**Wired connections**: When your iPhone is locked, it won't communicate with USB-connected devices
- You won't be able to plug in car displays or other USB accessories while locked

**Are these trade-offs acceptable?** [ ] Yes / [ ] No → If No, you can disable Lockdown Mode

---

#### 2.9 — iPhone: SIM PIN (Can do with Lockdown Mode)

**Why**: A SIM PIN prevents someone with physical access to your iPhone from removing the SIM and using it in another device.

##### Enable SIM PIN

1. Open Settings
2. Go to Cellular → SIM PIN
3. Toggle ON "SIM PIN"
4. Set a 6-digit PIN (different from your phone passcode)
5. You'll be prompted for this PIN each time you restart your iPhone

---

### Week 4+ (Weeks 4–8 of Phase 2): Automated Maintenance & Optional Hardening

**Focus**: Data broker automation + optional hardware security key  
**Time**: 0.5–1 hour setup, then recurring quarterly

#### 2.7 — Data Broker Opt-Outs: Automation Setup

**Why now**: Data brokers re-add records from public sources every 3–6 months. Manual opt-outs from Phase 1.6 will expire. Automated services continuously re-submit removals.

**Prerequisites**:
- [ ] You completed Phase 1.6 (manual opt-outs with all 10 brokers)
- [ ] Budget available (~$96/year) OR willing to do manual re-submissions quarterly

##### Option A: Incogni (Recommended, ~$96/year)

**Incogni** is a service that automatically removes you from 420+ data brokers with 60-day re-submission cycles.

1. **Sign up**
   - Go to incogni.com
   - Click "Get Started"
   - Enter your name, email, address, phone number
   - Create account with ProtonMail email (from Phase 2.2)

2. **Pay anonymously**
   - Buy a prepaid Visa/Mastercard gift card with cash
   - Use the prepaid card to pay for Incogni subscription
   - Incogni will start removing your records from brokers

3. **Verify periodically**
   - Incogni dashboard shows removal progress
   - Check in monthly to see status
   - Most removals complete within 2–4 weeks

4. **Cost**: ~$96/year billed annually (or ~$12/month if you prefer monthly)

##### Option B: EasyOptOuts (Budget, ~$20/year)

**EasyOptOuts** is a lower-cost alternative with more limited coverage:

1. Go to easyoptouts.com
2. Follow the same process as Incogni
3. Cost: ~$20/year

##### Option C: Manual Quarterly Re-Submissions (Free but time-intensive)

If budget is not available, you can manually re-submit to the top 5 priority brokers every 3 months:

1. Every 3 months, re-submit to:
   - BeenVerified
   - Spokeo
   - WhitePages
   - Intelius
   - Radaris

2. This takes 15 minutes per quarter and covers the highest-visibility brokers

---

#### 2.8 — Hardware Security Key (Optional, ~$55)

**Why optional**: Phishing-resistant 2FA using a physical key instead of TOTP codes. Prevents account takeover even if your password is known. This is optional but recommended for high-value accounts (email, Bitwarden).

**Prerequisites**:
- [ ] Budget available (~$55)
- [ ] You're willing to keep track of a small USB key

##### Purchase YubiKey 5 NFC

1. **Order from yubico.com** — do NOT buy from Amazon Marketplace (supply chain risk)
2. **Choose YubiKey 5 NFC** — this works with iPhone via NFC and Windows/Linux via USB
3. Estimated delivery: 3–7 days

##### Set Up YubiKey

Once you receive the key:

1. **Gmail setup**:
   - Go to myaccount.google.com → Security → 2-Step Verification
   - Under "Security keys," click "Add security key"
   - Plug YubiKey into your computer (or touch NFC on iPhone)
   - Google will register the key
   - Save backup codes

2. **Bitwarden setup**:
   - Go to bitwarden.com → Account → Security → Two-step Login
   - Add "WebAuthn" or "Security Key"
   - Register your YubiKey
   - Save backup codes

3. **ProtonMail setup**:
   - Settings → Security → Two-factor authentication
   - Add "Security Key"
   - Register your YubiKey

4. **Keep the key safe**:
   - Store in your home safe or secure location
   - Don't lose it — you'll need it to unlock these accounts
   - You can register multiple keys (recommended: order a second for backup)

---

## Recurring Maintenance: Quarterly Schedule

Phase 2 is not a one-time setup — several items require ongoing maintenance.

### Every 3 Months (Quarterly)

- [ ] Re-check Mullvad connection: Go to mullvad.net/check and verify "You are connected to Mullvad"
- [ ] Update all software: Windows Update, iOS updates, app updates
- [ ] If using Incogni, check dashboard for removal progress
- [ ] If using manual opt-outs, re-submit to top 5 brokers (BeenVerified, Spokeo, WhitePages, Intelius, Radaris)
- [ ] Verify Bitwarden 2FA is still working (log out and back in with Ente Auth code)

### Every 6 Months

- [ ] Search your name on BeenVerified and Spokeo in a private window — verify you don't appear
- [ ] Review Phase 1 success criteria from PHASE_1_COMPLETION_WALKTHROUGH.md — ensure all are still active

### Every 12 Months

- [ ] Rotate your Mullvad account number (create new account, transfer payment, discard old)
- [ ] Update Tor Browser to latest version
- [ ] Reassess threat model — have your circumstances changed?
- [ ] Check EFF Deeplinks (eff.org/deeplinks) and 404media.co for new surveillance techniques

---

## Success Metrics: Phase 2 Complete

You have successfully completed Phase 2 when:

### Signal Isolation
- [ ] Mullvad VPN connected and kill switch verified ON
- [ ] Mullvad shows "You are connected" on mullvad.net/check
- [ ] VPN auto-connects on startup (Windows and iPhone)

### Email & Communication
- [ ] ProtonMail account created with 2FA enabled
- [ ] Tor Browser installed and verified connected to Tor network
- [ ] Tor Browser set to "Safest" security level

### Telemetry Reduction
- [ ] Windows telemetry set to "Required diagnostic data only"
- [ ] Activity history disabled on Windows
- [ ] App permissions audited and unnecessary access disabled
- [ ] Linux /home or full disk encryption enabled (if applicable)

### Device Hardening
- [ ] iPhone Lockdown Mode enabled
- [ ] iPhone SIM PIN set
- [ ] Tested that iPhone still works (FaceTime, Messages, cellular)

### Data Broker Management
- [ ] Incogni account created and removing records, OR manual quarterly re-submissions scheduled
- [ ] Verified no appearance on BeenVerified/Spokeo (2–4 week check)

### Account Resilience
- [ ] (Optional) YubiKey registered on Gmail, Bitwarden, and ProtonMail

---

## Timeline Summary: Phase 2 Execution

| Week | Focus | Items | Time |
|------|-------|-------|------|
| 1–2 | Signal Isolation | 2.1 Mullvad VPN, 2.2 ProtonMail | 1–2 hours |
| 2–3 | Anonymous Research & Telemetry | 2.3 Tor Browser, 2.4 Windows privacy | 1.5–2 hours |
| 3–4 | Mobile Hardening | 2.5 Linux encryption (if needed), 2.6 Lockdown Mode, 2.9 SIM PIN | 0.5–2 hours |
| 4+ | Automated Maintenance | 2.7 Incogni/EasyOptOuts, 2.8 YubiKey (optional) | 0.5–1 hour |

**Total time**: 5–7 hours over 4–8 weeks  
**Ongoing maintenance**: 15–30 minutes quarterly

---

## Contingency Procedures

### If Mullvad Won't Connect

**Symptom**: "Connecting..." indefinitely, or "Connection failed"

**Recovery**:
1. Restart the Mullvad app
2. Restart your computer
3. Check internet connection — do you have WiFi/cellular?
4. Try switching to a different server: Mullvad → Select location → choose Sweden server
5. Check mullvad.net/help for platform-specific issues
6. If still failing: Your payment may have expired — log into mullvad.net and add more payment time

---

### If ProtonMail Account Gets Locked

**Symptom**: You see "Account locked" or can't log in

**Recovery**:
1. Click "Forgot password" on login page
2. ProtonMail will send a reset link to your recovery email (the Gmail you set up during signup)
3. Check Gmail (check spam folder)
4. Click the reset link and set a new password
5. Update password in Bitwarden

---

### If Tor Browser Won't Connect

**Symptom**: "Connecting to Tor..." for >5 minutes, or "Tor not responding"

**Recovery**:
1. Restart Tor Browser
2. Wait up to 30 seconds for initial connection
3. Verify your internet connection
4. Check torproject.org/help for Tor network status
5. If Tor network is down (rare), wait 1–2 hours and try again
6. Try a different network: move to a coffee shop WiFi, use mobile hotspot, etc.

---

### If iPhone Lockdown Mode Breaks a Critical App

**Symptom**: App crashes, website won't load, FaceTime doesn't work in Lockdown Mode

**Recovery**:
1. Disable Lockdown Mode temporarily: Settings → Privacy & Security → Lockdown Mode → Turn Off
2. Restart iPhone
3. Test the app/website
4. If it works without Lockdown Mode, you have a trade-off choice:
   - Keep Lockdown Mode off (less secure)
   - Keep Lockdown Mode on and use different app/website (more secure)
5. If only one or two apps are broken, it may be worth keeping Lockdown Mode on

---

### If Your Mullvad Account Payment Expires

**Symptom**: You can't connect to Mullvad, or you get "Account not found"

**Recovery**:
1. Go to mullvad.net and log in with your account number
2. Add payment (cash mail, prepaid card, or cryptocurrency)
3. You should be able to reconnect within minutes

---

## Spending Tracker: Phase 2 Budget

| Item | Cost | Frequency | Status |
|------|------|-----------|--------|
| Mullvad VPN | ~$60/year | Recurring | [ ] Active |
| Incogni (optional) | ~$96/year | Recurring | [ ] Subscribed / [ ] Using manual method |
| ProtonMail | Free tier | One-time | [ ] Account created |
| Prepaid gift cards | ~$20–50 | One-time | [ ] Purchased |
| YubiKey 5 NFC (optional) | ~$55 | One-time | [ ] Ordered / [ ] Setup |

**Total Phase 2 spending**: $60/year minimum, ~$200–250/year for comprehensive setup

---

## Transition to Phase 3

Once Phase 2 is complete, you're ready for Phase 3 (Ongoing Operational Security). Phase 3 items are behavioral habits rather than one-time setup:

- **3.1 Device Discipline**: Compartmentalized identities (sensitive activity on separate device)
- **3.2 Leave Your Phone at Home**: For high-stakes situations, power down or Faraday bag
- **3.3 Disable 2G on iPhone**: Prevents IMSI catchers
- **3.4 Physical Security Practices**: Power-down before law enforcement situations
- **3.5 Social Media Hygiene**: Reduce OSINT surface
- **3.6 Financial Compartmentalization**: Use prepaid cards for sensitive activity
- **3.7 Document Metadata Stripping**: Remove metadata before sharing
- **3.8 Quarterly Maintenance Schedule**: Ongoing upkeep
- **3.9 Legal Resources**: Know your rights

Phase 3 is not time-limited — these are habits and ongoing practices. See PERSONAL_OPSEC_PLAN.md for details.

---

## Final Checklist: Phase 2 Ready to Launch

Before starting Week 1 of Phase 2, verify:

- [ ] Phase 1 complete (all 7 steps verified from PHASE_2_READINESS_CHECKLIST.md Part 1)
- [ ] Disk encryption active (BitLocker, VeraCrypt, or LUKS)
- [ ] Threat model clarified (from PHASE_2_READINESS_CHECKLIST.md Part 3)
- [ ] Time available (5–7 hours over 4–8 weeks)
- [ ] Budget available (minimum $60/year for VPN)
- [ ] Systems ready (admin access, payment method, internet connection)

**Phase 2 launch approval**: [ ] Ready / [ ] Not yet ready

---

*Last updated: 2026-06-14*  
*Corresponds to PERSONAL_OPSEC_PLAN.md Phase 2 (Steps 2.1–2.9)*
