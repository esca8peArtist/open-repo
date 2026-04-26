# AgentCore Operator Setup Guide

**Audience**: Operators deploying and maintaining the AgentCore stack — not end users.
**Assumption**: Fresh machine. No prior installation required.
**Estimated setup time**: ~45 minutes on first run (plus model download time, which varies by internet speed and model size).

---

## Overview

AgentCore is a self-hosted, offline-capable AI agent platform. It runs as a Docker Compose stack and exposes a chat UI, a REST API, a first-boot configuration wizard, and optional communication channels (Telegram, SMS/WhatsApp via Twilio).

### Services that run

| Service | Image | Default Port | Purpose |
|---|---|---|---|
| `ollama` | `ollama/ollama:latest` | 11434 | Local LLM inference engine |
| `open-webui` | `ghcr.io/open-webui/open-webui:main` | 3000 | Chat UI and admin dashboard |
| `agentcore` | `agentcore:<version>` | 8080 | Orchestration API (FastAPI) |
| `wizard` | `wizard:<version>` | 8888 | First-boot setup wizard (profile: wizard only) |
| `postgres` | `postgres:16-alpine` | 5432 | Conversation history, config, audit log |
| `redis` | `redis:7-alpine` | 6379 | Message queue for multi-agent pipelines |
| `chromadb` | `chromadb/chroma:latest` | 8000 | Vector database for RAG |
| `nginx` | `nginx:1.27-alpine` | 80 | Reverse proxy (routes `/` to WebUI, `/api/` to AgentCore) |

All data is stored in named Docker volumes on the host — nothing is written to the project directory at runtime.

### Hardware requirements

| Tier | RAM | CPU | Storage | GPU | Recommended profiles |
|---|---|---|---|---|---|
| **Tier 1** (Minimum) | 16 GB | 4 cores | 60 GB free | None | Personal Productivity, Customer Support |
| **Tier 2** (Recommended) | 24 GB | 8 cores | 100 GB free | None / integrated | Sales Outreach, Business Intelligence |
| **Tier 3** (Power user) | 32–48 GB | 12+ cores | 150 GB free | Optional (NVIDIA/AMD) | Developer Assistant |
| **Tier 4** (Enterprise) | 64+ GB | 16+ cores | 200+ GB free | Recommended | Enterprise Orchestrator |

> **Storage note**: Docker images alone consume ~10–15 GB. Each LLM model adds 4–70 GB depending on size. A 7B model is ~4–5 GB; a 72B model is ~40–45 GB.

---

## Part 1: Windows Setup

### 1.1 System Requirements Check

Before installing anything, verify your machine meets the minimums.

**Check RAM:**
1. Press `Windows + R`, type `msinfo32`, press Enter.
2. Look for **Installed Physical Memory (RAM)**. You need at least 16 GB.

**Check free disk space:**
1. Open **File Explorer** → **This PC**.
2. Find your C: drive (or whichever drive you will install on). You need at least 60 GB free.

**Check CPU:**
1. In `msinfo32`, look for **Processor**. Count cores in **Task Manager** → **Performance** → **CPU** → look at "Cores" in the lower right.

**Windows version requirement**: Windows 10 version 2004 (Build 19041) or higher, or Windows 11.

Check your build: press `Windows + R`, type `winver`, press Enter. The dialog shows your version.

### 1.2 Install WSL2

WSL2 (Windows Subsystem for Linux) is required for Docker Desktop's backend.

Open **PowerShell as Administrator** (right-click the Start button → "Windows PowerShell (Admin)") and run:

```powershell
wsl --install
```

This installs WSL2 and the default Ubuntu distribution. When it finishes, **reboot your computer**.

After rebooting, a terminal window will open automatically to complete Ubuntu setup. You will be prompted to:

1. Choose a **Unix username** (lowercase, no spaces — e.g. `operator`).
2. Choose a **password** (you will not see characters as you type — this is normal).
3. Confirm the password.

Write these credentials down. You will need them when running commands in WSL2.

**Verify WSL2 installed correctly:**

Open PowerShell and run:

```powershell
wsl --status
```

Expected output includes `Default Version: 2`. If it shows version 1, run:

```powershell
wsl --set-default-version 2
```

### 1.3 Install Docker Desktop for Windows

1. Open a browser and go to: `https://www.docker.com/products/docker-desktop/`
2. Click **Download for Windows**.
3. Run the installer (`Docker Desktop Installer.exe`).
4. During installation, ensure the checkbox **"Use WSL 2 instead of Hyper-V"** is checked. Leave all other options at their defaults.
5. Click **OK** and wait for the installation to complete.
6. Click **Close and restart** when prompted.

After restarting, Docker Desktop launches automatically. Accept the terms of service when prompted.

**Allocate resources to Docker:**

Docker Desktop defaults to using very limited resources. You must increase this before starting the stack.

1. Click the Docker whale icon in the Windows system tray (bottom-right).
2. Click the ⚙ **Settings** gear icon.
3. Go to **Resources** → **Advanced**.
4. Set **Memory** to at least **10 GB** (10240 MB). If your machine has 32+ GB, set it to 16–24 GB.
5. Set **CPUs** to at least **4**. Use half your total cores for best results.
6. Set **Disk image size** to at least **80 GB** if the slider allows it.
7. Click **Apply & Restart**.

**Enable WSL2 integration:**

1. In Docker Desktop Settings, go to **Resources** → **WSL Integration**.
2. Enable **"Enable integration with my default WSL distro"**.
3. Turn on the toggle next to **Ubuntu** (or whatever distro you installed).
4. Click **Apply & Restart**.

**Verify Docker is working:**

Open a PowerShell or Ubuntu terminal and run:

```bash
docker --version
docker compose version
```

Expected output:

```
Docker version 27.x.x, build xxxxxxx
Docker Compose version v2.x.x
```

If either command fails, confirm Docker Desktop is running (look for the whale icon in the system tray).

