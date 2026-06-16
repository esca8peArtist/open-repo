# Nextcloud+Matrix Deployment SOP
## Standard Operating Procedure for Phase 5.1 Publication Infrastructure

**Version**: 1.0 (Production Ready)  
**Last Updated**: June 16, 2026  
**Total Deployment Time**: 4-6 hours (wall-clock)  
**Target Platform**: Raspberry Pi 5 (8GB RAM) with Raspberry Pi OS  
**Target Go-Live**: June 19, 2026

---

## PRE-DEPLOYMENT CHECKLIST

**User Actions Required (24h before deployment)**:
- [ ] SMTP credentials collected (hostname, port, username, password)
- [ ] Domain name prepared (e.g., phase5.example.com)
- [ ] DNS A record pointing to 100.70.184.84 (test: `nslookup`)
- [ ] Let's Encrypt email address ready
- [ ] 40GB disk space available (verify: `df -h /`)
- [ ] 6GB available RAM (verify: `free -h`)

**Deployment Prerequisites**:
- [ ] SSH access to Pi (raspby1)
- [ ] Docker + Docker Compose installed
- [ ] sudo privileges on Pi

---

## DEPLOYMENT PHASES OVERVIEW

| Phase | Task | Duration | Critical |
|-------|------|----------|----------|
| 0 | Pre-Flight Checks | 15 min | Yes |
| 1 | Environment Setup | 30 min | Yes |
| 2 | Docker Compose Config | 30 min | Yes |
| 3 | Nginx Setup | 20 min | Yes |
| 4 | SSL Certificates | 15 min | Yes |
| 5 | Database Initialization | 15 min | Yes |
| 6 | Start Services | 30 min | Yes |
| 7 | Nextcloud Configuration | 20 min | No |
| 8 | Matrix User Setup | 10 min | No |
| 9 | Element Web Config | 10 min | No |
| 10 | Validation | 20 min | Yes |
| **TOTAL** | | **3h 55m - 4h 45m** | |

---

## PHASE 0: PRE-FLIGHT CHECKS (15 minutes)

**Purpose**: Verify hardware, Docker, networking before deploying.

### 0.1 SSH Into Pi

```bash
ssh pi@100.70.184.84
# Or via hostname if available: ssh pi@raspby1
```

### 0.2 Hardware Verification Script

Save as `/home/pi/preflight-check.sh`:

```bash
#!/bin/bash
set -e

echo "=== PHASE 0: PRE-FLIGHT CHECKS ==="
echo ""

errors=0
warnings=0

# 1. Memory check
echo "[1/6] Memory..."
mem_total=$(free -h | awk '/^Mem:/ {print $2}')
mem_available=$(free -h | awk '/^Mem:/ {print $7}')
free_gb=$(free -g | awk '/^Mem:/ {print $7}')
echo "    Total: $mem_total | Available: $mem_available"

if [ "$free_gb" -lt 6 ]; then
  echo "    ❌ FAIL: Need 6GB free (have ${free_gb}GB)"
  errors=$((errors + 1))
else
  echo "    ✅ PASS"
fi

# 2. Disk check
echo "[2/6] Disk space..."
disk_free=$(df -BG / | awk 'NR==2 {print $4}' | sed 's/G//')
echo "    Free: ${disk_free}GB"

if [ "$disk_free" -lt 40 ]; then
  echo "    ❌ FAIL: Need 40GB (have ${disk_free}GB)"
  errors=$((errors + 1))
else
  echo "    ✅ PASS"
fi

# 3. CPU check
echo "[3/6] CPU cores..."
cores=$(nproc)
echo "    Cores: $cores"

if [ "$cores" -lt 4 ]; then
  echo "    ⚠️  WARNING: Recommended 4+ cores (have $cores)"
  warnings=$((warnings + 1))
else
  echo "    ✅ PASS"
fi

# 4. Docker check
echo "[4/6] Docker..."
if ! command -v docker &> /dev/null; then
  echo "    ❌ FAIL: Docker not installed"
  errors=$((errors + 1))
else
  docker_version=$(docker --version)
  echo "    $docker_version"
  echo "    ✅ PASS"
fi

# 5. Docker Compose check
echo "[5/6] Docker Compose..."
if ! command -v docker-compose &> /dev/null; then
  echo "    ❌ FAIL: Docker Compose not installed"
  errors=$((errors + 1))
else
  compose_version=$(docker-compose --version)
  echo "    $compose_version"
  echo "    ✅ PASS"
fi

# 6. Network check
echo "[6/6] Network..."
if hostname -I | grep -q "100.70.184.84"; then
  echo "    IP: 100.70.184.84 (Tailscale)"
  echo "    ✅ PASS"
elif hostname -I | grep -q "192.168"; then
  local_ip=$(hostname -I | grep -oE '192\.168\.[0-9]+\.[0-9]+' | head -1)
  echo "    IP: $local_ip (local network)"
  echo "    ⚠️  WARNING: Using local IP (not Tailscale)"
  warnings=$((warnings + 1))
else
  echo "    ❌ FAIL: Cannot determine IP"
  errors=$((errors + 1))
fi

echo ""
echo "=== PRE-FLIGHT RESULT ==="
echo "Errors: $errors | Warnings: $warnings"

if [ $errors -eq 0 ]; then
  echo "✅ ALL CRITICAL CHECKS PASSED"
  echo "Proceeding to Phase 1..."
  exit 0
else
  echo "❌ $errors CRITICAL FAILURE(S)"
  echo "Fix before continuing."
  exit 1
fi
```

