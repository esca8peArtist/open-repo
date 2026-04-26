"""
Database MCP tool — read-only SQL query executor.

Supports: SQLite (local files), PostgreSQL, MySQL.

Security controls
-----------------
- Only SELECT statements are permitted; any query containing DML/DDL keywords
  is rejected before execution.
- Results are capped at MAX_ROWS (1 000) to prevent memory exhaustion.
- Connection strings are supplied via environment variables so they never
  appear in prompts/logs.

Config (env vars)
-----------------
DB_SQLITE_PATH      — path to a SQLite file (e.g. /data/mydb.db)
DB_POSTGRES_URL     — PostgreSQL DSN (e.g. postgresql://user:pass@host/db)
DB_MYSQL_URL        — MySQL DSN (e.g. mysql+pymysql://user:pass@host/db)

Profiles: business_intelligence (5)
"""
from __future__ import annotations

import asyncio
import logging
import re
from functools import partial
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

MAX_ROWS = 1000

# Patterns that must not appear in a read-only query
_BLOCKED_PATTERNS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|REPLACE|MERGE|EXEC|EXECUTE|GRANT|REVOKE|ATTACH|DETACH|UNION)\b",
    re.IGNORECASE,
)

_PROFILES = ["business_intelligence"]


def _is_safe_query(sql: str) -> bool:
    """Return True only if the query is a pure SELECT statement."""
    stripped = sql.strip()
    if not stripped.upper().startswith("SELECT"):
        return False
    if _BLOCKED_PATTERNS.search(stripped):
        return False
    return True


def _execute_sqlite(path: str, sql: str, params: list) -> list[dict]:
    import sqlite3

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.execute(sql, params)
        rows = cursor.fetchmany(MAX_ROWS)
        return [dict(r) for r in rows]
    finally:
        conn.close()


def _execute_postgres(dsn: str, sql: str, params: list) -> list[dict]:
    import psycopg2  # type: ignore[import]
    import psycopg2.extras

    conn = psycopg2.connect(dsn)
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, params)
            rows = cur.fetchmany(MAX_ROWS)
            return [dict(r) for r in rows]
    finally:
        conn.close()


def _execute_mysql(dsn: str, sql: str, params: list) -> list[dict]:
    import pymysql  # type: ignore[import]
    import pymysql.cursors

    # Parse simple mysql+pymysql://user:pass@host/db DSN
    import re as _re

    m = _re.match(r"mysql\+pymysql://([^:]+):([^@]+)@([^/]+)/(.+)", dsn)
    if not m:
        raise ValueError(f"Cannot parse MySQL DSN: {dsn!r}")
    user, password, host, database = m.groups()

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchmany(MAX_ROWS)
    finally:
        conn.close()


class QueryDatabaseTool(MCPTool):
    """Execute a read-only SELECT query against a configured database."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="query_database",
            description=(
                "Execute a read-only SQL SELECT query against a local database. "
                "Supports SQLite, PostgreSQL, and MySQL. "
                "Returns results as a list of row objects. "
                "Maximum 1,000 rows returned. Only SELECT statements are permitted."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "The SQL SELECT statement to execute.",
                    },
                    "database_name": {
                        "type": "string",
                        "description": (
                            "Which database to query: 'sqlite', 'postgres', or 'mysql'. "
                            "Defaults to the first configured database."
                        ),
                    },
                    "params": {
                        "type": "array",
                        "items": {},
                        "description": "Optional list of query parameters (for parameterised queries).",
                    },
                },
                "required": ["sql"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        sql: str = arguments["sql"]
        db_name: str = arguments.get("database_name", "").lower()
        params: list = arguments.get("params", [])

        # Security: read-only enforcement
        if not _is_safe_query(sql):
            return MCPToolResult(
                success=False,
                content=None,
                error=(
                    "Only SELECT statements are permitted. "
                    "INSERT, UPDATE, DELETE, DROP, and other DML/DDL statements are blocked."
                ),
            )

        # Determine which backend to use
        _s = get_settings()
        sqlite_path = _s.db_sqlite_path
        postgres_url = _s.db_postgres_url
        mysql_url = _s.db_mysql_url

        executor_fn: Any = None

        if db_name == "sqlite" or (not db_name and sqlite_path):
            if not sqlite_path:
                return MCPToolResult(success=False, content=None, error="DB_SQLITE_PATH not configured.")
            executor_fn = partial(_execute_sqlite, sqlite_path, sql, params)
        elif db_name == "postgres" or (not db_name and postgres_url):
            if not postgres_url:
                return MCPToolResult(success=False, content=None, error="DB_POSTGRES_URL not configured.")
            executor_fn = partial(_execute_postgres, postgres_url, sql, params)
        elif db_name == "mysql" or (not db_name and mysql_url):
            if not mysql_url:
                return MCPToolResult(success=False, content=None, error="DB_MYSQL_URL not configured.")
            executor_fn = partial(_execute_mysql, mysql_url, sql, params)
        else:
            return MCPToolResult(
                success=False,
                content=None,
                error="No database configured. Set DB_SQLITE_PATH, DB_POSTGRES_URL, or DB_MYSQL_URL.",
            )

        try:
            loop = asyncio.get_running_loop()
            rows = await loop.run_in_executor(None, executor_fn)
            return MCPToolResult(
                success=True,
                content={"rows": rows, "count": len(rows), "truncated": len(rows) == MAX_ROWS},
            )
        except Exception as exc:
            logger.error("query_database error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
