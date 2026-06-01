---
title: "Phase 6 Platform Implementation Guide — Option A: Discourse (Bootstrap Path)"
project: systems-resilience
phase: 6
option: A
score: "8.0/10"
status: READY — pending June 3 decision
created: 2026-06-02
decision_deadline: 2026-06-03
operational_target: 2026-06-05 00:00 UTC
cost_annual: "$60–$300/yr (VPS + optional Loomio)"
cross_references:
  - PHASE_6_PLATFORM_ANALYSIS_v2.md
  - PHASE_6_DECISION_SUPPORT_CHECKLIST.md
---

# Option A: Discourse — Bootstrap Path Implementation Guide

**Score**: 32/40 (8.0/10) | **Annual cost**: $60–$300 | **Setup time**: 6–8 hours | **Technical requirement**: Docker familiarity

---

## 1. Pre-Implementation Checklist

Complete all items before running any installation commands. Gaps here cause delays that eat into the June 5 deadline.

**Domain and DNS**
- [ ] Domain name registered or subdomain carved out (e.g., `community.yourdomain.org` or a fresh `resilience-hub.org`). Namecheap or Cloudflare Registrar are both $10–15/year.
- [ ] Access to DNS control panel for that domain. You will need to create one A record pointing to your VPS IP.
- [ ] Allow 1–24 hours for DNS propagation. This is the longest uncontrollable delay in the process. Set the DNS record the moment you have a VPS IP — do not wait until installation is complete.

**VPS / Hosting**
- [ ] Account at Hetzner Cloud (recommended: CPX21, 3 vCPU / 4 GB RAM / 80 GB SSD, ~$7/month), DigitalOcean (Droplet, $12/month), or Vultr ($10/month). Hetzner is cheapest and well-suited for the workload.
- [ ] VPS running Ubuntu 22.04 LTS (required by official Discourse install script).
- [ ] SSH access confirmed: `ssh root@<VPS_IP>` succeeds.
- [ ] Port 80 and 443 open in VPS firewall (or security group).

**Email (Required — Discourse Will Not Install Without a Configured Mail Provider)**
- [ ] Transactional email provider configured. Options:
  - **Mailgun** (free tier: 100 emails/day, adequate for a small community): create account, verify domain, obtain SMTP credentials.
  - **Gmail SMTP** with an App Password (works; limited to 500 emails/day; suitable if community stays under 100 members). Not recommended long-term due to Google policy changes.
  - **Brevo (formerly Sendinblue)** free tier: 300 emails/day — adequate, no credit card required.
- [ ] You will need four values: `SMTP_ADDRESS`, `SMTP_PORT`, `SMTP_USER_NAME`, `SMTP_PASSWORD`.
- [ ] Dedicated `noreply@yourdomain.org` email address configured at your mail provider.

**GitHub OAuth (Strongly Recommended for Community UX)**
- [ ] GitHub account with admin access to a GitHub Organization, or a personal account is sufficient.
- [ ] Create a GitHub OAuth App at `https://github.com/settings/developers` → "New OAuth App". Set callback URL to `https://your-discourse-domain.org/auth/github/callback`. Note the Client ID and Client Secret.

**Credentials to Have Ready**
- VPS root password or SSH private key
- DNS panel login
- SMTP credentials (all four values)
- GitHub OAuth Client ID + Secret
- Your admin email address (will be the Discourse admin account)

---

## 2. Step-by-Step Installation

### Step 1 — Provision VPS (15 minutes)

Create a Hetzner CPX21 instance with Ubuntu 22.04. Note the public IP immediately and set your DNS A record before doing anything else.

```bash
# From your local machine — confirm SSH works
ssh root@<YOUR_VPS_IP>
```

### Step 2 — Server Preparation (10 minutes)

```bash
# Update the system
apt update && apt upgrade -y

# Install Docker (official Discourse requirement)
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Git (needed for Discourse launcher)
apt install -y git
```

### Step 3 — Clone Discourse and Configure (30 minutes)

