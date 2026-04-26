# Jetson Deployment Guide

Deploying the Containerized Agents stack on NVIDIA Jetson Orin hardware.

---

## Hardware Requirements

| SKU | RAM | Profile Tier | Open WebUI | ChromaDB | Recommended Model |
|-----|-----|-------------|------------|----------|-------------------|
| Jetson Orin Nano 8GB | 8 GB unified | Personal (Tier 1) | Opt-in only (`--profile full`); not recommended | Opt-in only; not recommended | phi3:mini (2.3 GB) |
| Jetson Orin NX 16GB | 16 GB unified | Tier 2 | Supported | Supported | mistral:7b-instruct (4.1 GB) |
| Jetson AGX Orin 32GB | 32 GB unified | Tier 3 | Supported | Supported | llama3:8b or mixtral:8x7b-instruct-q4 |

Notes:
- All Jetson Orin SKUs use unified CPU/GPU memory. Ollama + the OS kernel reserve ~2 GB, so usable capacity for models is roughly RAM minus 2 GB.
- Storage: 64 GB+ NVMe SSD strongly recommended. The full stack with a 7B model requires ~20 GB of disk.
- The AGX Orin 64GB variant follows the same Tier 3 profile as the 32GB; raise memory limits in `docker-compose.arm64.yml` accordingly.

---

## Prerequisites

### 1. JetPack 6.x

Flash your Jetson with JetPack 6.x using NVIDIA SDK Manager or `nvsdkmanager`.

```
SDK Manager: https://developer.nvidia.com/nvidia-sdk-manager
```

Verify after boot:

```bash
cat /etc/nv_tegra_release
# Expected: R36.x.x or later (JetPack 6)
```

### 2. NVIDIA Container Runtime

The `nvidia-container-runtime` package is required so Docker can pass the Jetson GPU/memory to containers.

```bash
sudo apt update
sudo apt install -y nvidia-container-runtime

# Register it with Docker
sudo tee /etc/docker/daemon.json > /dev/null <<'EOF'
{
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia"
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
```

Verify:

```bash
docker run --rm --runtime=nvidia ubuntu nvidia-smi
```

### 3. Docker CE

Install Docker CE (not Docker Desktop — it is not available for ARM64 Linux):

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
# Log out and back in, then verify:
docker info
```

### 4. Docker Buildx (for building images locally on Jetson)

Docker CE >= 23 includes buildx. Verify:

```bash
docker buildx version
```

### 5. Storage

Mount a 64 GB+ NVMe drive at `/var/lib/docker` or a subdirectory for Docker volumes. Ollama model data alone can reach 10–30 GB depending on the model.

```bash
sudo systemctl stop docker
sudo rsync -aP /var/lib/docker /mnt/nvme/docker
sudo rm -rf /var/lib/docker
sudo ln -s /mnt/nvme/docker /var/lib/docker
sudo systemctl start docker
```

---

## Step-by-Step Deployment

### Step 1: Clone the repository

```bash
git clone https://github.com/your-org/containerized-agents.git
cd containerized-agents
```

### Step 2: Configure environment

```bash
cp .env.template .env
# Edit .env — set POSTGRES_PASSWORD, AGENTCORE_SECRET, WEBUI_SECRET_KEY
# and any other required variables
nano .env
```

### Step 3: (Optional) Build ARM64 images locally

If you need to build custom images on the Jetson rather than pulling pre-built ones:

```bash
export BUNDLE_VERSION=1.0.0
export PROFILE=personal
export TARGET_ARCH=arm64
bash scripts/build_compose_bundle.sh
```

Images are tagged `agentcore:1.0.0-arm64` and `wizard:1.0.0-arm64`.

### Step 4: Start core services

```bash
# Core services only (recommended for Orin Nano 8GB)
docker compose -f docker-compose.yml -f docker-compose.arm64.yml up -d

# Check service health
docker compose ps
docker compose logs -f agentcore
```

### Step 5: (Orin NX / AGX only) Start full stack

```bash
# Includes open-webui and chromadb
docker compose -f docker-compose.yml -f docker-compose.arm64.yml \
  --profile full up -d
```

### Step 6: Run the setup wizard

Open your browser to `http://<jetson-ip>:8888` (or `http://agent.local:8888` if mDNS is configured) and complete the first-boot wizard.

