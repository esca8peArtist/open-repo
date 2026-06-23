---
title: "Docker Deployment Runbook for Open-Repo Backend"
subtitle: "raspby1 (Raspberry Pi 5) — Docker Compose Path"
project: open-repo
phase: 6 (infrastructure deployment)
document_type: deployment-procedures
status: READY FOR EXECUTION
created: 2026-06-23
estimated_duration: 25 minutes
target_deployment_date: 2026-06-24 (upon user platform decision)
---

# Docker Deployment Runbook

## Deployment Summary

- **Target Host**: raspby1 (Raspberry Pi 5, 100.70.184.84)
- **Deployment Method**: docker-compose with three containers (app, postgres, meilisearch)
- **Estimated Deployment Time**: 25 minutes
- **Prerequisites**: SSH access to raspby1, Docker installed (20.10+), git access to application code
- **Success Criteria**: All three containers running, health endpoint returns 200 OK, API responds to requests

---

## Phase 0: Pre-Flight Validation (5 minutes)

**Objective**: Confirm environment is ready for Docker deployment.

### Step 0.1: Verify SSH Access to raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "uname -a"
```

**Expected Output**:
```
Linux raspby1 6.6.X+rpt-rpi-2712 #1 SMP Debian 6.6.X-rpi-2 (2026-XX-XX) aarch64 GNU/Linux
```

**If fails**: Check SSH key permissions (`chmod 600 ~/.ssh/raspby1_key`) or confirm IP/DNS resolution.

---

### Step 0.2: Verify Docker Installation on raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker --version && docker-compose --version"
```

**Expected Output**:
```
Docker version 20.10.X, build XXXXXX
Docker Compose version 2.X.X, build XXXXXX
```

**If Docker not installed** (error: "command not found"):
```bash
# Execute on raspby1 (or via ssh):
sudo apt-get update && sudo apt-get install -y docker.io docker-compose
sudo usermod -aG docker pi
# Log out and log back in to apply group membership
```

**If Docker Compose v1 (old)** (output shows "version 1.X"):
```bash
# Upgrade to v2:
sudo apt-get install docker-compose-plugin
```

---

### Step 0.3: Verify Disk Space on raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "df -h /"
```

**Expected Output** (available space):
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       XXG   XXG  5.0G  XX% /
```

**Acceptance Criteria**: At least 5GB free. If less than 5GB:
```bash
# Clean up on raspby1:
docker system prune -a --volumes  # Remove old images/volumes
sudo apt-get autoremove && sudo apt-get clean
df -h /  # Verify space freed
```

---

### Step 0.4: Verify Network Connectivity from raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "ping -c 3 8.8.8.8"
```

**Expected Output**: 3 packets sent/received, 0% loss. Network is ready.

**If fails**: Check raspby1 network configuration (beyond scope of this runbook; escalate to user).

---

## Phase 1: Prepare Deployment Directory (5 minutes)

**Objective**: Create deployment structure and retrieve application code.

### Step 1.1: Create Deployment Directories on raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
mkdir -p /opt/open-repo/{backend,backups,config}
mkdir -p /opt/open-repo/postgres_data
mkdir -p /opt/open-repo/meilisearch_data
ls -la /opt/open-repo/
EOF
```

**Expected Output**: Directories created.

---

### Step 1.2: Copy Application Code to raspby1

**Option A: If code is in local git repo** (recommended):

```bash
# From your local machine
rsync -avz --exclude '.git' --exclude '__pycache__' \
  /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/ \
  pi@100.70.184.84:/opt/open-repo/backend/
```

**Expected Output**: Transfers ~50MB of code, ~30 seconds.

**Option B: If code is in GitHub repo**:

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo/backend
git clone https://github.com/YOUR_ORG/open-repo.git .
# (assumes your repo has the backend code)
EOF
```

**Expected Output**: Repository cloned, ~2 min.

---

### Step 1.3: Verify Application Code Transferred

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "ls -la /opt/open-repo/backend/app/"
```

