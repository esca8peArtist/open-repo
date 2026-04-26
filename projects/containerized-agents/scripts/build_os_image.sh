#!/usr/bin/env bash
# =============================================================================
# build_os_image.sh
# Builds the bootable OS image for the containerized-agents project.
#
# Uses mkosi (preferred) or debootstrap (fallback) to produce a bootable
# Ubuntu Server 24.04 LTS image with Docker CE, Python 3.12 + uv, and the
# AgentCore Docker Compose bundle pre-embedded.
#
# Required env vars:
#   IMAGE_VERSION  - Semver string, e.g. "1.0.0"
#   OUTPUT_DIR     - Destination directory for image artefacts (default: dist/os)
#
# Optional env vars:
#   PROFILE        - Agent profile name (default: "base")
#   BUILD_TOOL     - "mkosi" or "debootstrap" (auto-detected if not set)
#   BUNDLE_DIR     - Path to assembled bundle (default: dist/bundle)
#   WORK_DIR       - Scratch workspace (default: /tmp/agentcore-build)
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

ok()   { echo -e "${GREEN}  [OK]${RESET}  $*"; }
fail() { echo -e "${RED}  [FAIL]${RESET} $*" >&2; exit 1; }
info() { echo -e "${CYAN}  [INFO]${RESET} $*"; }
warn() { echo -e "${YELLOW}  [WARN]${RESET} $*"; }
step() { echo -e "\n${BOLD}${CYAN}$*${RESET}"; }

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

IMAGE_VERSION="${IMAGE_VERSION:-}"
OUTPUT_DIR="${OUTPUT_DIR:-${PROJECT_ROOT}/dist/os}"
PROFILE="${PROFILE:-base}"
BUNDLE_DIR="${BUNDLE_DIR:-${PROJECT_ROOT}/dist/bundle}"
WORK_DIR="${WORK_DIR:-/tmp/agentcore-build-$$}"
BUILD_TOOL="${BUILD_TOOL:-}"

UBUNTU_SUITE="noble"       # Ubuntu 24.04 LTS
UBUNTU_MIRROR="http://archive.ubuntu.com/ubuntu"
IMAGE_SIZE_GB=8            # Minimum image size in GB

# ---------------------------------------------------------------------------
# Step 0 — Banner
# ---------------------------------------------------------------------------
echo ""
echo -e "${BOLD}${CYAN}============================================================${RESET}"
echo -e "${BOLD}${CYAN}  Containerized Agents — OS Image Build${RESET}"
echo -e "${BOLD}${CYAN}============================================================${RESET}"
echo ""

# ---------------------------------------------------------------------------
# Step 1 — Validate prerequisites
# ---------------------------------------------------------------------------
step "[1/7] Validating prerequisites..."

# --- Required env vars ---
[[ -z "${IMAGE_VERSION}" ]] && fail "IMAGE_VERSION is not set. Export it before running this script."
[[ "${IMAGE_VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-.+)?$ ]] \
  || fail "IMAGE_VERSION '${IMAGE_VERSION}' is not a valid semver string (e.g. 1.0.0)."
ok "IMAGE_VERSION=${IMAGE_VERSION}"

[[ -n "${OUTPUT_DIR}" ]] || fail "OUTPUT_DIR must not be empty."
mkdir -p "${OUTPUT_DIR}"
ok "OUTPUT_DIR=${OUTPUT_DIR}"

# --- Detect build tool ---
if [[ -z "${BUILD_TOOL}" ]]; then
  if command -v mkosi &>/dev/null; then
    BUILD_TOOL="mkosi"
  elif command -v debootstrap &>/dev/null; then
    BUILD_TOOL="debootstrap"
  else
    fail "Neither 'mkosi' nor 'debootstrap' found. Install one to continue."
  fi
fi

case "${BUILD_TOOL}" in
  mkosi)
    command -v mkosi &>/dev/null   || fail "'mkosi' not found but BUILD_TOOL=mkosi was requested."
    command -v systemd-nspawn &>/dev/null || fail "'systemd-nspawn' not found (required by mkosi)."
    ok "Build tool: mkosi ($(mkosi --version 2>&1 | head -1))"
    ;;
  debootstrap)
    command -v debootstrap &>/dev/null || fail "'debootstrap' not found."
    command -v chroot &>/dev/null      || fail "'chroot' not found."
    command -v losetup &>/dev/null     || fail "'losetup' not found."
    command -v mkfs.ext4 &>/dev/null   || fail "'mkfs.ext4' not found (e2fsprogs)."
    ok "Build tool: debootstrap ($(debootstrap --version 2>&1 | head -1))"
    ;;
  *)
    fail "Unknown BUILD_TOOL='${BUILD_TOOL}'. Choose 'mkosi' or 'debootstrap'."
    ;;
