"""Service for managing endorsements."""

from typing import Optional, List, Dict, Any
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Endorsement, EndorsementType


class EndorsementService:
    """Service for endorsement CRUD and aggregation operations."""

    @staticmethod
    async def create_endorsement(
        db: AsyncSession,
        item_cid: str,
        user_id: str,
        endorsement_type: str,
    ) -> Endorsement:
        """Create or update an endorsement for a user on an item.

        If the user has already endorsed this item, update their endorsement.
        """
        # Check if user already has an endorsement for this item
        result = await db.execute(
            select(Endorsement).where(
                (Endorsement.item_cid == item_cid) & (Endorsement.user_id == user_id)
            )
        )
        existing = result.scalar_one_or_none()

        if existing:
            # Update existing endorsement
            existing.endorsement_type = EndorsementType(endorsement_type)
            db.add(existing)
        else:
            # Create new endorsement
            endorsement = Endorsement(
                item_cid=item_cid,
                user_id=user_id,
                endorsement_type=EndorsementType(endorsement_type),
            )
            db.add(endorsement)

        await db.commit()
        await db.refresh(existing if existing else endorsement)
        return existing if existing else endorsement

    @staticmethod
    async def delete_endorsement(
        db: AsyncSession,
        item_cid: str,
        user_id: str,
    ) -> bool:
        """Delete a user's endorsement for an item.

        Returns True if an endorsement was deleted, False if none existed.
        """
        result = await db.execute(
            select(Endorsement).where(
                (Endorsement.item_cid == item_cid) & (Endorsement.user_id == user_id)
            )
        )
        endorsement = result.scalar_one_or_none()

        if endorsement:
            await db.delete(endorsement)
            await db.commit()
            return True

        return False

    @staticmethod
    async def get_user_endorsement(
        db: AsyncSession,
        item_cid: str,
        user_id: str,
    ) -> Optional[Endorsement]:
        """Get a specific user's endorsement for an item."""
        result = await db.execute(
            select(Endorsement).where(
                (Endorsement.item_cid == item_cid) & (Endorsement.user_id == user_id)
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_endorsements_for_item(
        db: AsyncSession,
        item_cid: str,
    ) -> List[Endorsement]:
        """Get all endorsements for an item (admin audit log)."""
        result = await db.execute(
            select(Endorsement).where(Endorsement.item_cid == item_cid)
            .order_by(Endorsement.created_at.desc())
        )
        return result.scalars().all()

    @staticmethod
    async def get_endorsement_stats(
        db: AsyncSession,
        item_cid: str,
    ) -> Dict[str, Any]:
        """Get aggregated endorsement statistics for an item."""
        # Count upvotes
        upvote_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType.UPVOTE)
            )
        )
        upvote_count = upvote_result.scalar() or 0

        # Count downvotes
        downvote_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType.DOWNVOTE)
            )
        )
        downvote_count = downvote_result.scalar() or 0

        # Count flags
        flag_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType.FLAG)
            )
        )
        flag_count = flag_result.scalar() or 0

        # Total endorsements
        total_result = await db.execute(
            select(func.count(Endorsement.id)).where(Endorsement.item_cid == item_cid)
        )
        total_count = total_result.scalar() or 0

        return {
            "item_cid": item_cid,
            "upvote_count": upvote_count,
            "downvote_count": downvote_count,
            "flag_count": flag_count,
            "total_count": total_count,
            "score": upvote_count - downvote_count,  # Simple scoring: upvotes minus downvotes
        }

    @staticmethod
    async def delete_all_endorsements_for_item(
        db: AsyncSession,
        item_cid: str,
    ) -> int:
        """Delete all endorsements for an item (when item is deleted).

        Returns the number of endorsements deleted.
        """
        result = await db.execute(
            select(Endorsement).where(Endorsement.item_cid == item_cid)
        )
        endorsements = result.scalars().all()
        count = len(endorsements)

        for endorsement in endorsements:
            await db.delete(endorsement)

        await db.commit()
        return count
