#!/usr/bin/env bash
# pull_models.sh — Pull Ollama models for the specified hardware tier
# Containerized AI Agents — v1.0
#
# Usage:
#   ./pull_models.sh --tier [1|2|3|4]
#   ./pull_models.sh --tier 2 --profile sales_outreach
#
# Requirements:
#   - Ollama must be running and reachable at http://localhost:11434
#   - 'yq' (YAML processor) OR Python 3 must be available to parse models.yml
#   - Internet access is required on first run; skips already-present models

set -euo pipefail

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODELS_YML="${SCRIPT_DIR}/models.yml"
TIER=""
PROFILE=""
DRY_RUN=false

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; RESET='\033[0m'

info()    { echo -e "${BLUE}[INFO]${RESET}  $*"; }
success() { echo -e "${GREEN}[OK]${RESET}    $*"; }
warn()    { echo -e "${YELLOW}[WARN]${RESET}  $*"; }
error()   { echo -e "${RED}[ERROR]${RESET} $*" >&2; }
header()  { echo -e "\n${BOLD}=== $* ===${RESET}"; }

# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
usage() {
  cat <<EOF
Usage: $(basename "$0") --tier TIER [OPTIONS]

Options:
  --tier TIER        Hardware tier: 1, 2, 3, or 4  (required)
  --profile NAME     Only pull models for a specific agent profile (optional)
  --dry-run          Show what would be pulled without actually pulling
  --ollama-host URL  Ollama base URL (default: http://localhost:11434)
  -h, --help         Show this help message

Examples:
  $(basename "$0") --tier 1
  $(basename "$0") --tier 3 --profile developer_assistant
  $(basename "$0") --tier 2 --dry-run
EOF
}

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tier)         TIER="$2"; shift 2 ;;
    --profile)      PROFILE="$2"; shift 2 ;;
    --dry-run)      DRY_RUN=true; shift ;;
    --ollama-host)  OLLAMA_HOST="$2"; shift 2 ;;
    -h|--help)      usage; exit 0 ;;
    *) error "Unknown argument: $1"; usage; exit 1 ;;
  esac
done

if [[ -z "$TIER" ]]; then
  error "Missing required argument: --tier"
  usage
  exit 1
fi

if [[ ! "$TIER" =~ ^[1-4]$ ]]; then
  error "Invalid tier '$TIER'. Must be 1, 2, 3, or 4."
  exit 1
fi

# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------
check_dependencies() {
  if ! command -v ollama &>/dev/null; then
    error "'ollama' CLI not found in PATH. Is Ollama installed?"
    exit 1
  fi

  if command -v yq &>/dev/null; then
    YAML_PARSER="yq"
  elif command -v python3 &>/dev/null; then
    YAML_PARSER="python3"
  else
    error "Neither 'yq' nor 'python3' found. Install one to parse models.yml."
    exit 1
  fi
}

# ---------------------------------------------------------------------------
# YAML parsing — extract Ollama model names for a given tier
# Only returns models where served_by is NOT set (i.e., real Ollama models).
# ---------------------------------------------------------------------------
get_models_for_tier() {
  local tier_key="tier${TIER}"

  if [[ "$YAML_PARSER" == "yq" ]]; then
    # yq v4 syntax
    yq eval ".${tier_key} | to_entries | .[] | select(.value.served_by == null) | .value.model" \
      "$MODELS_YML" 2>/dev/null | grep -v '^null$' | grep -v '^---$' || true
  else
    # Python 3 fallback
    python3 - "$MODELS_YML" "$tier_key" <<'PYEOF'
import sys, json
try:
    import yaml
except ImportError:
    # Minimal YAML subset parser (handles simple key: value)
    import re
    def load_yaml_simple(path):
        result = {}
        current_tier = None
        current_role = None
        with open(path) as f:
            for line in f:
                stripped = line.rstrip()
                if not stripped or stripped.startswith('#'):
                    continue
                indent = len(stripped) - len(stripped.lstrip())
                stripped = stripped.lstrip()
                if indent == 0 and stripped.endswith(':'):
                    current_tier = stripped[:-1]
                    result[current_tier] = {}
                    current_role = None
                elif indent == 2 and stripped.endswith(':') and current_tier:
                    current_role = stripped[:-1]
                    result[current_tier][current_role] = {}
                elif indent == 4 and current_tier and current_role:
                    if ':' in stripped:
                        k, v = stripped.split(':', 1)
                        result[current_tier][current_role][k.strip()] = v.strip()
        return result
    data = load_yaml_simple(sys.argv[1])
else:
    with open(sys.argv[1]) as f:
        data = yaml.safe_load(f)

tier_key = sys.argv[2]
tier_data = data.get(tier_key, {})
for role, cfg in tier_data.items():
    if isinstance(cfg, dict):
        served_by = cfg.get('served_by')
        model = cfg.get('ollama_tag') or cfg.get('model')
        if model and not served_by:
            print(model)
PYEOF
  fi
}

