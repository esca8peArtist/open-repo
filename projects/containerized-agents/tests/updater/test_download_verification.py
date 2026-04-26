"""
Update system tests: SHA256 verification during component download.
"""
from __future__ import annotations

import hashlib
import io
import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.updater.installer import download_component


def _sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class TestDownloadVerification:
    """SHA256 verification tests for download_component."""

    @pytest.mark.asyncio
    async def test_correct_sha256_returns_true(self, tmp_path):
        """download_component must return True when SHA256 matches."""
        payload = b"agentcore image binary data" * 100
        expected_sha = _sha256_of(payload)
        dest = tmp_path / "agentcore.tar.gz"

        # Mock httpx streaming response
        mock_response = AsyncMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.headers = {"content-length": str(len(payload))}

        async def _aiter_bytes(chunk_size=1048576):
            yield payload

        mock_response.aiter_bytes = _aiter_bytes

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/agentcore.tar.gz",
                expected_sha256=expected_sha,
                dest=dest,
            )

        assert result is True
        assert dest.exists()
        assert dest.read_bytes() == payload

    @pytest.mark.asyncio
    async def test_wrong_sha256_returns_false(self, tmp_path):
        """download_component must return False when SHA256 does not match."""
        payload = b"correct payload data"
        wrong_sha = "a" * 64  # all-zeroes-like wrong hash
        dest = tmp_path / "bad.tar.gz"

        mock_response = AsyncMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.headers = {"content-length": str(len(payload))}

        async def _aiter_bytes(chunk_size=1048576):
            yield payload

        mock_response.aiter_bytes = _aiter_bytes

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/tampered.tar.gz",
                expected_sha256=wrong_sha,
                dest=dest,
            )

        assert result is False
        # Temp file must be cleaned up on mismatch
        assert not dest.exists()

    @pytest.mark.asyncio
    async def test_network_error_returns_false(self, tmp_path):
        """download_component must return False when network request fails."""
        dest = tmp_path / "never.tar.gz"

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(side_effect=Exception("Network unreachable"))
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://unreachable.example.com/file.tar.gz",
                expected_sha256="a" * 64,
                dest=dest,
            )

        assert result is False
        assert not dest.exists()

    @pytest.mark.asyncio
    async def test_http_error_status_returns_false(self, tmp_path):
        """HTTP 404 / 500 must cause download_component to return False."""
        dest = tmp_path / "notfound.tar.gz"

        import httpx

        mock_response = AsyncMock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found",
            request=MagicMock(),
            response=MagicMock(status_code=404),
        )
        mock_response.headers = {}

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/missing.tar.gz",
                expected_sha256="a" * 64,
                dest=dest,
            )

        assert result is False

    @pytest.mark.asyncio
    async def test_dest_directory_created_if_missing(self, tmp_path):
        """download_component must create parent directories if they don't exist."""
        payload = b"binary payload"
        expected_sha = _sha256_of(payload)
        # nested directory that doesn't exist yet
        dest = tmp_path / "nested" / "dir" / "agentcore.tar.gz"

        mock_response = AsyncMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.headers = {"content-length": str(len(payload))}

        async def _aiter_bytes(chunk_size=1048576):
            yield payload

        mock_response.aiter_bytes = _aiter_bytes

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/agentcore.tar.gz",
                expected_sha256=expected_sha,
                dest=dest,
            )

        assert result is True
        assert dest.exists()

    @pytest.mark.asyncio
    async def test_sha256_case_insensitive(self, tmp_path):
        """SHA256 comparison must be case-insensitive (uppercase hex must match)."""
        payload = b"test payload for case insensitivity"
        expected_sha = _sha256_of(payload).upper()  # uppercase
        dest = tmp_path / "upper.tar.gz"

        mock_response = AsyncMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.headers = {"content-length": str(len(payload))}

        async def _aiter_bytes(chunk_size=1048576):
            yield payload

        mock_response.aiter_bytes = _aiter_bytes

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/file.tar.gz",
                expected_sha256=expected_sha,
                dest=dest,
            )

        assert result is True

    @pytest.mark.asyncio
    async def test_chunked_download_sha256_correct(self, tmp_path):
        """SHA256 must be computed correctly across multiple chunks."""
        chunk1 = b"first chunk of data " * 50
        chunk2 = b"second chunk of data " * 50
        payload = chunk1 + chunk2
        expected_sha = _sha256_of(payload)
        dest = tmp_path / "chunked.tar.gz"

        mock_response = AsyncMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.headers = {"content-length": str(len(payload))}

        async def _aiter_bytes(chunk_size=1048576):
            yield chunk1
            yield chunk2

        mock_response.aiter_bytes = _aiter_bytes

        mock_stream_ctx = AsyncMock()
        mock_stream_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_stream_ctx.__aexit__ = AsyncMock(return_value=False)

        mock_client = MagicMock()
        mock_client.stream.return_value = mock_stream_ctx

        mock_client_ctx = AsyncMock()
        mock_client_ctx.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client_ctx.__aexit__ = AsyncMock(return_value=False)

        with patch("agentcore.updater.installer.httpx.AsyncClient", return_value=mock_client_ctx):
            result = await download_component(
                url="https://example.com/chunked.tar.gz",
                expected_sha256=expected_sha,
                dest=dest,
            )

        assert result is True
        assert dest.read_bytes() == payload