### 1.4 Get the code

**Option A: Clone with Git (recommended)**

First, install Git for Windows:

1. Go to `https://git-scm.com/download/win`
2. Download and run the installer. Accept all defaults.
3. Open a new **Git Bash** or **PowerShell** window.

Clone the repository:

```bash
git clone https://github.com/your-org/containerized-agents.git
cd containerized-agents
```

Replace `your-org` with the actual GitHub organization or user name where the repository is hosted.

**Option B: Download ZIP (no Git required)**

1. Go to the repository page on GitHub.
2. Click the green **Code** button → **Download ZIP**.
3. Extract the ZIP to a folder such as `C:\AgentCore`.
4. Open **PowerShell** and navigate to the folder:

```powershell
cd C:\AgentCore\containerized-agents
```

---

## Part 2: macOS Setup

### 2.1 System Requirements Check

**Check your chip type:**
Click the Apple menu () → **About This Mac**.

- If it shows **Apple M1**, **M2**, **M3**, or **M4** — you have Apple Silicon.
- If it shows **Intel Core i...** — you have an Intel Mac.

This matters for downloading the correct Docker installer.

**Check RAM:**
In the **About This Mac** window, look for **Memory**. You need at least 16 GB.

**Check free disk space:**
Click the Apple menu → **About This Mac** → **More Info** → **Storage**. You need at least 60 GB free on your main drive.

### 2.2 Install Docker Desktop for Mac

1. Go to `https://www.docker.com/products/docker-desktop/`
2. Click **Download for Mac**.
3. Choose the correct chip:
   - **Apple Silicon**: download `Docker Desktop for Mac with Apple Silicon`.
   - **Intel**: download `Docker Desktop for Mac with Intel Chip`.
4. Open the downloaded `.dmg` file.
5. Drag **Docker** into your **Applications** folder.
6. Open Docker from Applications. macOS will ask for permission to run — click **Open**.
7. Follow the onscreen prompts. Grant the required permissions when asked.

**Allocate resources:**

1. Click the Docker icon in the macOS menu bar (top-right area).
2. Click **Settings** (gear icon).
3. Go to **Resources** → **Advanced**.
4. Set **Memory** to at least **10 GB**.
5. Set **CPUs** to at least **4**.
6. Click **Apply & Restart**.

**Verify Docker is working:**

Open **Terminal** and run:

```bash
docker --version
docker compose version
```

### 2.3 Get the code

**Option A: Install Homebrew and Git, then clone**

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
git clone https://github.com/your-org/containerized-agents.git
cd containerized-agents
```

**Option B: Download ZIP**

1. Go to the repository on GitHub.
2. Click the green **Code** button → **Download ZIP**.
3. Extract the ZIP to your home folder or Documents.
4. Open Terminal and navigate:

```bash
cd ~/Downloads/containerized-agents
```

---

## Part 3: Common Setup (Both Platforms)

The remaining steps are identical on Windows (run commands in Ubuntu/WSL2 or Git Bash) and macOS (run commands in Terminal).

### 3.1 Navigate to the project directory

All commands from this point forward must be run from inside the project directory.

```bash
cd /path/to/containerized-agents
```

Confirm you are in the right place:

```bash
ls
```

You should see `docker-compose.yml`, `Makefile`, `.env.template`, and several directories (`agentcore/`, `wizard/`, `docker/`, etc.).

### 3.2 Generate secrets

You need to generate strong, unique random values for several security secrets. **Never use the placeholder values from `.env.template` in production.**

Run these commands to generate each secret. Copy each output — you will paste them into `.env` in the next step.

```bash
# Secret key for Open WebUI session encryption
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# API key for Open WebUI → AgentCore internal calls
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# AgentCore JWT / session signing secret
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# PostgreSQL database password
python3 -c "import secrets; print(secrets.token_urlsafe(24))"

# Redis password
python3 -c "import secrets; print(secrets.token_urlsafe(24))"
```

Each command produces a different random string. Run each command separately and keep track of which value is which (you can label them in a text file before pasting into `.env`).

### 3.3 Configure the .env file

Copy the template:

```bash
cp .env.template .env
```

Open `.env` in a text editor. On Linux/macOS you can use `nano`:

```bash
nano .env
```

On Windows (WSL2), you can also open it in Notepad:

```powershell
notepad.exe .env
```

Walk through every required field below. Fields marked **REQUIRED** will cause services to refuse to start if left blank.

---

#### Build metadata

```ini
BUNDLE_VERSION=1.0.0
PROFILE=base
```

- `BUNDLE_VERSION`: Must match the version tag on the Docker images you built or received. Leave as `1.0.0` if you are using the default build.
- `PROFILE`: The agent profile to activate. One of: `personal`, `customer-support`, `sales`, `developer`, `bi`, `enterprise`, `base`. You can change this during the wizard, but it affects which image is built. Leave as `base` for now; the wizard will guide profile selection.

---

#### Security secrets — CHANGE ALL OF THESE

```ini
WEBUI_SECRET_KEY=<paste value from step 3.2>
AGENTCORE_API_KEY=<paste value from step 3.2>
AGENTCORE_SECRET=<paste value from step 3.2>
```

- `WEBUI_SECRET_KEY`: Encrypts Open WebUI user sessions. If this changes, all logged-in users are logged out. **REQUIRED.**
- `AGENTCORE_API_KEY`: Internal key that Open WebUI sends with every request to AgentCore's REST API. Both services must have the same value. **REQUIRED.**
- `AGENTCORE_SECRET`: Used by AgentCore to sign JWTs. If this changes, all existing tokens are invalidated. **REQUIRED.**

---

#### PostgreSQL database

```ini
POSTGRES_USER=agentcore
POSTGRES_PASSWORD=<paste DB password from step 3.2>
POSTGRES_DB=agentcore
POSTGRES_URL=postgresql+asyncpg://agentcore:<paste same DB password>@postgres:5432/agentcore
POSTGRES_HOST=127.0.0.1
POSTGRES_EXPOSE_PORT=5432
```

- `POSTGRES_PASSWORD`: The password PostgreSQL will use. **REQUIRED.** Pick a strong value.
- `POSTGRES_URL`: The full connection string AgentCore uses internally. **You must replace `<password>` in this URL with the exact same value as `POSTGRES_PASSWORD`.** The format is `postgresql+asyncpg://agentcore:YOUR_ACTUAL_PASSWORD@postgres:5432/agentcore`.
- `POSTGRES_HOST`: Set to `127.0.0.1` to prevent the database port from being reachable outside the host machine. Only change this if you need remote database access (not recommended).

