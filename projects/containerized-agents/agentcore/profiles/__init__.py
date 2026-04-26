"""
Agent profile definitions for AgentCore.

Profiles 1-3: personal_productivity, customer_support, sales_outreach
Profiles 4-6: developer_assistant, business_intelligence, enterprise_orchestrator

Usage
-----
    from agentcore.profiles import get_all_profiles

    for cfg in get_all_profiles():
        print(cfg.name, cfg.profile, cfg.model)
"""
from __future__ import annotations

from agentcore.models import AgentConfig
from agentcore.profiles.profile1_personal import PROFILE_1_CONFIG
from agentcore.profiles.profile2_customer_support import PROFILE_2_CONFIG
from agentcore.profiles.profile3_sales_outreach import PROFILE_3_CONFIG
from agentcore.profiles.profile4_developer import PROFILE_4_CONFIG
from agentcore.profiles.profile5_business_intelligence import PROFILE_5_CONFIG
from agentcore.profiles.profile6_enterprise import PROFILE_6_CONFIG, SUBAGENT_CONFIGS

# Ordered list — index position corresponds to profile number (1-based)
_ALL_PROFILES: list[AgentConfig] = [
    PROFILE_1_CONFIG,
    PROFILE_2_CONFIG,
    PROFILE_3_CONFIG,
    PROFILE_4_CONFIG,
    PROFILE_5_CONFIG,
    PROFILE_6_CONFIG,
]


def get_all_profiles() -> list[AgentConfig]:
    """
    Return all registered AgentConfig objects in profile-number order.

    Returns a new list each call so callers can safely mutate the result
    without affecting the module-level registry.
    """
    return list(_ALL_PROFILES)


__all__ = [
    "PROFILE_1_CONFIG",
    "PROFILE_2_CONFIG",
    "PROFILE_3_CONFIG",
    "PROFILE_4_CONFIG",
    "PROFILE_5_CONFIG",
    "PROFILE_6_CONFIG",
    "SUBAGENT_CONFIGS",
    "get_all_profiles",
]