# ---------------------------------------------------------------------------
# Check if a model is already downloaded
# ---------------------------------------------------------------------------
model_is_present() {
  local model="$1"
  # Query the local Ollama instance for the model list
  local tags
  tags=$(curl -sf "${OLLAMA_HOST}/api/tags" 2>/dev/null || echo '{"models":[]}')
  # Normalise: strip digest tags for comparison; check both exact and base name
  echo "$tags" | grep -q "\"name\":\"${model}\"" && return 0
  # Also check without tag suffix
  local base_name="${model%%:*}"
  echo "$tags" | grep -q "\"name\":\"${base_name}" && return 0
  return 1
}

# ---------------------------------------------------------------------------
# Verify model integrity after pull
# ---------------------------------------------------------------------------
verify_model() {
  local model="$1"
  info "Verifying integrity of '${model}'..."
  # 'ollama show' returns model metadata; failure indicates corruption
  if ollama show "$model" &>/dev/null; then
    success "Integrity check passed for '${model}'"
    return 0
  else
    error "Integrity check FAILED for '${model}'"
    return 1
  fi
}

# ---------------------------------------------------------------------------
# Pull a single model with retry
# ---------------------------------------------------------------------------
pull_model() {
  local model="$1"
  local max_attempts=3
  local attempt=1

  if model_is_present "$model"; then
    success "Already present — skipping '${model}'"
    return 0
  fi

  while [[ $attempt -le $max_attempts ]]; do
    info "Pulling '${model}' (attempt ${attempt}/${max_attempts})..."

    if $DRY_RUN; then
      info "[DRY RUN] Would run: ollama pull ${model}"
      return 0
    fi

    if OLLAMA_HOST="$OLLAMA_HOST" ollama pull "$model"; then
      success "Successfully pulled '${model}'"
      verify_model "$model" || {
        warn "Model pull succeeded but integrity check failed — will retry"
        attempt=$((attempt + 1))
        continue
      }
      return 0
    else
      warn "Pull attempt ${attempt} failed for '${model}'"
      attempt=$((attempt + 1))
      if [[ $attempt -le $max_attempts ]]; then
        info "Retrying in 5 seconds..."
        sleep 5
      fi
    fi
  done

  error "Failed to pull '${model}' after ${max_attempts} attempts"
  return 1
}

# ---------------------------------------------------------------------------
# Wait for Ollama to be ready
# ---------------------------------------------------------------------------
wait_for_ollama() {
  local max_wait=60
  local elapsed=0
  local interval=3

  info "Waiting for Ollama at ${OLLAMA_HOST}..."
  while ! curl -sf "${OLLAMA_HOST}/api/tags" &>/dev/null; do
    if [[ $elapsed -ge $max_wait ]]; then
      error "Ollama did not become ready within ${max_wait}s"
      exit 1
    fi
    sleep $interval
    elapsed=$((elapsed + interval))
  done
  success "Ollama is ready"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
main() {
  header "Containerized AI Agents — Model Pull"
  info "Tier:         ${TIER}"
  info "Profile:      ${PROFILE:-all}"
  info "Ollama host:  ${OLLAMA_HOST}"
  info "Models file:  ${MODELS_YML}"
  $DRY_RUN && warn "DRY RUN mode — no models will actually be pulled"

  check_dependencies
  wait_for_ollama

  if [[ ! -f "$MODELS_YML" ]]; then
    error "models.yml not found at: ${MODELS_YML}"
    exit 1
  fi

  header "Resolving models for Tier ${TIER}"
  mapfile -t MODELS < <(get_models_for_tier)

  if [[ ${#MODELS[@]} -eq 0 ]]; then
    warn "No Ollama-served models found for tier${TIER} in models.yml"
    exit 0
  fi

  info "Models to pull: ${MODELS[*]}"

  local failed=()
  for model in "${MODELS[@]}"; do
    [[ -z "$model" ]] && continue
    header "Model: ${model}"
    if ! pull_model "$model"; then
      failed+=("$model")
    fi
  done

  header "Summary"
  if [[ ${#failed[@]} -eq 0 ]]; then
    success "All models for Tier ${TIER} are ready"
  else
    error "The following models failed to pull:"
    for m in "${failed[@]}"; do
      error "  - ${m}"
    done
    exit 1
  fi
}

main "$@"