**Example** (do not copy these exact values — generate your own):
```ini
POSTGRES_PASSWORD=Xk9mR3vQpL2nWjY8aB4cFz
POSTGRES_URL=postgresql+asyncpg://agentcore:Xk9mR3vQpL2nWjY8aB4cFz@postgres:5432/agentcore
```

---

#### Redis message queue

```ini
REDIS_PASSWORD=<paste Redis password from step 3.2>
REDIS_URL=redis://:<paste same Redis password>@redis:6379/0
REDIS_MAXMEMORY=512mb
REDIS_HOST=127.0.0.1
REDIS_EXPOSE_PORT=6379
```

- `REDIS_PASSWORD`: Password for Redis authentication. **REQUIRED.**
- `REDIS_URL`: Full connection string. **Replace `<password>` with the exact same value as `REDIS_PASSWORD`.** Note the format: `redis://:PASSWORD@redis:6379/0` (the colon before the password is required — there is no username for Redis).
- `REDIS_MAXMEMORY`: Cap Redis memory usage. `512mb` is sufficient for most deployments. Increase to `1gb` for heavy multi-agent workloads.

**Example**:
```ini
REDIS_PASSWORD=TpN7wKzLqM4rVhX2gJ6sYe
REDIS_URL=redis://:TpN7wKzLqM4rVhX2gJ6sYe@redis:6379/0
```

---

#### ChromaDB vector database

```ini
CHROMA_TOKEN=
CHROMA_AUTH_HEADER=X-Chroma-Token
CHROMA_AUTH_PROVIDER=
CHROMADB_HOST=127.0.0.1
CHROMADB_EXPOSE_PORT=8000
```

- `CHROMA_TOKEN`: Leave blank for local-only deployments. If ChromaDB will be network-accessible, generate a token with `python3 -c "import secrets; print(secrets.token_urlsafe(32))"` and set it here.
- `CHROMADB_HOST`: Set to `127.0.0.1` to keep the port local-only. **Do not expose ChromaDB to the network without authentication.**

---

#### Ollama inference engine

```ini
OLLAMA_MAX_LOADED_MODELS=2
OLLAMA_NUM_PARALLEL=1
OLLAMA_KEEP_ALIVE=5m
OLLAMA_HOST=127.0.0.1
OLLAMA_PORT=11434
```

- `OLLAMA_MAX_LOADED_MODELS`: How many models to keep loaded in memory simultaneously. `2` is a reasonable default. On Tier 1 hardware (16 GB RAM), reduce this to `1`.
- `OLLAMA_NUM_PARALLEL`: Parallel inference requests per model. `1` is appropriate for most hardware. Increase to `2` or `4` on Tier 3/4 if you have abundant RAM.
- `OLLAMA_KEEP_ALIVE`: How long a loaded model stays in memory after the last request. `5m` is a good balance. Set to `0` to unload immediately, or `-1` to keep loaded indefinitely.
- `OLLAMA_HOST`: Set to `127.0.0.1` so the Ollama API is not externally accessible. Ollama has no authentication.

---

#### Open WebUI

```ini
WEBUI_NAME=AgentCore
WEBUI_URL=http://agent.local
WEBUI_HOST=0.0.0.0
WEBUI_PORT=3000
WEBUI_ENABLE_SIGNUP=false
WEBUI_DEFAULT_ROLE=user
WEBUI_ENABLE_WEB_SEARCH=false
```

- `WEBUI_URL`: The public URL where the WebUI is accessible. Change `agent.local` to your server's IP address or hostname if you are not using mDNS. Example: `http://192.168.1.50`.
- `WEBUI_ENABLE_SIGNUP`: Set to `false` (default). The wizard creates the admin account. Keep signup disabled after setup unless you want users to self-register.
- `WEBUI_ENABLE_WEB_SEARCH`: Set to `true` only if your deployment has internet access and you want the chat UI to perform web searches.

---

#### AgentCore API

```ini
AGENTCORE_HOST=0.0.0.0
AGENTCORE_PORT=8080
AGENTCORE_BASE_URL=http://localhost:8080
ENVIRONMENT=production
```

- `AGENTCORE_BASE_URL`: The URL Telegram and Twilio webhooks use to reach AgentCore. Leave as `http://localhost:8080` for local deployments. For external channel access, this must be a publicly reachable URL.
- `ENVIRONMENT`: Leave as `production`. Set to `development` only for local development work.

---

#### Hardware binding (do not edit manually)

```ini
HARDWARE_FINGERPRINT=
LICENSE_KEY=
```

Leave both blank. The setup wizard populates these automatically during Step 10 (License Binding). Editing them manually will break license validation.

---

#### Communication channels (optional — configure during wizard)

```ini
TELEGRAM_BOT_TOKEN=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
```

These can all be left blank initially. You can configure them during the wizard (Step 4) or add them later and restart AgentCore. See Part 6 for detailed channel setup instructions.

---

#### Optional integrations (leave blank initially)

```ini
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REFRESH_TOKEN=
TAVILY_API_KEY=
GITHUB_TOKEN=
```

