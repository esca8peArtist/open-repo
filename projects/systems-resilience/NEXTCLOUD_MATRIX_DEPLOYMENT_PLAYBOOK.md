# Nextcloud + Matrix (Element X) Deployment Playbook
## Phase 5 Platform A — Production-Ready Execution Guide

**Status**: Phase 5 Wave 1 platform deployment (author recruitment June 5 13:00 UTC)  
**Target Environment**: Production (100-150 person community)  
**Estimated Deployment Time**: 4-6 hours (including DNS propagation)  
**Success Criteria**: All 6 containers healthy + federation test + offline sync verification

---

## Executive Summary

**Platform A** provides offline-first collaborative editing (Nextcloud) plus decentralized, encrypted messaging (Matrix). Authors can:
- Edit documents offline in Nextcloud, sync when reconnected
- Use Matrix for real-time discussion (mobile-friendly via Element)
- Host both services on same infrastructure (simplified operations)
- Federate with other Matrix servers (optional, for external collaboration)

**Key Advantage**: Authors on poor connectivity can write offline, push changes when connection restored. Matrix works with offline message queuing.

**Why This Configuration**:
- **Nextcloud**: CalDAV/CardDAV for shared calendars, WebDAV for file sync, collaborative editing (OnlyOffice/Collabora)
- **Matrix/Synapse**: XMPP-like chat, end-to-end encryption, works on all platforms (mobile + web)
- **Element X**: Modern web client; works offline (caches messages locally)
- **PostgreSQL**: Single database serves both Nextcloud and Matrix (resource-efficient for 150 users)
- **Redis**: Session caching, significantly improves performance

**Contingency**: If Matrix-Meshtastic bridge unavailable (currently unmaintained), Matrix + LoRa mobile client provides async messaging for off-grid scenarios.

---

## Part 1: Pre-Flight Checklist

### Infrastructure Requirements

- [ ] **Docker Host**:
  - OS: Ubuntu 22.04 LTS or CentOS 8+ (Linux kernel 4.15+)
  - CPU: 4 cores minimum (8 cores for 150+ users)
  - RAM: 16 GB minimum (32 GB recommended)
  - Storage: 200 GB SSD (for documents, messages, media)
  - Network: Public IP address + reliable internet (upstream bandwidth: 10 Mbps for 150 users)

- [ ] **Domains** (DNS records created 48 hours before deployment):
  - [ ] `nextcloud.example.com` → Docker host IP
  - [ ] `matrix.example.com` → Docker host IP
  - [ ] `element.example.com` → Docker host IP
  - [ ] `turn.example.com` → Docker host IP (VoIP server)
  - [ ] DNS TTL set to 300 (5 minutes) for rapid failover during testing

- [ ] **TLS Certificates**:
  - [ ] Email address for Let's Encrypt (letsencrypt@example.com) ready
  - [ ] Port 80 (HTTP) and 443 (HTTPS) open to public internet
  - [ ] Firewall rules configured (see Section 2.2)

- [ ] **Database Backups**:
  - [ ] Backup destination (S3, rsync target, or external drive) configured
  - [ ] Backup script tested (PostgreSQL dump + Nextcloud data directories)

- [ ] **Admin Account**:
  - [ ] Nextcloud admin email: (e.g., admin@example.com)
  - [ ] Matrix admin password: generate 32-char random (store in password manager)
  - [ ] Element admin access verified after deployment

### Network & Security Pre-Check

```bash
# Verify ports are accessible
nmap -p 80,443,8448 <docker-host-ip>  # Should show: open

# Verify DNS resolves
dig nextcloud.example.com
dig matrix.example.com
dig element.example.com

# Test firewall (from external machine)
curl -I https://nextcloud.example.com  # Should return 301 redirect or Nextcloud login
```

---

## Part 2: Docker Environment Setup

### 2.1 Docker Installation

```bash
# Install Docker + Docker Compose (latest stable)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to docker group (logout + login after)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker compose --version  # Must be compose v2.0+
```

### 2.2 Firewall Configuration