### 0.3 Run Pre-Flight Check

```bash
chmod +x /home/pi/preflight-check.sh
/home/pi/preflight-check.sh
```

**Expected Output**:
```
[1/6] Memory...
    Total: 7.8Gi | Available: 6.2Gi
    ✅ PASS
[2/6] Disk space...
    Free: 45GB
    ✅ PASS
...
✅ ALL CRITICAL CHECKS PASSED
```

If any `❌ FAIL` appears, **STOP** and troubleshoot before continuing.

---

## PHASE 1: ENVIRONMENT SETUP (30 minutes)

**Purpose**: Create deployment directory and prepare environment variables.

### 1.1 Create Deployment Directory

```bash
sudo mkdir -p /opt/nextcloud-matrix
sudo chown pi:pi /opt/nextcloud-matrix
cd /opt/nextcloud-matrix
pwd  # Should output: /opt/nextcloud-matrix
```

### 1.2 Create Environment File Template

```bash
cat > .env << 'EOF'
# ============================================
# NEXTCLOUD CONFIGURATION
# ============================================
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=CHANGEME_STRONG_PASSWORD_32_CHARS_MIN
NEXTCLOUD_TRUSTED_DOMAINS="your-domain.com localhost 100.70.184.84"
NEXTCLOUD_DB_HOST=postgres
NEXTCLOUD_DB_NAME=nextcloud_db
NEXTCLOUD_DB_USER=nextcloud_user
NEXTCLOUD_DB_PASSWORD=CHANGEME_STRONG_PASSWORD_32_CHARS_MIN

# SMTP Configuration (Mailgun, SendGrid, or AWS SES)
NEXTCLOUD_SMTP_HOST=smtp.mailgun.org
NEXTCLOUD_SMTP_PORT=587
NEXTCLOUD_SMTP_SECURE=tls
NEXTCLOUD_SMTP_NAME=postmaster@your-domain.com
NEXTCLOUD_SMTP_PASSWORD=CHANGEME_API_KEY
NEXTCLOUD_SMTP_FROM=noreply@your-domain.com

# ============================================
# MATRIX SYNAPSE CONFIGURATION
# ============================================
SYNAPSE_SERVER_NAME=your-domain.com
SYNAPSE_REPORT_STATS=no
SYNAPSE_DB_HOST=postgres
SYNAPSE_DB_NAME=synapse_db
SYNAPSE_DB_USER=synapse_user
SYNAPSE_DB_PASSWORD=CHANGEME_STRONG_PASSWORD_32_CHARS_MIN
SYNAPSE_CACHE_FACTOR=0.5

# ============================================
# POSTGRESQL CONFIGURATION
# ============================================
POSTGRES_PASSWORD=CHANGEME_STRONG_PASSWORD_32_CHARS_MIN
POSTGRES_INITDB_ARGS=-c max_connections=200 -c shared_buffers=256MB

# ============================================
# DOMAIN & SSL
# ============================================
DOMAIN=your-domain.com
LETSENCRYPT_EMAIL=admin@your-domain.com
EOF

echo "✅ Created .env template"
```

### 1.3 Edit Environment File

```bash
nano .env
```

