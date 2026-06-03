---
title: "Discourse Deployment Playbook"
project: systems-resilience
phase: 5
platform: "Path B — Discourse Self-Hosted (Secondary Option)"
confidence: 8.0/10
status: READY-TO-EXECUTE — 3-4 hour deployment if Path A is not chosen
deployment_window: "3–4 hours (June 5, 06:00–10:00 UTC)"
target_users: 30–50 concurrent authors
offline_capable: false
cost_annual: "$84–$204 (Hetzner VPS + email + domain)"
created: 2026-06-03
version: 2.0
extends: PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
cross_references:
  - PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
  - PHASE_6_PLATFORM_ANALYSIS.md
tradeoffs:
  advantage: "Fastest deployment (3-4h vs 6-8h); best community governance UX; GitHub Actions integration"
  limitation: "No offline mode; requires VPS ($7-10/month); external dependency"
---

# Discourse Deployment Playbook
## Path B: Production-Ready Copy-Paste Deployment Guide
### Target: June 5, 2026 — Phase 5 Wave 1 Author Recruitment

---

## Preface: When to Use This Playbook

Use this playbook if:
- Path A (Nextcloud+Matrix) fails to deploy on June 5 by 12:00 UTC
- User explicitly selects Discourse as the Phase 5 platform
- A simpler, browser-based author experience is prioritized over offline capability

**Key facts**:
- Discourse deploys in 3–4 hours (versus 6–8 for Nextcloud+Matrix)
- No offline document editing (browser-only; PWA caching for reading only)
- Requires a $7–10/month VPS (cannot run well on raspby1 alongside stockbot)
- Trust-level auto-governance is Discourse's strongest feature
- GitHub Actions integration enables automated publication announcements

