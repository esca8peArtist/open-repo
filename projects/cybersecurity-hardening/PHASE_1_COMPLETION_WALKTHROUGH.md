---
title: "Phase 1 Completion Walkthrough: Steps 1.3–1.7"
project: cybersecurity-hardening
created: 2026-06-14
status: active
phase: 1
---

# Phase 1 Completion Walkthrough: Steps 1.3–1.7

**Purpose**: Comprehensive, step-by-step guide to completing Phase 1 of your personal OPSEC plan. This document assumes you have completed steps 1.1 (Signal), 1.2 (iPhone tracking lock-down), and are now continuing with disk encryption and credential migration.

**Reading time**: 15 minutes. **Execution time**: 90–120 minutes across 1–3 days.

**Prerequisites**: You must have completed steps 1.1 and 1.2 from PERSONAL_OPSEC_PLAN.md before starting 1.3.

---

## Step 1.3 — Windows/Linux: Full-Disk Encryption (BitLocker or VeraCrypt)

**Execution time**: 15 minutes setup + background encryption (1–24 hours depending on drive size)  
**Reboot required**: Yes, mandatory system restart  
**Common issues**: Password recovery complications, interrupted encryption process

### For Windows 10/11 Pro Users (BitLocker)

#### Pre-Flight Checklist
- [ ] You have 30–60 GB of free disk space (allows encryption to proceed without pausing)
- [ ] Your laptop is plugged into power (encryption process will pause if battery drops below 10%)
- [ ] No important work is unsaved (restart is mandatory)
- [ ] You have a USB drive or way to store your recovery key (do not skip this)

#### Exact Steps

1. **Plug into power and save all work**
   - Close all applications
   - Plug laptop into AC power
   - Do not unplug during the entire process

2. **Open Manage BitLocker**
   - Press `Windows Key + R` to open the Run dialog
   - Type: `manage-bde.msc` and press Enter
   - (Alternative: search "Manage BitLocker" in Windows Start menu)

3. **Start encryption**
   - In the list of drives, find your main drive (usually `C:`)
   - Click "Turn on BitLocker" next to it

4. **Save the recovery key (CRITICAL)**
   - A dialog will ask: "How do you want to store your recovery key?"
   - **SELECT: "Save to a file"**
   - **DO NOT select "Save to your Microsoft account"** — this defeats the purpose; Microsoft can be compelled to provide it
   - Choose to save to a USB drive or network location
   - Save the file name as: `BitLocker_Recovery_Key_C_drive_[DATE].txt` (e.g., `BitLocker_Recovery_Key_C_drive_June14_2026.txt`)
   - **VERIFY THE FILE WAS SAVED**: Open File Explorer and navigate to where you saved it — actually open it and confirm it contains a 48-digit recovery key
   - **Back this file up** — copy it to a second USB drive if you have one, or print it and store it in a secure physical location
   - **Write down the recovery key** on paper and store it separately from all devices

5. **Configure encryption options**
   - When asked "Do you want to encrypt the entire drive?", select **"Encrypt entire drive"** (not just used space)
   - When asked about "New encryption mode," select **"New encryption mode"** for a fixed internal drive
   - When prompted to "Run the system check," **CHECK the box** "Run BitLocker system check" and click Continue

6. **Restart the system**
   - You will be prompted to restart your computer
   - Click "Restart now"
   - **Your computer will restart and perform a system check** — this is normal and required

7. **After restart — verify encryption is active**
   - Once you log back in, search for "Manage BitLocker" again
   - The C: drive should now show **"BitLocker on"** with an encryption status percentage (e.g., "10% encrypted")
   - Do not use your laptop for CPU-intensive tasks while encryption is running in the background
   - **Encryption will complete in the background** — on a typical 500GB drive, expect 1–24 hours depending on drive usage

#### Recovery If BitLocker Fails

**Symptom**: "BitLocker" option doesn't appear in Manage BitLocker, or you get "BitLocker is not available"

**Causes and fixes**:
- **Windows Home edition**: BitLocker is not available; see VeraCrypt instructions below
- **Device doesn't support TPM 2.0**: Search "Device Security" in Windows Settings. If "Core isolation" shows "Not supported," use VeraCrypt instead
- **Group Policy restriction**: Search "gpcdit.msc" → Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption → Computer Drive. Set "Require additional authentication at startup" to "Not configured" or "Allow BitLocker without compatible TPM"