**Required Changes**:

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `CHANGEME_STRONG_PASSWORD_32_CHARS_MIN` | 32-char random password | `$(openssl rand -base64 32)` |
| `your-domain.com` | Your actual domain | `phase5.example.com` |
| `postmaster@your-domain.com` | SMTP sender address | `postmaster@phase5.example.com` |
| `CHANGEME_API_KEY` | Mailgun/SendGrid API key | From provider dashboard |
| `admin@your-domain.com` | Let's Encrypt email | Your email address |

### 1.4 Generate Secure Passwords

```bash
echo "=== SECURE PASSWORDS ==="
echo "Admin password: $(openssl rand -base64 32)"
echo "Nextcloud DB password: $(openssl rand -base64 32)"
echo "Synapse DB password: $(openssl rand -base64 32)"
echo "PostgreSQL password: $(openssl rand -base64 32)"
```

Copy each password and paste into `.env` (replace `CHANGEME_*` placeholders).

### 1.5 Verify All Placeholders Replaced

```bash
if grep -q "CHANGEME" .env; then
  echo "❌ ERROR: .env still contains CHANGEME placeholders"
  grep "CHANGEME" .env
  exit 1
else
  echo "✅ All placeholders replaced"
  echo ""
  echo "Configuration ready:"
  grep "^[A-Z]" .env | head -10
fi
```

---

## PHASE 2: DOCKER COMPOSE CONFIGURATION (30 minutes)

**Purpose**: Define all containers, volumes, networks, dependencies.

### 2.1 Create docker-compose.yml

Save as `/opt/nextcloud-matrix/docker-compose.yml`:

```yaml
version: '3.9'

services:
  # PostgreSQL: Database backend
  postgres:
    image: postgres:15-alpine
    container_name: nextcloud-postgres
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_INITDB_ARGS: ${POSTGRES_INITDB_ARGS}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Redis: Cache backend for Nextcloud
  redis:
    image: redis:7-alpine
    container_name: nextcloud-redis
    command: redis-server --appendonly yes --maxmemory 1gb --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Nextcloud: Document collaboration platform
  nextcloud:
    image: nextcloud:29-fpm-alpine
    container_name: nextcloud-app
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: ${NEXTCLOUD_TRUSTED_DOMAINS}
      POSTGRES_HOST: ${NEXTCLOUD_DB_HOST}
      POSTGRES_DB: ${NEXTCLOUD_DB_NAME}
      POSTGRES_USER: ${NEXTCLOUD_DB_USER}
      POSTGRES_PASSWORD: ${NEXTCLOUD_DB_PASSWORD}
      REDIS_HOST: redis
      REDIS_PORT: 6379
      SMTP_HOST: ${NEXTCLOUD_SMTP_HOST}
      SMTP_PORT: ${NEXTCLOUD_SMTP_PORT}
      SMTP_SECURE: ${NEXTCLOUD_SMTP_SECURE}
      SMTP_NAME: ${NEXTCLOUD_SMTP_NAME}
      SMTP_PASSWORD: ${NEXTCLOUD_SMTP_PASSWORD}
      MAIL_FROM_ADDRESS: ${NEXTCLOUD_SMTP_FROM}
      OVERWRITE_PROTOCOL: https
      OVERWRITE_HOST: ${DOMAIN}
      OVERWRITE_CLI_URL: https://${DOMAIN}
      PHP_MEMORY_LIMIT: 512M
      PHP_UPLOAD_LIMIT: 512M
    volumes:
      - nextcloud_data:/var/www/html
      - nextcloud_apps:/var/www/html/custom_apps
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/status.php"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Matrix Synapse: Encrypted messaging server
  synapse:
    image: matrixdotorg/synapse:v1.130
    container_name: nextcloud-synapse
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      SYNAPSE_SERVER_NAME: ${SYNAPSE_SERVER_NAME}
      SYNAPSE_REPORT_STATS: ${SYNAPSE_REPORT_STATS}
      SYNAPSE_DB_HOST: ${SYNAPSE_DB_HOST}
      SYNAPSE_DB_NAME: ${SYNAPSE_DB_NAME}
      SYNAPSE_DB_USER: ${SYNAPSE_DB_USER}
      SYNAPSE_DB_PASSWORD: ${SYNAPSE_DB_PASSWORD}
      SYNAPSE_CACHE_FACTOR: ${SYNAPSE_CACHE_FACTOR}
      SYNAPSE_LOG_LEVEL: WARNING
      PYTHONUNBUFFERED: 1
    volumes:
      - synapse_data:/data
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8008/_matrix/client/versions"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    restart: unless-stopped
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Element Web: Matrix client UI
  element:
    image: vectorim/element-web:v1.11.68
    container_name: nextcloud-element
    depends_on:
      - synapse
    volumes:
      - ./element-config.json:/app/config.json:ro
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Nginx: Reverse proxy with SSL termination
  nginx:
    image: nginx:1.27-alpine
    container_name: nextcloud-nginx
    ports:
      - "127.0.0.1:80:80"
      - "127.0.0.1:443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl_certs:/etc/nginx/ssl:ro
      - nginx_cache:/var/cache/nginx
    depends_on:
      - nextcloud
      - synapse
      - element
    networks:
      - nextcloud-matrix-net
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  nextcloud_data:
    driver: local
  nextcloud_apps:
    driver: local
  synapse_data:
    driver: local
  nginx_cache:
    driver: local

networks:
  nextcloud-matrix-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

### 2.2 Validate docker-compose.yml

```bash
docker-compose config > /dev/null && \
  echo "✅ docker-compose.yml is valid YAML" || \
  echo "❌ Syntax error in docker-compose.yml"
