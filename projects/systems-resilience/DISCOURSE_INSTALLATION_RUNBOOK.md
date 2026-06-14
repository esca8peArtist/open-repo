---
title: "Discourse Installation Runbook — Execute Today"
project: systems-resilience
platform: "Discourse (Official Launcher + Bitnami ARM64 fallback)"
created: 2026-06-14
host: "raspby1 — 100.120.18.84 (Tailscale)"
status: "READY TO EXECUTE"
estimated_duration: "2–3 hours"
prerequisites: "SMTP credentials + hostname decision (see PLATFORM_DECISION_MATRIX_WITH_RUNBOOKS.md)"
---

# Discourse Installation Runbook
## Execute on raspby1 — June 14-15, 2026

**Time estimate**: 2–3 hours from start to live platform  
**Prerequisite**: Provide SMTP credentials and hostname before starting (see Prerequisites below)

---

## Prerequisites

Before starting, confirm or provide the following:

- [ ] **SMTP credentials** — host, port, username, password
  - OR: confirm GitHub OAuth is acceptable (eliminates SMTP dependency for registration)
  - Free SMTP: Brevo (`smtp-relay.brevo.com`, port 587, free tier 300 emails/day)
  - Gmail SMTP: `smtp.gmail.com`, port 587, use app password (not main password)
