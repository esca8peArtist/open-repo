"""
Shared utilities for profile management.

This module is the single source of truth for:
  - Loading seed JSON files from agentcore/profiles/seeds/
  - Retrieving a profile config by name at runtime
  - Seeding profiles into PostgreSQL (idempotent — skips existing rows)
  - Selecting the correct model for the node's hardware tier
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING

from agentcore.models import AgentConfig

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# Directory that contains the seed JSON files
_SEEDS_DIR = Path(__file__).parent / "seeds"

# Map profile numbers to their seed filenames (no suffix)
_SEED_FILES: dict[int, str] = {
    1: "profile1",
    2: "profile2",
    3: "profile3",
}


# ---------------------------------------------------------------------------
# Seed loading
# ---------------------------------------------------------------------------


def load_seed(profile_number: int) -> dict:
    """
    Load the seed JSON for a given profile number.

    Args:
        profile_number: Integer profile identifier (1, 2, 3, …).

    Returns:
        Parsed dict ready to be passed to AgentConfig(**data).

    Raises:
        ValueError: If *profile_number* has no registered seed file.
        FileNotFoundError: If the seed file is missing on disk.
    """
    stem = _SEED_FILES.get(profile_number)
    if stem is None:
        raise ValueError(
            f"No seed file registered for profile number {profile_number}. "
            f"Available: {sorted(_SEED_FILES)}"
        )

    seed_path = _SEEDS_DIR / f"{stem}.json"
    if not seed_path.exists():
        raise FileNotFoundError(
            f"Seed file not found: {seed_path}. "
            "Ensure agentcore/profiles/seeds/ is present and populated."
        )

    with seed_path.open(encoding="utf-8") as fh:
        data: dict = json.load(fh)

    logger.debug("Loaded seed for profile %d from %s", profile_number, seed_path)
    return data


# ---------------------------------------------------------------------------
# Profile lookup
# ---------------------------------------------------------------------------


def get_profile_by_name(name: str) -> AgentConfig | None:
    """
    Return the AgentConfig whose name matches *name* (case-insensitive).

    Searches all registered profiles.  Returns None if no match is found.

    Args:
        name: Human-readable profile name, e.g. "Personal Assistant".

    Returns:
        The matching AgentConfig, or None.
    """
    from agentcore.profiles import get_all_profiles  # local import to avoid circular

    name_lower = name.strip().lower()
    for config in get_all_profiles():
        if config.name.lower() == name_lower:
            return config
    return None


# ---------------------------------------------------------------------------
# Database seeding
# ---------------------------------------------------------------------------


async def seed_profiles_to_db(registry, profiles: list[AgentConfig]) -> None:
    """
    Insert profile seeds into the database if not already present.

    Called during the setup wizard when the user selects a profile.
    Uses the registry's storage backend to check for and persist configs.
    Skips any profile whose *name* already exists in the DB (idempotent).

    Args:
        registry: AgentCore agent registry (duck-typed; must expose
                  ``get_by_name(name) -> AgentConfig | None`` and
                  ``save(config) -> None`` as awaitable coroutines).
        profiles: List of AgentConfig objects to seed.
    """
    for config in profiles:
        try:
            existing = await registry.get_by_name(config.name)
            if existing is not None:
                logger.info(
                    "Profile '%s' already in DB — skipping seed.", config.name
                )
                continue

            await registry.save(config)
            logger.info("Seeded profile '%s' into DB (id=%s).", config.name, config.id)

        except Exception as exc:  # noqa: BLE001
            # Log but continue — a partial seed is better than a complete failure
            logger.error(
                "Failed to seed profile '%s': %s", config.name, exc, exc_info=True
            )


# ---------------------------------------------------------------------------
# Hardware-tier model selection
# ---------------------------------------------------------------------------


def select_model_for_tier(config: AgentConfig, tier: int) -> str:
    """
    Return the appropriate Ollama model tag for a given hardware tier.

    Decision logic:
    - If the node's *tier* is at least as capable as the profile's required
      ``hardware_tier``, use the primary model.
    - If the node's *tier* is lower AND a ``fallback_model`` is defined,
      use the fallback.
    - If the node's *tier* is lower AND no fallback is defined, log a warning
      and return the primary model anyway (caller must decide whether to abort).

    Args:
        config: The AgentConfig describing the profile.
        tier:   The hardware tier of the current node (1–4).

    Returns:
        Ollama model tag string (e.g. ``"qwen2.5:7b-instruct"``).
    """
    if tier >= config.hardware_tier:
        return config.model

    if config.fallback_model:
        logger.info(
            "Node tier %d < profile required tier %d — using fallback model '%s' "
            "instead of '%s' for profile '%s'.",
            tier,
            config.hardware_tier,
            config.fallback_model,
            config.model,
            config.name,
        )
        return config.fallback_model

    logger.warning(
        "Node tier %d < profile required tier %d and no fallback_model defined "
        "for profile '%s'. Attempting primary model '%s' — may exceed RAM budget.",
        tier,
        config.hardware_tier,
        config.name,
        config.model,
    )
    return config.model