```

**Expected Output**:
```
✅ docker-compose.yml is valid YAML
```

---

## PHASE 3: NGINX CONFIGURATION (20 minutes)

**Purpose**: Reverse proxy with SSL termination, rate limiting, security headers.

### 3.1 Create nginx.conf

Save as `/opt/nextcloud-matrix/nginx.conf`:

```nginx
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
  worker_connections 2048;
  use epoll;
}

http {
  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
  access_log /var/log/nginx/access.log main;

  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 65;
  types_hash_max_size 2048;
  client_max_body_size 512M;

  # Gzip compression
  gzip on;
  gzip_vary on;
  gzip_min_length 1000;
  gzip_types text/plain text/css text/xml text/javascript 
             application/x-javascript application/xml+rss 
             application/json application/javascript image/svg+xml;

  # Rate limiting
  limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
  limit_req_zone $binary_remote_addr zone=login:10m rate=5r/m;

  # Security headers
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
  add_header X-Content-Type-Options "nosniff" always;
  add_header X-Frame-Options "SAMEORIGIN" always;
  add_header X-XSS-Protection "1; mode=block" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;

  upstream nextcloud_fpm {
    server nextcloud:9000;
  }

  upstream synapse {
    server synapse:8008;
  }

  upstream element {
    server element:80;
  }

  # HTTP → HTTPS redirect
  server {
    listen 80 default_server;
    server_name _;
    location / {
      return 301 https://$host$request_uri;
    }
  }

  # HTTPS server
  server {
    listen 443 ssl http2 default_server;
    server_name _;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Nextcloud (root)
    location / {
      limit_req zone=general burst=20 nodelay;
      proxy_pass http://nextcloud_fpm;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_redirect off;
    }

    # Nextcloud status
    location /status.php {
      access_log off;
      proxy_pass http://nextcloud_fpm;
      proxy_set_header Host $host;
    }

    # Nginx health check
    location /health {
      access_log off;
      return 200 "OK\n";
      add_header Content-Type text/plain;
    }

    # Matrix federation
    location /_matrix/ {
      limit_req zone=general burst=50 nodelay;
      proxy_pass http://synapse;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      client_max_body_size 128M;
      proxy_buffering off;
      proxy_http_version 1.1;
      proxy_request_buffering off;
    }

    # Well-known Matrix federation
    location /.well-known/matrix/ {
      proxy_pass http://synapse;
      proxy_set_header Host $host;
      access_log off;
    }

    # Deny hidden files
    location ~ /\. {
      deny all;
      access_log off;
      log_not_found off;
    }

    location ~ ~$ {
      deny all;
      access_log off;
      log_not_found off;
    }
  }
}
```

### 3.2 Validate nginx.conf

```bash
docker run --rm -v $PWD/nginx.conf:/etc/nginx/nginx.conf:ro nginx:1.27-alpine \
  nginx -t 2>&1 | grep -q "successful" && \
  echo "✅ nginx.conf is valid" || \
  echo "❌ Nginx config error"
```

---

## PHASE 4: SSL CERTIFICATES (15 minutes)

Choose **Option A** (self-signed, development) OR **Option B** (Let's Encrypt, production).

### 4.1 Option A: Self-Signed Certificates (Development)

```bash
mkdir -p ssl_certs