esac

# --- Disk space (need at least 20 GB free in /tmp) ---
AVAIL_KB=$(df -k /tmp | awk 'NR==2{print $4}')
REQUIRED_KB=$(( (IMAGE_SIZE_GB + 12) * 1024 * 1024 ))   # image + overhead
if (( AVAIL_KB < REQUIRED_KB )); then
  fail "Insufficient disk space in /tmp. Need $(( REQUIRED_KB / 1024 / 1024 )) GB, have $(( AVAIL_KB / 1024 / 1024 )) GB."
fi
ok "Disk space: $(( AVAIL_KB / 1024 / 1024 )) GB free in /tmp (need $(( REQUIRED_KB / 1024 / 1024 )) GB)"

# --- Bundle directory (must exist for embedding) ---
if [[ ! -d "${BUNDLE_DIR}" ]]; then
  warn "Bundle directory '${BUNDLE_DIR}' not found — it will be created as an empty placeholder."
  mkdir -p "${BUNDLE_DIR}"
fi
ok "Bundle dir: ${BUNDLE_DIR}"

# --- systemd unit sources ---
SYSTEMD_SRC="${PROJECT_ROOT}/infra/systemd"
[[ -f "${SYSTEMD_SRC}/agentcore-wizard.service" ]] \
  || fail "Missing systemd unit: ${SYSTEMD_SRC}/agentcore-wizard.service"
[[ -f "${SYSTEMD_SRC}/agentcore.service" ]] \
  || fail "Missing systemd unit: ${SYSTEMD_SRC}/agentcore.service"
ok "Systemd units: found"

# --- Running as root (required for image manipulation) ---
if [[ "${EUID}" -ne 0 ]]; then
  fail "This script must be run as root (or via sudo) to mount loop devices and chroot."
fi
ok "Running as root"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
GIT_SHA=$(git -C "${PROJECT_ROOT}" rev-parse --short HEAD 2>/dev/null || echo "unknown")
BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
IMAGE_NAME="containerized-agents-${IMAGE_VERSION}.img"
IMAGE_PATH="${OUTPUT_DIR}/${IMAGE_NAME}"

cleanup() {
  info "Cleaning up temporary workspace..."
  if [[ -n "${LOOP_DEV:-}" ]] && losetup "${LOOP_DEV}" &>/dev/null; then
    umount "${WORK_DIR}/rootfs/proc"  2>/dev/null || true
    umount "${WORK_DIR}/rootfs/sys"   2>/dev/null || true
    umount "${WORK_DIR}/rootfs/dev"   2>/dev/null || true
    umount "${WORK_DIR}/rootfs"       2>/dev/null || true
    losetup -d "${LOOP_DEV}"          2>/dev/null || true
  fi
  rm -rf "${WORK_DIR}"
}
trap cleanup EXIT

mkdir -p "${WORK_DIR}"

# ---------------------------------------------------------------------------
# Step 2 — Prepare base OS
# ---------------------------------------------------------------------------
step "[2/7] Preparing base OS (Ubuntu Server 24.04 LTS — ${UBUNTU_SUITE})..."

RAW_IMAGE="${WORK_DIR}/raw.img"
ROOTFS="${WORK_DIR}/rootfs"
mkdir -p "${ROOTFS}"

if [[ "${BUILD_TOOL}" == "mkosi" ]]; then
  # ---- mkosi path --------------------------------------------------------
  MKOSI_DIR="${WORK_DIR}/mkosi"
  mkdir -p "${MKOSI_DIR}"

  # Write mkosi.conf
  cat > "${MKOSI_DIR}/mkosi.conf" <<EOF
[Distribution]
Distribution=ubuntu
Release=${UBUNTU_SUITE}
Mirror=${UBUNTU_MIRROR}

[Output]
Format=disk
Output=${RAW_IMAGE}
ImageId=containerized-agents
ImageVersion=${IMAGE_VERSION}
Bootable=yes

[Content]
Packages=
    apt-transport-https
    ca-certificates
    curl
    gnupg
    lsb-release
    python3.12
    python3.12-venv
    python3-pip
    jq
    avahi-daemon
    avahi-utils
    tpm2-tools
    ufw
    fail2ban
    openssh-server
    systemd
    systemd-sysv
    dbus
    iproute2
    net-tools

[Validation]
SecureBoot=no
EOF

  info "Running mkosi build (this may take several minutes)..."
  mkosi --directory="${MKOSI_DIR}" build
  ok "mkosi build complete"

