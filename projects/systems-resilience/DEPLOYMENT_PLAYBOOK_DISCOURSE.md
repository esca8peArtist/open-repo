---
title: "Discourse Deployment Playbook — Phase 5 Production Guide"
project: systems-resilience
phase: "5 — Wave 1 Author Recruitment & Community Forum"
platform: "Discourse 3.2+ Community Forum"
status: PRODUCTION-READY
created: 2026-06-04
target_date: 2026-06-05T13:00Z
deployment_window: "2-3 hours (June 4 06:00 UTC – June 5 09:00 UTC)"
resource_requirement: "8GB RAM, 2-4 CPU cores, 60GB+ storage"
success_criteria: "Platform online + HTTPS + admin account active + GitHub OAuth working + 10 test users created + publication workflow verified by June 5 13:00 UTC"
---

# Discourse Deployment Playbook
## Complete Production Guide for Phase 5 Wave 1 Author Community Forum

**Decision Context**: User selects Platform B (Discourse) by June 4 EOD. If selected, deployment begins June 4 06:00 UTC to meet June 5 13:00 UTC Wave 1 author recruitment kickoff.

**Critical Success Factor**: Authors must be able to (1) register/login, (2) read published Wave 1+2 documents, (3) post discussion threads/replies, and (4) access moderation/governance features **by June 5 13:00 UTC**. This playbook is designed to be deployable in 2-3 hours.

**Important Note on Deployment Method**: Discourse's official Docker deployment uses a custom launcher script (`discourse_docker`) and `app.yml` configuration, NOT a standard `docker-compose.yml`. The launcher handles asset precompilation, database initialization, and bootstrap processes that plain Docker Compose cannot. This playbook follows the official method exclusively. Alternative approaches (bitnami/docker-compose) are fallbacks only and not supported by Discourse core team.

---

## Part 0: Architecture Overview

### Service Stack

```
┌─────────────────────────────────────────────────┐
│ Authors (Browser)                               │
│ - Web browsers (Firefox, Chrome)                │
│ - Mobile browsers (Safari, Chrome mobile)       │
└────────────────────┬────────────────────────────┘
                     │
                     │ HTTPS
                     │
         ┌───────────▼──────────┐
         │                      │
      ┌──┴──────────────────┐   │
      │  nginx (managed by  │   │
      │  Discourse launcher)│   │
      │  TLS Termination    │◄──┘
      │  SSL/Let's Encrypt  │
      └──────────┬──────────┘
                 │
         ┌───────▼───────────────────────────────┐
         │                                       │
         │ Discourse (single Docker container)   │
         │ ├─ Rails application (Puma)           │
         │ ├─ PostgreSQL database (embedded)     │
         │ ├─ Redis cache (embedded)             │
         │ ├─ Sidekiq job processor              │
         │ ├─ nginx proxy (internal)             │
         │ └─ runit process manager              │
         │                                       │
         │ Services managed by launcher:         │
         │ ├─ Discourse core (read/write)        │
         │ ├─ User auth (local, OAuth, LDAP)     │
         │ ├─ Trust levels (auto-moderation)     │
         │ ├─ Plugins (GitHub, API integrations) │
         │ └─ Backups (S3-compatible storage)    │
         └───────────────────────────────────────┘
```

### Data Flow for Author Workflows

```
Author (Web Browser)
  │
  ├─→ Register/Login
  │   ├─ GitHub OAuth (recommended)
  │   ├─ Local account (fallback)
  │   └─ Session stored in Redis (embedded)
  │
  ├─→ Read Published Wave 1+2 Documents
  │   ├─ Posts in "Announcements" or "Wave 1" category
  │   ├─ Markdown content + embedded files
  │   └─ Cached for fast loading
  │
  ├─→ Create Discussion Thread
  │   ├─ Post reply to Wave 1 document
  │   ├─ Markdown formatting + code blocks
  │   ├─ Optional: attach files or images
  │   ├─ Stored in PostgreSQL
  │   └─ Notifies other authors via email
  │
  ├─→ Real-time Chat
  │   ├─ Direct messages (private convos)
  │   ├─ Or: Category/group messages
  │   └─ Indexed by search
  │
  └─→ Governance & Moderation
      ├─ Trust levels (auto-escalate based on activity)
      ├─ Category permissions (who can post where)
      ├─ Moderation tools (flag spam, hide posts)
      └─ Admin panel (view user activity, enforce rules)
```

### Resource Model for 150 Active Users