- `TAVILY_API_KEY`: Enables high-quality web search. Optional. Get a key at `https://tavily.com/`. Without it, web search falls back to DuckDuckGo (no key required).
- `GITHUB_TOKEN`: Required only if you use the GitHub tools (code search, issue creation, PR listing). Create a personal access token at `https://github.com/settings/tokens` with `repo` scope.

All other optional fields (email, CalDAV, CRM, filesystem paths) can be configured during the wizard or added later. Leave them blank for now.

**Save and close** the `.env` file when you are done. In `nano`, press `Ctrl+X`, then `Y`, then `Enter`.

### 3.4 Start the stack

Before starting, verify your `.env` has the required secrets set:

```bash
grep -E "^(WEBUI_SECRET_KEY|AGENTCORE_API_KEY|AGENTCORE_SECRET|POSTGRES_PASSWORD|REDIS_PASSWORD)=" .env
```

All five lines should show non-empty values (not just `=` with nothing after it).

Start all services in the background:

```bash
docker compose up -d
```

**What "pulling images" means**: On the first run, Docker downloads the container images from the internet before starting them. The external images (Ollama, Open WebUI, PostgreSQL, Redis, ChromaDB, Nginx) are typically 500 MB to 3 GB each. This can take 5–20 minutes on a fast connection. You will see progress output like:

```
[+] Pulling agentcore-ollama 1/6
 ✔ ollama Pulled                                    12.3s
[+] Building agentcore ...
```

The `agentcore` and `wizard` images are built locally from source (this is normal — they are not pre-published to a registry by default). The first build takes 2–5 minutes.

Check that all services started:

```bash
docker compose ps
```

Expected output (all services should show `Up` or `healthy`):

```
NAME                    IMAGE                             COMMAND        STATUS
agentcore-api           agentcore:1.0.0                   ...            Up (healthy)
agentcore-chromadb      chromadb/chroma:latest            ...            Up (healthy)
agentcore-nginx         nginx:1.27-alpine                 ...            Up (healthy)
agentcore-ollama        ollama/ollama:latest               ...            Up (healthy)
agentcore-open-webui    ghcr.io/open-webui/open-webui:main ...           Up (healthy)
agentcore-postgres      postgres:16-alpine                 ...            Up (healthy)
agentcore-redis         redis:7-alpine                     ...            Up (healthy)
```

The wizard container does not appear here because it runs under the `wizard` profile and must be started separately (see next section).

If any container shows `Restarting` or `Exit`, see Part 5: Troubleshooting.

### 3.5 First-boot wizard

The wizard guides you through initial configuration. It runs as a separate container under the `wizard` Docker Compose profile.

Start the wizard:

```bash
docker compose --profile wizard up -d wizard
```

Wait 15–20 seconds for it to start, then open a browser and go to:

```
http://localhost:8888
```

Work through the 12 wizard steps:

---

**Step 1 — Welcome**

- Select your **language** from the dropdown (English, Spanish, French, German, Portuguese, Japanese, Chinese, Arabic).
- Enter a **name for your agent** (e.g. `Aria`, `Assistant`, or your company name). This is the display name shown in the chat UI.
- Click **Next**.

---

**Step 2 — Profile Selection**

Choose the agent profile that best matches your use case:

| Profile | Min RAM | Best for |
|---|---|---|
| Personal Productivity | 8 GB | Calendar management, email drafting, document search, task reminders |
| Customer Support | 8 GB | Ticket handling, FAQ responses, escalation routing |
| Sales Outreach | 16 GB | Lead follow-up, meeting booking, proposal drafting, CRM |
| Developer Assistant | 24 GB | Code review, PR summaries, debugging, documentation |
| Business Intelligence | 16 GB | Data analysis, report generation, KPI monitoring |
| Enterprise Orchestrator | 64 GB | Multi-agent coordination, cross-department workflows |

Select the profile that matches your hardware and use case, then click **Next**.

> **Tip for Tier 1 hardware (16 GB RAM)**: Choose Personal Productivity or Customer Support. The Developer and Enterprise profiles require substantially more RAM than Tier 1 provides.

---

**Step 3 — Multi-Agent Setup**

This step lets you add additional agent profiles to run alongside your primary profile. Each additional profile consumes more RAM and CPU.

- On Tier 1 hardware, skip this step (click **Next** without adding additional profiles).
- On Tier 2–4 hardware, you can add one or two additional profiles and set CPU/RAM allocations for each.

---

**Step 4 — Communication Channels**

Configure the messaging channels your agent will receive messages from.

- **Telegram**: Enable and paste your bot token (format: `123456789:AAFxxxxxx`). The wizard validates the token format immediately. If you do not have a bot yet, leave this disabled and configure it later via Part 6.
- **Twilio (SMS)**: Enable and enter your Twilio Account SID, Auth Token, and phone number. Account SID starts with `AC` and is 34 characters long. The wizard validates credentials before advancing.
- **WhatsApp**: Toggle on if you have a Twilio WhatsApp-enabled number.
- **Voice calls**: Toggle on if you want to receive inbound voice calls via Twilio.

All channels can be skipped and configured later. Click **Next** to continue.

---

**Step 5 — Knowledge Base**

Upload documents or provide URLs to seed the agent's RAG (Retrieval-Augmented Generation) knowledge base.

- **Upload documents**: Drag and drop files. Supported formats: PDF, DOCX, TXT, MD, CSV. Maximum file size is limited by your Docker memory allocation.
- **URLs**: Paste URLs (one per line) that the agent should be able to answer questions about.

This step is optional. Click **Next** to skip.

---

**Step 6 — Integrations**

Configure calendar and email access.

- **CalDAV calendar**: Enter your CalDAV server URL (works with Google Calendar, Nextcloud, Apple Calendar). Example: `https://caldav.example.com/calendar/`. Enter your username and password for that service.
- **Email (SMTP/IMAP)**: Enter your SMTP server hostname, port (default 587), email address, and password. This enables the agent to draft and send emails.

Both are optional. Click **Next** to skip.

---

**Step 7 — Model Download**

