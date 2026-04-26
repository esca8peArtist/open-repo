# Containerized AI Agents — Product Requirements

**Project:** Containerized AI Agents (Deployable Edge AI Agent Packages)
**Version:** 1.1 (Final)
**Date:** 2026-03-09
**Status:** ✅ REQUIREMENTS FINALIZED — Ready for Architecture Phase

---

## 1. Executive Summary

A turnkey, fully-offline-capable product that ships as a deployable image pre-configured with an AI agent profile. Customers purchase hardware from us (or bring their own compatible hardware), the image is flashed/installed at setup time, and the agent boots up immediately operational — accessible via web chat, voice, and (when internet is available) SMS/WhatsApp. No ongoing subscription, no cloud inference costs, no data leaving the device.

**Business model:** One-time hardware + software bundle sale (no recurring fee). Software is cryptographically bound to the hardware it was installed on.

---

## 2. Answered Decisions

| # | Question | Decision |
|---|---|---|
| Image format | OS image or Docker Compose? | **Both** (see Section 3 for pros/cons) |
| Profiles | 6 profiles sufficient? | **Yes — keep as is** |
| Model licensing | Use compliant models only | **Flagged below — see Section 7** |
| Twilio billing | Who pays? | **Customer's own Twilio account** + free Telegram channel always included |
| Internet at runtime | Required or optional? | **Hybrid** — inference fully offline always; comms (SMS/WhatsApp/Telegram) work when internet available, degrade gracefully when not |
| Model updates | How delivered? | **Web UI with "Check for Updates" button + 1-click install** |
| Multi-tenancy | One box = one client? | **Multiple agents per machine supported** — admin dashboard to configure |
| Pricing | Recurring or one-time? | **One-time sale.** Image cryptographically locked to hardware via TPM binding. |
| Voice | Standard or optional? | **Standard on all profiles** (hardware-permitting) |
| Offline capability | Runtime offline? | **Yes — full offline inference. Internet-dependent tools degrade gracefully.** |
| Audio hardware | Bundle mic? | **Yes — USB microphone bundled with Tier 1 and Tier 2 hardware packages** |
| USB GSM modem | Include drivers? | **Add-on only** — drivers not included in base image; separate add-on package |
| Workflow orchestration | n8n vs Airflow vs custom? | **Custom lightweight orchestration layer** (see Section 4 — Orchestration) |

---

## 3. Image Format: Pros & Cons

Both formats will be produced. The OS image is the primary product. The Docker Compose bundle is the developer/self-hosted option.

### Option A: Bootable OS Image (.img / .iso)

**What it is:** A complete Ubuntu Server 24.04 LTS base with all services pre-installed, pre-configured, and ready to boot. Flash to an SSD/NVMe, plug in, power on — the setup wizard starts automatically.

| Pros | Cons |
|---|---|
| True plug-and-play — zero technical knowledge needed | Larger file size (~15–40GB depending on included models) |
| Entire system state is known and controlled | OS version is fixed at image build time |
| Easier to cryptographically bind to hardware (TPM, boot chain) | Harder to update the base OS later |
| Best customer experience — "just works" | Requires a tool to flash to NVMe (we provide a USB flasher stick) |
| Consistent environment — identical across all units | Cannot be installed on top of existing OS |
| Harder to extract and copy individual components | |

**Best for:** End customers who want zero setup friction. Primary product SKU.

---

### Option B: Docker Compose Bundle (.zip / .tar.gz)

**What it is:** A ZIP archive containing `docker-compose.yml`, environment templates, setup scripts, and a configuration wizard. Runs on any existing Ubuntu/Debian or macOS host. Customer installs Docker, runs one command, wizard starts.

| Pros | Cons |
|---|---|
| Flexible — installs on customer's existing machine | Requires Docker knowledge to troubleshoot |
| Each container can be updated independently | Harder to hardware-lock (customer controls the host OS) |
| Works on Mac Mini out of the box (macOS Docker Desktop) | Customer's host OS environment can affect behavior |
| Easier for developers to inspect and extend | More moving parts — potential compatibility issues |
| Smaller initial download (models pulled separately) | Less suitable for non-technical customers |

**Best for:** Technical users, developers, agencies deploying on their own infrastructure. Secondary SKU.

---

## 4. Core Technology Stack