- [ ] **Hostname decision** — one of:
  - `raspby1.your-tailnet.ts.net` (Tailscale MagicDNS — recommended, get from `tailscale status`)
  - `100.120.18.84` (raw IP — works, browser will warn about self-signed cert)
  - `forum.yourdomain.com` (public domain — requires DNS A record pointing to Pi's public IP)
- [ ] **Admin email** — the email address that gets admin privileges
- [ ] SSH access to raspby1 is working

---

## Phase 1: System Check (15 min)

```bash
# SSH to raspby1
ssh awank@raspby1  # or ssh awank@100.70.184.84

# Confirm architecture (must be aarch64)
uname -m
# Expected: aarch64

# Confirm Docker is operational
docker --version
# Expected: Docker 20.x or later

# Confirm disk space (need 10 GB minimum; we have ~189 GB)
df -h /
# Look for Avail column — expect 100+ GB

# Confirm ports 80 and 443 are free
sudo ss -tlnp | grep -E ':80|:443'
# Expected: no output (no services on those ports yet)

# If something is using port 80 (e.g., nginx, apache):
sudo ss -tlnp | grep ':80'
# Identify process, stop it:
# sudo systemctl stop nginx && sudo systemctl disable nginx

# Check Tailscale hostname (for TLS cert later)
tailscale status --json | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Tailscale IP:', d['Self']['TailscaleIPs'][0])
print('MagicDNS name:', d['Self']['DNSName'].rstrip('.'))
"
# Note down the MagicDNS name for use as DISCOURSE_HOSTNAME
```

**Phase 1 complete when**: `uname -m` = aarch64, Docker responds, ports free, Tailscale hostname noted.

---

## Phase 2: Launcher Setup (15 min)

```bash
# Create discourse directory
sudo mkdir -p /var/discourse
sudo chown $USER:$USER /var/discourse

# Clone official launcher
git clone https://github.com/discourse/discourse_docker.git /var/discourse
cd /var/discourse

# Verify clone
ls /var/discourse/launcher /var/discourse/samples/standalone.yml
# Both should exist

# Create containers directory
mkdir -p /var/discourse/containers

# Install yaml validation tool
sudo apt-get update -y && sudo apt-get install -y python3-yaml
```

---

## Phase 3: Configure app.yml (30 min)

```bash
# Copy template
cp /var/discourse/samples/standalone.yml /var/discourse/containers/app.yml
```

Open `/var/discourse/containers/app.yml` and replace the entire contents with the configuration below. Fill in your actual values for each `REPLACE_*` placeholder:

```bash
# Open in editor
nano /var/discourse/containers/app.yml
```

Paste the following, replacing every `REPLACE_*` with your actual values:

```yaml
## /var/discourse/containers/app.yml
## Systems Resilience Community — Pi5 (8GB ARM64)
## Fill in all REPLACE_* values before saving

templates:
  - "templates/postgres.template.yml"
  - "templates/redis.template.yml"
  - "templates/web.template.yml"
  - "templates/web.ratelimited.template.yml"

expose:
  ## CRITICAL: Use Tailscale IP (100.120.18.84) — NEVER 0.0.0.0
  - "100.120.18.84:80:80"
  - "100.120.18.84:443:443"

params:
  db_default_text_search_config: "pg_catalog.english"
  db_shared_buffers: "512MB"
  db_work_mem: "64MB"

env:
  LANG: en_US.UTF-8
  RAILS_ENV: production

  ## Hostname: use your Tailscale MagicDNS name (e.g. raspby1.tail1234.ts.net)
  ## OR use 100.120.18.84 for IP-only (self-signed cert)
  DISCOURSE_HOSTNAME: "REPLACE_WITH_HOSTNAME_OR_TAILSCALE_NAME"

  ## Admin email — this account gets admin on first login
  DISCOURSE_DEVELOPER_EMAILS: "REPLACE_WITH_YOUR_EMAIL"

  ## SMTP — remove these lines if using GitHub OAuth only
  DISCOURSE_SMTP_ADDRESS: "REPLACE_SMTP_HOST"
  DISCOURSE_SMTP_PORT: 587
  DISCOURSE_SMTP_USER_NAME: "REPLACE_SMTP_USERNAME"
  DISCOURSE_SMTP_PASSWORD: "REPLACE_SMTP_PASSWORD"
  DISCOURSE_SMTP_ENABLE_START_TLS: true
  DISCOURSE_SMTP_AUTHENTICATION: login
  DISCOURSE_NOTIFICATION_EMAIL: "noreply@REPLACE_YOUR_DOMAIN"
  DISCOURSE_CONTACT_EMAIL: "REPLACE_WITH_YOUR_EMAIL"

  DISCOURSE_TITLE: "Systems Resilience Community"

  ## Pi5 performance: 2 workers is correct for 8GB RAM
  UNICORN_WORKERS: 2
  UNICORN_TIMEOUT: 60

  ## Rate limits (generous for trusted community)
  DISCOURSE_MAX_REQS_PER_IP_PER_MINUTE: 300
  DISCOURSE_MAX_REQS_PER_IP_PER_10_SECONDS: 60

  ## Set true to require admin approval for new accounts (optional)
  DISCOURSE_MUST_APPROVE_USERS: false

  ## Uncomment ONLY if you have a public domain with DNS A record:
  # LETSENCRYPT_ACCOUNT_EMAIL: "REPLACE_WITH_YOUR_EMAIL"

volumes:
  - volume:
      host: /var/discourse/shared/standalone
      guest: /shared
  - volume:
      host: /var/discourse/shared/standalone/log/var-log
      guest: /var/log

hooks:
  after_code:
    - exec:
        cd: $home
        cmd:
          - git clone https://github.com/discourse/docker_manager.git plugins/docker_manager
```

Save the file, then validate:

```bash
# Validate YAML — must return no errors
python3 -c "
import yaml
with open('/var/discourse/containers/app.yml') as f:
    data = yaml.safe_load(f)
print('YAML OK')
print('Hostname:', data['env']['DISCOURSE_HOSTNAME'])
print('SMTP host:', data['env']['DISCOURSE_SMTP_ADDRESS'])
print('Unicorn workers:', data['env']['UNICORN_WORKERS'])
"

# Confirm no unreplaced placeholders remain
grep "REPLACE_" /var/discourse/containers/app.yml
# Expected: no output — if anything prints, fix those values before proceeding
```

---

## Phase 4: Bootstrap (15–25 min, Pi5 ARM64)

```bash
cd /var/discourse

# Start bootstrap — this compiles Discourse from source on ARM64
# Takes 15–25 minutes on Pi5 — do not interrupt
sudo ./launcher bootstrap app 2>&1 | tee /tmp/discourse-bootstrap.log

# In a second terminal, monitor progress:
# tail -f /tmp/discourse-bootstrap.log
```

**What happens during bootstrap**: Docker pulls base image (~1.5 GB), installs Ruby gems, compiles JavaScript assets, runs database migrations. This is the longest step. The Pi5 will run warm (87–88°C) — this is expected.

**Expected end of bootstrap output**:
```
Runtime error: ...  (final warning lines are normal — ignore them)
```

Check exit code:
```bash
echo "Bootstrap exit code: $?"
# Expected: 0 (success)
```

### If Bootstrap Fails (ARM64 Fallback)

If you see `exec format error` or the bootstrap takes more than 35 minutes:

```bash
# Check for architecture errors
grep -i "exec format\|arm\|amd64\|cannot execute" /tmp/discourse-bootstrap.log | tail -10
```

If architecture errors appear, switch to Bitnami (pre-built ARM64, no compilation):

```bash
sudo mkdir -p /opt/discourse-bitnami
cd /opt/discourse-bitnami

# Create docker-compose.yml with your values (replace all REPLACE_ placeholders):
cat > docker-compose.yml << 'BITNAMI_EOF'
version: '3.8'
services:
  postgresql:
    image: docker.io/bitnami/postgresql:16
    volumes:
      - postgresql_data:/bitnami/postgresql
    environment:
      POSTGRESQL_USERNAME: discourse
      POSTGRESQL_PASSWORD: REPLACE_POSTGRES_PASSWORD
      POSTGRESQL_DATABASE: discourse
    ports:
      - "127.0.0.1:5432:5432"
  redis:
    image: docker.io/bitnami/redis:7.2
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - redis_data:/bitnami/redis/data
    ports:
      - "127.0.0.1:6379:6379"
  discourse:
    image: docker.io/bitnami/discourse:3
    ports:
      - "100.120.18.84:80:3000"
      - "100.120.18.84:443:3001"
    depends_on:
      - postgresql
      - redis
    volumes:
      - discourse_data:/bitnami/discourse
    environment:
      DISCOURSE_HOST: REPLACE_HOSTNAME
      DISCOURSE_DATABASE_HOST: postgresql
      DISCOURSE_DATABASE_USER: discourse
      DISCOURSE_DATABASE_PASSWORD: REPLACE_POSTGRES_PASSWORD
      DISCOURSE_DATABASE_NAME: discourse
      DISCOURSE_REDIS_HOST: redis
      DISCOURSE_SMTP_HOST: REPLACE_SMTP_HOST
      DISCOURSE_SMTP_PORT: "587"
      DISCOURSE_SMTP_USER: REPLACE_SMTP_USER
      DISCOURSE_SMTP_PASSWORD: REPLACE_SMTP_PASSWORD
      DISCOURSE_SITE_NAME: "Systems Resilience Community"
      DISCOURSE_USERNAME: admin
      DISCOURSE_PASSWORD: REPLACE_ADMIN_PASSWORD
      DISCOURSE_EMAIL: REPLACE_ADMIN_EMAIL
  sidekiq:
    image: docker.io/bitnami/discourse:3
    depends_on:
      - discourse
    volumes:
      - discourse_data:/bitnami/discourse
    command: /opt/bitnami/scripts/discourse-sidekiq/run.sh
    environment:
      DISCOURSE_HOST: REPLACE_HOSTNAME
      DISCOURSE_DATABASE_HOST: postgresql
      DISCOURSE_DATABASE_USER: discourse
      DISCOURSE_DATABASE_PASSWORD: REPLACE_POSTGRES_PASSWORD
      DISCOURSE_DATABASE_NAME: discourse
      DISCOURSE_REDIS_HOST: redis
volumes:
  postgresql_data:
  redis_data:
  discourse_data:
BITNAMI_EOF

# Replace all placeholders in the file, then start:
docker compose up -d

# Wait 3–5 minutes for Discourse to initialize
docker compose logs -f discourse
# Look for: "Discourse initialized" or similar startup message
```

Note: If using Bitnami, subsequent commands that reference `sudo ./launcher enter app` become `docker compose exec discourse bash`, and `sudo ./launcher restart app` becomes `docker compose restart discourse`.

---

## Phase 5: Start and SSL (20 min)

```bash
# Start Discourse (official launcher path)
cd /var/discourse
sudo ./launcher start app

# Check status
sudo ./launcher status app
# Expected: "app: up"  (with uptime counter)

# Health check
curl -sk http://100.120.18.84/ | head -5
# Expected: HTML response (may redirect to HTTPS)
```

### SSL — Tailscale HTTPS (Recommended)

```bash
# Issue Tailscale cert for MagicDNS hostname
tailscale_host=$(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
echo "Your Tailscale hostname: $tailscale_host"
sudo tailscale cert "$tailscale_host"
# Cert written to /var/lib/tailscale/certs/

# Update hostname in app.yml
sed -i "s/REPLACE_WITH_HOSTNAME_OR_TAILSCALE_NAME/$tailscale_host/" /var/discourse/containers/app.yml

# Rebuild to apply new hostname (10–15 min on Pi5)
sudo ./launcher rebuild app
```

### SSL — Self-Signed (Fallback if Tailscale Cert Fails)

```bash
# Self-signed cert is generated automatically by the launcher
# Users will see a browser warning on first visit; they click "Accept" once
# No additional action needed
```

---

## Phase 6: Admin and Community Setup (45 min)

### 6.1 Complete Admin Setup via Web Wizard

Open a browser to `https://[your-hostname]` and complete the setup wizard. Enter your admin email and set a password.

OR complete via Rails console (if web wizard is not accessible):

```bash
cd /var/discourse
sudo ./launcher enter app
rails c

# Check if admin exists
admin = User.find_by(email: "YOUR_ADMIN_EMAIL")
if admin
    puts "Admin exists: #{admin.username}"
    admin.grant_admin! unless admin.admin?
else
    admin = User.new(email: "YOUR_ADMIN_EMAIL", username: "admin", name: "Admin", password: "STRONG_PASSWORD")
    admin.active = true; admin.approved = true; admin.save!
    admin.grant_admin!
    puts "Admin created: #{admin.username}"
end
exit
```

### 6.2 Configure Automated Backups

```bash
cd /var/discourse && sudo ./launcher enter app
rails c

SiteSetting.backup_frequency = 1        # Daily
SiteSetting.maximum_backups = 14         # Keep 14 days
SiteSetting.backup_with_uploads = true
SiteSetting.enable_backups = true
puts "Backup configured"
exit
```

### 6.3 Trigger First Backup

```bash
cd /var/discourse && sudo ./launcher enter app
rails c
BackupRestore::Backuper.new(User.find_by(admin: true).id, {}).run
puts "Backup running (check /var/discourse/shared/standalone/backups/ in 3 min)"
exit

# Wait 3 minutes, then verify
ls -lah /var/discourse/shared/standalone/backups/default/
# Expected: at least one .gz file
```

### 6.4 Create Community Categories

```bash
cd /var/discourse && sudo ./launcher enter app
rails c

admin_user = User.find_by(admin: true)

[
    { name: "Announcements", color: "F7941D", position: 0 },
    { name: "Phase 5 — Published Research", color: "3AB54A", position: 1 },
    { name: "Discussion", color: "0088CC", position: 2 },
    { name: "Project Coordination", color: "808281", position: 3 },
    { name: "Meta", color: "E45735", position: 4 }
].each do |attrs|
    cat = Category.new(name: attrs[:name], color: attrs[:color], position: attrs[:position], user: admin_user)
    cat.save!
    puts "Created: #{cat.name}"
end
exit
```

### 6.5 Create API Key (for publication automation)

```bash
cd /var/discourse && sudo ./launcher enter app
rails c

key = ApiKey.create!(
    key: SecureRandom.hex(32),
    description: "Phase 5.1 publication automation",
    user: User.find_by(admin: true)
)
puts "API KEY: #{key.key}"
puts "Save this — it cannot be retrieved later"
exit

# Store the key
echo "DISCOURSE_API_KEY=YOUR_KEY_HERE" > /home/awank/.discourse-api-credentials
chmod 600 /home/awank/.discourse-api-credentials
```

### 6.6 Verify SMTP

```bash
cd /var/discourse && sudo ./launcher enter app
rails c
Jobs.enqueue(:test_email, to_address: "YOUR_EMAIL_HERE")
puts "Test email queued — check inbox in 2-3 minutes"
exit
```

If email does not arrive within 5 minutes, check `EmailLog.last(3)` in rails console for error details. Platform still works without SMTP (users just cannot receive email notifications).

---

## Phase 7: Validation (30 min)

```bash
# Load API key
source /home/awank/.discourse-api-credentials
DISCOURSE_URL="https://100.120.18.84"  # or your hostname

# Forum metadata
curl -sk "$DISCOURSE_URL/about.json" | python3 -m json.tool | grep -E '"title"|"version"'

# Categories
curl -sk "$DISCOURSE_URL/categories.json" | \
    python3 -c "
import sys, json
cats = json.load(sys.stdin)['category_list']['categories']
print(f'Categories ({len(cats)}):')
for c in cats:
    print(f'  {c[\"id\"]}: {c[\"name\"]}')
"
# Expected: 5 categories

# Authenticated API check
curl -sk -H "Api-Key: $DISCOURSE_API_KEY" -H "Api-Username: system" \
    "$DISCOURSE_URL/admin/dashboard.json" | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print('Sidekiq queue:', d.get('sidekiq_queued_jobs', 'unknown'))"
# Expected: Sidekiq queue: 0

# Create and delete a test topic via API
test_response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"[TEST DELETE ME] API validation $(date +%s)\",
        \"raw\": \"API post test. Delete after validation.\",
        \"category\": 5
    }")

topic_id=$(echo "$test_response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id', 'ERROR'))")
echo "Test topic created: id=$topic_id"

# Clean up
curl -s -X DELETE "$DISCOURSE_URL/t/$topic_id.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" -H "Api-Username: system"
echo "Test topic deleted"
```

### Concurrent Load Test

```bash
# Test 20 concurrent reads
for i in $(seq 1 20); do
    curl -sk -o /dev/null -w "%{time_total}\n" "$DISCOURSE_URL/about.json" &
done
wait
# Expected: all times < 2.0 seconds
```

---

## Phase 8: External Backup Script (10 min)

```bash
cat > /opt/discourse-backup-external.sh << 'EOF'
#!/bin/bash
set -euo pipefail
BACKUP_DIR="/home/awank/backups/discourse"
DATE=$(date -u +%Y-%m-%d)
LOG="/var/log/discourse-backup.log"
mkdir -p "$BACKUP_DIR/$DATE"
latest=$(ls -t /var/discourse/shared/standalone/backups/default/*.gz 2>/dev/null | head -1)
if [[ -z "$latest" ]]; then
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] WARNING: no backup found" >> "$LOG"
    exit 1
fi
cp "$latest" "$BACKUP_DIR/$DATE/"
cp /var/discourse/containers/app.yml "$BACKUP_DIR/$DATE/app.yml.bak"
find "$BACKUP_DIR" -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null || true
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] External backup complete: $(du -sh "$BACKUP_DIR/$DATE" | cut -f1)" >> "$LOG"
EOF

chmod +x /opt/discourse-backup-external.sh
mkdir -p /home/awank/backups/discourse
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/discourse-backup-external.sh") | crontab -
# Verify cron entry
crontab -l | grep discourse-backup
```

---

## Deployment Complete Checklist

- [ ] `uname -m` returns `aarch64`
- [ ] `sudo ./launcher status app` returns "app: up"
- [ ] `curl -sk https://[hostname]/about.json` returns JSON
- [ ] All 5 categories visible at `/categories.json`
- [ ] Admin account can log in via browser
- [ ] API key stored in `/home/awank/.discourse-api-credentials`
- [ ] SMTP test email received (or SMTP failure documented)
- [ ] At least one backup file in `/var/discourse/shared/standalone/backups/default/`
- [ ] External backup cron installed (`crontab -l | grep discourse-backup`)
- [ ] Load test: all 20 concurrent requests < 2.0 seconds
- [ ] Test topic created and deleted via API

**When all checked**: Platform is live and ready for Phase 5.1 publication.

---

## Quick Reference

```bash
# Start Discourse
cd /var/discourse && sudo ./launcher start app

# Stop Discourse
cd /var/discourse && sudo ./launcher stop app

# Restart Discourse
cd /var/discourse && sudo ./launcher restart app

# View logs
cd /var/discourse && sudo ./launcher logs app --tail 100

# Enter container shell
cd /var/discourse && sudo ./launcher enter app

# Rails console (inside container)
rails c

# Rebuild after app.yml changes
cd /var/discourse && sudo ./launcher rebuild app
```

**Cross-references**: `DISCOURSE_DEPLOYMENT_TECHNICAL_SPEC.md`, `DISCOURSE_DEPLOYMENT_RUNBOOK.md` (more detailed, Phase 1–12), `PLATFORM_DECISION_MATRIX_WITH_RUNBOOKS.md`
