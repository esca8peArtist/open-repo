"""
Prometheus metrics for AgentCore.

All metrics are defined at module level so they are registered once and
reused across the application lifetime.  Import this module wherever you
need to record an observation.
"""
from __future__ import annotations

from prometheus_client import Counter, Gauge, Histogram

# ---------------------------------------------------------------------------
# Chat / LLM metrics
# ---------------------------------------------------------------------------

CHAT_REQUESTS = Counter(
    "agentcore_chat_requests_total",
    "Total number of chat requests processed",
    ["agent_id", "status"],
)

CHAT_DURATION = Histogram(
    "agentcore_chat_duration_seconds",
    "Duration of chat requests in seconds",
    ["agent_id"],
    buckets=[1, 5, 10, 30, 60, 120],
)

ACTIVE_SESSIONS = Gauge(
    "agentcore_active_sessions",
    "Number of currently active chat sessions",
)

LLM_TOKENS = Counter(
    "agentcore_llm_tokens_total",
    "Total LLM tokens consumed",
    ["agent_id", "direction"],  # direction: "input" | "output" | "total"
)

# ---------------------------------------------------------------------------
# Tool metrics
# ---------------------------------------------------------------------------

TOOL_CALLS = Counter(
    "agentcore_tool_calls_total",
    "Total MCP/dispatcher tool invocations",
    ["tool_name", "status"],  # status: "success" | "error"
)

# ---------------------------------------------------------------------------
# Pipeline metrics
# ---------------------------------------------------------------------------

PIPELINE_DURATION = Histogram(
    "agentcore_pipeline_duration_seconds",
    "Duration of pipeline executions in seconds",
    ["pipeline_id"],
)

# ---------------------------------------------------------------------------
# HTTP metrics
# ---------------------------------------------------------------------------

HTTP_REQUESTS = Counter(
    "agentcore_http_requests_total",
    "Total HTTP requests received",
    ["method", "path", "status"],
)

HTTP_DURATION = Histogram(
    "agentcore_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "path"],
)
