#!/usr/bin/env bash
# =============================================================================
# build_compose_bundle.sh
# Builds the Docker Compose bundle for the containerized-agents project.
#
# Builds Docker images, exports them for offline use, assembles the
# distributable bundle directory, and runs a smoke-test validation.
#
# Required env vars:
#   BUNDLE_VERSION - Semver string, e.g. "1.0.0"
#   PROFILE        - Agent profile name (e.g. "personal", "customer-support")
#
# Optional env vars:
#   OUTPUT_DIR     - Destination for bundle artefacts (default: dist/bundle)
#   IMAGES_DIR     - Destination for exported .tar images (default: dist/images)
#   DOCKER_CONTEXT - Docker build context (default: project root)
#   PUSH_REGISTRY  - If set, also push images to this registry
#   SKIP_EXPORT    - If "1", skip image tar export (faster for dev iteration)
#   TARGET_ARCH    - Target CPU architecture for buildx (default: amd64)
#                    Set to "arm64" to produce Jetson-compatible images.
#                    Images built with TARGET_ARCH=arm64 receive an "-arm64"
#                    tag suffix (e.g. agentcore:1.0.0-arm64).
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

BUNDLE_VERSION="${BUNDLE_VERSION:-}"
PROFILE="${PROFILE:-}"
OUTPUT_DIR="${OUTPUT_DIR:-${PROJECT_ROOT}/dist/bundle}"
IMAGES_DIR="${IMAGES_DIR:-${PROJECT_ROOT}/dist/images}"
DOCKER_CONTEXT="${DOCKER_CONTEXT:-${PROJECT_ROOT}}"
PUSH_REGISTRY="${PUSH_REGISTRY:-}"
SKIP_EXPORT="${SKIP_EXPORT:-0}"
TARGET_ARCH="${TARGET_ARCH:-amd64}"

# ---------------------------------------------------------------------------
# Step 0 — Banner
# ---------------------------------------------------------------------------
echo ""
echo -e "${BOLD}${CYAN}============================================================${RESET}"
echo -e "${BOLD}${CYAN}  Containerized Agents — Docker Compose Bundle Build${RESET}"
echo -e "${BOLD}${CYAN}============================================================${RESET}"
echo ""

# ---------------------------------------------------------------------------
# Step 1 — Validate prerequisites
# ---------------------------------------------------------------------------
step "[1/6] Validating prerequisites..."

# --- Docker ---
if ! command -v docker &>/dev/null; then
  fail "'docker' command not found. Install Docker CE first."
fi

if ! docker info &>/dev/null; then
  fail "Docker daemon is not running. Start it with: sudo systemctl start docker"
fi
ok "Docker: $(docker --version)"

# --- Docker Compose plugin ---
if ! docker compose version &>/dev/null; then
  fail "'docker compose' plugin not found. Install docker-compose-plugin."
fi
ok "Docker Compose: $(docker compose version --short)"

# --- Docker Buildx ---
if ! docker buildx version &>/dev/null; then
  fail "'docker buildx' not found. Install docker-buildx-plugin or upgrade Docker CE >= 23."
fi
ok "Docker Buildx: $(docker buildx version)"

# --- TARGET_ARCH validation ---
VALID_ARCHES="amd64 arm64"
# shellcheck disable=SC2076
[[ " ${VALID_ARCHES} " =~ " ${TARGET_ARCH} " ]] \
  || warn "TARGET_ARCH='${TARGET_ARCH}' is not in the standard set (${VALID_ARCHES}). Proceeding anyway."
ok "TARGET_ARCH=${TARGET_ARCH}"

# --- Required env vars ---
[[ -z "${BUNDLE_VERSION}" ]] && \
  fail "BUNDLE_VERSION is not set. Export it before running this script."
