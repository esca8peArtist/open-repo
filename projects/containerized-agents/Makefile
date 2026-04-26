# =============================================================================
# Containerized Agents - Makefile
# Autonomous agents running in a fully self-hosted, offline-capable OS image
# =============================================================================

.DEFAULT_GOAL := help

.PHONY: help dev test test-cov lint format typecheck build-image build-os wizard agentcore clean doctor

# -----------------------------------------------------------------------------
# Help
# -----------------------------------------------------------------------------

help: ## Show available targets
	@echo ""
	@echo "  Containerized Agents"
	@echo "  Autonomous agents running in a fully self-hosted, offline-capable OS image"
	@echo ""
	@echo "  Usage: make <target>"
	@echo ""
	@echo "  Targets:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "    %-16s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""

# -----------------------------------------------------------------------------
# Development
# -----------------------------------------------------------------------------

dev: ## Install agentcore in editable mode with dev dependencies (using uv)
	uv pip install -e ".[dev]"

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

test: ## Run full test suite
	uv run pytest

test-cov: ## Run tests with coverage report
	uv run pytest --cov=agentcore --cov-report=term-missing --cov-report=html

# -----------------------------------------------------------------------------
# Code Quality
# -----------------------------------------------------------------------------

lint: ## Run ruff linter
	uv run ruff check .

format: ## Run ruff formatter
	uv run ruff format .

typecheck: ## Run type checker (pyright preferred, mypy fallback)
	@if uv run pyright --version > /dev/null 2>&1; then \
		uv run pyright; \
	else \
		uv run mypy agentcore; \
	fi

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------

build-image: ## Build the Docker Compose bundle
	@chmod +x scripts/build_compose_bundle.sh
	./scripts/build_compose_bundle.sh

build-os: ## Build the bootable OS image
	@chmod +x scripts/build_os_image.sh
	./scripts/build_os_image.sh

# -----------------------------------------------------------------------------
# Runtime
# -----------------------------------------------------------------------------

wizard: ## Start the setup wizard in dev mode
	uv run python -m wizard.app

agentcore: ## Start AgentCore API server in dev mode
	uv run python -m agentcore.server

# -----------------------------------------------------------------------------
# Maintenance
# -----------------------------------------------------------------------------

clean: ## Remove build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".coverage" -delete 2>/dev/null || true
	@echo "Build artifacts removed."

doctor: ## Run health check (verify all services are running)
	@echo "Running health checks..."
	@echo ""
	@echo "  [uv]         checking uv installation..."
	@uv --version && echo "  [uv]         OK" || echo "  [uv]         MISSING - install from https://github.com/astral-sh/uv"
	@echo ""
	@echo "  [docker]     checking Docker..."
	@docker info > /dev/null 2>&1 && echo "  [docker]     OK" || echo "  [docker]     NOT RUNNING - start Docker daemon"
	@echo ""
	@echo "  [compose]    checking Docker Compose..."
	@docker compose version > /dev/null 2>&1 && echo "  [compose]    OK" || echo "  [compose]    NOT FOUND - install docker-compose-plugin"
	@echo ""
	@echo "Health check complete."
