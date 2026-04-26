"""
Filesystem MCP tools — read-only access to allowed directories.

Security
--------
- Only reads; no writes, renames, deletes, or permission changes.
- Access is restricted to an allowlist of directory prefixes.
  Defaults: /data/ and /workspace/.  Override via FILESYSTEM_ALLOWED_PATHS
  (colon-separated list of absolute path prefixes).
- Path traversal (../ sequences, symlinks outside the allowed tree) is blocked.

Tools
-----
read_file       — return file contents as a string
list_directory  — list entries in a directory
search_files    — find files matching a glob pattern

Profiles: developer_assistant (4)
"""
from __future__ import annotations

import asyncio
import fnmatch
import logging
import os
from pathlib import Path
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["developer_assistant"]
_DEFAULT_ALLOWED_PATHS = ["/data", "/workspace"]
_MAX_FILE_SIZE_BYTES = 1 * 1024 * 1024  # 1 MB read limit per file
_MAX_SEARCH_RESULTS = 200


def _allowed_prefixes() -> list[str]:
    env = get_settings().filesystem_allowed_paths
    if env:
        return [p.rstrip("/") for p in env.split(":") if p.strip()]
    return _DEFAULT_ALLOWED_PATHS


def _is_path_allowed(path: str) -> bool:
    """Return True if *path* resolves within one of the allowed prefixes."""
    try:
        resolved = str(Path(path).resolve())
    except Exception:
        return False
    for prefix in _allowed_prefixes():
        if resolved.startswith(prefix + "/") or resolved == prefix:
            return True
    return False


def _safe_resolve(raw_path: str) -> tuple[str, str | None]:
    """
    Resolve *raw_path* and validate it is within the allowed tree.

    Returns (resolved_path, None) on success or ("", error_message) on failure.
    """
    if not raw_path:
        return "", "Path must not be empty."
    try:
        resolved = str(Path(raw_path).resolve())
    except Exception as exc:
        return "", f"Cannot resolve path: {exc}"
    if not _is_path_allowed(resolved):
        allowed = ", ".join(_allowed_prefixes())
        return "", (
            f"Access denied: '{resolved}' is outside the allowed paths ({allowed}). "
            "Only /data/ and /workspace/ are accessible by default."
        )
    return resolved, None


# ---------------------------------------------------------------------------
# Tool 1: read_file
# ---------------------------------------------------------------------------


class ReadFileTool(MCPTool):
    """Read the contents of a file (read-only, restricted to allowed paths)."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="read_file",
            description=(
                "Read the text contents of a file. "
                "Only files within /data/ and /workspace/ are accessible. "
                "Maximum file size: 1 MB."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path to the file to read.",
                    }
                },
                "required": ["path"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        raw_path: str = arguments["path"]
        resolved, err = _safe_resolve(raw_path)
        if err:
            return MCPToolResult(success=False, content=None, error=err)

        if not os.path.exists(resolved):
            return MCPToolResult(success=False, content=None, error=f"File not found: '{resolved}'")
        if os.path.isdir(resolved):
            return MCPToolResult(
                success=False, content=None, error=f"'{resolved}' is a directory, not a file."
            )

        size = os.path.getsize(resolved)
        if size > _MAX_FILE_SIZE_BYTES:
            return MCPToolResult(
                success=False,
                content=None,
                error=f"File too large ({size:,} bytes). Maximum is {_MAX_FILE_SIZE_BYTES:,} bytes.",
            )

        try:
            loop = asyncio.get_running_loop()
            content = await loop.run_in_executor(None, _read_file_sync, resolved)
            return MCPToolResult(
                success=True,
                content={"path": resolved, "content": content, "size_bytes": size},
            )
        except Exception as exc:
            logger.error("read_file error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


def _read_file_sync(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Tool 2: list_directory
# ---------------------------------------------------------------------------


class ListDirectoryTool(MCPTool):
    """List the contents of a directory (read-only)."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="list_directory",
            description=(
                "List files and subdirectories in a directory. "
                "Only directories within /data/ and /workspace/ are accessible. "
                "Returns name, type (file/directory), and size for each entry."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path of the directory to list.",
                    }
                },
                "required": ["path"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        raw_path: str = arguments["path"]
        resolved, err = _safe_resolve(raw_path)
        if err:
            return MCPToolResult(success=False, content=None, error=err)

        if not os.path.exists(resolved):
            return MCPToolResult(success=False, content=None, error=f"Directory not found: '{resolved}'")
        if not os.path.isdir(resolved):
            return MCPToolResult(
                success=False, content=None, error=f"'{resolved}' is not a directory."
            )

        try:
            loop = asyncio.get_running_loop()
            entries = await loop.run_in_executor(None, _list_dir_sync, resolved)
            return MCPToolResult(
                success=True, content={"path": resolved, "entries": entries, "count": len(entries)}
            )
        except Exception as exc:
            logger.error("list_directory error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


def _list_dir_sync(path: str) -> list[dict]:
    entries = []
    try:
        for entry in sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name)):
            try:
                stat = entry.stat(follow_symlinks=False)
                entries.append(
                    {
                        "name": entry.name,
                        "type": "directory" if entry.is_dir() else "file",
                        "size_bytes": stat.st_size if entry.is_file() else None,
                    }
                )
            except OSError:
                entries.append({"name": entry.name, "type": "unknown", "size_bytes": None})
    except PermissionError as exc:
        raise PermissionError(f"Permission denied: {path}") from exc
    return entries


# ---------------------------------------------------------------------------
# Tool 3: search_files
# ---------------------------------------------------------------------------


class SearchFilesTool(MCPTool):
    """Search for files matching a glob pattern within an allowed directory."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="search_files",
            description=(
                "Search for files matching a glob pattern within an allowed directory. "
                "Returns up to 200 matching file paths. "
                "Example patterns: '*.py', '**/*.json', 'report_*.pdf'."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Glob pattern to match filenames (e.g. '*.py', 'report*.pdf').",
                    },
                    "directory": {
                        "type": "string",
                        "description": "Directory to search in (default: /data).",
                        "default": "/data",
                    },
                },
                "required": ["pattern"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        pattern: str = arguments["pattern"]
        directory: str = arguments.get("directory", "/data")

        resolved, err = _safe_resolve(directory)
        if err:
            return MCPToolResult(success=False, content=None, error=err)

        if not os.path.isdir(resolved):
            return MCPToolResult(
                success=False, content=None, error=f"'{resolved}' is not a directory."
            )

        try:
            loop = asyncio.get_running_loop()
            matches = await loop.run_in_executor(None, _search_sync, resolved, pattern)
            return MCPToolResult(
                success=True,
                content={"matches": matches, "count": len(matches), "pattern": pattern},
            )
        except Exception as exc:
            logger.error("search_files error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


def _search_sync(directory: str, pattern: str) -> list[str]:
    matches: list[str] = []
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                full_path = os.path.join(root, filename)
                if _is_path_allowed(full_path):
                    matches.append(full_path)
                    if len(matches) >= _MAX_SEARCH_RESULTS:
                        return matches
    return matches