| Component | RAM | CPU | Purpose |
|-----------|-----|-----|---------|
| PostgreSQL (embedded) | 1.5 GB | 1 core | User accounts, posts, settings |
| Redis (embedded) | 512 MB | shared | Sessions, cache, real-time updates |
| Rails (Puma) | 2.0 GB | 2 cores | Web application, request handling |
| Sidekiq | 1.0 GB | 1 core | Background jobs (email, search indexing) |
| nginx (internal) | 256 MB | shared | Request routing, compression |
| OS / runit | 2.0 GB | shared | System services, process management |
| **Total Recommended** | **8 GB** | **2-4 cores** | All-in-one container approach |

**Scaling Notes**:
- 150-300 users: 8 GB RAM, 2-4 cores comfortable
- 300-500 users: 16 GB RAM, 4+ cores + external PostgreSQL recommended
- 500+ users: Dedicated PostgreSQL host, Discourse standalone container, separate Redis

---

## Part 1: Pre-Deployment Checklist

### 1.1 Infrastructure Requirements

**Hardware** (must meet ALL):
- [ ] **Host Machine**: Ubuntu 22.04 LTS or 24.04 (strongly recommended)
- [ ] **RAM**: Minimum 6 GB usable (4 GB for Discourse + 2 GB OS/buffer); 8+ GB recommended
- [ ] **CPU**: 2 cores minimum; 4 cores recommended
- [ ] **Storage**: 60 GB minimum (OS + Discourse database + uploads); 100+ GB recommended
- [ ] **Network**: Static public IP address (not dynamic DHCP)
- [ ] **Uptime**: Host available 24/7 or configured with auto-restart on crash

**Software Prerequisites** (install before starting deployment):
- [ ] Docker (v20.10+): `docker --version` should return `Docker version 20.10+`
- [ ] curl: `curl --version` works
- [ ] git: `git --version` works (needed to clone discourse_docker repo)
- [ ] openssh-server: `ssh localhost` works (for management access)

**Network Requirements** (must meet ALL):
- [ ] **DNS Domain**: Registered, owns `forum.yourdomain.com` (e.g., `collab.example.com`)
- [ ] **DNS TTL**: Set to 300 seconds (5 minutes) for fast updates during deployment
- [ ] **Firewall**: Inbound allowed on ports 80 (HTTP), 443 (HTTPS) from anywhere
- [ ] **Outbound**: Can reach mail servers (for email notifications), GitHub (for OAuth)
- [ ] **No ISP restrictions**: Some ISPs block port 25 (outbound SMTP); verify with your provider

**Pre-Flight Checks** (run 30 minutes before deployment start):

```bash
# Check Ubuntu version
lsb_release -a
# Expected: Ubuntu 22.04 LTS or 24.04

# Check available RAM
free -h
# Expected: At least 6 GB free in Mem/Available

# Check CPU
nproc
# Expected: 2 or more

# Check disk space
df -h /
# Expected: At least 60 GB free

# Check Docker
docker --version
docker ps
# Expected: both commands work without error

# Check git
git --version
# Expected: 2.30+

# Verify ports 80/443 are free
sudo ss -tlnp | grep -E ':80|:443'
# Expected: nothing listed (ports free)

# Test internet connectivity
curl -I https://github.com
# Expected: HTTP/2 200 or similar

# Test DNS resolution
nslookup forum.example.com
# Expected: resolves to your server's public IP
```

### 1.2 Information Required Before Deployment

Gather these values **before** starting:

| Item | Example | Purpose |
|------|---------|---------|
| **Public Domain Name** | `forum.example.com` | nginx host, TLS, SMTP from address |
| **Server Public IP** | `203.0.113.42` | DNS A record, firewall rules |
| **Admin Email** | `admin@example.com` | Admin account, Let's Encrypt notifications |
| **Admin Username** | `admin` | Discourse admin login |
| **Admin Password** | [secure, 16+ chars] | Initial admin access |
| **SMTP Provider** | `smtp.mailgun.org` or `AWS SES` | Email notifications (required) |
| **SMTP Username** | `postmaster@example.com` | Authenticated sender |
| **SMTP Password** | [secure, from provider] | SMTP authentication |
| **GitHub OAuth App** (optional) | Client ID + secret | Single-sign-on for authors |
| **Backup S3 Bucket** (optional) | `discourse-backups` on AWS/DigitalOcean Spaces | Automatic backup storage |
| **S3 Credentials** (optional) | Access key + secret key | Backup authentication |

### 1.3 SMTP Email Setup

Discourse **requires** outbound email for:
- Account activation emails
- Password reset emails
- Post notification emails
- Admin alerts

**Free/Cheap SMTP Options**:

