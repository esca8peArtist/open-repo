---
title: "systemd/venv Deployment Runbook for Open-Repo Backend"
subtitle: "raspby1 (Raspberry Pi 5) — Native Linux systemd Path"
project: open-repo
phase: 6 (infrastructure deployment)
document_type: deployment-procedures
status: READY FOR EXECUTION
created: 2026-06-23
estimated_duration: 35 minutes
target_deployment_date: 2026-06-24 (upon user platform decision)
---

# systemd/venv Deployment Runbook

## Deployment Summary

- **Target Host**: raspby1 (Raspberry Pi 5, 100.70.184.84)
- **Deployment Method**: Python venv + systemd service + native postgres/meilisearch daemons
- **Estimated Deployment Time**: 35 minutes
- **Prerequisites**: SSH access to raspby1, Python 3.10+, sudo privileges for system service setup
- **Success Criteria**: systemd service running, health endpoint returns 200 OK, API responds to requests

---

## Phase 0: Pre-Flight Validation (5 minutes)

**Objective**: Confirm environment is ready for systemd/venv deployment.

### Step 0.1: Verify SSH Access and Sudo Privileges

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo -v"
```

**Expected Output**: No prompt, or "sudo: 1 incorrect password attempt allowed" message. Indicates sudo access works.

**If fails with "not in sudoers file"**:
```bash
# Execute on raspby1 as root or sudo user:
sudo usermod -aG sudo pi
# Log out and log back in
```

---

### Step 0.2: Verify Python 3.10+ Available

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "python3 --version"
```

**Expected Output**:
```
Python 3.10.X or higher
```

**If Python 3.9 or older** (not acceptable):
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo apt-get update && sudo apt-get install -y python3.10 python3.10-venv python3.10-dev
EOF
```

Then use `python3.10` instead of `python3` in subsequent commands.

---

### Step 0.3: Verify PostgreSQL and Meilisearch Installed

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo systemctl is-enabled postgresql || echo "PostgreSQL not installed"
sudo systemctl is-enabled meilisearch || echo "Meilisearch not installed"
EOF
```

**Expected Output**: If either not installed, this section will error.

**If PostgreSQL not installed**:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo apt-get update && sudo apt-get install -y postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql
EOF
```

**If Meilisearch not installed**:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
# Download Meilisearch binary for ARM64
cd /tmp
wget https://github.com/meilisearch/meilisearch/releases/download/v1.X.X/meilisearch-linux-arm64
sudo mv meilisearch-linux-arm64 /usr/local/bin/meilisearch
sudo chmod +x /usr/local/bin/meilisearch
# Verify installation
meilisearch --version
EOF
```

---

### Step 0.4: Verify Disk Space

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "df -h / | tail -1"
```

**Expected Output**:
```
/dev/root  XXG  XXG  5.0G  XX%  /
```

**Acceptance Criteria**: At least 5GB free. If less:
```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo apt-get autoremove && sudo apt-get clean
df -h /
EOF
```

---

## Phase 1: Create Deployment Directory and User (3 minutes)

**Objective**: Set up directory structure and service account.

### Step 1.1: Create Deployment Directory

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo mkdir -p /opt/open-repo
sudo mkdir -p /opt/open-repo/backups
sudo mkdir -p /opt/open-repo/logs
sudo chown -R pi:pi /opt/open-repo
chmod 755 /opt/open-repo
ls -la /opt/open-repo
EOF
```

**Expected Output**: Directories created with pi as owner.

---

### Step 1.2: Create systemd Service Account (Optional, Recommended)

For better security, create a dedicated service user:

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
# Create 'open-repo' service user (non-login)
sudo useradd -r -s /bin/false -m -d /opt/open-repo open-repo 2>/dev/null || true
# Verify user created
id open-repo
EOF
```

**Expected Output**: User created with UID and system groups.

---

## Phase 2: Set Up Python Virtual Environment (8 minutes)

**Objective**: Create isolated Python environment with dependencies.

### Step 2.1: Copy Application Code to raspby1

```bash
# From your local machine
rsync -avz --exclude '.git' --exclude '__pycache__' \
  /home/awank/dev/SuperClaude_Framework/projects/open-repo/backend/ \
  pi@100.70.184.84:/opt/open-repo/
