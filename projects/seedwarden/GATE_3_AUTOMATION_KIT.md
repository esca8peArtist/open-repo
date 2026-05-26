---
title: "Gate 3 Automation Kit — Kit Email + DNS CNAME Setup"
created: 2026-05-26
status: ready-for-may-27-execution
purpose: >
  Self-contained execution kit for Gate 3 critical path.
  No orchestrator help needed during session. All steps copy-paste ready.
  DNS CNAME must start May 27 13:00 UTC. Hard deadline May 28 17:00 UTC.
references:
  - GATE_3_KIT_PREBUILD_BRIEF.md (full decisions doc)
  - MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md (phase-by-phase checklist)
  - TRACK_B_EMAIL_SEQUENCES.md (copy-paste email bodies)
  - GATE_3_VERIFICATION_SCRIPT.sh (automated pass/fail checks)
---

# Gate 3 Automation Kit

**Hard start**: May 27 13:00 UTC (DNS propagation requires 48-72 hours minimum)
**DNS hard deadline**: May 28 17:00 UTC (DNS entry must be submitted by this time for May 30 propagation)
**Launch deadline**: May 30 10:00 UTC

This document is self-contained. Open it, follow it top to bottom, and Gate 3 is done.

---

## Timeline Constraints

| Milestone | Time (UTC) | Why it cannot move |
|---|---|---|
| Gate 3 start | May 27 13:00 | Kit SPF/DKIM records need 48+ hr propagation before May 30 |
| DNS CNAME submitted | May 28 17:00 | 48-72 hr propagation puts resolution at May 30 17:00-May 31 17:00 — submit earlier to have buffer |
| Email automation published | May 27 23:59 | Automation must be PUBLISHED (not Draft) to allow SPF warmup |
| 3-test protocol | May 28 09:00 | Run after Email 1 has propagated at least 8 hours |
| Go/No-Go decision | May 29 21:00 UTC | Final checkpoint before launch day |
| Launch | May 30 10:00 UTC | All gates must be COMPLETE |

**DNS is the longest lead item.** Every hour of delay past May 28 17:00 UTC carries risk that DNS is still propagating when launch traffic hits the landing page on May 30.

---

## Part 1: Kit Email Automation Setup

### Step 1 — Create Kit Account (15 minutes)

Open kit.co in an incognito browser window.

```
Account configuration (paste into each field):
  Email:        wanka95@gmail.com
  Sender name:  Seedwarden
  Sender email: wanka95@gmail.com
  Time zone:    Your local time zone
  Plan:         FREE (do not pay)
  Business type: Creator
```

After signing up, Kit sends a verification email to wanka95@gmail.com. Click the confirmation link before doing anything else. Dashboard must load before proceeding to Step 2.

### Step 2 — Create All 15 Tags (5 minutes)

Navigate to: Kit > Subscribers > Tags > "Create a tag"

Create tags in this exact order. Names are case-sensitive. No spaces. No capitals.

**Zone tags (8) — create these first:**

```
zone-3
zone-4
zone-5
zone-6
zone-7
zone-8
zone-9
zone-10
```

**Interest cohort tags (7) — create immediately after:**

```
seed-saver
forager
food-preserver
homesteader
medicinal-herbs
vip-buyer
phase-1-buyer
```

Verification: Kit > Subscribers > Tags should show exactly 15 entries. Take a screenshot.

### Step 3 — Build Landing Page (25 minutes)

Navigate to: Kit > Landing Pages > Create > select "Minimal" or "Simple" template.

Paste all fields exactly as shown below. Do not rephrase.

**Headline:**
```
Your Free Zone Quick-Start Card
```

**Subheadline:**
```
Know exactly what to plant, when to plant it, and what to do right now in your zone — one-page reference card, free.
```

**Form fields (add in this order):**
1. First Name — required
2. Email — required
3. Growing Zone — required, type: Dropdown

Dropdown options for Growing Zone (add all 8, in order):
```
Zone 3
Zone 4
Zone 5
Zone 6
Zone 7
Zone 8
Zone 9
Zone 10
```

**CTA button text:**
```
Send My Zone Card
```

**Trust text (add below button, smaller/gray font):**
```
No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing, foraging, and real food.
```