**Expected Output**:
```
-rw-r--r--  1 pi pi  XXXX  Jun 23 12:00 __init__.py
-rw-r--r--  1 pi pi  XXXX  Jun 23 12:00 main.py
-rw-r--r--  1 pi pi  XXXX  Jun 23 12:00 database.py
-rw-r--r--  1 pi pi  XXXX  Jun 23 12:00 models.py
-rw-r--r--  1 pi pi  XXXX  Jun 23 12:00 routes.py
drwxr-xr-x  X pi pi  XXXX  Jun 23 12:00 api/
```

**If missing**: Re-run Step 1.2 (rsync or git clone).

---

## Phase 2: Create Docker Compose Configuration (5 minutes)

**Objective**: Configure docker-compose.yml for three-container stack.

### Step 2.1: Create docker-compose.yml on raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "cat > /opt/open-repo/docker-compose.yml" << 'EOF'
version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    container_name: open-repo-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: open_repo
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "127.0.0.1:5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always
    networks:
      - open-repo-net

  meilisearch:
    image: getmeili/meilisearch:latest
    container_name: open-repo-meilisearch
    environment:
      MEILI_ENV: production
      MEILI_MASTER_KEY: super_secret_key_change_in_production
    volumes:
      - meilisearch_data:/data.ms
    ports:
      - "127.0.0.1:7700:7700"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7700/health"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always
    networks:
      - open-repo-net

  app:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: open-repo-api
    depends_on:
      postgres:
        condition: service_healthy
      meilisearch:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql+asyncpg://postgres:postgres@postgres:5432/open_repo
      MEILISEARCH_URL: http://meilisearch:7700
      MEILISEARCH_KEY: super_secret_key_change_in_production
      LOG_LEVEL: info
    ports:
      - "127.0.0.1:8000:8000"
    volumes:
      - ./backend:/app
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/health"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always
    networks:
      - open-repo-net

volumes:
  postgres_data:
    driver: local
  meilisearch_data:
    driver: local

networks:
  open-repo-net:
    driver: bridge
EOF
```

**Expected Output**: docker-compose.yml created successfully.

---

### Step 2.2: Create Dockerfile for Application

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "cat > /opt/open-repo/backend/Dockerfile" << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY pyproject.toml /app/
RUN pip install --no-cache-dir -e .

# Copy application code
COPY . /app/

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
EOF
```

**Expected Output**: Dockerfile created successfully.

**Security Note**: Application will bind to `0.0.0.0:8000` inside the container (isolated network namespace). Docker compose maps this to `127.0.0.1:8000` on host (no exposure to external network). Compliant with security rules.

---

## Phase 3: Build and Start Containers (10 minutes)

**Objective**: Pull images, build app, and start all three containers.

### Step 3.1: Pull Base Images and Build Application Container

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
docker-compose build
EOF
```

**Expected Output**:
```
Building app
[+] Building 45.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => [stage-0 1/7] FROM python:3.11-slim
 ...
 => => naming to open-repo-api:latest
```

**Time**: 3-5 minutes (first build pulls base images; subsequent builds faster). Pi5 ARM compilation may take longer than x86.

**If build fails with "No space left"**:
- Run `docker system prune -a --volumes` on raspby1 to free space
- Re-run build

---

### Step 3.2: Start All Three Containers

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
docker-compose up -d
EOF
```

**Expected Output**:
```
[+] Running 3/3
 ✔ Container open-repo-postgres    Started                             1.2s
 ✔ Container open-repo-meilisearch Started                             1.3s
 ✔ Container open-repo-api         Started                             2.1s
```

**Time**: 3-5 seconds to start containers. PostgreSQL and Meilisearch will initialize in background.

---

