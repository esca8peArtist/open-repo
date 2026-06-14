---
title: "Discourse Deployment Technical Specification"
project: systems-resilience
platform: "Discourse (Official Docker Launcher + Bitnami ARM64 fallback)"
created: 2026-06-14
purpose: "Technical specification for June 14-15 platform decision. Covers resource requirements, deployment method, ARM64 architecture notes, backup, and troubleshooting. Companion to NEXTCLOUD_DEPLOYMENT_TECHNICAL_SPEC.md."
decision_context: "Discourse is the recommended platform for Pi5 (8GB RAM, ARM64). See PLATFORM_DECISION_MATRIX_WITH_RUNBOOKS.md for the recommendation rationale."
---

# Discourse Deployment Technical Specification
## Raspberry Pi 5 (8GB RAM, ARM64) — June 14, 2026

---

## 1. Infrastructure Requirements

### Hardware Requirements

| Resource | Minimum | Recommended | Pi5 (ours) | Status |
|----------|---------|-------------|------------|--------|
| RAM | 2 GB | 4–8 GB | 8 GB | EXCELLENT |
| CPU cores | 2 | 4 | 4 (ARM Cortex-A76) | EXCELLENT |
| Free storage | 10 GB | 30–100 GB | ~189 GB | EXCELLENT |
| Network | 50 Mbps | 100 Mbps | Tailscale/home | ADEQUATE |

**RAM Assessment**: At idle, Discourse (all-in-one container) uses approximately 1.5–2 GB RAM. Under 50–100 concurrent users it uses 2.5–3 GB. With 8 GB total RAM and ~500 MB OS overhead, there is 5–5.5 GB of free RAM under load. This is comfortable. There is no memory risk on this hardware for the anticipated user load.

**Concurrent user capacity**: 50–100 users — no problem at all. Discourse's built-in PostgreSQL and Redis handle this load well within the RAM and CPU budget. Scaling concerns only arise beyond 500–1,000 concurrent users.

### ARM64 Architecture — CRITICAL NOTE

The Pi5 is `aarch64` (ARM64). There are two Discourse deployment paths for ARM64:

**Path 1 — Official Discourse Docker Launcher (builds from source)**
- The official `discourse_docker` launcher with `./launcher bootstrap app` compiles Discourse from source during bootstrap. This works on ARM64 because it builds a native binary rather than pulling a pre-compiled x86-64 image.
- Bootstrap time on Pi5 ARM64: **15–25 minutes** (vs 5–10 minutes on x86 VPS). This is due to Ruby gem compilation and asset precompilation on the Pi's ARM cores.
- Pi5 thermal note: Bootstrap will push CPU to 87–88°C. This is within operational limits for Pi5 but slower than x86.
- **After bootstrap**: Discourse runs as a native ARM64 binary — no emulation overhead. Performance in production is good.
- **Status**: This is the officially supported method; use it unless bootstrap fails.

**Path 2 — Bitnami ARM64 Docker Compose (pre-built)**
- `docker.io/bitnami/discourse:3` is a pre-built ARM64 image that skips source compilation.
- Bootstrap time on Pi5: **3–5 minutes** (no compilation step).
- Trade-off: Bitnami packages may lag Discourse releases by 1–3 minor versions. Not a concern for initial deployment.
- **Use this path if**: the official bootstrap fails with architecture errors or if bootstrap exceeds 30 minutes.

The existing `DISCOURSE_DEPLOYMENT_RUNBOOK.md` has full instructions for both paths including error detection and fallback switching.

---

## 2. Docker Deployment Configuration

### 2.1 Architecture — All-in-One Container

Unlike Nextcloud+Matrix (7 containers), Discourse is a single managed container containing all services:

