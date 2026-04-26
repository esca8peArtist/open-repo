"""Service for logging and querying federation conflicts.

Wave 4 Phase 4: Conflict logging + admin dashboard for federation monitoring.
Tracks signature verification failures, key issues, and trust failures.
"""

import logging
from datetime import datetime
from typing import Optional, Dict, List, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func

from app.models import (
    FederationConflict,
    ConflictType,
    ConflictResolutionAction,
    ConflictStatus,
    FederationPartner,
    Activity,
)

logger = logging.getLogger(__name__)


class FederationConflictService:
    """Service for logging and querying federation conflicts."""

    @staticmethod
    async def log_conflict(
        db: AsyncSession,
        partner_id: int,
        conflict_type: ConflictType,
        error_message: Optional[str] = None,
        activity_id: Optional[int] = None,
    ) -> FederationConflict:
        """Log a federation conflict.

        Args:
            db: Database session
            partner_id: ID of the federation partner
            conflict_type: Type of conflict (signature_mismatch | key_expired | key_revoked | trust_failure)
            error_message: Optional error details
            activity_id: Optional activity ID associated with conflict

        Returns:
            Created FederationConflict record

        Raises:
            ValueError: If partner_id doesn't exist
        """
        # Verify partner exists
        partner_result = await db.execute(
            select(FederationPartner).where(FederationPartner.id == partner_id)
        )
        partner = partner_result.scalar_one_or_none()
        if not partner:
            raise ValueError(f"Federation partner with id {partner_id} not found")

        conflict = FederationConflict(
            partner_id=partner_id,
            activity_id=activity_id,
            conflict_type=conflict_type,
            status=ConflictStatus.ACTIVE,
            error_message=error_message,
            detected_at=datetime.utcnow(),
        )

        db.add(conflict)
        await db.flush()

        logger.warning(
            f"Federation conflict logged: partner_id={partner_id}, type={conflict_type.value}, "
            f"activity_id={activity_id}, error={error_message}"
        )

        return conflict

    @staticmethod
    async def resolve_conflict(
        db: AsyncSession,
        conflict_id: int,
        resolution_action: ConflictResolutionAction,
        resolved_by: Optional[str] = None,
        resolution_notes: Optional[str] = None,
    ) -> FederationConflict:
        """Mark a conflict as resolved.

        Args:
            db: Database session
            conflict_id: ID of conflict to resolve
            resolution_action: Action taken (auto_downgrade | manual_review | ignore)
            resolved_by: Admin user ID or system identifier
            resolution_notes: Notes on resolution

        Returns:
            Updated FederationConflict record

        Raises:
            ValueError: If conflict_id doesn't exist
        """
        result = await db.execute(
            select(FederationConflict).where(FederationConflict.id == conflict_id)
        )
        conflict = result.scalar_one_or_none()
        if not conflict:
            raise ValueError(f"Conflict with id {conflict_id} not found")

        conflict.status = ConflictStatus.RESOLVED
        conflict.resolution_action = resolution_action
        conflict.resolved_by = resolved_by
        conflict.resolution_notes = resolution_notes
        conflict.resolved_at = datetime.utcnow()

        await db.flush()

        logger.info(
            f"Federation conflict resolved: conflict_id={conflict_id}, "
            f"action={resolution_action.value}, resolved_by={resolved_by}"
        )

        return conflict

    @staticmethod
    async def get_active_conflicts(
        db: AsyncSession,
        partner_id: Optional[int] = None,
        conflict_type: Optional[ConflictType] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Get active (unresolved) conflicts with optional filtering.

        Args:
            db: Database session
            partner_id: Optional filter by partner
            conflict_type: Optional filter by conflict type
            limit: Max results to return

        Returns:
            List of conflict records as dicts
        """
        query = select(FederationConflict).where(
            FederationConflict.status == ConflictStatus.ACTIVE
        )

        if partner_id:
            query = query.where(FederationConflict.partner_id == partner_id)

        if conflict_type:
            query = query.where(FederationConflict.conflict_type == conflict_type)

        query = query.order_by(FederationConflict.detected_at.desc()).limit(limit)

        result = await db.execute(query)
        conflicts = result.scalars().all()

        return [
            {
                "id": c.id,
                "partner_id": c.partner_id,
                "activity_id": c.activity_id,
                "conflict_type": c.conflict_type.value,
                "status": c.status.value,
                "error_message": c.error_message,
                "detected_at": c.detected_at.isoformat() if c.detected_at else None,
            }
            for c in conflicts
        ]

    @staticmethod
    async def get_resolved_conflicts(
        db: AsyncSession,
        partner_id: Optional[int] = None,
        conflict_type: Optional[ConflictType] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Get resolved conflicts with optional filtering.

        Args:
            db: Database session
            partner_id: Optional filter by partner
            conflict_type: Optional filter by conflict type
            limit: Max results to return

        Returns:
            List of conflict records as dicts
        """
        query = select(FederationConflict).where(
            FederationConflict.status == ConflictStatus.RESOLVED
        )

        if partner_id:
            query = query.where(FederationConflict.partner_id == partner_id)

        if conflict_type:
            query = query.where(FederationConflict.conflict_type == conflict_type)

        query = query.order_by(FederationConflict.resolved_at.desc()).limit(limit)

        result = await db.execute(query)
        conflicts = result.scalars().all()

        return [
            {
                "id": c.id,
                "partner_id": c.partner_id,
                "activity_id": c.activity_id,
                "conflict_type": c.conflict_type.value,
                "status": c.status.value,
                "resolution_action": c.resolution_action.value if c.resolution_action else None,
                "resolved_by": c.resolved_by,
                "resolution_notes": c.resolution_notes,
                "detected_at": c.detected_at.isoformat() if c.detected_at else None,
                "resolved_at": c.resolved_at.isoformat() if c.resolved_at else None,
            }
            for c in conflicts
        ]

    @staticmethod
    async def get_all_conflicts(
        db: AsyncSession,
        partner_id: Optional[int] = None,
        conflict_type: Optional[ConflictType] = None,
        status: Optional[str] = None,  # "active" | "resolved" | "all"
        limit: int = 100,
    ) -> Dict[str, Any]:
        """Get all conflicts (active or resolved) with filtering.

        Args:
            db: Database session
            partner_id: Optional filter by partner
            conflict_type: Optional filter by conflict type
            status: Optional filter by status ("active" | "resolved" | "all")
            limit: Max results to return

        Returns:
            Dict with conflicts list and total count
        """
        query = select(FederationConflict)

        # Status filter
        if status == "active":
            query = query.where(FederationConflict.status == ConflictStatus.ACTIVE)
        elif status == "resolved":
            query = query.where(FederationConflict.status == ConflictStatus.RESOLVED)
        # "all" returns no status filter

        # Partner filter
        if partner_id:
            query = query.where(FederationConflict.partner_id == partner_id)

        # Type filter
        if conflict_type:
            query = query.where(FederationConflict.conflict_type == conflict_type)

        # Get total count before limit
        count_result = await db.execute(select(func.count(FederationConflict.id)).select_from(query.froms[0]).where(query.whereclause))
        total = count_result.scalar() or 0

        # Order and limit
        query = query.order_by(FederationConflict.detected_at.desc()).limit(limit)

        result = await db.execute(query)
        conflicts = result.scalars().all()

        conflict_list = [
            {
                "id": c.id,
                "partner_id": c.partner_id,
                "activity_id": c.activity_id,
                "conflict_type": c.conflict_type.value,
                "status": c.status.value,
                "error_message": c.error_message,
                "resolution_action": c.resolution_action.value if c.resolution_action else None,
                "resolved_by": c.resolved_by,
                "resolution_notes": c.resolution_notes,
                "detected_at": c.detected_at.isoformat() if c.detected_at else None,
                "resolved_at": c.resolved_at.isoformat() if c.resolved_at else None,
            }
            for c in conflicts
        ]

        return {
            "conflicts": conflict_list,
            "total": total,
            "limit": limit,
        }

    @staticmethod
    async def get_partner_conflict_summary(
        db: AsyncSession,
        partner_id: int,
    ) -> Dict[str, Any]:
        """Get conflict summary for a specific partner.

        Args:
            db: Database session
            partner_id: ID of the federation partner

        Returns:
            Dict with active/resolved conflict counts by type
        """
        # Get partner
        partner_result = await db.execute(
            select(FederationPartner).where(FederationPartner.id == partner_id)
        )
        partner = partner_result.scalar_one_or_none()
        if not partner:
            raise ValueError(f"Federation partner with id {partner_id} not found")

        # Get active conflicts by type
        active_result = await db.execute(
            select(FederationConflict.conflict_type, func.count(FederationConflict.id))
            .where(
                and_(
                    FederationConflict.partner_id == partner_id,
                    FederationConflict.status == ConflictStatus.ACTIVE,
                )
            )
            .group_by(FederationConflict.conflict_type)
        )
        active_by_type = dict(active_result.all()) or {}

        # Get resolved conflicts by type
        resolved_result = await db.execute(
            select(FederationConflict.conflict_type, func.count(FederationConflict.id))
            .where(
                and_(
                    FederationConflict.partner_id == partner_id,
                    FederationConflict.status == ConflictStatus.RESOLVED,
                )
            )
            .group_by(FederationConflict.conflict_type)
        )
        resolved_by_type = dict(resolved_result.all()) or {}

        # Get total counts
        total_active = await db.execute(
            select(func.count(FederationConflict.id)).where(
                and_(
                    FederationConflict.partner_id == partner_id,
                    FederationConflict.status == ConflictStatus.ACTIVE,
                )
            )
        )
        total_active_count = total_active.scalar() or 0

        total_resolved = await db.execute(
            select(func.count(FederationConflict.id)).where(
                and_(
                    FederationConflict.partner_id == partner_id,
                    FederationConflict.status == ConflictStatus.RESOLVED,
                )
            )
        )
        total_resolved_count = total_resolved.scalar() or 0

        return {
            "partner_id": partner_id,
            "partner_name": partner.name,
            "partner_url": partner.base_url,
            "active_conflicts": {
                "total": total_active_count,
                "by_type": {
                    conflict_type.value: count
                    for conflict_type, count in active_by_type.items()
                },
            },
            "resolved_conflicts": {
                "total": total_resolved_count,
                "by_type": {
                    conflict_type.value: count
                    for conflict_type, count in resolved_by_type.items()
                },
            },
        }