### Inference Layer
- **Ollama** — Local model serving (OpenAI-compatible REST API). GPU/unified-memory accelerated. Pulls and manages all models. Fully offline after initial model download.

### Interface Layer
- **Open WebUI** — Primary web chat interface. RAG, voice chat, function calling, multi-user auth, model switching. Accessible on local network at `http://agent.local`.
- **AgentCore** (custom-built, internal codename) — Lightweight real-time event-driven orchestration layer written in Python (asyncio + FastAPI). Handles tool dispatch, multi-step task pipelines, message routing between agent modules, and inter-agent communication. Exposed at `http://agent.local:8080/api`. Configuration via the admin web UI (no code required for end users).
  - *Why not Apache Airflow:* Apache 2.0 license is clean, but Airflow is architected for scheduled batch pipelines — incompatible with sub-3-second real-time agent responses. Wrong tool for this job.
  - *Why not n8n:* Sustainable Use License explicitly prohibits embedding in commercial products without an Enterprise agreement.

### Agent Framework
- **OpenAI Agents SDK** (provider-agnostic, pointed at Ollama's API) — Multi-agent orchestration, tool calling, guardrails
- **MCP (Model Context Protocol)** — Standardized tool protocol for all integrations

### Voice Layer (Standard — All Profiles)
- **STT (Speech-to-Text):** faster-whisper (Whisper large-v3 model, MIT license) — 90+ languages, runs fully offline, ~1-2s transcription latency
- **TTS (Text-to-Speech):** Kokoro-82M (Apache 2.0 license) — high-quality natural voices, runs fully offline, ~0.5-1s synthesis latency
- Voice input/output integrated directly into Open WebUI (built-in support)
- Also available via phone if customer's hardware has audio ports (USB microphone/speaker)

### Communication Layer
- **Telegram Bot** (free, no per-message cost) — Always included on all profiles. Operator talks to their agent via Telegram app. Works over internet when available. Great for the device owner's own phone.
- **Twilio** (customer's own account — paid, ~$1/month for phone number + ~$0.008/SMS) — Optional channel for SMS and WhatsApp to end customers. Configured during setup wizard if customer has a Twilio account. Requires internet connectivity.
- **Web chat** (Open WebUI) — Always available on local network. No internet required.

### RAG / Knowledge Base
- **ChromaDB** — Local vector database. Containerized. All embeddings computed locally.
- **Embedding model:** nomic-embed-text (MIT license, runs via Ollama) — no external API calls
- Documents ingested: PDF, DOCX, TXT, Markdown, web pages (scraped at setup time)

### Database / Logging
- **PostgreSQL** — Conversation history, audit logs, agent configurations, user management
- **Redis** — Message queue and caching (Tier 3+ profiles with concurrent agents)

### Update Management
- **Custom Update Server** (built by us) — Serves signed update manifests listing available versions
- **Agent Web UI** — "Check for Updates" button pings our update server (only when internet is available). Shows changelog. Installs with one click.
- **Updates include:** model version upgrades, container image updates, tool/plugin additions

### Multi-Agent Management Dashboard
- Built on top of Open WebUI admin panel
- Allows configuring multiple agent profiles on one machine
- Each agent has its own: model, system prompt, tools, knowledge base, communication channel
- Hardware resource allocation per agent (VRAM/RAM limits via Ollama config)

---

## 5. Copy Protection — Hardware Binding

### Requirement
Software image must be cryptographically bound to the specific hardware it was installed on. Copying the image to another machine must not work.

### Approach: TPM-Based Hardware Fingerprint Binding

**How it works:**
1. At first boot, the setup wizard reads the machine's hardware fingerprint:
   - TPM 2.0 endorsement key (unique per chip, cannot be spoofed)
   - CPU serial number
   - System board UUID
   - Primary NIC MAC address
2. These values are combined into a SHA-256 hardware fingerprint
3. A symmetric encryption key is derived from this fingerprint (PBKDF2)
4. All sensitive configuration data (system prompts, API keys, agent configs) is encrypted with this derived key
5. The key derivation salt is stored in the TPM's sealed storage — it can only be read by that specific TPM on that specific machine
6. If the image is copied to a different machine: the TPM key is missing, the derived key cannot be reproduced, the configuration fails to decrypt, and the agent will not start

**What this means in practice:** Even if someone clones the NVMe drive, the image simply will not boot into a working state on different hardware.

**Fallback (for Docker Compose SKU where TPM binding is harder):**
- Offline license key generated at purchase time, bound to hardware fingerprint
- Customer enters license key during first-run setup wizard
- License key is validated against hardware fingerprint locally (no internet needed)
- Key is one-time use and tied to one set of hardware identifiers

### No USB Dongle Required
USB dongles add complexity and a point of failure (dongle gets lost/broken). TPM binding is invisible, more secure, and requires no extra hardware since all modern mini PCs and Mac Minis include a TPM or Apple Secure Enclave equivalent.

---

## 6. Offline Operation

### Core Offline Capabilities (All working without internet after setup)

| Feature | Offline? | Notes |
|---|---|---|
| LLM inference (Ollama) | ✅ Yes | All models run locally |
| Web chat (Open WebUI) | ✅ Yes | Accessible on local network |
| Voice input (Whisper STT) | ✅ Yes | Runs locally |
| Voice output (Kokoro TTS) | ✅ Yes | Runs locally |
| RAG / knowledge base queries | ✅ Yes | ChromaDB + local embeddings |
| Document ingestion | ✅ Yes | Pre-loaded at setup time |
| Conversation logging | ✅ Yes | Local PostgreSQL |
| Multi-agent management | ✅ Yes | All local |
| Update check | ⚠️ When internet available | "Check for Updates" only works online |
| Telegram bot | ⚠️ When internet available | Telegram requires internet |

---

### ⚠️ CRITICAL CONFLICT — SMS/WhatsApp + Offline Requirement

**The problem:** Twilio (SMS and WhatsApp) is a cloud service. To receive an SMS, Twilio routes the message to a webhook URL on the agent's machine. This requires the agent machine to have internet access and a reachable URL. This fundamentally conflicts with the "full offline after setup" requirement.

**Options to resolve — needs your decision:**

| Option | Description | Trade-off |
|---|---|---|
| **A) Accept internet for comms** | Inference is offline; SMS/WhatsApp still requires internet | Simplest. Most customers will have internet. Just document the requirement. |
| **B) USB GSM Modem** | Plug a USB SIM card modem into the machine. Agent receives SMS directly via cellular without internet. | Adds cost (~$30–80 modem), customer needs active SIM card. Fully offline cellular SMS. |
| **C) Local-only channels only** | Remove Twilio/SMS entirely. Use web chat + voice + Telegram (when internet available) only. | Simplest for offline but loses "reach customers via their phone" capability. |
| **D) Hybrid** | Core inference offline. Comms tier (Twilio) is an optional add-on that requires internet. Graceful degradation — if internet is down, agent still responds to local web chat and voice. | Most flexible. Recommended. |