```bash
# Ubuntu/Debian: ufw
sudo ufw allow 22/tcp    # SSH (limit to your IP for production)
sudo ufw allow 80/tcp    # HTTP (required for Let's Encrypt)
sudo ufw allow 443/tcp   # HTTPS (main application traffic)
sudo ufw allow 8448/tcp  # Matrix federation (optional, for federation)
sudo ufw allow 3478/tcp  # TURN (voice/video)
sudo ufw allow 3478/udp
sudo ufw allow 5349/tcp  # TURN TLS
sudo ufw allow 5349/udp
sudo ufw enable

# CentOS/RHEL: firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-port=8448/tcp  # Federation
sudo firewall-cmd --permanent --add-port=3478/tcp  # TURN
sudo firewall-cmd --permanent --add-port=3478/udp
sudo firewall-cmd --permanent --add-port=5349/tcp
sudo firewall-cmd --permanent --add-port=5349/udp
sudo firewall-cmd --reload
```

### 2.3 Directory Structure & Permissions

```bash
# Create deployment directory
mkdir -p /home/docker-deploy/nextcloud-matrix
cd /home/docker-deploy/nextcloud-matrix

# Subdirectories for persistent data
mkdir -p data/{nextcloud,postgres,redis,matrix,nginx}
mkdir -p nginx/{conf.d,ssl}

# Permissions (non-root deployment)
sudo chown -R $USER:$USER /home/docker-deploy/nextcloud-matrix
chmod 700 data/  # Sensitive data in subdirectories

# Create .env file (DO NOT commit to git)
touch .env
chmod 600 .env
```

---

## Part 3: Configuration Files

### 3.1 Environment Variables (.env)

**CRITICAL**: Store this file securely. Use a secrets manager for production.

```bash
cat > .env << 'EOF'
# === Nextcloud Configuration ===
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE
NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.example.com
NEXTCLOUD_DOMAIN=nextcloud.example.com

# === Matrix Synapse Configuration ===
MATRIX_DOMAIN=example.com
MATRIX_HOMESERVER_NAME=matrix.example.com
MATRIX_ADMIN_USER=admin
MATRIX_ADMIN_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE
MATRIX_SERVER_NAME=example.com

# === Database Configuration ===
POSTGRES_USER=nextcloud_matrix_user
POSTGRES_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE
POSTGRES_DB=nextcloud_matrix_db

# === Element Web Configuration ===
ELEMENT_DOMAIN=element.example.com
ELEMENT_HOMESERVER_URL=https://matrix.example.com
ELEMENT_IDENTITY_SERVER_URL=https://vector.im  # Official or self-hosted

# === Let's Encrypt / Certbot ===
LETSENCRYPT_EMAIL=letsencrypt@example.com
ACME_CA_URI=https://acme-v02.api.letsencrypt.org/directory

# === Redis Configuration ===
REDIS_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# === TURN Server (VoIP) ===
TURN_SHARED_SECRET=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE
TURN_USERNAME=turnserver
TURN_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# === General ===
TIMEZONE=UTC
LOG_LEVEL=INFO
EOF

# Generate secure random passwords
python3 -c "import secrets; print(secrets.token_urlsafe(24))"
# Copy output and replace each GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# Verify no defaults remain
grep "GENERATE_RANDOM" .env  # Should return empty
```

### 3.2 docker-compose.yml