else
  # ---- debootstrap path --------------------------------------------------
  info "Creating raw disk image (${IMAGE_SIZE_GB} GB)..."
  dd if=/dev/zero of="${RAW_IMAGE}" bs=1M count=$(( IMAGE_SIZE_GB * 1024 )) status=progress

  info "Partitioning image..."
  parted -s "${RAW_IMAGE}" mklabel gpt
  parted -s "${RAW_IMAGE}" mkpart primary ext4 1MiB 100%

  LOOP_DEV=$(losetup --find --partscan --show "${RAW_IMAGE}")
  ok "Loop device: ${LOOP_DEV}"

  PART_DEV="${LOOP_DEV}p1"
  mkfs.ext4 -L agentcore-root "${PART_DEV}"
  mount "${PART_DEV}" "${ROOTFS}"

  info "Running debootstrap (stage 1)..."
  debootstrap --arch=amd64 --variant=minbase \
    "${UBUNTU_SUITE}" "${ROOTFS}" "${UBUNTU_MIRROR}"
  ok "debootstrap stage 1 complete"

  # Bind mounts for chroot
  mount --bind /proc "${ROOTFS}/proc"
  mount --bind /sys  "${ROOTFS}/sys"
  mount --bind /dev  "${ROOTFS}/dev"

  info "Configuring apt sources inside chroot..."
  cat > "${ROOTFS}/etc/apt/sources.list" <<EOF
deb ${UBUNTU_MIRROR} ${UBUNTU_SUITE} main restricted universe multiverse
deb ${UBUNTU_MIRROR} ${UBUNTU_SUITE}-updates main restricted universe multiverse
deb ${UBUNTU_MIRROR} ${UBUNTU_SUITE}-security main restricted universe multiverse
EOF

  chroot "${ROOTFS}" apt-get update -q
  ok "Base OS prepared"
fi

# ---------------------------------------------------------------------------
# Step 3 — Install system dependencies
# ---------------------------------------------------------------------------
step "[3/7] Installing system dependencies..."

install_in_chroot() {
  chroot "${ROOTFS}" env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends "$@"
}

run_in_chroot() {
  chroot "${ROOTFS}" bash -c "$*"
}

if [[ "${BUILD_TOOL}" == "debootstrap" ]]; then
  info "Installing base packages..."
  install_in_chroot \
    curl ca-certificates gnupg lsb-release apt-transport-https \
    jq python3.12 python3.12-venv python3-pip \
    avahi-daemon avahi-utils \
    tpm2-tools \
    ufw fail2ban \
    openssh-server \
    systemd systemd-sysv dbus \
    iproute2 net-tools sudo

  ok "Base packages installed"

  # --- Docker CE ---
  info "Installing Docker CE..."
  run_in_chroot "install -m 0755 -d /etc/apt/keyrings"
  run_in_chroot "curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | gpg --dearmor -o /etc/apt/keyrings/docker.gpg"
  run_in_chroot "chmod a+r /etc/apt/keyrings/docker.gpg"
  run_in_chroot 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    > /etc/apt/sources.list.d/docker.list'
  chroot "${ROOTFS}" apt-get update -q
  install_in_chroot \
    docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ok "Docker CE installed"

  # --- uv (Python package manager) ---
  # Install a pinned uv release via the official GitHub releases page so we can
  # verify the binary's SHA256 checksum before executing it.
  UV_VERSION="0.6.6"
  UV_INSTALLER_URL="https://github.com/astral-sh/uv/releases/download/${UV_VERSION}/uv-installer.sh"
  # SHA256 of the installer script for uv ${UV_VERSION} (aarch64 + x86_64 wrapper).
  # Update this value whenever UV_VERSION is bumped:
  #   curl -LsSf "${UV_INSTALLER_URL}" | sha256sum
  UV_INSTALLER_SHA256="7edba24cca60da7e4e3b01b8df55b6a28fb16d1ee8b4879fc23e2fda7ea3ba98"

  info "Downloading uv ${UV_VERSION} installer..."
  run_in_chroot "curl -LsSf '${UV_INSTALLER_URL}' -o /tmp/uv-installer.sh"

  info "Verifying uv installer SHA256 checksum..."
  run_in_chroot "echo '${UV_INSTALLER_SHA256}  /tmp/uv-installer.sh' | sha256sum --check --status" \
    || fail "uv installer checksum mismatch — aborting to prevent supply-chain compromise. \
Recompute the expected hash with: curl -LsSf '${UV_INSTALLER_URL}' | sha256sum"

  info "Executing uv installer..."
  run_in_chroot "sh /tmp/uv-installer.sh && rm -f /tmp/uv-installer.sh"
  # Make uv available system-wide
  run_in_chroot "ln -sf /root/.cargo/bin/uv /usr/local/bin/uv || \
    ln -sf /root/.local/bin/uv /usr/local/bin/uv || true"
  ok "uv ${UV_VERSION} installed and checksum verified"
