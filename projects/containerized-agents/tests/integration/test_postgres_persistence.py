"""
Integration tests — PostgreSQL conversation persistence.

These tests verify that AgentInstance correctly persists conversations and
messages to a real PostgreSQL database.

Requires:  pytest -m integration
"""
from __future__ import annotations

import uuid

import pytest
import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


pytestmark = pytest.mark.integration


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest_asyncio.fixture(scope="module")
async def pg_engine(wait_for_postgres):
    """Create a SQLAlchemy async engine connected to the test Postgres instance."""
    engine = create_async_engine(
        wait_for_postgres["url"],
        pool_pre_ping=True,
    )

    # Ensure required tables exist (same DDL the app uses at startup)
    ddl = [
        """
        CREATE TABLE IF NOT EXISTS conversations (
            id            TEXT         PRIMARY KEY,
            agent_profile VARCHAR(50)  NOT NULL,
            channel       VARCHAR(50)  NOT NULL DEFAULT 'web',
            started_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
            ended_at      TIMESTAMPTZ,
            metadata      JSONB        NOT NULL DEFAULT '{}'
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS messages (
            id              TEXT         PRIMARY KEY,
            conversation_id TEXT         NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
            role            VARCHAR(20)  NOT NULL,
            content         TEXT         NOT NULL,
            tokens_used     INTEGER,
            model           VARCHAR(100),
            created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
            metadata        JSONB        NOT NULL DEFAULT '{}'
        )
        """,
    ]
    async with engine.begin() as conn:
        for stmt in ddl:
            await conn.execute(text(stmt))

    yield engine

    await engine.dispose()


@pytest_asyncio.fixture
async def conv_store(wait_for_postgres):
    """Return a fresh ConversationStore pointed at the test database."""
    from agentcore.core.agent import ConversationStore

    store = ConversationStore(postgres_url=wait_for_postgres["url"])
    yield store
    await store.close()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_create_conversation_returns_uuid(conv_store):
    """create_conversation() should insert a row and return a UUID string."""
    conv_id = await conv_store.create_conversation(
        agent_profile="personal_productivity",
        channel="web",
        metadata={"test": True},
    )

    assert conv_id is not None
    # Should be a valid UUID string
    uuid.UUID(conv_id)


@pytest.mark.asyncio
async def test_save_and_retrieve_messages(conv_store, pg_engine):
    """Messages saved via save_message() must be persisted and retrievable."""
    conv_id = await conv_store.create_conversation(
        agent_profile="personal_productivity",
        channel="web",
    )
    assert conv_id is not None

    # Save a user message followed by an assistant reply
    await conv_store.save_message(conv_id, "user", "Hello, how are you?")
    await conv_store.save_message(
        conv_id,
        "assistant",
        "I'm doing well, thank you!",
        tokens_used=15,
        model="qwen2.5:7b-instruct",
    )

    # Verify directly in the database
    async with pg_engine.connect() as conn:
        result = await conn.execute(
            text("SELECT role, content FROM messages WHERE conversation_id = :cid ORDER BY created_at"),
            {"cid": conv_id},
        )
        rows = result.fetchall()

    assert len(rows) == 2
    assert rows[0].role == "user"
    assert rows[0].content == "Hello, how are you?"
    assert rows[1].role == "assistant"
    assert rows[1].content == "I'm doing well, thank you!"


@pytest.mark.asyncio
async def test_ensure_conversation_creates_when_none(conv_store):
    """ensure_conversation(None, ...) should create a new conversation row."""
    conv_id = await conv_store.ensure_conversation(
        conversation_id=None,
        agent_profile="developer_assistant",
        channel="web",
    )

    assert conv_id is not None
    uuid.UUID(conv_id)


@pytest.mark.asyncio
async def test_ensure_conversation_passes_through_existing_id(conv_store):
    """ensure_conversation(existing_id, ...) should return the same id unchanged."""
    existing_id = str(uuid.uuid4())
    # First create the conversation so the FK is satisfied
    created_id = await conv_store.create_conversation(
        agent_profile="general",
        channel="web",
    )

    returned_id = await conv_store.ensure_conversation(
        conversation_id=created_id,
        agent_profile="general",
        channel="web",
    )

    assert returned_id == created_id


@pytest.mark.asyncio
async def test_message_count_matches_saves(conv_store, pg_engine):
    """The number of persisted messages must equal the number of save calls."""
    conv_id = await conv_store.create_conversation("general", "web")
    assert conv_id is not None

    messages_to_save = [
        ("user", "Message one"),
        ("assistant", "Response one"),
        ("user", "Message two"),
        ("assistant", "Response two"),
        ("user", "Message three"),
    ]

    for role, content in messages_to_save:
        await conv_store.save_message(conv_id, role, content)

    async with pg_engine.connect() as conn:
        result = await conn.execute(
            text("SELECT COUNT(*) as cnt FROM messages WHERE conversation_id = :cid"),
            {"cid": conv_id},
        )
        row = result.fetchone()

    assert row.cnt == len(messages_to_save)


@pytest.mark.asyncio
async def test_conversation_metadata_stored_as_jsonb(conv_store, pg_engine):
    """Metadata passed to create_conversation should be stored as JSONB."""
    meta = {"user_agent": "TestBrowser/1.0", "locale": "en-US", "session_flags": [1, 2, 3]}
    conv_id = await conv_store.create_conversation(
        agent_profile="customer_support",
        channel="telegram",
        metadata=meta,
    )
    assert conv_id is not None

    async with pg_engine.connect() as conn:
        result = await conn.execute(
            text("SELECT metadata FROM conversations WHERE id = :cid"),
            {"cid": conv_id},
        )
        row = result.fetchone()

    assert row is not None
    # asyncpg/SQLAlchemy returns JSONB as a Python dict
    stored_meta = row.metadata
    if isinstance(stored_meta, str):
        import json
        stored_meta = json.loads(stored_meta)

    assert stored_meta.get("locale") == "en-US"
    assert stored_meta.get("user_agent") == "TestBrowser/1.0"