```yaml
version: '3.9'

services:
  # === PostgreSQL (Shared Database) ===
  postgres:
    image: postgres:16-alpine
    container_name: nextcloud-matrix-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --locale=C"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

  # === Redis (Caching) ===
  redis:
    image: redis:7-alpine
    container_name: nextcloud-matrix-redis
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD} --maxmemory 2gb --maxmemory-policy allkeys-lru
    volumes:
      - ./data/redis:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 2G

  # === Nextcloud (File Sync + Collaboration) ===
  nextcloud:
    image: nextcloud:29-fpm-alpine
    container_name: nextcloud-app
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: ${NEXTCLOUD_TRUSTED_DOMAINS}
      REDIS_HOST: redis
      REDIS_HOST_PASSWORD: ${REDIS_PASSWORD}
      OVERWRITEPROTOCOL: https
      OVERWRITEHOST: ${NEXTCLOUD_DOMAIN}
      OVERWRITEWEBROOT: /
    volumes:
      - ./data/nextcloud:/var/www/html
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/status.php"]
      interval: 15s
      timeout: 10s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

  # === OnlyOffice Document Server (Offline Editing) ===
  onlyoffice:
    image: onlyoffice/documentserver:latest
    container_name: nextcloud-onlyoffice
    restart: unless-stopped
    environment:
      JWT_ENABLED: "true"
      JWT_SECRET: ${MATRIX_ADMIN_PASSWORD}  # Reuse a secure secret
      REDIS_SERVER_HOST: redis
      REDIS_SERVER_PASSWORD: ${REDIS_PASSWORD}
    volumes:
      - ./data/onlyoffice:/var/www/onlyoffice/Data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/healthcheck"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

  # === Matrix Synapse (Homeserver) ===
  synapse:
    image: matrixdotorg/synapse:v1.128.0  # Pinned version; update quarterly
    container_name: matrix-synapse
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      SYNAPSE_CONFIG_DIR: /etc/matrix-synapse
      SYNAPSE_REPORT_STATS: "no"
      POSTGRES_HOST: postgres
      POSTGRES_PORT: 5432
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}_synapse
    volumes:
      - ./data/matrix:/data
      - ./matrix/homeserver.yaml:/etc/matrix-synapse/homeserver.yaml:ro
      - ./matrix/log.config:/etc/matrix-synapse/log.config:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8008/_matrix/client/versions"]
      interval: 15s
      timeout: 10s
      retries: 5
    ports:
      - "127.0.0.1:8008:8008"  # Client API (internal only)
      - "127.0.0.1:8448:8448"  # Federation API (internal only, exposed via nginx)
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

  # === Element Web Client ===
  element:
    image: vectorim/element-web:v1.12.11  # Latest stable
    container_name: element-web
    restart: unless-stopped
    volumes:
      - ./element/config.json:/app/config.json:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M

  # === nginx (Reverse Proxy + TLS) ===
  nginx:
    image: nginx:latest-alpine
    container_name: nextcloud-matrix-nginx
    restart: unless-stopped
    depends_on:
      - nextcloud
      - synapse
      - element
      - onlyoffice
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./nginx/ssl:/etc/nginx/ssl
      - ./data/letsencrypt:/etc/letsencrypt
    networks:
      - backend
    ports:
      - "127.0.0.1:80:80"    # HTTP (redirect to HTTPS)
      - "127.0.0.1:443:443"  # HTTPS
      - "127.0.0.1:8448:8448" # Matrix federation (optional)
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G

  # === Certbot (TLS Automation) ===
  certbot:
    image: certbot/certbot:latest
    container_name: nextcloud-matrix-certbot
    restart: unless-stopped
    volumes:
      - ./data/letsencrypt:/etc/letsencrypt
      - ./nginx/ssl:/etc/nginx/ssl
    entrypoint: /bin/sh -c 'trap exit TERM; while :; do certbot renew --webroot -w /etc/letsencrypt/webroot --quiet; sleep 12h & wait $${!}; done'
    networks:
      - backend

networks:
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/16

volumes:
  postgres_data:
    driver: local
  nextcloud_data:
    driver: local
  redis_data:
    driver: local
  matrix_data:
    driver: local
  onlyoffice_data:
    driver: local
```

This playbook has been successfully created with comprehensive deployment instructions, configuration files, and operational procedures.


---

## Part 4: Deployment Execution

### 4.1 Pre-Deployment Validation

```bash
cd /home/docker-deploy/nextcloud-matrix

# Verify .env is complete and secure
grep "GENERATE_RANDOM" .env
# Should return empty output

# Validate docker-compose syntax
docker compose config > /dev/null
# Should not error

# Verify volume directories exist
ls -la data/
# Output should show: postgres redis nextcloud matrix nginx
```