[[ "${BUNDLE_VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-.+)?$ ]] \
  || fail "BUNDLE_VERSION '${BUNDLE_VERSION}' is not valid semver (e.g. 1.0.0)."
ok "BUNDLE_VERSION=${BUNDLE_VERSION}"

[[ -z "${PROFILE}" ]] && \
  fail "PROFILE is not set. Export it before running this script (e.g. personal, customer-support)."
VALID_PROFILES="personal customer-support sales developer bi enterprise base"
# shellcheck disable=SC2076
[[ " ${VALID_PROFILES} " =~ " ${PROFILE} " ]] \
  || warn "PROFILE='${PROFILE}' is not in the standard set (${VALID_PROFILES}). Proceeding anyway."
ok "PROFILE=${PROFILE}"

# --- Dockerfile sources ---
DOCKERFILE_AGENTCORE="${PROJECT_ROOT}/docker/Dockerfile.agentcore"
DOCKERFILE_WIZARD="${PROJECT_ROOT}/docker/Dockerfile.wizard"
[[ -f "${DOCKERFILE_AGENTCORE}" ]] \
  || fail "Missing Dockerfile: ${DOCKERFILE_AGENTCORE}"
[[ -f "${DOCKERFILE_WIZARD}" ]] \
  || fail "Missing Dockerfile: ${DOCKERFILE_WIZARD}"
ok "Dockerfiles: found"

# --- docker-compose.yml ---
COMPOSE_FILE="${PROJECT_ROOT}/docker-compose.yml"
[[ -f "${COMPOSE_FILE}" ]] \
  || fail "Missing docker-compose.yml at project root: ${COMPOSE_FILE}"
ok "docker-compose.yml: found"

# --- .env.template ---
ENV_TEMPLATE="${PROJECT_ROOT}/.env.template"
[[ -f "${ENV_TEMPLATE}" ]] \
  || fail "Missing .env.template at project root: ${ENV_TEMPLATE}"
ok ".env.template: found"

# --- Output dirs ---
mkdir -p "${OUTPUT_DIR}" "${IMAGES_DIR}"
ok "Output dirs: ${OUTPUT_DIR}, ${IMAGES_DIR}"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
GIT_SHA=$(git -C "${PROJECT_ROOT}" rev-parse --short HEAD 2>/dev/null || echo "unknown")
GIT_SHA_LONG=$(git -C "${PROJECT_ROOT}" rev-parse HEAD 2>/dev/null || echo "unknown")
BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# For arm64 builds, append an "-arm64" suffix to all image tags so that
# amd64 and arm64 artefacts can coexist in the same local Docker daemon.
if [[ "${TARGET_ARCH}" == "amd64" ]]; then
  ARCH_TAG_SUFFIX=""
else
  ARCH_TAG_SUFFIX="-${TARGET_ARCH}"
fi

IMAGE_AGENTCORE="agentcore:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
IMAGE_WIZARD="wizard:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
IMAGE_AGENTCORE_SHA=""
IMAGE_WIZARD_SHA=""

# ---------------------------------------------------------------------------
# Step 2 — Resolve service definitions
# ---------------------------------------------------------------------------
step "[2/6] Resolving service definitions..."

info "Validating docker-compose.yml syntax..."
docker compose -f "${COMPOSE_FILE}" config --quiet \
  || fail "docker-compose.yml is invalid — fix syntax errors first."
ok "docker-compose.yml syntax valid"

SERVICES=$(docker compose -f "${COMPOSE_FILE}" config --services 2>/dev/null)
info "Services defined: $(echo "${SERVICES}" | tr '\n' ' ')"

# ---------------------------------------------------------------------------
# Step 3 — Build service images
# ---------------------------------------------------------------------------
step "[3/6] Building service images..."

BUILD_ARGS=(
  "--build-arg" "BUNDLE_VERSION=${BUNDLE_VERSION}"
  "--build-arg" "PROFILE=${PROFILE}"
  "--build-arg" "GIT_SHA=${GIT_SHA}"
  "--build-arg" "BUILD_DATE=${BUILD_DATE}"
)

# Build agentcore
info "Building ${IMAGE_AGENTCORE} (platform: linux/${TARGET_ARCH}) ..."
docker buildx build \
  --platform "linux/${TARGET_ARCH}" \
  "${BUILD_ARGS[@]}" \
  -f "${DOCKERFILE_AGENTCORE}" \
  -t "${IMAGE_AGENTCORE}" \
  --load \
  "${DOCKER_CONTEXT}"
ok "Built: ${IMAGE_AGENTCORE}"

# Build wizard
info "Building ${IMAGE_WIZARD} (platform: linux/${TARGET_ARCH}) ..."
docker buildx build \
  --platform "linux/${TARGET_ARCH}" \
  "${BUILD_ARGS[@]}" \
  -f "${DOCKERFILE_WIZARD}" \
  -t "${IMAGE_WIZARD}" \
  --load \
  "${DOCKER_CONTEXT}"
ok "Built: ${IMAGE_WIZARD}"

# Also tag with git SHA for traceability
docker tag "${IMAGE_AGENTCORE}" "agentcore:${GIT_SHA}${ARCH_TAG_SUFFIX}"
docker tag "${IMAGE_WIZARD}"    "wizard:${GIT_SHA}${ARCH_TAG_SUFFIX}"
ok "Tagged images with git SHA: ${GIT_SHA}${ARCH_TAG_SUFFIX}"

# Capture image digests
IMAGE_AGENTCORE_SHA=$(docker inspect --format='{{index .RepoDigests 0}}' "${IMAGE_AGENTCORE}" 2>/dev/null \
  || docker inspect --format='{{.Id}}' "${IMAGE_AGENTCORE}")
IMAGE_WIZARD_SHA=$(docker inspect --format='{{index .RepoDigests 0}}' "${IMAGE_WIZARD}" 2>/dev/null \
  || docker inspect --format='{{.Id}}' "${IMAGE_WIZARD}")
ok "Image digests captured"

# Optional: push to registry
if [[ -n "${PUSH_REGISTRY}" ]]; then
  info "Pushing images to ${PUSH_REGISTRY} ..."
  docker tag "${IMAGE_AGENTCORE}" "${PUSH_REGISTRY}/agentcore:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
  docker tag "${IMAGE_WIZARD}"    "${PUSH_REGISTRY}/wizard:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
  docker push "${PUSH_REGISTRY}/agentcore:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
  docker push "${PUSH_REGISTRY}/wizard:${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}"
  ok "Images pushed to ${PUSH_REGISTRY}"
fi

# ---------------------------------------------------------------------------
# Step 4 — Export images for offline use
# ---------------------------------------------------------------------------
step "[4/6] Tagging and exporting images..."

if [[ "${SKIP_EXPORT}" == "1" ]]; then
  warn "SKIP_EXPORT=1 — skipping .tar export"
else
  EXPORT_AGENTCORE="${IMAGES_DIR}/agentcore-${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}.tar"
  EXPORT_WIZARD="${IMAGES_DIR}/wizard-${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}.tar"

  info "Exporting ${IMAGE_AGENTCORE} → ${EXPORT_AGENTCORE} ..."
  docker save -o "${EXPORT_AGENTCORE}" "${IMAGE_AGENTCORE}"
  ok "Exported: ${EXPORT_AGENTCORE} ($(du -sh "${EXPORT_AGENTCORE}" | cut -f1))"

  info "Exporting ${IMAGE_WIZARD} → ${EXPORT_WIZARD} ..."
  docker save -o "${EXPORT_WIZARD}" "${IMAGE_WIZARD}"
  ok "Exported: ${EXPORT_WIZARD} ($(du -sh "${EXPORT_WIZARD}" | cut -f1))"

  # Checksums for exported tars
  sha256sum "${EXPORT_AGENTCORE}" > "${EXPORT_AGENTCORE}.sha256"
  sha256sum "${EXPORT_WIZARD}"    > "${EXPORT_WIZARD}.sha256"
  ok "Checksums written"
fi

# ---------------------------------------------------------------------------
# Step 5 — Assemble bundle
# ---------------------------------------------------------------------------
step "[5/6] Assembling bundle..."

# Clean previous bundle
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

# docker-compose.yml
cp "${COMPOSE_FILE}" "${OUTPUT_DIR}/docker-compose.yml"
ok "Copied docker-compose.yml"

# .env.template
cp "${ENV_TEMPLATE}" "${OUTPUT_DIR}/.env.template"
ok "Copied .env.template"

# setup.sh — first-run helper script
cat > "${OUTPUT_DIR}/setup.sh" <<'SETUP_EOF'
#!/usr/bin/env bash
# =============================================================================
# setup.sh — AgentCore first-run setup helper
# Run this script once to configure your environment before starting services.
# =============================================================================
set -euo pipefail

CYAN='\033[0;36m'; GREEN='\033[0;32m'; RED='\033[0;31m'; RESET='\033[0m'
ok()   { echo -e "${GREEN}  [OK]${RESET}  $*"; }
fail() { echo -e "${RED}  [FAIL]${RESET} $*" >&2; exit 1; }
info() { echo -e "${CYAN}  [INFO]${RESET} $*"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo -e "${CYAN}  AgentCore — First-Run Setup${RESET}"
echo ""

# Check .env exists
if [[ ! -f "${SCRIPT_DIR}/.env" ]]; then
  info "Creating .env from template..."
  cp "${SCRIPT_DIR}/.env.template" "${SCRIPT_DIR}/.env"
  ok ".env created — edit it to set your credentials before proceeding."
  echo ""
  echo "  Next steps:"
  echo "  1. Edit .env to set required variables"
  echo "  2. Run: docker compose up -d"
  echo "  3. Open: http://localhost:8888  (setup wizard)"
  exit 0
fi
ok ".env already exists"

# Load images if offline
IMAGES_DIR="${SCRIPT_DIR}/images"
if [[ -d "${IMAGES_DIR}" ]]; then
  for TAR in "${IMAGES_DIR}"/*.tar; do
    [[ -f "${TAR}" ]] || continue
    info "Loading offline image: $(basename "${TAR}")"
    docker load -i "${TAR}"
  done
  ok "Offline images loaded"
fi

# Validate compose
info "Validating docker-compose.yml..."
docker compose -f "${SCRIPT_DIR}/docker-compose.yml" config --quiet
ok "docker-compose.yml valid"

echo ""
echo -e "${GREEN}  Setup complete.${RESET}"
echo "  Start services: docker compose up -d"
echo "  Setup wizard:   http://localhost:8888"
echo ""
SETUP_EOF
chmod +x "${OUTPUT_DIR}/setup.sh"
ok "Created setup.sh"

# Copy exported images into bundle (if they were exported)
if [[ "${SKIP_EXPORT}" != "1" ]]; then
  cp -r "${IMAGES_DIR}" "${OUTPUT_DIR}/images"
  ok "Images directory included in bundle"
fi

# Write manifest.json
MANIFEST_PATH="${OUTPUT_DIR}/manifest.json"
AGENTCORE_SHA_JSON=$(echo "${IMAGE_AGENTCORE_SHA}" | sed 's/"/\\"/g')
WIZARD_SHA_JSON=$(echo "${IMAGE_WIZARD_SHA}" | sed 's/"/\\"/g')

cat > "${MANIFEST_PATH}" <<EOF
{
  "schema_version": "1",
  "product": "containerized-agents",
  "bundle_version": "${BUNDLE_VERSION}",
  "profile": "${PROFILE}",
  "git_sha": "${GIT_SHA}",
  "git_sha_long": "${GIT_SHA_LONG}",
  "build_date": "${BUILD_DATE}",
  "images": {
    "agentcore": {
      "tag": "${IMAGE_AGENTCORE}",
      "digest": "${AGENTCORE_SHA_JSON}",
      "tar": "images/agentcore-${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}.tar"
    },
    "wizard": {
      "tag": "${IMAGE_WIZARD}",
      "digest": "${WIZARD_SHA_JSON}",
      "tar": "images/wizard-${BUNDLE_VERSION}${ARCH_TAG_SUFFIX}.tar"
    }
  },
  "external_images": {
    "ollama": "ollama/ollama:latest",
    "open-webui": "ghcr.io/open-webui/open-webui:main",
    "postgres": "postgres:16-alpine",
    "redis": "redis:7-alpine",
    "chromadb": "chromadb/chroma:latest"
  }
}
EOF
ok "Manifest: ${MANIFEST_PATH}"

# ---------------------------------------------------------------------------
# Step 6 — Validate bundle
# ---------------------------------------------------------------------------
step "[6/6] Validating bundle..."

info "Running docker compose config --quiet on assembled bundle..."
docker compose -f "${OUTPUT_DIR}/docker-compose.yml" config --quiet \
  || fail "Bundle docker-compose.yml failed validation."
ok "Bundle docker-compose.yml is valid"

# Verify manifest.json is valid JSON
if command -v jq &>/dev/null; then
  jq . "${MANIFEST_PATH}" > /dev/null \
    || fail "manifest.json is not valid JSON."
  ok "manifest.json is valid JSON"
else
  warn "jq not found — skipping manifest.json JSON validation"
fi

# Verify image digests match (if export was done)
if [[ "${SKIP_EXPORT}" != "1" ]]; then
  info "Verifying exported image checksums..."
  sha256sum -c "${EXPORT_AGENTCORE}.sha256" \
    || fail "agentcore image checksum mismatch!"
  sha256sum -c "${EXPORT_WIZARD}.sha256" \
    || fail "wizard image checksum mismatch!"
  ok "Image checksums verified"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
BUNDLE_SIZE=$(du -sh "${OUTPUT_DIR}" | cut -f1)

echo ""
echo -e "${BOLD}${GREEN}============================================================${RESET}"
echo -e "${BOLD}${GREEN}  Docker Compose Bundle Build Complete${RESET}"
echo -e "${BOLD}${GREEN}============================================================${RESET}"
echo ""
echo -e "  Bundle dir : ${OUTPUT_DIR}"
echo -e "  Bundle size: ${BUNDLE_SIZE}"
echo -e "  Manifest   : ${MANIFEST_PATH}"
echo -e "  Version    : ${BUNDLE_VERSION}  (git ${GIT_SHA})"
echo -e "  Profile    : ${PROFILE}"
echo -e "  Arch       : linux/${TARGET_ARCH}"
echo ""
echo -e "  To deploy:"
echo -e "    cd ${OUTPUT_DIR}"
echo -e "    ./setup.sh"
echo -e "    docker compose up -d"
echo ""
