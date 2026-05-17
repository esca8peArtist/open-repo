---
title: "Phase 1 Next Steps — Steps 1.4 to 1.7 Detailed Guide"
project: cybersecurity-hardening
created: 2026-05-17
status: active
workflow: After Windows restart + VeraCrypt encryption starts, proceed with 1.4-1.7
---

# Phase 1 Completion Guide: Steps 1.4–1.7

**Current Status**: Steps 1.1–1.3 done or in-progress. This guide covers the remaining Phase 1 steps.

**Timeline**: 1.5–2 hours total for all four steps if done in sequence.

**What's blocking**: Step 1.3 (VeraCrypt) requires Windows restart. Once that's complete and encryption is running in the background, proceed here.

---

## Step 1.4 — Ente Auth: Switch Email + Financial 2FA Off SMS

**Time**: ~30 minutes  
**Device**: iPhone (downloaded from App Store) + any account with 2FA enabled  
**Cost**: Free  
**Threat addressed**: SIM swapping → account compromise → identity theft and law enforcement access to email/banking

### Install Ente Auth

1. On iPhone: **App Store** → search "Ente Auth"
2. Tap the app labeled **"Ente Auth"** (icon: lock + "e" logo; developer: Ente)
3. Tap **"Get"** → authenticate with Face ID
4. Tap **"Open"** when installation completes

### Get Recovery Codes Before You Change Anything

**Critical**: Each account provides "backup codes" when you enable 2FA. These are 10-16 one-time use codes that let you access your account if you lose your phone. You MUST save these before enabling Ente Auth.

**Storage**: Save them in:
- Bitwarden (once you set it up in step 1.5), marked as backup codes
- A printed document locked in a safe
- Do NOT email them to yourself
- Do NOT screenshot them unsecurely

### Email Accounts: Gmail → Ente Auth