### Step 3.3: Monitor Container Startup (3 minutes)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker-compose ps"
```

**Expected Output** (watch this until all show "healthy"):
```
NAME                     COMMAND                  SERVICE      STATUS
open-repo-postgres       "postgres"               postgres     Up 15s (health: starting)
open-repo-meilisearch    "meilisearch"            meilisearch  Up 14s (health: starting)
open-repo-api            "uvicorn app.main:c..."  app          Up 13s (health: starting)
```

**Success criteria**: Wait until STATUS shows `healthy` for all three. Typically 1-2 minutes. If stuck at "starting" after 5 minutes, check logs:

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker-compose logs app"
```

**Common errors and fixes**:
- **"Connection refused to postgres"**: PostgreSQL still initializing. Wait 30 more seconds.
- **"Meilisearch failed to start"**: Disk space issue. Run `docker system prune`.
- **"Port 5432 already in use"**: Kill conflicting process: `sudo lsof -i :5432` and `kill -9 <PID>`

---

### Step 3.4: Verify Logs Show Clean Startup

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker-compose logs --tail=50 app"
```

**Expected Output**:
```
app  | INFO:     Started server process [12]
app  | INFO:     Waiting for application startup.
app  | INFO:     Application startup complete
app  | INFO:     Uvicorn running on http://0.0.0.0:8000
```

**If errors present**: Check database initialization logs:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker-compose logs postgres"
```

---

## Phase 4: Health Checks and Validation (3 minutes)

**Objective**: Confirm all three containers responding correctly.

### Step 4.1: Check API Health Endpoint

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "curl -s http://localhost:8000/api/health | jq ."
```

**Expected Output**:
```json
{
  "status": "ok",
  "version": "0.2.0"
}
```

**If fails with "connection refused"**:
- Wait 30 more seconds (startup may still in progress)
- Check: `docker-compose logs app` (should show "Application startup complete")
- If app container is not running: `docker-compose up -d app` to restart

---

### Step 4.2: Check PostgreSQL Connection from App

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
docker-compose exec app curl -s http://localhost:8000/api/health
EOF
```

**Expected Output**: Same 200 OK response as 4.1.

---

### Step 4.3: List Running Containers

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker ps"
```

**Expected Output** (3 containers running):
```
CONTAINER ID   IMAGE                        COMMAND                  CREATED        STATUS              PORTS
xxxxxxxxxx     open-repo-api:latest         "uvicorn app.main:c..."  1 min ago      Up 1 min (healthy)  127.0.0.1:8000->8000/tcp
xxxxxxxxxx     getmeili/meilisearch:latest  "meilisearch"            1 min ago      Up 1 min (healthy)  127.0.0.1:7700->7700/tcp
xxxxxxxxxx     postgres:16-alpine           "postgres"               1 min ago      Up 1 min (healthy)  127.0.0.1:5432->5432/tcp
```

**If container missing or unhealthy**:
- Check logs: `docker-compose logs <service>`
- Restart: `docker-compose restart <service>`
- Full restart: `docker-compose down && docker-compose up -d`

---

### Step 4.4: Check Container Resource Usage

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "docker stats --no-stream"
```

**Expected Output**:
```
CONTAINER ID   NAME                  CPU %   MEM USAGE / LIMIT     MEM %
xxxxxxxxxx     open-repo-api         5.2%    280MiB / 7.8GiB       3.6%
xxxxxxxxxx     open-repo-meilisearch 0.8%    85MiB / 7.8GiB        1.1%
xxxxxxxxxx     open-repo-postgres    1.2%    95MiB / 7.8GiB        1.2%
```

**Acceptance Criteria**: 
- Total memory <1GB (idle) ✅
- No container over 2GB (even under load)
- CPU not consistently >50% (should be low at idle)

---

## Phase 5: Rollback Procedure (If Deployment Fails)

**Objective**: Recover from deployment failure mid-way.

### Step 5.1: Stop All Containers

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
docker-compose down
EOF
```

**Expected Output**:
```
[+] Stopping 3/3
 ✔ Container open-repo-api         Stopped
 ✔ Container open-repo-meilisearch Stopped
 ✔ Container open-repo-postgres    Stopped
[+] Removing 3/3
 ✔ Container open-repo-api         Removed
 ✔ Container open-repo-meilisearch Removed
 ✔ Container open-repo-postgres    Removed