| Provider | Limit | Cost | Setup Time |
|----------|-------|------|-----------|
| Brevo (Sendinblue) | 300/day | Free | 5 min (just account + API key) |
| Mailgun | 100/day free trial | $20/month standard | 10 min (domain verification) |
| AWS SES | 200/day (sandbox) | $0.10 per email | 15 min (identity verification) |
| DigitalOcean Spaces + Spaces Email | Unlimited | $1/month spaces | 20 min (domain DNS) |

**Recommended**: Brevo (300/day free, no credit card required for free tier)

1. Go to https://www.brevo.com/products/transactional-email/
2. Sign up with email
3. Verify email
4. Go to Settings → SMTP & API → SMTP
5. Copy SMTP credentials:
   - Host: `smtp-relay.brevo.com`
   - Port: `587`
   - Username: `your-email@example.com`
   - Password: (API key, from account settings)

### 1.4 GitHub OAuth Setup (Recommended for SSO)

Optional but recommended for easy author onboarding:

1. Go to GitHub → Settings → Developer Settings → OAuth Apps
2. New OAuth App:
   - Application name: "Systems Resilience Collab"
   - Homepage URL: `https://forum.example.com`
   - Authorization callback URL: `https://forum.example.com/auth/github/callback`
3. Copy:
   - Client ID
   - Client Secret (save securely)
4. Later: configure in Discourse admin panel (Part 7.2)

---

## Part 2: Installation Setup (30 Minutes)

### 2.1 Create Deployment Directory

```bash
# Create directory for Discourse
sudo mkdir -p /var/discourse
sudo chown -R $(whoami):$(whoami) /var/discourse
cd /var/discourse

# Clone official Discourse Docker repository
git clone https://github.com/discourse/discourse_docker.git .

# Create containers directory (holds your app.yml)
mkdir -p containers

# Create backups directory
mkdir -p backups

echo "✓ Discourse deployment directory initialized"
ls -la /var/discourse/
```

### 2.2 DNS Configuration

**Before deploying**: Ensure DNS points to your server.

At your domain registrar (GoDaddy, Namecheap, AWS Route53, etc.):

```
Record Type: A
Host: forum.example.com
Points To: 203.0.113.42  (your public IP)
TTL: 300 (5 minutes)
```

**Verify DNS Resolution**:

```bash
# From your local machine
nslookup forum.example.com
# Should return your public IP

# From server itself
dig forum.example.com
# Should return your public IP

# If DNS not resolving after 5 min, troubleshoot at registrar
# (DNS propagation can take 1-5 minutes with TTL 300)
```

### 2.3 Create app.yml Configuration File

```bash
# Copy the official Discourse standalone template
cp /var/discourse/samples/standalone.yml /var/discourse/containers/app.yml

# Edit with your values
nano /var/discourse/containers/app.yml
```

**Complete app.yml** (replace all REPLACE_* values):

