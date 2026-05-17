---
title: "Autonomous Agent Containerization and Deployment — Requirements Analysis"
project: containerized-agents
status: research-complete
date: 2026-05-17
author: research-agent
---

# Autonomous Agent Containerization and Deployment Patterns
## Requirements Analysis for Multi-Project Orchestration

---

## Executive Summary

Containerization adds meaningful value to this specific setup — but only in the right places, and not as a wholesale migration of the orchestrator itself. The current multi-project workflow (resistance-research, seedwarden, stockbot, systems-resilience, mfg-farm, cybersecurity-hardening) is coordinator-driven: one orchestrator session spawns specialized research agents as needed, agents run sequentially or in small parallel batches, and the bottleneck is almost always token budget and API rate limits rather than process isolation or compute scheduling.

**What containerization concretely adds here:**

1. **Sandboxed code execution environments** — agents that write and run code (stockbot backtesting scripts, civic-tracker.py, mfg-farm print scripts) should run inside ephemeral containers so a bad script cannot touch the host filesystem or spawn persistent processes. The Claude Agent SDK's official guidance explicitly requires this.

2. **Service dependency isolation for AgentCore** — the existing `docker-compose.yml` already implements this correctly for the edge product: Ollama, PostgreSQL, Redis, ChromaDB, Open WebUI each run in isolated containers with health checks and named volumes. This is the right pattern for that use case.

3. **Reproducibility for the research pipeline** — running research agents with pinned Python environments (uv.lock) and predictable working directories reduces environment drift across sessions on the RPi 5 and any future machines.

**What containerization does NOT add here (and the complexity is not justified):**

- Kubernetes for 5-10 concurrent agents on a single RPi 5 or Jetson — the orchestration overhead exceeds the parallelization gains at this scale.
- Docker Compose for the orchestrator itself — the parent coordinator is a long-running Python/Claude process; wrapping it in a container adds startup latency without isolation benefit since it already owns the host shell.
- Ray for the current workload — Ray is appropriate at 50+ parallel agents or when cross-machine distribution is needed. Current workload peaks at 3-4 concurrent agents.

**Recommended approach:** Python asyncio coordinator (already present) + Docker for code execution sandboxes only + existing AgentCore Docker Compose for the edge product. Implement in two phases: Phase 1 is a one-day change; Phase 2 is optional if parallel research scales up.

**Confidence level:** High (80%+) on the lightweight recommendation. Medium (60%) on specific container specs for RPi 5 — memory budgets depend on which profiles are co-resident.

---

## 1. Current Deployment Pattern Assessment

### 1.1 What is actually running today

The SuperClaude Framework operates on a single RPi 5 (ARM64, inferred from platform metadata) with the following pattern:

- `ORCHESTRATOR_STATE.md` as shared state between sessions
- Sequential or lightly parallel agent sessions dispatched by a human or parent coordinator
- Projects are isolated at the filesystem level only (separate subdirectories under `projects/`)
- No process isolation between agents — if an agent writes to the wrong directory or spawns a subprocess, there is no sandboxing layer
- The stockbot project runs on a separate Jetson device with its own Docker Compose stack (confirmed from `docker-compose.jetson.yml` reference in ORCHESTRATOR_STATE.md)
- The containerized-agents project has a complete, production-quality Docker Compose stack for the AgentCore edge product

### 1.2 What the Claude Agent SDK requires for production use

The official SDK hosting guide (code.claude.com/docs/en/agent-sdk/hosting) states:

> "For security and isolation, the SDK should run inside a sandboxed container environment. This provides process isolation, resource limits, network control, and ephemeral filesystems."

Minimum resource allocation per SDK instance: 1 GiB RAM, 5 GiB disk, 1 CPU. The SDK is a long-running process, not a stateless API call — it maintains a persistent shell environment and manages file operations within a working directory.

### 1.3 What the Anthropic Managed Agents service offers (as of April 2026)