```
External users (50–200 concurrent)
    |
    v
Pi5 Tailscale IP (100.120.18.84)
    |
    v
Discourse container (port 80 + 443)
    ├── nginx (TLS termination, internal)
    ├── Puma (Rails app server, Unicorn workers × 2)
    ├── Sidekiq (background jobs: email, search indexing)
    ├── PostgreSQL (embedded database)
    └── Redis (embedded cache)
    |
    v
/var/discourse/shared/standalone/   (persistent volume — uploads, backups, logs)
```

This single-container architecture is why Discourse is simpler to operate: one process tree to monitor, one log stream, one restart command.

### 2.2 Official Launcher Method — app.yml

The deployment is controlled by `/var/discourse/containers/app.yml`. This is not a `docker-compose.yml` file. The launcher script (`/var/discourse/launcher`) builds and manages the container.

**Complete app.yml for Pi5 deployment** (fill in all `REPLACE_*` values):

```yaml
## /var/discourse/containers/app.yml
## Systems Resilience Community — Raspberry Pi 5 (8GB ARM64)
## Generated 2026-06-14

templates:
  - "templates/postgres.template.yml"
  - "templates/redis.template.yml"
  - "templates/web.template.yml"
  - "templates/web.ratelimited.template.yml"

## Port bindings
## CRITICAL: Bind to Tailscale IP only — NEVER 0.0.0.0
expose:
  - "100.120.18.84:80:80"
  - "100.120.18.84:443:443"

params:
  db_default_text_search_config: "pg_catalog.english"
  ## Pi5-tuned PostgreSQL (8GB RAM, ARM64)
  db_shared_buffers: "512MB"
  db_work_mem: "64MB"

env:
  LANG: en_US.UTF-8
  RAILS_ENV: production

  ## Hostname — use Tailscale MagicDNS name OR IP
  ## Tailscale hostname example: raspby1.tail1234.ts.net
  ## IP-only example: 100.120.18.84 (browser will warn about self-signed cert)
  DISCOURSE_HOSTNAME: "REPLACE_WITH_HOSTNAME_OR_IP"

  ## Admin email — this address gets admin privileges on first setup
  DISCOURSE_DEVELOPER_EMAILS: "REPLACE_WITH_ADMIN_EMAIL"

  ## SMTP Configuration
  ## If SMTP is not available: Discourse works but cannot send email
  ## Free SMTP options: Brevo (300/day free), Gmail SMTP (500/day with app password)
  DISCOURSE_SMTP_ADDRESS: "REPLACE_SMTP_HOST"
  DISCOURSE_SMTP_PORT: 587
  DISCOURSE_SMTP_USER_NAME: "REPLACE_SMTP_USER"
  DISCOURSE_SMTP_PASSWORD: "REPLACE_SMTP_PASSWORD"
  DISCOURSE_SMTP_ENABLE_START_TLS: true
  DISCOURSE_SMTP_AUTHENTICATION: login
  DISCOURSE_NOTIFICATION_EMAIL: "noreply@REPLACE_YOUR_DOMAIN"
  DISCOURSE_CONTACT_EMAIL: "REPLACE_WITH_ADMIN_EMAIL"

  ## Site identity
  DISCOURSE_TITLE: "Systems Resilience Community"

  ## Pi5 performance tuning
  ## 2 Unicorn workers is correct for 8GB RAM — do not increase to 3
  UNICORN_WORKERS: 2
  UNICORN_TIMEOUT: 60

  ## Rate limiting (generous for trusted community of 50–200 users)
  DISCOURSE_MAX_REQS_PER_IP_PER_MINUTE: 300
  DISCOURSE_MAX_REQS_PER_IP_PER_10_SECONDS: 60

  ## Access control (set false for public read community)
  DISCOURSE_MUST_APPROVE_USERS: false

  ## Let's Encrypt — only works with public domain (not Tailscale IP)
  ## Uncomment if you have a public domain pointing to this Pi:
  # LETSENCRYPT_ACCOUNT_EMAIL: "REPLACE_WITH_ADMIN_EMAIL"

## Persistent volume — DO NOT modify these paths
volumes:
  - volume:
      host: /var/discourse/shared/standalone
      guest: /shared
  - volume:
      host: /var/discourse/shared/standalone/log/var-log
      guest: /var/log

## Plugins
hooks:
  after_code:
    - exec:
        cd: $home
        cmd:
          - git clone https://github.com/discourse/docker_manager.git plugins/docker_manager
          ## Optional: uncomment to install solved plugin
          # - git clone https://github.com/discourse/discourse-solved.git plugins/discourse-solved
```