```yaml
## /var/discourse/containers/app.yml
## Discourse standalone Docker configuration
## Phase 5 systems-resilience project

version: tests-passed

templates:
  - "templates/postgres.14.template.yml"
  - "templates/redis.template.yml"
  - "templates/web.template.yml"
  - "templates/web.ratelimit.template.yml"

expose:
  - "80:80"
  - "443:443"

params:
  db_default_text_search_config: "pg_catalog.english"
  db_shared_buffers: "2048MB"
  db_work_mem: "10MB"
  db_maintenance_work_mem: "256MB"
  
  db_name: discourse
  db_username: discourse
  db_password: "REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_A"
  db_host: localhost
  db_port: 5432

  redis_shared_buffers: "512MB"

  smtp_address: "REPLACE_WITH_SMTP_HOST"
  smtp_port: 587
  smtp_user_name: "REPLACE_WITH_SMTP_USERNAME"
  smtp_password: "REPLACE_WITH_SMTP_PASSWORD"
  smtp_enable_start_tls: true
  smtp_authentication: login

  discourse_hostname: forum.example.com
  discourse_developer_emails: 'admin@example.com'
  
  discourse_smtp_address: "REPLACE_WITH_SMTP_HOST"
  discourse_smtp_port: 587
  discourse_smtp_user_name: "REPLACE_WITH_SMTP_USERNAME"
  discourse_smtp_password: "REPLACE_WITH_SMTP_PASSWORD"
  discourse_smtp_enable_start_tls: true
  
  discourse_notification_email: 'noreply@example.com'
  discourse_reply_by_email_address: 'replies+%{reply_key}@example.com'

  letsencrypt_account_email: admin@example.com
  letsencrypt_dir: /shared/ssl/letsencrypt

  discourse_force_https: true
  discourse_enable_cors: false
  discourse_cors_origins: ""

  discourse_max_upload_size_kb: 102400
  discourse_max_attachment_size_kb: 51200

  discourse_default_locale: en

  discourse_authentication_types: "email oauth2_basic"

  discourse_enable_local_logins: true

  discourse_enable_facebook_logins: false
  discourse_enable_twitter_logins: false
  discourse_enable_google_logins: false
  discourse_enable_github_logins: true

  discourse_github_client_id: "REPLACE_WITH_GITHUB_CLIENT_ID_OR_LEAVE_BLANK"
  discourse_github_client_secret: "REPLACE_WITH_GITHUB_CLIENT_SECRET_OR_LEAVE_BLANK"

  discourse_backup_location: 's3'
  discourse_s3_bucket: 'REPLACE_WITH_S3_BUCKET_OR_LEAVE_BLANK'
  discourse_s3_region: 'us-east-1'
  discourse_s3_access_key_id: 'REPLACE_WITH_S3_KEY_OR_LEAVE_BLANK'
  discourse_s3_secret_access_key: 'REPLACE_WITH_S3_SECRET_OR_LEAVE_BLANK'
  discourse_s3_cdn_url: ''

  discourse_enable_s3_uploads: false
  discourse_s3_upload_bucket: ''

run:
  - replace:
      filename: /etc/nginx/conf.d/discourse.conf
      from: /server_name.+$/
      to: server_name forum.example.com;

  - replace:
      filename: /etc/nginx/conf.d/discourse.conf
      from: /client_max_body_size.+$/
      to: client_max_body_size 20m;

volumes:
  - volume:
      host: /var/discourse/shared/standalone
      guest: /shared
  - volume:
      host: /var/discourse/shared/standalone/log/var-log
      guest: /var/log

hooks:
  before_code:
    - exec: echo "Beginning Discourse setup for forum.example.com..."
    - exec: mkdir -p /shared/ssl/letsencrypt

env:
  LANG: en_US.UTF-8
  DISCOURSE_DB_SOCKET: ""
  DISCOURSE_REDIS_SLAVE_HOST: ""
  DISCOURSE_REDIS_SLAVE_PORT: ""
```

**Key Configuration Values Explained**:

| Parameter | Example | Purpose |
|-----------|---------|---------|
| `discourse_hostname` | `forum.example.com` | Primary domain, used in URLs |
| `discourse_developer_emails` | `admin@example.com` | Initial admin account email |
| `smtp_address` | `smtp-relay.brevo.com` | Email provider SMTP host |
| `letsencrypt_account_email` | `admin@example.com` | Let's Encrypt certificate notifications |
| `discourse_max_upload_size_kb` | `102400` | Max file size (100 MB) |
| `discourse_enable_github_logins` | `true` | Enable OAuth via GitHub |
| `discourse_backup_location` | `s3` or `local` | Where to store backups |

### 2.4 Secrets Management

Create a separate secrets file (not in git):

```bash
cat > /var/discourse/secrets.env << 'SECRETSEOF'
###############################################################################
# Discourse Secrets — DO NOT COMMIT TO GIT
###############################################################################

# Database password (32+ random chars)
DB_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_A

# SMTP credentials
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_USERNAME=your-email@example.com
SMTP_PASSWORD=REPLACE_WITH_BREVO_API_KEY

# Email notification address
NOTIFICATION_EMAIL=noreply@example.com
REPLY_BY_EMAIL=replies+%{reply_key}@example.com

# Admin account (first login)
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_B

# GitHub OAuth (optional)
GITHUB_CLIENT_ID=REPLACE_IF_USING_GITHUB_SSO
GITHUB_CLIENT_SECRET=REPLACE_IF_USING_GITHUB_SSO

# AWS S3 Backups (optional)
S3_BUCKET=discourse-backups
S3_REGION=us-east-1
S3_ACCESS_KEY=REPLACE_IF_USING_S3
S3_SECRET_KEY=REPLACE_IF_USING_S3

###############################################################################
SECRETSEOF

chmod 600 /var/discourse/secrets.env
echo "✓ Secrets file created (keep secure)"
```

---

## Part 3: Docker Deployment (30 Minutes)

### 3.1 Build and Start Discourse

