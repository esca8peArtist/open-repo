---
title: "Phase 2 Planning — Hardening and Advanced Protection"
project: cybersecurity-hardening
created: 2026-05-17
status: planning
depends-on: PHASE_1_NEXT_STEPS_GUIDE.md (Phase 1 complete)
---

# Phase 2: Hardening & Advanced Protection

**What Phase 1 accomplished**: You've now encrypted your laptop, locked down your email and financial accounts, disconnected your devices from tracking infrastructure, and removed yourself from public data brokers.

**What Phase 2 adds**: Always-on VPN to encrypt your internet traffic, hardware security keys to replace passwords entirely, automated data broker monitoring, and behavioral practices that become permanent habits.

**Timeline**: 2–3 weeks at 1–2 hours per week  
**Cost**: ~$70–150 total (VPN + security keys + misc. tools)  
**Payoff**: Near-total isolation from commercial tracking + law enforcement surveillance + third-party account takeover

---

## Phase 2 Modules

### 2.1 — Always-On VPN: Mullvad with Kill Switch

**Time to set up**: 1 hour (Windows + iPhone)  
**Ongoing time**: 0 (invisible after setup)  
**Cost**: ~$5/month (~$60/year)  
**Threat addressed**: ISP tracking, commercial location aggregation, law enforcement access to browsing history, DNS hijacking, corporate Man-in-the-Middle attacks

**Why Mullvad**:
- Headquartered in Sweden (outside U.S. legal process jurisdiction)
- No-log guarantee verified by Swedish police investigation (they tried to subpoena data, got nothing)
- Account is anonymous (16-digit number, no email, no password)
- Kill switch: if VPN connection drops, all traffic blocks until you reconnect (prevents accidentally leaking unencrypted traffic)
- Supports Tor connections (additional anonymity layer if needed)

