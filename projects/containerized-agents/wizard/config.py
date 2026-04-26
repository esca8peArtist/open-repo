"""
Wizard configuration — environment-driven settings.
"""
from __future__ import annotations

import os
from pathlib import Path

# Port wizard listens on
WIZARD_PORT: int = int(os.environ.get("WIZARD_PORT", "8888"))
WIZARD_HOST: str = os.environ.get("WIZARD_HOST", "0.0.0.0")

# Written by Step 12 to signal setup is complete
WIZARD_COMPLETE_MARKER: Path = Path(
    os.environ.get("WIZARD_COMPLETE_MARKER", "/opt/agentcore/.wizard-complete")
)

# Wizard session state persistence.
# Default location is inside the container's data volume (/app/data), which is
# owned by the wizard process and not world-readable like /tmp.
# Override via WIZARD_STATE_FILE env var if needed.
STATE_FILE: Path = Path(
    os.environ.get("WIZARD_STATE_FILE", "/app/data/wizard-state.json")
)

# AgentCore dashboard URL after setup
DASHBOARD_URL: str = os.environ.get("AGENTCORE_DASHBOARD_URL", "http://agent.local:8080")

# Ollama API base (for model pull and benchmark)
OLLAMA_URL: str = os.environ.get("OLLAMA_URL", "http://ollama:11434")

# AgentCore licensing API
AGENTCORE_URL: str = os.environ.get("AGENTCORE_URL", "http://agentcore:8080")

TOTAL_STEPS: int = 12

# Profile metadata for display in the wizard (augments AgentConfig)
PROFILE_DISPLAY: dict[int, dict] = {
    1: {
        "icon": "📅",
        "tagline": "Personal Productivity",
        "use_cases": ["Calendar management", "Email drafting", "Document search", "Task reminders"],
        "min_ram_gb": 8,
        "recommended_tier": 1,
    },
    2: {
        "icon": "💬",
        "tagline": "Customer Support",
        "use_cases": ["Ticket handling", "FAQ responses", "Escalation routing", "Sentiment tracking"],
        "min_ram_gb": 8,
        "recommended_tier": 1,
    },
    3: {
        "icon": "📈",
        "tagline": "Sales Outreach",
        "use_cases": ["Lead follow-up", "Meeting booking", "Proposal drafting", "CRM integration"],
        "min_ram_gb": 16,
        "recommended_tier": 2,
    },
    4: {
        "icon": "💻",
        "tagline": "Developer Assistant",
        "use_cases": ["Code review", "PR summaries", "Debugging help", "Documentation generation"],
        "min_ram_gb": 24,
        "recommended_tier": 3,
    },
    5: {
        "icon": "📊",
        "tagline": "Business Intelligence",
        "use_cases": ["Data analysis", "Report generation", "KPI monitoring", "Trend detection"],
        "min_ram_gb": 16,
        "recommended_tier": 2,
    },
    6: {
        "icon": "🏢",
        "tagline": "Enterprise Orchestrator",
        "use_cases": ["Multi-agent coordination", "Cross-department workflows", "Executive summaries", "Compliance reporting"],
        "min_ram_gb": 64,
        "recommended_tier": 4,
    },
}

# Models per profile (from requirements Section 15)
PROFILE_MODELS: dict[int, list[str]] = {
    1: ["qwen2.5:7b-instruct", "phi4-mini", "nomic-embed-text"],
    2: ["qwen2.5:7b-instruct", "nomic-embed-text"],
    3: ["qwen2.5:14b-instruct", "nomic-embed-text"],
    4: ["qwen3-coder:30b-a3b", "nomic-embed-text"],
    5: ["deepseek-r1:14b", "nomic-embed-text"],
    6: ["qwen3:72b", "nomic-embed-text"],
}

LANGUAGES: list[dict] = [
    {"code": "en", "label": "English"},
    {"code": "es", "label": "Español"},
    {"code": "fr", "label": "Français"},
    {"code": "de", "label": "Deutsch"},
    {"code": "pt", "label": "Português"},
    {"code": "ja", "label": "日本語"},
    {"code": "zh", "label": "中文"},
    {"code": "ar", "label": "العربية"},
]
