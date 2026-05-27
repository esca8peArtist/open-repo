#!/usr/bin/env bash
# phase-6-project-init.sh
#
# Purpose: Stage Phase 6 launch infrastructure for June 1 06:00 UTC activation.
# Idempotent: safe to run multiple times; skips existing directories and files,
# never overwrites content already written.
#
# Usage:
#   bash projects/systems-resilience/phase-6-project-init.sh
#   bash projects/systems-resilience/phase-6-project-init.sh --dry-run
#   bash projects/systems-resilience/phase-6-project-init.sh --rollback
#
# Options:
#   --dry-run     Print all actions without executing any
#   --rollback    Remove only the directories and files created by this script
#                 (uses MANIFEST file written during a prior run)
#
# Activation trigger: June 1 2026 06:00 UTC
# Preparation deadline: May 31 2026 23:59 UTC
#
# Dependencies: bash >= 4.0, git (for commit step), standard coreutils
# All paths are relative to the repository root. Script must be run from the
# repository root, or set REPO_ROOT explicitly below.

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
PROJECT_DIR="$REPO_ROOT/projects/systems-resilience"
PHASE6_DIR="$PROJECT_DIR/phase-6-research"
COLLAB_DIR="$PROJECT_DIR/phase-6-author-collaboration"
MANIFEST_FILE="$PROJECT_DIR/.phase6-init-manifest"
WORKLOG_FILE="$PROJECT_DIR/PHASE6_WORKLOG.md"
CHECKLIST_FILE="$PROJECT_DIR/PHASE6_LAUNCH_CHECKLIST.md"

# Onboarding kit source (already written; copied to shared folder)
ONBOARDING_SRC="$PROJECT_DIR/phase-6-author-onboarding-kit.md"

# Scaffolding subdirectories under phase-6-research/
DOMAIN_A_DIR="$PHASE6_DIR/domain-a-community-economic-resilience"
DOMAIN_C_DIR="$PHASE6_DIR/domain-c-skills-development"
DOMAIN_D_DIR="$PHASE6_DIR/domain-d-governance-scaling"
SOURCES_DIR="$PHASE6_DIR/sources"
DRAFTS_DIR="$PHASE6_DIR/drafts"
REVIEW_DIR="$PHASE6_DIR/peer-review"

DRY_RUN=0
ROLLBACK=0

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

for arg in "$@"; do
  case "$arg" in
    --dry-run)  DRY_RUN=1 ;;
    --rollback) ROLLBACK=1 ;;
    *)
      echo "ERROR: Unknown argument: $arg" >&2
      echo "Usage: $0 [--dry-run] [--rollback]" >&2
      exit 1
      ;;
  esac
done

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

log() {
  local level="$1"; shift
  echo "[$level] $(date -u '+%Y-%m-%dT%H:%M:%SZ') $*"
}

run() {
  # Execute or print depending on --dry-run flag.
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "[DRY-RUN] $*"
  else
    eval "$*"
  fi
}

make_dir() {
  local dir="$1"
  if [ -d "$dir" ]; then
    log INFO "Directory already exists (skip): $dir"
  else
    run mkdir -p "\"$dir\""
    log INFO "Created directory: $dir"
    # Record in manifest for rollback (only in non-dry-run mode)
    if [ "$DRY_RUN" -eq 0 ]; then
      echo "DIR:$dir" >> "$MANIFEST_FILE"
    fi
  fi
}

write_file_if_absent() {
  # Write $2 (content heredoc variable name) to $1 only if $1 does not exist.
  local path="$1"
  local content="$2"
  if [ -f "$path" ]; then
    log INFO "File already exists (skip): $path"
  else
    if [ "$DRY_RUN" -eq 1 ]; then
      echo "[DRY-RUN] Would write: $path"
    else
      printf '%s\n' "$content" > "$path"
      log INFO "Created file: $path"
      echo "FILE:$path" >> "$MANIFEST_FILE"
    fi
  fi
}

copy_file_if_absent() {
  local src="$1"
  local dest="$2"
  if [ ! -f "$src" ]; then
    log WARN "Source file not found (skip copy): $src"
    return 0
  fi
  if [ -f "$dest" ]; then
    log INFO "Destination already exists (skip copy): $dest"
  else
    run cp "\"$src\"" "\"$dest\""
    log INFO "Copied $src -> $dest"
    if [ "$DRY_RUN" -eq 0 ]; then
      echo "FILE:$dest" >> "$MANIFEST_FILE"
    fi
  fi
}