### 2.3 Bitnami Fallback (ARM64 pre-built)

If the official bootstrap fails, use this docker-compose.yml at `/opt/discourse-bitnami/docker-compose.yml`:

```yaml
version: '3.8'
# Bitnami Discourse — ARM64 pre-built images
# Use this if official launcher bootstrap fails on Pi5

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
      - "127.0.0.1:5432:5432"  # loopback only

  redis:
    image: docker.io/bitnami/redis:7.2
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - redis_data:/bitnami/redis/data
    ports:
      - "127.0.0.1:6379:6379"  # loopback only

  discourse:
    image: docker.io/bitnami/discourse:3
    ports:
      - "100.120.18.84:80:3000"    # Tailscale IP only — NEVER 0.0.0.0
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
```

---

## 3. Configuration Steps

### Step 1: System Setup

```bash
# Confirm ARM64 architecture
uname -m
# Expected: aarch64

# Confirm Docker is installed
docker --version
# Expected: Docker 20.x or later (already installed per June 7 audit)

# Confirm disk space (189GB free — well above the 10GB minimum)
df -h /
```

### Step 2: Clone Discourse Launcher

```bash
sudo mkdir -p /var/discourse
sudo chown $USER:$USER /var/discourse
git clone https://github.com/discourse/discourse_docker.git /var/discourse
cd /var/discourse
mkdir -p /var/discourse/containers
cp /var/discourse/samples/standalone.yml /var/discourse/containers/app.yml
```

### Step 3: Edit and Validate app.yml

Fill in all `REPLACE_*` values. Validate before bootstrapping (a YAML error causes a 20-minute wasted bootstrap):

```bash
# Validate YAML syntax
python3 -c "
import yaml
try:
    with open('/var/discourse/containers/app.yml') as f:
        data = yaml.safe_load(f)
    print('YAML OK')
    print('Hostname:', data['env']['DISCOURSE_HOSTNAME'])
    print('SMTP host:', data['env']['DISCOURSE_SMTP_ADDRESS'])
except Exception as e:
    print('YAML ERROR:', e)
"

# Confirm no unreplaced placeholders
grep "REPLACE_" /var/discourse/containers/app.yml
# Expected: no output
```

### Step 4: Bootstrap (15–25 minutes on Pi5)

```bash
cd /var/discourse
sudo ./launcher bootstrap app 2>&1 | tee /tmp/discourse-bootstrap.log
# Monitor in second terminal:
# tail -f /tmp/discourse-bootstrap.log
```

If bootstrap exceeds 30 minutes or shows architecture errors, switch to Bitnami path (Section 2.3).

### Step 5: Start and Verify

```bash
cd /var/discourse
sudo ./launcher start app
sudo ./launcher status app
# Expected: "app: up" with uptime counter

curl -sk http://100.120.18.84/about.json | python3 -m json.tool | head -10
# Expected: JSON response with site title and stats
```

### Step 6: SSL Certificate

```bash
# Option A: Tailscale HTTPS (no public domain needed)
tailscale_host=$(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
sudo tailscale cert "$tailscale_host"
# Update DISCOURSE_HOSTNAME in app.yml to the MagicDNS hostname, then:
cd /var/discourse && sudo ./launcher rebuild app  # 10–15 min on Pi5

# Option B: Let's Encrypt (requires public domain with DNS A record)
# Uncomment LETSENCRYPT_ACCOUNT_EMAIL in app.yml and rebuild

# Option C: Self-signed (users see browser warning once)
# Leave SSL settings commented out — launcher generates self-signed automatically
```

