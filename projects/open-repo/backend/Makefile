.PHONY: help install dev test test-cov lint format serve load-seed clean docs

help:
	@echo "Open-Repo Backend - Development Commands"
	@echo ""
	@echo "  make install       Install dependencies (production)"
	@echo "  make dev           Install development dependencies"
	@echo "  make test          Run test suite (24 tests)"
	@echo "  make test-cov      Run tests with coverage report"
	@echo "  make serve         Start development server (http://localhost:8000)"
	@echo "  make load-seed     Load 32 OpenFarm crops into database"
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

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .coverage -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ dist/ build/ *.egg-info
	@echo "Cleaned up build artifacts"
