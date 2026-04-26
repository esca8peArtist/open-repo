"""
Task scheduler MCP tools — PostgreSQL-backed scheduled task queue.

Table (auto-created if missing)
--------------------------------
scheduled_tasks(
    id           TEXT PRIMARY KEY,
    task_type    TEXT NOT NULL,
    target       TEXT NOT NULL,     -- email address, contact id, etc.
    scheduled_at TEXT NOT NULL,     -- ISO 8601 UTC
    payload      TEXT DEFAULT '{}', -- JSON blob
    status       TEXT DEFAULT 'pending',  -- pending | running | done | cancelled | failed
    created_at   TEXT NOT NULL,
    updated_at   TEXT NOT NULL
)

AgentCore polls this table and executes due tasks.

Config (env vars)
-----------------
SCHEDULER_DB_URL — PostgreSQL DSN (falls back to DB_POSTGRES_URL, then SQLite /data/scheduler.db)

Profiles: personal_productivity (1), customer_support (2), sales_outreach (3)
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import sqlite3
import uuid
from datetime import datetime, timezone
from functools import partial
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["personal_productivity", "customer_support", "sales_outreach"]

_VALID_STATUSES = {"pending", "running", "done", "cancelled", "failed"}

_SQLITE_FALLBACK = "/data/scheduler.db"

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS scheduled_tasks (
    id           TEXT PRIMARY KEY,
    task_type    TEXT NOT NULL,
    target       TEXT NOT NULL,
    scheduled_at TEXT NOT NULL,
    payload      TEXT DEFAULT '{}',
    status       TEXT DEFAULT 'pending',
    created_at   TEXT NOT NULL,
    updated_at   TEXT NOT NULL
);
"""


def _scheduler_db_path() -> str:
    s = get_settings()
    return s.scheduler_db_url or s.db_postgres_url


def _sqlite_conn() -> sqlite3.Connection:
    path = _SQLITE_FALLBACK
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute(_SCHEMA_SQL)
    conn.commit()
    return conn


def _is_postgres_url(url: str) -> bool:
    return url.startswith("postgresql") or url.startswith("postgres")


def _execute_on_db(fn_sqlite, fn_postgres):
    """Route execution to Postgres or SQLite based on config."""
    url = _scheduler_db_path()
    if url and _is_postgres_url(url):
        return fn_postgres(url)
    return fn_sqlite()


# ---------------------------------------------------------------------------
# Tool 1: schedule_task
# ---------------------------------------------------------------------------


