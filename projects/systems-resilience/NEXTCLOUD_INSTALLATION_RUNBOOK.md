---
title: "Nextcloud + Matrix Installation Runbook — Execute Today"
project: systems-resilience
platform: "Nextcloud 29 + Matrix Synapse + Element Web"
created: 2026-06-14
host: "raspby1 — 100.120.18.84 (Tailscale)"
status: "READY TO EXECUTE (if Nextcloud+Matrix chosen)"
estimated_duration: "4–6 hours"
prerequisites: "SMTP credentials + hostname decision + acknowledgment of ARM64/RAM limitations"
warning: "OnlyOffice (collaborative editing) is NOT available on Pi5 ARM64. Real-time co-editing is not possible on this hardware."
---

# Nextcloud + Matrix Installation Runbook
## Execute on raspby1 — June 14-15, 2026

**Time estimate**: 4–6 hours from start to live platform  
**Warning**: This runbook is for the non-recommended path. See `PLATFORM_DECISION_MATRIX_WITH_RUNBOOKS.md` for the full recommendation context. OnlyOffice (collaborative editing) has no ARM64 Docker image and is unavailable on Pi5.

---

## Prerequisites

Before starting, confirm or provide the following:

- [ ] **SMTP credentials** — host, port, username, password
- [ ] **Hostname for Nextcloud**: e.g., `nextcloud.raspby1.your-tailnet.ts.net`
- [ ] **Hostname for Matrix**: e.g., `matrix.raspby1.your-tailnet.ts.net`
- [ ] **Nextcloud admin username + password** (you choose)
- [ ] **Acknowledgment**: OnlyOffice is not available on Pi5 ARM64; collaborative in-browser editing is not possible
- [ ] **Acknowledgment**: RAM headroom is 1.7–4 GB at 100 users; some degradation expected at peak

---

## Phase 1: System Check (20 min)

```bash
# SSH to raspby1
ssh awank@raspby1

# Confirm ARM64
uname -m
# Expected: aarch64

# Confirm Docker
docker --version && docker compose version
# Expected: Docker 20.x, compose 2.x

# Confirm disk space
df -h /
# Expected: 100+ GB available

# Confirm ports free
sudo ss -tlnp | grep -E ':80|:443'
# Expected: no output

# Check available RAM (need at least 6 GB available for stack startup)
free -h
# Expected: Mem available > 6 GB on a fresh boot

# Confirm Tailscale working
tailscale status --json | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('IP:', d['Self']['TailscaleIPs'][0])
print('Hostname:', d['Self']['DNSName'].rstrip('.'))
"
```

---

## Phase 2: Create Working Directory and Config Files (60 min)

```bash
sudo mkdir -p /opt/nextcloud-matrix/{nginx,synapse,element}
sudo chown -R $USER:$USER /opt/nextcloud-matrix
cd /opt/nextcloud-matrix
```

### 2.1 Generate Secrets

```bash
# Generate all required secrets
POSTGRES_PASSWORD=$(openssl rand -hex 24)
NEXTCLOUD_ADMIN_PASSWORD=$(openssl rand -hex 16)
REGISTRATION_SECRET=$(openssl rand -hex 24)

echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD"
echo "NEXTCLOUD_ADMIN_PASSWORD=$NEXTCLOUD_ADMIN_PASSWORD"
echo "REGISTRATION_SECRET=$REGISTRATION_SECRET"
# Save these to your password manager before continuing
```

### 2.2 Database Init Script

```bash
cat > /opt/nextcloud-matrix/init-multiple-databases.sh << 'EOF'
#!/bin/bash
set -e
# Creates both nextcloud and synapse databases on first PostgreSQL startup
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE synapse;
    GRANT ALL PRIVILEGES ON DATABASE synapse TO "$POSTGRES_USER";
    CREATE DATABASE nextcloud;
    GRANT ALL PRIVILEGES ON DATABASE nextcloud TO "$POSTGRES_USER";
EOSQL
echo "Databases created: synapse, nextcloud"
EOF
chmod +x /opt/nextcloud-matrix/init-multiple-databases.sh
```

