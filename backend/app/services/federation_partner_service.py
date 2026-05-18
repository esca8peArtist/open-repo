"""Service layer for federation partner management.

Phase 4 Wave 4 — Partner registration, trust state machine, key rotation,
HTTP signature verification, audit log, and partner lifecycle management.
"""

import base64
import logging
from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.http_signatures import HTTPSignatureUtils
from app.models import Activity, FederationPartner, TrustStatus

logger = logging.getLogger(__name__)

# State machine: valid transitions from each source state.
# pending can move to trusted, untrusted, or revoked.
# trusted can move to untrusted or revoked.
# untrusted can move to trusted or revoked.
# revoked is terminal.
_VALID_TRANSITIONS: dict[str, set[str]] = {
    TrustStatus.PENDING.value: {
        TrustStatus.TRUSTED.value,
        TrustStatus.UNTRUSTED.value,
        TrustStatus.REVOKED.value,
    },
    TrustStatus.TRUSTED.value: {
        TrustStatus.UNTRUSTED.value,
        TrustStatus.REVOKED.value,
    },
    TrustStatus.UNTRUSTED.value: {
        TrustStatus.TRUSTED.value,
        TrustStatus.REVOKED.value,
    },
    TrustStatus.REVOKED.value: set(),  # terminal state
}

# Number of consecutive failed signature verifications before auto-downgrade.
_FAILURE_THRESHOLD = 5

# How long (days) to consider a partner "recently active" for delete safety check.
_RECENT_ACTIVITY_DAYS = 30


