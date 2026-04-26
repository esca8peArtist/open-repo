"""
Comprehensive shared fixtures for the AgentCore test suite.
Covers all test areas: API, security, offline, tools, RAG, voice, channels,
hardware, updater, and wizard.
"""
from __future__ import annotations

import os
# Set required Settings fields for test environment before anything imports agentcore
os.environ.setdefault("POSTGRES_URL", "postgresql+asyncpg://test:test@localhost/testdb")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
os.environ.setdefault("API_SECRET_KEY", "test-secret-key-that-is-long-enough")
os.environ.setdefault("AGENTCORE_BASE_URL", "http://localhost:8080")
os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")
os.environ.setdefault("UPDATE_PUBLIC_KEY_HEX", "")

import asyncio
import json
import sqlite3
import tempfile
import uuid
from pathlib import Path
from typing import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

from agentcore.config import Settings
from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ChatRequest,
    ChatResponse,
    ToolConfig,
)
from agentcore.mcp.protocol import MCPContext


# ---------------------------------------------------------------------------
# Event loop
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def event_loop():
    """Session-scoped event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# ---------------------------------------------------------------------------
# Settings & API key
# ---------------------------------------------------------------------------

TEST_API_KEY = "test-secret-key-32-chars-minimum!!"


@pytest.fixture
def mock_settings() -> Settings:
    """Settings pointing to test endpoints (no real services required)."""
    return Settings(
        ollama_base_url="http://localhost:11434",
        postgres_url="postgresql+asyncpg://test:test@localhost:5432/test",
        redis_url="redis://localhost:6379/0",
        chroma_url="http://localhost:8000",
        api_secret_key=TEST_API_KEY,
        hardware_tier=1,
    )


# ---------------------------------------------------------------------------
# MCP contexts
# ---------------------------------------------------------------------------


@pytest.fixture
def offline_context() -> MCPContext:
    """MCPContext with is_online=False — used for offline degradation tests."""
    return MCPContext(agent_id="test-agent", session_id="test-session", is_online=False)


@pytest.fixture
def online_context() -> MCPContext:
    """MCPContext with is_online=True — used for online-capable tests."""
    return MCPContext(agent_id="test-agent", session_id="test-session", is_online=True)


# ---------------------------------------------------------------------------
# Agent config
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_agent_config() -> AgentConfig:
    """Minimal AgentConfig for unit tests — no external dependencies."""
    return AgentConfig(
        name="Test Agent",
        profile=AgentProfile.PERSONAL_PRODUCTIVITY,
        model="qwen2.5:7b-instruct",
        system_prompt="You are a helpful test assistant.",
        tools=[
            ToolConfig(name="get_current_time", description="Get current time", enabled=True, requires_internet=False),
            ToolConfig(name="echo", description="Echo arguments", enabled=True, requires_internet=False),
        ],
        channels=[ChannelConfig(channel_type=ChannelType.WEB, enabled=True)],
        hardware_tier=1,
        rag_enabled=False,
        active=True,
    )


# ---------------------------------------------------------------------------
# Ollama mock
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_ollama_response() -> dict:
    """Mock Ollama chat-completion API response."""
    return {
        "model": "qwen2.5:7b-instruct",
        "message": {"role": "assistant", "content": "Hello! How can I help you today?"},
        "done": True,
        "total_duration": 1_500_000_000,
        "eval_count": 12,
    }


# ---------------------------------------------------------------------------
# AgentInstance
# ---------------------------------------------------------------------------


@pytest.fixture
def agent_instance(sample_agent_config, mock_settings):
    """AgentInstance with a mocked OpenAI client so tests don't hit Ollama."""
    from agentcore.core.agent import AgentInstance

    instance = AgentInstance(config=sample_agent_config, settings=mock_settings)

    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Test response"
    mock_response.choices[0].message.tool_calls = None
    mock_response.choices[0].finish_reason = "stop"
    mock_response.usage.total_tokens = 10
    mock_client.chat.completions.create = AsyncMock(return_value=mock_response)
    instance.client = mock_client

    return instance


# ---------------------------------------------------------------------------
# FastAPI test app
# ---------------------------------------------------------------------------


@pytest.fixture
def test_app(mock_settings):
    """FastAPI test application with mocked registry, dispatcher, and router."""
    from agentcore.api.chat import router as chat_router
    from agentcore.api.agents import router as agents_router
    from agentcore.api.health import router as health_router
    from agentcore.api.admin import router as admin_router

    app = FastAPI()
    app.include_router(health_router)
    app.include_router(chat_router)
    app.include_router(agents_router)
    app.include_router(admin_router)

    # Mock registry
    mock_registry = MagicMock()
    mock_registry._engine = MagicMock()
    mock_registry._instances = {}
    mock_registry.list_agents = AsyncMock(return_value=[])
    mock_registry.get_agent = AsyncMock(return_value=None)
    mock_registry.create_agent = AsyncMock(return_value=str(uuid.uuid4()))
    mock_registry.update_agent = AsyncMock(return_value=True)
    mock_registry.delete_agent = AsyncMock(return_value=True)
    mock_registry.reload = AsyncMock()

    # Mock dispatcher
    mock_dispatcher = MagicMock()
    mock_dispatcher.is_online = AsyncMock(return_value=True)
    mock_dispatcher.invalidate_connectivity_cache = MagicMock()

    # Mock message router
    mock_message_router = MagicMock()
    mock_message_router._routing_table = {}
    mock_message_router.rebuild_routing_table = AsyncMock()

    # Mock redis
    mock_redis = MagicMock()
    mock_redis.ping = AsyncMock()

    app.state.settings = mock_settings
    app.state.registry = mock_registry
    app.state.dispatcher = mock_dispatcher
    app.state.message_router = mock_message_router
    app.state.redis = mock_redis

    return app