**Recommendation: Option D (Hybrid)** — Internet-dependent tools (Twilio, web search, external APIs) are optional modules that work when internet is available and fail gracefully when it is not. The core agent always works offline.

> **ACTION REQUIRED:** Confirm which option you prefer before architecture phase begins.

---

## 7. ⚠️ Model Licensing Flags — READ CAREFULLY

All models selected must allow: (1) commercial use, (2) redistribution as part of a packaged product, (3) use in a product sold to third parties.

### ✅ APPROVED MODELS

#### Qwen2.5 / Qwen3 (Alibaba) — Apache 2.0
- **License:** Apache 2.0 — most permissive possible
- **Commercial use:** ✅ Fully allowed including resale and redistribution
- **Requirements:** Include original license notice in the product. No attribution branding required.
- **Verdict: PREFERRED. Use Qwen models as the primary models across all profiles.**

#### DeepSeek-R1 / DeepSeek-V3 (DeepSeek AI) — MIT License
- **License:** MIT — extremely permissive
- **Commercial use:** ✅ Fully allowed including resale, modification, redistribution
- **Requirements:** Include original license and copyright notice only
- **Verdict: APPROVED. Excellent for reasoning-heavy profiles (BI, Enterprise).**

#### Phi-4 / Phi-3.5 (Microsoft) — MIT License
- **License:** MIT
- **Commercial use:** ✅ Fully allowed
- **Requirements:** Include license notice only
- **Verdict: APPROVED. Best for Tier 1 edge hardware (smallest footprint).**

#### Mistral 7B / Mistral-Large (Mistral AI) — Apache 2.0
- **License:** Apache 2.0
- **Commercial use:** ✅ Fully allowed
- **Verdict: APPROVED. Good fallback option.**