```

**Expected Output**: Transfers ~50MB of code, ~30 seconds.

---

### Step 2.2: Create Virtual Environment

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
python3 -m venv venv
source venv/bin/activate
python --version
EOF
```

**Expected Output**:
```
Python 3.10.X (or higher)
```

---

### Step 2.3: Install Python Dependencies

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -e .
EOF
```

**Expected Output**: Installs FastAPI, uvicorn, SQLAlchemy, asyncpg, meilisearch, and all dependencies. Takes 3-5 minutes on Pi5 (slower than x86 due to ARM compilation).

**If pip install fails with "No such file or directory"**:
- Verify `pyproject.toml` exists: `ls -la /opt/open-repo/pyproject.toml`
- If missing, check Step 2.1 (code copy)

---

### Step 2.4: Verify Installation

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
source venv/bin/activate
python -c "import fastapi; import sqlalchemy; import asyncpg; import meilisearch; print('All imports successful')"
EOF
```

**Expected Output**:
```
All imports successful
```

---

## Phase 3: Configure PostgreSQL Database (5 minutes)

**Objective**: Create database and run migrations.

### Step 3.1: Ensure PostgreSQL is Running

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo systemctl start postgresql && sudo systemctl status postgresql"
```

**Expected Output**:
```
● postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (...)
   Active: active (running) since ...
```

---

### Step 3.2: Create Database and User

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo -u postgres psql << SQL
CREATE DATABASE open_repo;
CREATE USER open_repo WITH PASSWORD 'open_repo_password';
ALTER ROLE open_repo SET client_encoding TO 'utf8';
ALTER ROLE open_repo SET default_transaction_isolation TO 'read committed';
ALTER ROLE open_repo SET default_transaction_deferrable TO on;
ALTER ROLE open_repo SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE open_repo TO open_repo;
SQL
EOF
```

**Expected Output**: No errors. Database and user created.

---

### Step 3.3: Run Database Migrations

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
source venv/bin/activate
export DATABASE_URL="postgresql+asyncpg://open_repo:open_repo_password@localhost/open_repo"
alembic upgrade head
EOF
```

**Expected Output**:
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade -> [revision], add initial tables
[migration summary]
```

---

## Phase 4: Configure Meilisearch Service (3 minutes)

**Objective**: Set up Meilisearch daemon and systemd unit.

### Step 4.1: Create Meilisearch Directory and systemd Unit

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo mkdir -p /var/lib/meilisearch
sudo chown meilisearch:meilisearch /var/lib/meilisearch 2>/dev/null || true

sudo tee /etc/systemd/system/meilisearch.service > /dev/null << 'UNIT'
[Unit]
Description=Meilisearch Search Engine
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/meilisearch --db-path /var/lib/meilisearch --listen 127.0.0.1:7700
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
UNIT

sudo systemctl daemon-reload
sudo systemctl enable meilisearch
sudo systemctl start meilisearch
EOF
```

**Expected Output**: Service created and started.

---

### Step 4.2: Verify Meilisearch Running

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
curl -s http://localhost:7700/health | jq .
EOF
```

**Expected Output**:
```json
{
  "status": "available"
}
```

---

## Phase 5: Create systemd Service for Open-Repo (5 minutes)

**Objective**: Create and enable systemd unit for FastAPI application.

### Step 5.1: Create systemd Unit File

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo tee /etc/systemd/system/open-repo.service" << 'EOF'
[Unit]
Description=Open-Repo Backend API
After=network.target postgresql.service meilisearch.service
Wants=postgresql.service meilisearch.service

[Service]
Type=notify
User=open-repo
WorkingDirectory=/opt/open-repo
Environment="PATH=/opt/open-repo/venv/bin"
Environment="DATABASE_URL=postgresql+asyncpg://open_repo:open_repo_password@localhost/open_repo"
Environment="MEILISEARCH_URL=http://localhost:7700"
Environment="MEILISEARCH_KEY=super_secret_key_change_in_production"
Environment="LOG_LEVEL=info"
ExecStart=/opt/open-repo/venv/bin/uvicorn app.main:create_app --host 127.0.0.1 --port 8000
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=open-repo