### 2.3 Synapse Configuration

First generate the signing key and base config:

```bash
# Generate Synapse homeserver.yaml and signing key
docker run --rm \
    -v /opt/nextcloud-matrix/synapse:/data \
    -e SYNAPSE_SERVER_NAME=REPLACE_MATRIX_HOSTNAME \
    -e SYNAPSE_REPORT_STATS=no \
    matrixdotorg/synapse:latest generate
# This writes /opt/nextcloud-matrix/synapse/homeserver.yaml and signing key
```

Then edit `/opt/nextcloud-matrix/synapse/homeserver.yaml` to add PostgreSQL connection:

```bash
# Replace the sqlite3 database block with PostgreSQL:
cat >> /opt/nextcloud-matrix/synapse/homeserver.yaml << 'EOF'

# Replace the default sqlite3 database section with this:
database:
  name: psycopg2
  args:
    user: REPLACE_POSTGRES_USER
    password: REPLACE_POSTGRES_PASSWORD
    database: synapse
    host: postgres
    cp_min: 5
    cp_max: 10
registration_shared_secret: "REPLACE_REGISTRATION_SECRET"
EOF
```

### 2.4 Element Web Config

```bash
cat > /opt/nextcloud-matrix/element/config.json << 'EOF'
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "https://REPLACE_MATRIX_HOSTNAME",
            "server_name": "REPLACE_MATRIX_HOSTNAME"
        }
    },
    "brand": "Systems Resilience Community",
    "showLabsSettings": false,
    "default_theme": "light"
}
EOF
# Replace REPLACE_MATRIX_HOSTNAME with your actual Matrix hostname
```

### 2.5 nginx Configuration

```bash
cat > /opt/nextcloud-matrix/nginx/nginx.conf << 'EOF'
# nginx reverse proxy for Nextcloud + Matrix + Element
# Pi5 ARM64 deployment

events {
    worker_connections 512;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    sendfile on;
    client_max_body_size 512M;
    
    # Nextcloud
    upstream nextcloud_fpm {
        server nextcloud:9000;
    }
    
    server {
        listen 443 ssl http2;
        server_name REPLACE_NEXTCLOUD_HOSTNAME;
        
        ssl_certificate /etc/nginx/certs/cert.pem;
        ssl_certificate_key /etc/nginx/certs/key.pem;
        
        root /var/www/html;
        
        location / {
            try_files $uri $uri/ /index.php$request_uri;
        }
        
        location ~ \.php(?:$|/) {
            fastcgi_split_path_info ^(.+?\.php)(/.*)$;
            fastcgi_param PATH_INFO $fastcgi_path_info;
            fastcgi_param HTTPS on;
            fastcgi_param modHeadersAvailable true;
            fastcgi_param front_controller_active true;
            fastcgi_pass nextcloud:9000;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_intercept_errors on;
            fastcgi_request_buffering off;
            fastcgi_read_timeout 300;
        }
        
        # Nextcloud well-known
        location ^~ /.well-known {
            return 301 $scheme://$host/index.php$request_uri;
        }
        
        # Health check
        location /nginx-health {
            return 200 "OK";
        }
    }
    
    # Matrix Synapse
    server {
        listen 443 ssl http2;
        server_name REPLACE_MATRIX_HOSTNAME;
        
        ssl_certificate /etc/nginx/certs/cert.pem;
        ssl_certificate_key /etc/nginx/certs/key.pem;
        
        location / {
            proxy_pass http://synapse:8008;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host $host;
            client_max_body_size 50M;
        }
    }
    
    # Element Web
    server {
        listen 443 ssl http2;
        server_name REPLACE_ELEMENT_HOSTNAME;
        
        ssl_certificate /etc/nginx/certs/cert.pem;
        ssl_certificate_key /etc/nginx/certs/key.pem;
        
        root /usr/share/nginx/html;
        index index.html;
        
        location / {
            try_files $uri $uri/ /index.html;
        }
    }
    
    # HTTP → HTTPS redirect
    server {
        listen 80;
        server_name _;
        return 301 https://$host$request_uri;
    }
}
EOF
```

