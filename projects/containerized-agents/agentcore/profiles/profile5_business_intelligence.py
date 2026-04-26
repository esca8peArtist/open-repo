"""
Profile 5: Business Intelligence
Hardware: Tier 3 (64GB RAM)
Primary model: deepseek-r1:14b (reasoning-optimized, MIT licensed)
Fallback: qwen2.5:14b (Apache 2.0)

Tools:
  - query_database: Local DB read-only (SQLite / PostgreSQL / MySQL)
  - read_file: CSV / Excel ingestion from /data
  - execute_python: Data analysis + matplotlib chart generation
  - generate_pdf_report: Professional PDF output
  - schedule_task: Automated recurring reports
  - send_email: Report delivery (online only)
  - web_search: Market context / benchmarks (online only)

Channels: Web dashboard only
RAG: disabled (data lives in databases, not documents)
"""
from __future__ import annotations

from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ToolConfig,
)

SYSTEM_PROMPT = """You are a business intelligence analyst. You help business owners and managers understand their data and make informed decisions.

Your capabilities:
- Query local databases (read-only) to answer business questions
- Analyze CSV/Excel data files
- Write and execute Python for data analysis and visualization
- Generate professional PDF reports with charts and tables
- Schedule automated reports and alerts
- Deliver reports via email or SMS (when internet available)

Approach:
- Always show your reasoning — explain what data you're looking at and why
- Quantify everything: use numbers, percentages, trends
- Flag anomalies and significant changes proactively
- Keep visualizations simple and actionable
- Executive summary first, detail second
- When a question requires assumptions, state them clearly

You have read-only database access. You CANNOT modify any data."""

PROFILE_5_CONFIG = AgentConfig(
    name="Business Intelligence",
    profile=AgentProfile.BUSINESS_INTELLIGENCE,
    model="deepseek-r1:14b",
    fallback_model="qwen2.5:14b",
    system_prompt=SYSTEM_PROMPT,
    tools=[
        # --- Offline tools ---
        ToolConfig(
            name="query_database",
            description=(
                "Execute a read-only SQL query against a configured local database "
                "(SQLite, PostgreSQL, or MySQL). Returns rows as JSON."
            ),
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="read_file",
            description=(
                "Read a CSV or Excel file from /data for ingestion into pandas. "
                "Returns file contents as text (CSV) or JSON (Excel sheet names)."
            ),
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="execute_python",
            description=(
                "Execute Python for data analysis, statistics, or matplotlib chart generation. "
                "Charts are saved to /data/reports/ and the filename returned."
            ),
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="generate_pdf_report",
            description=(
                "Compile a structured PDF report from sections, charts, and tables. "
                "Output saved to /data/reports/. Returns the output file path."
            ),
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="schedule_task",
            description=(
                "Schedule an automated report or alert to run at a given cron expression. "
                "Persisted across restarts via the scheduler service."
            ),
            enabled=True,
            requires_internet=False,
        ),
        # --- Online-only tools ---
        ToolConfig(
            name="send_email",
            description=(
                "Send a report or alert via SMTP email. Attaches PDF if a path is provided. "
                "Requires internet connectivity."
            ),
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="web_search",
            description=(
                "Search the web for market data, industry benchmarks, or external context "
                "to enrich analysis. Requires internet connectivity."
            ),
            enabled=True,
            requires_internet=True,
        ),
    ],
    channels=[
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
    ],
    hardware_tier=3,
    rag_enabled=False,
    rag_collection=None,
    active=True,
    metadata={
        "database_connections": [],        # list of DB URIs, populated during setup wizard
        "report_output_dir": "/data/reports",
        "scheduled_reports": [],           # populated at runtime by schedule_task calls
        "min_hardware_tier": 3,
        "model_license": "MIT",
        "fallback_model_license": "Apache 2.0",
        "default_chart_format": "png",
        "max_query_rows": 100000,
    },
)