@pytest.fixture
def api_client(test_app):
    """Synchronous TestClient for the test app."""
    return TestClient(test_app)


@pytest.fixture
def auth_headers() -> dict:
    """Headers with valid API key."""
    return {"X-API-Key": TEST_API_KEY}


# ---------------------------------------------------------------------------
# SQLite in-memory DB helpers
# ---------------------------------------------------------------------------


@pytest.fixture
def crm_db_path(tmp_path):
    """Temporary SQLite path for CRM tool tests, with Settings cache cleared."""
    from agentcore.config import get_settings

    db = tmp_path / "crm_test.db"
    db_str = str(db)
    os.environ["CRM_DB_PATH"] = db_str
    get_settings.cache_clear()
    try:
        yield db_str
    finally:
        get_settings.cache_clear()
        os.environ.pop("CRM_DB_PATH", None)


@pytest.fixture
def scheduler_db_path(tmp_path) -> str:
    """Temporary SQLite path for scheduler tool tests."""
    db = tmp_path / "scheduler_test.db"
    return str(db)


# ---------------------------------------------------------------------------
# Mock Twilio
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_twilio_client():
    """Mock Twilio REST client."""
    client = MagicMock()
    client.messages.create = MagicMock(return_value=MagicMock(sid="SM123", status="queued"))
    return client


# ---------------------------------------------------------------------------
# Mock Telegram Bot
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_telegram_bot():
    """Mock python-telegram-bot Bot object."""
    bot = MagicMock()
    bot.send_message = AsyncMock(return_value=MagicMock(message_id=42))
    bot.get_file = AsyncMock(return_value=MagicMock(download_as_bytearray=AsyncMock(return_value=bytearray(b"\x00\x01\x02"))))
    return bot


# ---------------------------------------------------------------------------
# Voice fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def minimal_wav_bytes() -> bytes:
    """Minimal valid 44-byte WAV file header + a tiny data chunk."""
    import struct
    # 44-byte WAV header + 100 bytes of silence
    num_samples = 100
    sample_rate = 16000
    num_channels = 1
    bits_per_sample = 16
    byte_rate = sample_rate * num_channels * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    data_size = num_samples * block_align
    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF",
        36 + data_size,
        b"WAVE",
        b"fmt ",
        16,  # PCM chunk size
        1,   # PCM format
        num_channels,
        sample_rate,
        byte_rate,
        block_align,
        bits_per_sample,
        b"data",
        data_size,
    )
    return header + b"\x00" * data_size


@pytest.fixture
def mock_transcription_result():
    """Mock TranscriptionResult from the STT transcriber."""
    result = MagicMock()
    result.text = "Hello, this is a test transcription."
    result.language = "en"
    result.duration_seconds = 2.5
    result.segments = [{"start": 0.0, "end": 2.5, "text": "Hello, this is a test transcription."}]
    return result


@pytest.fixture
def mock_synthesis_result():
    """Mock SynthesisResult from the TTS synthesizer."""
    result = MagicMock()
    result.audio_bytes = b"\x00" * 44 + b"\x00" * 100  # Fake WAV bytes
    result.voice = "af_heart"
    result.duration_seconds = 1.2
    result.sample_rate = 24000
    return result


# ---------------------------------------------------------------------------
# Hardware / crypto fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def test_signing_key() -> bytes:
    """32-byte AES-256 / HMAC key for test use."""
    return os.urandom(32)


@pytest.fixture
def test_fingerprint_hex() -> str:
    """Valid 64-char hex fingerprint string."""
    return "ab" * 32


# ---------------------------------------------------------------------------
# Ed25519 test key pair
# ---------------------------------------------------------------------------


@pytest.fixture
def ed25519_keypair():
    """Generate a fresh Ed25519 key pair for update manifest signing tests."""
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


# ---------------------------------------------------------------------------
# Update manifest fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_manifest() -> dict:
    """Unsigned sample update manifest."""
    return {
        "schema_version": 1,
        "generated_at": "2026-03-11T00:00:00Z",
        "latest": {"version": "1.2.0"},
        "releases": [
            {
                "version": "1.2.0",
                "min_version": "1.0.0",
                "changelog": "Bug fixes and performance improvements.",
                "components": {
                    "agentcore": {
                        "image_url": "https://example.com/agentcore-1.2.0.tar.gz",
                        "sha256": "a" * 64,
                        "size_bytes": 104857600,
                        "docker_tag": "1.2.0",
                    }
                },
            }
        ],
    }