```bash
cd /var/discourse

# Verify app.yml is configured correctly
echo "=== Checking app.yml configuration ==="
grep -E "discourse_hostname|discourse_developer_emails|smtp_address" containers/app.yml

# Build the Discourse container (this takes 5-10 minutes)
echo "Building Discourse Docker image (first time only)..."
./launcher bootstrap app

# This will:
# 1. Build Docker image from templates
# 2. Create PostgreSQL database
# 3. Create Redis instance
# 4. Initialize Discourse Rails app
# 5. Request TLS certificate from Let's Encrypt

# Expected output includes:
# "Compiling assets... (takes 5-10 minutes)"
# "Let's Encrypt certificate issued successfully"
# "Discourse is now running"
```

**If build fails**:

```bash
# View detailed logs
./launcher logs app | tail -100

# Common issues:
# - "Connection refused": DNS not resolving, wait 2-5 minutes for propagation
# - "Certificate failed": Let's Encrypt error, check `letsencrypt_account_email`
# - "SMTP connection failed": verify SMTP credentials in app.yml

# Retry after fixing
./launcher bootstrap app
```

### 3.2 Start Discourse Service

```bash
# Start the container (if bootstrap completed but not auto-started)
./launcher start app

# Verify it's running
./launcher status app
# Expected: "Container app is running"

# Wait for port 80/443 to be listening
sleep 10
curl -I http://localhost/
# Expected: HTTP/1.1 301 (redirect to HTTPS)

curl -k https://localhost/
# Expected: HTML response with Discourse page
```

### 3.3 Health Verification

```bash
# Check service is fully initialized
docker ps | grep discourse_app

# View logs for any errors
./launcher logs app | grep -E "ERROR|error" | head -10

# Test web access
curl -k https://localhost/ | grep -o "<title>.*</title>"
# Expected: <title>Discourse</title> or similar

# Test from external machine (SSH tunnel)
# From your laptop:
# ssh -L 443:localhost:443 user@server.com
# Then open https://localhost in browser

# Direct test (if server is public)
curl -k https://forum.example.com/ | head -20
```

---

## Part 4: Post-Deployment Configuration (1-2 Hours)

### 4.1 Initial Admin Access

```bash
# Get the password reset link
./launcher logs app | grep "Admin username"
./launcher logs app | grep "Password:"

# OR: Go to web interface at https://forum.example.com
# Click "Login" → "Create Account"
# Email: admin@example.com (from app.yml)
# Complete signup and email verification
```

**Access Admin Panel**:

1. Navigate to `https://forum.example.com/admin`
2. Login with credentials created during setup
3. You'll see the admin dashboard

### 4.2 Configure GitHub OAuth (Optional but Recommended)

In Discourse Admin Panel:

1. **Settings** → **Login** → **Enable GitHub Logins**: `enabled`
2. **Settings** → **GitHub Logins**:
   - GitHub Client ID: (from Part 1.4)
   - GitHub Client Secret: (from Part 1.4)
3. Click **Save**

Test OAuth:
- Logout of Discourse
- Click "Sign up with GitHub"
- Authorize and verify login works

### 4.3 Configure Categories and Initial Content

**Create Categories for Phase 5**:

1. **Admin** → **Categories**
2. Create:
   - **Wave 1 Documents** (public, everyone can read/reply)
   - **Wave 1 Discussion** (public, for feedback threads)
   - **General** (for off-topic, already exists)
   - **Private: Core Team** (private, only admins)

**Create Initial Announcement Post**:

1. **Admin** → **New Post** (or just create from homepage)
2. Category: **Wave 1 Documents**
3. Title: "Phase 5 Wave 1 — Initial Briefing"
4. Content: Wave 1 document text (or embed via file attachment)
5. Make it a "pinned" post (sticky, appears at top)

### 4.4 User Trust Levels Configuration

Discourse has automatic trust levels (0-4) that grant permissions:

- **TL0** (new): Read-only access
- **TL1** (basic): Can post in most categories
- **TL2** (member): Can use more features
- **TL3** (regular): Can moderate flags
- **TL4** (leader): Can edit/delete others' posts

**Configure Promotion Criteria**:

1. **Admin** → **Site Settings** → **Trust Levels**
2. Adjust thresholds (defaults are usually good):
   - TL0 → TL1: 5 posts, 30 min total time
   - TL1 → TL2: 20 posts, 3 days
   - TL2 → TL3: 50 posts, 100 days, 20% read
3. Click **Save**

**Create Initial Test Users**:

```bash
# Create test users (for verification)
./launcher enter app

# Inside container, run Rails console
cd /var/www/discourse
RAILS_ENV=production rails c

# Create user
user = User.create!(
  email: 'author1@example.com',
  username: 'author1',
  password: 'temp_password_123',
  active: true,
  approved: true
)

# Make moderator (optional)
user.grant_moderation!
user.save

# Exit
exit
exit
```

