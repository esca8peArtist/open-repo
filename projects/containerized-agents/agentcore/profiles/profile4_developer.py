"""
Profile 4: Developer Assistant
Hardware: Tier 2 minimum (24GB), Tier 3 recommended (64GB)
Primary model: qwen3-coder:30b-a3b (MoE — only 3B active params, efficient)
Fallback: deepseek-coder-v2-lite:7b (Tier 2)

Tools:
  - Filesystem read-only (read_file, list_directory, search_files)
  - Code execution sandbox (execute_python)
  - GitHub API: search_code, get_file, create_issue, list_pull_requests (online only)
  - Web search (online only)
  - RAG over codebase (ChromaDB collection: "codebase")

Channels: Web chat, Voice
"""
from __future__ import annotations

from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ToolConfig,
)

SYSTEM_PROMPT = """You are an expert software engineering assistant with deep knowledge of software architecture, debugging, and best practices.

You can:
- Answer technical questions using the project codebase (via RAG)
- Review and explain code
- Help debug issues by reading relevant files
- Search GitHub for examples and documentation (when online)
- Execute Python code snippets to verify solutions
- Create GitHub issues for bugs/features found during exploration

Guidelines:
- Always read the relevant code before making suggestions — never guess at structure
- Prefer targeted, minimal changes over large rewrites
- Explain your reasoning, especially for architectural decisions
- When code execution would help verify an answer, use it
- Cite file paths and line numbers when referencing code
- If Slack is available, you can send summaries to configured channels

You have read-only filesystem access to the workspace and codebase."""

PROFILE_4_CONFIG = AgentConfig(
    name="Developer Assistant",
    profile=AgentProfile.DEVELOPER_ASSISTANT,
    model="qwen3-coder:30b-a3b",
    fallback_model="deepseek-coder-v2-lite:7b",
    system_prompt=SYSTEM_PROMPT,
    tools=[
        # --- Offline tools ---
        ToolConfig(
            name="read_file",
            description="Read the text contents of a file within /workspace or /data.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="list_directory",
            description="List files and subdirectories within /workspace or /data.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="search_files",
            description="Search for files matching a glob pattern within /workspace or /data.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="execute_python",
            description="Execute a Python code snippet in a sandboxed environment and return stdout/stderr.",
            enabled=True,
            requires_internet=False,
        ),
        # --- Online-only tools ---
        ToolConfig(
            name="search_code",
            description="Search code on GitHub using the code search API. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="get_file",
            description="Retrieve the contents of a file from a GitHub repository. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="create_issue",
            description="Create a new issue in a GitHub repository. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="list_pull_requests",
            description="List pull requests for a GitHub repository. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="web_search",
            description="Search the web for documentation, examples, and answers. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
    ],
    channels=[
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
        ChannelConfig(channel_type=ChannelType.VOICE, enabled=True),
    ],
    hardware_tier=2,
    rag_enabled=True,
    rag_collection="codebase",
    active=True,
    metadata={
        "github_repo": "",          # set during setup wizard (e.g. "owner/repo")
        "workspace_path": "/workspace",
        "slack_webhook": "",        # optional Slack incoming webhook URL
        "min_hardware_tier": 2,
        "recommended_hardware_tier": 3,
        "model_license": "Apache 2.0",
        "fallback_model_license": "Apache 2.0",
    },
)