**Background color:** white or `#F5EDD6` (Warm Cream). Use white if template requires custom CSS for hex input.

Click Publish. Copy the landing page URL and paste it here before closing:

```
Landing page URL: _______________________________
```

Test in incognito: page loads, zone dropdown shows 8 options, form submits without errors.

### Step 4 — Build Email Sequence (60-90 minutes)

**Prerequisite:** Zone card PDFs must already be uploaded to Google Drive with tested download links before this step. Each Email 1 variant requires the Google Drive URL for that zone.

Google Drive link format (use download format, NOT viewer format):
```
CORRECT:   https://drive.google.com/uc?export=download&id=[FILE_ID]
INCORRECT: https://drive.google.com/file/d/[FILE_ID]/view
```

Test each link in incognito before pasting into Kit. It must trigger an immediate PDF download.

Navigate to: Kit > Automations > Create New Automation
- Name: `Seedwarden Welcome`
- Trigger: "When subscriber joins via landing page"

**Email 1 — Build 8 zone variants (build Zone 5 first)**

Build order: Zone 5 → Zone 6 → Zone 7 → Zone 8 → Zone 3 → Zone 4 → Zone 9 → Zone 10

For each variant, change only these three things:
- Subject line zone number
- Zone card Google Drive URL
- One mention of zone number in the opening paragraph

Subject line template (change only the zone number):
```
Your Zone [X] Quick-Start Card is here
```

CTA button: "Download Your Zone Card"
CTA URL format:
```
https://drive.google.com/uc?export=download&id=[ZONE_X_FILE_ID]?utm_source=kit&utm_medium=email&utm_campaign=welcome_seq&utm_content=email1_cta
```

Body copy: paste from `TRACK_B_EMAIL_SEQUENCES.md` Email 1 section.

CRITICAL FIX before saving each Email 1 variant: search the body for any date in parentheses (e.g., "May 20 (tomorrow)"). Delete the entire parenthetical. Keep only the surrounding sentence.

After building all 8 Email 1 variants, add conditional routing:
```
If subscriber has tag zone-3 → send Email 1 Zone 3 variant
If subscriber has tag zone-4 → send Email 1 Zone 4 variant
[repeat for all 8 zones]
```

**Emails 2-5 — Single version, paste from TRACK_B_EMAIL_SEQUENCES.md**

| Email | Source section | Delay setting | Critical fix |
|---|---|---|---|
| Email 2 | Email 2 section | 2 days after Email 1 | None |
| Email 3 | Email 3 section | 3 days after Email 2 | None |
| Email 4 | Email 4 section | 2 days after Email 3 | None |
| Email 5 | Email 5 section | 3 days after Email 4 | Remove "May 20 (tomorrow)" — replace with just the surrounding sentence without the parenthetical |

**Set automation status to Published** (not Draft, not Test). This is required for the sequence to send automatically. If Kit shows a toggle or status field, it must read "Active" or "Published" before you close the browser.

### Step 5 — Connect Landing Page to Automation (5 minutes)

Navigate to: Kit > Landing Pages > [your landing page] > Settings
- Connect to automation: select "Seedwarden Welcome"
- Confirm: when a subscriber joins via landing page, the zone selection applies the corresponding zone-X tag, which triggers the correct Email 1 variant

### Step 6 — 5-Email Sequencing Validation

Verify the sequence is wired correctly before running tests:

| Check | Expected | Verified |
|---|---|---|
| Email 1 trigger | Immediately on subscribe | |
| Email 2 delay | 2 days after Email 1 | |
| Email 3 delay | 3 days after Email 2 (Day 5) | |
| Email 4 delay | 2 days after Email 3 (Day 7) | |
| Email 5 delay | 3 days after Email 4 (Day 10) | |
| Automation status | Published / Active | |
| Landing page connection | Linked to "Seedwarden Welcome" | |
| Zone tag routing | 8 conditional rules present | |
| Total tags in system | 15 | |

---

## Part 2: DNS CNAME Entry Configuration

**Hard deadline: May 28 17:00 UTC**