The wizard will:
1. Detect hardware and select a default model for your SKU
2. Pull the recommended Ollama model
3. Write the hardware fingerprint and license configuration
4. Signal AgentCore to start serving requests

### Step 7: Verify deployment

```bash
# All services healthy
docker compose ps

# AgentCore API responding
curl http://localhost:8080/health

# Ollama model loaded
curl http://localhost:11434/api/tags
```

---

## Recommended Models per SKU

| SKU | Model | Pull command | VRAM (approx) |
|-----|-------|-------------|---------------|
| Orin Nano 8GB | phi3:mini | `ollama pull phi3:mini` | 2.3 GB |
| Orin NX 16GB | mistral:7b-instruct | `ollama pull mistral:7b-instruct` | 4.1 GB |
| AGX Orin 32GB | llama3:8b | `ollama pull llama3:8b` | 4.7 GB |
| AGX Orin 32GB (alt) | mixtral:8x7b-instruct-q4_K_M | `ollama pull mixtral:8x7b-instruct-q4_K_M` | 26 GB |

Pull a model manually at any time:

```bash
docker exec -it agentcore-ollama ollama pull phi3:mini
```

---

## Memory Tuning

### Orin Nano 8GB — conservative limits (default in docker-compose.arm64.yml)

| Service | Limit |
|---------|-------|
| ollama | 6 GB |
| agentcore | 1 GB |
| postgres | 256 MB |
| redis | 128 MB |

Total reserved: ~7.4 GB. The kernel and OS require ~0.6 GB.

### Orin NX 16GB — suggested limits

Edit `docker-compose.arm64.yml` (or create a local override `docker-compose.local.yml`):

```yaml
services:
  ollama:
    deploy:
      resources:
        limits:
          memory: 12g
  agentcore:
    deploy:
      resources:
        limits:
          memory: 2g
  open-webui:
    deploy:
      resources:
        limits:
          memory: 1g
  chromadb:
    deploy:
      resources:
        limits:
          memory: 512m
```

### Redis memory cap

The base compose file sets `REDIS_MAXMEMORY=512mb`. On Nano, override in `.env`:

```
REDIS_MAXMEMORY=128mb
```

---

## Known Limitations

### No TPM on Orin Nano

The Jetson Orin Nano does not expose a discrete TPM 2.0 chip. The setup wizard detects this and falls back to a software-derived hardware fingerprint (based on board serial number + MAC address). License enforcement operates in fallback mode — all features remain available but the fingerprint may change if the eMMC is re-flashed.

Jetson Orin NX and AGX Orin do expose a security enclave that the wizard uses for hardware binding.

### Open WebUI not recommended on Orin Nano 8GB

Open WebUI requires approximately 800 MB–1 GB of RAM at idle. Combined with Ollama running phi3:mini (~2.3 GB), postgres, redis, and AgentCore, total memory consumption reaches ~5 GB, leaving only ~3 GB for the Ollama inference context window. This significantly limits maximum context length and concurrent requests.

For Orin Nano deployments, access AgentCore directly via the API or use a lightweight web client that calls the AgentCore REST API.

To enable Open WebUI anyway (accept the tradeoff):

```bash
docker compose -f docker-compose.yml -f docker-compose.arm64.yml \
  --profile full up -d open-webui
```

### No GPU passthrough via Docker `--gpus all` syntax on Jetson

Jetson does not use discrete PCIe GPUs. The `nvidia-container-runtime` default runtime (set in `/etc/docker/daemon.json`) automatically enables Jetson GPU/NVMM access without the `--gpus` flag. The `runtime: nvidia` key in `docker-compose.arm64.yml` achieves the same effect for specific services.

### ChromaDB ARM64 image

`chromadb/chroma:latest` publishes a multi-arch manifest that includes `linux/arm64`. If a specific version tag does not have an ARM64 variant, pin to `:latest` or a version confirmed to include ARM64 in the manifest.

### avahi / mDNS for `agent.local`

On Jetson Ubuntu, install avahi for `http://agent.local` resolution:

```bash
sudo apt install -y avahi-daemon avahi-utils
sudo systemctl enable --now avahi-daemon
```