### Step 7: Admin Account and Community Setup

After bootstrap, access the web setup wizard at `https://[hostname]` or use the Rails console:

```bash
sudo ./launcher enter app
rails c

# Create admin if not created via web wizard
admin = User.find_by(email: "your@email.com")
admin.grant_admin! if admin
```

For complete community setup (categories, trust levels, groups), refer to `DISCOURSE_DEPLOYMENT_RUNBOOK.md` Phase 7–9, which has full copy-paste Rails console commands for the Systems Resilience community structure.

### Step 8: OAuth Integration (Optional)

Discourse supports GitHub OAuth for one-click signup without email confirmation:

```bash
# In app.yml, add:
# DISCOURSE_GITHUB_CLIENT_ID: your-github-app-client-id
# DISCOURSE_GITHUB_CLIENT_SECRET: your-github-app-client-secret
# Rebuild after adding
```

GitHub OAuth eliminates the SMTP dependency for user registration (users can sign up via GitHub OAuth even with no SMTP configured).

---

## 4. Backup Strategy

### 4.1 Discourse Built-in Backups

Discourse has a built-in backup system that creates compressed archives of the database and uploaded files. Configure via Rails console:

```bash
sudo ./launcher enter app
rails c

SiteSetting.backup_frequency = 1         # Daily backups
SiteSetting.maximum_backups = 14          # Keep 14 days
SiteSetting.backup_with_uploads = true    # Include uploaded files
SiteSetting.enable_backups = true
exit
```

Backups are stored at `/var/discourse/shared/standalone/backups/default/`.

### 4.2 External Backup Script

```bash
cat > /opt/discourse-backup-external.sh << 'EOF'
#!/bin/bash
# External backup — runs after Discourse's midnight internal backup
set -euo pipefail

DISCOURSE_DIR="/var/discourse/shared/standalone"
BACKUP_DIR="/home/awank/backups/discourse"
DATE=$(date -u +%Y-%m-%d)
LOG="/var/log/discourse-backup-external.log"

mkdir -p "$BACKUP_DIR/$DATE"

# Copy latest internal backup
latest=$(ls -t "$DISCOURSE_DIR/backups/default/"*.gz 2>/dev/null | head -1)
if [[ -z "$latest" ]]; then
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] WARNING: no backup found" >> "$LOG"
    exit 1
fi

cp "$latest" "$BACKUP_DIR/$DATE/"
cp /var/discourse/containers/app.yml "$BACKUP_DIR/$DATE/app.yml.bak"

# Keep 30 days of external backups
find "$BACKUP_DIR" -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null || true

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] External backup complete: $(du -sh "$BACKUP_DIR/$DATE" | cut -f1)" >> "$LOG"
EOF

chmod +x /opt/discourse-backup-external.sh
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/discourse-backup-external.sh") | crontab -
```

### 4.3 Restore Procedure

```bash
# 1. Stop Discourse
cd /var/discourse && sudo ./launcher stop app

# 2. Enter container and trigger restore (database + uploads)
cd /var/discourse && sudo ./launcher enter app

# List available backups
ls -lah /var/discourse/shared/standalone/backups/default/

# Run restore via rails console
rails c
BackupRestore::Restorer.new(
    User.find_by(admin: true).id,
    filename: "discourse-YYYY-MM-DD-HHMMSS.tar.gz",
    factory_reset: false
).run
exit

# 3. Restart
cd /var/discourse && sudo ./launcher restart app
```

---

## 5. Advantages on Pi5 (and Why Discourse Is Recommended)

1. **RAM comfort**: 2–3 GB usage leaves 5 GB free. No OOM risk at 50–100 users. The system can absorb traffic spikes without service degradation.

2. **Single-container simplicity**: One container to manage, restart, monitor, and troubleshoot. Fewer failure modes. When something goes wrong, there is one log stream to check.