```bash
# Clone the official Discourse Docker launcher
mkdir -p /var/discourse
git clone https://github.com/discourse/discourse_docker.git /var/discourse
cd /var/discourse

# Copy the sample config
cp samples/standalone.yml containers/app.yml
```

Edit `containers/app.yml` with your values. The critical fields:

```yaml
# Hostname — must match your DNS A record exactly
DISCOURSE_HOSTNAME: 'community.yourdomain.org'

# Admin credentials
DISCOURSE_DEVELOPER_EMAILS: 'you@yourdomain.org'

# SMTP (example using Mailgun)
DISCOURSE_SMTP_ADDRESS: smtp.mailgun.org
DISCOURSE_SMTP_PORT: 587
DISCOURSE_SMTP_USER_NAME: postmaster@mg.yourdomain.org
DISCOURSE_SMTP_PASSWORD: 'your-mailgun-api-password'
DISCOURSE_SMTP_ENABLE_START_TLS: true

# GitHub OAuth (add after the SMTP block)
DISCOURSE_GITHUB_CLIENT_ID: 'your-client-id'
DISCOURSE_GITHUB_CLIENT_SECRET: 'your-client-secret'
```

### Step 4 — Bootstrap and Launch Discourse (60–90 minutes, mostly automated)

```bash
cd /var/discourse
./launcher bootstrap app
./launcher start app
```

The bootstrap step downloads all images and compiles assets. It runs unattended. When it finishes, Discourse is live at your configured hostname. Navigate there and complete the web-based setup wizard: site name, logo, first category.

### Step 5 — SSL/TLS (Automatic via Let's Encrypt)

The official Discourse Docker configuration automatically provisions a Let's Encrypt certificate when:
- DNS propagation is complete (your A record resolves to the VPS IP)
- Port 80 is accessible from the internet

No manual certificate steps are needed. If SSL fails, verify DNS with `dig +short your-domain.org` before investigating further.

### Step 6 — Initial Configuration (60 minutes)

Navigate to Admin → Settings and configure:

**Trust Levels (critical for self-governing community)**
- `min_trust_level_to_post_links: 1` (TL1 basic — earned automatically after reading; prevents link spam from new joiners)
- `invite_only: true` (community is invite-gated, not public)
- `must_approve_users: false` (invites self-approve; no admin bottleneck)
- `email_editable: true`

**Categories to create**
1. "Knowledge Base" — restricted to TL1+; wiki posts enabled (Phase 5 documents go here)
2. "Discussion" — open to all TL0+ (new members can participate)
3. "Events" — for community coordination posts (install Events plugin below)
4. "Meta" — for platform feedback and governance

**Moderation: Akismet Anti-Spam**
- Admin → Plugins → Akismet. Requires a WordPress.com Akismet API key (free for personal use at `akismet.com/signup`). Enter the API key in Admin → Settings → Spam.

**Events Plugin Installation**
Add to `containers/app.yml` in the `hooks.after_code.commands` block:

```yaml
- git clone https://github.com/paviliondev/discourse-events.git /var/www/discourse/plugins/discourse-events
```

Then rebuild: `./launcher rebuild app` (15–20 minutes). After rebuild, the Events plugin appears in Admin → Plugins. Enable it. Events are then created from the "+ New Event" button in any category.

**GitHub OAuth Activation**
- Admin → Settings → Login → Enable "Allow GitHub login"
- Test by logging out and using the "Sign in with GitHub" button.

---

## 3. Integration With Existing Systems

**GitHub Pages**
Discourse provides a JavaScript embed widget. Add this snippet to any GitHub Pages HTML page to show recent forum discussions inline:

```html
<div id="discourse-comments"></div>
<script type="text/javascript">
  DiscourseEmbed = {
    discourseUrl: 'https://community.yourdomain.org/',
    topicId: 42  // the Discourse topic ID you want to embed
  };
  (function() {
    var d = document.createElement('script');
    d.type = 'text/javascript'; d.async = true;
    d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(d);
  })();
</script>
```