def _schedule_task_sync(task_type: str, target: str, scheduled_at: str, payload: dict) -> dict:
    task_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()
    url = _scheduler_db_path()

    if url and _is_postgres_url(url):
        import psycopg2  # type: ignore[import]

        conn = psycopg2.connect(url)
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO scheduled_tasks (id, task_type, target, scheduled_at, payload, status, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, 'pending', %s, %s)
                    """,
                    (task_id, task_type, target, scheduled_at, json.dumps(payload), now, now),
                )
            conn.commit()
        finally:
            conn.close()
    else:
        conn = _sqlite_conn()
        try:
            conn.execute(
                """
                INSERT INTO scheduled_tasks (id, task_type, target, scheduled_at, payload, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 'pending', ?, ?)
                """,
                (task_id, task_type, target, scheduled_at, json.dumps(payload), now, now),
            )
            conn.commit()
        finally:
            conn.close()

    return {
        "task_id": task_id,
        "task_type": task_type,
        "target": target,
        "scheduled_at": scheduled_at,
        "status": "pending",
    }


class ScheduleTaskTool(MCPTool):
    """Schedule a future task for AgentCore to execute."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="schedule_task",
            description=(
                "Schedule a task to be executed at a future time. "
                "Returns the task ID. "
                "AgentCore polls the task queue and runs due tasks automatically."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "task_type": {
                        "type": "string",
                        "description": "Type of task (e.g. 'send_email', 'send_sms', 'follow_up').",
                    },
                    "target": {
                        "type": "string",
                        "description": "Target identifier (email address, phone number, contact ID, etc.).",
                    },
                    "scheduled_at": {
                        "type": "string",
                        "description": "When to execute the task (ISO 8601 UTC datetime).",
                    },
                    "payload": {
                        "type": "object",
                        "description": "Optional JSON payload passed to the task handler.",
                    },
                },
                "required": ["task_type", "target", "scheduled_at"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        task_type: str = arguments["task_type"]
        target: str = arguments["target"]
        scheduled_at: str = arguments["scheduled_at"]
        payload: dict = arguments.get("payload", {})

        # Validate scheduled_at is parseable
        try:
            datetime.fromisoformat(scheduled_at)
        except ValueError as exc:
            return MCPToolResult(
                success=False, content=None, error=f"Invalid scheduled_at format: {exc}"
            )

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None, partial(_schedule_task_sync, task_type, target, scheduled_at, payload)
            )
            return MCPToolResult(success=True, content=result)
        except Exception as exc:
            logger.error("schedule_task error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 2: list_scheduled_tasks
# ---------------------------------------------------------------------------


def _list_tasks_sync(status_filter: str | None) -> list[dict]:
    url = _scheduler_db_path()

    if url and _is_postgres_url(url):
        import psycopg2  # type: ignore[import]
        import psycopg2.extras

        conn = psycopg2.connect(url)
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                if status_filter:
                    cur.execute(
                        "SELECT * FROM scheduled_tasks WHERE status = %s ORDER BY scheduled_at LIMIT 200",
                        (status_filter,),
                    )
                else:
                    cur.execute("SELECT * FROM scheduled_tasks ORDER BY scheduled_at LIMIT 200")
                return [dict(r) for r in cur.fetchall()]
        finally:
            conn.close()
    else:
        conn = _sqlite_conn()
        try:
            if status_filter:
                rows = conn.execute(
                    "SELECT * FROM scheduled_tasks WHERE status = ? ORDER BY scheduled_at LIMIT 200",
                    (status_filter,),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM scheduled_tasks ORDER BY scheduled_at LIMIT 200"
                ).fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()


class ListScheduledTasksTool(MCPTool):
    """List scheduled tasks, optionally filtered by status."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="list_scheduled_tasks",
            description=(
                "List scheduled tasks from the task queue. "
                "Optionally filter by status. Returns up to 200 tasks."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "enum": sorted(_VALID_STATUSES),
                        "description": "Filter by task status (omit to return all statuses).",
                    }
                },
                "required": [],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        status_filter: str | None = arguments.get("status")
        if status_filter and status_filter not in _VALID_STATUSES:
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Invalid status '{status_filter}'. Must be one of: {', '.join(sorted(_VALID_STATUSES))}",
            )
        try:
            loop = asyncio.get_running_loop()
            tasks = await loop.run_in_executor(None, partial(_list_tasks_sync, status_filter))
            return MCPToolResult(success=True, content={"tasks": tasks, "count": len(tasks)})
        except Exception as exc:
            logger.error("list_scheduled_tasks error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 3: cancel_task
# ---------------------------------------------------------------------------


def _cancel_task_sync(task_id: str) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    url = _scheduler_db_path()

    if url and _is_postgres_url(url):
        import psycopg2  # type: ignore[import]

        conn = psycopg2.connect(url)
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE scheduled_tasks SET status = 'cancelled', updated_at = %s WHERE id = %s AND status = 'pending'",
                    (now, task_id),
                )
                rows_affected = cur.rowcount
            conn.commit()
        finally:
            conn.close()
    else:
        conn = _sqlite_conn()
        try:
            cur = conn.execute(
                "UPDATE scheduled_tasks SET status = 'cancelled', updated_at = ? WHERE id = ? AND status = 'pending'",
                (now, task_id),
            )
            rows_affected = cur.rowcount
            conn.commit()
        finally:
            conn.close()

    if rows_affected == 0:
        raise ValueError(f"Task '{task_id}' not found or is not in 'pending' state.")

    return {"task_id": task_id, "new_status": "cancelled"}


class CancelTaskTool(MCPTool):
    """Cancel a pending scheduled task."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="cancel_task",
            description="Cancel a pending scheduled task by its ID. Only pending tasks can be cancelled.",
            input_schema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "string", "description": "The task ID to cancel."}
                },
                "required": ["task_id"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        task_id: str = arguments["task_id"]
        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(None, partial(_cancel_task_sync, task_id))
            return MCPToolResult(success=True, content=result)
        except ValueError as exc:
            return MCPToolResult(success=False, content=None, error=str(exc))
        except Exception as exc:
            logger.error("cancel_task error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