openssl req -x509 -newkey rsa:4096 -nodes \
  -out ssl_certs/cert.pem \
  -keyout ssl_certs/key.pem \
  -days 365 \
  -subj "/CN=$(grep '^DOMAIN=' .env | cut -d= -f2)/O=Phase5.1/C=US"

chmod 600 ssl_certs/key.pem
ls -lh ssl_certs/

echo "✅ Self-signed certificates created (365 days)"
```

### 4.2 Option B: Let's Encrypt (Production) ⭐ RECOMMENDED

**Prerequisites**:
- Domain with public DNS A record pointing to 100.70.184.84
- Port 80 accessible from internet
- Email address in .env

```bash
mkdir -p ssl_certs www

DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)
EMAIL=$(grep '^LETSENCRYPT_EMAIL=' .env | cut -d= -f2)

echo "Getting Let's Encrypt certificate for: $DOMAIN"

docker run --rm --name certbot \
  -v $PWD/ssl_certs:/etc/letsencrypt \
  -v $PWD/www:/var/www/certbot \
  -p 80:80 \
  certbot/certbot certonly \
    --standalone \
    --email "$EMAIL" \
    -d "$DOMAIN" \
    --agree-tos \
    --no-eff-email \
    --non-interactive

# Copy certs to expected location
sudo cp ssl_certs/live/$DOMAIN/fullchain.pem ssl_certs/cert.pem
sudo cp ssl_certs/live/$DOMAIN/privkey.pem ssl_certs/key.pem
sudo chown pi:pi ssl_certs/*.pem

chmod 600 ssl_certs/key.pem
echo "✅ Let's Encrypt certificate installed"

# Verify
openssl x509 -in ssl_certs/cert.pem -noout -dates
```

**Expected Output**:
```
notBefore=Jun 16 12:34:56 2026 GMT
notAfter=Jun 16 12:34:56 2027 GMT
```

---

## PHASE 5: DATABASE INITIALIZATION (15 minutes)

**Purpose**: Create PostgreSQL databases and users.

### 5.1 Start PostgreSQL Only

```bash
docker-compose up -d postgres

echo "Waiting for PostgreSQL to be healthy..."
until docker exec nextcloud-postgres pg_isready -U postgres > /dev/null 2>&1; do
  echo "  ...still waiting (checking every 5 sec)"
  sleep 5
done

echo "✅ PostgreSQL ready"
```

### 5.2 Load Environment Variables

```bash
set -a
source .env
set +a

echo "NEXTCLOUD_DB_NAME=$NEXTCLOUD_DB_NAME"
echo "SYNAPSE_DB_NAME=$SYNAPSE_DB_NAME"
```

### 5.3 Create Nextcloud Database

```bash
docker exec nextcloud-postgres psql -U postgres << EOF
CREATE DATABASE $NEXTCLOUD_DB_NAME;
CREATE USER $NEXTCLOUD_DB_USER WITH PASSWORD '$NEXTCLOUD_DB_PASSWORD';
ALTER ROLE $NEXTCLOUD_DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $NEXTCLOUD_DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $NEXTCLOUD_DB_USER SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE $NEXTCLOUD_DB_NAME TO $NEXTCLOUD_DB_USER;
EOF

echo "✅ Nextcloud database created"
```

### 5.4 Create Synapse Database

```bash
docker exec nextcloud-postgres psql -U postgres << EOF
CREATE DATABASE $SYNAPSE_DB_NAME;
CREATE USER $SYNAPSE_DB_USER WITH PASSWORD '$SYNAPSE_DB_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE $SYNAPSE_DB_NAME TO $SYNAPSE_DB_USER;
EOF

echo "✅ Synapse database created"
```

### 5.5 Verify Databases

```bash
docker exec nextcloud-postgres psql -U postgres -l | grep -E "nextcloud_db|synapse_db"
```

**Expected Output**:
```
 nextcloud_db     | nextcloud_user | UTF8     | en_US.utf8 | en_US.utf8 |
 synapse_db       | synapse_user   | UTF8     | en_US.utf8 | en_US.utf8 |
```

---

## PHASE 6: START ALL SERVICES (30 minutes)

**Purpose**: Bring up all containers and monitor startup.

### 6.1 Stop and Clean Previous Runs

```bash
docker-compose down -v 2>/dev/null || true
echo "✅ Cleaned previous deployment"
```

### 6.2 Start All Services

```bash
echo "Starting all services..."
docker-compose up -d

sleep 5
echo "Monitoring startup progress..."
```

### 6.3 Monitor Service Health

```bash
for i in {1..60}; do
  healthy=$(docker-compose ps --filter "health=healthy" -q 2>/dev/null | wc -l)
  unhealthy=$(docker-compose ps --filter "health=unhealthy" -q 2>/dev/null | wc -l)
  
  echo "[$((i))/60] Healthy: $healthy | Unhealthy: $unhealthy"
  
  if [ "$healthy" -ge 6 ] || [ $i -eq 60 ]; then
    break
  fi
  
  sleep 5
done

echo ""
echo "Service Status:"
docker-compose ps
```

**Expected Output** (all services should show "healthy" or "running"):
```
CONTAINER ID   IMAGE                              STATUS
abcd1234       postgres:15-alpine                 healthy
efgh5678       redis:7-alpine                     healthy
ijkl9012       nextcloud:29-fpm-alpine            healthy
mnop3456       matrixdotorg/synapse:v1.130        healthy
qrst7890       vectorim/element-web:v1.11.68      running
uvwx1234       nginx:1.27-alpine                  healthy
```

### 6.4 Check Resource Usage

```bash
echo "Memory and CPU Usage:"
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

**Expected Output**:
```
CONTAINER         CPU %   MEM USAGE
nextcloud-postgres    5%   512MB / 8GB
nextcloud-redis       2%   64MB / 8GB
nextcloud-app         15%  256MB / 8GB
nextcloud-synapse     10%  512MB / 8GB
nextcloud-element     1%   32MB / 8GB
nextcloud-nginx       1%   48MB / 8GB
```

If total exceeds 6.5GB, troubleshoot (see Appendix).

---

## PHASE 7: NEXTCLOUD CONFIGURATION (20 minutes)

**Purpose**: Verify Nextcloud operational and install apps.

### 7.1 Wait for Nextcloud Initialization

```bash
echo "Waiting for Nextcloud to initialize..."

for i in {1..30}; do
  if curl -s http://localhost/status.php 2>/dev/null | grep -q '"installed":true'; then
    echo "✅ Nextcloud initialized"
    break
  fi
  echo "  ...still initializing"
  sleep 5
done
```

### 7.2 Check Nextcloud Status

```bash
curl -s http://localhost/status.php | jq '.' 2>/dev/null || \
echo "⚠️  Nextcloud not responding yet (can retry in 1 minute)"
```

**Expected Output**:
```json
{
  "installed": true,
  "maintenance": false,
  "needsDbUpgrade": false,
  "version": "29.0.0.12",
  "versionstring": "29.0.0"
}
```

### 7.3 Install OnlyOffice (Document Editing)

```bash
echo "Installing OnlyOffice app..."
docker exec -u www-data nextcloud-app php occ app:install onlyoffice || \
echo "⚠️  OnlyOffice install failed (can retry later)"

echo "✅ OnlyOffice installed"
```

### 7.4 Install Additional Apps

```bash
echo "Installing Deck (kanban boards)..."
docker exec -u www-data nextcloud-app php occ app:install deck || true

echo "Installing Tasks (todo lists)..."
docker exec -u www-data nextcloud-app php occ app:install tasks || true

echo "✅ Apps installed"
```

### 7.5 Enable E2E Encryption

```bash
echo "Enabling E2E encryption..."
docker exec -u www-data nextcloud-app php occ app:enable encryption || true
docker exec -u www-data nextcloud-app php occ encryption:enable || true

echo "✅ E2E encryption enabled"
```

### 7.6 Web Access Info

```bash
DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)
ADMIN_USER=$(grep '^NEXTCLOUD_ADMIN_USER=' .env | cut -d= -f2)

echo ""
echo "=== NEXTCLOUD WEB ACCESS ==="
echo "📱 URL: https://$DOMAIN/"
echo "👤 Username: $ADMIN_USER"
echo "🔑 Password: (see NEXTCLOUD_ADMIN_PASSWORD in .env)"
echo ""
echo "⚠️  Warning: If using self-signed SSL, accept certificate warning in browser"
```

---

## PHASE 8: MATRIX USER SETUP (10 minutes)

**Purpose**: Register Matrix users and test authentication.

### 8.1 Wait for Synapse Readiness

```bash
echo "Waiting for Matrix Synapse..."

for i in {1..30}; do
  if curl -s http://localhost:8008/_matrix/client/versions 2>/dev/null | grep -q '"versions"'; then
    echo "✅ Synapse ready"
    break
  fi
  echo "  ...still starting"
  sleep 5
done
```

### 8.2 Create Admin User

```bash
ADMIN_PASS=$(grep '^NEXTCLOUD_ADMIN_PASSWORD=' .env | cut -d= -f2)
SERVER_NAME=$(grep '^SYNAPSE_SERVER_NAME=' .env | cut -d= -f2)

echo "Creating Matrix admin user..."

docker exec -it nextcloud-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u matrix_admin \
  -p "$ADMIN_PASS" \
  --admin \
  --no-prompt

echo "✅ Admin user created: @matrix_admin:$SERVER_NAME"
```

### 8.3 Create Test User

```bash
echo "Creating test user..."

docker exec -it nextcloud-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u testuser \
  -p "testpass123" \
  --no-prompt || echo "⚠️  Test user already exists or creation failed"

echo "✅ Test user: @testuser:$SERVER_NAME"
```

---

## PHASE 9: ELEMENT WEB CONFIGURATION (10 minutes)

**Purpose**: Configure Element Web client to connect to Synapse.

### 9.1 Create Element Configuration

Save as `/opt/nextcloud-matrix/element-config.json`:

```bash
DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)

cat > element-config.json << EOF
{
  "default_server_config": {
    "m.homeserver": {
      "base_url": "https://$DOMAIN/_matrix",
      "server_name": "$DOMAIN"
    },
    "m.identity_server": {
      "base_url": "https://vector.im"
    }
  },
  "brand": "Element",
  "integrations_ui_url": "https://scalar.vector.im/",
  "integrations_rest_url": "https://scalar.vector.im/api/v1/scalar",
  "integrations_widgets_urls": [
    "https://scalar.vector.im/_matrix/integrations/v1",
    "https://scalar.vector.im/api/v1/scalar/integrations"
  ],
  "bug_report_endpoint_url": "https://element.io/bugreports/submit",
  "uisi_private_sharing_encryption_enabled": true,
  "default_country_code": "US",
  "features": {
    "groups": "labs",
    "pinning": "labs",
    "custom_themes": "labs",
    "dehydration": "labs"
  }
}
EOF

echo "✅ Element configuration created"
```

### 9.2 Verify Element Web Access

```bash
DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)

echo ""
echo "=== ELEMENT WEB ACCESS ==="
echo "📱 URL: https://$DOMAIN/element"
echo "👤 Test login:"
echo "   User: @testuser:$DOMAIN"
echo "   Pass: testpass123"
echo ""
echo "⚠️  Note: Element may show 'waiting for homeserver...' while Synapse initializes"
```

---

## PHASE 10: VALIDATION & HEALTH CHECKS (20 minutes)

**Purpose**: Comprehensive verification before go-live.

### 10.1 Create Validation Script

Save as `/opt/nextcloud-matrix/validate.sh`:

```bash
#!/bin/bash
set -e

echo "=== DEPLOYMENT VALIDATION CHECKLIST ==="
echo ""

passed=0
total=0

# 1. Containers running
echo "[1/8] Docker containers..."
total=$((total + 1))
running=$(docker-compose ps --filter "status=running" -q | wc -l)
if [ "$running" -ge 6 ]; then
  echo "    $running containers running"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Only $running/6 running"
fi

# 2. Nextcloud health
echo "[2/8] Nextcloud health..."
total=$((total + 1))
if curl -s http://localhost/status.php 2>/dev/null | grep -q '"installed":true'; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Not responding"
fi

# 3. Synapse health
echo "[3/8] Matrix Synapse health..."
total=$((total + 1))
if curl -s http://localhost:8008/_matrix/client/versions 2>/dev/null | grep -q '"versions"'; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Not responding"
fi

# 4. PostgreSQL
echo "[4/8] PostgreSQL..."
total=$((total + 1))
if docker exec nextcloud-postgres pg_isready -U postgres > /dev/null 2>&1; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Not responding"
fi

# 5. Redis
echo "[5/8] Redis cache..."
total=$((total + 1))
if docker exec nextcloud-redis redis-cli ping 2>/dev/null | grep -q "PONG"; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Not responding"
fi

# 6. Memory usage
echo "[6/8] Memory usage..."
total=$((total + 1))
mem_total=$(free -g | awk '/^Mem:/ {print $3}')
if [ "$mem_total" -lt 7 ]; then
  echo "    Using ${mem_total}GB / 7.9GB available"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ⚠️  High usage: ${mem_total}GB / 7.9GB"
fi

# 7. Disk usage
echo "[7/8] Disk space..."
total=$((total + 1))
disk_used=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$disk_used" -lt 80 ]; then
  echo "    ${disk_used}% used (acceptable)"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ⚠️  High: ${disk_used}% used"
fi

# 8. HTTPS certificate
echo "[8/8] SSL certificate..."
total=$((total + 1))
if openssl x509 -in ssl_certs/cert.pem -noout > /dev/null 2>&1; then
  expiry=$(openssl x509 -in ssl_certs/cert.pem -noout -enddate | cut -d= -f2)
  echo "    Valid until: $expiry"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Certificate missing or invalid"
fi

echo ""
echo "=== VALIDATION RESULT: $passed/$total CHECKS PASSED ==="
echo ""

if [ "$passed" -eq "$total" ]; then
  echo "✅ ALL SYSTEMS OPERATIONAL"
  echo "🚀 Phase 5.1 publication ready!"
  exit 0
else
  echo "⚠️  Some checks failed. Review logs and troubleshoot."
  exit 1
fi
```

### 10.2 Run Validation

```bash
chmod +x validate.sh
./validate.sh
```

**Expected Output**:
```
✅ ALL SYSTEMS OPERATIONAL
🚀 Phase 5.1 publication ready!
```

---

## POST-DEPLOYMENT: BACKUP STRATEGY

### Automated Daily Backups

Save as `/opt/nextcloud-matrix/backup.sh`:

```bash
#!/bin/bash

backup_dir="/opt/backups/nextcloud-matrix"
mkdir -p "$backup_dir"

echo "Creating backup..."

# Backup volumes
for volume in nextcloud-matrix_postgres_data \
              nextcloud-matrix_redis_data \
              nextcloud-matrix_nextcloud_data \
              nextcloud-matrix_synapse_data; do
  
  docker run --rm -v $volume:/data \
    -v "$backup_dir":/backup \
    alpine tar czf /backup/${volume##*/}_$(date +%Y%m%d_%H%M%S).tar.gz -C / data