Replace `topicId` with the ID of the relevant knowledge base topic. This makes the Phase 5 publication site interactive without moving community members off GitHub Pages.

**Email**
Discourse handles all community email natively via SMTP. Members receive digests, mention notifications, and DM alerts automatically. No additional configuration after SMTP setup.

**Loomio Governance Supplement**
In the Discourse "Meta" category, pin a post titled "Governance Decisions" with a direct link to the community's Loomio group. Members use Discourse for discussion and click through to Loomio for formal votes. No technical integration needed; a pinned link is sufficient.

---

## 4. Timeline and Effort Estimate

| Date | Action | Time Required | Prerequisite |
|---|---|---|---|
| June 3 (decision day) | VPS provisioned, SSH confirmed | 20 min | Decision made |
| June 3 | DNS A record set | 5 min | VPS IP known |
| June 3 | SMTP credentials obtained (Mailgun or Brevo) | 20 min | Email provider account |
| June 3 | GitHub OAuth app created | 10 min | GitHub account |
| June 3–4 | DNS propagation window | 1–24 hr | A record set |
| June 4 | `app.yml` configured and `launcher bootstrap` run | 90 min (mostly automated) | DNS resolving |
| June 4 | Admin wizard, categories, trust levels, Akismet | 60 min | Bootstrap complete |
| June 4 | Events plugin installed and rebuilt | 30 min + 20 min rebuild | Initial install complete |
| June 4–5 | GitHub OAuth tested; invite link generated | 20 min | All settings confirmed |
| June 5 (target) | Phase 5 documents posted as wiki posts; pinned onboarding thread | 90 min | Platform operational |

**Critical path**: DNS propagation is the only uncontrollable delay. Set the A record at the same moment you create the VPS, even before installation starts.

**Total active effort**: approximately 6–7 hours across June 3–5.

---

## 5. Post-Launch Validation

Run these checks before inviting the first community member.

**Infrastructure**
- [ ] `https://community.yourdomain.org` loads with a valid green padlock (TLS active)
- [ ] Admin account accessible; admin panel visible at `/admin`
- [ ] Send a test email: Admin → Email → Test (sends to admin address; confirm delivery)

**Access Control**
- [ ] Create a test account via invite link; verify it lands in TL0 with rate limits active (cannot post links)
- [ ] Promote test account to TL1 manually; verify link posting is now allowed
- [ ] GitHub OAuth login: sign out, click "Sign in with GitHub", confirm account creation

**Content**
- [ ] Post one wiki post in Knowledge Base category; verify it shows "Edit" to TL2+ users
- [ ] Create one test Event; verify it appears in Events category with RSVP option

**Email**
- [ ] Test account receives welcome email within 5 minutes of creation
- [ ] Reply-to-topic via email works (if desired — requires SMTP reception config; optional)

**Success criteria**: A new invitee can register via GitHub OAuth, read the knowledge base, see the upcoming event, and receive their welcome email — all within 10 minutes of accepting an invite.

---

## 6. Rollback and Migration Path

**If you need to switch away from Discourse before June 5:**

Discourse stores all data in PostgreSQL, accessible inside the Docker container. A full data export is available at Admin → Backups → "Create New Backup". This produces a `.tar.gz` containing the full database and uploaded files.

Content migration to Option B (Mighty Networks): paste content manually; no automated import. Estimated 2–4 hours for the Phase 5 document set.

Content migration to Option C (Nextcloud + Matrix): Discourse topic content can be exported as JSON via the API (`GET /t/{topic_id}.json`) and reformatted for Nextcloud file upload. Matrix rooms replace Discourse categories. Estimated 3–5 hours.

**If the VPS needs to be decommissioned**: Download the Admin Backup, delete the VPS. DNS A record can be removed or pointed elsewhere. Total cost to walk away: one month of VPS (approximately $7–12).

**Minimum viable rollback time**: 2 hours to spin down and export data; 4–6 hours to rebuild content on an alternative platform.