Replace `REPLACE_NEXTCLOUD_HOSTNAME`, `REPLACE_MATRIX_HOSTNAME`, `REPLACE_ELEMENT_HOSTNAME` with actual hostnames.

### 2.6 docker-compose.yml

```bash
cat > /opt/nextcloud-matrix/docker-compose.yml << 'COMPOSE_EOF'
# Nextcloud + Matrix docker-compose.yml
# Pi5 ARM64 — fill in all REPLACE_* values before starting

networks:
  backend:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  nextcloud_html:
  nextcloud_data:
  nextcloud_config:
  nginx_certs:
  synapse_data:

services:

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    networks: [backend]
    environment:
      POSTGRES_USER: REPLACE_POSTGRES_USER
      POSTGRES_PASSWORD: REPLACE_POSTGRES_PASSWORD
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-multiple-databases.sh:/docker-entrypoint-initdb.d/init.sh:ro
    command: >
      postgres
        -c shared_buffers=256MB
        -c effective_cache_size=512MB
        -c work_mem=32MB
        -c max_connections=100
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U REPLACE_POSTGRES_USER"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 60s

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    networks: [backend]
    command: redis-server --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes: [redis_data:/data]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 10s
      retries: 5

  nextcloud:
    image: nextcloud:29-fpm-alpine
    restart: unless-stopped
    networks: [backend]
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: nextcloud
      POSTGRES_USER: REPLACE_POSTGRES_USER
      POSTGRES_PASSWORD: REPLACE_POSTGRES_PASSWORD
      REDIS_HOST: redis
      NEXTCLOUD_ADMIN_USER: REPLACE_NEXTCLOUD_ADMIN_USER
      NEXTCLOUD_ADMIN_PASSWORD: REPLACE_NEXTCLOUD_ADMIN_PASSWORD
      NEXTCLOUD_TRUSTED_DOMAINS: "REPLACE_NEXTCLOUD_HOSTNAME"
      SMTP_HOST: REPLACE_SMTP_HOST
      SMTP_SECURE: tls
      SMTP_PORT: 587
      SMTP_AUTHTYPE: LOGIN
      SMTP_NAME: REPLACE_SMTP_USER
      SMTP_PASSWORD: REPLACE_SMTP_PASSWORD
      MAIL_FROM_ADDRESS: noreply
      MAIL_DOMAIN: REPLACE_YOUR_DOMAIN
      PHP_UPLOAD_LIMIT: 512M
      PHP_MEMORY_LIMIT: 512M
    volumes:
      - nextcloud_html:/var/www/html
      - nextcloud_data:/var/www/html/data
      - nextcloud_config:/var/www/html/config
    healthcheck:
      test: ["CMD-SHELL", "php-fpm -t && echo OK || exit 1"]
      interval: 60s
      timeout: 30s
      retries: 3
      start_period: 120s
    deploy:
      resources:
        limits:
          memory: 1536M

  synapse:
    image: matrixdotorg/synapse:latest
    restart: unless-stopped
    networks: [backend]
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - synapse_data:/data
      - ./synapse/homeserver.yaml:/data/homeserver.yaml:ro
    healthcheck:
      test: ["CMD-SHELL", "curl -sf http://localhost:8008/_matrix/client/versions || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 90s
    deploy:
      resources:
        limits:
          memory: 1G

  element:
    image: vectorim/element-web:latest
    restart: unless-stopped
    networks: [backend]
    volumes:
      - ./element/config.json:/app/config/config.json:ro
    deploy:
      resources:
        limits:
          memory: 256M

  nginx:
    image: nginx:alpine
    restart: unless-stopped
    networks: [backend]
    depends_on: [nextcloud, synapse, element]
    ports:
      # CRITICAL: Tailscale IP only — NEVER 0.0.0.0
      - "100.120.18.84:80:80"
      - "100.120.18.84:443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - nginx_certs:/etc/nginx/certs
      - nextcloud_html:/var/www/html:ro
    deploy:
      resources:
        limits:
          memory: 128M
COMPOSE_EOF
```

