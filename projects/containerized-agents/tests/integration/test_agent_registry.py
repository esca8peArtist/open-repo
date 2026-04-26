"""
Integration tests — AgentRegistry CRUD against real PostgreSQL.

These tests verify:
1. Full create / get / update / delete lifecycle against a live database.
2. Cache invalidation: after update_agent(), a fresh get_agent() returns
   the updated config rather than a stale cached instance.

Requires:  pytest -m integration
"""
from __future__ import annotations

import uuid

import pytest
import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ToolConfig,
)


pytestmark = pytest.mark.integration


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest_asyncio.fixture(scope="module")
async def registry(wait_for_postgres, integration_env):
    """
    Return a fully-started AgentRegistry connected to the test database.

    The registry's _ensure_schema() call creates the agents table if it does
    not already exist.
    """
    from agentcore.config import get_settings
    from agentcore.core.registry import AgentRegistry

    settings = get_settings()
    reg = AgentRegistry(settings=settings)
    await reg.start()

    yield reg

    await reg.stop()


@pytest.fixture
def sample_config() -> AgentConfig:
    """A minimal AgentConfig for CRUD tests."""
    return AgentConfig(
        name=f"Integration Test Agent {uuid.uuid4().hex[:6]}",
        profile=AgentProfile.PERSONAL_PRODUCTIVITY,
        model="qwen2.5:7b-instruct",
        system_prompt="You are a helpful integration test assistant.",
        tools=[
            ToolConfig(
                name="echo",
                description="Echo input back",
                enabled=True,
                requires_internet=False,
            )
        ],
        channels=[ChannelConfig(channel_type=ChannelType.WEB, enabled=True)],
        hardware_tier=1,
        active=True,
    )


# ---------------------------------------------------------------------------
# Tests — CRUD lifecycle
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_create_agent_persisted(registry, sample_config):
    """create_agent() should persist the config and return a UUID string."""
    agent_id = await registry.create_agent(sample_config)

    assert agent_id is not None
    uuid.UUID(agent_id)  # raises ValueError if not a valid UUID

    # Config should be in the in-memory cache
    assert agent_id in registry._configs


@pytest.mark.asyncio
async def test_get_agent_returns_instance(registry, sample_config):
    """get_agent() should return a live AgentInstance for a created agent."""
    agent_id = await registry.create_agent(sample_config)

    instance = await registry.get_agent(agent_id)

    assert instance is not None
    assert instance.config.id == agent_id
    assert instance.config.name == sample_config.name


@pytest.mark.asyncio
async def test_list_agents_includes_created(registry, sample_config):
    """list_agents() should include an agent after it has been created."""
    agent_id = await registry.create_agent(sample_config)

    agents = await registry.list_agents()
    ids = [a.id for a in agents]

    assert agent_id in ids


@pytest.mark.asyncio
async def test_update_agent_changes_config(registry, sample_config):
    """update_agent() should persist the new config and return True."""
    agent_id = await registry.create_agent(sample_config)

    updated_config = sample_config.model_copy(
        update={"name": "Updated Agent Name", "system_prompt": "Updated system prompt."}
    )
    result = await registry.update_agent(agent_id, updated_config)

    assert result is True

    # Fetch fresh config from DB via reload then get
    await registry.reload()
    cfg = registry._configs.get(agent_id)
    assert cfg is not None
    assert cfg.name == "Updated Agent Name"


@pytest.mark.asyncio
async def test_update_agent_invalidates_instance_cache(registry, sample_config):
    """After update_agent(), the old AgentInstance should be evicted from cache."""
    agent_id = await registry.create_agent(sample_config)

    # Pre-warm the instance cache
    old_instance = await registry.get_agent(agent_id)
    assert old_instance is not None
    assert agent_id in registry._instances

    # Update the agent
    updated_config = sample_config.model_copy(update={"name": "Cache Invalidation Test"})
    await registry.update_agent(agent_id, updated_config)

    # Instance should have been evicted
    assert agent_id not in registry._instances, (
        "AgentInstance cache should be invalidated after update_agent()"
    )

    # Getting the agent again should create a fresh instance with the new config
    new_instance = await registry.get_agent(agent_id)
    assert new_instance is not None
    assert new_instance.config.name == "Cache Invalidation Test"


@pytest.mark.asyncio
async def test_delete_agent_removes_from_db(registry, sample_config):
    """delete_agent() should remove the agent from both the DB and caches."""
    agent_id = await registry.create_agent(sample_config)
    assert agent_id in registry._configs

    result = await registry.delete_agent(agent_id)
    assert result is True

    # Should be gone from in-memory caches
    assert agent_id not in registry._configs
    assert agent_id not in registry._instances

    # Should be gone from DB (get_agent returns None for unknown IDs)
    instance = await registry.get_agent(agent_id)
    assert instance is None


@pytest.mark.asyncio
async def test_get_nonexistent_agent_returns_none(registry):
    """get_agent() should return None for an ID that does not exist."""
    fake_id = str(uuid.uuid4())
    instance = await registry.get_agent(fake_id)
    assert instance is None


@pytest.mark.asyncio
async def test_reload_syncs_with_database(registry, sample_config):
    """reload() should refresh the in-memory config cache from the database."""
    agent_id = await registry.create_agent(sample_config)

    # Manually corrupt the in-memory cache
    registry._configs.pop(agent_id, None)
    assert agent_id not in registry._configs

    # reload() should restore it from DB
    await registry.reload()
    assert agent_id in registry._configs


@pytest.mark.asyncio
async def test_create_agent_sets_timestamps(registry, sample_config):
    """created_at and updated_at should be set on creation."""
    agent_id = await registry.create_agent(sample_config)
    cfg = registry._configs.get(agent_id)

    assert cfg is not None
    assert cfg.created_at is not None
    assert cfg.updated_at is not None