**If you lose the recovery key**:
- You must suspend BitLocker before you can unlock the drive
- Open Manage BitLocker, find your C: drive, click "Suspend protection"
- You'll then have the option to reset the recovery key
- This is a recovery path, but it requires you to have Windows access — so complete this immediately if recovery key is lost

---

### For Windows Home or Linux Users (VeraCrypt Alternative)

VeraCrypt is a free, open-source full-disk encryption tool. Use this if BitLocker is not available.

#### Pre-Flight Checklist
- [ ] Your laptop is plugged into power
- [ ] No important work is unsaved (restart is mandatory)
- [ ] You have at least 1 GB of RAM free
- [ ] You can access `veracrypt.fr` (use your phone as hotspot if needed)

#### Exact Steps

1. **Download VeraCrypt**
   - Go to `https://www.veracrypt.fr/en/Downloads.html`
   - Download the Windows or Linux installer for your system
   - **Verify the download**: Check the file hash on the veracrypt.fr website to ensure you downloaded the legitimate version
   - Run the installer and follow the standard installation process

2. **Launch VeraCrypt**
   - Open VeraCrypt
   - You'll see a window with a list of "Virtual Devices"

3. **Start system encryption**
   - Click **"System" → "Encrypt System Partition/Drive"**
   - Select **"Normal"** mode (not hidden volume)
   - Select **"Single-boot"** (you're only encrypting one OS)
   - Click **"Next"**

4. **Choose encryption method**
   - VeraCrypt will ask which encryption algorithm to use
   - **Select "AES"** — this is the standard and secure choice
   - Click **"Next"**

5. **Set your encryption password**
   - Choose a strong passphrase (6+ random words, or 20+ random characters)
   - Write this password down physically and store it securely
   - **If you forget this password, your drive is unrecoverable** — there is no recovery key like BitLocker
   - Type the password twice to confirm
   - Click **"Next"**

6. **Generate a rescue disk**
   - VeraCrypt will prompt you to create a "Rescue Disk"
   - **Click "Create Rescue Disk"** — this is a bootable USB drive that can help you recover if VeraCrypt won't boot
   - Save the ISO file to a USB drive using a tool like Rufus (rufus.ie) or Windows Disk Manager
   - **Keep this USB drive in a secure location** — label it "VeraCrypt Rescue Disk"
   - Click **"Next"**

7. **Test encryption**
   - VeraCrypt will ask if you want to "Test" or "Install"
   - **SELECT "Test"** — this verifies encryption will work before committing
   - Your computer will restart and boot from the VeraCrypt pre-boot environment
   - You'll enter your encryption password at a black screen with white text before Windows loads
   - **Verify you can enter your password and Windows boots normally** — this is critical
   - Once Windows loads, VeraCrypt will ask if the test succeeded
   - Click **"Yes"** to confirm

8. **Encrypt the drive**
   - Close VeraCrypt
   - Open VeraCrypt again
   - Click **"System" → "Encrypt System Partition/Drive"** again
   - Follow the same steps as before
   - At the final step, **SELECT "Install"** (not "Test")
   - Confirm the message asking if you're sure
   - Your system will restart and begin encryption

9. **After restart — verify encryption is active**
   - You'll see a black screen before Windows boots — this is the VeraCrypt pre-boot authentication
   - Enter your encryption password
   - Once Windows loads, open VeraCrypt and verify "System encryption" shows as active

#### Recovery If VeraCrypt Fails

**Symptom**: VeraCrypt won't boot, or you get an error at the pre-boot screen

**Causes and fixes**:
- **Incorrect password at boot**: The pre-boot screen shows your password in plaintext as you type. If you see an error "No valid keyfile found" or "Invalid password," verify Caps Lock is off and try again. You get 3 attempts before VeraCrypt locks you out for safety
- **Rescue Disk recovery**: If you're locked out, boot from the VeraCrypt Rescue Disk (you created this in step 6). The Rescue Disk can help you troubleshoot or reinstall the VeraCrypt bootloader
- **Windows won't boot after encryption**: If Windows fails to boot after encryption completes, you may need to use the Rescue Disk. This is rare but possible if encryption was interrupted

---

## Step 1.4 — iPhone: Authenticator App + Account Transition (Ente Auth)

**Execution time**: 30–45 minutes  
**Accounts to convert**: Email (Gmail, Outlook, iCloud), financial (banking, investment accounts), social media (if applicable)  
**Parallel possibility**: Can be done while 1.3 disk encryption runs in background

### Part A: Install Ente Auth

#### Pre-Flight Checklist
- [ ] You have your iPhone
- [ ] You are connected to WiFi or cellular
- [ ] You have internet access for scanning QR codes (you'll need to be able to open account security pages on your computer or another device simultaneously)

#### Exact Steps

1. **Download Ente Auth from App Store**
   - Open the App Store on your iPhone
   - Search for "Ente Auth"
   - Verify the developer is "Ente" (or "Ente Technologies SZ")
   - Tap "Get" → "Install"
   - Open the app once installed

2. **Create an Ente Auth account (optional but recommended)**
   - Ente Auth can sync your TOTP codes across devices if you create an account
   - Tap the menu icon (three horizontal lines) in Ente Auth
   - Tap "Settings" → "Account"
   - Tap "Create an account" (use your email)
   - This is optional — you can also use Ente Auth locally without syncing
   - If you skip this, your TOTP codes will be stored only on this device

3. **Verify installation**
   - You should see an empty list of "Accounts" in Ente Auth
   - You're ready to add your first two-factor codes

---

### Part B: Transition Your Email Account to Authenticator App

**Critical order**: Do email accounts first. If email gets compromised while SMS 2FA is still active, an attacker can reset your SMS 2FA and take over the account. Ente Auth removes this window.

#### Gmail / Google Account

1. **Open Gmail account security page**
   - On your computer, go to `myaccount.google.com`
   - Click "Security" on the left sidebar
   - Scroll to "How you sign in to Google"
   - Click "2-Step Verification"

2. **Remove SMS 2FA (after setting up authenticator app)**
   - You'll see a list of verification methods
   - **Do not delete SMS yet** — we'll set up the authenticator app first, then remove SMS
   - Click "Authenticator app" or "Add another authenticator app"

3. **Scan QR code with Ente Auth**
   - Google will show a QR code
   - On your iPhone, open Ente Auth
   - Tap the "+" button (add new code)
   - Select "Scan QR code"
   - Point your iPhone camera at the QR code on your computer screen
   - Ente Auth will automatically capture the code and add "Google" to your account list

4. **Verify Ente Auth is working**
   - In Ente Auth, tap the "Google" entry
   - A 6-digit code will appear (it changes every 30 seconds)
   - Go back to the Google security page and enter this code to verify
   - Google will show "Authenticator app verified"

5. **Save backup codes**
   - Google will display 8 backup codes
   - **IMPORTANT**: Take a screenshot or write these codes down on paper
   - Store them in a secure location (encrypted password manager, printed and physically stored)
   - These codes are your recovery if you lose your phone

6. **Remove SMS 2FA**
   - Go back to the 2-Step Verification page
   - You should see both "Authenticator app" and your "Phone" listed
   - Click "Phone" and select "Remove"
   - Confirm that you want to remove phone verification
   - You're done with Gmail — you now have authenticator-based 2FA instead of SMS

#### Microsoft / Outlook Account

1. **Open Outlook security settings**
   - Go to `account.microsoft.com` on your computer
   - Click "Security" in the left sidebar
   - Click "Advanced security options"
   - Scroll to "Verify your identity" section
   - Click "Set up authenticator app"

2. **Scan QR code with Ente Auth**
   - Microsoft will show a QR code
   - On your iPhone, open Ente Auth
   - Tap the "+" button
   - Select "Scan QR code"
   - Point your camera at the Microsoft QR code
   - Ente Auth will add "Microsoft" to your account list

3. **Verify Ente Auth is working**
   - In Ente Auth, tap the "Microsoft" entry
   - Copy the 6-digit code
   - Go back to the Microsoft page and paste the code
   - Microsoft will show "Authenticator app verified"

4. **Save backup codes**
   - Microsoft will display backup codes (usually 10 codes)
   - Screenshot or write them down on paper
   - Store securely in password manager or printed location

5. **Remove SMS/phone verification**
   - On the "Advanced security options" page, find your registered phone number under "Ways to verify your identity"
   - Click the X next to it to remove it
   - Confirm you want to remove phone verification

#### iCloud Account

1. **Open iCloud security settings**
   - On your computer, go to `appleid.apple.com`
   - Sign in with your Apple ID
   - Click "Security" on the left
   - Scroll to "Two-Factor Authentication"
   - You should see "Two-Factor Authentication is turned on"

2. **Add authenticator app**
   - Scroll down to "Security key and password sign-in"
   - iCloud doesn't have a traditional "authenticator app" setting — instead, you'll use your iPhone's built-in "Authenticator" or Ente Auth for any backup access
   - For iCloud, the main 2FA method is your trusted devices
   - **Ensure all non-trusted devices are removed**: On the "Security" page, scroll to "Devices" and remove any devices you no longer use

3. **For third-party iCloud access (less important)**
   - iCloud's 2FA is primarily device-based, not code-based
   - You don't need to add a TOTP code for iCloud itself
   - Verify that "Two-Factor Authentication is on" — that's sufficient

#### Financial Accounts (Bank, Investment, Broker)

Repeat the pattern for each account:

1. **Log into your bank's website**
2. **Navigate to Settings → Security or "Two-Factor Authentication"**
3. **Find the option "Add authenticator app" or "Switch from SMS to authenticator"**
4. **Scan the QR code with Ente Auth** — tap the "+" in Ente Auth, select "Scan QR code," point at the QR code
5. **Verify the code works** — enter the 6-digit code from Ente Auth into your bank's page
6. **Save backup codes** — screenshot or write them down
7. **Remove SMS 2FA** — find the option to remove phone verification from that account

**Common variations**:
- Some banks call it "2FA," others call it "Multi-Factor Authentication" or "MFA"
- Some banks don't show a QR code — they show a "secret key" (a long alphanumeric string). In Ente Auth, tap "+" → "Enter code manually" and paste the secret key
- Some banks let you keep SMS as a backup while adding the authenticator app — this is fine, but prioritize removing SMS as the primary method

---

### Part C: Set Carrier Port-Out PIN (Prevents SIM Swap)

While you're in account security settings, add a PIN to your carrier's account. This prevents someone from calling your carrier and having your phone number transferred to another SIM.

#### AT&T

1. Call AT&T customer service: 1-800-331-0500
2. Ask to enable "Extra Security" on your account
3. This will require a PIN for any account changes

#### T-Mobile

1. Open the T-Mobile app on your iPhone
2. Tap Profile (person icon at bottom right)
3. Go to Security → SIM Protection
4. Enable SIM Protection
5. Set a PIN (different from your phone's PIN)

#### Verizon

1. Go to `myverizon.verizon.com` on your computer
2. Go to Profile → Account settings → Security
3. Click "Number Lock"
4. Enable Number Lock with a PIN

---

## Step 1.5 — Password Manager Setup (Bitwarden)

**Execution time**: 30–45 minutes  
**Platforms**: Windows (desktop app) + iPhone (mobile app) + browser extension  
**Parallel possibility**: Can overlap with disk encryption running in background

### Part A: Download and Install Bitwarden

#### Windows Desktop App

1. **Download Bitwarden**
   - Go to `bitwarden.com` in your browser
   - Click "Get started" or "Download"
   - Download the Windows executable
   - Run the installer and follow prompts
   - Open Bitwarden once installed

2. **Create a Bitwarden account**
   - You'll see a login screen with "Create account" link
   - Click "Create account"
   - **Email**: Use your primary email (the one you just secured with authenticator app)
   - **Master password**: Choose a strong passphrase (6+ random words, similar to your disk encryption password)
   - **Master password confirmation**: Repeat it
   - Click "Create account"

3. **Write down your master password**
   - **CRITICAL**: If you forget the master password, Bitwarden cannot recover it — the vault is irrecoverable
   - Write it on paper and store it securely (in your home safe, or with a trusted person)
   - Do not store it in any cloud service or on your computer

4. **Verify email**
   - Bitwarden will send you a verification email
   - Open the email and click the verification link
   - Your Bitwarden account is now active

#### iPhone App

1. **Download Bitwarden from App Store**
   - Search for "Bitwarden"
   - Verify the developer is "Bitwarden Inc."
   - Tap "Get" → "Install"

2. **Sign in**
   - Open the Bitwarden app
   - Tap "Log in"
   - Enter the email and master password you just created
   - Tap "Log in"

3. **Enable Face ID (optional but recommended)**
   - After logging in, tap the menu icon (three lines, bottom right)
   - Tap "Settings"
   - Tap "Unlock with Face ID" and enable it
   - This lets you unlock Bitwarden with Face ID instead of re-entering your master password each time

---

### Part B: Enable Two-Factor Authentication on Bitwarden Itself

Your Bitwarden account now needs 2FA (using Ente Auth from Step 1.4).

1. **Access Bitwarden settings**
   - On your computer, go to `bitwarden.com` and log in
   - Click your email/profile icon in the top right
   - Click "Account settings"

2. **Enable 2FA**
   - Click "Security" on the left sidebar
   - Scroll to "Two-step Login"
   - Click the Authenticator option
   - Bitwarden will show a QR code

3. **Scan with Ente Auth**
   - On your iPhone, open Ente Auth
   - Tap the "+" button
   - Select "Scan QR code"
   - Point at the Bitwarden QR code
   - Ente Auth will add "Bitwarden" to your account list

4. **Verify and save backup codes**
   - Go back to Bitwarden and enter the 6-digit code from Ente Auth
   - Bitwarden will show backup codes — screenshot or write them down
   - Store these codes securely

---

### Part C: Install Browser Extension

1. **Add Bitwarden to your browser**
   - Open your web browser (Chrome, Firefox, Edge, Safari)
   - Go to `bitwarden.com/download` and select your browser
   - Click "Install" for your browser extension
   - Approve the extension installation
   - A Bitwarden icon will appear in your toolbar

2. **Set up extension login**
   - Click the Bitwarden icon in your toolbar
   - Log in with your email and master password
   - Enable "Unlock with OS login" (uses Windows/Mac password) — this is optional
   - Click the lock icon to lock the extension (it will auto-lock when your computer sleeps)

---

### Part D: Import Your First Passwords

You now have three options:

**Option 1: Manual entry** (safest, more friction)
- For each important account, manually create an entry in Bitwarden
- Next time you log in to a site, the browser extension will prompt you to save the password

**Option 2: Export from existing password manager** (if you're switching from another tool)
- If you use Password Manager, Chrome Password Manager, etc., you can export and import those passwords
- Bitwarden's help docs explain how to do this: `bitwarden.com/help/import-data`

**Option 3: Save passwords as you log in**
- Every time you log into a website, Bitwarden will ask "Do you want to save this password?"
- Click "Save" — this gradually builds your password vault

**Recommended approach for now**: Manual entry for your 5–10 most important accounts (email, bank, investment accounts, Mullvad account, etc.), then add the rest as you log in to them over the next week.

#### Manual Entry Example

1. Click the Bitwarden icon in your browser
2. Click the "+" button (Add item)
3. **Name**: "Gmail" or "Google"
4. **Username**: your email address
5. **Password**: generate a new random password (click the dice icon) — this is now 20+ characters and unique to Gmail
6. Click "Save"

**Then, go to Gmail.com and update your password**:
1. Go to `myaccount.google.com`
2. Click "Security" → "Your password"
3. Enter your old password
4. Enter the new password Bitwarden generated
5. Confirm

Your Gmail account now has a unique, strong, random password stored in Bitwarden.

---

### Alternative: KeePassXC (Offline Password Manager)

If you prefer a local-only password manager with zero cloud exposure:

1. **Download KeePassXC**
   - Go to `keepassxc.org`
   - Download for Windows
   - Install normally

2. **Create a local vault**
   - Open KeePassXC
   - Click "Create new database"
   - Choose a location to save (your encrypted drive)
   - Set a master password
   - Save

3. **Trade-offs**:
   - No cloud sync — you manually copy passwords to your iPhone via AirDrop or copying passphrases
   - More friction than Bitwarden, but zero cloud exposure
   - Use KeePassXC on Windows + Bitwarden on iPhone for a hybrid approach

---

## Step 1.6 — Data Broker Opt-Outs: First Wave

**Execution time**: 45–60 minutes  
**Platforms**: Computer with web browser  
**Parallel possibility**: Can be done while disk encryption runs in background  
**Important note**: Bring up all 10 sites in separate browser tabs before starting — this reduces time spent switching contexts

### Pre-Flight Checklist

- [ ] You have 45 minutes of uninterrupted time
- [ ] You have a browser open (Chrome, Firefox, Safari, Edge — all work the same)
- [ ] You have your name, city, and phone number available (needed for some opt-out forms)
- [ ] You have the ability to verify email addresses (check your spam folder frequently)

### Batch Opt-Out Instructions

**Why we're doing this in one sitting**: Data brokers monitor the same forms. Doing them all at once creates a batch signal that you're actively protecting yourself. Doing them one per week spreads out the signal.

#### Step 1: Open All 10 Sites in New Tabs

Right-click these links and select "Open in new tab" for each one:

1. LexisNexis: https://optout.lexisnexis.com/
2. BeenVerified: https://www.beenverified.com/app/optout/search
3. Spokeo: https://www.spokeo.com/optout
4. WhitePages: https://www.whitepages.com/suppression-requests
5. Intelius: https://www.intelius.com/opt-out/
6. TruePeopleSearch: https://www.truepeoplesearch.com/removal
7. FastPeopleSearch: https://www.fastpeoplesearch.com/removal
8. FamilyTreeNow: https://www.familytreenow.com/optout
9. Radaris: https://radaris.com/page/how-to-remove
10. Acxiom: https://isapps.acxiom.com/optout/optout.aspx

You should now have 10 tabs open.

---

#### Step 2: Process Each Site (Estimated Times)

**LexisNexis (5–10 minutes)** — Highest priority, confirmed ICE contract

1. Go to the LexisNexis tab
2. Click "Find My Records" or "Search Records"
3. Enter your name and city
4. Click "Search"
5. You may see 0–10 results with your records
6. For each record showing your information:
   - Select it (checkbox)
   - Follow the "Opt-Out" button
7. LexisNexis may ask for ID verification (driver's license or other government ID)
   - You can upload a photo of your ID
   - Or skip this step, and re-submit in 2–4 weeks if the record re-appears
8. Confirm your request
9. **Status**: LexisNexis will email you a confirmation — check your email (including spam folder) in 24–48 hours

**BeenVerified (3–5 minutes)**

1. Go to the BeenVerified tab
2. Enter your name and click "Search"
3. You may see a result with your information
4. Click "Remove" or "Opt-Out" (varies by layout)
5. Enter your email to confirm the opt-out
6. BeenVerified will send a confirmation email — verify in 24 hours

**Spokeo (3–5 minutes)**

1. Go to the Spokeo tab
2. Search for your name and city
3. If you appear in results, click "Remove this profile"
4. Enter your email
5. Confirm your opt-out
6. Check email for confirmation

**WhitePages (3–5 minutes)**

1. Go to the WhitePages tab
2. Search your name and city
3. If you appear, click "Suppress this listing" or "Remove"
4. Confirm your email address
5. Complete the opt-out

**Intelius (3–5 minutes)**

1. Go to the Intelius tab
2. Search your name
3. If results appear, click "Opt Out" next to each result
4. Enter your email
5. Confirm

**TruePeopleSearch (2–3 minutes)**

1. Go to the TruePeopleSearch tab
2. Search your name
3. Click "Remove" next to your result
4. Enter your email address
5. Submit

**FastPeopleSearch (2–3 minutes)**

1. Go to the FastPeopleSearch tab
2. Search your name
3. Click "Remove" next to your result
4. Enter your email
5. Confirm removal request

**FamilyTreeNow (2–3 minutes)**

1. Go to the FamilyTreeNow tab
2. Search your name
3. Click "Remove" next to your profile
4. Enter your email
5. Submit

**Radaris (3–5 minutes)**

1. Go to the Radaris tab
2. Search your name
3. Click "Remove" or "Opt-Out"
4. You may need to solve a CAPTCHA
5. Enter email
6. Confirm

**Acxiom (3–5 minutes)**

1. Go to the Acxiom tab
2. Click "Request Your Data" or "Opt-Out"
3. Enter your name, email, and address
4. Acxiom may require email verification
5. Confirm the opt-out

---

#### Step 3: Federal Opt-Outs (2–3 minutes)

Open these three in new tabs and complete them:

**OptOutPrescreen (1–2 minutes)** — Pre-screened credit/insurance offers

1. Go to https://www.optoutprescreen.com
2. Click "Opt Out Online"
3. Confirm "I want to opt out for 5 years"
4. Scroll through and confirm all the checkboxes
5. Click "Submit" — you're done

**Network Advertising Initiative (1–2 minutes)** — Ad network opt-out

1. Go to https://optout.networkadvertising.org
2. Click "Visit our tool"
3. Click "Opt-Out" (you may need to open in a private/incognito window if it doesn't load)
4. A list of ad networks appears — you can select all and click "Opt-Out All"
5. You should see "You have successfully opted-out of X ad networks"

**About Ads (1–2 minutes)** — Another ad network opt-out (different member networks)

1. Go to https://optout.aboutads.info
2. Click "Choices" or "Learn more about these ads"
3. Click "Opt-Out All"
4. Confirm all listed networks are opt-ed out

---

### Step 4: Verification and Re-Submission (Do This in 2–4 Weeks)

1. **Check your email** (spam folder) for confirmation messages from each broker
2. **Search yourself in 2–4 weeks**: In a private browser window, search your name on BeenVerified and Spokeo
3. **Re-submit if needed**: If your information re-appeared, submit the opt-out again

---

### Recovery If a Site Doesn't Process Your Opt-Out

**Common issues**:

- **"Cannot find your record"**: The site may not have your data, or your search method didn't match. Try searching with different name variations (middle initial, full middle name, different city)
- **CAPTCHA won't load**: Refresh the page or try a different browser
- **Email confirmation doesn't arrive**: Check spam folder. If it doesn't arrive in 48 hours, submit the opt-out again with a different email address (use a secondary email if you have one)

**If you get stuck on one broker**: Skip it and move on. You can return to it later. The goal is to complete the batch process — 8/10 completed is better than getting stuck on 1/10.

---

## Step 1.7 — iPhone: Passcode Over Face ID

**Execution time**: 5 minutes  
**Devices**: iPhone only  
**No restart required**

### Why This Matters

In most U.S. jurisdictions, law enforcement can compel you to use your fingerprint or face to unlock a device by court order. However, compelling you to reveal a PIN is legally contested under the Fifth Amendment (protection against self-incrimination). A PIN you refuse to provide is more legally defensible than a face you cannot hide.

### Exact Steps

1. **Open iPhone Settings**
   - Tap "Settings" (gear icon) on your home screen
   - Scroll down and tap "Face ID & Passcode" (or "Touch ID & Passcode" on older iPhones)

2. **Disable Face ID for iPhone Unlock**
   - You'll see "Use Face ID For:" with options listed below (Unlock iPhone, Apple Pay, etc.)
   - Toggle OFF the switch next to "Unlock iPhone"
   - You'll be prompted to confirm — tap "Turn Off"
   - Face ID is now disabled for unlocking, but it still works for Apple Pay and Apps

3. **Verify your passcode is strong**
   - Scroll down in the same screen to see "Change Passcode"
   - Your current passcode should be at least 6 digits
   - For maximum security, tap "Change Passcode" and upgrade to an **alphanumeric custom passcode**:
     - Tap "Change Passcode"
     - Enter your current passcode
     - Tap "Passcode Options" (appears during setup)
     - Select "Custom Alphanumeric Code"
     - Enter a new password with letters, numbers, and special characters (e.g., "BlueMoon#2026Safe")
     - Confirm it twice

4. **Test the new unlock method**
   - Press the side button to lock your iPhone
   - Press it again and swipe up — you should see a numeric keypad (or alphanumeric if you chose custom)
   - Enter your passcode to unlock

5. **Practice Emergency SOS gesture**
   - Press the side button (power button) and either volume button simultaneously
   - Hold for 3 seconds — you should see "Emergency SOS" slider
   - Release — Face ID is now disabled until you enter your passcode
   - This gesture also works if someone tries to force you to unlock with Face ID
   - Practice this gesture 3–5 times until it's automatic muscle memory

### Verification

- [ ] Face ID toggle next to "Unlock iPhone" is OFF
- [ ] Your passcode is 6+ digits (or alphanumeric custom code)
- [ ] You can unlock your iPhone with your passcode
- [ ] You practiced the Emergency SOS gesture (side button + volume button)

---

## Phase 1 Completion Checklist

After completing all 7 steps, verify the following:

### Disk Encryption (1.3)
- [ ] BitLocker shows "on" in Manage BitLocker, or VeraCrypt pre-boot authentication works
- [ ] Recovery key/Rescue Disk is saved in two separate locations
- [ ] Encryption is in progress or complete (check status in Manage BitLocker)

### Authenticator App (1.4)
- [ ] Ente Auth is installed on iPhone
- [ ] Gmail 2FA is using authenticator app (SMS removed)
- [ ] Microsoft/Outlook 2FA is using authenticator app (SMS removed)
- [ ] iCloud security is set to Two-Factor Authentication (on)
- [ ] Bank account(s) have 2FA via authenticator app (SMS removed)
- [ ] Carrier SIM PIN or port-out PIN is enabled (AT&T Extra Security, T-Mobile SIM Protection, or Verizon Number Lock)

### Password Manager (1.5)
- [ ] Bitwarden desktop app is installed and logged in
- [ ] Bitwarden iPhone app is installed and logged in
- [ ] Bitwarden browser extension is installed
- [ ] Bitwarden account has 2FA enabled (via Ente Auth)
- [ ] At least 5 passwords are saved (email, bank, Mullvad, Bitwarden master password written down and stored securely)

### Data Broker Opt-Outs (1.6)
- [ ] All 10 broker opt-outs submitted
- [ ] OptOutPrescreen submitted
- [ ] Network Advertising Initiative and About Ads opt-outs submitted
- [ ] You have a reminder to re-submit in 2–4 weeks

### iPhone Passcode (1.7)
- [ ] Face ID is disabled for iPhone unlock
- [ ] Passcode is 6+ digits (or alphanumeric custom)
- [ ] You can unlock with passcode
- [ ] You practiced Emergency SOS gesture (side button + volume button)

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| BitLocker won't start on Windows Home | Use VeraCrypt instead (included in Windows Home support above) |
| VeraCrypt password forgotten | Use VeraCrypt Rescue Disk to reset bootloader, or reinstall Windows |
| Ente Auth won't scan QR code | Ensure app has camera permission (Settings → Privacy → Camera) |
| Bitwarden account locked after 2FA setup | Use backup codes from step 1.5 to regain access |
| Data broker opt-out email doesn't arrive | Check spam folder; re-submit with different email if needed |
| Face ID still unlocks after disabling | Restart iPhone; check that toggle is actually OFF |

---

## Success Criteria: Phase 1 Complete

You have successfully completed Phase 1 when:

1. **Your Windows/Linux drive is encrypted** — disk encryption in progress or complete
2. **All SMS 2FA is gone** — email, bank, and investment accounts use authenticator app
3. **Password manager is in use** — Bitwarden storing passwords on Windows, iPhone, and browser
4. **Data brokers have received opt-outs** — all 10 brokers + federal opt-outs submitted
5. **iPhone is more resilient** — passcode replaces Face ID as primary unlock method, SIM PIN set

**Estimated completion time**: 90–120 minutes across 1–3 days (disk encryption may run 1–24 hours in background).

**Next step**: Once all 7 steps are complete, you're ready to assess Phase 2 readiness. See PHASE_2_READINESS_CHECKLIST.md.

---

*Last updated: 2026-06-14*  
*Corresponds to PERSONAL_OPSEC_PLAN.md Phase 1 (Steps 1.3–1.7)*