This step downloads the LLM models required for your selected profile. The wizard shows real-time download progress.

Model sizes by profile:

| Profile | Models downloaded | Approximate total size |
|---|---|---|
| Personal Productivity | qwen2.5:7b-instruct, phi4-mini, nomic-embed-text | ~8 GB |
| Customer Support | qwen2.5:7b-instruct, nomic-embed-text | ~5 GB |
| Sales Outreach | qwen2.5:14b-instruct, nomic-embed-text | ~10 GB |
| Developer Assistant | qwen3-coder:30b-a3b, nomic-embed-text | ~20 GB |
| Business Intelligence | deepseek-r1:14b, nomic-embed-text | ~10 GB |
| Enterprise Orchestrator | qwen3:72b, nomic-embed-text | ~45 GB |

**Expected time**: 5–30 minutes depending on your internet speed and model size. On a 100 Mbps connection, the Personal Productivity models take approximately 10 minutes. The Enterprise Orchestrator models may take over an hour on slow connections.

Do not close the browser during this step. If the download stalls, see Part 5: Troubleshooting.

---

**Step 8 — Voice Setup**

Configure speech-to-text (Whisper large-v3) and text-to-speech (Kokoro 82M) models.

- Click **Test Microphone** to verify your microphone is accessible.
- Click **Test Speaker** to play a test tone.
- Click **Download Voice Models** to download the STT and TTS models (~3 GB total).

Voice is optional. Click **Skip** if you do not need voice input/output.

---

**Step 9 — Hardware Validation**

The wizard runs an inference benchmark using the smallest available model and measures tokens per second. It also reads your total RAM and maps it to a hardware tier.

- The benchmark takes 30–60 seconds.
- Click **Run Benchmark** and wait for results.
- The wizard will warn if your hardware is below the minimum for your selected profile. You can go back and choose a lighter profile, or continue anyway.

---

**Step 10 — License Binding**

- **Docker Compose SKU**: Paste your license key into the field and click **Bind License**. The license is validated against the AgentCore licensing server and bound to this deployment.
- **OS image SKU**: Click **Bind via TPM** to generate a hardware fingerprint from your system's TPM chip, CPU serial, board UUID, and MAC address. This fingerprint is stored in `.env` as `HARDWARE_FINGERPRINT`.

If you do not have a license key, you can skip this step for evaluation use. Some features may be restricted without a valid license.

---

**Step 11 — Health Check**

The wizard connects to all services and reports their status. Click **Run Health Check** to start the check. Wait for all services to show a green status.

Expected results:

```
✅ ollama       — HTTP 200
✅ open_webui   — HTTP 200
✅ agentcore    — HTTP 200
✅ chromadb     — HTTP 200
✅ postgres     — accepting connections
```

If any service shows ❌, note the error message and refer to Part 5: Troubleshooting before proceeding.

---

**Step 12 — Go Live**

The final step writes the wizard-complete marker file (`/app/agentcore-data/.wizard-complete`) and signals AgentCore that setup is finished.

A QR code is displayed for the agent dashboard URL. Scan it with your phone or click the link to open the dashboard.

The wizard container stops on its own after this step (it has `restart: "no"` in the compose file). You do not need to stop it manually.

### 3.6 Verify everything works

Run through this checklist after the wizard completes. Each item has a specific command or URL to check.

```bash
# Check all containers are running
docker compose ps
```

✅ All containers show `Up` and `(healthy)` in the STATUS column.
❌ Any container shows `Restarting` or `Exit N` — see Part 5.

```bash
# AgentCore health endpoint
curl http://localhost:8080/health
```

✅ Returns `{"status": "ok"}` or similar JSON.
❌ `Connection refused` — AgentCore is not running or still starting up.

```bash
# AgentCore Prometheus metrics
curl http://localhost:8080/metrics
```

✅ Returns a large block of text starting with `# HELP` lines.

```bash
# AgentCore API with authentication
curl -H "Authorization: Bearer YOUR_AGENTCORE_API_KEY" http://localhost:8080/api/agents
```

Replace `YOUR_AGENTCORE_API_KEY` with the value of `AGENTCORE_API_KEY` from your `.env` file.

✅ Returns a JSON array (may be empty `[]` on first run).
❌ Returns 401 — check the API key in your `.env`.

**Open WebUI (Chat interface)**

Open `http://localhost:3000` in a browser.

✅ The Open WebUI login page loads.

Log in with the admin credentials you set during the wizard. Send a test message to the agent. ✅ The agent responds.

**Dashboard**

Open `http://localhost:8080/dashboard` in a browser.

✅ The AgentCore dashboard loads showing agent status, model info, and configuration options.

**Nginx reverse proxy**

Open `http://localhost` (port 80) in a browser.

✅ Redirects to the Open WebUI chat interface at `http://agent.local` or your configured `WEBUI_URL`.

### 3.7 Configure the agent profile

After the wizard, you can further customize agent behavior through the dashboard at `http://localhost:8080/dashboard`.

**Choosing the right profile**

If you chose the wrong profile during the wizard, you can reconfigure it:

1. Open the dashboard.
2. Navigate to **Agent Configuration**.
3. Select the desired profile from the dropdown.
4. Save and restart AgentCore: `docker compose restart agentcore`.

**Profile-specific notes**:

- **Personal Productivity**: Best used with calendar (CalDAV) and email (SMTP/IMAP) integrations enabled.
- **Customer Support**: Pair with Telegram or Twilio SMS for customer-facing channel access. Upload your FAQ documents in the knowledge base.
- **Sales Outreach**: Connect your CRM database via `CRM_DB_PATH` or `DB_SQLITE_PATH` in `.env`.
- **Developer Assistant**: Configure `GITHUB_TOKEN` in `.env` to enable code search and PR tooling.
- **Business Intelligence**: Connect your data source via `DB_POSTGRES_URL` or `DB_MYSQL_URL` in `.env`.
- **Enterprise Orchestrator**: Requires Tier 4 hardware. Enable multi-agent mode during the wizard (Step 3).