### 4.5 Email Notification Settings

**Verify SMTP is working**:

```bash
# Inside container
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rails c

# Send test email
User.find_by(username: 'admin').update(email: 'admin@example.com')
SystemMessage.create(type: 'welcome_user', user_id: User.first.id)
Jobs::SendEmail.new.execute(user_id: User.first.id, type: 'system_message')

# Check logs for delivery confirmation
exit
exit

./launcher logs app | grep "mail" | tail -20
```

**Configure Email Settings** (Admin → Settings → Email):

- `notification_email`: noreply@example.com
- `reply_by_email_address`: replies+%{reply_key}@example.com
- `disable_emails`: "no"
- `email_digest_min_threshold`: 1 (send digest for 1+ new posts)

---

## Part 5: Integration with Wave 1 Documents

### 5.1 Publishing Wave 1 Documents to Discourse

**Option A: Forum Posts** (recommended for discussion):

1. Create category: "Wave 1 Documents"
2. For each Wave 1 document:
   - Click "Create New Topic"
   - Paste document content as post body
   - Or: upload .md file as attachment, with summary as post text
   - Enable "Pin this topic" if it's critical
3. Authors can reply with questions/feedback

**Option B: Discourse Wiki** (alternative, read-only):

1. Create "Docs" category (private, admins-only)
2. Each document is a topic
3. Toggle "Make this topic a wiki" (allows all TL2+ to edit)
4. Pin at top of category

**Option C: GitHub Pages Integration** (external storage):

1. Keep Wave 1 documents on GitHub Pages
2. Post summary + link in Discourse
3. Embed iframe (if GitHub Pages supports embedding)
4. Use Discourse REST API to sync content (advanced)

**Recommended for Phase 5**: **Option A** (forum posts)
- Easier to moderate
- Better for discussion
- Authors can ask questions inline
- All feedback in one place

### 5.2 REST API for Content Sync

**Discourse API Key Setup**:

1. **Admin** → **API Keys**
2. Create new:
   - User: System (or specific user)
   - Description: "Phase 5 Automation"
   - Scope: "admin"
   - Save
3. Copy API key

**Example: Create Post via API**

```bash
API_KEY="your-api-key-from-admin"
FORUM_URL="https://forum.example.com"

# Create a post in Wave 1 Documents category
curl -X POST "${FORUM_URL}/posts.json" \
  -H "Api-Key: ${API_KEY}" \
  -H "Api-Username: system" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Wave 1: Individual-Scale Resilience Toolkit",
    "raw": "# Document Body\n\nMarkdown content here...",
    "category": 3,
    "skip_validations": false
  }'
```

**Example: List Posts in Category**

```bash
curl "${FORUM_URL}/c/wave-1-documents/3/l/latest.json" \
  -H "Api-Key: ${API_KEY}"
```

(See Discourse API docs at `https://docs.discourse.org/`)

---

## Part 6: Backup & Disaster Recovery

### 6.1 Automated Backups

**Configure S3 Backups** (optional but recommended):

```bash
# Create AWS S3 bucket (or use DigitalOcean Spaces)
aws s3 mb s3://discourse-backups-resilience

# In app.yml, set:
discourse_backup_location: 's3'
discourse_s3_bucket: 'discourse-backups-resilience'
discourse_s3_region: 'us-east-1'
discourse_s3_access_key_id: 'YOUR_AWS_KEY'
discourse_s3_secret_access_key: 'YOUR_AWS_SECRET'

# Rebuild to apply
./launcher rebuild app
```

**Enable Automatic Backups** (Admin → Settings → Backups):

- `backup_location`: s3 (or local)
- `backup_frequency`: daily (24 hours)
- `backup_with_uploads`: true
- `max_backup_size_gb`: 50

**Manual Backup**:

```bash
./launcher enter app
cd /var/www/discourse

# Create backup
RAILS_ENV=production rake 'backup:create'
# Wait for "Backup created successfully"

# List backups
RAILS_ENV=production rake 'backup:list'

# Backup will be stored in:
# /shared/backups/default/ (local)
# OR S3 bucket (if configured)
```

### 6.2 Disaster Recovery

**Restore from Backup**:

```bash
cd /var/discourse

# Stop container
./launcher stop app

# Restore from backup
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rake 'backup:restore[backup-name-20260604.tar.gz]'

# Start container
./launcher start app

# Verify restore
./launcher logs app | grep "restore"
```

---

## Part 7: Operational Runbooks

### 7.1 Daily Operations Checklist