fi

# ---------------------------------------------------------------------------
# Step 4 — Embed Docker Compose bundle
# ---------------------------------------------------------------------------
step "[4/7] Embedding Docker Compose bundle..."

AGENTCORE_OPT="${ROOTFS}/opt/agentcore"
mkdir -p "${AGENTCORE_OPT}"

if [[ -d "${BUNDLE_DIR}" && "$(ls -A "${BUNDLE_DIR}" 2>/dev/null)" ]]; then
  cp -r "${BUNDLE_DIR}/." "${AGENTCORE_OPT}/"
  ok "Bundle copied to /opt/agentcore"
else
  warn "Bundle directory is empty — embedding skeleton structure only"
  mkdir -p "${AGENTCORE_OPT}"/{images,config}
  echo "# Bundle not yet populated — run build_compose_bundle.sh first" \
    > "${AGENTCORE_OPT}/README.txt"
fi

chmod -R 750 "${AGENTCORE_OPT}"

# ---------------------------------------------------------------------------
# Step 5 — Install systemd units
# ---------------------------------------------------------------------------
step "[5/7] Installing systemd units..."

SYSTEMD_DEST="${ROOTFS}/etc/systemd/system"
mkdir -p "${SYSTEMD_DEST}"

cp "${SYSTEMD_SRC}/agentcore-wizard.service" "${SYSTEMD_DEST}/"
cp "${SYSTEMD_SRC}/agentcore.service"        "${SYSTEMD_DEST}/"
chmod 644 "${SYSTEMD_DEST}/agentcore-wizard.service" \
          "${SYSTEMD_DEST}/agentcore.service"

# Enable agentcore-wizard on first boot; agentcore will be enabled by wizard
MULTI_USER_WANTS="${ROOTFS}/etc/systemd/system/multi-user.target.wants"
mkdir -p "${MULTI_USER_WANTS}"
ln -sf "/etc/systemd/system/agentcore-wizard.service" \
  "${MULTI_USER_WANTS}/agentcore-wizard.service"

ok "agentcore-wizard.service enabled (first-boot)"
ok "agentcore.service installed (enabled by wizard after first boot)"

# ---------------------------------------------------------------------------
# Step 6 — Security hardening
# ---------------------------------------------------------------------------
step "[6/7] Applying security hardening..."

if [[ "${BUILD_TOOL}" == "debootstrap" ]]; then
  # --- Disable root login via SSH ---
  SSHD_CONF="${ROOTFS}/etc/ssh/sshd_config"
  if [[ -f "${SSHD_CONF}" ]]; then
    sed -i 's/^#*PermitRootLogin.*/PermitRootLogin no/'          "${SSHD_CONF}"
    sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' "${SSHD_CONF}"
    sed -i 's/^#*PubkeyAuthentication.*/PubkeyAuthentication yes/' "${SSHD_CONF}"
  fi
  ok "SSH: root login disabled, password auth disabled"

  # --- UFW baseline rules ---
  # Pre-seed UFW config; actual `ufw enable` runs inside wizard on first boot
  cat > "${ROOTFS}/etc/ufw/applications.d/agentcore" <<'EOF'
[AgentCore]
title=AgentCore API
description=Containerized Agents orchestration API
ports=8080/tcp

[AgentCore-Wizard]
title=AgentCore Setup Wizard
description=First-boot setup wizard
ports=8888/tcp

[AgentCore-WebUI]
title=Open WebUI
description=Local AI chat interface
ports=3000/tcp
EOF

  # Pre-configure ufw defaults
  cat > "${ROOTFS}/etc/ufw/ufw.conf" <<'EOF'
ENABLED=yes
LOGLEVEL=low
EOF

  # Default rules (written directly to avoid running ufw in chroot without kernel)
  cat > "${ROOTFS}/etc/ufw/user.rules" <<'EOF'