```

---

### Step 5.2: Clean Up Volumes (If Corrupted)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
docker-compose down -v  # Remove volumes
docker system prune -a  # Clean up images
EOF
```

**Expected Output**: Containers, volumes, and dangling images removed.

---

### Step 5.3: Restore from Backup (If Database Corrupted)

**Option A: If daily backup exists**:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
# Restore database from backup
docker-compose up -d postgres  # Start postgres only
sleep 30  # Wait for postgres to initialize
docker-compose exec -T postgres psql -U postgres -d open_repo < /opt/open-repo/backups/open-repo-$(date +%Y%m%d).sql
docker-compose up -d  # Start all containers
EOF
```

**Option B: If no backup, start fresh**:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
docker-compose up -d  # Containers start with fresh DB
EOF
```

---

## Phase 6: Post-Deployment Monitoring Setup (Optional)

**Objective**: Configure automated health checks and log rotation.

### Step 6.1: Create Backup Script

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "cat > /opt/open-repo/backup.sh" << 'EOF'
#!/bin/bash
# Daily backup script for open-repo database

BACKUP_DIR=/opt/open-repo/backups
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE=$BACKUP_DIR/open-repo_${TIMESTAMP}.sql

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Dump database
docker-compose -f /opt/open-repo/docker-compose.yml exec -T postgres pg_dump -U postgres open_repo > $BACKUP_FILE

# Compress
gzip $BACKUP_FILE

# Keep only last 7 days
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

echo "Backup completed: $BACKUP_FILE.gz"
EOF

chmod +x /opt/open-repo/backup.sh
```

---

### Step 6.2: Schedule Daily Backup via Cron

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
# Add to crontab
echo "0 2 * * * /opt/open-repo/backup.sh >> /opt/open-repo/backups/backup.log 2>&1" | crontab -
crontab -l  # Verify entry
EOF
```

**Expected Output**: Crontab entry shows `0 2 * * * /opt/open-repo/backup.sh...` (backup runs daily at 02:00 UTC).

---

## Phase 7: Configure Reverse Proxy (TLS Setup)

**Objective**: Expose API securely on port 443 (optional but recommended for production).

### Step 7.1: Install Nginx on raspby1

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo apt-get update && sudo apt-get install -y nginx certbot python3-certbot-nginx
sudo systemctl enable nginx
sudo systemctl start nginx
EOF
```

---

### Step 7.2: Create Nginx Reverse Proxy Configuration

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo tee /etc/nginx/sites-available/open-repo" << 'EOF'
server {
    listen 80;
    server_name open-repo.local;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF
```

---

### Step 7.3: Enable Site and Test

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo ln -sf /etc/nginx/sites-available/open-repo /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl reload nginx
EOF
```

**Expected Output**: `nginx: configuration is ok`.

---

## Summary

**Deployment Completed**:
- ✅ 3 containers running (app, postgres, meilisearch)
- ✅ Health endpoint responding (200 OK)
- ✅ Database initialized
- ✅ Search service ready
- ✅ Daily backup cron scheduled
- ✅ Nginx reverse proxy configured (optional)

**Estimated Total Time**: 25 minutes
- Phase 0 (pre-flight): 5 min
- Phase 1 (directories): 5 min
- Phase 2 (docker-compose): 5 min
- Phase 3 (build & start): 10 min
- Phase 4 (health checks): 3 min

**Next Steps**: Proceed to `DEPLOYMENT_SUCCESS_CRITERIA_AND_VALIDATION.md` for post-deployment validation and SLA definition.

**Emergency Contacts**: If deployment fails:
1. Check logs: `docker-compose logs app`
2. Restart containers: `docker-compose down && docker-compose up -d`
3. Verify disk space: `df -h /`
4. Check Docker daemon: `docker ps` (should list 3 containers)

**Rollback Window**: If deployment fails at any phase <10 minutes, execute Phase 5 rollback (5 minutes) to return to clean state.