# ---------------------------------------------------------------------------
# Rollback mode
# ---------------------------------------------------------------------------

do_rollback() {
  if [ ! -f "$MANIFEST_FILE" ]; then
    log WARN "No manifest file found at $MANIFEST_FILE — nothing to roll back."
    exit 0
  fi

  log INFO "Rolling back files and directories recorded in manifest..."

  # Reverse order: remove files first, then directories
  local files=()
  local dirs=()

  while IFS= read -r line; do
    case "$line" in
      FILE:*) files+=("${line#FILE:}") ;;
      DIR:*)  dirs+=("${line#DIR:}")  ;;
    esac
  done < "$MANIFEST_FILE"

  for f in "${files[@]}"; do
    if [ -f "$f" ]; then
      rm -f "$f"
      log INFO "Removed file: $f"
    fi
  done

  # Remove directories in reverse order (deepest first)
  for d in $(printf '%s\n' "${dirs[@]}" | sort -r); do
    if [ -d "$d" ] && [ -z "$(ls -A "$d" 2>/dev/null)" ]; then
      rmdir "$d"
      log INFO "Removed empty directory: $d"
    else
      log WARN "Directory not empty or not found, skipped: $d"
    fi
  done

  rm -f "$MANIFEST_FILE"
  log INFO "Rollback complete. Manifest removed."
  exit 0
}

# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------

preflight() {
  log INFO "Pre-flight checks..."

  if [ ! -d "$PROJECT_DIR" ]; then
    log ERROR "Project directory not found: $PROJECT_DIR"
    log ERROR "Run this script from the repository root, or set REPO_ROOT."
    exit 1
  fi

  if [ ! -f "$ONBOARDING_SRC" ] && [ "$DRY_RUN" -eq 0 ]; then
    log WARN "Onboarding kit source not found: $ONBOARDING_SRC"
    log WARN "Shared-folder copy will be skipped. Run after author-onboarding-kit is committed."
  fi

  log INFO "Repository root: $REPO_ROOT"
  log INFO "Project dir:     $PROJECT_DIR"
  log INFO "Phase 6 research dir: $PHASE6_DIR"
  log INFO "Collaboration dir:    $COLLAB_DIR"
  log INFO "Dry run: $DRY_RUN | Rollback: $ROLLBACK"
  echo ""
}

# ---------------------------------------------------------------------------
# Step 1: Create directory structure
# ---------------------------------------------------------------------------

create_directories() {
  log INFO "=== Step 1: Creating directory structure ==="

  make_dir "$PHASE6_DIR"
  make_dir "$DOMAIN_A_DIR"
  make_dir "$DOMAIN_C_DIR"
  make_dir "$DOMAIN_D_DIR"
  make_dir "$SOURCES_DIR"
  make_dir "$DRAFTS_DIR"
  make_dir "$REVIEW_DIR"
  make_dir "$COLLAB_DIR"
  make_dir "$COLLAB_DIR/domain-a"
  make_dir "$COLLAB_DIR/shared"
  echo ""
}

# ---------------------------------------------------------------------------
# Step 2: Copy onboarding kit to shared collaboration folder
# ---------------------------------------------------------------------------

copy_onboarding_kit() {
  log INFO "=== Step 2: Copying author onboarding kit to shared folder ==="

  copy_file_if_absent \
    "$ONBOARDING_SRC" \
    "$COLLAB_DIR/domain-a/author-onboarding-kit.md"

  # Also copy domain research roadmap if present
  local roadmap_src="$PROJECT_DIR/phase-6-domain-a-research-roadmap.md"
  copy_file_if_absent \
    "$roadmap_src" \
    "$COLLAB_DIR/domain-a/research-roadmap.md"

  # Copy author outreach tracking
  local tracking_src="$PROJECT_DIR/author-outreach-tracking.md"
  copy_file_if_absent \
    "$tracking_src" \
    "$COLLAB_DIR/shared/author-outreach-tracking.md"

  echo ""
}

# ---------------------------------------------------------------------------
# Step 3: Initialize Phase 6 WORKLOG.md
# ---------------------------------------------------------------------------

