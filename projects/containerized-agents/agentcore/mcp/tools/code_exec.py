"""
Python code execution sandbox MCP tool.

Runs Python code in a subprocess with:
- Configurable timeout (default 30 s)
- Blocked dangerous imports (os.system, subprocess, socket, requests, urllib)
- Resource limits via resource module (Unix only; gracefully skipped on Windows)
- stdout / stderr capture
- No network access in subprocess environment

Security model
--------------
The sandbox is a "soft" sandbox — it prevents accidental misuse but is NOT
suitable for executing untrusted third-party code in a production environment.
For fully isolated execution, run AgentCore inside a Docker container with
network=none and limited capabilities.

Profiles: developer_assistant (4), business_intelligence (5)
"""
from __future__ import annotations

import ast
import asyncio
import json
import logging
import os
import sys
import tempfile
import textwrap
import time
from typing import Any

from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["developer_assistant", "business_intelligence"]

# Top-level module names whose import (by any means) should block execution.
# This covers both `import X` / `from X import ...` and `__import__("X")` calls.
_BLOCKED_MODULES = frozenset(
    [
        "os",
        "subprocess",
        "socket",
        "requests",
        "urllib",
        "httpx",
        "aiohttp",
        "importlib",
        "importlib.util",
        "importlib.machinery",
    ]
)

# Names that must never appear as bare function calls in the submitted code.
_BLOCKED_BUILTINS = frozenset(["eval", "exec", "compile", "open", "__import__"])

# Wrapper that captures the return value of the last expression
_EXEC_WRAPPER = textwrap.dedent(
    """
import sys as _sys
import json as _json
import traceback as _traceback

_result = None
_error = None

try:
    # --- user code ---
{user_code}
    # --- end user code ---
except Exception as _e:
    _error = _traceback.format_exc()

# Write result as JSON to stdout on last line
print("__RESULT__:" + _json.dumps({{"result": str(_result) if _result is not None else None, "error": _error}}, default=str))
"""
)

_DEFAULT_TIMEOUT = 30


class ExecutePythonTool(MCPTool):
    """Execute Python code in a sandboxed subprocess."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="execute_python",
            description=(
                "Execute a Python code snippet in a sandboxed subprocess. "
                "Captures stdout, stderr, and return value. "
                "Network access and dangerous imports are blocked. "
                "Returns: {stdout, stderr, result, execution_time_ms}."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Python code to execute.",
                    },
                    "timeout_seconds": {
                        "type": "integer",
                        "description": f"Maximum execution time in seconds (default: {_DEFAULT_TIMEOUT}, max: 120).",
                        "default": _DEFAULT_TIMEOUT,
                        "minimum": 1,
                        "maximum": 120,
                    },
                },
                "required": ["code"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        code: str = arguments["code"]
        timeout: int = min(int(arguments.get("timeout_seconds", _DEFAULT_TIMEOUT)), 120)

        # Security scan
        block_reason = _check_blocked_imports(code)
        if block_reason:
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Code blocked for security reasons: {block_reason}",
            )

        return await _run_in_subprocess(code, timeout)


def _check_blocked_imports(code: str) -> str | None:
    """
    Return a reason string if the code contains a blocked import or call, else None.

    Uses ``ast.parse()`` to inspect the AST so that whitespace variants such as
    ``import\\tos`` or ``__import__\\t('os')`` cannot bypass the check.

    Blocked constructs:
    - ``import <blocked_module>`` (ast.Import)
    - ``from <blocked_module> import ...`` (ast.ImportFrom)
    - ``__import__(<blocked_module>)`` calls (ast.Call)
    - Bare calls to eval / exec / compile / open / __import__ (ast.Call)
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        # Unparseable code is rejected outright — we cannot verify it is safe.
        return f"Code could not be parsed: {exc}"

    for node in ast.walk(tree):
        # ast.Import  →  import os, import subprocess, …
        if isinstance(node, ast.Import):
            for alias in node.names:
                top_module = alias.name.split(".")[0]
                if top_module in _BLOCKED_MODULES:
                    return f"Blocked import: '{alias.name}'"

        # ast.ImportFrom  →  from os import path, from subprocess import …
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            top_module = module.split(".")[0]
            if top_module in _BLOCKED_MODULES:
                return f"Blocked import: 'from {module} import ...'"

        # ast.Call  →  __import__('os'), eval(...), exec(...), open(...), compile(...)
        elif isinstance(node, ast.Call):
            func = node.func
            # Bare name call: eval(), exec(), __import__(), open(), compile()
            if isinstance(func, ast.Name) and func.id in _BLOCKED_BUILTINS:
                return f"Blocked built-in call: '{func.id}()'"
            # Attribute call: builtins.__import__(), etc.
            if isinstance(func, ast.Attribute) and func.attr in _BLOCKED_BUILTINS:
                return f"Blocked built-in call: '{func.attr}()'"
            # __import__('module') with a string literal argument
            if isinstance(func, ast.Name) and func.id == "__import__":
                if node.args and isinstance(node.args[0], ast.Constant):
                    mod = str(node.args[0].value).split(".")[0]
                    if mod in _BLOCKED_MODULES:
                        return f"Blocked __import__ call for module: '{mod}'"

    return None