class FederationPartnerService:
    """Manages federation partner registration, key exchange, and lifecycle.

    All methods are static and accept an AsyncSession as first argument so they
    compose cleanly with FastAPI's dependency injection.
    """

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    @staticmethod
    async def register_partner(
        db: AsyncSession,
        name: str,
        base_url: str,
        public_key_pem: str,
        key_id: str,
    ) -> FederationPartner:
        """Register a new federation partner with status PENDING.

        Args:
            db: Database session.
            name: Human-readable partner name (must be unique).
            base_url: Partner node base URL (must be unique).
            public_key_pem: PEM-encoded RSA public key supplied by the admin.
            key_id: Key identifier URI (must be unique, e.g. https://node-b.example.com#main-key).

        Returns:
            Newly created FederationPartner with trust_state=PENDING.

        Raises:
            ValueError: If public_key_pem is not a valid RSA public key.
            IntegrityError: Re-raised when name, base_url, or key_id already exists.
        """
        # Validate that the supplied PEM can actually be loaded as a public key.
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.backends import default_backend

            serialization.load_pem_public_key(
                public_key_pem.encode("utf-8"),
                backend=default_backend(),
            )
        except Exception as exc:
            raise ValueError(f"Invalid public key PEM: {exc}") from exc

        partner = FederationPartner(
            name=name,
            base_url=base_url.rstrip("/"),
            public_key_pem=public_key_pem,
            key_id=key_id,
            trust_state=TrustStatus.PENDING,
            last_key_refresh_at=datetime.utcnow(),
        )

        try:
            db.add(partner)
            await db.commit()
            await db.refresh(partner)
        except IntegrityError:
            await db.rollback()
            raise

        logger.info("Registered federation partner %s (id=%s)", name, partner.id)
        return partner

    # ------------------------------------------------------------------
    # Retrieval
    # ------------------------------------------------------------------

    @staticmethod
    async def get_partner(
        db: AsyncSession,
        partner_id: int,
    ) -> FederationPartner:
        """Fetch a single FederationPartner by primary key.

        Args:
            db: Database session.
            partner_id: Partner primary key.

        Returns:
            FederationPartner object.

        Raises:
            KeyError: If partner_id does not exist.
        """
        result = await db.execute(
            select(FederationPartner).where(FederationPartner.id == partner_id)
        )
        partner = result.scalar_one_or_none()
        if partner is None:
            raise KeyError(f"Federation partner {partner_id} not found")
        return partner

    @staticmethod
    async def list_partners(
        db: AsyncSession,
        filter_by_state: Optional[str] = None,
    ) -> List[FederationPartner]:
        """List all federation partners with an optional trust-state filter.

        Args:
            db: Database session.
            filter_by_state: Optional TrustStatus value string to filter on.
                Accepted values: 'pending', 'trusted', 'untrusted', 'revoked'.

        Returns:
            List of FederationPartner objects ordered by created_at descending.

        Raises:
            ValueError: If filter_by_state is not a valid TrustStatus value.
        """
        query = select(FederationPartner).order_by(FederationPartner.created_at.desc())

        if filter_by_state is not None:
            valid_states = {s.value for s in TrustStatus}
            if filter_by_state not in valid_states:
                raise ValueError(
                    f"Invalid filter_by_state '{filter_by_state}'. "
                    f"Must be one of: {', '.join(sorted(valid_states))}"
                )
            query = query.where(FederationPartner.trust_state == filter_by_state)

        result = await db.execute(query)
        return list(result.scalars().all())

    # ------------------------------------------------------------------
    # Trust state machine
    # ------------------------------------------------------------------

    @staticmethod
    async def update_partner_trust_state(
        db: AsyncSession,
        partner_id: int,
        new_state: str,
    ) -> FederationPartner:
        """Transition a partner's trust state with machine validation.

        Valid transitions:
        - pending → trusted | untrusted | revoked
        - trusted → untrusted | revoked
        - untrusted → trusted | revoked
        - revoked → (no transitions — terminal)

        Args:
            db: Database session.
            partner_id: Partner primary key.
            new_state: Target TrustStatus value string.

        Returns:
            Updated FederationPartner.

        Raises:
            KeyError: If partner_id does not exist.
            ValueError: If the transition is invalid or new_state is not recognised.
        """
        valid_states = {s.value for s in TrustStatus}
        if new_state not in valid_states:
            raise ValueError(
                f"Invalid trust state '{new_state}'. "
                f"Must be one of: {', '.join(sorted(valid_states))}"
            )

        partner = await FederationPartnerService.get_partner(db, partner_id)
        current = partner.trust_state.value

        allowed = _VALID_TRANSITIONS.get(current, set())
        if new_state not in allowed:
            raise ValueError(
                f"Invalid state transition: {current} → {new_state}. "
                f"Allowed from '{current}': {sorted(allowed) or 'none (terminal)'}"
            )

        partner.trust_state = TrustStatus(new_state)
        partner.updated_at = datetime.utcnow()
        db.add(partner)
        await db.commit()
        await db.refresh(partner)

        logger.info(
            "Partner %s trust state changed: %s → %s", partner_id, current, new_state
        )
        return partner

    # ------------------------------------------------------------------
    # Key rotation
    # ------------------------------------------------------------------

    @staticmethod
    async def rotate_partner_public_key(
        db: AsyncSession,
        partner_id: int,
        new_key_pem: str,
        new_key_id: str,
    ) -> FederationPartner:
        """Update a partner's public key (manual key rotation).

        Safety check: validates that the new PEM is a valid RSA public key before
        persisting, so a bad key never replaces a working one.

        Args:
            db: Database session.
            partner_id: Partner primary key.
            new_key_pem: PEM-encoded RSA public key (new value).
            new_key_id: New key identifier URI.

        Returns:
            Updated FederationPartner with refreshed key fields.

        Raises:
            KeyError: If partner_id does not exist.
            ValueError: If new_key_pem is not a valid RSA public key.
        """
        # Validate new key before touching the database.
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.backends import default_backend

            serialization.load_pem_public_key(
                new_key_pem.encode("utf-8"),
                backend=default_backend(),
            )
        except Exception as exc:
            raise ValueError(f"Invalid public key PEM: {exc}") from exc

        partner = await FederationPartnerService.get_partner(db, partner_id)
        partner.public_key_pem = new_key_pem
        partner.key_id = new_key_id
        partner.last_key_refresh_at = datetime.utcnow()
        partner.updated_at = datetime.utcnow()

        db.add(partner)
        await db.commit()
        await db.refresh(partner)

        logger.info("Rotated public key for partner %s (new key_id=%s)", partner_id, new_key_id)
        return partner

    # ------------------------------------------------------------------
    # HTTP signature verification
    # ------------------------------------------------------------------

    @staticmethod
    async def verify_http_signature(
        db: AsyncSession,
        signature_header: str,
        request_target: str,
        host: str,
        date: str,
    ) -> Tuple[bool, Optional[str], Optional[FederationPartner]]:
        """Verify an inbound HTTP Signature header (RFC 8017 + W3C ActivityPub).

        Flow:
        1. Parse the Signature header to extract keyId.
        2. Look up the partner by key_id.
        3. Verify the partner is in 'trusted' state.
        4. Reconstruct the signed string from headers.
        5. Verify signature against the partner's stored public key.
        6. On success: update last_verified_at.
        7. On failure: increment failed_signature_count; auto-downgrade after threshold.

        Args:
            db: Database session.
            signature_header: Raw value of the HTTP Signature header.
            request_target: HTTP request target string (e.g. "post /inbox").
            host: Value of the HTTP Host header.
            date: Value of the HTTP Date header.

        Returns:
            Tuple of (valid: bool, error_message: str | None, partner: FederationPartner | None).
            On success: (True, None, <partner>).
            On failure: (False, <reason>, None).
        """
        if not signature_header:
            return False, "Missing Signature header", None

        # --- Parse the Signature header ---
        key_id = _parse_signature_field(signature_header, "keyId")
        if not key_id:
            return False, "Signature header missing keyId field", None

        # --- Look up partner ---
        result = await db.execute(
            select(FederationPartner).where(FederationPartner.key_id == key_id)
        )
        partner = result.scalar_one_or_none()
        if partner is None:
            return False, f"Unknown keyId: {key_id}", None

        # --- Trust check ---
        if partner.trust_state != TrustStatus.TRUSTED:
            return (
                False,
                f"Partner is not trusted (state={partner.trust_state.value})",
                None,
            )

        # --- Verify signature using HTTPSignatureUtils ---
        valid = HTTPSignatureUtils.verify_signature_header(
            signature_header=signature_header,
            public_key_pem=partner.public_key_pem,
            request_target=request_target,
            host=host,
            date=date,
        )

        if valid:
            partner.last_activity_at = datetime.utcnow()
            partner.updated_at = datetime.utcnow()
            db.add(partner)
            await db.commit()
            return True, None, partner

        # --- Handle verification failure ---
        # Increment counter safely even if field starts as None.
        current_failures = (
            int(partner.failed_signature_count)
            if partner.failed_signature_count is not None
            else 0
        )
        new_failures = current_failures + 1
        partner.failed_signature_count = new_failures
        partner.updated_at = datetime.utcnow()

        if new_failures > _FAILURE_THRESHOLD and partner.trust_state == TrustStatus.TRUSTED:
            partner.trust_state = TrustStatus.UNTRUSTED
            logger.warning(
                "Partner %s auto-downgraded to UNTRUSTED after %d signature failures",
                partner.id,
                new_failures,
            )

        db.add(partner)
        await db.commit()

        return False, "Signature verification failed", None

    # ------------------------------------------------------------------
    # Activity log (audit trail)
    # ------------------------------------------------------------------

    @staticmethod
    async def get_activity_log(
        db: AsyncSession,
        partner_id: int,
        limit: int = 100,
    ) -> List[Activity]:
        """Return recent activities linked to a given partner.

        Args:
            db: Database session.
            partner_id: Partner primary key.
            limit: Maximum number of activities to return (default 100).

        Returns:
            List of Activity objects ordered by created_at descending.

        Raises:
            KeyError: If partner_id does not exist.
        """
        # Validate partner exists.
        await FederationPartnerService.get_partner(db, partner_id)

        result = await db.execute(
            select(Activity)
            .where(Activity.partner_id == partner_id)
            .order_by(Activity.created_at.desc())
            .limit(limit)
        )
        return list(result.scalars().all())

    # ------------------------------------------------------------------
    # Hard delete
    # ------------------------------------------------------------------

    @staticmethod
    async def delete_partner(
        db: AsyncSession,
        partner_id: int,
    ) -> None:
        """Hard-delete a partner record.

        Safety constraints:
        - Partner must be in REVOKED state.
        - Partner must have no activities in the last _RECENT_ACTIVITY_DAYS days.

        Args:
            db: Database session.
            partner_id: Partner primary key.

        Raises:
            KeyError: If partner_id does not exist.
            ValueError: If partner is not REVOKED, or has recent activity.
        """
        partner = await FederationPartnerService.get_partner(db, partner_id)

        if partner.trust_state != TrustStatus.REVOKED:
            raise ValueError(
                f"Cannot delete partner with trust_state='{partner.trust_state.value}'. "
                "Partner must be REVOKED before deletion."
            )

        if partner.last_activity_at is not None:
            delta = datetime.utcnow() - partner.last_activity_at
            if delta.days < _RECENT_ACTIVITY_DAYS:
                raise ValueError(
                    f"Cannot delete partner with activity in the last {_RECENT_ACTIVITY_DAYS} days. "
                    f"Last activity was {delta.days} day(s) ago."
                )

        await db.delete(partner)
        await db.commit()
        logger.info("Hard-deleted federation partner %s", partner_id)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _parse_signature_field(signature_header: str, field: str) -> Optional[str]:
    """Extract a named field value from an HTTP Signature header string.

    Handles both quoted values (keyId="...") and unquoted values.

    Args:
        signature_header: Raw Signature header string.
        field: Field name to extract (e.g. "keyId", "algorithm").

    Returns:
        Extracted value string, or None if not found.
    """
    # Search for field= pattern
    search = f"{field}="
    idx = signature_header.find(search)
    if idx == -1:
        return None

    start = idx + len(search)
    if start >= len(signature_header):
        return None

    if signature_header[start] == '"':
        # Quoted value
        end = signature_header.find('"', start + 1)
        if end == -1:
            return None
        return signature_header[start + 1 : end]
    else:
        # Unquoted value (ends at comma or end of string)
        end = signature_header.find(",", start)
        if end == -1:
            return signature_header[start:].strip()
        return signature_header[start:end].strip()