[Install]
WantedBy=multi-user.target
EOF
```

**Expected Output**: Unit file created at `/etc/systemd/system/open-repo.service`.

---

### Step 5.2: Reload systemd and Enable Service

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo systemctl daemon-reload
sudo systemctl enable open-repo.service
sudo systemctl start open-repo.service
sudo systemctl status open-repo.service
EOF
```

**Expected Output**:
```
● open-repo.service - Open-Repo Backend API
   Loaded: loaded (/etc/systemd/system/open-repo.service; enabled)
   Active: active (running) since ... 
   Main PID: XXXX (uvicorn)
```

---

### Step 5.3: Verify Service Logs

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo journalctl -u open-repo -n 20 --no-pager"
```

**Expected Output**:
```
Jun 24 12:00:01 raspby1 open-repo[XXXX]: INFO:     Started server process [12]
Jun 24 12:00:01 raspby1 open-repo[XXXX]: INFO:     Waiting for application startup
Jun 24 12:00:02 raspby1 open-repo[XXXX]: INFO:     Application startup complete
Jun 24 12:00:02 raspby1 open-repo[XXXX]: INFO:     Uvicorn running on http://127.0.0.1:8000
```

**If errors present**: Check environment variables and database connectivity in logs.

---

## Phase 6: Health Checks and Validation (3 minutes)

**Objective**: Confirm service is responding correctly.

### Step 6.1: Test Health Endpoint

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
- Wait 10 seconds (service may still be starting)
- Check: `systemctl status open-repo` (should show "active (running)")
- If not running: `sudo systemctl start open-repo`
- Check logs: `sudo journalctl -u open-repo -n 50`

---

### Step 6.2: Verify Service Status

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
systemctl status open-repo.service
systemctl status postgresql.service
systemctl status meilisearch.service
EOF
```

**Expected Output**: All three services showing "active (running)".

---

### Step 6.3: Check Memory Usage

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "free -h && ps aux | grep -E 'python|postgres|meilisearch' | grep -v grep"
```

**Expected Output**:
```
               total        used        free
Mem:           7.8G        1.2G        6.6G

open-repo    XXXX  0.8%  250M  1234 ?  S  12:00  0:05 /opt/open-repo/venv/bin/python
postgres     XXXX  1.2%  95M   5678 ?  S  12:00  0:10 /usr/lib/postgresql/XX/bin/postgres
meilisearch  XXXX  0.6%  85M   9012 ?  S  12:00  0:02 /usr/local/bin/meilisearch
```

**Acceptance Criteria**: Total memory <1GB, individual processes under 500MB each.

---

## Phase 7: Configure Log Rotation (3 minutes)

**Objective**: Set up automatic log cleanup via logrotate.

### Step 7.1: Create Logrotate Configuration

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo tee /etc/logrotate.d/open-repo" << 'EOF'
/var/log/open-repo/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 open-repo open-repo
    sharedscripts
    postrotate
        systemctl reload open-repo > /dev/null 2>&1 || true
    endscript
}
EOF
```

**Expected Output**: Logrotate configuration created. Logs rotate daily, keep 7 days.

---

### Step 7.2: Test Logrotate Configuration

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo logrotate -d /etc/logrotate.d/open-repo"
```

**Expected Output**: Debug output showing configuration is valid (no errors).

---

## Phase 8: Configure Backup Script (3 minutes)

**Objective**: Set up automated daily database backups.

### Step 8.1: Create Backup Script

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "cat > /opt/open-repo/backup.sh" << 'EOF'
#!/bin/bash
# Daily backup script for open-repo PostgreSQL database

BACKUP_DIR=/opt/open-repo/backups
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE=$BACKUP_DIR/open-repo_${TIMESTAMP}.sql

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Dump database
pg_dump -U open_repo -d open_repo > $BACKUP_FILE

# Compress
gzip $BACKUP_FILE

# Keep only last 7 days
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

echo "Backup completed: $BACKUP_FILE.gz"
EOF

chmod +x /opt/open-repo/backup.sh
```

---