This section covers adding the Kit SPF/DKIM CNAME records at your domain registrar. These records allow Kit to send email on behalf of a custom domain. Even if you are using wanka95@gmail.com as the sender for now, Kit still creates SPF/DKIM records when you create an account — and those records need 48-72 hours to propagate before they affect deliverability.

### Step 1 — Find Your CNAME Records in Kit

After creating your Kit account:
1. Kit > Settings > Email Sending
2. Look for "Custom Domain" or "Email Authentication" section
3. Kit shows 2-3 DNS records to add (SPF TXT record and one or two CNAME records)
4. Copy all of them — you need the exact "Name" (host) and "Value" (target) for each

If Kit does not prompt you for DNS records during setup, check: Kit > Settings > Domains

### Step 2 — Add Records at Your Domain Registrar

The steps below work for all major registrars (Namecheap, GoDaddy, Google Domains, Cloudflare, Hover, etc.). The UI labels differ slightly but the fields are the same.

**For each record Kit gives you:**

1. Log in to your domain registrar (wherever you bought your domain)
2. Navigate to DNS settings:
   - Namecheap: Domain List > Manage > Advanced DNS
   - GoDaddy: My Products > DNS > Manage
   - Cloudflare: Dashboard > your domain > DNS
   - Google Domains: DNS > Resource records
3. Click "Add record" or "Add new record"
4. Set record type to **CNAME** (or TXT for SPF record)
5. Fill in the fields:

```
Type:  CNAME (or TXT — match what Kit specifies)
Name:  [exactly what Kit shows in the "Name" or "Host" column]
Value: [exactly what Kit shows in the "Value" or "Target" column]
TTL:   3600 (or "Automatic" if that is the only option)
```

6. Save. Repeat for each record Kit lists.

**Screenshot guidance:** Before saving each record, take a screenshot showing the filled-in Name and Value fields. This is your proof of configuration if anything needs debugging later.

**Common registrar-specific notes:**
- Namecheap: The "Host" field should not include your domain name — Namecheap appends it automatically. If Kit shows `em.seedwarden.com`, enter only `em` in the Host field.
- GoDaddy: Same as Namecheap — enter only the subdomain portion in "Host."
- Cloudflare: Make sure "Proxy status" for CNAME records is set to **DNS only** (gray cloud icon), not proxied (orange). Kit authentication breaks if proxied.
- Google Domains: Use the "Custom records" section, not the built-in email records section.

### Step 3 — Verify Records Are Saved

After adding all records:
1. Return to Kit > Settings > Email Authentication / Domains
2. Kit shows a verification status for each record
3. Click "Verify" or "Check records" — Kit will attempt to look up the records
4. Status may show "Pending" for up to 72 hours while DNS propagates — this is normal

**Do not wait for Kit to confirm before moving on.** Submit the records and proceed. DNS propagation is passive — it happens in the background.

---

## Part 3: Verification Checklist

Run this checklist in order on May 28, at least 8 hours after completing Parts 1 and 2.

For automated verification, run `GATE_3_VERIFICATION_SCRIPT.sh` (in the same directory as this file). The script checks CNAME propagation, zone card PDF links, and email tag existence via API.

### Email Automation Verification

- [ ] Kit account dashboard loads at kit.co with wanka95@gmail.com
- [ ] Subscribers > Tags shows exactly 15 tags
- [ ] Landing page is live and reachable at the URL recorded in Step 3
- [ ] Automation "Seedwarden Welcome" shows status: Published (not Draft)
- [ ] Email 1 has 8 zone variants visible in the automation editor
- [ ] Each Email 1 variant has a conditional rule (if tag = zone-X, send this variant)
- [ ] Email 5 does not contain "May 20 (tomorrow)" or any stale date parenthetical
- [ ] Delay settings: Email 2 = 2d, Email 3 = 3d, Email 4 = 2d, Email 5 = 3d

### 3-Test Protocol

**Test 1 — Zone 5 delivery:**
1. Open landing page in incognito browser
2. Fill form: First Name = "Test", Email = `wanka95+test1@gmail.com`, Zone = Zone 5
3. Click "Send My Zone Card"
4. Check `wanka95+test1@gmail.com` inbox
5. PASS criteria: Email 1 arrives within 60 seconds, subject line says "Zone 5", PDF link downloads immediately without "Request access" error