```bash
# Run daily (automated or manual)
echo "=== Daily Discourse Operational Check ==="

# 1. Service health
./launcher status app
# Expected: "Container app is running"

# 2. Disk space (alert if <20% free)
df -h /var/discourse/

# 3. Recent errors in logs
./launcher logs app | grep -i ERROR | tail -5

# 4. Test web access
curl -k https://forum.example.com/
# Expected: HTTP/2 200 or 301 redirect

# 5. Check backups (verify one completed today)
ls -lh /var/discourse/shared/standalone/backups/default/ | tail -1
```

### 7.2 Weekly Maintenance

```bash
# Run weekly (e.g., Sunday 01:00 UTC)

# 1. Update Discourse (brings security patches + features)
cd /var/discourse
./launcher rebuild app
# Takes 10-15 minutes, Discourse restarts after

# 2. Review admin dashboard for security issues
# Admin → Security → "View all security issues"
# Apply recommended patches

# 3. Review trust level promotions (TL0→TL1 escalation)
# Admin → Users → Automatic Trust Level Promotion
```

### 7.3 Monthly Maintenance

```bash
# Run monthly (e.g., first Sunday, 00:00 UTC)

# 1. Full backup audit
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rake backup:list
exit

# 2. Database maintenance
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rake db:maintenance:vacuum
exit

# 3. System package updates
sudo apt-get update && sudo apt-get upgrade -y

# 4. Review admin settings for outdated configs
# Admin → Settings → find deprecated settings
```

---

## Part 8: Monitoring & Troubleshooting

### 8.1 Check Service Logs

```bash
# View all logs
./launcher logs app | tail -100

# Follow logs in real-time
./launcher logs app -f

# Search for specific errors
./launcher logs app | grep -i "error\|fail\|critical"

# View specific service logs (inside container)
./launcher enter app
tail -100 /var/log/rails/production.log
tail -100 /var/log/postgres/
tail -100 /var/log/nginx/error.log
exit
```

### 8.2 Common Issues & Solutions

**Issue: "Connection refused" when accessing site**

```bash
# Check if container is running
./launcher status app

# If not running, restart
./launcher start app

# Wait 30 seconds, then test
sleep 30
curl -k https://localhost/

# Check logs
./launcher logs app | tail -20
```

**Issue: "503 Service Unavailable" or "Bad Gateway"**

```bash
# Usually means Puma (Rails) crashed or is restarting
# Wait 30-60 seconds for recovery

# Check status
./launcher status app

# Force restart if hung
./launcher restart app

# View error logs
./launcher logs app | grep -i "error" | tail -20
```

**Issue: SMTP/Email not sending**

```bash
# Verify SMTP config in app.yml
grep -E "smtp_|discourse_smtp" /var/discourse/containers/app.yml

# Test SMTP connection
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rails c

# In Rails console:
Mail.deliver_now do
  from 'noreply@example.com'
  to 'test@example.com'
  subject 'Test'
  body 'Test email'
end

# Should see "Net::SMTPAuthenticationError" if credentials wrong
# Should see "250 OK" if successful
exit
exit

# View mail queue
./launcher enter app
cd /var/www/discourse
RAILS_ENV=production rake mail:logs
exit
```

**Issue: Out of disk space**

```bash
# Check disk usage
du -sh /var/discourse/

# Find large files
find /var/discourse -size +1G

# Common culprits:
# - /shared/backups/default/ (old backups)
# - /shared/uploads/ (user uploads)

# Remove old backups manually
rm /var/discourse/shared/standalone/backups/default/backup-20260501*.tar.gz

# Or configure automatic cleanup (Admin → Settings → Backups)
```

**Issue: GitHub OAuth login failing**

```bash
# Verify OAuth credentials in app.yml
grep -E "github" /var/discourse/containers/app.yml

# Ensure callback URL matches:
# https://forum.example.com/auth/github/callback

# Test OAuth manually:
./launcher logs app | grep -i "github\|oauth"

# Restart container if config changed
./launcher rebuild app
```

---

## Part 9: Timeline & Success Criteria

### Deployment Timeline

| Phase | Task | Estimated Time | Success Criteria |
|-------|------|-----------------|------------------|
| 1 | Pre-flight checklist + DNS config | 20 min | DNS resolves, ports accessible |
| 2 | Installation setup + app.yml config | 20 min | Docker images pulled, app.yml created |
| 3 | Docker build + deployment | 20 min | Container running, TLS cert issued |
| 4 | Post-deployment config | 30 min | Admin access works, categories created |
| 5 | Testing + user creation | 20 min | 10 test users created, Wave 1 post published |
| **TOTAL** | | **2-2.5 hours** | **Platform ready for authors by June 5 13:00 UTC** |