init_worklog() {
  log INFO "=== Step 3: Initializing Phase 6 WORKLOG ==="

  local worklog_content
  worklog_content="# Phase 6 WORKLOG

Project: systems-resilience Phase 6
Initialized: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
Activation target: 2026-06-01 06:00 UTC

---

## Format

Each entry: Date | Agent/Author | Task | Output | Hours | Notes

---

## Log

| Date | Agent | Task | Output | Hours | Notes |
|------|-------|------|--------|-------|-------|
| $(date -u '+%Y-%m-%d') | phase-6-project-init.sh | Infrastructure staging | Directories + scaffolding created | 0.1 | Pre-activation setup |
"

  write_file_if_absent "$WORKLOG_FILE" "$worklog_content"
  echo ""
}

# ---------------------------------------------------------------------------
# Step 4: Initialize launch checklist
# ---------------------------------------------------------------------------

init_checklist() {
  log INFO "=== Step 4: Initializing Phase 6 launch checklist ==="

  local checklist_content
  checklist_content="# Phase 6 Launch Checklist

Status: PRE-ACTIVATION
Activation date: 2026-06-01 06:00 UTC
Decision deadline: 2026-05-31 23:59 UTC

---

## Pre-Activation (Complete by May 31)

### User Decisions
- [ ] Phase 5 publication timing confirmed (Option A, B, or C)
- [ ] Phase 6 domain selection confirmed (Domain A recommended, A+D combo also viable)
- [ ] Author confirmed or contingency path locked (see author-outreach-tracking.md)

### Infrastructure (Created by this script)
- [x] phase-6-research/ directory created
- [x] domain-a-community-economic-resilience/ directory created
- [x] domain-c-skills-development/ directory created (if applicable)
- [x] domain-d-governance-scaling/ directory created (if applicable)
- [x] sources/ directory created
- [x] drafts/ directory created
- [x] peer-review/ directory created
- [x] phase-6-author-collaboration/ directory created
- [x] Author onboarding kit copied to shared folder
- [x] PHASE6_WORKLOG.md initialized

### Pre-Research Assets (Already committed to master)
- [x] phase-6/01-community-economic-resilience.md (6,800 words, 38 citations)
- [x] phase-6/phase-6-candidate-a-one-pager.md
- [x] phase-6/phase-6-sequencing-recommendation.md
- [x] phase-6-domain-a-research-roadmap.md
- [x] phase-6-author-onboarding-kit.md
- [x] author-confirmation-email.md
- [x] author-outreach-tracking.md

---

## Activation Day (June 1)

- [ ] Author onboarded (onboarding kit delivered, scope call complete)
- [ ] Source library audit begun (top 40 sources accessibility check)
- [ ] Domain A production timeline confirmed with author
- [ ] Phase 5 Wave 1+2 editorial pass begun (if Option A selected)
- [ ] WORKLOG updated with June 1 entry

---

## Week 1 Milestones (June 1-7)

- [ ] Source library 90% verified accessible
- [ ] Domain A Section 3 outline drafted (policy and reform pathways)
- [ ] Section 4 case study selection finalized (WIR, Mondragon, Emilia-Romagna, Argentina)
- [ ] Inter-community trade protocol research begun (Gap 3 — highest priority)
- [ ] USDA grant mechanics research complete (Gap 4)

---

## Production Checkpoints

- [ ] June 15: Section 1 complete (~10,000 words)
- [ ] June 22: Sections 2-3 complete (~18,000 words cumulative)
- [ ] June 29: Section 4 complete (~8,000 words cumulative)
- [ ] July 6:  Section 5 complete (~7,000 words cumulative)
- [ ] July 13: Full draft complete (~45,000 words)
- [ ] July 27: Revision and citation pass complete
- [ ] August 9: Final production-ready document committed to master

---

## Success Criteria

- Word count: 45,000-55,000 total
- Citations: 120-150 verified
- Zone 5 examples: present in every section
- USDA grant section: actionable (reader can start application process)
- Zero placeholders in final document
- Committed to master by August 9
"

  write_file_if_absent "$CHECKLIST_FILE" "$checklist_content"
  echo ""
}

# ---------------------------------------------------------------------------
# Step 5: Domain research scaffolding (stub files)
# ---------------------------------------------------------------------------