---

### ⚠️ CONDITIONAL MODELS — USE WITH RESTRICTIONS

#### Meta Llama 3.1 / 3.3 — Meta Community License (NOT open source)
- **License:** Meta Community License Agreement (custom, not Apache/MIT)
- **Commercial use:** ✅ Allowed **with conditions:**
  1. Must register with Meta at [llama.com](https://llama.com) before downloading/distributing
  2. Must display **"Built with Meta Llama"** prominently in your product and marketing
  3. Must include "Llama" in the name of any derived AI model
  4. The 700M monthly active user cap before needing Meta's explicit approval (irrelevant at our scale)
  5. Cannot use Llama outputs to train models that compete with Meta's products
- **Verdict:** ⚠️ **CONDITIONALLY OK — but requires Meta registration and "Built with Llama" branding in the product. This branding obligation may conflict with your own product branding. Recommend using Qwen/DeepSeek instead to avoid this obligation. Only use if there's a specific capability reason.**

---

### ❌ FLAGGED MODELS — DO NOT USE

#### Google Gemma 3 — Gemma Terms of Use (NOT open source)
- **License:** Custom Gemma Terms of Use
- **Commercial use:** ⚠️ Restricted
- **Key restrictions:**
  1. You cannot use Gemma to develop any AI model that competes with Google products
  2. Google can terminate your license unilaterally if they determine the use causes harm (subjective)
  3. "Prohibited uses" list is broad and vaguely worded — legal risk in commercial product
  4. Redistribution in a packaged commercial product enters a gray zone under Gemma's terms
- **Verdict: ❌ DO NOT USE. Legal risk for a commercial resale product. Replace with Qwen (Apache 2.0) or Phi-4 (MIT).**

---

### ⚠️ TOOL/FRAMEWORK LICENSING FLAGS

| Tool | License | Commercial Use | Flag |
|---|---|---|---|
| Ollama | MIT | ✅ Yes | None |
| Open WebUI | BSD-3-Clause | ✅ Yes | None |
| AgentCore (custom-built) | Owned by us | ✅ Yes | None — no third-party risk |
| faster-whisper (STT) | MIT | ✅ Yes | None |
| Kokoro-82M (TTS) | Apache 2.0 | ✅ Yes | None |
| ChromaDB | Apache 2.0 | ✅ Yes | None |
| OpenAI Agents SDK | MIT | ✅ Yes | None |
| PostgreSQL | PostgreSQL License | ✅ Yes | None |

#### ✅ n8n — RESOLVED: Replaced with AgentCore (custom)
- **Decision:** Build a custom lightweight orchestration layer (AgentCore) instead of using n8n or Apache Airflow.
- **Why not n8n:** Sustainable Use License prohibits commercial embedding without Enterprise agreement.
- **Why not Apache Airflow:** Apache 2.0 license is fully clean, but Airflow is architected for scheduled batch pipelines — high overhead, incompatible with sub-3-second real-time agent response requirements.
- **AgentCore spec:** Python asyncio + FastAPI, event-driven, handles tool dispatch, multi-step pipelines, message routing, inter-agent communication. Fully owned by us — no third-party license constraints ever.

---

## 8. Agent Profiles (Confirmed — No Changes)

### Profile 1: Personal Productivity
**Models:** Qwen2.5-7B-Instruct (primary) | Phi-4-mini (Tier 1 fallback)
**Tools:** Calendar (Google / CalDAV), Email (IMAP/SMTP local), RAG on personal docs, Web search (online only), Scheduler
**Channels:** Web chat, Voice, Telegram (online only), SMS/WhatsApp (online + Twilio)
**Hardware:** Tier 1

### Profile 2: Customer Support
**Models:** Qwen2.5-7B-Instruct + RAG
**Tools:** RAG over company knowledge base, Ticket DB (local), Email alerts (SMTP), Conversation logger, Business hours scheduler
**Channels:** Web chat widget, Voice, SMS/WhatsApp (online only)
**Hardware:** Tier 1

### Profile 3: Sales Outreach
**Models:** Qwen2.5-14B-Instruct (primary) | Qwen2.5-7B (Tier 1 fallback)
**Tools:** Calendar booking, Local CRM DB, SMS/WhatsApp (Twilio, online), Outreach scheduler, Lead scoring
**Channels:** SMS (primary), WhatsApp, Email (SMTP), Web chat
**Hardware:** Tier 2 (recommended); Tier 1 with lighter model

### Profile 4: Developer Assistant
**Models:** Qwen3-Coder-30B-A3B (primary, MoE — 3B active) | DeepSeek-Coder-V2-Lite-7B (Tier 2 fallback)
**Tools:** RAG over codebase, GitHub API (online only), Code execution sandbox, Slack webhook (online only), File system read-only
**Channels:** Web chat, Voice, Slack (online only)
**Hardware:** Tier 2 (minimum), Tier 3 (recommended)

### Profile 5: Business Intelligence
**Models:** DeepSeek-R1-14B (primary reasoning) | Qwen2.5-14B (fallback)
**Tools:** Local DB connector (SQLite/PostgreSQL/MySQL read-only), CSV/Excel ingestion, Python code execution, Report generator (PDF), Alert scheduler, Email/SMS delivery (online only)
**Channels:** Web dashboard, Email reports (online only), SMS alerts (online only)
**Hardware:** Tier 3

### Profile 6: Enterprise Orchestrator
**Models:** Qwen3-72B (orchestrator, quantized) + multiple Qwen2.5-7B sub-agents
**Tools:** All tools from Profiles 1–5, Multi-agent bus (Redis), Audit log (PostgreSQL), Admin dashboard, Webhook manager, Multi-user access control
**Channels:** All channels
**Hardware:** Tier 4

---

## 9. Hardware Tiers (Confirmed)

### Tier 1 — Entry (~$400–600)
**Recommended:** Mac Mini M4 16GB (~$599) or Beelink EQR6 32GB (~$449)
**Runs:** Profiles 1, 2 | Models: 7B–8B | Speed: 15–25 tok/s

### Tier 2 — Mid (~$800–1,400)
**Recommended:** Mac Mini M4 Pro 24GB (~$1,399)
**Runs:** Profiles 1, 2, 3, 4 (lightweight) | Models: up to 14B–32B (MoE) | Speed: 10–18 tok/s

### Tier 3 — Pro (~$2,400–3,500)
**Recommended:** Mac Mini M4 Pro 64GB (~$2,399) or custom RTX 4090 Mini-ITX PC (~$3,000)
**Runs:** Profiles 4 (full), 5 | Models: 70B quantized | Speed: 8–15 tok/s

### Tier 4 — Enterprise (~$4,000–8,000)
**Recommended:** NVIDIA DGX Spark (~$3,999)
**Runs:** Profile 6 + concurrent multi-agent | Models: up to 200B | Speed: 20–40 tok/s

---

## 10. Communication Channels — Final Design

### Always Included (Fully Offline Capable)
| Channel | Tech | Cost | Offline? |
|---|---|---|---|
| Web Chat | Open WebUI (local network) | Free | ✅ Yes |
| Voice In/Out | Whisper STT + Kokoro TTS | Free | ✅ Yes |

### Included (Requires Internet When Used)
| Channel | Tech | Cost | Offline? |
|---|---|---|---|
| Telegram | Telegram Bot API | Free | ❌ Needs internet |

### Optional Add-On (Requires Customer's Own Account + Internet)
| Channel | Tech | Cost | Offline? |
|---|---|---|---|
| SMS | Twilio SMS | ~$1/mo + $0.008/msg (customer pays) | ❌ Needs internet |
| WhatsApp | Twilio WhatsApp API | ~$0.005/msg (customer pays) | ❌ Needs internet |
| Voice Calls | Twilio ConversationRelay | Per-minute (customer pays) | ❌ Needs internet |

### Free SMS Alternative (No Internet Needed — Optional Add-On)
| Channel | Tech | Cost | Offline? |
|---|---|---|---|
| Cellular SMS | USB GSM Modem + SIM card | ~$30–80 modem + SIM plan | ✅ Offline via cellular |

*USB GSM modem option: plug a USB cellular modem with an active SIM card into the machine. Agent receives/sends SMS directly over cellular — no internet routing needed. Customer buys their own SIM plan.*

---

## 11. First Boot Setup Wizard — Requirements

Must run automatically in a web browser on the local network after first power-on. Steps:

1. **Welcome** — Choose language, name the agent
2. **Profile selection** — Pick one of 6 profiles (with descriptions and use-case examples)
3. **Multi-agent setup** (if applicable) — Add additional profiles to same machine, allocate resources
4. **Communication channels** — Enable web chat (always on), Telegram (enter bot token), SMS/WhatsApp (enter Twilio credentials), USB modem (detect and configure)
5. **Knowledge base** — Upload documents for RAG (PDF, DOCX, TXT, URLs to scrape at setup)
6. **Integration setup** — Connect calendar, CRM, email (all optional; offline-only if not connected)
7. **Model pull** — Recommended model auto-downloads (requires internet this one time)
8. **Voice setup** — Test microphone and speaker, download STT/TTS models
9. **Hardware validation** — Benchmark the hardware, confirm profile compatibility
10. **License binding** — Generate hardware fingerprint, bind license (no internet required)
11. **Health check** — Run self-test on all services
12. **Go live** — Agent starts, display the local URL and QR code

---

## 12. Update System — Requirements

- **Update server:** We host a signed manifest at a fixed URL listing available updates per product version
- **On-device:** "Check for Updates" button in the admin dashboard — pings update server if internet is available
- **Notification:** Dashboard shows a badge/banner when a new version is available: "Update available: v1.2.0 — [View Changelog]"
- **Installation:** "Install Update" button — one click. Downloads signed container images or model files, verifies signature before applying, restarts services gracefully. No SSH required.
- **Rollback:** Previous version is kept for 1 cycle; "Rollback" button available for 24 hours after an update
- **Offline devices:** Will not check for updates automatically. User must manually trigger check when connected.

---

## 13. All Questions Resolved ✅

| # | Question | Decision |
|---|---|---|
| 1 | SMS/Offline conflict | **Hybrid (Option D)** — inference always offline; comms degrade gracefully without internet |
| 2 | Workflow orchestration | **Custom AgentCore** (Python asyncio + FastAPI) — no third-party license risk |
| 3 | USB GSM modem in image | **Add-on only** — separate add-on package, not in base image |
| 4 | Internet-dependent tools | Setup wizard asks customer to confirm internet availability; only shown tools that work offline-first with optional online features noted |
| 5 | Audio hardware (mic) | **USB microphone bundled** with Tier 1 and Tier 2 hardware packages |
| 6 | Update server infra | **AWS S3 + CloudFront** for signed update manifest (low cost, highly available) — the one always-on server-side component we maintain |

---

## 14. Out of Scope (Version 1.0)

- Model fine-tuning or training on customer data (inference only)
- Native mobile app (iOS/Android) — handled via web chat, voice, and Telegram
- HIPAA / SOC 2 compliance (required before healthcare profiles — future roadmap)
- Multi-location distributed agent clusters
- GPU training workloads
- Public cloud deployment option
- Customer analytics / usage dashboard on our end (no phone-home telemetry)

---

## 15. Model Selection Reference (All Profiles)

Models to be pre-selected at setup time based on hardware tier. All are compliant with commercial resale licensing.

| Model | License | Best For | Min RAM |
|---|---|---|---|
| Qwen2.5-7B-Instruct | Apache 2.0 ✅ | Profiles 1, 2 (general) | 8GB |
| Phi-4-mini-instruct | MIT ✅ | Tier 1 edge fallback | 4GB |
| Qwen2.5-14B-Instruct | Apache 2.0 ✅ | Profile 3 (sales) | 16GB |
| Qwen3-Coder-30B-A3B | Apache 2.0 ✅ | Profile 4 (dev) — MoE | 24GB |
| DeepSeek-R1-14B | MIT ✅ | Profile 5 (BI) reasoning | 16GB |
| DeepSeek-V3 (quantized) | MIT ✅ | Profile 5 (BI) heavy | 48GB |
| Qwen3-72B (quantized) | Apache 2.0 ✅ | Profile 6 orchestrator | 64GB |
| nomic-embed-text | Apache 2.0 ✅ | RAG embeddings (all) | 2GB |
| Whisper large-v3 | MIT ✅ | STT voice (all) | 2GB |
| Kokoro-82M | Apache 2.0 ✅ | TTS voice (all) | 1GB |

**Models explicitly excluded:** Gemma (Google — restricted commercial terms), Llama 3.x (Meta — branding obligations, unless acceptable to you after review)

---

*v1.1 finalized: 2026-03-09 | All questions resolved | Ready for architecture and build phase*