Gmail is highest priority (it's your account recovery mechanism for every other service).

**Steps**:
1. **On your Mac/iPad/laptop**: Go to https://myaccount.google.com
2. **Left sidebar** → **"Security"** → **"How you sign in to Google"** → **"2-Step Verification"**
3. **Scroll to "Authenticator app"** → click **"Get started"**
4. If you have an existing authenticator (e.g., Google Authenticator): click **"Change your authenticator app"** → **"Switch to a different authenticator app"**
5. A QR code will appear
6. **On your iPhone**, open Ente Auth → tap **"+"** (plus button, upper right)
7. Tap **"Scan QR code"** → scan the Google QR code
8. Ente Auth will now show a 6-digit code for Gmail
9. Enter that 6-digit code on the Google web page → tap **"Turn on"**
10. Google will show you **10 recovery codes** → **SAVE THESE IMMEDIATELY** to Bitwarden (step 1.5) or print them
11. After saving recovery codes, complete the setup

**Verification**: Sign out of Gmail and sign back in. When prompted for the 2-step code, open Ente Auth and enter the code.

### Email Accounts: Microsoft (Outlook/Hotmail) → Ente Auth

Same process as Gmail:

1. Go to https://account.microsoft.com/security
2. **"Advanced security options"** → **"Additional security verification"** → **"Set up a different app"**
3. Scan the QR code with Ente Auth
4. Enter the 6-digit code
5. **SAVE THE RECOVERY CODES** (Microsoft will display them)

### Financial Accounts (Bank, Credit Card, Brokerage)

**Warning**: Bank accounts are often picky about authenticator changes. If the bank requires you to call in or visit a branch, that's normal. Do it.

**Process** (varies by bank, but usually):
1. Log into your bank's website
2. **Settings** → **"Security"** or **"Two-Factor Authentication"**
3. Find option to change from SMS to Authenticator app
4. Some banks will send a confirmation to your email AND SMS before allowing the change (for security)
5. Once approved, scan the QR code with Ente Auth
6. Save recovery codes

**Example**: For Fidelity/Schwab: log in → **Settings** → **Security** → **Two-Factor Authentication** → toggle SMS off → enable "App-based" → scan with Ente Auth.

**If your bank doesn't support authenticator apps**:
- Call their security team and ask what 2FA methods they support
- Request one that is NOT SMS (hardware key or TOTP authenticator app)
- If they insist on SMS only, that's a problem — seriously consider switching banks

### Social Media (if used): Twitter, Facebook, etc.

These are lower priority than financial accounts. Follow the same pattern:
1. **Settings** → **Security** → **Two-Factor Authentication**
2. Change from SMS → authenticator app
3. Scan QR code
4. Save recovery codes

### After Ente Auth Setup

- Test it: sign out and sign back in, use Ente Auth code for 2FA
- In Ente Auth settings: enable "Setup key (if lost)" backup option if available
- Leave Ente Auth on your home screen; you'll be opening it frequently

---

## Step 1.5 — Bitwarden: Password Manager Setup

**Time**: ~20 minutes  
**Platform**: Windows desktop app + iPhone app + browser extension  
**Cost**: Free  
**Threat addressed**: Password reuse → credential breach → account takeover → attacker assumes your identity

### Install Bitwarden

**Windows**:
1. Go to https://bitwarden.com/download/ in your web browser
2. Download the **Windows Desktop app**
3. Run the installer and complete installation
4. Launch Bitwarden

**iPhone**:
1. **App Store** → search "Bitwarden"
2. Tap the official Bitwarden app (developer: Bitwarden)
3. Tap **"Get"** → authenticate → **"Open"**

**Browser extension** (install this on every browser you use — Chrome, Edge, Firefox, Safari, etc.):
1. In your browser, search for "Bitwarden" in the extensions store (e.g., Chrome Web Store)
2. Install the official Bitwarden extension
3. Pin it to your toolbar for easy access

### Create Your Bitwarden Master Password

This is the MOST critical password you'll ever create. You cannot recover it if lost — Bitwarden cannot reset it.

**Rules**:
- 12+ characters
- Mix of uppercase, lowercase, numbers, symbols
- Completely random (not derived from your name, address, birthday, etc.)
- **Write it down on physical paper** and store the paper in a safe location
- Do NOT email it to yourself
- Do NOT save it in notes on your phone

**Better approach — passphrase**:
- 5–6 random, unrelated words: "trumpet-gallop-mountain-fern-bicycle" (longer, easier to remember)
- Write it down anyway as a backup

### Create Bitwarden Account

1. Open Bitwarden desktop app or browser extension
2. Tap **"Create Account"**
3. **Email**: your primary email address
4. **Master Password**: your strong password from above
5. **Master Password Hint** (optional): something only you understand (e.g., "First dog favorite color" if your first dog was a golden retriever — the answer would be "golden" — but make it idiosyncratic)
6. Accept terms → **"Create Account"**
7. Log in with your email and master password

### Enable Two-Factor Authentication on Bitwarden

Your Bitwarden vault is now password-protected, but we need to add 2FA to it as well.

1. **Settings** (gear icon, top right of Bitwarden) → **"Account"** → **"Two-step Login"**
2. Tap **"Authenticator app"** (TOTP)
3. A QR code will appear
4. **On your iPhone**, open **Ente Auth** → tap **"+"** (plus)
5. Scan the Bitwarden QR code
6. Ente Auth will show a 6-digit code
7. Enter that code in Bitwarden → **"Enable"**
8. Bitwarden will show recovery codes → **SAVE THESE IMMEDIATELY**
9. From now on, when you log into Bitwarden, you'll be asked for a 6-digit code from Ente Auth

### Start Adding Passwords

1. **Browser extension**: When you log into any website, Bitwarden will ask "Save this password?" → tap **"Save"**
2. **Desktop app**: Tap **"+ New item"** → **"Login"** → fill in website/username/password → **"Save"**

**For accounts you've already created**, you can manually add them:
- Desktop app → **"+ New item"** → **"Login"**
- **Name**: website name (e.g., "Gmail")
- **Username**: your email or username
- **Password**: password (or tap **"Generate"** to create a strong random one)
- **URL**: https://accounts.google.com (or the login page URL)

### Critical: Update Key Passwords

Immediately update passwords for these accounts in Bitwarden and on the websites:
- Email accounts (Gmail, Outlook, etc.)
- Financial accounts (banks, credit cards, brokerages)
- Your router admin password (if you've never changed it)

**How to generate strong passwords**:
- In Bitwarden, when creating a new login or editing an existing one, tap **"Generate"**
- It will create a 20-character random password: `Np!x%K2mL@5qJ&9wR#7v`
- You never need to memorize this — Bitwarden autofills it for you

---

## Step 1.6 — Data Broker Opt-Outs: Remove Yourself from Public Databases

**Time**: ~45 minutes (this is tedious but high-impact)  
**Platform**: Any browser  
**Cost**: Free (automated services cost ~$96/year; manual is free)  
**Threat addressed**: Doxxers finding your address/phone/family → harassment; law enforcement purchasing your data without warrant

### Why This Matters

Palantir's ELITE platform links commercial data broker data (your address, phone number, relatives) into government law enforcement records. ICE explicitly purchases data from BeenVerified, Spokeo, and similar services. Doxxers use these same sites. Removing yourself from them degrades both threat vectors simultaneously.

### The 10 Priority Broker Opt-Outs

**Highest priority** (confirmed to contain extensive data, used by law enforcement):

| Broker | Opt-Out URL | Est. Time |
|--------|------------|-----------|
| **LexisNexis** (highest priority — ICE contract confirmed) | https://optout.lexisnexis.com/ | 5 min |
| **BeenVerified** | https://www.beenverified.com/app/optout/search | 3 min |
| **Spokeo** | https://www.spokeo.com/optout | 3 min |
| **WhitePages** | https://www.whitepages.com/suppression-requests | 3 min |
| **Intelius** | https://www.intelius.com/opt-out/ | 3 min |
| **TruePeopleSearch** | https://www.truepeoplesearch.com/removal | 2 min |
| **FastPeopleSearch** | https://www.fastpeoplesearch.com/removal | 2 min |
| **FamilyTreeNow** | https://www.familytreenow.com/optout | 2 min |
| **Radaris** | https://radaris.com/page/how-to-remove | 3 min |
| **Acxiom** | https://isapps.acxiom.com/optout/optout.aspx | 3 min |

**Also submit** (federal/advertising opt-outs):
- https://www.optoutprescreen.com — remove from pre-screened credit/insurance offers
- https://optout.networkadvertising.org — online ad networks
- https://optout.aboutads.info — digital advertising

### Step-by-Step Process

1. **Open all 10 links in separate browser tabs** (or do them one at a time — your preference)
2. **For each site**:
   - Search for your full name OR your first name + last name + city
   - If your record appears, click the opt-out/removal link
   - Follow the site's instructions (some may ask you to upload ID, some may email a confirmation link, some immediate removal)
   - **If asked**: upload your driver's license (ID verification) — this is normal for them to verify you own the account
   - Confirm removal
3. **Save proof**: Screenshot or note down the confirmation message (in case you need to dispute later)

### Important Notes

- **Some sites require ID upload**: Be comfortable uploading a photo of your license to 1–2 sites (usually LexisNexis and BeenVerified). This is how they verify you actually own that data and have the right to remove it. They're required by privacy law to do this.
- **Some take 2–4 weeks**: Not everything removes instantly. Check back in 3 weeks.
- **Re-submission required**: These brokers re-scrape public records every 3–6 months and re-add your record. You'll need to re-submit every 90 days, or use an automated service (see Phase 2).

### Verification (2–4 weeks later)

After submission, wait 2–4 weeks, then:
1. Open a **private browser window** (Ctrl+Shift+P / Cmd+Shift+P)
2. Search for your name on BeenVerified.com and Spokeo.com
3. If your record still appears, re-submit
4. Once removed, you've degraded law enforcement's access to your contact information

---

## Step 1.7 — iPhone: Passcode-Only Lock Screen

**Time**: ~5 minutes  
**Platform**: iPhone  
**Cost**: Free  
**Threat addressed**: Law enforcement using Face ID/Touch ID to unlock phone without consent

### The Legal Principle

In most U.S. jurisdictions:
- **You CAN be compelled to unlock your phone with Face ID or Touch ID** by court order (not a Fifth Amendment violation — your biometric is you, not your thoughts)
- **You CANNOT be compelled to reveal your PIN** — this is your knowledge, protected under Fifth Amendment (your thoughts, your memory)
- A PIN you refuse to provide is more legally defensible than a face or finger law enforcement controls

### Steps

1. **Settings** → **"Face ID & Passcode"**
2. Enter your current passcode
3. **Scroll down** to the "Use Face ID For" section
4. Toggle **"iPhone Unlock"** to **OFF**
5. Face ID will still work for:
   - App authentication
   - Apple Pay
   - App Store purchases
   - ...but NOT for unlocking the home screen

### Optional: Make Your Passcode Stronger

1. In the same **Face ID & Passcode** settings
2. Tap **"Change Passcode"**
3. When asked "What type of passcode?", tap **"Passcode Options"** → **"Custom Alphanumeric Code"**
4. Create a password with letters + numbers (e.g., `M7x!Kp2n` instead of just `123456`)
5. Bitwarden will store it if you want to save it (you can also write it down)

### Emergency Disable (if needed)

If law enforcement or a threatening person is forcing you to unlock your phone:

1. **Press the side button + volume button simultaneously** for about 1 second
2. This triggers **Emergency SOS** and disables Face ID until you enter your passcode
3. Practice this gesture until it's muscle memory

### Note: iOS Automatic Reboot

iOS 18 has a built-in feature: your iPhone automatically reboots if it hasn't been unlocked for 72 hours. This puts the phone into **"Before First Unlock" (BFU)** state where forensic tools cannot extract data. This is enabled by default and is GOOD — you want it on.

---

## Quick Verification Checklist: Phase 1 Complete

After finishing 1.4–1.7, verify:

- [ ] Ente Auth installed on iPhone with at least Gmail + 1 financial account
- [ ] Bitwarden desktop app and iPhone app installed and synced
- [ ] Bitwarden contains all critical passwords (email, financial, social media)
- [ ] Data broker opt-outs submitted (at least LexisNexis, BeenVerified, Spokeo)
- [ ] iPhone Face ID disabled for lock screen (passcode only)
- [ ] Recovery codes for Ente Auth and Bitwarden saved in safe location
- [ ] Master password for Bitwarden written down and stored physically

**Status**: Once all of above are checked, Phase 1 is complete.

---

## Next: Phase 2 Planning

Phase 2 addresses:
- Always-on VPN (Mullvad)
- Hardware security key (Yubikey or Solokey)
- Linux security hardening
- Automated data broker re-submission
- Secure messaging for sensitive contacts

See `PHASE_2_PLANNING.md` for detailed roadmap.

