"""
AgentRegistry — loads and caches AgentConfig records from PostgreSQL.
Creates AgentInstance objects on demand and caches them in memory.

Database access uses SQLAlchemy 2.x async engine with asyncpg.
"""
from __future__ import annotations

import asyncio
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Any

from agentcore.config import Settings
from agentcore.models import AgentConfig, AgentProfile, ChannelConfig, ChannelType, ToolConfig

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Lazy imports of SQLAlchemy to avoid hard import errors in environments
# without a database (e.g., unit tests with a mock registry).
# ---------------------------------------------------------------------------


class AgentRegistry:
    """
    Central registry for AgentInstance objects.

    Responsibilities:
    1. CRUD operations on AgentConfig records stored in PostgreSQL.
    2. In-memory cache of AgentInstance objects (one per agent_id).
    3. On-demand instantiation: first access for an agent_id creates the instance.
    4. Full reload from DB on demand (e.g., after admin config change).
    """

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._engine: Any = None
        self._lock = asyncio.Lock()

        # Cache: agent_id -> AgentInstance
        self._instances: dict[str, Any] = {}

        # Cache: agent_id -> AgentConfig
        self._configs: dict[str, AgentConfig] = {}

        # Shared dispatcher and pipeline engine (injected post-construction)
        self._dispatcher: Any = None
        self._pipeline_engine: Any = None

    # ------------------------------------------------------------------
    # Startup / teardown
    # ------------------------------------------------------------------

    async def start(self) -> None:
        """Initialise database connection and warm the config cache."""
        try:
            from sqlalchemy.ext.asyncio import create_async_engine

            self._engine = create_async_engine(
                self.settings.postgres_url,
                pool_pre_ping=True,
                pool_size=5,
                max_overflow=10,
            )
            await self._ensure_schema()
            await self.reload()
            logger.info("AgentRegistry started — loaded %d agent configs", len(self._configs))
        except Exception as exc:
            logger.error("AgentRegistry failed to connect to PostgreSQL: %s", exc)
            logger.warning("Running with empty in-memory registry (no persistence).")

    async def stop(self) -> None:
        """Dispose database connection pool."""
        if self._engine is not None:
            await self._engine.dispose()
            logger.info("AgentRegistry database connection closed.")

    def set_dispatcher(self, dispatcher: Any) -> None:
        self._dispatcher = dispatcher
        # Apply to all already-instantiated agents
        for instance in self._instances.values():
            instance.set_dispatcher(dispatcher)

    def set_pipeline_engine(self, engine: Any) -> None:
        self._pipeline_engine = engine
        for instance in self._instances.values():
            instance.set_pipeline_engine(engine)

    # ------------------------------------------------------------------
    # Schema management
    # ------------------------------------------------------------------

    async def _ensure_schema(self) -> None:
        """Create the agents table if it does not exist."""
        ddl = """
        CREATE TABLE IF NOT EXISTS agents (
            id          TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            profile     TEXT NOT NULL DEFAULT 'general',
            model       TEXT NOT NULL DEFAULT 'llama3.1:8b',
            system_prompt TEXT NOT NULL DEFAULT '',
            tools       JSONB NOT NULL DEFAULT '[]',
            channels    JSONB NOT NULL DEFAULT '[]',
            hardware_tier INTEGER NOT NULL DEFAULT 1,
            active      BOOLEAN NOT NULL DEFAULT TRUE,
            created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        """
        from sqlalchemy import text

        async with self._engine.begin() as conn:
            await conn.execute(text(ddl))

    # ------------------------------------------------------------------
    # Public CRUD API
    # ------------------------------------------------------------------

    async def get_agent(self, agent_id: str) -> Any | None:
        """
        Return the live AgentInstance for agent_id, instantiating it if needed.
        Returns None if the agent_id is not found.
        """
        async with self._lock:
            if agent_id in self._instances:
                return self._instances[agent_id]

            config = self._configs.get(agent_id)
            if config is None:
                # Try a fresh DB fetch
                config = await self._fetch_config(agent_id)
                if config is None:
                    return None
                self._configs[agent_id] = config

            instance = self._make_instance(config)
            self._instances[agent_id] = instance
            return instance

    async def list_agents(self) -> list[AgentConfig]:
        """Return all AgentConfig records (from cache, refreshed from DB if empty)."""
        if not self._configs:
            await self.reload()
        return list(self._configs.values())

    async def create_agent(self, config: AgentConfig) -> str:
        """
        Persist a new AgentConfig to PostgreSQL.
        Returns the agent_id (which is set on the config object).
        """
        if not config.id:
            config.id = str(uuid.uuid4())
        config.created_at = datetime.now(timezone.utc)
        config.updated_at = datetime.now(timezone.utc)

        await self._upsert_config(config)
        self._configs[config.id] = config
        logger.info("Created agent: %s (%s)", config.name, config.id)
        return config.id

    async def update_agent(self, agent_id: str, config: AgentConfig) -> bool:
        """Update an existing agent config. Returns True on success."""
        config.id = agent_id
        config.updated_at = datetime.now(timezone.utc)

        try:
            await self._upsert_config(config)
            self._configs[agent_id] = config
            # Invalidate the cached instance so it gets recreated with fresh config
            self._instances.pop(agent_id, None)
            logger.info("Updated agent: %s", agent_id)
            return True
        except Exception as exc:
            logger.error("Failed to update agent %s: %s", agent_id, exc)
            return False

    async def delete_agent(self, agent_id: str) -> bool:
        """Delete an agent from the database and invalidate caches."""
        try:
            if self._engine is not None:
                from sqlalchemy import text

                async with self._engine.begin() as conn:
                    await conn.execute(text("DELETE FROM agents WHERE id = :id"), {"id": agent_id})

            self._configs.pop(agent_id, None)
            self._instances.pop(agent_id, None)
            logger.info("Deleted agent: %s", agent_id)
            return True
        except Exception as exc:
            logger.error("Failed to delete agent %s: %s", agent_id, exc)
            return False

    async def reload(self) -> None:
        """Re-read all agent configs from PostgreSQL and invalidate instance cache."""
        if self._engine is None:
            return

        try:
            from sqlalchemy import text

            async with self._engine.connect() as conn:
                result = await conn.execute(text("SELECT * FROM agents WHERE active = TRUE"))
                rows = result.mappings().all()

            new_configs: dict[str, AgentConfig] = {}
            for row in rows:
                cfg = self._row_to_config(dict(row))
                new_configs[cfg.id] = cfg

            async with self._lock:
                self._configs = new_configs
                # Purge instances for configs that no longer exist or have changed
                stale = [
                    aid for aid in self._instances
                    if aid not in new_configs
                ]
                for aid in stale:
                    self._instances.pop(aid)

            logger.info("AgentRegistry reloaded — %d agents active", len(self._configs))

        except Exception as exc:
            logger.error("AgentRegistry reload failed: %s", exc)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _fetch_config(self, agent_id: str) -> AgentConfig | None:
        """Fetch a single AgentConfig from DB by id."""
        if self._engine is None:
            return None
        try:
            from sqlalchemy import text

            async with self._engine.connect() as conn:
                result = await conn.execute(
                    text("SELECT * FROM agents WHERE id = :id"),
                    {"id": agent_id},
                )
                row = result.mappings().first()
                if row is None:
                    return None
                return self._row_to_config(dict(row))
        except Exception as exc:
            logger.error("Failed to fetch agent %s: %s", agent_id, exc)
            return None

    async def _upsert_config(self, config: AgentConfig) -> None:
        """Insert or update an AgentConfig row in the database."""
        if self._engine is None:
            return  # In-memory only mode

        from sqlalchemy import text

        sql = text("""
            INSERT INTO agents (id, name, profile, model, system_prompt, tools, channels,
                                hardware_tier, active, created_at, updated_at)
            VALUES (:id, :name, :profile, :model, :system_prompt, :tools::jsonb, :channels::jsonb,
                    :hardware_tier, :active, :created_at, :updated_at)
            ON CONFLICT (id) DO UPDATE SET
                name = EXCLUDED.name,
                profile = EXCLUDED.profile,
                model = EXCLUDED.model,
                system_prompt = EXCLUDED.system_prompt,
                tools = EXCLUDED.tools,
                channels = EXCLUDED.channels,
                hardware_tier = EXCLUDED.hardware_tier,
                active = EXCLUDED.active,
                updated_at = EXCLUDED.updated_at
        """)
        async with self._engine.begin() as conn:
            await conn.execute(
                sql,
                {
                    "id": config.id,
                    "name": config.name,
                    "profile": config.profile.value,
                    "model": config.model,
                    "system_prompt": config.system_prompt,
                    "tools": json.dumps([t.model_dump() for t in config.tools]),
                    "channels": json.dumps([c.model_dump() for c in config.channels]),
                    "hardware_tier": config.hardware_tier,
                    "active": config.active,
                    "created_at": config.created_at,
                    "updated_at": config.updated_at,
                },
            )

    @staticmethod
    def _row_to_config(row: dict[str, Any]) -> AgentConfig:
        """Convert a raw DB row dict to an AgentConfig Pydantic model."""
        # tools and channels may come back as already-parsed lists (asyncpg + jsonb)
        raw_tools = row.get("tools") or []
        raw_channels = row.get("channels") or []

        if isinstance(raw_tools, str):
            raw_tools = json.loads(raw_tools)
        if isinstance(raw_channels, str):
            raw_channels = json.loads(raw_channels)

        return AgentConfig(
            id=row["id"],
            name=row["name"],
            profile=AgentProfile(row.get("profile", "general")),
            model=row.get("model", "llama3.1:8b"),
            system_prompt=row.get("system_prompt", ""),
            tools=[ToolConfig(**t) for t in raw_tools],
            channels=[ChannelConfig(**c) for c in raw_channels],
            hardware_tier=row.get("hardware_tier", 1),
            active=row.get("active", True),
            created_at=row.get("created_at", datetime.now(timezone.utc)),
            updated_at=row.get("updated_at", datetime.now(timezone.utc)),
        )

    def _make_instance(self, config: AgentConfig) -> Any:
        """Create a new AgentInstance from config, injecting shared dependencies."""
        from agentcore.core.agent import AgentInstance

        instance = AgentInstance(config=config, settings=self.settings)
        if self._dispatcher is not None:
            instance.set_dispatcher(self._dispatcher)
        if self._pipeline_engine is not None:
            instance.set_pipeline_engine(self._pipeline_engine)
        return instance