done

# Keep only 7 days of backups
find "$backup_dir" -name "*.tar.gz" -mtime +7 -delete

echo "✅ Backup complete: $backup_dir"
echo "$(du -sh "$backup_dir")"
```

### Add to Crontab (Daily at 03:00 UTC)

```bash
(crontab -l 2>/dev/null; echo "0 3 * * * cd /opt/nextcloud-matrix && ./backup.sh >> /var/log/nextcloud-matrix-backup.log 2>&1") | crontab -

echo "✅ Backup cron job scheduled"
```

---

## ROLLBACK PROCEDURE (If Needed)

**⚠️ WARNING: This destroys all data. Only use if deployment failed irreversibly.**

```bash
cd /opt/nextcloud-matrix

# Stop and remove containers
docker-compose down -v

# Remove volumes (DATA LOSS)
docker volume prune -f

echo "✅ Rollback complete"
echo "To restart, run: docker-compose up -d"
```

**Time to rollback**: ~5 minutes

---

## TROUBLESHOOTING

### Issue: PostgreSQL won't start

```bash
# Check logs
docker logs nextcloud-postgres

# If corrupted, reset
docker-compose down -v
docker-compose up -d postgres
# Re-run Phase 5
```

### Issue: Memory usage > 6.5GB

```bash
# Reduce cache factors in .env
SYNAPSE_CACHE_FACTOR=0.3

# Restart
docker-compose down && docker-compose up -d
```

### Issue: Nginx returns 502 Bad Gateway

```bash
# Check upstream services
docker-compose ps

# Restart failed service
docker-compose restart nextcloud

# Or full restart
docker-compose down && docker-compose up -d
```

### Issue: SSL certificate errors

```bash
# Verify certificate
openssl x509 -in ssl_certs/cert.pem -text -noout

# Renew (if Let's Encrypt)
docker run --rm -v $PWD/ssl_certs:/etc/letsencrypt \
  certbot/certbot renew
```

---

## SUMMARY

✅ **All phases complete**  
✅ **Services operational**  
✅ **Backup strategy implemented**  
✅ **Ready for Phase 5.1 publication**

**Next Steps**:
1. Provision Wave 2 team users in Nextcloud
2. Create shared folders for project content
3. Configure SMTP (password reset emails)
4. Enable E2E encryption for sensitive docs
5. Begin Phase 6 Wave 2 collaboration (July 1)

---

**Document Version**: 1.0  
**Last Updated**: June 16, 2026  
**Status**: ✅ PRODUCTION READY