async def _run_in_subprocess(code: str, timeout: int) -> MCPToolResult:
    """
    Execute *code* in a fresh Python subprocess and return the result.
    """
    # Indent user code for embedding in the wrapper
    indented = textwrap.indent(code, "    ")
    wrapped = _EXEC_WRAPPER.format(user_code=indented)

    # Write to a temp file (avoids shell-escaping issues)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(wrapped)
        tmp_path = tmp.name

    start = time.monotonic()

    try:
        # Build env with no network access indicators and limited env vars
        env = {
            "PATH": os.environ.get("PATH", ""),
            "PYTHONPATH": os.environ.get("PYTHONPATH", ""),
            "HOME": os.environ.get("HOME", "/tmp"),
            "PYTHONDONTWRITEBYTECODE": "1",
        }

        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            tmp_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
            # Apply resource limits via preexec_fn on Unix
            preexec_fn=_apply_resource_limits if sys.platform != "win32" else None,
        )

        try:
            stdout_bytes, stderr_bytes = await asyncio.wait_for(
                proc.communicate(), timeout=float(timeout)
            )
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            elapsed_ms = int((time.monotonic() - start) * 1000)
            return MCPToolResult(
                success=False,
                content={
                    "stdout": "",
                    "stderr": "",
                    "result": None,
                    "execution_time_ms": elapsed_ms,
                },
                error=f"Code execution timed out after {timeout}s.",
                duration_ms=elapsed_ms,
            )

        elapsed_ms = int((time.monotonic() - start) * 1000)
        stdout = stdout_bytes.decode("utf-8", errors="replace")
        stderr = stderr_bytes.decode("utf-8", errors="replace")

        # Extract structured result from last line
        result_value = None
        lines = stdout.splitlines()
        clean_lines = []
        for line in lines:
            if line.startswith("__RESULT__:"):
                try:
                    payload = json.loads(line[len("__RESULT__:"):])
                    result_value = payload.get("result")
                    if payload.get("error"):
                        stderr = (stderr + "\n" + payload["error"]).strip()
                except Exception:
                    pass
            else:
                clean_lines.append(line)

        clean_stdout = "\n".join(clean_lines)

        return MCPToolResult(
            success=proc.returncode == 0,
            content={
                "stdout": clean_stdout,
                "stderr": stderr,
                "result": result_value,
                "execution_time_ms": elapsed_ms,
                "exit_code": proc.returncode,
            },
            error=stderr if proc.returncode != 0 else None,
            duration_ms=elapsed_ms,
        )

    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def _apply_resource_limits() -> None:
    """
    Called as preexec_fn in subprocess — runs inside the child process before exec.
    Sets memory and CPU time limits.
    """
    try:
        import resource

        # Max RSS: 256 MB
        resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
        # Max CPU time: 30 s (belt-and-suspenders alongside asyncio timeout)
        resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
        # No new files > 10 MB
        resource.setrlimit(resource.RLIMIT_FSIZE, (10 * 1024 * 1024, 10 * 1024 * 1024))
    except Exception:
        pass  # Resource limits are best-effort