init_domain_scaffolding() {
  log INFO "=== Step 5: Creating domain research scaffolding ==="

  # Domain A source index stub
  local domain_a_sources_content
  domain_a_sources_content="# Domain A Source Index

Status: STUB — populate during June 1-7 source library audit
Domain: Community Economic Resilience
Pre-research citations: 38 (see phase-6/01-community-economic-resilience.md)
Additional sources needed: 82-112

---

## Tier 1 — Canonical Sources

| # | Author/Title | URL | Sections | Status |
|---|-------------|-----|---------|--------|
| 1 | Ostrom, Governing the Commons | https://www.cambridge.org/core/books/governing-the-commons | All | Verified |
| 2 | WIR Bank annual reports | https://www.wir.ch/en/ | Section 4 | Verify June 1 |
| 3 | Mondragon Annual Report 2024 | https://www.mondragon-corporation.com/en/about-us/annual-report/ | Section 4 | Verify June 1 |
| 4 | USDA RBCS program docs | https://www.rd.usda.gov/programs-services/business-programs/rural-cooperative-development-grants | Section 3 | Verify June 1 |

---

## Tier 2 — Supporting Sources

[Populate during source library audit, June 1-7]

---

## Tier 3 — Zone 5 Primary Sources

[Populate during source library audit, June 1-7]

---

## Gap Tracking

| Gap | Description | Priority | Sources Needed | Status |
|----|-------------|----------|---------------|--------|
| Gap 1 | Timebanking quantitative impact data | Refinement | Timebanks USA, Nesta Foundation reviews | Open |
| Gap 2 | Midwest cooperative formation barriers | High | USDA RD state guides, NFCDCU | Open |
| Gap 3 | Inter-community trade protocols | Highest | Red de Trueque node structure, Good Food Network | Open |
| Gap 4 | USDA grant application mechanics | Moderate | USDA RBCS current NOFA, NSAC guides | Open |
| Gap 5 | Community land trust legal framework | Low | Grounded Solutions Network, Lincoln Institute | Open |
"

  write_file_if_absent "$DOMAIN_A_DIR/source-index.md" "$domain_a_sources_content"

  # Domain A draft stub
  local domain_a_draft_stub
  domain_a_draft_stub="# Domain A Draft — Community Economic Resilience

Status: STUB — production begins June 5-8
Pre-research chapter: see phase-6/01-community-economic-resilience.md (6,800 words, 38 citations)

---

## Planned Structure

- Section 1: Economic failure scenarios (COMPLETE in pre-research chapter)
- Section 2: Community-scale economic institutions (STARTED in pre-research chapter)
- Section 3: Policy barriers and reform pathways (AUTHOR TASK)
- Section 4: International case studies — WIR, Mondragon, Emilia-Romagna, Argentina (AUTHOR TASK)
- Section 5: Zone 5 Midwest implementation (AUTHOR TASK)
- Section 6: Inter-community economic architecture (AUTHOR TASK — highest priority gap)
- Section 7: Implementation roadmap — minimum viable through phase-three (AUTHOR TASK)

---

[Draft content begins here after June 5 production start]
"

  write_file_if_absent "$DRAFTS_DIR/domain-a-draft.md" "$domain_a_draft_stub"

  echo ""
}

# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------

main() {
  echo "========================================================"
  echo " Phase 6 Project Init — systems-resilience"
  echo " Activation target: 2026-06-01 06:00 UTC"
  echo "========================================================"
  echo ""

  if [ "$ROLLBACK" -eq 1 ]; then
    do_rollback
  fi

  preflight

  # Initialize manifest file (idempotent — append if exists)
  if [ "$DRY_RUN" -eq 0 ] && [ ! -f "$MANIFEST_FILE" ]; then
    touch "$MANIFEST_FILE"
    log INFO "Created manifest file: $MANIFEST_FILE"
  fi

  create_directories
  copy_onboarding_kit
  init_worklog
  init_checklist
  init_domain_scaffolding

  echo ""
  log INFO "=== Phase 6 initialization complete ==="
  echo ""
  echo "Summary of actions:"
  local dir_count file_count
  dir_count=$(grep -c '^DIR:' "$MANIFEST_FILE" 2>/dev/null) || dir_count=0
  file_count=$(grep -c '^FILE:' "$MANIFEST_FILE" 2>/dev/null) || file_count=0
  echo "  Directories created: ${dir_count} new"
  echo "  Files created:       ${file_count} new"
  echo ""
  echo "Next steps:"
  echo "  1. Confirm author by May 30 16:00 UTC (see author-outreach-tracking.md)"
  echo "  2. Log May 31 decisions (Phase 5 timing + Phase 6 domain selection)"
  echo "  3. Activate June 1 06:00 UTC — author onboarding begins"
  echo "  4. Update PHASE6_WORKLOG.md each production day"
  echo ""
  echo "Rollback: bash $0 --rollback"
  echo "Dry run:  bash $0 --dry-run"
}

main "$@"
