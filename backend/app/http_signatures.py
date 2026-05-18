"""HTTP Signature generation and verification for ActivityPub."""

import base64
import hashlib
from datetime import datetime
from typing import Dict, Optional, Tuple
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


class HTTPSignatureUtils:
    """Utilities for HTTP signature generation and verification per RFC 8017 + W3C extension."""

    @staticmethod
    def generate_keypair(key_id: str) -> Tuple[str, str]:
        """Generate a 2048-bit RSA keypair.

        Returns:
            Tuple of (private_key_pem, public_key_pem) as strings.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Export private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

        # Export public key
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

        return private_pem, public_pem

    @staticmethod
    def sign_message(message: str, private_key_pem: str) -> str:
        """Sign a message using RSA-SHA256.

        Args:
            message: The message to sign.
            private_key_pem: PEM-encoded private key.

        Returns:
            Base64-encoded signature.
        """
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

        signature = private_key.sign(
            message.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return base64.b64encode(signature).decode('utf-8')

    @staticmethod
    def verify_signature(message: str, signature_b64: str, public_key_pem: str) -> bool:
        """Verify a message signature using RSA-SHA256.

        Args:
            message: The signed message.
            signature_b64: Base64-encoded signature.
            public_key_pem: PEM-encoded public key.

        Returns:
            True if signature is valid, False otherwise.
        """
        try:
            public_key = serialization.load_pem_public_key(
                public_key_pem.encode('utf-8'),
                backend=default_backend()
            )

            signature_bytes = base64.b64decode(signature_b64)

            public_key.verify(
                signature_bytes,
                message.encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA256()
            )

            return True
        except Exception:
            return False

    @staticmethod
    def build_signature_header(
        key_id: str,
        private_key_pem: str,
        request_target: str,
        host: str,
        date: str,
        body: str = "",
    ) -> str:
        """Build an HTTP Signature header for outgoing activity.

        Per RFC 8017 + W3C extension.

        Args:
            key_id: The key ID (e.g., "https://example.com/actor#main-key").
            private_key_pem: PEM-encoded private key.
            request_target: HTTP request target (e.g., "post /inbox").
            host: HTTP Host header value.
            date: HTTP Date header (RFC 7231 format).
            body: HTTP request body (for Digest calculation, optional).

        Returns:
            Signature header value: 'keyId="...",algorithm="rsa-sha256",headers="...",signature="..."'
        """
        # Build the signing string
        # Headers to sign: (request-target), host, date
        headers_to_sign = ["(request-target)", "host", "date"]

        signing_parts = [
            f"(request-target): {request_target}",
            f"host: {host}",
            f"date: {date}",
        ]

        signing_string = "\n".join(signing_parts)

        # Sign the string
        signature = HTTPSignatureUtils.sign_message(signing_string, private_key_pem)

        # Build the header
        headers_str = " ".join(headers_to_sign)
        signature_header = (
            f'keyId="{key_id}",'
            f'algorithm="rsa-sha256",'
            f'headers="{headers_str}",'
            f'signature="{signature}"'
        )

        return signature_header

    @staticmethod
    def verify_signature_header(
        signature_header: str,
        public_key_pem: str,
        request_target: str,
        host: str,
        date: str,
    ) -> bool:
        """Verify an HTTP Signature header from an incoming request.

        Args:
            signature_header: The Signature header value.
            public_key_pem: PEM-encoded public key of the sender.
            request_target: HTTP request target (e.g., "post /inbox").
            host: HTTP Host header value.
            date: HTTP Date header.

        Returns:
            True if signature is valid, False otherwise.
        """
        try:
            # Parse the Signature header
            # Format: keyId="...",algorithm="rsa-sha256",headers="...",signature="..."
            parts = {}
            i = 0
            while i < len(signature_header):
                # Find key
                eq_idx = signature_header.find('=', i)
                if eq_idx == -1:
                    break

                key = signature_header[i:eq_idx].strip()

                # Find value (quoted)
                if signature_header[eq_idx + 1] == '"':
                    # Find closing quote
                    start = eq_idx + 2
                    end = start
                    while end < len(signature_header) and signature_header[end] != '"':
                        end += 1
                    value = signature_header[start:end]
                    parts[key] = value

                    # Move past the closing quote and comma
                    i = end + 1
                    if i < len(signature_header) and signature_header[i] == ',':
                        i += 1
                else:
                    break

            # Extract components
            headers_str = parts.get("headers", "")
            signature_b64 = parts.get("signature", "")

            # Parse headers list
            headers_to_verify = [h.strip() for h in headers_str.split()]

            # Build the signing string in the same order
            signing_parts = []
            for header in headers_to_verify:
                if header == "(request-target)":
                    signing_parts.append(f"(request-target): {request_target}")
                elif header == "host":
                    signing_parts.append(f"host: {host}")
                elif header == "date":
                    signing_parts.append(f"date: {date}")

            signing_string = "\n".join(signing_parts)

            # Verify
            return HTTPSignatureUtils.verify_signature(signing_string, signature_b64, public_key_pem)

        except Exception:
            return False


    @staticmethod
    def sign_request(
        method: str,
        url: str,
        private_key_pem: str,
        key_id: str,
        host: Optional[str] = None,
        date: Optional[str] = None,
    ) -> Dict[str, str]:
        """Sign an outbound HTTP request and return headers to include.

        Builds the canonical signing string from ``(request-target)``,
        ``host``, and ``date``, signs it with the supplied private key, and
        returns a dict of HTTP headers that must be attached to the outbound
        request:

        - ``Signature`` — the full Signature header value
        - ``Date``       — RFC 7231-formatted date used in the signature
        - ``Host``       — host extracted from *url* (or the override)

        Args:
            method: HTTP method in any case (e.g. ``"POST"``).
            url: Full URL of the target endpoint (e.g.
                ``"https://node-b.example.com/inbox"``).
            private_key_pem: PEM-encoded RSA private key of the local node.
            key_id: Key identifier URI (e.g.
                ``"https://node-a.example.com#main-key"``).
            host: Override for the ``Host`` header.  Defaults to the host
                extracted from *url*.
            date: Override for the ``Date`` header (RFC 7231 format).
                Defaults to :func:`get_rfc7231_date`.

        Returns:
            Dict of HTTP headers to merge into the outbound request.
        """
        from urllib.parse import urlparse

        parsed = urlparse(url)
        request_host = host or parsed.netloc
        request_date = date or get_rfc7231_date()
        path = parsed.path or "/"
        if parsed.query:
            path = f"{path}?{parsed.query}"
        request_target = f"{method.lower()} {path}"

        signature_header = HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=private_key_pem,
            request_target=request_target,
            host=request_host,
            date=request_date,
        )

        return {
            "Signature": signature_header,
            "Date": request_date,
            "Host": request_host,
        }


def get_rfc7231_date() -> str:
    """Get current date in RFC 7231 format (HTTP Date header)."""
    from email.utils import formatdate
    return formatdate(timeval=None, localtime=False, usegmt=True)