**Test 2 — Zone 8 delivery:**
1. Open landing page in new incognito session
2. Fill form: First Name = "Test2", Email = `wanka95+test2@gmail.com`, Zone = Zone 8
3. Click "Send My Zone Card"
4. Check `wanka95+test2@gmail.com` inbox
5. PASS criteria: Email 1 arrives with Zone 8 subject line and Zone 8 PDF link

**Test 3 — Delay validation:**
1. Wait exactly 1 minute after Test 2 form submit
2. Check `wanka95+test2@gmail.com` inbox again
3. PASS criteria: ONLY Email 1 is present. Email 2 must NOT have arrived.
4. If Email 2 has arrived: the delay is broken. Go to Kit > Automations > edit Email 2 delay setting. Must be 2 days, not 0 or Immediately.

Record test results:
```
Test 1: [ ] PASS  [ ] FAIL
Test 2: [ ] PASS  [ ] FAIL
Test 3: [ ] PASS  [ ] FAIL
```

### DNS Verification

Run the verification script or check manually:
```bash
# Check if Kit CNAME record is propagated
nslookup [your-cname-name].[yourdomain.com]

# Expected output: a response pointing to Kit's servers (not NXDOMAIN)
# NXDOMAIN means the record has not propagated yet — wait and try again
```

Replace `[your-cname-name].[yourdomain.com]` with the Name/Host value from Kit's DNS settings.

DNS propagation can take 24-72 hours. If the record is not resolving by May 29 18:00 UTC, run the verification script and check the error output for registrar-specific guidance.

### Zone Card PDF Link Verification

For each zone, verify the Google Drive link downloads the correct PDF:
```
Zone 3: https://drive.google.com/uc?export=download&id=[FILE_ID_3]
Zone 4: https://drive.google.com/uc?export=download&id=[FILE_ID_4]
Zone 5: https://drive.google.com/uc?export=download&id=[FILE_ID_5]
Zone 6: https://drive.google.com/uc?export=download&id=[FILE_ID_6]
Zone 7: https://drive.google.com/uc?export=download&id=[FILE_ID_7]
Zone 8: https://drive.google.com/uc?export=download&id=[FILE_ID_8]
Zone 9: https://drive.google.com/uc?export=download&id=[FILE_ID_9]
Zone 10: https://drive.google.com/uc?export=download&id=[FILE_ID_10]
```

Each link must trigger an immediate PDF download in an incognito browser. "Request access" error means the sharing setting on that file is not set to "Anyone with the link can view."

---

## Gate 3 Go/No-Go Criteria

Gate 3 is COMPLETE when all of the following are true:

- [ ] Kit account created and email verified
- [ ] All 15 tags created (8 zone + 7 interest)
- [ ] Landing page published and accessible via public URL
- [ ] All 5 emails built (Email 1 with 8 zone variants, Emails 2-5 single version)
- [ ] Automation status: Published (not Draft)
- [ ] All 3 tests PASS
- [ ] DNS CNAME records submitted at registrar by May 28 17:00 UTC
- [ ] Social bios updated with landing page URL (Instagram, TikTok, Pinterest)

**If all items checked:** Gate 3 is COMPLETE. Proceed to May 29 pre-launch audit.

**If any item is unchecked after May 28 23:59 UTC:** Log the specific blocker in WORKLOG.md and assess the contingency path in SEEDWARDEN_TRACK_B_GATES_RUNBOOK.md Contingency D or E.

---

## Post-Gate 3 Social Bio Update (2 minutes)

Immediately after Gate 3 is complete, add the Kit landing page URL to all three social bios. This is required for the lead magnet to activate on launch day.

```
Instagram: Edit Profile > Bio link > paste landing page URL
TikTok:    Edit Profile > Website > paste landing page URL
Pinterest: Settings > Public Profile > Website > paste landing page URL
```

---

*Created: 2026-05-26. Gate 3 execution window: May 27-28, 2026.*
*DNS hard deadline: May 28 17:00 UTC. Launch: May 30 10:00 UTC.*
*Verification script: GATE_3_VERIFICATION_SCRIPT.sh (same directory).*