### Success Verification Checklist

- [ ] Platform accessible at https://forum.example.com with valid TLS certificate
- [ ] Admin login works (from admin email + credentials)
- [ ] HTTPS certificate from Let's Encrypt (browser shows valid cert)
- [ ] 10 test user accounts created
- [ ] GitHub OAuth login tested and working
- [ ] "Wave 1 Documents" category created and visible
- [ ] Wave 1 sample document posted as pinned topic
- [ ] Email notifications working (verify with test user)
- [ ] File upload tested (PDF or image)
- [ ] Category permissions verified (test TL0 user permissions)
- [ ] Backup process runs without errors
- [ ] All services start cleanly after `./launcher restart app`

---

## Part 10: Advanced Configuration

### 10.1 Custom Domain Email (Reply-by-Email)

To enable authors to reply by email:

1. Setup SMTP for outbound (already done in Part 1)
2. Setup mail service for inbound (POP3 or webhook)
3. Configure in Admin → Settings:
   - `reply_by_email_enabled`: true
   - `reply_by_email_address`: replies+%{reply_key}@example.com
   - `reply_by_email_sender`: noreply@example.com

Note: requires setting up email alias on mail server (complex; skip for Phase 5).

### 10.2 Plugins for Phase 5

**Useful Plugins** (optional enhancements):

```bash
# Add to app.yml under "hooks: before_code:"
- git clone https://github.com/discourse/discourse-github-linkback.git plugins/discourse-github-linkback

# Then rebuild
./launcher rebuild app
```

**Recommended Plugins**:
- `discourse-github-linkback`: Link Discourse topics to GitHub issues
- `discourse-poll`: Add polls to posts
- `discourse-markdown-tables`: Better table formatting
- `discourse-api`: Enhanced REST API endpoints

### 10.3 Scaling to 300+ Users

For Phase 6 expansion:

1. Increase RAM allocation in app.yml:
   - `db_shared_buffers`: 4096MB
   - `redis_shared_buffers`: 1024MB

2. Add more CPUs (if available)

3. Consider external PostgreSQL (for very large databases)

4. Monitor performance:
   ```bash
   ./launcher logs app | grep "slow"
   ```

---

## Part 11: Comparison with Nextcloud+Matrix

| Aspect | Discourse | Nextcloud+Matrix |
|--------|-----------|------------------|
| **Deployment Time** | 2-3 hours | 4-6 hours |
| **Resource Usage** | 8 GB RAM | 16 GB RAM |
| **Offline Document Editing** | No (web-only) | Yes (desktop client + browser cache) |
| **Real-time Messaging** | Direct messages (asynchronous) | Matrix (synchronous + E2E encryption) |
| **File Collaboration** | File upload/download only | True collaborative editing (OnlyOffice) |
| **Discussion Model** | Forum threads (threaded) | Chat rooms (flat stream) |
| **Governance** | Trust levels (automatic) | Manual room permissions |
| **Setup Complexity** | Simple (one container) | Complex (5+ services) |
| **Learning Curve** | Low (familiar forum UI) | Medium (federation concepts) |

**Choose Discourse if**:
- Prefer forum discussion style
- Faster deployment critical (deadline pressure)
- Authors have reliable internet
- Lower resource budget
- Simpler operations preferred

**Choose Nextcloud+Matrix if**:
- Offline authoring needed
- E2E encryption critical
- Real-time editing preferred
- Future federation important
- Willing to invest in complexity for capabilities

---

## Final Notes

### Communication Plan for Phase 5 Launch

**June 4 18:00 UTC**: 
- Platform deployed and tested
- Admin panel verified working

**June 5 08:00 UTC**:
- Wave 1 documents published to forum
- Author recruitment email sent with login instructions
- GitHub OAuth tested

**June 5 13:00 UTC**:
- Live author recruitment begins
- Support team on-call for login issues

### Support Escalation

**Tier 1** (Author-facing issues):
- Password reset: Admin → Users → "Reset Password"
- Account creation: Send signup link
- Permission issues: Check user trust level (Admin → Users)

**Tier 2** (Technical issues):
- Service down: `./launcher restart app`
- Memory full: Check disk space, clean backups
- SMTP error: Review app.yml, test credentials

**Tier 3** (Infrastructure):
- Database corruption: restore from backup
- Hardware failure: provision new server, restore backup
- Security incident: review logs, isolate if needed

---

**Document Status**: PRODUCTION-READY  
**Last Updated**: 2026-06-04  
**For support**: See troubleshooting in Part 8, or refer to official docs at meta.discourse.org
