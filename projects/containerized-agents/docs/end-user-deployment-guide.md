# AgentCore — End-User Deployment Guide

Welcome! This guide will walk you through setting up your personal or business AI agent from start to finish. No technical background is required — just follow the numbered steps, and you will have a fully working AI agent running on your computer.

**Estimated time:** 30–60 minutes (most of that is waiting for downloads)

---

## Table of Contents

1. [Welcome — What Are You Setting Up?](#1-welcome--what-are-you-setting-up)
2. [Before You Start](#2-before-you-start)
3. [Install Docker (One-Time Setup)](#3-install-docker-one-time-setup)
4. [Set Up Your Agent](#4-set-up-your-agent)
5. [First-Time Configuration Wizard](#5-first-time-configuration-wizard)
6. [Using Your Agent](#6-using-your-agent)
7. [Adding Documents and Knowledge](#7-adding-documents-and-knowledge)
8. [Managing Your Agent](#8-managing-your-agent)
9. [Getting Updates](#9-getting-updates)
10. [Troubleshooting](#10-troubleshooting)
11. [Privacy and Security](#11-privacy-and-security)
12. [Quick Reference Card](#12-quick-reference-card)

---

## 1. Welcome — What Are You Setting Up?

You are setting up **AgentCore** — an AI agent that runs entirely on your own computer. It is like having a smart personal assistant that can:

- **Chat with you** in a web browser, just like chatting with a person
- **Manage your calendar** — check upcoming events, create new ones
- **Read and send email** — draft and fetch messages from your inbox
- **Search the web** for up-to-date information (when your internet is on)
- **Answer questions about your documents** — upload PDFs, Word files, or text files and ask questions about them
- **Set reminders and schedule tasks** for you
- **Respond on Telegram, SMS, or WhatsApp** (optional — requires extra setup)
- **Speak and listen** (optional voice mode — requires a microphone and speaker)

Depending on the "profile" your operator chose for you, it may also:

- **Handle customer support** questions by reading your company's knowledge base
- **Assist with sales outreach** by tracking leads and drafting follow-ups
- **Help developers** browse code, search GitHub, and run code snippets
- **Analyze business data** and generate PDF reports from your databases
- **Coordinate a team of specialized agents** (Enterprise mode)

### A Note on Privacy

All AI processing happens on your computer. Your conversations, documents, and data are stored locally — nothing is sent to an external AI company's servers unless you specifically add an API key for a cloud service. Once the AI models are downloaded during setup, the core system works completely offline.

---

## 2. Before You Start

### What You Will Need

- **A computer** running:
  - Windows 10 or Windows 11, or
  - macOS 12 (Monterey) or later
- **At least 16 GB of RAM** (memory). Less than 16 GB will work for basic use but may be slow.
  - To check on **Windows**: Click the Start menu, type "System Information," and open it. Look for "Installed Physical Memory (RAM)."
  - To check on **Mac**: Click the Apple logo in the top-left corner of your screen, then click "About This Mac." The amount of memory is listed on that screen.
- **At least 60 GB of free disk space.** AI models are large files.
  - To check on **Windows**: Open File Explorer, right-click on "This PC," and choose "Properties." Your free space is shown next to your main drive (usually C:).
  - To check on **Mac**: Click the Apple logo, then "About This Mac," then the "Storage" tab. Your available space is shown in the bar at the top.
- **A stable internet connection** for the initial setup. After setup, the agent works offline. (Some optional features like Telegram and web search need internet whenever you use them.)
- **Your license key and any API keys** that your operator provided. Keep these handy — the wizard will ask for them.

### Gather These Before Starting

Your operator should have given you:

| Item | Where it comes from | Notes |
|------|---------------------|-------|
| License key | Your operator | Looks like: `AGNT-XXXX-XXXX-XXXX` |
| WEBUI_SECRET_KEY | Your operator or you generate it | A long random string |
| AGENTCORE_API_KEY | Your operator or you generate it | A long random string |
| AGENTCORE_SECRET | Your operator or you generate it | A long random string |
| POSTGRES_PASSWORD | Your operator or you generate it | A password for the internal database |
| REDIS_PASSWORD | Your operator or you generate it | A password for the internal message queue |
| Telegram bot token | Optional — from Telegram's @BotFather | Only if you want Telegram |
| Twilio credentials | Optional — from twilio.com | Only if you want SMS or WhatsApp |

If you need to generate passwords/keys yourself, the section [3.3 Configure Your Settings](#33-configure-your-settings) explains how to do this safely.

---

## 3. Install Docker (One-Time Setup)

### What Is Docker?

Docker is free software that runs your AI agent in a self-contained "box" on your computer. Think of it like a very tidy kitchen that has every ingredient and appliance your agent needs, all kept separate from the rest of your computer. Once Docker is installed, you will not need to touch it again — it just quietly runs in the background.

You only need to do this once. If you already have Docker installed, skip to [Part 4](#4-set-up-your-agent).

---

### Installing Docker on Windows

1. Open your web browser and go to: **https://docs.docker.com/desktop/install/windows-install/**

2. Click the large blue **"Download Docker Desktop for Windows"** button.

3. Once the file finishes downloading (it is about 500 MB), double-click it to start the installer. It will be named something like `Docker Desktop Installer.exe`.

4. A security prompt may appear asking "Do you want to allow this app to make changes to your device?" Click **Yes**.

5. The installer will show a checkbox that says "Use WSL 2 instead of Hyper-V." Leave it checked (this is the recommended option). Click **OK**.

6. Wait for the installation to finish. It may take a few minutes.

7. When it completes, click **Close and restart** (or just **Close** if it does not ask you to restart). If it asks you to restart your computer, go ahead and do so.

8. After restarting, Docker Desktop will launch automatically. You will see the Docker whale icon appear in your system tray (the row of small icons near the clock in the bottom-right corner of your screen).

9. The first time Docker starts, it may ask you to accept a license agreement. Click **Accept**.

10. **Verify Docker is working:** Click the Start menu and type "Command Prompt," then press Enter. In the black window that opens, type the following and press Enter:
    ```
    docker --version
    ```
    You should see something like: `Docker version 27.x.x` — any version number means it worked.

---

### Installing Docker on macOS

**First, determine which kind of Mac you have:**

- If your Mac was made **after November 2020**, it likely has an **Apple Silicon** chip (M1, M2, M3, or M4). You can check by clicking the Apple logo → "About This Mac" — it will say "Apple M1" (or M2/M3/M4) under "Chip."
- If it says "Intel" under "Processor," you have an **Intel Mac**.

1. Open your web browser and go to: **https://docs.docker.com/desktop/install/mac-install/**

2. Click the download button that matches your chip:
   - **Apple Silicon**: "Docker Desktop for Mac with Apple Silicon"
   - **Intel**: "Docker Desktop for Mac with Intel chip"

3. Once the `.dmg` file downloads (it is in your Downloads folder), double-click it.

4. A window will open showing the Docker icon and an Applications folder. **Drag the Docker icon into the Applications folder.**

5. Open your Applications folder (click Finder, then "Applications" in the left sidebar), and double-click **Docker**.

6. macOS may ask "Are you sure you want to open this?" Click **Open**.

7. Docker will ask for your Mac's password to complete the setup. Enter it and click **OK**.

8. Docker Desktop will open. The first time, it may ask you to accept a license. Click **Accept**.

9. You will see the Docker whale icon appear in your Mac's menu bar at the top of the screen.

10. **Verify Docker is working:** Open Terminal (press Command + Space, type "Terminal," press Enter). In the window that opens, type:
    ```bash
    docker --version
    ```
    You should see something like: `Docker version 27.x.x`

---

## 4. Set Up Your Agent

### 4.1 Extract the Bundle

Your operator sent you a ZIP file or folder containing at minimum these files:
- `docker-compose.yml` — the recipe for all the agent's components
- `.env.template` — a template for your settings
- `setup.sh` — a helper script that does the first-run preparation
- (Optional) an `images/` folder with pre-downloaded software packages for offline installation

**Where to put it:**

- **Windows**: Create a folder at `C:\AgentCore` and extract (unzip) everything there. Your folder should look like: `C:\AgentCore\docker-compose.yml`, `C:\AgentCore\setup.sh`, etc.
- **Mac**: Create a folder at `/Users/YourName/Documents/AgentCore` and extract everything there.

To extract a ZIP file:
- **Windows**: Right-click the ZIP file → "Extract All…" → browse to `C:\AgentCore` → click "Extract."
- **Mac**: Double-click the ZIP file. It will extract next to itself. Then move the resulting folder to Documents/AgentCore.

---

### 4.2 Run the Setup Script

The setup script does two things: it creates your settings file from the template, and it loads any offline images (if your bundle included them).

**On Windows:**

1. Open File Explorer and navigate to `C:\AgentCore`.
2. If you have **Git for Windows** installed: right-click an empty area of the folder and choose "Git Bash Here." In the Git Bash window that opens, type:
   ```bash
   bash setup.sh
   ```
   and press Enter.

   If you do **not** have Git for Windows: open the Start menu, search for "Windows Subsystem for Linux" or "Ubuntu" (if you have it), or use Command Prompt and run:
   ```
   docker run --rm -v C:\AgentCore:/work -w /work bash bash setup.sh
   ```

**On Mac:**

1. Open Terminal (Command + Space, type "Terminal," press Enter).
2. Type the following, replacing `YourName` with your actual Mac username:
   ```bash
   cd ~/Documents/AgentCore
   bash setup.sh
   ```
   Press Enter after each line.

**What you will see:**

The script will print lines starting with `[OK]` or `[INFO]`. At the end, it will say something like:

```
  AgentCore — First-Run Setup

  [INFO] Creating .env from template...
  [OK]   .env created — edit it to set your credentials before proceeding.

  Next steps:
  1. Edit .env to set required variables
  2. Run: docker compose up -d
  3. Open: http://localhost:8888  (setup wizard)
```

This is the expected output. Now proceed to the next step.

---

### 4.3 Configure Your Settings

The script created a file called `.env` in your AgentCore folder. This file holds all your private settings. You need to open it and fill in a few required values.

> **Note:** `.env` files start with a dot, which means they are "hidden" files on Mac. If you cannot see the `.env` file in Finder, press **Command + Shift + .** (that is Command, Shift, and the period key together) to show hidden files.

**Open the `.env` file:**
- **Windows**: Right-click the `.env` file → "Open with" → choose Notepad. (If you do not see `.env`, make sure "Show hidden files" is enabled in File Explorer: click View → Show → Hidden items.)
- **Mac**: Right-click the `.env` file → "Open With" → TextEdit.

**Fields you must set before starting:**

You will see many lines in this file. Most have sensible defaults. **Only change the ones listed below for now.** Lines that start with `#` are comments (explanations) and are ignored — do not worry about them.

Look for these lines and fill them in:

---

**WEBUI_SECRET_KEY** — Used to protect your login sessions. Must be a long, random string.

```
WEBUI_SECRET_KEY=
```

Change it to something like (do not use this exact value — generate your own):
```
WEBUI_SECRET_KEY=kQ3mW9xLpN7vR2cT8jA5uB1eF6gH4iM0
```

To generate a proper random value, open a Terminal or Command Prompt and run:
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```
Paste whatever it prints in place of the empty value.

---

**AGENTCORE_API_KEY** — An internal key used between components. Generate one the same way as above.

```
AGENTCORE_API_KEY=your-generated-key-here
```

---

**AGENTCORE_SECRET** — Another internal secret for security. Generate one the same way.

```
AGENTCORE_SECRET=your-generated-secret-here
```

---

**POSTGRES_PASSWORD** — The password for the internal database. Generate one the same way.

```
POSTGRES_PASSWORD=your-database-password-here
```

After setting `POSTGRES_PASSWORD`, you must also update `POSTGRES_URL` on the line below it. Find this line:
```
POSTGRES_URL=postgresql+asyncpg://agentcore:<password>@postgres:5432/agentcore
```
Replace `<password>` with whatever you set for `POSTGRES_PASSWORD`. For example:
```
POSTGRES_URL=postgresql+asyncpg://agentcore:your-database-password-here@postgres:5432/agentcore
```

---

**REDIS_PASSWORD** — Password for the internal message queue. Generate one the same way.

```
REDIS_PASSWORD=your-redis-password-here
```

After setting `REDIS_PASSWORD`, also update `REDIS_URL`:
```
REDIS_URL=redis://:your-redis-password-here@redis:6379/0
```

---

**LICENSE_KEY** — Enter the license key your operator gave you.

```
LICENSE_KEY=AGNT-XXXX-XXXX-XXXX
```

---

That is it for now. Save the file (Ctrl+S on Windows, Command+S on Mac) and close it.

> **Optional features** like Telegram, email, and web search can be configured either here in the `.env` file or later through the setup wizard. The wizard is easier, so leave those blank for now.

---

### 4.4 Start the Agent

Now you are ready to start everything up. Go back to your Terminal or Command Prompt in the AgentCore folder and run:

```bash
docker compose up -d
```

The `-d` means "detached" — it runs in the background so your terminal window stays usable.

**The first time you run this**, Docker needs to download several software packages (the chat interface, the database, etc.). This takes **5 to 15 minutes** depending on your internet speed. You will see lines like:

```
Pulling ollama ...
Pulling open-webui ...
Pulling postgres ...
...
```

When it is done, you will see something like:

```
Container agentcore-postgres      Started
Container agentcore-redis         Started
Container agentcore-chromadb      Started
Container agentcore-ollama        Started
Container agentcore-open-webui    Started
Container agentcore-api           Started
Container agentcore-nginx         Started
```

And your command prompt will return. No red error text means everything is running.

> **Tip:** If you see a red error saying a port is already in use (e.g., "port 3000 is already allocated"), another program on your computer is using that port. Contact your operator for help adjusting the port settings.

---

## 5. First-Time Configuration Wizard

Once the agent is running, you need to complete the setup wizard. This is a simple web-based form that guides you through personalizing your agent.

**Open your web browser** (Chrome, Firefox, Edge, or Safari) and go to:

```
http://localhost:8888
```

You should see the AgentCore setup wizard. If you see a blank page or an error, wait 30 more seconds and try refreshing.

The wizard has 12 steps. Here is what each one does:

---

### Step 1: Welcome

This step has two fields:

- **Display language**: Choose the language you want the wizard to display in.
- **Agent name**: Give your agent a name. This is the name it will use when talking to you. You can choose anything — "Aria," "Max," "Alex," or even your company's name.

Click **Continue** when done.

---

### Step 2: Profile Selection

This is the most important choice. A "profile" is a preset that configures what your agent is good at and what tools it has access to. Choose the one that best matches your intended use:

| Profile | Best for | Minimum RAM | Key capabilities |
|---------|----------|-------------|-----------------|
| **Personal Assistant** | Individuals who want help with daily tasks | 8 GB | Calendar, email, web search, reminders, personal documents |
| **Customer Support** | Businesses answering customer questions | 8 GB | Company knowledge base, ticket tracking, email alerts |
| **Sales Outreach** | Sales teams managing leads | 16 GB | CRM contacts, SMS/WhatsApp outreach, meeting booking |
| **Developer Assistant** | Software developers | 24 GB | Code reading, GitHub search, Python execution, documentation Q&A |
| **Business Intelligence** | Managers and analysts | 64 GB | Database queries, data analysis, chart generation, PDF reports |
| **Enterprise Orchestrator** | Large organizations with multiple needs | 64 GB+ | Coordinates all of the above simultaneously, role-based access |

Each profile card in the wizard shows a RAM recommendation. If your computer has less RAM than recommended, choose a simpler profile. Click on a card to select it, then click **Continue**.

---

### Step 3: Multi-Agent Setup (Optional)

This step lets you add additional profiles running alongside your primary one. For most users, this is not needed — click **Continue** to skip it.

If you have a powerful computer (64 GB of RAM or more) and want multiple specialized agents running at once (for example, a Customer Support agent and a Sales agent working together), you can enable them here by checking the boxes next to them.

---

### Step 4: Communication Channels (Optional)

This step connects your agent to messaging apps so you can reach it from your phone or other devices. **If you just want to chat in the browser, click Continue to skip this step entirely.**

**Telegram** (free, requires internet when sending messages):

Telegram is a free messaging app. If you want to send messages to your agent from your phone via Telegram:

1. Open Telegram on your phone and search for **@BotFather** (the official Telegram bot creation tool, with a blue checkmark).
2. Send BotFather the message `/newbot`.
3. Follow its instructions: give your bot a name and a username.
4. BotFather will give you a **token** — a long string of numbers and letters separated by a colon (like `123456789:ABCdefGHIjklMNOpqrstu`). Copy this.
5. Paste that token into the "Telegram Bot Token" field in the wizard.
6. Check the "Enable Telegram" box.

**Twilio — SMS and WhatsApp** (requires a paid Twilio account and internet):

Twilio is a paid service that lets your agent send and receive text messages and WhatsApp messages. If you have a Twilio account:

1. Log into twilio.com and find your Account SID and Auth Token on the dashboard.
2. Find the Twilio phone number you want to use.
3. Enter all three values in the wizard fields.
4. Check "Enable SMS" and/or "Enable WhatsApp" as needed.

The wizard validates your credentials automatically when you type them in — a green checkmark means they are correct.

Click **Continue** when done (or skip if not using these).

---

### Step 5: Knowledge Base (Optional)

This step lets you give your agent documents to learn from — your company's FAQ, product manuals, employee handbook, or personal notes.

**To upload documents:**

1. Click the **"Choose files"** button (or drag and drop files onto the upload area).
2. Supported file types: PDF, Word documents (.docx), plain text (.txt), Markdown (.md), and CSV spreadsheets.
3. Upload as many as you like. The agent will be able to answer questions about them.

**To add websites:**

You can also paste web addresses (URLs) into the text box, one per line. The agent will download and index those pages. This is useful for public documentation sites or your company's website.

Click **Continue** when done (or skip if you have no documents yet — you can always add them later).

---

### Step 6: Integrations (Optional)

This step connects your agent to your email and calendar. **Skip this step if you do not need email or calendar features.**

**Calendar (CalDAV):**

CalDAV is the standard protocol used by Google Calendar, Apple Calendar, Nextcloud, and many others. To connect your calendar:

- **Google Calendar**: Enter `https://apidata.googleusercontent.com/caldav/v2/` as the URL, your Google email as username, and an "App Password" (not your regular Google password — generate one at myaccount.google.com → Security → App Passwords).
- **Apple Calendar (iCloud)**: Enter `https://caldav.icloud.com` as the URL and your Apple ID email and password (or an app-specific password).
- **Nextcloud**: Enter your Nextcloud URL followed by `/remote.php/dav`, then your Nextcloud username and password.

**Email (SMTP/IMAP):**

- **SMTP host**: Your email provider's outgoing mail server (e.g., `smtp.gmail.com` for Gmail, `smtp.office365.com` for Outlook).
- **SMTP port**: Usually 587 (leave this as-is unless your provider says otherwise).
- **Email address and password**: Your email login. For Gmail, use an App Password (same as above).

Click **Continue** when done (or skip).

---

### Step 7: Download AI Models

This is where the agent downloads its "brain" — the AI models that power its intelligence. Models are large files (2–15 GB each depending on your profile) and are downloaded once, then stored on your computer and used offline from then on.

You will see a table listing the models needed for your chosen profile. Click **Start Download** and wait. A progress log will appear showing download status.

**What to expect:**

- A typical download takes **10–30 minutes** on a fast home internet connection.
- The progress log will show lines like `Pulling model...` followed by data transfer numbers.
- When a model finishes, it shows a green "Downloaded" badge.
- When all models are done, you will see "All models downloaded successfully."

**Do not close the browser tab** while downloading. If the download gets interrupted, click the button again — it will resume where it left off.

Click **Continue** when all models show "Downloaded."

---

### Step 8: Voice Setup (Optional)

This step sets up speech-to-text (talking to your agent) and text-to-speech (your agent talking back to you). **Skip this step if you just want to type in the browser.**

If you want voice capability:

1. Click **Test Microphone** — speak a few words, and it will confirm your microphone was detected.
2. Click **Test Speaker** — you should hear a short tone.
3. Click **Download Voice Models** — this downloads two additional AI models (Whisper for speech recognition, Kokoro for voice synthesis). This takes another 5–10 minutes.

If either test fails, check that your microphone and speaker are plugged in and not muted in your system settings.

Click **Continue** (or click **Skip Voice** if you do not want this feature).

---

### Step 9: Hardware Validation

This step automatically tests your computer's performance to make sure it is compatible with your chosen profile.

Click the **Run Hardware Check** button. The wizard will:

1. Detect how much RAM you have.
2. Run a quick speed test using your AI model.
3. Show you your results, including "tokens per second" — a measure of how fast your agent thinks.

**Reading the results:**

- **Compatible: Yes** — your computer meets the requirements for your profile.
- **Compatible: No** — your computer may be too slow for the selected profile. The wizard will suggest which profile to switch to.
- **Tokens per second**: Higher is better. 5+ is comfortable for conversation. Under 2 means responses will be slow (30–60 seconds each).

Click **Continue** when done.

---

### Step 10: License Binding

Enter the **license key** your operator gave you in the text field (it looks like `AGNT-XXXX-XXXX-XXXX`). Click **Bind License**.

You will see a confirmation with your license tier and expiry date. If you see an error, double-check that you copied the full key exactly as provided.

Click **Continue**.

---

### Step 11: Health Check

The wizard automatically checks that all the internal components started correctly. It checks: the AI engine, the chat interface, the agent core, the database, and the document search system.

Click **Run Health Check**. Within a few seconds, you will see a list of services, each with either a green checkmark (healthy) or a red cross (problem).

**If everything is green:** Click **Continue** to proceed to the final step.

**If something shows red:** Do not panic. Wait 30 seconds and click "Run Health Check" again. Services sometimes take a moment to fully start. If a service still shows red after two attempts, see the [Troubleshooting](#10-troubleshooting) section.

---

### Step 12: Go Live!

You are done! The wizard will:

1. Save all your configuration.
2. Start your agent.
3. Display a QR code you can scan with your phone to open the chat interface on any device on your home or office network.

Click **Complete Setup**. Your agent is now live.

---

## 6. Using Your Agent

### Chatting in the Browser

Open your web browser and go to:

```
http://localhost:3000
```

This is the Open WebUI chat interface — a clean, modern chat window that works similarly to consumer AI chat products you may have seen.

**First-time account creation:**

The first time you open the chat interface, you will be asked to create an account. Enter your name, email address, and a password (this is a local account — it does not connect to any external service). This becomes your admin account.

**Starting a conversation:**

1. Click the **"New Chat"** button (usually in the top-left corner or center of the screen).
2. Type your message in the text box at the bottom and press Enter.
3. Your agent will respond, typically within a few seconds (longer for complex questions).

**Switching between agents (if you set up multiple profiles):**

If you configured multiple profiles in Step 3, you can switch between them using the model selector dropdown at the top of the chat window.

**Uploading a document for questions:**

1. In the chat input area, look for a paperclip or attachment icon.
2. Click it and choose a file from your computer.
3. After the file uploads, ask your question about it.

---

### Using Telegram (if configured)

1. Open the Telegram app on your phone.
2. Search for your bot's username (the one you chose when creating it with @BotFather).
3. Tap on it and then tap **Start**.
4. Type your message — your agent will respond, usually within a few seconds.

**Voice messages:** If you send a voice message in Telegram, your agent will automatically transcribe it and respond as if you had typed it.

**Useful Telegram commands:**

- `/start` — Begins a new conversation
- `/help` — Shows what the agent can do
- `/clear` — Clears the current conversation history

---

### Using SMS or WhatsApp (if configured)

Text your agent at the Twilio phone number your operator configured. Start with a normal message like "Hello" to introduce yourself.

**What works well via text:**

- Asking questions ("What time is my next meeting?")
- Setting reminders ("Remind me to call John at 3pm tomorrow")
- Requesting information ("What was in the email from Sarah last week?")
- Short research questions ("What is the weather forecast for tomorrow?")

**What works less well via text:**

- Long back-and-forth conversations (no conversation history between separate text threads)
- Uploading documents (not supported via SMS)
- Requesting very long or detailed responses (texts have length limits)

---

## 7. Adding Documents and Knowledge

Your agent can answer questions about documents you give it — a process called "document Q&A" or "RAG" (Retrieval-Augmented Generation, but do not worry about the technical name).

### Uploading Documents via the Chat Interface

1. Open **http://localhost:3000** in your browser.
2. In the chat area, click the **paperclip / attachment icon** in the message input bar.
3. Select a file from your computer. Supported formats: PDF, Word (.docx), plain text (.txt), Markdown (.md), CSV.
4. Wait for the upload indicator to finish.
5. Ask a question about the document in the same message or the next one. For example: "Summarize the main points of this document" or "What does this document say about return policies?"

### Uploading Documents via the Wizard (during setup)

If you are still in the setup wizard, you can upload documents in Step 5. These become part of the agent's permanent knowledge base and persist even after you restart the agent.

### What Happens to Your Documents?

Uploaded documents are:

1. Stored in a folder inside Docker (inside your computer — not sent anywhere external).
2. Broken down into chunks of text.
3. Converted into a mathematical form ("embeddings") that the AI can search.
4. Stored in a local database called ChromaDB.

When you ask a question, the agent searches this database for relevant chunks and uses them to form its answer. It will cite where it found the information.

---

## 8. Managing Your Agent

### Checking Status

To see whether all components are running:

**Windows — Command Prompt** (type `cmd` in the Start menu):
```
cd C:\AgentCore
docker compose ps
```

**Mac — Terminal:**
```bash
cd ~/Documents/AgentCore
docker compose ps
```

You will see a table listing each component and its status. All should show `running` or `healthy`.

### Starting and Stopping

**To start the agent** (after it has been stopped):

```bash
docker compose up -d
```

Wait about 60 seconds for everything to start, then open http://localhost:3000.

**To stop the agent** (to free up computer resources, or before shutting down your computer):

```bash
docker compose down
```

This stops all components cleanly. Your data (conversations, documents) is preserved.

**To restart the agent** (useful if something seems stuck):

```bash
docker compose restart
```

**Important:** When you stop the agent with `docker compose down`, your data is safe — it is stored in Docker volumes on your computer. The command `docker compose down -v` (with the `-v` flag) permanently deletes all your data. Only use that if you specifically want to wipe everything and start fresh.

---

### Auto-Start on Boot (Optional)

If you want the agent to start automatically every time your computer turns on:

**Windows — Task Scheduler:**

1. Press the Windows key + R, type `taskschd.msc`, and press Enter.
2. In the right panel, click **"Create Basic Task…"**
3. Name it "Start AgentCore" and click Next.
4. Choose "When the computer starts" and click Next.
5. Choose "Start a program" and click Next.
6. In the "Program/script" field, enter: `docker`
7. In the "Add arguments" field, enter: `compose -f C:\AgentCore\docker-compose.yml up -d`
8. Click Next, then Finish.

**Mac — Login Items:**

1. Click the Apple logo → "System Settings" (or "System Preferences" on older macOS).
2. Click "General" → "Login Items."
3. Click the **+** button under "Open at Login."
4. Navigate to your Applications folder and select **Docker** (to ensure Docker Desktop starts on login).

For the agent itself on Mac, the simplest approach is to create a small script and add it to Login Items:

1. Open TextEdit, go to Format → Make Plain Text, and paste:
   ```bash
   #!/bin/bash
   sleep 30
   cd ~/Documents/AgentCore
   docker compose up -d
   ```
2. Save it as `start-agentcore.sh` in your Documents folder.
3. Open Terminal and run: `chmod +x ~/Documents/start-agentcore.sh`
4. Add `start-agentcore.sh` to Login Items using the same steps above.

---

## 9. Getting Updates

Your operator may periodically release updates with improvements and bug fixes.

### Checking for Updates

Open the admin dashboard at **http://localhost:8080/dashboard** and look for an "Updates" tab or section. If an update is available, it will show the new version number and what changed.

### Applying an Update

When an update is available:

1. Stop the agent: `docker compose down`
2. Your operator will provide you with an updated bundle ZIP file. Extract it to your AgentCore folder, overwriting the existing files (but **not** your `.env` file — preserve that).
3. Run: `bash setup.sh`
4. Start the agent: `docker compose up -d`
5. Open http://localhost:3000 and verify everything works.

If the update requires database changes, the agent applies them automatically on first start.

---

## 10. Troubleshooting

### "I cannot open http://localhost:3000"

**Check 1 — Is Docker running?**

- **Windows**: Look for the Docker whale icon in your system tray (bottom-right). If it is not there, open Docker Desktop from the Start menu and wait for it to say "Running."
- **Mac**: Look for the Docker whale icon in the menu bar at the top. If missing, open Docker from your Applications folder.

**Check 2 — Is the agent started?**

Open a terminal in your AgentCore folder and run `docker compose ps`. If you see services listed as "exited" instead of "running," start them: `docker compose up -d`

**Check 3 — Wait a little longer.**

After starting the agent, the chat interface (Open WebUI) can take up to 60 seconds to finish loading. Try refreshing after a minute.

---

### "The agent is very slow or takes a long time to respond"

AI responses take longer when:

- Your computer does not have much RAM (less than 16 GB)
- A larger AI model is loaded (larger models are more capable but slower)
- Other programs on your computer are using a lot of memory

**What to try:**

- Close other programs while using the agent.
- In the wizard (or in the model selector at http://localhost:3000), switch to a smaller model. The `phi4-mini` model is much faster on lower-end hardware, though slightly less capable.
- Check how much RAM is being used: on Windows, open Task Manager (Ctrl+Shift+Esc) and look at the "Memory" column. On Mac, open Activity Monitor (spotlight search "Activity Monitor").

---

### "The agent does not know about recent events"

By default, the AI model has knowledge up to its training date (usually several months to a year or more before you installed it). To get current information:

- Make sure the **web search tool** is enabled. You can check this in the Setup Wizard (re-run it if needed) or by asking your agent: "Can you search the web?"
- The web search tool requires an active internet connection.
- You can also enable the Tavily web search API (a free tier is available at tavily.com) by adding your `TAVILY_API_KEY` to the `.env` file for better search quality.

---

### "My Telegram bot is not responding"

1. Check that the agent is running: `docker compose ps`
2. Verify the bot token in your `.env` file matches what @BotFather gave you.
3. Restart just the agent component: `docker compose restart agentcore`
4. Wait 30 seconds and try messaging the bot again.
5. If still not working, check the logs: `docker compose logs --tail=50 agentcore`

---

### "I ran out of disk space"

AI models take up significant disk space (2–15 GB each). If your computer's disk is filling up:

**See what is taking space:**

```bash
docker system df
```

**Remove unused Docker resources (safe — keeps your data):**

```bash
docker system prune
```

**Remove a specific AI model** (your agent will need to re-download it if you want it back):

```bash
docker exec agentcore-ollama ollama rm model-name-here
```

To see which models are installed: `docker exec agentcore-ollama ollama list`

---

### "The agent forgot our conversation"

By default, each new chat session starts fresh. Your conversation history is saved within a session, but previous sessions are archived, not automatically loaded.

- To review past conversations: open http://localhost:3000 and look for a "History" or sidebar icon.
- If you want the agent to remember facts between sessions (like your preferences), tell it directly: "Remember that I prefer short bullet-point answers." Many profiles support this.
- If conversations are disappearing unexpectedly, this may indicate a database issue — run `docker compose logs postgres` and send the output to your operator.

---

### "Setup complete but something is clearly wrong"

Copy and send the following to your operator for help:

```bash
docker compose ps
docker compose logs --tail=50 agentcore
docker compose logs --tail=50 open-webui
```

These commands show the current state of all components and any recent error messages.

---

## 11. Privacy and Security

### Where Your Data Lives

All data is stored on your computer inside Docker volumes (named folders managed by Docker):

| Data | Stored in |
|------|-----------|
| Conversation history | PostgreSQL database (agentcore_postgres_data) |
| Uploaded documents | ChromaDB database (agentcore_chromadb_data) |
| AI models | Ollama data (agentcore_ollama_data) |
| Agent configuration | AgentCore data (agentcore_agentcore_data) |
| Chat interface settings | Open WebUI data (agentcore_open_webui_data) |

None of this data leaves your computer unless you explicitly configure a cloud API (like adding a Telegram bot token or a Google Calendar connection).

### Who Can Access the Agent?

By default, the chat interface (http://localhost:3000) is only accessible from your own computer. The word "localhost" means "this computer only."

If you want other people on your home or office network to access it (for example, from another computer or your phone while on the same Wi-Fi), the URL would be `http://[your computer's IP address]:3000` instead of `localhost`. Ask your operator to configure this if needed.

### How to Completely Delete All Data

If you want to remove the agent and all its data permanently:

```bash
docker compose down -v
```

**Warning:** The `-v` flag permanently deletes all conversations, uploaded documents, AI models, and configuration. This cannot be undone. Only use this if you want a completely fresh start or are decommissioning the system.

To also remove the Docker images (frees up even more disk space):

```bash
docker compose down -v --rmi all
```

---

## 12. Quick Reference Card

Cut out or bookmark this section for easy day-to-day reference.

### Your Agent's Addresses

| What | Address |
|------|---------|
| Chat interface (main) | http://localhost:3000 |
| Setup wizard | http://localhost:8888 |
| Admin/API dashboard | http://localhost:8080/dashboard |

### Common Commands

Open a Terminal (Mac) or Command Prompt (Windows) in your AgentCore folder, then run:

| What you want to do | Command |
|--------------------|---------|
| Start the agent | `docker compose up -d` |
| Stop the agent | `docker compose down` |
| Restart the agent | `docker compose restart` |
| Check if everything is running | `docker compose ps` |
| See recent error messages | `docker compose logs --tail=50 agentcore` |
| See all logs | `docker compose logs` |

### How to Open a Terminal in Your AgentCore Folder

**Windows:** Open File Explorer, navigate to `C:\AgentCore`, then click the address bar at the top, type `cmd`, and press Enter.

**Mac:** Open Terminal, then type `cd ~/Documents/AgentCore` and press Enter.

---

### Getting Help

If you cannot resolve an issue using this guide, contact your operator. When reaching out, please include:

1. A description of what you were trying to do.
2. What happened (exact error text if possible).
3. The output of these two commands:
   ```bash
   docker compose ps
   docker compose logs --tail=50 agentcore
   ```

---

*AgentCore — End-User Deployment Guide*
*For technical operator documentation, refer to the separate operator guide.*