**Modifying agent behavior**

1. Open the dashboard → **Agent Configuration** → **System Prompt**.
2. Edit the system prompt to customize the agent's persona, tone, and constraints.
3. Click **Save**. Changes take effect immediately for new conversations.

**Adding tools and MCP integrations**

1. Open the dashboard → **Tools**.
2. Toggle individual tools on or off (e.g., web search, calendar, email, code execution).
3. MCP integrations are configured via environment variables in `.env`. Restart AgentCore after changing tool credentials: `docker compose restart agentcore`.

---

## Part 4: Ongoing Operations

### 4.1 Starting and stopping

```bash
# Start all services (safe to run if already running)
docker compose up -d

# Stop all services (data is preserved in volumes)
docker compose down

# Stop all services AND delete all data volumes (CAUTION: irreversible)
docker compose down -v

# Restart a single service
docker compose restart agentcore

# Restart all services
docker compose restart
```

> **Warning**: `docker compose down -v` permanently deletes all conversation history, configuration, uploaded documents, and downloaded models. Only use this to completely reset the installation.

### 4.2 Viewing logs

```bash
# Follow live logs from AgentCore
docker compose logs -f agentcore

# Follow live logs from Ollama (useful for model loading issues)
docker compose logs -f ollama

# See the last 100 lines from AgentCore
docker compose logs --tail=100 agentcore

# See logs from all services simultaneously
docker compose logs -f

# See logs from Postgres (useful for DB errors)
docker compose logs --tail=50 postgres

# See logs from the wizard (check for setup errors)
docker compose logs wizard
```

Press `Ctrl+C` to stop following logs. The services keep running.

### 4.3 Updating

**Checking for updates via dashboard**: Open `http://localhost:8080/dashboard` → **System** → **Updates**. The dashboard checks the update server at `https://updates.agentcore.io/manifest.json` and shows if a newer version is available.

**Applying updates manually**:

```bash
# Pull the latest versions of all external images
docker compose pull

# Rebuild the local agentcore and wizard images
docker compose build --no-cache

# Restart all services with new images
docker compose up -d
```

> Before updating, ensure you have a backup (see Section 4.4). Some updates may require database migrations that run automatically on first start.

**Updating a single service**:

```bash
# Update only Ollama
docker compose pull ollama && docker compose up -d ollama

# Update only Open WebUI
docker compose pull open-webui && docker compose up -d open-webui
```

### 4.4 Backups

All persistent data lives in Docker named volumes. The volumes are:

| Volume name | Contains |
|---|---|
| `agentcore_ollama_data` | Downloaded LLM models (~4–45 GB per model) |
| `agentcore_open_webui_data` | Open WebUI user accounts and settings |
| `agentcore_agentcore_data` | AgentCore configuration, wizard-complete marker |
| `agentcore_wizard_data` | Wizard session state |
| `agentcore_postgres_data` | All conversation history, agent configs, audit log |
| `agentcore_redis_data` | Redis append-only log (message queue state) |
| `agentcore_chromadb_data` | Vector embeddings for RAG |

**Back up the PostgreSQL database** (most critical — contains all conversations and config):

```bash
# Dump database to a SQL file on your host
docker compose exec postgres pg_dump -U agentcore agentcore > backup_$(date +%Y%m%d_%H%M%S).sql
```

**Back up all named volumes** (full backup):

```bash
# Back up postgres data volume to a tar file
docker run --rm \
  -v agentcore_postgres_data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/postgres-backup-$(date +%Y%m%d).tar.gz /data

# Back up chromadb data volume
docker run --rm \
  -v agentcore_chromadb_data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/chromadb-backup-$(date +%Y%m%d).tar.gz /data
```

Model downloads do not need backing up — they can be re-downloaded. Configuration in `.env` should be kept in a secure password manager or secrets vault.

**Restore from a SQL backup**:

```bash
# Stop agentcore first to prevent writes during restore
docker compose stop agentcore open-webui

# Restore
cat backup_20240101_120000.sql | docker compose exec -T postgres psql -U agentcore agentcore

# Restart
docker compose start agentcore open-webui
```

---

## Part 5: Troubleshooting

### "Cannot connect to the Docker daemon"

**Full error**: `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`

**Cause**: Docker Desktop is not running.

**Fix**:
- **Windows**: Look for the Docker whale icon in the system tray (bottom-right). If it is not there, open Docker Desktop from the Start menu and wait for it to show "Docker Desktop is running".
- **macOS**: Look for the Docker icon in the menu bar (top-right). Click it to see status. If absent, open Docker Desktop from Applications.

After Docker Desktop is running, retry your command.

---

### "Port is already allocated" or "address already in use"

**Full error**: `Error response from daemon: driver failed programming external connectivity on endpoint agentcore-postgres ... Bind for 0.0.0.0:5432 failed: port is already allocated`

**Cause**: Another process on your host is already using that port.

**Find what is using the port** (replace 5432 with the conflicting port):

```bash
# On Linux/macOS
sudo lsof -i :5432

# On Windows (PowerShell)
netstat -ano | findstr :5432
```

**Fix options**:

1. Stop the conflicting process (e.g., a local PostgreSQL installation: `sudo systemctl stop postgresql`).
2. Or change the exposed port in `.env`. For example, to expose Postgres on port 5433 instead:
   ```ini
   POSTGRES_EXPOSE_PORT=5433
   ```
   Then restart: `docker compose up -d`.

---

### "Out of memory" — containers crashing with exit code 137

**Cause**: Docker does not have enough memory allocated.

**Check memory allocation**:

```bash
docker system info | grep -i memory
```

**Fix**:
- **Windows/macOS**: Increase memory in Docker Desktop → Settings → Resources → Advanced. Set Memory to at least 10 GB, ideally 16 GB. Click "Apply & Restart".
- **Linux native Docker**: No memory limit by default. Check available system RAM: `free -h`. If RAM is genuinely insufficient, see the hardware tier table in the Overview section.