*filter
:ufw-user-input - [0:0]
:ufw-user-output - [0:0]
:ufw-user-forward - [0:0]
:ufw-before-logging-input - [0:0]
:ufw-before-logging-output - [0:0]
:ufw-before-logging-forward - [0:0]
:ufw-user-limit - [0:0]
:ufw-user-limit-accept - [0:0]
### RULES ###
### tuple ### allow tcp 22 0.0.0.0/0 any 0.0.0.0/0 in
-A ufw-user-input -p tcp --dport 22 -j ACCEPT
### tuple ### allow tcp 3000 0.0.0.0/0 any 0.0.0.0/0 in
-A ufw-user-input -p tcp --dport 3000 -j ACCEPT
### tuple ### allow tcp 8080 0.0.0.0/0 any 0.0.0.0/0 in
-A ufw-user-input -p tcp --dport 8080 -j ACCEPT
### tuple ### allow tcp 8888 0.0.0.0/0 any 0.0.0.0/0 in
-A ufw-user-input -p tcp --dport 8888 -j ACCEPT
### END RULES ###
-A ufw-user-limit -m limit --limit 3/minute -j LOG --log-prefix "[UFW LIMIT BLOCK] "
-A ufw-user-limit -j REJECT
-A ufw-user-limit-accept -j ACCEPT
COMMIT
EOF
  ok "UFW: baseline rules written (enabled at first boot)"

  # --- fail2ban basics ---
  cat > "${ROOTFS}/etc/fail2ban/jail.d/agentcore.conf" <<'EOF'
[sshd]
enabled  = true
port     = ssh
filter   = sshd
maxretry = 5
bantime  = 3600
findtime = 600
EOF
  ok "fail2ban: SSH jail configured"

  # --- Disable unused services ---
  for svc in snapd snap.amazon-ssm-agent motd-news; do
    MASK_PATH="${ROOTFS}/etc/systemd/system/${svc}.service"
    ln -sf /dev/null "${MASK_PATH}" 2>/dev/null || true
  done
  ok "Masked unused services"

  # --- agentcore system user ---
  run_in_chroot "id -u agentcore &>/dev/null || useradd --system --no-create-home \
    --shell /usr/sbin/nologin --groups docker agentcore"
  ok "agentcore system user created"
fi

# ---------------------------------------------------------------------------
# Step 7 — Write output artefacts
# ---------------------------------------------------------------------------
step "[7/7] Writing output artefacts..."

mkdir -p "${OUTPUT_DIR}"

if [[ "${BUILD_TOOL}" == "debootstrap" ]]; then
  # Unmount before copying
  umount "${ROOTFS}/proc" "${ROOTFS}/sys" "${ROOTFS}/dev" || true
  umount "${ROOTFS}"
  losetup -d "${LOOP_DEV}"
  unset LOOP_DEV
fi

# Copy / move final image
if [[ "${RAW_IMAGE}" != "${IMAGE_PATH}" ]]; then
  info "Writing image to ${IMAGE_PATH} ..."
  cp "${RAW_IMAGE}" "${IMAGE_PATH}"
fi
ok "Image: ${IMAGE_PATH}"

# SHA256 checksum
info "Computing SHA256 checksum..."
sha256sum "${IMAGE_PATH}" > "${IMAGE_PATH}.sha256"
ok "Checksum: ${IMAGE_PATH}.sha256"

# Build manifest JSON
MANIFEST_PATH="${OUTPUT_DIR}/build-manifest.json"
cat > "${MANIFEST_PATH}" <<EOF
{
  "schema_version": "1",
  "product": "containerized-agents",
  "version": "${IMAGE_VERSION}",
  "profile": "${PROFILE}",
  "git_sha": "${GIT_SHA}",
  "build_date": "${BUILD_DATE}",
  "base_os": "Ubuntu Server 24.04 LTS (${UBUNTU_SUITE})",
  "build_tool": "${BUILD_TOOL}",
  "image_file": "${IMAGE_NAME}",
  "image_sha256": "$(awk '{print $1}' "${IMAGE_PATH}.sha256")",
  "embedded_bundle": "$(ls "${BUNDLE_DIR}/" 2>/dev/null | head -1 && echo yes || echo no)"
}
EOF
ok "Manifest: ${MANIFEST_PATH}"

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo -e "${BOLD}${GREEN}============================================================${RESET}"
echo -e "${BOLD}${GREEN}  OS Image Build Complete${RESET}"
echo -e "${BOLD}${GREEN}============================================================${RESET}"
echo ""
echo -e "  Image    : ${IMAGE_PATH}"
echo -e "  Checksum : ${IMAGE_PATH}.sha256"
echo -e "  Manifest : ${MANIFEST_PATH}"
echo -e "  Version  : ${IMAGE_VERSION}  (git ${GIT_SHA})"
echo -e "  Profile  : ${PROFILE}"
echo ""
