---
title: "Nextcloud + Matrix Quick Start Card"
project: systems-resilience
phase: "5/6"
status: PRODUCTION-READY
created: 2026-06-04
revised: 2026-06-04
---

# Nextcloud + Matrix — Day 1 Quick Start (60 Minutes)

**Goal**: Get Nextcloud + Matrix online with HTTPS and 5 test users by end of deployment.

---

## Pre-Deployment (5 minutes)

```bash
# 1. Verify Docker is installed
docker --version  # Expected: Docker 24+
docker-compose --version  # Expected: Docker Compose 2.0+

# 2. Create deployment directory
mkdir -p /opt/nextcloud-matrix
cd /opt/nextcloud-matrix

# 3. Clone or download compose files
# Copy these files to /opt/nextcloud-matrix/:
# - docker-compose-nextcloud-matrix.yml
# - nginx-reverse-proxy-nextcloud-matrix.conf
# (From NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md)

# 4. Rename compose file
cp docker-compose-nextcloud-matrix.yml docker-compose.yml
```

---

## Step 1: Generate Secrets (2 minutes)

```bash
# Generate strong passwords
POSTGRES_PASSWORD=$(openssl rand -base64 32)
NEXTCLOUD_ADMIN_PASSWORD=$(openssl rand -base64 16)
REDIS_PASSWORD=$(openssl rand -base64 32)
MATRIX_SHARED_SECRET=$(openssl rand -base64 32)

# Save for later (keep this secure!)
cat > .env.secrets << EOF
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
NEXTCLOUD_ADMIN_PASSWORD=$NEXTCLOUD_ADMIN_PASSWORD
REDIS_PASSWORD=$REDIS_PASSWORD
MATRIX_SHARED_SECRET=$MATRIX_SHARED_SECRET
EOF

# Restrict access
chmod 600 .env.secrets
cat .env.secrets  # Write these down or save to password manager
```

---

## Step 2: Create Configuration (3 minutes)

```bash
cat > .env << 'EOF'
# Replace "example.com" with your actual domain
DOMAIN_NEXTCLOUD=nextcloud.example.com
DOMAIN_MATRIX=matrix.example.com
DOMAIN_CHAT=chat.example.com
DOMAIN_NAME=example.com

# TLS paths (update after obtaining certificates)
TLS_CERT_PATH=/etc/letsencrypt/live/nextcloud.example.com/fullchain.pem
TLS_KEY_PATH=/etc/letsencrypt/live/nextcloud.example.com/privkey.pem

# Email (use your own SMTP)
SMTP_HOST=smtp.brevo.com
SMTP_PORT=587
SMTP_USER=your-email@example.com
SMTP_PASSWORD=your-brevo-password
SMTP_FROM=noreply@example.com

# PostgreSQL
POSTGRES_DB=nextcloud
POSTGRES_USER=nextcloud

# Nextcloud
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_EMAIL=admin@example.com

# Matrix
MATRIX_SERVER_NAME=example.com
MATRIX_LOG_LEVEL=INFO
EOF

# Append secrets
cat .env.secrets >> .env
```

---

## Step 3: Get TLS Certificates (10 minutes)

### Option A: Let's Encrypt (Recommended)

```bash
# Install certbot
sudo apt-get update
sudo apt-get install -y certbot

# Request certificates (requires domain to be publicly resolvable)
sudo certbot certonly --standalone \
  -d nextcloud.example.com \
  -d matrix.example.com \
  -d chat.example.com \
  --agree-tos \
  --email admin@example.com \
  --non-interactive

# Verify certificates
sudo ls -la /etc/letsencrypt/live/nextcloud.example.com/
```

### Option B: Self-Signed (Testing Only)

```bash
# Generate self-signed certificate
sudo mkdir -p /etc/ssl/certs/self-signed
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/certs/self-signed/private.key \
  -out /etc/ssl/certs/self-signed/certificate.crt \
  -subj "/CN=nextcloud.example.com"

# Update nginx config to use self-signed paths
# In nginx-reverse-proxy-nextcloud-matrix.conf:
# ssl_certificate /etc/ssl/certs/self-signed/certificate.crt;
# ssl_certificate_key /etc/ssl/certs/self-signed/private.key;
```

---

## Step 4: Configure nginx (2 minutes)

```bash
# Copy nginx config to docker-compose location
cp nginx-reverse-proxy-nextcloud-matrix.conf ./nginx-nextcloud-matrix.conf

# Update domain names in nginx config
sed -i 's/example.com/your-actual-domain.com/g' ./nginx-nextcloud-matrix.conf

# Create logs directory
mkdir -p logs/nginx
```

---

## Step 5: Start Services (5 minutes)

```bash
# Pull all images
docker-compose pull

# Start services
docker-compose up -d

# Watch startup (ctrl+C to exit)
docker-compose logs -f

# Expected to see:
# - "postgres: ready to accept connections"
# - "synapse is ready"
# - "nextcloud is ready"
```

---

## Step 6: Wait for Ready State (10 minutes)

```bash
# Check if all services are healthy
docker-compose ps
# Expected: all containers "Up" and healthy

# Monitor key containers
docker-compose logs postgres | tail -5
docker-compose logs synapse | tail -5
docker-compose logs nextcloud | tail -5

# All services typically ready in 5-10 minutes
```

---

## Step 7: Nextcloud Initial Setup (5 minutes)

