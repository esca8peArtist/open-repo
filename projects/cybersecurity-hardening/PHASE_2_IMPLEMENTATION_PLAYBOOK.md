---
title: "Phase 2 Implementation Playbook — Hardening & Advanced Protection"
project: cybersecurity-hardening
phase: 2
status: "production-ready playbook — ready for Phase 1 completion"
created: 2026-05-19
session: 1329
depends-on: "Phase 1 completion (VeraCrypt encryption, Ente Auth, Bitwarden, data broker opt-outs)"
timeline: "2–3 weeks at 1–2 hours/week"
total-cost: "$200–300 (VPN + security keys + optional automation)"
---

# Phase 2: Implementation Playbook — Hardening & Advanced Protection

**Purpose**: Step-by-step execution guide for Phase 2 (modules 2.1–2.7). Assumes Phase 1 is complete.

**What Phase 1 achieved**: Encrypted laptop, protected email/financial accounts, disconnected from tracking infrastructure, data broker opt-outs complete.

**What Phase 2 adds**: Always-on VPN encryption, hardware security keys (passwordless login), automated data broker monitoring, behavioral isolation practices.

**Outcome after Phase 2**: Near-total isolation from commercial tracking, law enforcement surveillance, and third-party account takeover.

---

## Part 1: Module Prioritization & Timeline

### Priority Ranking

| Module | Priority | Reason | Time | Cost |
|--------|----------|--------|------|------|
| **2.1: Mullvad VPN** | TIER 1 | Encrypts ALL internet traffic; blocks ISP + corporate tracking | 1 hour | $5/mo |
| **2.2: Hardware Security Keys** | TIER 1 | Eliminates password-based account takeover risk; replaces SMS 2FA | 2 hours + 15 min/account | $120+ (2–3 keys) |
| **2.3: Data Broker Automation** | TIER 2 | Continuous monitoring + auto-removal of personal data | 1 hour | $90–120/yr (optional) |
| **2.5: Signal Backup Account** | TIER 2 | Compartmentalized communication for sensitive organizing | 20 min | Free |
| **2.4: Linux Hardening** | TIER 3 | Kernel hardening, SELinux/AppArmor. Only if you use Linux | 2–3 hours | Free |
| **2.6: Email Aliases** | TIER 3 | Identity fragmentation across services; prevents email correlation | 1 hour | Free (SimpleLogin) or $100/yr (ProtonMail Plus) |
| **2.7: Behavioral Practices** | TIER 3 | Time-shifting, browser profiles, counter-surveillance | 10 min/day ongoing | Free |

### Suggested 3-Week Execution Schedule

| Week | Task | Hours | Cumulative | Notes |
|------|------|-------|-----------|-------|
| **Week 1** | 2.1: Mullvad VPN setup (Windows + iPhone) | 1 | 1 hr | Start here; enables everything else |
| Week 1 | 2.2: Order security keys (Yubikey x2–3) | 0.25 | 1.25 hr | Order early; delivery takes 3–5 days |
| Week 1 | 2.2: Register keys on email + banking (initial setup) | 1 | 2.25 hr | As keys arrive, register progressively |
| **Week 2** | 2.2: Register keys on remaining accounts (ongoing) | 1.5 | 3.75 hr | Migrate accounts as you log in |
| Week 2 | 2.3: Data broker automation OR manual recheck | 1 | 4.75 hr | Either subscribe to monitoring service or manually re-verify |
| Week 2 | 2.5: Signal backup account + settings audit | 0.5 | 5.25 hr | Separate account for organizing comms |
| **Week 3** | 2.6: Email alias setup (SimpleLogin or ProtonMail) | 1 | 6.25 hr | Fragment identity across services |
| Week 3+ | 2.7: Behavioral practices | 10 min/day | Ongoing | Becomes automatic within 3–4 weeks |

**Total: 6–8 hours over 3 weeks; $200–300 one-time cost.**

---

## Part 2: Module Implementation — Step-by-Step

### Module 2.1: Always-On VPN (Mullvad) — Week 1