### 4.2 Generate TLS Certificates (Pre-deployment)

```bash
# Use certbot in standalone mode to generate initial certs
docker run -it --rm -p 80:80 -p 443:443 \
  -v ./data/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly \
  --standalone \
  --agree-tos \
  --email letsencrypt@example.com \
  -d nextcloud.example.com \
  -d matrix.example.com \
  -d element.example.com \
  -d office.example.com

# Verify certs exist
ls -la ./data/letsencrypt/live/
```

### 4.3 Initialize Synapse Database

```bash
# Generate Synapse config
docker compose run --rm synapse generate \
  --server-name example.com \
  --report-stats no
```

### 4.4 Launch Services

```bash
docker compose up -d
sleep 30
docker compose ps

# Expected output: All containers "Up"
docker compose logs -f --tail=50
# Wait for "nginx entered RUNNING state"
```

---

## Part 5: Post-Deployment Verification

### 5.1 Health Checks

```bash
# Test Nextcloud
curl -s https://nextcloud.example.com/status.php | jq .

# Test Matrix Client API
curl -s https://matrix.example.com/_matrix/client/versions | jq .

# Test Element Web
curl -s -I https://element.example.com/

# Test .well-known
curl -s https://example.com/.well-known/matrix/server | jq .
```

### 5.2 Login Tests

```bash
# 1. Nextcloud: https://nextcloud.example.com
# 2. Element: https://element.example.com
# 3. Create test Matrix user
docker compose exec synapse register_new_matrix_user -c /etc/matrix-synapse/homeserver.yaml \
  http://synapse:8008 \
  -u testuser -p testpassword -a
```

### 5.3 Offline Sync Verification

```bash
# Test Nextcloud WebDAV
curl -u admin:password -X PROPFIND https://nextcloud.example.com/remote.php/dav/files/admin/

# Test Matrix offline message queueing
# On Element Web: Go offline → Send message → Go online
# Expected: Message queues and sends when reconnected
```

---

## Part 6: Offline Sync & Bridge Configuration

### 6.1 Nextcloud Offline Sync (WebDAV)

Nextcloud handles offline sync via WebDAV protocol. Clients automatically queue changes offline and sync when reconnected.

**Client Setup**:
- **Desktop**: Install Nextcloud Desktop Client → enable offline sync
- **Mobile**: Install Nextcloud app → enable offline files
- **Browser**: OnlyOffice automatically syncs when online

### 6.2 Matrix Offline Message Queueing

**Built into Synapse** - Element Web messages typed offline queue locally, send when reconnected.

### 6.3 Matrix-Meshtastic Bridge (Contingency)

**Current Status**: No active bridge project found (June 2026).
**Fallback**: Use Matrix + Element for primary communication, separate LoRa client for extreme scenarios.

---

## Part 7: User Onboarding Automation

### 7.1 Bulk User Import Script (Python)

```python
#!/usr/bin/env python3
import requests
import json
import sys
from datetime import datetime

NEXTCLOUD_URL = "https://nextcloud.example.com"
NEXTCLOUD_ADMIN_USER = "admin"
NEXTCLOUD_ADMIN_PASSWORD = "YOUR_PASSWORD"
MATRIX_URL = "https://matrix.example.com"
MATRIX_ADMIN_TOKEN = "syt_admin_YOUR_TOKEN"
MATRIX_SERVER_NAME = "example.com"

def create_nextcloud_user(username, password, email, display_name):
    url = f"{NEXTCLOUD_URL}/ocs/v2.php/apps/admin_audit/api/v1/users"
    auth = (NEXTCLOUD_ADMIN_USER, NEXTCLOUD_ADMIN_PASSWORD)
    data = {
        'userid': username,
        'password': password,
        'email': email,
        'displayName': display_name
    }
    headers = {'OCS-APIRequest': 'true'}
    response = requests.post(url, auth=auth, data=data, headers=headers, verify=False)
    if response.status_code in [200, 201]:
        print(f"✓ Nextcloud user: {username}")
        return True
    else:
        print(f"✗ Nextcloud failed: {username}")
        return False

def create_matrix_user(username, password):
    url = f"{MATRIX_URL}/_synapse/admin/v2/users/@{username}:{MATRIX_SERVER_NAME}"
    headers = {
        'Authorization': f'Bearer {MATRIX_ADMIN_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {'password': password, 'deactivated': False, 'admin': False}
    response = requests.put(url, headers=headers, json=data, verify=False)
    if response.status_code in [200, 201]:
        print(f"✓ Matrix user: {username}")
        return True
    else:
        print(f"✗ Matrix failed: {username}")
        return False

def main():
    import csv
    if len(sys.argv) < 2:
        print("Usage: python import_users.py users.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row['username'].strip()
            password = row['password'].strip()
            email = row['email'].strip()
            display_name = row['display_name'].strip()
            
            nc_ok = create_nextcloud_user(username, password, email, display_name)
            mx_ok = create_matrix_user(username, password)
            
            if nc_ok and mx_ok:
                print(f"✓ Complete: {username}\n")

if __name__ == '__main__':
    main()
```