3. **Built-in governance**: Trust levels, moderation queue, spam detection, flag handling, and user reputation are all built-in. Nextcloud+Matrix requires manual room administration and has no equivalent automated moderation.

4. **Deployment speed**: 2–3 hours (including 15–25 min ARM64 bootstrap) vs 4–6 hours for Nextcloud+Matrix. This is significant given the tight deadline.

5. **Backup built-in**: Discourse's internal backup system handles database and uploads together. Nextcloud requires separate procedures for database, config, and file volumes.

6. **Community fit for publication**: The systems-resilience project is publishing research documents for community reading and discussion. Discourse's forum structure (topic per document, replies for discussion) is a natural fit. Nextcloud's file sharing metaphor is less natural for public reading.

---

## 6. Known Limitations

1. **No real-time collaborative editing**: Discourse has no equivalent to Nextcloud's file sync and collaborative editing (and OnlyOffice is not available on ARM64 anyway). Authors cannot co-edit documents in-browser.

2. **No end-to-end encryption**: All content is visible to administrators. For sensitive community communications, this is a limitation. For public research publication, it is acceptable.

3. **Not federated**: Discourse is a single-tenant platform. There is no Matrix federation. Users must create an account on this specific Discourse instance.

4. **Email required for full functionality**: Without SMTP, user registration requires manual admin intervention to activate accounts. GitHub OAuth eliminates this dependency for registration.

5. **ARM64 bootstrap compilation**: The official bootstrap compiles from source on ARM64. This takes 15–25 minutes and cannot be interrupted. If power or network fails during bootstrap, start over.

---

## 7. Troubleshooting

### Bootstrap fails with architecture errors

```bash
grep -i "exec format error\|cannot execute binary\|arm\|amd64" /tmp/discourse-bootstrap.log | tail -20
# If present: switch to Bitnami path (Section 2.3)
cd /opt/discourse-bitnami
docker compose up -d
```

### Container won't start after bootstrap

```bash
cd /var/discourse
sudo ./launcher logs app --tail 100 | grep -E "(ERROR|FATAL|fail)"
# Most common: database connection failure
# Solution: wait 60s for PostgreSQL to initialize, then retry ./launcher start app
```

### SMTP not working

```bash
sudo ./launcher enter app
rails c
# Check config
puts SiteSetting.smtp_address
puts SiteSetting.smtp_user_name
# Send test
Jobs.enqueue(:test_email, to_address: "your@email.com")
# Check email log
EmailLog.last(3).each { |e| puts "#{e.created_at}: #{e.to_address} — #{e.smtp_transaction_response}" }
exit
```

### Slow response times under load

```bash
# Check RAM
free -h
# Check Sidekiq queue depth
sudo ./launcher enter app
rails c
puts Sidekiq::Queue.new.size  # should be < 100
exit
# If queue is growing: Sidekiq is behind; watch for SMTP backlog or search indexing delay
```

### Disk full

```bash
df -h /var/discourse/shared
# Clean old logs:
sudo ./launcher enter app
find /var/log -name "*.log" -mtime +7 -exec truncate -s 0 {} \;
exit
# Also: reduce maximum_backups setting to trim old backup files
```

---

## Deployment Time Estimate: 2–3 hours

| Phase | Duration |
|-------|---------|
| System check + launcher clone | 15 min |
| Edit and validate app.yml | 30 min |
| Bootstrap (Pi5 ARM64) | 25 min |
| SSL setup | 20 min |
| Admin + community setup via Rails console | 45 min |
| Smoke tests + troubleshooting buffer | 30 min |
| **Total** | **~2.75 hours typical** |

**Cross-references**: `DISCOURSE_DEPLOYMENT_RUNBOOK.md` (full step-by-step with Phase 1–12 detail), `DEPLOYMENT_PLAYBOOK_DISCOURSE.md`, `DISCOURSE_DEPLOYMENT_PLAYBOOK.md`