Anthropic launched Claude Managed Agents on April 8, 2026. Key specs:
- Each agent runs in a gVisor-isolated container on Anthropic infrastructure
- Network egress is default-deny; filesystem access scoped to `/workspace` (writable) and `/source` (read-only)
- Billing: $0.08/session-hour for runtime (idle time not charged) plus token costs (Sonnet 4.6: $3/$15 per MTok input/output; Opus 4.6: $5/$25)
- Session/harness/sandbox are decoupled — each can fail and recover independently
- The harness operates outside containers, treating them as tools via `execute(name, input) → string`

**Practical implication for this setup:** Managed Agents is appropriate for production, user-facing deployments where infrastructure management is a burden. For a self-hosted research pipeline on known hardware, the cost model ($0.08/hr runtime × parallel agents × continuous operation) adds up quickly compared to the existing zero-infrastructure-overhead pattern.

### 1.4 Existing containerization gaps to fix immediately

The current `docker-compose.yml` has two confirmed `0.0.0.0` bindings that violate project security rules:

- `open-webui`: `"${WEBUI_HOST:-0.0.0.0}:${WEBUI_PORT:-3000}:3000"` — should default to `127.0.0.1`
- `agentcore`: `"${AGENTCORE_HOST:-0.0.0.0}:${AGENTCORE_PORT:-8080}:8080"` — should default to `127.0.0.1`
- `wizard`: `"${WIZARD_HOST:-0.0.0.0}:${WIZARD_PORT:-8888}:8888"` — should default to `127.0.0.1`
- `nginx`: `"80:80"` — bare binding, should be `127.0.0.1:80:80` or Tailscale IP

These must be fixed before deploying the edge product in any environment with network exposure.

---

## 2. Architecture Options Matrix

### Option A: Current Pattern + Code Execution Sandboxes Only (Recommended — Phase 1)

**Description:** Keep the Python asyncio coordinator as-is. Add a single lightweight Docker sandbox container (or use the existing AgentCore Docker infrastructure) as a code execution jail for agents that need to run scripts. No changes to the orchestrator itself.

**Implementation:**
- One `sandbox` service in Docker Compose: a minimal Python 3.12-slim container with no persistent state
- Agent coordinator spawns `docker exec` or API calls to the sandbox for code execution
- The sandbox is ephemeral: started at task begin, destroyed at task end (Pattern 1 from the SDK hosting guide)
- Optionally, a second long-running sandbox for the stockbot backtesting loop (Pattern 2)

**Pros:**
- Near-zero additional overhead — sandbox container uses ~200-300 MB RAM idle
- Failure isolation for code execution: a crashed backtesting script cannot affect the host or other projects
- Reproducible Python environment (same container image = same result on RPi 5 and Jetson)
- Implementation time: 1 day
- Does not require Kubernetes or cluster management knowledge
- Compatible with current ARM64/RPi 5 setup

**Cons:**
- Does not isolate agent processes from each other at the OS level — still one Python interpreter running multiple coroutines
- No resource quotas between projects (a heavy resistance-research scraping job can still starve stockbot)

**Best for:** Current workload. Handles the top-priority isolation requirement (code execution safety) without introducing orchestration overhead.

---

### Option B: Docker Compose Multi-Agent Stack (Phase 2 — if parallel research scales)

**Description:** Each major project category gets its own container in a Docker Compose stack. The orchestrator container dispatches work to project-specific agent containers via a shared Redis queue.

**Sample compose structure:**
```
orchestrator        — coordinator, dispatches tasks
agent-research      — resistance-research, systems-resilience agents
agent-stockbot      — stockbot + backtesting sandbox
agent-seedwarden    — seedwarden + mfg-farm agents
redis               — task queue and result bus
postgres            — shared state store
```