After increasing memory, restart the stack: `docker compose up -d`.

---

### "Model download stuck" — wizard shows no progress on Step 7

**Cause**: Ollama is downloading a large model, Docker networking is slow, or the model pull stalled.

**Check Ollama logs for progress**:

```bash
docker compose logs -f ollama
```

You should see download progress lines. If the log is silent for more than 5 minutes:

1. Check available disk space: `df -h` (Linux/macOS) or File Explorer → This PC (Windows). You need free space equal to the model size.
2. Restart Ollama and retry: `docker compose restart ollama`. Then go back to Step 7 in the wizard and click the download button again.
3. If a specific model keeps failing, try pulling it manually:
   ```bash
   docker compose exec ollama ollama pull qwen2.5:7b-instruct
   ```

---

### "Permission denied" (WSL2 / Linux)

**Full error**: `permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock`

**Cause**: Your user is not in the `docker` group.

**Fix**:

```bash
sudo usermod -aG docker $USER
```

Then **log out and log back in** (closing and reopening the terminal is not sufficient — you must fully log out of WSL2). Verify with:

```bash
groups
```

`docker` should appear in the list.

---

### Wizard won't load or returns 502

**Cause**: The wizard container failed to start, or AgentCore/Ollama/Postgres are not healthy yet (the wizard depends on them).

**Check wizard status**:

```bash
docker compose --profile wizard ps wizard
docker compose logs wizard
```

**Check dependencies**:

```bash
docker compose ps
```

All of `ollama`, `postgres`, and the other services must be `healthy` before the wizard starts. The wizard's `depends_on` conditions enforce this. If Postgres is still starting, wait 30–60 seconds and refresh the wizard URL.

If the wizard container exited, look at the last few log lines:

```bash
docker compose logs --tail=50 wizard
```

Common errors in wizard logs and their fixes:

- `Could not reach Ollama` → Ollama not yet healthy. Wait and retry.
- `address already in use` on port 8888 → Another service is using 8888. Change `WIZARD_PORT` in `.env`.

---

### Containers keep restarting

**Identify which container and why**:

```bash
docker compose ps
docker compose logs --tail=30 <service-name>
```

Replace `<service-name>` with the name of the restarting container (e.g., `agentcore`, `postgres`).

**Common causes and fixes**:

| Log message | Cause | Fix |
|---|---|---|
| `AGENTCORE_SECRET must be set` | Missing required secret | Set `AGENTCORE_SECRET` in `.env`, run `docker compose up -d` |
| `POSTGRES_PASSWORD must be set` | Missing DB password | Set `POSTGRES_PASSWORD` in `.env`, run `docker compose up -d` |
| `WEBUI_SECRET_KEY must be set` | Missing WebUI secret | Set `WEBUI_SECRET_KEY` in `.env`, run `docker compose up -d` |
| `could not connect to server: Connection refused` | Postgres not yet ready | Wait for postgres to be healthy; check `docker compose ps` |
| `OOMKilled` | Out of memory | Increase Docker memory allocation |

After fixing any `.env` issues, always run:

```bash
docker compose up -d
```

Docker will re-read the `.env` file and recreate any containers that have changed configuration.

---

## Part 6: Channel Setup (Optional)

### Telegram