**Payment anonymously**:
- Generate account number (no email)
- Mail physical cash to Mullvad office (instructions at https://mullvad.net/help/sending-cash/)
- OR buy a prepaid Visa/Mastercard with cash, use that

**Setup**:
1. Visit https://mullvad.net/en/download
2. Download Mullvad for Windows (or iPhone/Linux as needed)
3. Install and open app
4. Tap "Create account" — generates a 16-digit number instantly
5. Note: Your account is now created with that number
6. Scroll to "Settings" → enable "Lockdown mode" (kill switch)
7. Set "Connect on start-up" to ON
8. Tap "Connect"
9. Your internet traffic is now encrypted

**Verify it worked**: Go to https://www.whatismyip.com — your IP address will be a Mullvad server IP, not your ISP's IP. Your actual IP is now hidden.

**On iPhone**: Same process via the Mullvad app.

**Cost**: ~$5/month. Payment via cash mail, prepaid card (purchased with cash), or cryptocurrency accepted.

### 2.2 — Hardware Security Keys: Yubikey 5 NFC or Solokey 2

**Time to set up**: 1 hour (initial setup) + 15 min per account (ongoing, amortized)  
**Ongoing time**: 0 (invisible; you just tap/insert key when logging in)  
**Cost**: ~$50–70 per key (buy 2–3 physical keys for redundancy)  
**Threat addressed**: Phishing attacks, SIM swapping, account takeover via compromised credentials, law enforcement social engineering

**What a security key is**: A small USB or NFC device (looks like a USB drive or key fob) that proves you own an account without ever revealing a password or code to the website.

**Why it's better than TOTP (Ente Auth codes)**:
- TOTP codes (6-digit numbers) can be phished — you think you're typing into your real bank, but you're typing into a fake phishing site
- Security keys use cryptography that only works on legitimate domains — phishing sites cannot accept your key
- Impossible to remotely compromise (the key is a physical device in your hand)

**Recommended keys**:
- **Yubikey 5 NFC** (~$60): USB + NFC (tap to iPhone) + FIDO2/OTP support. Industry standard, trusted by FISA, DOD, most Fortune 500s.
- **Solokey 2** (~$50): Open source, same FIDO2 support, no NFC
- Buy 2–3 keys and register them on the same account so you have backup if one is lost

**Setup** (per key):
1. Plug Yubikey into USB port (or use NFC on iPhone)
2. Go to your account settings for Gmail, Bitwarden, bank, etc.
3. **Security** → **Security keys** → **Add security key**
4. Tap the Yubikey when prompted
5. It will register on that account
6. Repeat for each account

**Supported accounts** (as of 2026):
- Google (Gmail, YouTube, etc.)
- Microsoft (Outlook, OneDrive, etc.)
- GitHub
- Apple (iCloud)
- Bitwarden
- Most major banks (Chase, Fidelity, Wells Fargo, etc.)
- Financial brokerages (Interactive Brokers, Tastytrade, etc.)

**Timeline**: Week 1-2 of Phase 2. Gradually migrate accounts as you log in:
- When you log into Gmail, add the key
- When you log into your bank, add the key
- After 4–6 weeks, most accounts will have registered keys

**Why multiple keys**: If you lose your phone, you want a backup way to unlock your accounts. Register a security key on every account that's critical (email, banking, hosting).

### 2.3 — Automated Data Broker Monitoring & Re-Submission

**Time to set up**: 1 hour  
**Ongoing time**: 0 (automated)  
**Cost**: ~$90–120/year (optional; manual is free but tedious)  
**Threat addressed**: Recurring data broker re-scraping; law enforcement tracking data updates

**What happens**: Data brokers re-scrape public records (DMV, property records, court filings) every 3–6 months and re-add you. Manual opt-out is temporary.

**Solution**: Automated service monitors all brokers monthly and re-submits your opt-out request if they re-add your record.

**Services**:
- **DeleteMe** (~$140/year): Manages 200+ brokers, runs monthly, includes monitoring dashboard
- **Abine Blur Plus** (~$80/year): Includes email masking, password manager, VPN, plus data broker removal
- **OneRep** (~$120/year): 100+ brokers, monthly re-submission

**Verdict**: If you do manual opt-outs today (step 1.6), do them again in 90 days to verify. After that, automate with one of the services above.

### 2.4 — Linux Hardening & Encrypted Boot

**Applies to**: If you use Linux for sensitive work (e.g., storing domain keys, deploying infrastructure, handling GPG keys)

**Time to set up**: 2–3 hours (one-time, complex)  
**Cost**: Free  
**Threat addressed**: Physical device seizure; forensic extraction of unencrypted Linux partitions

**Core setup**:
1. **LUKS full-disk encryption** during Linux install (select "Encrypt this disk" during installation)
2. **GRUB bootloader password** to prevent cold-boot attacks
3. **SELinux** or **AppArmor** mandatory access control (sandboxing for each app)
4. **Automatic lock on idle** (15 min of inactivity locks screen)

**Tools**:
- **Ubuntu**: Built-in LUKS and AppArmor support
- **Fedora**: Built-in LUKS and SELinux support
- **Arch**: Requires manual LUKS setup (advanced users only)

**Defer this** if you're not comfortable with Linux sysadmin. It's valuable but complex. Start with Windows + iPhone hardening first.

### 2.5 — Secure Messaging for High-Risk Contacts

**Time to set up**: 15 minutes (ongoing 2–5 min per contact)  
**Cost**: Free  
**Threat addressed**: Law enforcement intercepting your communications; hostile nation-state surveillance

**Tools by threat level**:

| Threat Level | Tool | Setup | Notes |
|---|---|---|---|
| **Low** (general privacy, corporate tracking) | Signal (you already have this) | Already done (Phase 1) | End-to-end encryption, no metadata collection beyond last-seen time |
| **Medium** (government surveillance of specific conversation) | Signal group with disappearing messages | Settings > Privacy > Default timer for new chats = 1 week | Messages auto-delete after time window |
| **High** (activist/sensitive organizing) | Briar + offline mesh | Download Briar app; create account | Works without internet via Bluetooth mesh; excellent for hostile environments |

**What to do now**:
- Use Signal for day-to-day sensitive communication
- Create a separate Signal account for truly sensitive organizing (different phone number if possible)
- Disable "Show my name in contact info" in Signal settings
- Audit your Signal contact list — remove anyone you don't trust

**Defer**:
- Briar is high-friction (mesh networking requires multiple devices running Briar); implement only for high-risk scenarios
- Wire/ProtonMail are okay but less battle-tested than Signal for US-focused threats

### 2.6 — Email Forwarding & Alias Strategy

**Time to set up**: 1–2 hours  
**Cost**: Free (SimpleLogin) or ~$100/year (ProtonMail Plus)  
**Threat addressed**: Email address harvesting; correlation of your identity across services

**The problem**: Every signup gives a company another copy of your email address. Eventually, all your email addresses get linked by data brokers into a single identity. Using different email addresses for different accounts fragments that graph.

**Solution**: Email alias/forwarding service.

**Tools**:
- **SimpleLogin** (acquired by Proton; free tier: 15 aliases) — open source, free tier is excellent
- **Apple iCloud+ private email** (if you use Apple) — free with iCloud+ subscription
- **ProtonMail Plus** (~$100/year) — full email hosting with unlimited aliases

**Setup** (SimpleLogin example):
1. Visit https://app.simplelogin.io
2. Create account with your main email
3. Create new "alias" email addresses: `shopping+amazon@simplelogin.io`, `banking+chase@simplelogin.io`, etc.
4. When signing up for a service, use the alias specific to that service
5. All mail forwards to your real email
6. If that service is breached or sells your address, only that one alias is exposed

**Benefit**: If Amazon is breached and your email is sold, you see WHERE it came from. Then disable that alias.

**Defer if**: You're comfortable with your current email setup. This is a quality-of-life improvement, not critical security.

### 2.7 — Behavioral Practices: Becoming Invisible

**Time investment**: 5–10 min/day (habit formation, weeks 3–8)  
**Cost**: Free  
**Threat addressed**: Passive deanonymization through behavioral patterns

**Practices**:
1. **Check Mullvad IP before sensitive activity** (visiting activist websites, leaked document research, etc.)
   - If VPN is down, wait; don't browse unencrypted
2. **Use separate browser profiles**:
   - Profile 1: General browsing (Gmail, Facebook, shopping) — logged in
   - Profile 2: Sensitive research (news aggregators, archived.org, leaked docs, etc.) — logged out, VPN always on
   - Profile 3: Hidden/private (Tor via Mullvad if needed)
3. **Time-shift your behavior**:
   - Don't always check Signal at 8am and email at 5pm
   - Vary your times to prevent traffic analysis
4. **Avoid mixing identities**:
   - Don't talk about your activist organizing on your personal Facebook account
   - Keep personal social media completely disconnected from any organizing activity
5. **Practice OPSEC for physical meetings**:
   - Check if you're being followed (counter-surveillance)
   - Meet in public places with multiple exits
   - Use pseudonyms for event signup if possible

**This becomes automatic after a few weeks.**

---

## Phase 2 Timeline

Suggested approach (2–3 weeks):

| Week | Task | Time | Cost |
|------|------|------|------|
| 1 | 2.1: Mullvad VPN setup | 1 hr | $5/mo |
| 1 | 2.2: Order security keys (Yubikey x2) | 10 min | $120 |
| 1–2 | 2.2: Register keys on email, banking, hosting | 2 hrs | — |
| 2 | 2.3: Data broker automated service signup OR manual recheck | 1 hr | $90–120/yr |
| 2–3 | 2.5: Signal backup account + settings audit | 20 min | — |
| 3 | 2.6: SimpleLogin alias setup | 1 hr | Free |
| Ongoing | 2.7: Behavioral practices | 10 min/day | — |

**Total**: 6–8 hours over 2–3 weeks  
**Total cost**: $200–300 (VPN + keys + optional automation)

---

## Phase 3: Permanent Behavioral Integration

Phase 3 is not a step-by-step guide. It's the practices that become automatic.

After Phase 1 and Phase 2, you've built:
- ✅ Encrypted storage (Windows BitLocker + iPhone + Mullvad VPN)
- ✅ Encrypted communications (Signal + HTTPS)
- ✅ Password security (Bitwarden + hardware keys)
- ✅ Data broker isolation (opt-outs + aliases)

**Phase 3 = maintaining these as reflexes**:
- Always check that Mullvad is connected before opening your browser
- Always use different aliases for new accounts
- Never reuse passwords (Bitwarden auto-fills)
- Default to Signal for sensitive conversations
- Time-shift your behavior to avoid patterns

These become muscle memory within 3–4 weeks. After that, security is invisible.

---

## Decision Points

### Should you move to Phase 2 immediately after Phase 1?

**Yes, if**: You've verified Phase 1 is working (Ente Auth logs you in, Bitwarden auto-fills, data broker opt-outs confirmed).

**Wait, if**: You want to stabilize Phase 1 first (live with it for 2–3 weeks, get comfortable, then add Phase 2).

### Which Phase 2 modules are most critical?

**Tier 1 (do first)**:
- 2.1 Mullvad VPN (most impactful: hides all your internet traffic)
- 2.2 Hardware security keys (replaces password risk entirely)

**Tier 2 (do second)**:
- 2.3 Automated data broker monitoring
- 2.5 Signal backup account

**Tier 3 (do last)**:
- 2.4 Linux hardening (only if you use Linux)
- 2.6 Email aliases (convenience + identity fragmentation)

### What if you don't have time for Phase 2?

Phase 1 alone is a massive upgrade. You've now got:
- Encrypted laptop, encrypted iPhone backups, encrypted email
- Two-factor authentication on critical accounts
- Removed yourself from public data brokers
- Switched from SMS to authenticator for account recovery

**You're in the 85th percentile of security without Phase 2.** Phase 2 pushes you to 98th percentile.

---

## Contingency: If You're Arrested

Having a security plan is good. But **know what to do if law enforcement confronts you**:

1. **Say nothing except your name and "I want a lawyer"**
   - Do not explain your security setup
   - Do not claim innocence
   - This is not admission; it's Fifth Amendment protection
2. **They cannot force you to unlock a device with your PIN** (Fifth Amendment protection)
   - They CAN force Face ID/Touch ID (not a Fifth Amendment violation)
   - They CANNOT force you to reveal your passphrase
3. **With Bitwarden master password protected**: They cannot access your accounts even if they unlock your phone
4. **With hardware keys**: They cannot access your accounts even if they have your password
5. **Request a lawyer immediately** — you are not required to answer questions

---

## Quarterly Security Audit (Phase 3)

Every 3 months, spend 15 minutes on:
- [ ] Check if data broker opt-outs are still valid (search yourself on Spokeo/BeenVerified)
- [ ] Update passwords in Bitwarden for any sites with known breaches (check https://haveibeenpwned.com)
- [ ] Verify Signal/Ente Auth/Bitwarden are still installed and updated
- [ ] Confirm Mullvad is running and no kill-switch warnings

This becomes routine very quickly.