### Step 8.2: Schedule Daily Backup via Cron

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
# Add to crontab
echo "0 2 * * * /opt/open-repo/backup.sh >> /opt/open-repo/backups/backup.log 2>&1" | crontab -
crontab -l  # Verify entry
EOF
```

**Expected Output**: Crontab entry shows `0 2 * * * /opt/open-repo/backup.sh...` (backup runs daily at 02:00 UTC).

---

## Phase 9: Configure Reverse Proxy (Nginx + TLS) (5 minutes)

**Objective**: Expose API securely on port 443 (optional but recommended for production).

### Step 9.1: Install Nginx

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo apt-get update && sudo apt-get install -y nginx certbot python3-certbot-nginx
sudo systemctl enable nginx
sudo systemctl start nginx
EOF
```

---

### Step 9.2: Create Nginx Reverse Proxy Configuration

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
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
EOF
```

---

### Step 9.3: Enable Nginx Site and Reload

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo ln -sf /etc/nginx/sites-available/open-repo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
EOF
```

**Expected Output**: `nginx: configuration is ok`.

---

## Phase 10: Rollback Procedure (If Deployment Fails)

**Objective**: Recover from deployment failure mid-way.

### Step 10.1: Stop Services

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo systemctl stop open-repo.service
sudo systemctl stop meilisearch.service
# PostgreSQL typically left running (drop database if needed)
EOF
```

---

### Step 10.2: Remove systemd Unit

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo rm /etc/systemd/system/open-repo.service
sudo systemctl daemon-reload
EOF
```

---

### Step 10.3: Restore Database (If Corrupted)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sudo -u postgres dropdb open_repo  # Drop corrupted database
# Then re-run Phase 3 (database creation and migrations)
EOF
```

---

### Step 10.4: Remove venv (Complete Reset)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
rm -rf /opt/open-repo/venv
# Then re-run Phase 2 (venv creation)
EOF
```

---

## Phase 11: Update Procedure (Rolling Updates)

**Objective**: Safely deploy new application versions.

### Step 11.1: Pull New Code

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
sudo -u open-repo git pull origin main  # If using git
# OR manually copy new code via rsync
EOF
```

---

### Step 11.2: Upgrade Dependencies (If Changed)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
source /opt/open-repo/venv/bin/activate
pip install -U -e .
EOF
```

---

### Step 11.3: Run Migrations (If Database Schema Changed)

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
cd /opt/open-repo
source venv/bin/activate
export DATABASE_URL="postgresql+asyncpg://open_repo:open_repo_password@localhost/open_repo"
alembic upgrade head
EOF
```

---

### Step 11.4: Restart Service

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 "sudo systemctl restart open-repo.service"
```

---

### Step 11.5: Verify Health

```bash
ssh -i ~/.ssh/raspby1_key pi@100.70.184.84 << 'EOF'
sleep 5  # Wait for service to start
curl -s http://localhost:8000/api/health | jq .
EOF
```

**Expected Output**: 200 OK with version number indicating new version deployed.

---

## Summary

**Deployment Completed**:
- ✅ Python venv with all dependencies installed
- ✅ PostgreSQL database created with migrations
- ✅ Meilisearch search service running
- ✅ systemd service configured and enabled
- ✅ Health endpoint responding (200 OK)
- ✅ Daily backup cron scheduled
- ✅ Nginx reverse proxy configured (optional)

**Estimated Total Time**: 35 minutes
- Phase 0 (pre-flight): 5 min
- Phase 1 (directories): 3 min
- Phase 2 (venv + deps): 8 min
- Phase 3 (database): 5 min
- Phase 4 (meilisearch): 3 min
- Phase 5 (systemd): 5 min
- Phase 6 (health checks): 3 min
- Phase 7-11 (optional): 15 min

**Next Steps**: Proceed to `DEPLOYMENT_SUCCESS_CRITERIA_AND_VALIDATION.md` for post-deployment validation and SLA definition.

**Emergency Contacts**: If deployment fails:
1. Check service logs: `sudo journalctl -u open-repo -n 50`
2. Verify database: `sudo -u postgres psql -l`
3. Check ports in use: `sudo lsof -i -P -n | grep LISTEN`
4. Restart services: `sudo systemctl restart open-repo.service`

**Rollback Window**: If deployment fails at any phase <10 minutes, execute Phase 10 rollback (5 minutes) to return to clean state.