**Goal**: Encrypt all internet traffic. Hides IP from ISP, corporate networks, law enforcement (requires court + Mullvad cooperation, which they don't give).

**Time**: 1 hour (Windows + iPhone)  
**Cost**: ~$5/month  
**Threat model**: ISP tracking, corporate MITM, DNS hijacking, law enforcement passive surveillance

#### Setup: Windows

1. **Visit https://mullvad.net/en/download**
2. **Download Mullvad for Windows** (64-bit or 32-bit; if unsure, use 64-bit)
3. **Install**:
   - Run the installer
   - Accept license
   - Choose install location (default is fine: `C:\Program Files\Mullvad VPN\`)
   - Finish
4. **Launch Mullvad** (desktop icon or Start menu > Mullvad)
5. **Create account**:
   - Click "Create account"
   - Note the 16-digit account number (e.g., `1234567890123456`)
   - Save this number somewhere safe (you need it to log back in from other devices)
6. **Enable Kill Switch**:
   - Click Settings (gear icon)
   - Scroll to "Lockdown Mode"
   - Toggle **ON** (turns red when active)
   - This blocks ALL internet if VPN drops (prevents accidental unencrypted traffic)
7. **Enable Auto-Connect**:
   - Settings > General
   - Toggle "Connect on start-up" to **ON**
8. **Connect**:
   - Click the large "Connect" button
   - Status changes to "Connected" with a green checkmark
9. **Verify**:
   - Open browser (Firefox, Chrome, Edge)
   - Go to https://www.whatismyip.com
   - Your IP should show a Mullvad server IP (e.g., `193.x.x.x` in Sweden), NOT your ISP's IP
   - If it shows your ISP IP, Mullvad didn't connect; try again

#### Setup: iPhone

1. **Open App Store**
2. **Search: "Mullvad VPN"** (by Mullvad VPN AB)
3. **Install**
4. **Open app**
5. **Tap "Create account"**
   - Note the 16-digit number (same as Windows if you want to use the same account; use a different number for separate iPhone account)
6. **Enable Lockdown Mode**:
   - Settings (gear icon bottom-right)
   - "Lockdown Mode" → toggle **ON**
7. **Connect**:
   - Tap the main "Connect" button
   - Status shows "Connected" with a lock icon
8. **Verify**:
   - Open Safari
   - Go to https://www.whatismyip.com
   - Should show Mullvad IP, not your cellular IP

#### Payment Options (Choose One)

**Option A: Monthly subscription via Mullvad account** (simplest):
- Open Mullvad app → Account → click your account number
- Opens Mullvad website with your account
- Click "Add funds"
- Pay via cryptocurrency (Bitcoin, Monero) or bank transfer
- Cost: ~$5/month (~$60/year)

**Option B: Cash by mail** (most anonymous):
- Visit https://mullvad.net/help/sending-cash/
- Follow instructions to mail physical cash to Mullvad office
- Enclose account number on a note
- Mullvad credits your account

**Option C: Prepaid card** (cash → card → Mullvad):
- Buy a prepaid Visa/Mastercard with cash at grocery store
- Use prepaid card number in Mullvad app to add funds

**Success criteria**:
- [ ] Mullvad app installed on Windows + iPhone
- [ ] Both devices show "Connected" status
- [ ] whatismyip.com shows Mullvad IP (not your real IP)
- [ ] Lockdown mode is ON (kill switch active)
- [ ] Auto-connect is ON on both devices

---

### Module 2.2: Hardware Security Keys (Yubikey) — Week 1–2

**Goal**: Replace passwords + SMS 2FA with cryptographic keys. Impossible to phish or remotely compromise.

**Time**: 2 hours initial + 15 min per account (amortized)  
**Cost**: $50–70 per key × 2–3 keys = $120–210 total  
**Threat model**: Phishing attacks, SIM swapping, credential stuffing, account takeover via breached passwords

#### Why Hardware Security Keys?

| Defense | SMS 2FA | TOTP (Ente Auth) | Hardware Security Key |
|---------|---------|------------------|----------------------|
| **Phishing vulnerability** | ❌ High (attacker intercepts SMS) | ❌ Medium (codes can be phished) | ✅ Immune (key works ONLY on legitimate domain) |
| **SIM swap vulnerability** | ❌ Vulnerable (attacker redirects SMS) | ✅ Safe (codes stored locally, not carrier) | ✅ Safe (key is physical device) |
| **Remote compromise** | ❌ Yes (SIM swap, carrier breach) | ✅ No (TOTP is local) | ✅ No (key is offline hardware) |
| **Convenience** | ⭐⭐⭐ (automatic) | ⭐⭐ (type 6 digits) | ⭐⭐⭐ (tap/insert key) |

#### Which Keys to Buy?

**Option A: Yubikey 5 NFC** (~$60 each) — RECOMMENDED
- Industry standard (used by FISA, DOD, Fortune 500s)
- USB + NFC (tap on iPhone/Android)
- FIDO2 + OTP + PIV support
- Firmware updates available
- **Recommended**: Buy 2–3 keys for redundancy

**Option B: Solokey 2** (~$50 each)
- Open source (auditable code)
- FIDO2 support
- No NFC (USB only)
- **Recommended**: Also buy 2–3

**Buy from**: Amazon, Best Buy, Yubico.com, Solokeys.com  
**Delivery time**: 3–5 days

#### Setup: Register Keys on Each Account

**Week 1–2 goal**: Register 2–3 keys on email, banking, hosting, and other critical accounts.

**Generic setup process** (works for most services):

1. **Go to account settings** (Gmail, Chase, GitHub, etc.)
2. **Find Security → Security keys** (or "Two-factor authentication" → "Security keys")
3. **Click "Add security key"**
4. **Device prompt appears**:
   - If USB key: Insert Yubikey into USB port and touch it
   - If NFC key on phone: Hold iPhone to key (or tap key to phone if key has NFC)
5. **Key registers**; you're done for that account
6. **Register 2–3 keys per account** (so you have backup if one is lost)

#### Accounts to Prioritize (in order)

| Account Type | Service Examples | Priority | Time |
|---|---|---|---|
| Email | Gmail, Outlook, Yahoo | Tier 1 (CRITICAL) | 15 min |
| Banking | Chase, Fidelity, Wells Fargo, etc. | Tier 1 (CRITICAL) | 20 min |
| Password manager | Bitwarden | Tier 1 (CRITICAL) | 10 min |
| Cloud hosting | GitHub, AWS, Google Drive, Dropbox | Tier 1 | 15 min |
| Financial brokers | Interactive Brokers, Tastytrade, etc. | Tier 1 | 15 min |
| Social media | Facebook, LinkedIn (if used) | Tier 2 | 10 min each |
| Work accounts | Slack, company email, Jira, etc. | Tier 2 | 10 min each |
| Other accounts | Apple, Microsoft, etc. | Tier 2 | 10 min each |

#### Timeline: Progressive Migration

**Week 1**: Order keys
**Week 1–2**: As keys arrive, register on 3–4 critical accounts:
- When you next log into Gmail → add key
- When you next log into bank → add key
- When you next log into Bitwarden → add key
- When you next log into GitHub/AWS → add key

**By Week 3**: 5–8 accounts have keys registered  
**By Week 4–6**: Most daily-use accounts have keys (happens naturally as you log in)

#### Backup & Redundancy Strategy

**Why redundancy matters**: If you lose or break a key, you can still log in via registered backup keys.

**Recommended approach**:
1. **Register 3 keys** on each critical account (email, banking, Bitwarden)
2. **Physical storage**:
   - Key 1: On your keychain (daily use)
   - Key 2: Home safe / desk drawer (backup)
   - Key 3: Different location (parent's house, office, bank safe deposit) or with trusted person
3. **If key is lost**: Log in via backup key, revoke lost key, order replacement

#### Logistical Checklist

- [ ] Order 3 × Yubikey 5 NFC (or equivalent)
- [ ] Keep order confirmation + delivery tracking
- [ ] As each key arrives, test on a non-critical account first (e.g., Facebook)
- [ ] Register keys on critical accounts:
  - [ ] Email (Gmail, Outlook, Yahoo)
  - [ ] Banking (Chase, Fidelity, etc.)
  - [ ] Password manager (Bitwarden)
  - [ ] Cloud/hosting (GitHub, AWS, Google Drive)
  - [ ] Financial brokers (Tastytrade, Interactive Brokers)
- [ ] Test that backup keys work (log out, log in via different key)
- [ ] Store backup keys in safe locations
- [ ] Add "Yubikey registration" reminder in Bitwarden for each account you use

#### Success Criteria

- [ ] 2–3 keys ordered and in hand
- [ ] Keys registered on email, banking, password manager, and 1–2 other critical accounts
- [ ] Tried logging into each account with different keys (verified redundancy works)
- [ ] Backup keys stored in secure location

---

### Module 2.3: Data Broker Automation — Week 2

**Goal**: Continuously monitor + automatically remove your personal data from broker databases.

**Time**: 1 hour (setup) + 10 min/month (monitoring)  
**Cost**: $90–120/year (optional; manual opt-outs are free but time-consuming)  
**Threat model**: Data aggregators selling your identity to marketers, law enforcement, bounty hunters

#### Two Paths

**Path A: Paid automation service** (~$100/year)
- Services: Incogni, DeleteMe, PrivacyDuck
- What they do: Continuously submit data removal requests to 200+ brokers; monitor if data reappears
- Pros: Hands-off; covers brokers you don't know about
- Cons: Paid; slightly invasive (you're giving them your personal data to remove; choose trusted provider)

**Path B: Manual rechecking** (Free but time-consuming)
- You manually re-verify each broker you already opted out of (Session 1332) using:
  - https://backgroundchecks.org/
  - https://www.peoplesearch.com/
  - https://www.whitepages.com/
  - https://www.intelius.com/
- Do this every 3–6 months
- Cost: Free, but ~30 minutes every quarter

#### If You Choose Path A: Setup Incogni (Example)

1. **Visit https://www.incogni.com/**
2. **Sign up** (email, password, name, address)
3. **Choose plan**:
   - Annual plan: ~$100/year (best value)
   - Monthly: ~$15/month
4. **Authorize**:
   - Incogni needs your personal data to submit removal requests
   - Review privacy policy; decide if you trust them
5. **Select brokers to target** (pre-selected list of 200+)
6. **Confirm and pay**
7. **Monitor**:
   - Incogni sends reports on removal progress
   - Monitor dashboard for reappearances

#### If You Choose Path B: Manual Recheck (Free)

**Every 3 months, check**:
1. https://backgroundchecks.org/ (search yourself)
2. https://www.spokeo.com/ (search yourself)
3. https://www.intelius.com/ (search yourself)
4. https://www.whitepages.com/ (search yourself)

**If your info reappears**:
- Go back to that broker's opt-out form
- Re-submit removal request
- Note the date in Bitwarden or calendar as reminder to recheck in 3 months

#### Phase 1 Refresh (Optional)

From Phase 1, you already opted out of ~10 major brokers manually. You can re-verify they stayed removed:
- [ ] Recheck data-removal confirmations from Phase 1
- [ ] If any say "removal expires," re-submit
- [ ] Document in a Bitwarden note: "Data broker status check — [date] — all clear"

#### Success Criteria

- [ ] **Path A chosen**: Incogni (or equivalent) account set up, monthly reports arriving
- [ ] **Path B chosen**: Quarterly calendar reminder set; initial recheck completed
- [ ] Data broker opt-out status confirmed for 5–10 major brokers

---

### Module 2.5: Signal Backup Account — Week 2

**Goal**: Compartmentalized encrypted messaging. Separate account for organizing/sensitive comms.

**Time**: 20 minutes  
**Cost**: Free  
**Threat model**: Metadata analysis, correlation of identity across communications

#### Why a Backup Account?

Signal encrypts messages (good), but metadata (who messages whom, when) is not encrypted. Creating a separate account for sensitive organizing prevents metadata linking your organizing activity to your personal social networks.

#### Setup: Second Signal Account

1. **Phone number** (you need a second one):
   - Option A: Use a separate phone line (cost: $10–20/month)
   - Option B: Use a Google Voice number (free)
   - Option C: Use a temporary phone service (Twilio, etc.; cost: varies)

2. **Creating with Google Voice**:
   - Go to https://voice.google.com
   - Sign in with your Gmail
   - Click "Create" (if first time) or look for phone setup
   - Choose a local area code
   - Google assigns you a free phone number (e.g., `+1-555-XXX-XXXX`)
   - This number can send SMS and receive calls (though you'll receive via Google Voice app)

3. **Installing Signal on a second device** (optional):
   - If you only have one phone, you can use the same device (Signal handles multiple accounts via phone number)
   - Go to Settings > apps > Signal > Data > clear Signal data (only if you want to fully reset)
   - Or: use a second phone if you have one

4. **Creating Signal account with Google Voice number**:
   - Open Signal on second phone (or same phone after clearing data)
   - Choose "Register with phone number"
   - Enter Google Voice number (e.g., `+1-555-XXX-XXXX`)
   - Verify via SMS (Signal sends code to Google Voice)
   - Create account

5. **Settings Hardening**:
   - Settings > Privacy
   - "Show my name in contact info" → toggle **OFF** (people see only your number)
   - "Phone number discovery" → toggle **OFF** (your number won't appear in others' discovery)
   - "Default timer for new chats" → set to **1 week** (messages auto-delete after 7 days)

6. **Share carefully**:
   - Give this number ONLY to people you trust for sensitive comms
   - Keep it completely separate from personal contacts
   - Do not link it to your personal Signal account

#### Structural Separation

| Account | Purpose | Contacts | Privacy Level |
|---------|---------|----------|---------------|
| **Personal Signal** (main phone number) | Family, friends, colleagues | 50–200 people | Standard |
| **Organizing Signal** (Google Voice number) | Activism, sensitive organizing, protests | 5–20 people (trusted) | High isolation, auto-delete |

#### Settings Checklist (Organizing Account)

- [ ] Phone number: Google Voice (separate from personal)
- [ ] "Show my name in contact info" → OFF
- [ ] "Phone number discovery" → OFF
- [ ] "Default timer for new chats" → 1 week
- [ ] Only share this number with people you trust for sensitive comms
- [ ] Do NOT add this number to personal contacts (use "Unknown" or pseudonym in organizing group)

#### Success Criteria

- [ ] Second Signal account created with separate phone number (Google Voice or equivalent)
- [ ] Auto-delete set to 1 week
- [ ] Privacy settings hardened (name/discovery disabled)
- [ ] Shared only with small trusted group

---

### Module 2.4: Linux Hardening — Week 3 (Optional — Skip if No Linux)

**Goal**: Kernel hardening, SELinux/AppArmor enforcement, secure boot.

**Time**: 2–3 hours  
**Cost**: Free  
**Threat model**: Local privilege escalation, kernel exploits, malware persistence via boot

**Skip this module if**:
- You only use Windows and iPhone
- You're not a developer/sysadmin
- You don't run a Linux server

**If you do use Linux** (Ubuntu/Fedora desktop or server):

#### Quick Setup: AppArmor (Ubuntu)

1. **Check if AppArmor is installed**:
   ```bash
   sudo systemctl status apparmor
   ```
   - If "active (running)" → already enabled, skip to step 3
   - If "inactive" → enable it: `sudo systemctl enable apparmor && sudo systemctl start apparmor`

2. **Enable strict mode for common apps**:
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.bin.firefox
   sudo aa-enforce /etc/apparmor.d/usr.bin.thunderbird
   ```

3. **Verify**:
   ```bash
   sudo aa-status
   ```
   - Should show 20+ loaded profiles in "enforce" mode

#### Fedora: SELinux Hardening

1. **Check SELinux status**:
   ```bash
   getenforce
   ```
   - If "Enforcing" → already enabled, you're done
   - If "Permissive" or "Disabled":
     ```bash
     sudo semanage permissive -d domain_t  # (adjust as needed)
     ```

2. **Boot hardening** (both Ubuntu + Fedora):
   ```bash
   sudo grub-mkconfig -o /boot/grub/grub.cfg
   ```
   (This enables GRUB password if configured)

#### Kernel Parameters Hardening

Edit `/etc/sysctl.conf` and add:
```
# Disable kexec (prevents rootkit persistence)
kernel.kexec_load_disabled = 1

# Restrict access to kernel logs
kernel.printk = 3 3 3 3

# Disable YAMA (optional, more restrictive)
kernel.yama.ptrace_scope = 3
```

**Then apply**:
```bash
sudo sysctl -p
```

#### Success Criteria (if Linux user)

- [ ] AppArmor or SELinux is in "enforce" mode
- [ ] Common apps (Firefox, Thunderbird) have AppArmor profiles enabled
- [ ] Kernel hardening parameters applied (`kernel.kexec_load_disabled = 1`, etc.)
- [ ] Verified after reboot that protections are still active

---

### Module 2.6: Email Alias Strategy — Week 3

**Goal**: Fragment identity across services. Use different email address per account to prevent correlation.

**Time**: 1 hour  
**Cost**: Free (SimpleLogin) or $100/year (ProtonMail Plus)  
**Threat model**: Email harvesting, identity correlation by data brokers, account enumeration attacks

#### Path A: SimpleLogin (Free + Open Source) — RECOMMENDED

1. **Visit https://app.simplelogin.io**
2. **Create account**:
   - Email: your main email (Gmail, etc.)
   - Password: strong (use Bitwarden to generate)
   - Verify: check email, click verification link
3. **Create your first alias**:
   - Dashboard > "+ New alias"
   - Alias name: `shopping+amazon` (or similar)
   - Full alias: `shopping+amazon@simplelogin.io`
   - Description: "Amazon account"
   - Recipient: your main email
4. **Use this alias when signing up**:
   - When signing up for Amazon, use `shopping+amazon@simplelogin.io` as email
   - All emails forward to your real email
   - If Amazon is breached, only that one alias is exposed

#### Alias Naming Strategy

Use format: `[service]+[category]@simplelogin.io`

| Service | Alias | Purpose |
|---------|-------|---------|
| Amazon | `shopping+amazon@simplelogin.io` | E-commerce |
| Chase | `banking+chase@simplelogin.io` | Finance |
| Spotify | `media+spotify@simplelogin.io` | Subscriptions |
| GitHub | `dev+github@simplelogin.io` | Dev services |
| Google | `social+google@simplelogin.io` | Social/Search |

#### Path B: ProtonMail Plus ($100/year) — Alternative

- Full email hosting (not just aliases)
- Includes unlimited aliases
- More privacy-forward than SimpleLogin (Swiss jurisdiction, encryption focus)
- Setup: Buy ProtonMail Plus, enable catch-all domain if self-hosted

#### Gradual Migration Strategy

**Don't migrate everything overnight.** Instead:

1. **Create 5–10 aliases for main services** (banking, email, social):
   - `banking+chase@simplelogin.io`
   - `banking+fidelity@simplelogin.io`
   - `social+google@simplelogin.io`
   - `social+facebook@simplelogin.io`
   - `shopping+amazon@simplelogin.io`

2. **Use aliases going forward**:
   - New signups → use appropriate alias
   - Existing accounts → leave as-is (migrating email on 50 accounts is tedious)

3. **After 6 months**: Review. Most active accounts will naturally have aliases. Old dormant accounts can stay on your main email.

#### SimpleLogin Checklist

- [ ] SimpleLogin account created
- [ ] 5–10 aliases created (banking, shopping, social, dev, subscriptions)
- [ ] Main email added as recipient for all aliases
- [ ] Test: sign up for a test account (e.g., Reddit) using alias, verify email arrives
- [ ] Disable alias: if a service is breached, disable its alias from SimpleLogin dashboard

#### Success Criteria

- [ ] SimpleLogin (or ProtonMail Plus) account active
- [ ] 5–10 aliases created for common services
- [ ] Next signup will use appropriate alias

---

### Module 2.7: Behavioral Practices — Week 3+

**Goal**: Automated practices that prevent passive deanonymization through behavioral patterns.

**Time**: 10 min/day (becomes automatic within 3–4 weeks)  
**Cost**: Free  
**Threat model**: Traffic analysis, timing correlation, behavioral profiling

#### Practice 1: Check VPN Before Sensitive Activity

**Reflex**: Before visiting activist websites, news sites, leaked document archives, or research on sensitive topics, **check that Mullvad is connected**.

**How**:
- Click Mullvad system tray icon (or app)
- Verify "Connected" status
- If not connected, click Connect and wait 5 seconds
- Then open browser

**Why**: If your VPN disconnects mid-session (network glitch, app crash), you want to catch it before accidentally leaking your real IP.

#### Practice 2: Separate Browser Profiles

**Setup** (Chrome/Firefox):

- **Profile 1: Personal** (logged in to personal accounts)
  - Gmail, Facebook, YouTube, personal shopping
  - Can be logged in to personal identity

- **Profile 2: Research/Sensitive** (completely logged out)
  - No personal accounts logged in
  - Always use Mullvad + Tor via Mullvad if researching highly sensitive topics
  - For: news aggregators, archived.org, leaked documents, activist research

- **Profile 3: Hidden/Private** (optional, very high isolation)
  - Use Firefox "Private Window" (Ctrl+Shift+P on Windows, Cmd+Shift+P on Mac)
  - Mullvad always on
  - Tor via Mullvad
  - For: rare cases of highest sensitivity

**Implementation**:
- Chrome: Settings > Manage other people > Add person > name "Research" → use that profile when doing sensitive work
- Firefox: Multiple profiles via about:profiles

#### Practice 3: Time-Shift Your Behavior

**The threat**: If you always check Signal at 8am and email at 5pm, traffic analysis can correlate your devices across networks by identifying the pattern.

**The practice**:
- Check Signal at 8:15am one day, 7:45am the next, 8:30am another
- Check email at 5:10pm, 4:55pm, 5:25pm (vary the time)
- After 2–3 weeks, these variations become automatic

**Why**: Random jitter defeats traffic timing correlation. ISP/network observer can see "device talks to Signal API, then email API" but can't confidently correlate your devices if the timing varies.

#### Practice 4: Avoid Mixing Identities

**Red line**: Never discuss organizing/activism on your personal social media (Facebook, Instagram, LinkedIn).

**Compartmentalization**:
- Personal Facebook: family, friends, casual interests
- Organizing: Signal organizing account + encrypted messaging
- Public activism (if applicable): separate account/pseudonym
- No overlap

**Why**: Data brokers + law enforcement correlate your identities. If your Facebook profile mentions you work in IT, and your organizing research correlates to IT-competent people, that's a linkage.

#### Practice 5: Physical OPSEC (if organizing)

**If you're attending organizing meetings or protests**:
1. **Check for surveillance**: Walk a loop; see if anyone follows
2. **Meet in public spaces** with multiple exits
3. **Use pseudonyms** for event signup if possible
4. **Don't bring personal devices** to very sensitive meetings (or leave phone at home)
5. **Pay cash** for parking/transportation (not card)

**Resources**:
- Tactical Tech's "Security in-a-Box" (tacticaltech.org)
- EFF's Surveillance Self-Defense (ssd.eff.org)

#### Practice Checklist

- [ ] Mullvad status check before sensitive browsing (automatic within 2 weeks)
- [ ] Separate browser profiles set up (Personal / Research / Hidden)
- [ ] Time-shift behavior in place (vary Signal check time, email check time, etc.)
- [ ] No activism discussion on personal social media
- [ ] Physical OPSEC practiced if attending meetings/protests

---

## Part 3: Success Criteria & Verification

### By End of Week 1

- [ ] Mullvad VPN installed and connected on Windows + iPhone
- [ ] whatismyip.com shows Mullvad IP (not your real IP)
- [ ] Kill switch enabled (Lockdown Mode on both devices)
- [ ] Auto-connect enabled
- [ ] Security keys ordered (3 × Yubikey or equivalent)

### By End of Week 2

- [ ] Security keys received and registered on:
  - [ ] Email (Gmail, Outlook, or equivalent)
  - [ ] Banking (Chase, Fidelity, etc.)
  - [ ] Password manager (Bitwarden)
- [ ] 2–3 backup keys stored in safe locations
- [ ] Data broker automation OR manual recheck scheduled
- [ ] Signal backup account created with Google Voice number
  - [ ] Auto-delete set to 1 week
  - [ ] Privacy settings hardened

### By End of Week 3

- [ ] Email aliases created (SimpleLogin or ProtonMail) — at least 5 aliases
- [ ] Browser profiles set up (Personal / Research / Hidden)
- [ ] Behavioral practices started:
  - [ ] Check Mullvad before sensitive browsing
  - [ ] Time-shift Signal/email check times
  - [ ] No activism on personal social media

### Ongoing (Weeks 4–8)

- [ ] Behavioral practices become automatic
- [ ] Security keys gradually registered on remaining accounts (as you log in)
- [ ] Data broker status monitored (monthly if automated, quarterly if manual)
- [ ] Mullvad connection verified daily before sensitive work

---

## Part 4: Troubleshooting

### "Mullvad won't connect"
- Check internet connection (open non-VPN browser, verify you can reach any website)
- Restart Mullvad app
- If still broken, restart device
- If persistent, check Mullvad forums (mullvad.net/forum)

### "Security key not recognized"
- Ensure key is a supported protocol (FIDO2)
- Try a different USB port
- Try key on a different device to isolate the problem
- For NFC: ensure NFC is enabled on iPhone (Settings > NFC)

### "SimpleLogin alias not receiving email"
- Check spam folder (mark as "Not spam")
- Verify alias recipient email is correct (SimpleLogin dashboard > alias > check recipient)
- Manually forward test email: send email to alias, verify it arrives at recipient email
- If still broken, check SimpleLogin status page for outages

### "Signal backup account won't verify"
- Ensure Google Voice number is active and can receive SMS
- Try requesting SMS again (wait 60 seconds between attempts)
- If SMS fails, try Signal's "Call me instead" option
- Verify you can access Google Voice dashboard (voice.google.com)

---

## Part 5: Cost Summary

| Item | Cost | One-Time or Recurring |
|------|------|----------------------|
| Mullvad VPN | $60/year (~$5/month) | Recurring |
| Yubikey 5 NFC × 3 | $180–210 | One-time |
| Data broker automation (Incogni or equivalent) | $100/year | Recurring (optional) |
| SimpleLogin | Free | One-time (optional; free tier) |
| **Total (recommended)** | ~$340/year | — |
| **Total (minimal)** | ~$60/year | Mullvad only |

---

## Part 6: Phase 3: Permanent Integration

After Phase 2 is complete, Phase 3 is not a checklist — it's reflexive behavior.

**What becomes automatic**:
- Always check Mullvad before sensitive browsing
- Always use different aliases for new accounts
- Never reuse passwords (Bitwarden auto-fills)
- Default to organizing Signal for sensitive comms
- Time-shift behavior (vary check times)

**Timeline**: 3–4 weeks of Phase 2 usage, then these become muscle memory. You'll do them without thinking.

---

## Document History

| Version | Date | Session | Changes |
|---------|------|---------|---------|
| 1.0 | 2026-05-19 | 1329 | Initial creation: 7-module playbook, 3-week timeline, all setup steps |