Telegram is free to use and does not require a paid account or public URL during operation (the bot polls Telegram's servers).

**Step 1: Create a bot**

1. Open Telegram and search for `@BotFather`.
2. Start a conversation and send `/newbot`.
3. Follow the prompts:
   - Give your bot a name (e.g., `Aria Assistant`).
   - Give your bot a username (must end in `bot`, e.g., `aria_mycompany_bot`).
4. BotFather responds with your bot token in the format: `7123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

**Step 2: Add the token to .env**

```bash
nano .env
```

Find the line:
```ini
TELEGRAM_BOT_TOKEN=
```

And set it:
```ini
TELEGRAM_BOT_TOKEN=7123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Step 3: Restart AgentCore**

```bash
docker compose restart agentcore
```

**Step 4: Test**

1. Open Telegram and search for your bot by its username (e.g., `@aria_mycompany_bot`).
2. Send `/start` or any message.
3. The agent should respond within a few seconds.

If the bot does not respond:
```bash
docker compose logs -f agentcore | grep -i telegram
```

---

### Twilio SMS / WhatsApp

Twilio requires a paid Twilio account and a public-facing webhook URL. For production, this means your server must be reachable from the internet. For local testing, use `ngrok` to create a temporary public URL.

**Prerequisites**:
- A Twilio account at `https://www.twilio.com/`
- A Twilio phone number with SMS capability (purchased in the Twilio console)
- For WhatsApp: WhatsApp Business approval from Twilio (additional setup required in the Twilio console)

**Step 1: Get your Twilio credentials**

1. Log in to the [Twilio Console](https://console.twilio.com/).
2. From the dashboard, copy:
   - **Account SID** (starts with `AC`, 34 characters)
   - **Auth Token** (click the eye icon to reveal)
3. Go to **Phone Numbers** → **Manage** → **Active Numbers** and copy your Twilio phone number in E.164 format (e.g., `+14155552671`).

**Step 2: Set up a public webhook URL**

AgentCore must be reachable from Twilio's servers to receive inbound messages.

For production deployments, ensure your server has a public IP or domain and that port 8080 is open.

For local testing with ngrok:

```bash
# Install ngrok from https://ngrok.com/download
ngrok http 8080
```

Copy the HTTPS URL it provides (e.g., `https://abc123.ngrok-free.app`).

**Step 3: Configure the Twilio webhook**

1. In the Twilio Console, go to **Phone Numbers** → **Manage** → **Active Numbers**.
2. Click your phone number.
3. Under **Messaging** → **A Message Comes In**, set the webhook URL to:
   ```
   https://your-public-url/api/channels/twilio/sms
   ```
4. Set the HTTP method to **POST**.
5. Click **Save**.

**Step 4: Add credentials to .env**

```ini
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+14155552671
```

**Step 5: Restart AgentCore**

```bash
docker compose restart agentcore
```

**Step 6: Test**

Send an SMS to your Twilio phone number from any phone. The agent should reply within a few seconds.

---

## Appendix

### Docker Compose command reference

| Command | Description |
|---|---|
| `docker compose up -d` | Start all services in the background |
| `docker compose down` | Stop all services, preserve volumes |
| `docker compose down -v` | Stop all services and delete all data (irreversible) |
| `docker compose restart` | Restart all services |
| `docker compose restart agentcore` | Restart a single service |
| `docker compose ps` | Show service status |
| `docker compose logs -f` | Follow logs from all services |
| `docker compose logs -f agentcore` | Follow logs from a single service |
| `docker compose logs --tail=100 agentcore` | Show last 100 lines from a service |
| `docker compose pull` | Pull latest versions of external images |
| `docker compose build --no-cache` | Rebuild local images from scratch |
| `docker compose exec agentcore bash` | Open a shell inside a running container |
| `docker compose --profile wizard up -d wizard` | Start the wizard container |
| `docker system prune -f` | Remove stopped containers and dangling images (frees disk) |
| `docker system df` | Show disk usage by Docker |

### Service ports reference

| Port | Service | Container name | Accessible from host | Notes |
|---|---|---|---|---|
| 80 | Nginx reverse proxy | `agentcore-nginx` | Yes (all interfaces) | Routes `/` to WebUI, `/api/` to AgentCore |
| 3000 | Open WebUI | `agentcore-open-webui` | Yes (all interfaces) | Chat UI and admin dashboard |
| 8080 | AgentCore API | `agentcore-api` | Yes (all interfaces) | REST API, metrics, dashboard |
| 8888 | Setup Wizard | `agentcore-wizard` | Yes (all interfaces) | Only active when wizard profile is running |
| 11434 | Ollama | `agentcore-ollama` | Localhost only | LLM inference API |
| 5432 | PostgreSQL | `agentcore-postgres` | Localhost only | Database — do not expose externally |
| 6379 | Redis | `agentcore-redis` | Localhost only | Message queue — do not expose externally |
| 8000 | ChromaDB | `agentcore-chromadb` | Localhost only | Vector database — do not expose externally |

Ports marked "Localhost only" are bound to `127.0.0.1` by default in `.env`. To expose them on all interfaces (required for network access), change the corresponding `*_HOST` variable in `.env` to `0.0.0.0`. Only do this if you understand the security implications.

### Environment variable reference

| Variable | Required | Default | Description |
|---|---|---|---|
| `BUNDLE_VERSION` | Yes | `1.0.0` | Semver version tag matching built images |
| `PROFILE` | Yes | `base` | Agent profile: personal, customer-support, sales, developer, bi, enterprise, base |
| `WEBUI_SECRET_KEY` | Yes | _(blank)_ | Open WebUI session encryption key |
| `AGENTCORE_API_KEY` | Yes | _(blank)_ | Internal API key for WebUI → AgentCore |
| `AGENTCORE_SECRET` | Yes | _(blank)_ | AgentCore JWT signing secret |
| `POSTGRES_PASSWORD` | Yes | _(blank)_ | PostgreSQL password |
| `POSTGRES_URL` | Yes | _(placeholder)_ | Full asyncpg DSN including password |
| `POSTGRES_USER` | No | `agentcore` | PostgreSQL username |
| `POSTGRES_DB` | No | `agentcore` | PostgreSQL database name |
| `REDIS_PASSWORD` | Yes | _(blank)_ | Redis authentication password |
| `REDIS_URL` | Yes | _(placeholder)_ | Full Redis DSN including password |
| `REDIS_MAXMEMORY` | No | `512mb` | Redis memory cap |
| `OLLAMA_MAX_LOADED_MODELS` | No | `2` | Max models loaded in memory |
| `OLLAMA_NUM_PARALLEL` | No | `1` | Parallel inference requests per model |
| `OLLAMA_KEEP_ALIVE` | No | `5m` | Time to keep model in memory after last use |
| `WEBUI_NAME` | No | `AgentCore` | Display name in Open WebUI |
| `WEBUI_URL` | No | `http://agent.local` | Public URL for links and QR codes |
| `WEBUI_ENABLE_SIGNUP` | No | `false` | Allow self-registration |
| `WEBUI_ENABLE_WEB_SEARCH` | No | `false` | Enable web search in chat UI |
| `ENVIRONMENT` | No | `production` | `production` or `development` |
| `HARDWARE_FINGERPRINT` | No | _(blank)_ | Set automatically by wizard — do not edit |
| `LICENSE_KEY` | No | _(blank)_ | Set automatically by wizard — do not edit |
| `TELEGRAM_BOT_TOKEN` | No | _(blank)_ | Telegram bot token from @BotFather |
| `TWILIO_ACCOUNT_SID` | No | _(blank)_ | Twilio Account SID (starts with AC) |
| `TWILIO_AUTH_TOKEN` | No | _(blank)_ | Twilio Auth Token |
| `TWILIO_PHONE_NUMBER` | No | _(blank)_ | Twilio phone number in E.164 format |
| `TAVILY_API_KEY` | No | _(blank)_ | Tavily web search API key |
| `GITHUB_TOKEN` | No | _(blank)_ | GitHub personal access token |
| `CHROMA_TOKEN` | No | _(blank)_ | ChromaDB auth token (leave blank for local) |
| `UPDATE_SERVER_URL` | No | `https://updates.agentcore.io/manifest.json` | Update manifest URL |
| `UPDATE_PUBLIC_KEY_HEX` | No | _(blank)_ | Ed25519 public key for update verification |