**Resource estimate per container (RPi 5, 8GB RAM):**
- orchestrator: 512 MB
- agent-research: 1 GiB (matches SDK minimum)
- agent-stockbot: 1 GiB + 512 MB for sandbox
- agent-seedwarden: 512 MB
- redis + postgres: 256 + 128 MB
- Total: ~4 GiB — leaves 4 GiB for the OS and Ollama (if running local inference)

**Pros:**
- Per-project resource limits enforced by Docker (`--memory`, `--cpus`)
- Failure isolation: crashed stockbot agent does not affect research agents
- Independent update and restart of individual project agents
- Standard Docker Compose tooling — easy to operate

**Cons:**
- Each container needs 1 GiB minimum per SDK requirement — with 8 GiB total, this limits concurrent containers to 4-5
- Container startup latency: 5-15 seconds cold start vs. sub-second coroutine launch
- Image build and maintenance overhead for each agent type
- Requires careful volume mount planning to avoid agents writing to each other's project directories

**Best for:** When 3+ projects are consistently running in parallel and you need hard resource guarantees between them.

---

### Option C: Kubernetes (k3s) Single-Node

**Description:** Deploy k3s (lightweight Kubernetes) on the RPi 5. Each agent type becomes a Kubernetes Deployment. The orchestrator becomes a Kubernetes Job or CronJob that dispatches Tasks.

**Pros:**
- Industry-standard tooling for multi-agent orchestration
- Native resource quotas via ResourceQuota and LimitRange
- Rolling updates with zero downtime
- Health checks and automatic pod restart
- Scales naturally if additional nodes (e.g., the Jetson) are added to the cluster

**Cons:**
- k3s overhead on RPi 5: ~512 MB RAM just for control plane (etcd, kubelet, scheduler, API server) — this is 6% of an 8 GB machine and up to 12.5% on a 4 GB variant
- Significant learning curve investment: Helm charts, RBAC, PersistentVolumeClaims, Services, Ingress
- For 5-10 agents on a single machine, orchestration overhead exceeds the concurrency gains
- Container image build times on ARM64 are slower than x86 (QEMU cross-compilation adds 5-10x penalty for x86 base images)
- The Gas Town and Multiclaude patterns (multi-agent Claude Code coordination at scale) explicitly describe this as suitable only for "20-30 Claude Code instances working in parallel on the same codebase" — not the current 3-5 agent workload

**Best for:** If the project expands to a multi-node cluster (RPi 5 + Jetson + cloud node) with 20+ concurrent agents.

---

### Option D: Ray for Distributed Task Orchestration

**Description:** Replace or augment the Python asyncio coordinator with Ray, a distributed computing framework. Agent tasks become Ray remote functions; Ray handles scheduling, retries, and distributed execution.

**Pros:**
- Simple Python API: adding `@ray.remote` decorator to existing agent functions is the primary change
- Automatic retry and fault tolerance
- Can scale from single-machine (local mode) to multi-machine cluster transparently
- First-class support for parallel tool calls across hundreds of nodes
- Works with Docker and Kubernetes