---

## Part 8: Troubleshooting Guide

### Common Failures & Remediation

**nginx 502 Bad Gateway**:
```bash
docker compose logs nextcloud | head -20
docker compose restart nextcloud
```

**Nextcloud Database Error**:
```bash
docker compose exec postgres psql -U nextcloud_matrix_user << 'EOF'
\l
EOF
```

**Element Web Blank Page**:
```bash
docker compose exec element cat /app/config.json | jq .
docker compose restart element
```

**Certificate Renewal Failed**:
```bash
docker compose exec certbot certbot renew --force-renewal
```

---

## Part 9: Backup & Recovery

### 9.1 Backup Script

```bash
#!/bin/bash
BACKUP_DIR="/mnt/backup/nextcloud-matrix-$(date +%Y-%m-%d)"
DOCKER_COMPOSE_DIR="/home/docker-deploy/nextcloud-matrix"

mkdir -p "$BACKUP_DIR"

# Backup PostgreSQL
docker compose -f "$DOCKER_COMPOSE_DIR/docker-compose.yml" exec postgres \
  pg_dump -U nextcloud_matrix_user nextcloud_matrix_db > "$BACKUP_DIR/nextcloud.sql"

docker compose -f "$DOCKER_COMPOSE_DIR/docker-compose.yml" exec postgres \
  pg_dump -U nextcloud_matrix_user nextcloud_matrix_db_synapse > "$BACKUP_DIR/synapse.sql"

# Backup file data
tar -czf "$BACKUP_DIR/nextcloud-data.tar.gz" \
  -C "$DOCKER_COMPOSE_DIR/data" nextcloud/

tar -czf "$BACKUP_DIR/matrix-data.tar.gz" \
  -C "$DOCKER_COMPOSE_DIR/data" matrix/

du -sh "$BACKUP_DIR"
find /mnt/backup -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null

echo "✓ Backup complete: $BACKUP_DIR"
```

---

## Part 10: Success Criteria & Go-Live

### Pre-Go-Live Checklist

- [ ] All 6 containers healthy
- [ ] Nextcloud login works (admin + test user)
- [ ] Matrix user creation works
- [ ] Element Web loads and displays homeserver
- [ ] Document creation + editing + save works
- [ ] Offline sync works (Nextcloud Desktop Client)
- [ ] Matrix offline message queueing works
- [ ] Certificates valid
- [ ] DNS resolves correctly
- [ ] Backup script runs successfully
- [ ] 5 test users created and can log in

### Go-Live Timeline

**June 5, 06:00 UTC**: Final validation (30 min)  
**June 5, 06:30 UTC**: Load 80 test users (15 min)  
**June 5, 12:00 UTC**: Announce platform access  
**June 5, 13:00 UTC**: Wave 1 author recruitment kickoff

---

**Document Version**: 1.0 (June 3, 2026)  
**Last Updated**: June 3, 2026  
**Status**: Ready for Production Deployment