Replace all `REPLACE_*` placeholders with actual values.

---

## Phase 3: SSL Certificate Setup (30 min)

```bash
# Create certs directory
mkdir -p /opt/nextcloud-matrix/nginx/certs

# Option A: Tailscale cert (recommended)
tailscale_host=$(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
sudo tailscale cert "$tailscale_host"
sudo cp /var/lib/tailscale/certs/$tailscale_host.crt /opt/nextcloud-matrix/nginx/certs/cert.pem
sudo cp /var/lib/tailscale/certs/$tailscale_host.key /opt/nextcloud-matrix/nginx/certs/key.pem
sudo chown $USER:$USER /opt/nextcloud-matrix/nginx/certs/*.pem

# Option B: Self-signed (fallback)
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /opt/nextcloud-matrix/nginx/certs/key.pem \
    -out /opt/nextcloud-matrix/nginx/certs/cert.pem \
    -subj "/CN=REPLACE_NEXTCLOUD_HOSTNAME/O=Systems Resilience"
```

---

## Phase 4: Start Stack (30 min)

```bash
cd /opt/nextcloud-matrix

# Pull all images first (shows download progress)
docker compose pull

# Start the stack
docker compose up -d

# Watch all services come up
watch docker compose ps
# Wait until all services show "healthy" — takes 3–5 minutes
# Nextcloud has a 120-second start_period due to PHP initialization
```

### Verify All Services Healthy

```bash
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Health}}"
# Expected: all services show "Up" and "healthy"

# If a service is unhealthy:
docker compose logs [service-name] --tail=50
```

---

## Phase 5: Nextcloud Post-Installation (30 min)

```bash
# Wait for Nextcloud to fully initialize (check logs first)
docker compose logs nextcloud --tail=20

# Configure trusted proxy (nginx is the reverse proxy)
docker compose exec nextcloud php occ config:system:set trusted_proxies 0 --value="nginx"

# Force HTTPS
docker compose exec nextcloud php occ config:system:set overwriteprotocol --value="https"
docker compose exec nextcloud php occ config:system:set overwrite.cli.url --value="https://REPLACE_NEXTCLOUD_HOSTNAME"

# Configure Redis session caching
docker compose exec nextcloud php occ config:system:set redis host --value="redis"
docker compose exec nextcloud php occ config:system:set redis port --value="6379" --type=integer
docker compose exec nextcloud php occ config:system:set memcache.local --value="\\OC\\Memcache\\Redis"
docker compose exec nextcloud php occ config:system:set memcache.distributed --value="\\OC\\Memcache\\Redis"
docker compose exec nextcloud php occ config:system:set memcache.locking --value="\\OC\\Memcache\\Redis"

# Verify Nextcloud status
docker compose exec nextcloud php occ status
# Expected: installed: true, maintenance: false
```

---

## Phase 6: Matrix Synapse Setup (30 min)

```bash
# Check Synapse is running and responding
curl -sf http://100.120.18.84/_matrix/client/versions 2>/dev/null | python3 -m json.tool | head -5
# If Synapse is behind nginx: curl -sk https://REPLACE_MATRIX_HOSTNAME/_matrix/client/versions

# Create admin user in Synapse
docker compose exec synapse register_new_matrix_user \
    -u admin \
    -p REPLACE_MATRIX_ADMIN_PASSWORD \
    -a \
    -c /data/homeserver.yaml \
    http://localhost:8008
# Expected: Success

# Verify Matrix version endpoint
curl -sk https://REPLACE_MATRIX_HOSTNAME/_matrix/client/versions | python3 -m json.tool | grep versions
```

---

## Phase 7: Validation (30 min)

