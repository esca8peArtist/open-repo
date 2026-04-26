.PHONY: help install dev test test-cov lint format serve load-seed clean docs meilisearch meilisearch-stop

help:
	@echo "Open-Repo Backend - Development Commands"
	@echo ""
	@echo "  make install       Install dependencies (production)"
	@echo "  make dev           Install development dependencies"
	@echo "  make test          Run test suite (24+ tests)"
	@echo "  make test-cov      Run tests with coverage report"
	@echo "  make serve         Start development server (http://localhost:8000)"
	@echo "  make load-seed     Load 32 OpenFarm crops into database"
	@echo "  make meilisearch   Start Meilisearch in Docker (http://localhost:7700)"
	@echo "  make meilisearch-stop  Stop Meilisearch container"
	@echo "  make lint          Lint code with ruff"
	@echo "  make format        Format code with ruff"
	@echo "  make clean         Remove build artifacts"
	@echo ""

install:
	uv pip install -e .

dev:
	uv pip install -e ".[dev]"

test:
	uv run pytest tests/ -v

test-cov:
	uv run pytest tests/ --cov=app --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

serve:
	uv run uvicorn app.main:create_app --reload --host 0.0.0.0 --port 8000

load-seed:
	uv run python scripts/load_seed_data.py

lint:
	uv run ruff check app/ tests/

format:
	uv run ruff format app/ tests/

meilisearch:
	@echo "Starting Meilisearch in Docker..."
	docker run -d \
	  --name open_repo_meilisearch \
	  -p 7700:7700 \
	  -e MEILI_ENV=development \
	  -e MEILI_MASTER_KEY=masterKey \
	  getmeili/meilisearch:latest
	@echo "Meilisearch is running at http://localhost:7700"
	@echo "Master key: masterKey"

meilisearch-stop:
	@echo "Stopping Meilisearch..."
	docker stop open_repo_meilisearch 2>/dev/null || true
	docker rm open_repo_meilisearch 2>/dev/null || true
	@echo "Meilisearch stopped"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .coverage -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ dist/ build/ *.egg-info
	@echo "Cleaned up build artifacts"