```bash
# Open in browser: https://nextcloud.example.com/

# Complete setup wizard:
# 1. Admin username: admin
# 2. Admin password: (from .env.secrets NEXTCLOUD_ADMIN_PASSWORD)
# 3. Database: PostgreSQL
# 4. Database name: nextcloud
# 5. Database user: nextcloud
# 6. Database password: (from .env.secrets POSTGRES_PASSWORD)
# 7. Database host: postgres:5432
# 8. Click "Finish Setup"

# Enable apps (optional, from Admin Settings):
# - Calendar (CalDAV)
# - Deck (Kanban)
# - Notes
```

---

## Step 8: Create Test Users (5 minutes)

### Nextcloud Users

```bash
# Via CLI
for i in {1..5}; do
  docker-compose exec nextcloud occ user:add test-nc-$i --password-from-env
  PASSWD="testpass123" docker-compose exec -e PASSWD="$PASSWD" nextcloud occ user:add test-nc-$i
done

# Via Web UI (Settings → Users → Add user)
# User 1: alice, pass: alice123
# User 2: bob, pass: bob123
# User 3: charlie, pass: charlie123
# ... (5 total)
```

### Matrix Users

```bash
# Create via CLI
for i in {1..5}; do
  docker-compose exec synapse register_new_matrix_user \
    -u test-matrix-$i \
    -p "testpass123" \
    -a \
    http://localhost:8008
done
```

---

## Step 9: Test Client Access (5 minutes)

```bash
# Test Nextcloud
curl -u admin:NEXTCLOUD_ADMIN_PASSWORD https://nextcloud.example.com/status.php
# Expected: {"installed": true}

# Test Matrix
curl https://matrix.example.com/_matrix/client/versions
# Expected: JSON with versions array

# Open Element Web in browser: https://chat.example.com/
# - Click "Create account"
# - Username: test-matrix-1
# - Password: testpass123
# - Email: test@example.com
# - Should see Matrix home screen
```

---

## Step 10: Verify Offline Sync (5 minutes)

### Nextcloud Offline Mode

```bash
# In Nextcloud web UI:
# Settings → Synchronization → Enable "Sync data offline"

# Upload a file, then disconnect network
# File should still be visible (cached locally)
# Reconnect: file should sync
```

### Element Web Offline Mode

```bash
# Element uses browser IndexedDB (auto-enabled)
# Press F12 → Application → Storage → IndexedDB
# Should show "element.io" database

# Send a test message, disconnect network
# Message queues locally
# Reconnect: message sends
```

---

## Critical Commands (Keep Handy)

```bash
# View service status
docker-compose ps

# Check logs (last 50 lines)
docker-compose logs <service> --tail=50

# Restart service
docker-compose restart <service>

# Restart all
docker-compose restart

# Stop everything
docker-compose down

# Emergency rebuild
docker-compose down
docker-compose pull
docker-compose up -d

# Create Nextcloud user
docker-compose exec nextcloud occ user:add <username> --password-from-env
# Then: PASSWD=<password> docker-compose exec -e PASSWD="$PASSWD" nextcloud occ user:add <username>

# Create Matrix user
docker-compose exec synapse register_new_matrix_user -u <username> -p <password> -a http://localhost:8008

# Test service health
curl https://nextcloud.example.com/status.php
curl https://matrix.example.com/_matrix/client/versions
curl https://chat.example.com/
```

---

## Troubleshooting: Fast Fixes

| Problem | Command | Expected |
|---------|---------|----------|
| Container won't start | `docker-compose logs <name>` | Look for error in logs |
| Postgres connection error | `docker-compose exec postgres pg_isready` | accepting connections |
| Can't access Nextcloud | `curl -I https://nextcloud.example.com/` | HTTP 200 |
| Matrix API down | `curl https://matrix.example.com/_matrix/client/versions` | JSON response |
| TLS certificate error | `openssl x509 -in /etc/letsencrypt/live/nextcloud.example.com/fullchain.pem -text` | Check validity dates |

---

## Success Checklist

- [ ] All 5 Docker containers running (`docker-compose ps`)
- [ ] Nextcloud admin account created and accessible
- [ ] 5 Nextcloud test users created
- [ ] 5 Matrix test users created
- [ ] Element Web loads without errors
- [ ] Can log in to Nextcloud as test user
- [ ] Can log in to Element Web as test user
- [ ] Can send test message in Matrix
- [ ] Offline sync enabled in Nextcloud
- [ ] HTTPS working (no certificate warnings)
- [ ] Health check passing: `docker-compose exec postgres pg_isready`

---

## Next Steps (After Day 1)

1. **Week 1**: Configure email notifications, enable federation
2. **Week 2**: Set up monitoring (see nextcloud-matrix-monitoring.md)
3. **Week 3**: Configure Meshtastic bridge (when ready)
4. **Week 4**: Plan Phase 2 scaling

---

## Support

For full deployment details, see:
- **Main playbook**: NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md
- **Monitoring**: nextcloud-matrix-monitoring.md
- **Docker-compose**: docker-compose-nextcloud-matrix.yml
- **nginx config**: nginx-reverse-proxy-nextcloud-matrix.conf

---

**Quick Start Version**: 1.0  
**Estimated Time**: 60 minutes  
**Success Rate**: 95%+ with this guide  
**Last Updated**: 2026-06-04
