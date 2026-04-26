# AgentCore Test Suite

## Overview

This directory contains the full test suite for AgentCore, organised into two
categories:

| Category | Location | What it tests |
|---|---|---|
| **Unit** | `tests/unit/` | Individual classes and functions — no external services |
| **Integration** | `tests/integration/` | End-to-end flows with mocked external services |

---

## Running Tests

All commands must be run from the project root (`containerized-agents/`).

### Run the full suite

```bash
uv run pytest
```

### Run unit tests only

```bash
uv run pytest tests/unit/ -v
```

### Run integration tests only

```bash
uv run pytest tests/integration/ -v
```

### Run a specific file

```bash
uv run pytest tests/unit/test_mcp_tools.py -v
```

### Run by marker

```bash
uv run pytest -m offline         # Offline-capability tests
uv run pytest -m crypto          # Cryptographic primitives
uv run pytest -m license         # License system tests
uv run pytest -m profiles        # Profile config validation
uv run pytest -m pipeline        # PipelineEngine tests
uv run pytest -m channels        # Telegram / Twilio channel tests
```

### Run with coverage

```bash
uv run pytest --cov=agentcore --cov=security --cov-report=term-missing
```

---

## Test Files

### Unit Tests (`tests/unit/`)

| File | What it covers |
|---|---|
| `test_mcp_tools.py` | MCP tool invocation, offline degradation, SQL security, code execution sandbox |
| `test_pipeline_engine.py` | PipelineEngine step execution, parallel batches, dependency ordering, timeouts |
| `test_message_router.py` | ToolDispatcher routing, connectivity caching, Telegram/Twilio message splitting |
| `test_license_system.py` | License generation/validation, AES-256-GCM crypto, PBKDF2 key derivation |
| `test_hardware_detection.py` | Hardware fingerprint collection, tier detection from Settings |

### Integration Tests (`tests/integration/`)

| File | What it covers |
|---|---|
| `test_agentcore_api.py` | FastAPI REST endpoints — health, chat, agents CRUD |
| `test_offline_capability.py` | Core features work without internet (LLM, RAG, voice, pipelines) |
| `test_graceful_degradation.py` | All internet-dependent tools return graceful errors offline |
| `test_hardware_binding.py` | Full TPM/license lifecycle: purchase-time generation → boot validation |
| `test_profiles.py` | All 6 profile configs are valid, tools registered, channels correct |
| `test_rag_pipeline.py` | Document ingestion + retrieval against mocked ChromaDB |
| `test_voice_pipeline.py` | STT (Whisper) + TTS (Kokoro) pipeline with mocked models |
| `test_channels.py` | Telegram + Twilio setup/teardown, inbound parsing, message splitting |
| `test_update_flow.py` | Update check offline graceful failure, manifest validation, rollback |
| `test_multi_agent.py` | Profile 6 enterprise orchestrator, sub-agent delegation, parallel execution |

---

## Shared Fixtures (`tests/conftest.py`)

| Fixture | Scope | Description |
|---|---|---|
| `event_loop` | session | Session-scoped asyncio event loop |
| `mock_settings` | function | Settings pointing to localhost test endpoints |
| `mock_ollama_response` | function | Fake Ollama chat completion response |
| `sample_agent_config` | function | Minimal AgentConfig (Personal Productivity, no external deps) |
| `offline_context` | function | `MCPContext(is_online=False)` for offline tests |
| `online_context` | function | `MCPContext(is_online=True)` for online tests |
| `agent_instance` | function | `AgentInstance` with mocked OpenAI client (no real Ollama needed) |

---

## Test Philosophy

### No External Services Required (Unit Tests)

Unit tests must run with zero external infrastructure. All network calls,
database connections, and process invocations are mocked.

### Mocked External Services (Integration Tests)

Integration tests mock external boundaries (Ollama, ChromaDB, Twilio, Telegram)
but test the full internal pipeline including config loading, routing logic,
and error handling.

### Offline-First Testing

The most critical tests are the offline capability tests (`test_offline_capability.py`
and `test_graceful_degradation.py`). These verify that the product's core promise
— "fully offline after setup" — is upheld.

Key rules:
- All `requires_internet=True` MCP tools must return `MCPToolResult(success=False)` when `context.is_online=False`
- The agent must remain responsive on web chat even when Telegram / Twilio are down
- The license validation must work without any internet call

### Real Crypto, Mocked Hardware

The license and crypto tests use **real** AES-256-GCM and PBKDF2 operations
(via the `cryptography` library). Only the OS-level hardware collection calls
(`tpm2-tools`, `dmidecode`, `/sys/class/net`) are mocked.

---

## Adding New Tests

1. **Unit test**: add to `tests/unit/` — no network, no subprocess calls
2. **Integration test**: add to `tests/integration/` — mock at the network boundary
3. Register any new custom markers in `pytest.ini`
4. Add shared fixtures to `tests/conftest.py` if reused across multiple files