```bash
# Nextcloud health check
curl -sk https://REPLACE_NEXTCLOUD_HOSTNAME/status.php | python3 -m json.tool
# Expected: {"installed":true,"maintenance":false,"needsDbUpgrade":false,...}

# Matrix federation check
curl -sf https://REPLACE_MATRIX_HOSTNAME/_matrix/federation/v1/version | python3 -m json.tool
# Expected: {"server":{"name":"Synapse","version":"..."}}

# Element Web check
curl -sk https://REPLACE_ELEMENT_HOSTNAME/ | grep -q "Element" && echo "Element: OK" || echo "Element: FAIL"

# Check RAM usage
free -h
# Check all container RAM
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}"
# Total should be < 5 GB on idle stack
```

---

## Phase 8: Backup Setup (20 min)

```bash
cat > /opt/nextcloud-matrix-backup.sh << 'EOF'
#!/bin/bash
set -euo pipefail
BACKUP_DIR="/home/awank/backups/nextcloud-matrix"
DATE=$(date -u +%Y-%m-%d)
LOG="/var/log/nextcloud-matrix-backup.log"
COMPOSE_DIR="/opt/nextcloud-matrix"

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting backup..." >> "$LOG"
mkdir -p "$BACKUP_DIR/$DATE"

# PostgreSQL dump (both databases)
docker compose -f "$COMPOSE_DIR/docker-compose.yml" exec -T postgres \
    pg_dumpall -U REPLACE_POSTGRES_USER | gzip > "$BACKUP_DIR/$DATE/postgres-all.sql.gz"

# Nextcloud config
docker run --rm \
    -v nextcloud-matrix_nextcloud_config:/data alpine \
    tar czf - /data > "$BACKUP_DIR/$DATE/nextcloud-config.tar.gz"

# Synapse signing key
docker run --rm \
    -v nextcloud-matrix_synapse_data:/data alpine \
    tar czf - /data > "$BACKUP_DIR/$DATE/synapse-data.tar.gz"

# Prune old backups (keep 14 days)
find "$BACKUP_DIR" -maxdepth 1 -type d -mtime +14 -exec rm -rf {} \; 2>/dev/null || true

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Backup complete: $(du -sh "$BACKUP_DIR/$DATE" | cut -f1)" >> "$LOG"
EOF

chmod +x /opt/nextcloud-matrix-backup.sh
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/nextcloud-matrix-backup.sh") | crontab -
crontab -l | grep nextcloud-matrix-backup
```

---

## Deployment Complete Checklist

- [ ] All containers show "healthy" in `docker compose ps`
- [ ] Nextcloud accessible at `https://REPLACE_NEXTCLOUD_HOSTNAME/status.php` (JSON response)
- [ ] Nextcloud admin login works via browser
- [ ] Matrix Synapse responds at `/_matrix/client/versions`
- [ ] Element Web loads in browser
- [ ] Redis caching configured (`php occ config:system:get memcache.local` returns Redis)
- [ ] Synapse admin user created
- [ ] Backup script installed and verified
- [ ] RAM usage at idle < 3 GB total (`free -h` shows > 4 GB available)
- [ ] SMTP test email sent (or failure documented)

**When all checked**: Platform is live and ready for Phase 5.1 publication.

---

## Quick Reference

```bash
# Start stack
cd /opt/nextcloud-matrix && docker compose up -d

# Stop stack
cd /opt/nextcloud-matrix && docker compose down

# Restart a service
cd /opt/nextcloud-matrix && docker compose restart [service]

# View logs
cd /opt/nextcloud-matrix && docker compose logs --tail=50 [service]

# Nextcloud admin CLI
docker compose exec nextcloud php occ [command]

# Check RAM
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}"

# Enter PostgreSQL
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -d nextcloud
```

**Cross-references**: `NEXTCLOUD_DEPLOYMENT_TECHNICAL_SPEC.md`, `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` (comprehensive, existing), `DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md`, `docker-compose-nextcloud-matrix.yml` (existing template)