**Cons:**
- Ray head node overhead: ~1.5-2 GiB RAM on startup — substantial on RPi 5
- Designed for ML training workloads (PyTorch, data pipelines) — applying it to LLM agent orchestration introduces a pattern mismatch
- Most Ray tutorials assume cloud-scale workloads; community support for RPi ARM64 is thin
- The asyncio queue-based pattern already implemented (ORCHESTRATOR_STATE.md + Python coordinator) achieves the same parallelism with far lower overhead for 5-10 agents
- RayAI (Ray's dedicated agent orchestration layer) is new as of 2025 and has limited production case studies

**Best for:** If this project evolves to include distributed ML training (fine-tuning, data pipeline processing) alongside agent orchestration.

---

### Option E: Anthropic Managed Agents (Cloud Offload)

**Description:** Move specific long-running or computation-heavy agent tasks to Anthropic's managed infrastructure. The local coordinator dispatches tasks to the Managed Agents API instead of running them in-process.

**Pros:**
- Zero local resource consumption for offloaded agents
- Built-in gVisor sandboxing, session persistence, error recovery
- Latency improvement: Anthropic reports ~60% p50 improvement in time-to-first-token from deferred container provisioning
- Good fit for tasks that don't require access to local files (pure research, summarization, drafting)

**Cons:**
- $0.08/session-hour runtime cost × long-running research sessions adds up — a 4-hour research session costs $0.32 in runtime alone plus token costs
- Network dependency: requires outbound HTTPS to api.anthropic.com for every agent call
- Cannot access local files, local databases, or the resistance-research/projects directory hierarchy without additional API surface
- Data sovereignty concern for resistance-research content — submissions through Anthropic's infrastructure
- The current workload is heavily file-I/O dependent (reading and writing Markdown files, checking WORKLOG.md, updating PROJECTS.md) — this does not fit the Managed Agents isolation model

**Best for:** Specific subtasks that are purely generative and do not require local file access: drafting distribution emails, summarizing external research, generating boilerplate.

---

## 3. Recommended Approach with Implementation Roadmap

### Phase 1 (Recommended — implement now, ~1 day effort)

**Goal:** Add code execution sandboxing without changing the orchestrator architecture.

**Step 1:** Add a `sandbox` service to the AgentCore `docker-compose.yml` (or a separate `docker-compose.research.yml` for the research workflow):

```yaml
sandbox:
  image: python:3.12-slim
  container_name: research-sandbox
  restart: unless-stopped
  networks:
    - agentcore-net
  ports:
    - "127.0.0.1:9000:9000"
  volumes:
    - ./sandbox-workspace:/workspace
  mem_limit: 1g
  cpus: "1.0"
  read_only: false
  tmpfs:
    - /tmp
  security_opt:
    - no-new-privileges:true
```

**Step 2:** Fix the three `0.0.0.0` bindings in the existing `docker-compose.yml` (open-webui, agentcore, wizard, nginx).

**Step 3:** Update the Python coordinator to route code execution calls through `docker exec research-sandbox python /workspace/<script>` rather than running scripts on the host.

**Step 4:** Add memory limits to the existing AgentCore stack services (currently none are set). Recommended limits for RPi 5 (8 GB):

| Service | mem_limit | cpus |
|---------|-----------|------|
| ollama | 4g | 3.0 |
| open-webui | 512m | 0.5 |
| agentcore | 512m | 1.0 |
| postgres | 256m | 0.5 |
| redis | 256m | 0.25 |
| chromadb | 512m | 0.5 |
| sandbox | 1g | 1.0 |

**Step 5:** Enable cgroup memory limits on the RPi 5 if not already set (required for Docker `--memory` flags to be enforced). Add to `/boot/firmware/cmdline.txt`:
```
cgroup_enable=memory swapaccount=1
```

---

### Phase 2 (Optional — implement if 3+ projects run concurrently for >2 hours/day)

**Goal:** Add project-level isolation via Docker Compose multi-service agent stack.

- Create `docker-compose.agents.yml` with one container per project category (research, stockbot, seedwarden/mfg)
- Share the existing postgres and redis services from AgentCore stack
- Use Docker networks to control which agents can reach which services
- Set `--memory 1g` and `--cpus 1.0` per agent container

**Do not proceed to Phase 2 unless:** You are hitting resource contention between projects in Phase 1, or you need hard isolation guarantees for concurrent execution.

---

### Phase 3 (Long-term — only if cluster expands to 3+ nodes)

**Goal:** Kubernetes (k3s) cluster spanning RPi 5 + Jetson + optional cloud node.

- Not warranted until node count exceeds 2
- Start with k3s rather than full Kubernetes — far lower overhead, same API surface
- Stockbot on Jetson already has its own Docker Compose stack; bridging it into a k3s cluster is the natural Phase 3 starting point

---

## 4. Cost-Benefit Analysis Per Use Case

### 4.1 Resistance-Research (parallel research agents)

**Current pattern:** Sequential or 2-agent parallel, writes to `projects/resistance-research/`  
**Isolation need:** Low — research agents only write Markdown files; no code execution risk  
**Containerization benefit:** Low  
**Recommendation:** No container needed. Keep as asyncio-based parallel agent calls.  
**Cost if containerized unnecessarily:** 1 GiB RAM per container × 2-3 agents = 2-3 GiB overhead during research sessions, reducing available memory for inference

### 4.2 Stockbot (backtesting, model training scripts)

**Current pattern:** Dedicated Jetson with separate Docker Compose stack; Python scripts for backtesting  
**Isolation need:** High — backtesting scripts can consume unbounded memory; model training can fill disk  
**Containerization benefit:** High  
**Recommendation:** Already containerized (Jetson stack). Verify mem_limit and cpus are set in docker-compose.jetson.yml. Add a dedicated backtesting sandbox container with strict resource limits.  
**Container startup cost:** Cold start 5-15s — acceptable for backtesting tasks that run for minutes to hours

### 4.3 Seedwarden / MFG-Farm (external API calls, file generation)

**Current pattern:** Agents write to `projects/seedwarden/` and `projects/mfg-farm/`; no code execution  
**Isolation need:** Low-medium — no risky code execution; external API calls are the main concern  
**Containerization benefit:** Low for file operations; medium for network isolation (blocking outbound to wrong endpoints)  
**Recommendation:** Phase 1 network isolation via Docker network policy if needed. No code execution sandbox required.

### 4.4 Civic-Tracker and Domain Research Scripts

**Current pattern:** `civic-tracker.py` runs on host; web scraping scripts run unsandboxed  
**Isolation need:** Medium — web scraping can hit unexpected content, install packages, consume disk  
**Containerization benefit:** Medium  
**Recommendation:** Route civic-tracker.py through the Phase 1 code execution sandbox. Ephemeral container (Pattern 1) is correct for one-off script runs.  
**Cost:** Minimal — ephemeral containers are destroyed after use; no persistent overhead

### 4.5 AgentCore Edge Product (existing Docker Compose stack)

**Current pattern:** Full Docker Compose stack already implemented  
**Isolation need:** Already addressed  
**Containerization benefit:** Already achieved  
**Remaining work:** Fix 0.0.0.0 bindings, add mem_limit/cpus to all services, test ARM64 images on RPi 5 (docker-compose.arm64.yml exists — verify Ollama and open-webui ARM64 tags are current)

---

## 5. RPi 5 — Specific Constraints and Mitigations

The RPi 5 has confirmed ARM64 (aarch64) architecture with Docker fully supported. Key constraints:

**Memory limits must be explicitly enabled** — Docker on Raspberry Pi requires cgroup memory support activated in the kernel command line. Without `cgroup_enable=memory swapaccount=1` in cmdline.txt, `--memory` flags are silently ignored. This is the most commonly missed RPi Docker configuration step.

**ARM64 native images only** — Using x86 images via QEMU emulation incurs a 5-10x performance penalty. Always verify that the image tag includes `linux/arm64` in its manifest. The existing docker-compose.arm64.yml in the project confirms awareness of this — verify that chromadb/chroma and ghcr.io/open-webui/open-webui have ARM64 variants published.

**Swap configuration** — Docker swap limits (`--memory-swap`) require swap to be configured on the host. For RPi 5 with SSD/NVMe, set swappiness to 10 to minimize swap use while retaining it as an overflow buffer. A 4 GB swap file on NVMe is appropriate backup for inference workloads.

**Total RAM budget for 8 GB RPi 5 running full AgentCore + research agents:**
- OS + system processes: ~1 GB
- AgentCore stack (as above with limits): ~6 GB headroom (Ollama dominates at 4 GB)
- Research sandbox container: 1 GB
- Leaves ~1 GB free — tight but workable if not running large models concurrently

**For 4 GB RPi 5:** The full AgentCore stack is not viable concurrently with research agents. Either run AgentCore or run research agents, not both. Use profiles (Docker Compose `--profile` flag) to activate only the needed services.

---

## 6. Security Notes

The Claude Agent SDK explicitly documents the credential isolation requirement: credentials should never reach the sandbox. Two patterns from the Anthropic managed-agents architecture apply directly:

1. **Git tokens and secrets:** inject during container initialization via environment variables, never baked into the image
2. **OAuth tokens:** route through a proxy (MCP server or local API) so the sandbox only sees the proxy URL, not the raw credential

The existing AgentCore docker-compose.yml correctly uses `${VAR:?must be set}` syntax for required secrets. This pattern should be replicated in any new sandbox containers.

The `wizard` container correctly avoids mounting `docker.sock` — noted in the compose file comment. Maintain this discipline for all agent containers: no container should have docker.sock access unless it is explicitly an orchestrator container with a documented justification.

---

## 7. What to Monitor After Implementation

- Per-container memory usage: `docker stats --no-stream`
- Container restart counts (a restarting container signals a resource limit being hit): `docker ps --format "{{.Names}} {{.Status}}"`
- RPi 5 swap usage: a nonzero swap rate while containers are running indicates memory limits are too tight
- Agent task queue depth (if Phase 2 Redis queue is implemented): high queue depth indicates agents cannot keep up with dispatch rate
- Token budget consumption per project per session (already tracked in ORCHESTRATOR_STATE.md — keep this)

---

## Sources

- [Claude Agent SDK — Hosting Guide](https://code.claude.com/docs/en/agent-sdk/hosting) — official Anthropic documentation on container requirements, deployment patterns, and resource allocation
- [Anthropic — Building Agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) — architecture reference for session/harness/sandbox decoupling
- [Anthropic — Managed Agents](https://www.anthropic.com/engineering/managed-agents) — gVisor isolation, billing model, network egress policy
- [Augment Code — Claude Agent SDK: What It Ships vs. What You Build](https://www.augmentcode.com/guides/anthropic-agent-sdk-what-ships-vs-what-you-build) — gap analysis: 2,200-4,500 engineer-hours to implement missing platform layers
- [Docker — Run Claude Code with Docker](https://www.docker.com/blog/run-claude-code-with-docker/) — Docker sandbox, MCP toolkit, and Model Runner deployment patterns
- [Shipyard — Multi-Agent Orchestration for Claude Code in 2026](https://shipyard.build/blog/claude-code-multi-agent/) — Gas Town, Agent Teams, Multiclaude patterns; resource consumption realities
- [Zylos Research — Claude Agent SDK and Managed Agents Architecture](https://zylos.ai/research/2026-04-20-claude-agent-sdk-managed-agents-architecture) — cost model ($0.08/session-hour), self-hosted vs. managed trade-offs
- [Docker Docs — Resource Constraints](https://docs.docker.com/engine/containers/resource_constraints/) — mem_limit, cpus, memory-swap enforcement
- [dalwar23.com — Fix "No memory limit support" for Docker on Raspberry Pi](https://dalwar23.com/how-to-fix-no-memory-limit-support-for-docker-in-raspberry-pi/) — cgroup_enable=memory kernel parameter requirement
- [Ray — Use Cases](https://docs.ray.io/en/latest/ray-overview/use-cases.html) — distributed agent orchestration; appropriate scale thresholds
- [OpenAI Agents SDK — Multi-Agent Orchestration](https://openai.github.io/openai-agents-python/multi_agent/) — asyncio.gather() vs. Docker overhead for lightweight parallel agents
- [DEV Community — 7 AI Agent Orchestration Patterns](https://dev.to/dohkoai/7-ai-agent-orchestration-patterns-for-scaling-concurrent-systems-with-production-code-1onc) — queue-based backpressure, asyncio coordinator patterns in production