**Decision gate**: If choosing Path B, DNS must be configured by June 4 (24h propagation required for Let's Encrypt). See Part 1, Section 1.2.

---

## Part 1: Pre-Deployment Checklist

Complete all items by June 4, 23:59 UTC.

### 1.1 VPS Provisioning

**Recommended: Hetzner Cloud CPX21** (~$7/month)
- 3 vCPU, 4 GB RAM, 80 GB NVMe SSD
- Ubuntu 22.04 LTS (Discourse requirement; do not use Ubuntu 24.04 LTS)
- Sign up at https://www.hetzner.com/cloud
- Create project → Add Server → CPX21 → Ubuntu 22.04 → SSH key (add your public key)
- Note the IPv4 address immediately

**Alternatives** (if Hetzner is not available):
- DigitalOcean Basic Droplet: $12/month, 2 GB RAM (minimum; Discourse recommends 2 GB+)
- Vultr Cloud Compute: $12/month, similar spec

**Post-provisioning verification**:
```bash
# Test SSH access (should work within 60 seconds of VPS creation)
ssh root@<VPS_IP>

# Confirm OS
lsb_release -a
# Must show: Ubuntu 22.04.x LTS

# Confirm disk
df -h /
# Must show 60+ GB available (80 GB SSD minus OS)

# Confirm RAM
free -h
# Must show 4+ GB total
```

### 1.2 Domain and DNS (CRITICAL — Do First, Allow 24h Propagation)

**Register a domain**:
- Namecheap: ~$10/year for `.org`
- Cloudflare Registrar: ~$8.50/year (also manages DNS, recommended)
- Google Domains (now Squarespace): ~$12/year

**Recommended domain**: `resilience-hub.org` or `community.resilience-hub.org`

**DNS Configuration** (after registering):
```
Type: A
Name: @  (or "community" for subdomain)
Value: <VPS_IP>
TTL: 300 (5 minutes)
```

**Test propagation**:
```bash
# Run from any machine — should resolve to VPS IP
nslookup resilience-hub.org 8.8.8.8
# or
dig resilience-hub.org +short

# Let's Encrypt will fail if DNS is not propagated
# Wait until nslookup returns the VPS IP before proceeding to Part 2
```

### 1.3 Email / SMTP

**Required: Discourse will refuse to start without valid SMTP credentials.**

**Mailgun** (recommended for small communities):
1. Create account at https://www.mailgun.com/
2. Add your domain under "Sending" → "Domains" → "Add a sending domain"
3. Add the DNS records Mailgun provides (2 TXT records, 1 CNAME)
4. Go to "Sending" → "Domain settings" → "SMTP credentials"
5. Copy SMTP hostname, port (587), username, and password

**Brevo** (alternative, 300 emails/day free):
1. Sign up at https://app.brevo.com/
2. Settings → SMTP & API → SMTP tab
3. Copy SMTP server, port, login, password

**Credentials needed**:
```
SMTP_ADDRESS=smtp.mailgun.org
SMTP_PORT=587
SMTP_USER_NAME=postmaster@mg.resilience-hub.org
SMTP_PASSWORD=<your-mailgun-password>
DISCOURSE_DEVELOPER_EMAILS=admin@youremail.com
```

### 1.4 GitHub Configuration (for OAuth + GitHub Actions)

**GitHub OAuth App** (enables "Login with GitHub" button):
1. Go to https://github.com/settings/developers → "OAuth Apps" → "New OAuth App"
2. Application name: `Resilience Hub`
3. Homepage URL: `https://resilience-hub.org`
4. Authorization callback URL: `https://resilience-hub.org/auth/github/callback`
5. Register application
6. Note the **Client ID** and generate a **Client Secret**

**GitHub Personal Access Token** (for GitHub Actions automation):
1. Go to https://github.com/settings/tokens → "Generate new token (classic)"
2. Note: `repo`, `workflow` scopes
3. Generate and copy token — store in `.env` or GitHub Secrets

---

## Part 2: Step-by-Step Deployment

**Total time: 3–4 hours** (including DNS wait time if done same-day).

### Step 1: VPS Initial Setup (15 min — 06:00–06:15 UTC)

```bash
ssh root@<VPS_IP>

# System update
apt update && apt upgrade -y

# Install Docker (Discourse official installer requires Docker; not docker-compose)
curl -fsSL https://get.docker.com | bash

# Verify Docker
docker --version
# Expected: Docker version 24.x.x or higher

# Install git
apt install -y git curl

# Create discourse user with Docker access
adduser --disabled-password --gecos "" discourse
usermod -aG docker discourse

# Create SSH directory for discourse user
mkdir -p /home/discourse/.ssh
cp ~/.ssh/authorized_keys /home/discourse/.ssh/ 2>/dev/null || true
chown -R discourse:discourse /home/discourse/.ssh
chmod 700 /home/discourse/.ssh

# Switch to discourse user for installation
su - discourse
```

### Step 2: Install Discourse Official Launcher (45 min — 06:15–07:00 UTC)

```bash
# As discourse user

# Clone official Discourse Docker
git clone https://github.com/discourse/discourse_docker.git ~/discourse
cd ~/discourse

# Create containers directory (needed by launcher)
mkdir -p containers

# Copy the standalone app template
cp samples/standalone.yml containers/app.yml
```

**Edit `containers/app.yml`** (this is the key configuration file):

```bash
# Open for editing
nano containers/app.yml
```

Required changes in `app.yml`:

```yaml
# ── Core Settings ──────────────────────────────────────────────────────────
env:
  DISCOURSE_HOSTNAME: 'resilience-hub.org'  # Your domain
  DISCOURSE_DEVELOPER_EMAILS: 'admin@youremail.com'

  # SMTP settings
  DISCOURSE_SMTP_ADDRESS: smtp.mailgun.org
  DISCOURSE_SMTP_PORT: 587
  DISCOURSE_SMTP_USER_NAME: 'postmaster@mg.resilience-hub.org'
  DISCOURSE_SMTP_PASSWORD: 'REPLACE_WITH_SMTP_PASSWORD'
  DISCOURSE_SMTP_ENABLE_START_TLS: true
  DISCOURSE_SMTP_AUTHENTICATION: login

  # Let's Encrypt
  LETSENCRYPT_ACCOUNT_EMAIL: 'admin@youremail.com'

  # Performance tuning for small VPS (4 GB RAM)
  UNICORN_WORKERS: 2
  DISCOURSE_DB_POOL: 5

# ── Volumes ────────────────────────────────────────────────────────────────
volumes:
  - volume:
      host: /var/discourse/shared/standalone
      guest: /shared
  - volume:
      host: /var/discourse/shared/standalone/log/var-log
      guest: /var/log
```

**Validate the configuration**:
```bash
./launcher check app
# Should print no errors
```

**Bootstrap (takes 20–40 minutes)**:
```bash
./launcher bootstrap app
# This builds the Discourse Docker image — takes 20-40 min
# Expected final line: "Successfully bootstrapped, to start use ./launcher start app"
```

**Start Discourse**:
```bash
./launcher start app
# Wait 60 seconds, then verify:
docker ps | grep discourse_app
# Should show: Up About a minute
```

### Step 3: Service Verification (20 min — 07:00–07:20 UTC)

```bash
# Test HTTP/HTTPS from VPS itself
curl -I http://resilience-hub.org
# Expected: HTTP/1.1 301 Moved Permanently → to HTTPS

curl -I https://resilience-hub.org
# Expected: HTTP/2 200 OK (with Let's Encrypt cert)

# View live logs
docker logs discourse_app --tail 50 | grep -E "INFO|ERROR|WARN"

# If you see "Puma starting" → Discourse is up
# If you see "Errno::ECONNREFUSED" → wait 30 more seconds

# Test from external machine
curl -s https://resilience-hub.org | grep -o "<title>.*</title>"
# Expected: <title>Resilience Hub</title>
```

### Step 4: Admin Account Creation (15 min — 07:20–07:35 UTC)

```bash
# Register first admin user (this links to the DISCOURSE_DEVELOPER_EMAILS)
./launcher exec app discourse email:update

# Open https://resilience-hub.org in browser
# Click "Sign Up"
# Use the DISCOURSE_DEVELOPER_EMAILS address
# A confirmation email will be sent

# OR create admin via rails console (no email required):
./launcher exec app rake admin:create
# Enter email, password when prompted
# Type "Y" to make admin
```

### Step 5: Core Configuration (30 min — 07:35–08:05 UTC)

All via `/admin/site_settings` in browser:

**Branding**:
- `title`: Resilience Hub
- `site_description`: Community coordination for Phase 5 & 6 resilience projects
- `contact_email`: admin@youremail.com
- `notification_email`: noreply@resilience-hub.org

**Authentication**:
- `enable_local_logins`: true (allow username/password)
- `github_client_id`: (from Part 1, Step 1.4)
- `github_client_secret`: (from Part 1, Step 1.4)
- `enable_github_logins`: true

**Posting restrictions** (reduce spam during Phase 5):
- `min_post_length`: 20
- `max_topics_per_day`: 10 (for new users)
- `min_first_post_length`: 100

**Email settings**:
- `reply_by_email_enabled`: false (keep email simple for now)
- `email_digests`: true
- `digest_frequency`: daily

### Step 6: Create Category Structure (20 min — 08:05–08:25 UTC)

Via `/admin/categories` → New Category:

```
Category 1: Announcements
- Description: Phase 5 Wave publications, critical updates
- Color: #0088CC (blue)
- Permissions: staff (post) + everyone (read)

Category 2: Wave 1 — Community Implementation
- Description: Feedback thread for Community Implementation Playbook
- Color: #2CA089 (green)
- Permissions: author_phase5 group (post) + trust_level_0 (read)

Category 3: Wave 1 — Energy Systems
- Description: Feedback thread for Microgrids Infrastructure guide
- Color: #2CA089

Category 4: Wave 1 — Human Systems
- Description: Psychological support + conflict resolution guides
- Color: #2CA089

Category 5: Wave 1 — Animal Protocols
- Description: Veterinary care guide
- Color: #2CA089

Category 6: Phase 6 Coordination
- Description: Phase 6 domain planning (editors only)
- Permissions: staff (full) + trust_level_3 (post)

Category 7: General Discussion
- Color: #808080 (gray)
- Permissions: everyone

Category 8: Technical Issues
- Color: #BB2929 (red)
```

Create user group for authors:
- `/admin/groups` → New Group
- Name: `author_phase5`
- Automatic membership: invite-only
- Add members as they are onboarded

### Step 7: GitHub OAuth Verification (10 min — 08:25–08:35 UTC)

```bash
# Test GitHub OAuth login:
# 1. Log out of admin account
# 2. Click "Log In" → "GitHub"
# 3. Authorize the GitHub OAuth application
# 4. Should redirect back to Discourse and log in

# If OAuth fails, check:
# - Authorization callback URL matches exactly: https://resilience-hub.org/auth/github/callback
# - Client ID and Secret copied without leading/trailing spaces
# - GitHub OAuth app is not suspended
```

---

## Part 3: Trust-Level Self-Governance Configuration

Discourse's trust level system automates moderation. Configure once; no manual intervention needed.

### Trust Level Settings (`/admin/site_settings` → search "trust_level")

```
# Level 0 → Level 1 (Basic User) — earned in first session
trust_level_0_requires_topics_entered: 2
trust_level_1_requires_days_visited: 1
trust_level_1_requires_read_posts: 5
trust_level_1_requires_time_spent_mins: 10
trust_level_1_requires_topics_replied_to: 0

# Level 1 → Level 2 (Member) — earned after regular participation
trust_level_2_requires_days_visited: 10
trust_level_2_requires_read_posts: 50
trust_level_2_requires_time_spent_mins: 60
trust_level_2_requires_topics_replied_to: 3
trust_level_2_requires_likes_received: 0

# Level 2 → Level 3 (Regular) — auto-promoted after sustained engagement
trust_level_3_requires_days_visited: 50
trust_level_3_requires_read_posts: 500
trust_level_3_requires_posts_created: 10
trust_level_3_requires_topics_replied_to: 10

# Rate limits for Level 0 (new users)
# These prevent spam before trust is established
max_new_topics_per_day: 3
max_topics_in_first_day: 2
max_replies_in_first_day: 5
```

### Trust Level Capabilities Reference

| Level | Name | What they can do | Phase 5 meaning |
|-------|------|-----------------|-----------------|
| 0 | New | Read, post with approval | Guest readers |
| 1 | Basic | Post freely, like, use all post types | Active readers |
| 2 | Member | Invite others, wiki posts, post summaries | Peer reviewers |
| 3 | Regular | Recategorize, rename, close topics | Trusted authors |
| 4 | Leader | All moderation actions | Editors |

**For Phase 5 authors**: Manually grant Trust Level 3 to all confirmed authors upon account creation. This gives them full posting capability immediately, bypassing the 50-day accumulation requirement.

```bash
# Grant trust level 3 to an author via admin panel:
# /admin/users/username → Trust Level → "Grant Trust Level 3"

# OR via Discourse API (automated):
curl -X PUT https://resilience-hub.org/admin/users/<user_id>/trust_level \
  -H "Api-Key: <admin-api-key>" \
  -H "Api-Username: admin" \
  -d "level=3"
```

---

## Part 4: REST API Automation Scripts

### 4.1 Generate Admin API Key

```bash
# Via browser: /admin/api → "Generate New API Key"
# Scope: Global
# Username: admin

# Test key works
DISCOURSE_URL="https://resilience-hub.org"
API_KEY="<paste-key-here>"

curl -s -H "Api-Key: ${API_KEY}" \
     -H "Api-Username: admin" \
     "${DISCOURSE_URL}/admin/users/list.json" | jq '.[0].username'
```

### 4.2 Bulk Author Account Creation Script

```bash
cat > create-discourse-authors.sh << 'EOF'
#!/bin/bash
# Creates Discourse accounts for all Phase 5 authors via REST API
# Discourse sends welcome email automatically on account creation

DISCOURSE_URL="https://resilience-hub.org"
API_KEY="REPLACE_WITH_API_KEY"

# Author list: username "Display Name" email trust_level
AUTHORS=(
  "author1_fname_lname \"Author One Name\" author1@email.com 3"
  "author2_fname_lname \"Author Two Name\" author2@email.com 3"
  # Add all Wave 1 authors from PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md
)

create_user() {
  local username="$1"
  local name="$2"
  local email="$3"
  local trust_level="$4"

  echo "Creating: ${username} (${email})"

  # Create user
  result=$(curl -s -X POST "${DISCOURSE_URL}/users" \
    -H "Api-Key: ${API_KEY}" \
    -H "Api-Username: admin" \
    -H "Content-Type: application/json" \
    -d "{
      \"name\": \"${name}\",
      \"username\": \"${username}\",
      \"email\": \"${email}\",
      \"password\": \"$(openssl rand -base64 16)\",
      \"active\": true,
      \"approved\": true
    }")

  user_id=$(echo "$result" | jq -r '.user.id // .user_id // empty')

  if [ -z "$user_id" ]; then
    echo "  WARN: Could not create ${username}: $(echo $result | jq .errors)"
    return
  fi

  echo "  Created user ID: ${user_id}"

  # Set trust level
  curl -s -X PUT "${DISCOURSE_URL}/admin/users/${user_id}/trust_level" \
    -H "Api-Key: ${API_KEY}" \
    -H "Api-Username: admin" \
    -d "level=${trust_level}" > /dev/null

  echo "  Trust level set to ${trust_level}"

  # Add to author group
  curl -s -X PUT "${DISCOURSE_URL}/groups/author_phase5/members.json" \
    -H "Api-Key: ${API_KEY}" \
    -H "Api-Username: admin" \
    -H "Content-Type: application/json" \
    -d "{\"usernames\": \"${username}\"}" > /dev/null

  echo "  Added to author_phase5 group"
}

for entry in "${AUTHORS[@]}"; do
  eval "create_user $entry"
done

echo "Done. All authors created."
EOF

chmod +x create-discourse-authors.sh
```

### 4.3 Wave 1 Announcement Script

```bash
cat > post-wave1-announcement.sh << 'EOF'
#!/bin/bash
# Posts the Wave 1 + 2 launch announcement to Discourse
DISCOURSE_URL="https://resilience-hub.org"
API_KEY="REPLACE_WITH_API_KEY"

# Get category ID for Announcements
CATEGORY_ID=$(curl -s "${DISCOURSE_URL}/categories.json" | \
  jq '.category_list.categories[] | select(.name=="Announcements") | .id')

echo "Posting to category ID: ${CATEGORY_ID}"

curl -s -X POST "${DISCOURSE_URL}/posts" \
  -H "Api-Key: ${API_KEY}" \
  -H "Api-Username: admin" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Phase 5 Wave 1 + 2 Publication — Community Guides Available\",
    \"raw\": \"The Phase 5 Wave 1 + 2 publication is now available for author feedback and community review.\n\n## Documents (43,621 words total)\n\n1. **Community Implementation Playbook** (8,619 words)\n2. **Microgrids Infrastructure** (6,545 words)\n3. **Psychological Support Guide** (9,163 words)\n4. **Conflict Resolution Framework** (8,596 words)\n5. **Veterinary Care Guide** (10,698 words)\n\n## What to do\n- Review the guide in your category\n- Leave feedback in the category thread\n- Authors respond within 24 hours\n\n**Feedback deadline**: June 13, 2026 17:00 UTC\",
    \"category\": ${CATEGORY_ID},
    \"pinned_globally\": true,
    \"tags\": [\"phase-5\", \"announcement\", \"wave-1\"]
  }" | jq '.post.id'

echo "Announcement posted."
EOF

chmod +x post-wave1-announcement.sh
```

### 4.4 Response Routing Automation (Phase 5 Wave Monitoring)

```bash
cat > wave-response-monitor.py << 'EOF'
#!/usr/bin/env python3
"""
wave-response-monitor.py
Monitors Discourse topics for author activity and flags inactive threads.

Usage: python3 wave-response-monitor.py
       Schedule via cron: 0 9 * * * python3 /path/to/wave-response-monitor.py

Requires: pip install requests
"""

import requests
import json
from datetime import datetime, timedelta, timezone

DISCOURSE_URL = "https://resilience-hub.org"
API_KEY = "REPLACE_WITH_API_KEY"
ADMIN_USERNAME = "admin"
INACTIVITY_THRESHOLD_DAYS = 2  # Flag if no response in 2 days

HEADERS = {
    "Api-Key": API_KEY,
    "Api-Username": ADMIN_USERNAME,
}

def get_topics_in_category(category_id: int) -> list:
    r = requests.get(
        f"{DISCOURSE_URL}/c/{category_id}.json",
        headers=HEADERS,
    )
    r.raise_for_status()
    return r.json().get("topic_list", {}).get("topics", [])

def check_topics_for_inactivity(topics: list) -> list:
    """Return list of topics with no activity in threshold period."""
    now = datetime.now(timezone.utc)
    threshold = now - timedelta(days=INACTIVITY_THRESHOLD_DAYS)
    stale = []

    for topic in topics:
        if topic.get("pinned"):
            continue  # Skip pinned announcements

        last_posted = topic.get("last_posted_at", "")
        if not last_posted:
            continue

        last_post_dt = datetime.fromisoformat(last_posted.replace("Z", "+00:00"))
        if last_post_dt < threshold:
            stale.append({
                "id": topic["id"],
                "title": topic["title"],
                "last_posted": last_posted,
                "reply_count": topic.get("reply_count", 0),
            })

    return stale

def post_nudge(topic_id: int, message: str) -> None:
    """Post a nudge message to a stale topic."""
    requests.post(
        f"{DISCOURSE_URL}/posts",
        headers=HEADERS,
        json={
            "topic_id": topic_id,
            "raw": message,
        }
    )

def main():
    # Get Wave 1 category IDs
    categories_r = requests.get(f"{DISCOURSE_URL}/categories.json", headers=HEADERS)
    categories = categories_r.json()["category_list"]["categories"]

    wave1_cats = [c for c in categories if c["name"].startswith("Wave 1")]

    all_stale = []
    for cat in wave1_cats:
        topics = get_topics_in_category(cat["id"])
        stale = check_topics_for_inactivity(topics)
        all_stale.extend(stale)

    if all_stale:
        print(f"Found {len(all_stale)} stale topics:")
        for t in all_stale:
            print(f"  [{t['id']}] {t['title']} — last post: {t['last_posted']}")
    else:
        print("All Wave 1 topics are active.")

if __name__ == "__main__":
    main()
EOF
```

---

## Part 5: Community Moderation Playbook

### 5.1 Escalation Tiers

| Tier | Trigger | Action | Owner |
|------|---------|--------|-------|
| 0 — Auto | Off-topic, spam, low quality | Trust level system auto-flags; Discourse hides post | System |
| 1 — Soft | Author conflict in a thread | Moderator (TL4) sends private message to both parties | TL4 user |
| 2 — Hard | Policy violation, harassment | Admin suspends user 24–72h; posts hidden | Admin |
| 3 — Escalate | Persistent bad actor | User banned; IP blocked via `/admin/logs/screened_ip_addresses` | Admin |

### 5.2 Community Health Metrics

Check daily at 09:00 UTC via `/admin/dashboard`:

| Metric | Healthy | Warning | Action |
|--------|---------|---------|--------|
| Daily active users | >60% of author count | 40–60% | Send nudge email |
| New posts/day | 10–50 | <5 | Post conversation starter topic |
| Flagged posts | 0 | 1–3 | Review within 4h |
| Users with 0 posts | <20% of total | >30% | Direct onboarding follow-up |
| Email bounce rate | <5% | >10% | Audit email list |

**Quick health check via API**:
```bash
DISCOURSE_URL="https://resilience-hub.org"
API_KEY="REPLACE_WITH_API_KEY"

curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "${DISCOURSE_URL}/admin/dashboard.json" | jq '{
  users_active_30_days: .global_reports[] | select(.type=="consolidated_page_views"),
  posts_7_day: .global_reports[] | select(.type=="posts")
}' 2>/dev/null || \
curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "${DISCOURSE_URL}/admin/reports.json" | jq '.reports[].title' | head -10
```

### 5.3 Moderation Actions Quick Reference

```bash
# View all flagged posts
open https://resilience-hub.org/admin/flags

# Silence a user (they can read but not post) for 24h
curl -s -X PUT "https://resilience-hub.org/admin/users/<user_id>/silence" \
  -H "Api-Key: ${API_KEY}" \
  -H "Api-Username: admin" \
  -d "silenced_till=2026-06-06T09:00:00.000Z&reason=Policy violation (first warning)"

# Suspend a user
curl -s -X PUT "https://resilience-hub.org/admin/users/<user_id>/suspend" \
  -H "Api-Key: ${API_KEY}" \
  -H "Api-Username: admin" \
  -d "suspend_until=2026-06-10T09:00:00.000Z&reason=Repeated policy violations"

# Delete a post
curl -s -X DELETE "https://resilience-hub.org/posts/<post_id>" \
  -H "Api-Key: ${API_KEY}" \
  -H "Api-Username: admin"
```

---

## Part 6: GitHub Pages Integration

### 6.1 Create GitHub Pages Archive Repository

```bash
# Create repository for static archive
# Via browser: github.com → New repository → "resilience-hub-archive"
# Settings → Pages → Source: "Deploy from branch" → branch: main, /docs folder
```

### 6.2 GitHub Actions Workflow — Auto-Announce and Archive

Create `.github/workflows/discourse-phase5.yml` in the SuperClaude_Framework repo:

```yaml
name: Phase 5 — Discourse Announce + GitHub Pages Archive

on:
  push:
    branches: [master]
    paths:
      - 'projects/systems-resilience/phase-5-wave-*.md'
      - 'projects/systems-resilience/PHASE_5_WAVE_*.md'

jobs:
  announce-and-archive:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Identify changed Phase 5 files
        id: changes
        run: |
          CHANGED=$(git diff --name-only HEAD~1..HEAD | grep -E 'phase-5-wave|PHASE_5_WAVE' | head -10)
          echo "files=${CHANGED}" >> $GITHUB_OUTPUT

          # Build word-count summary
          SUMMARY=""
          for f in $CHANGED; do
            COUNT=$(wc -w < "$f" 2>/dev/null || echo 0)
            BASENAME=$(basename "$f" .md | tr '_' ' ' | tr '-' ' ')
            SUMMARY="${SUMMARY}\n- **${BASENAME}**: ${COUNT} words"
          done
          echo "summary=${SUMMARY}" >> $GITHUB_OUTPUT

      - name: Post announcement to Discourse
        if: steps.changes.outputs.files != ''
        run: |
          # Build announcement body
          BODY=$(cat <<BODY
          New Phase 5 content published — $(date -u '+%B %d, %Y')

          **Updated guides:**
          ${{ steps.changes.outputs.summary }}

          **View on GitHub**: [$(git log -1 --pretty=%s)](${{ github.server_url }}/${{ github.repository }}/commit/${{ github.sha }})

          Review and provide feedback in the relevant category thread.
          BODY
          )

          curl -s -X POST "${{ secrets.DISCOURSE_URL }}/posts" \
            -H "Api-Key: ${{ secrets.DISCOURSE_API_KEY }}" \
            -H "Api-Username: admin" \
            -H "Content-Type: application/json" \
            -d "{\"title\": \"Publication Update: $(date -u '+%b %d')\", \"raw\": \"${BODY}\", \"category\": 1}"

      - name: Convert Markdown to HTML for GitHub Pages
        if: steps.changes.outputs.files != ''
        run: |
          sudo apt-get install -y pandoc
          mkdir -p docs/phase-5

          # Simple HTML template
          cat > /tmp/template.html << 'TMPL'
          <!DOCTYPE html>
          <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>$title$ — Resilience Hub</title>
            <style>
              body { font-family: Georgia, serif; max-width: 800px; margin: 2rem auto; padding: 1rem; line-height: 1.7; }
              h1, h2, h3 { font-family: sans-serif; }
              code { background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
              pre { background: #f4f4f4; padding: 1rem; overflow-x: auto; }
            </style>
          </head>
          <body>
          $body$
          </body>
          </html>
          TMPL

          for FILE in projects/systems-resilience/phase-5-wave-*.md; do
            [ -f "$FILE" ] || continue
            BASENAME=$(basename "$FILE" .md)
            pandoc "$FILE" \
              --from markdown \
              --to html5 \
              --template /tmp/template.html \
              --output "docs/phase-5/${BASENAME}.html"
            echo "Converted: $BASENAME"
          done

          # Create index page
          echo "<html><body><h1>Phase 5 Guides</h1><ul>" > docs/phase-5/index.html
          for FILE in docs/phase-5/*.html; do
            NAME=$(basename "$FILE" .html | tr '-' ' ')
            echo "<li><a href=\"$(basename $FILE)\">$NAME</a></li>"
          done >> docs/phase-5/index.html
          echo "</ul></body></html>" >> docs/phase-5/index.html

      - name: Deploy to GitHub Pages
        if: steps.changes.outputs.files != ''
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
          destination_dir: phase-5
```

**Add GitHub Secrets**:
1. Repository → Settings → Secrets → New repository secret
2. `DISCOURSE_URL`: `https://resilience-hub.org`
3. `DISCOURSE_API_KEY`: (from `/admin/api`)

---

## Part 7: Backup and Disaster Recovery

### 7.1 Automated Daily Backup

```bash
# On the VPS, as discourse user
cat > ~/backup-discourse.sh << 'EOF'
#!/bin/bash
# Discourse nightly backup — runs via cron at 02:00 UTC
set -e

BACKUP_DIR=/home/discourse/backups
mkdir -p "${BACKUP_DIR}"
DATE=$(date +%Y%m%d)

echo "Discourse backup starting at $(date -u)"

# Discourse built-in backup via rails
cd ~/discourse
./launcher exec app rake posts:rebake_uncooked_posts 2>/dev/null || true

# Database dump
./launcher exec app pg_dump discourse > "${BACKUP_DIR}/discourse-db-${DATE}.sql"
gzip "${BACKUP_DIR}/discourse-db-${DATE}.sql"

# Uploads backup
rsync -a /var/discourse/shared/standalone/uploads/ "${BACKUP_DIR}/uploads-${DATE}/"

# Retention: 30 days
find "${BACKUP_DIR}" -name "*.sql.gz" -mtime +30 -delete
find "${BACKUP_DIR}" -maxdepth 1 -type d -name "uploads-*" -mtime +30 -exec rm -rf {} + 2>/dev/null || true

echo "Backup complete: $(du -sh ${BACKUP_DIR}/${DATE}* 2>/dev/null | head -5)"
EOF

chmod +x ~/backup-discourse.sh

# Schedule via cron
(crontab -l 2>/dev/null; echo "0 2 * * * /home/discourse/backup-discourse.sh >> /home/discourse/backup.log 2>&1") | crontab -
```

### 7.2 Disaster Recovery Procedure

**Full server rebuild from backup** (if VPS fails):

```bash
# 1. Provision new VPS (same spec)
# 2. Repeat Steps 1–3 from Part 2 (stop before bootstrap)
# 3. After new Discourse is installed, restore database:

ssh root@<NEW_VPS_IP>

# Copy backup files from old server or local machine
rsync -avz /path/to/backups/ root@<NEW_VPS_IP>:/tmp/discourse-backup/

# On new VPS: restore database
cd ~/discourse
./launcher enter app
psql -U discourse discourse < /tmp/discourse-backup/discourse-db-20260605.sql
exit

# Restore uploads
rsync -a /tmp/discourse-backup/uploads-20260605/ /var/discourse/shared/standalone/uploads/

# Rebuild application
./launcher rebuild app
```

**Estimated recovery time from backup**: 45–90 minutes.

### 7.3 Discourse Built-in Backup

Discourse also has a built-in backup system via admin panel:

```
/admin/backups → "Backup Now"
```

This creates a downloadable `.tar.gz` containing database + uploads. Schedule automatic backups:
- `/admin/site_settings` → "maximum_backups": 7
- `/admin/site_settings` → "backup_frequency": daily

---

## Part 8: Monitoring and Health Checks

### 8.1 Daily Health Check Script

```bash
cat > ~/check-discourse.sh << 'EOF'
#!/bin/bash
DISCOURSE_URL="https://resilience-hub.org"
API_KEY="REPLACE_WITH_API_KEY"

echo "=== Discourse Health Check — $(date -u) ==="

# Container running
docker ps | grep discourse_app | grep -q "Up" \
  && echo "PASS: discourse_app container running" \
  || echo "FAIL: discourse_app container not running"

# HTTP responding
curl -s -o /dev/null -w "HTTP %{http_code}" "${DISCOURSE_URL}" | grep -q "200" \
  && echo "PASS: HTTPS responding" \
  || echo "FAIL: HTTPS not responding"

# Disk usage
DISK_PCT=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
[ "$DISK_PCT" -lt 80 ] \
  && echo "PASS: Disk ${DISK_PCT}% used" \
  || echo "WARN: Disk ${DISK_PCT}% used — clean up soon"

# User count
USER_COUNT=$(curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "${DISCOURSE_URL}/admin/users/list.json?show_emails=false&stats=false" 2>/dev/null | jq '. | length' 2>/dev/null)
echo "INFO: User count: ${USER_COUNT:-unknown}"

# Active users (last 7 days)
ACTIVE=$(curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "${DISCOURSE_URL}/admin/reports/dau_by_mau.json?start_date=$(date -u -d '7 days ago' +%Y-%m-%d)&end_date=$(date -u +%Y-%m-%d)" 2>/dev/null | jq '.report.data[-1].y' 2>/dev/null)
echo "INFO: Active users (7d): ${ACTIVE:-unknown}"

echo "=== Check complete ==="
EOF

chmod +x ~/check-discourse.sh
(crontab -l 2>/dev/null; echo "0 9 * * * /home/discourse/check-discourse.sh >> /home/discourse/health.log 2>&1") | crontab -
```

### 8.2 Performance Metrics Targets

| Metric | Target | Check command |
|--------|--------|---------------|
| Page load (Lighthouse) | <2 seconds | https://pagespeed.web.dev |
| Container uptime | 100% | `docker ps` (RESTARTS column = 0) |
| Database size | <5 GB | `./launcher exec app rake db:stats` |
| Disk free | >20 GB | `df -h /` |
| Email delivery | >95% | `/admin/email` → Sent logs |
| Backup age | <24h | Check `/admin/backups` |

---

## Part 9: Troubleshooting Quick Reference

### T1: Discourse won't start after bootstrap

```bash
cd ~/discourse

# View startup logs
docker logs discourse_app 2>&1 | tail -100 | grep -E "ERROR|WARN|Started|Failed"

# Most common: SMTP credentials wrong (Discourse refuses to start)
# Solution: Edit containers/app.yml SMTP section and rebuild
nano containers/app.yml   # fix SMTP settings
./launcher rebuild app    # takes 5-10 min

# If Let's Encrypt fails (DNS not propagated):
# In app.yml, comment out LETSENCRYPT lines, bootstrap with HTTP only first
./launcher rebuild app
# After DNS propagates, re-enable LETSENCRYPT and rebuild again
```

### T2: "too many redirects" error

```bash
# Usually caused by DISCOURSE_HOSTNAME not matching actual domain
docker exec discourse_app grep DISCOURSE_HOSTNAME /etc/discourse/app.yml

# Fix: update DISCOURSE_HOSTNAME in containers/app.yml, rebuild
./launcher rebuild app
```

### T3: Email not being sent

```bash
# Test SMTP from within container
./launcher exec app rails runner \
  'TestMailer.send_test("admin@youremail.com").deliver_now rescue puts $!.message'

# Check mail queue
./launcher exec app rake jobs:run_later &

# View Discourse mail log
./launcher exec app tail -30 /var/log/nginx/access.log | grep mail
```

### T4: GitHub OAuth not working

```bash
# Common causes:
# 1. Callback URL mismatch — must exactly match setting in GitHub OAuth app
#    Expected: https://resilience-hub.org/auth/github/callback

# Check current callback URL in Discourse settings
curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "https://resilience-hub.org/admin/site_settings.json" | \
  jq '.settings[] | select(.name | test("github")) | {name, value}'
```

### T5: API key not working

```bash
# Verify key is not revoked
curl -s -H "Api-Key: ${API_KEY}" -H "Api-Username: admin" \
  "https://resilience-hub.org/admin/api/keys.json" | jq '.[0].description'

# If 403 error: key may be scoped to specific endpoints
# Solution: Create new Global key via /admin/api
```

### T6: VPS disk full

```bash
# Identify large files
du -sh /var/discourse/shared/standalone/* | sort -h | tail -10

# Clean Discourse logs
./launcher exec app find /var/log -name "*.log" -size +100M -exec truncate -s 50M {} \;

# Remove old Docker images
docker image prune -f
docker container prune -f

# Clear Discourse tmp files
./launcher exec app rake tmp:clear
```

### Key Log Paths

| Log | Location |
|-----|---------|
| Discourse main | `docker logs discourse_app` |
| Nginx | `/var/discourse/shared/standalone/log/nginx.log` |
| PostgreSQL | `./launcher exec app tail /shared/log/var-log/postgresql.log` |
| Email (Postfix) | `./launcher exec app tail /var/log/mail.log` |
| Rails production | `./launcher exec app tail /shared/log/production.log` |

---

## Part 10: Admin Dashboard Orientation

### Key Admin Sections

| URL path | Purpose | Check daily |
|----------|---------|-------------|
| `/admin/dashboard` | Usage overview (users, posts, page views) | Yes |
| `/admin/users` | User list, trust levels, account actions | On-demand |
| `/admin/flags` | Flagged posts awaiting review | Yes |
| `/admin/email` | Email delivery log, SMTP status | If bounce suspected |
| `/admin/logs` | Error log, screened IPs, rate limits | If issues reported |
| `/admin/backups` | Backup status, download backups | Weekly |
| `/admin/api` | API key management | On-demand |

### Discourse Admin CLI Reference

```bash
# Most admin actions done via browser; these are power-user CLI shortcuts

# Force-send all pending emails
./launcher exec app rake jobs:run_later

# Rebuild search index
./launcher exec app rake search:reindex

# Regenerate missing thumbnails
./launcher exec app rake posts:rebake_uncooked_posts

# Check database consistency
./launcher exec app rake db:check

# List all site settings (search for specific setting)
./launcher exec app rails runner \
  'SiteSetting.all_settings.each { |s| puts "#{s[:setting]}: #{s[:value]}" }' | grep -i smtp
```

---

## Part 11: Rollback to Path A (Nextcloud+Matrix)

If Discourse experiences unresolvable issues during Phase 5:

1. **Export all Discourse content**:
   ```bash
   # Via admin panel: /admin/backups → Backup Now
   # Download the .tar.gz file
   ```

2. **Convert Discourse posts to Markdown** (for Nextcloud import):
   ```python
   # Discourse API: GET /posts/{id}.json returns raw Markdown content
   import requests
   r = requests.get("https://resilience-hub.org/posts.json", 
       headers={"Api-Key": API_KEY, "Api-Username": "admin"})
   for post in r.json()["latest_posts"]:
       filename = f"post_{post['id']}.md"
       with open(filename, "w") as f:
           f.write(f"# {post['topic_title']}\n\n{post['raw']}")
   ```

3. **Deploy Nextcloud+Matrix** using the companion playbook
4. **Upload exported Markdown files** to Nextcloud

Timeline: 2–4 hours to full migration, assuming Nextcloud stack is healthy.

---

## Deployment Timeline Summary

| Step | Duration | Start (UTC) | Gate |
|------|----------|-------------|------|
| VPS provisioned + SSH access | 15 min | June 5 06:00 | SSH works |
| System update + Docker install | 15 min | 06:15 | Docker version OK |
| Clone Discourse + configure app.yml | 20 min | 06:30 | Config reviewed |
| Bootstrap (Docker image build) | 35 min | 06:50 | "Successfully bootstrapped" |
| Start Discourse + verify HTTPS | 20 min | 07:25 | Browser shows homepage |
| Admin account creation | 10 min | 07:45 | Admin panel accessible |
| Core settings + GitHub OAuth | 30 min | 07:55 | OAuth login tested |
| **Go-live gate** | — | **08:25** | Platform accessible |
| Category structure | 20 min | 08:25 | 8 categories created |
| GitHub Actions config | 30 min | 08:45 | Webhook configured |
| Author account creation | 30 min | 09:15 | All accounts active |
| Wave 1 announcement post | 15 min | 09:45 | Pinned post visible |
| Onboarding emails sent | 15 min | 10:00 | Emails in transit |
| **Operational gate** | — | **10:15** | Authors can log in |

**Total**: 3–4 hours from zero to author-accessible.

---

*Status: READY-TO-EXECUTE | Confidence: 8.0/10 | Offline capability: browser cache only*
*Use this playbook if Path A (Nextcloud+Matrix) fails by June 5 12:00 UTC, or if user explicitly selects Discourse*
*Cross-reference: PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md (strategic context), PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md (Phase 6 integration)*
