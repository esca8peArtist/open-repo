"""Service for managing contributions, reviews, and moderation workflow."""

import json
import hashlib
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime, timedelta
from sqlalchemy import select, func, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    Contribution,
    ContributionStatus,
    ContributionType,
    ReviewerQueueItem,
    ContributionFeedback,
    ContentItem,
)


def compute_cid(content: dict) -> str:
    """Compute SHA256-based CID for content."""
    content_str = json.dumps(content, sort_keys=True, separators=(',', ':'))
    sha256_hash = hashlib.sha256(content_str.encode()).hexdigest()
    return f"sha256-{sha256_hash}"


class ContributionService:
    """Service for contribution CRUD, state management, and review workflow."""

    @staticmethod
    async def create_contribution(
        db: AsyncSession,
        contribution_type: str,
        item_data: Dict[str, Any],
        contributor_id: Optional[str] = None,
        target_item_cid: Optional[str] = None,
        edit_diff: Optional[Dict[str, Any]] = None,
    ) -> Tuple[Contribution, str]:
        """Create a new contribution (new_item or edit_item).

        Returns: (contribution, proposed_cid)
        """
        # Compute proposed CID
        proposed_cid = compute_cid(item_data)

        # For new items, check for duplicate
        if contribution_type == "new_item":
            existing_item = await db.execute(
                select(ContentItem).where(ContentItem.cid == proposed_cid)
            )
            if existing_item.scalar_one_or_none():
                raise ValueError(f"Item with CID {proposed_cid} already exists")

        # Create contribution
        contribution = Contribution(
            contribution_type=ContributionType(contribution_type),
            status=ContributionStatus.PENDING,
            contributor_id=contributor_id or "anonymous",
            item_data=item_data,
            proposed_cid=proposed_cid,
            target_item_cid=target_item_cid if contribution_type == "edit_item" else None,
            edit_diff=edit_diff if contribution_type == "edit_item" else None,
        )

        db.add(contribution)
        await db.flush()  # Flush to get the ID
        await db.commit()
        await db.refresh(contribution)

        return contribution, proposed_cid

    @staticmethod
    async def get_contribution(db: AsyncSession, contribution_id: int) -> Optional[Contribution]:
        """Retrieve a single contribution by ID."""
        result = await db.execute(
            select(Contribution).where(Contribution.id == contribution_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_contributions(
        db: AsyncSession,
        limit: int = 10,
        offset: int = 0,
        state: Optional[str] = None,
        contribution_type: Optional[str] = None,
        submitted_by: Optional[str] = None,
    ) -> Tuple[List[Contribution], int]:
        """List contributions with optional filtering.

        Returns: (contributions, total_count)
        """
        query = select(Contribution)

        # Apply filters
        conditions = []
        if state:
            conditions.append(Contribution.status == ContributionStatus(state))
        if contribution_type:
            conditions.append(Contribution.contribution_type == ContributionType(contribution_type))
        if submitted_by:
            conditions.append(Contribution.contributor_id == submitted_by)

        if conditions:
            query = query.where(and_(*conditions))

        # Get total count
        count_result = await db.execute(
            select(func.count(Contribution.id)).select_from(Contribution)
        )
        total = count_result.scalar() or 0

        # Get paginated results
        query = query.order_by(Contribution.created_at.desc()).limit(limit).offset(offset)
        result = await db.execute(query)
        contributions = result.scalars().all()

        return contributions, total

    @staticmethod
    async def update_contribution_status(
        db: AsyncSession,
        contribution_id: int,
        status: str,
        reviewer_notes: Optional[str] = None,
        revision_requests: Optional[List[Dict[str, str]]] = None,
    ) -> Contribution:
        """Update contribution status and related metadata."""
        contribution = await ContributionService.get_contribution(db, contribution_id)
        if not contribution:
            raise ValueError(f"Contribution {contribution_id} not found")

        contribution.status = ContributionStatus(status)
        if reviewer_notes:
            contribution.reviewer_notes = reviewer_notes
        if revision_requests:
            contribution.required_revisions = revision_requests

        db.add(contribution)
        await db.commit()
        await db.refresh(contribution)
        return contribution

    @staticmethod
    async def compute_edit_diff(
        existing_content: Dict[str, Any],
        proposed_content: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Compute a structured diff between existing and proposed content.

        Returns: {field: {old: x, new: y}} for changed fields
        """
        diff = {}

        # Simple field-by-field comparison
        all_keys = set(existing_content.keys()) | set(proposed_content.keys())

        for key in all_keys:
            old_val = existing_content.get(key)
            new_val = proposed_content.get(key)

            if old_val != new_val:
                diff[key] = {
                    "old": old_val,
                    "new": new_val,
                }

        return diff


class ReviewService:
    """Service for review workflow, feedback, and consensus logic."""

    @staticmethod
    async def assign_reviewer(
        db: AsyncSession,
        contribution_id: int,
        reviewer_id: str,
    ) -> ReviewerQueueItem:
        """Assign a reviewer to a contribution."""
        # Check for existing assignment
        existing = await db.execute(
            select(ReviewerQueueItem).where(
                and_(
                    ReviewerQueueItem.contribution_id == contribution_id,
                    ReviewerQueueItem.reviewer_id == reviewer_id,
                )
            )
        )
        if existing.scalar_one_or_none():
            raise ValueError(f"Reviewer {reviewer_id} already assigned to contribution {contribution_id}")

        queue_item = ReviewerQueueItem(
            contribution_id=contribution_id,
            reviewer_id=reviewer_id,
        )

        db.add(queue_item)
        await db.commit()
        await db.refresh(queue_item)
        return queue_item

    @staticmethod
    async def get_review_queue(
        db: AsyncSession,
        reviewer_id: Optional[str] = None,
        limit: int = 10,
        offset: int = 0,
        assignment_status: Optional[str] = None,
    ) -> Tuple[List[ReviewerQueueItem], int]:
        """Get review queue items for a reviewer or all pending items.

        Returns: (queue_items, total_count)
        """
        query = select(ReviewerQueueItem).join(Contribution)

        conditions = [
            Contribution.status == ContributionStatus.PENDING,
        ]

        if reviewer_id:
            conditions.append(ReviewerQueueItem.reviewer_id == reviewer_id)

        if assignment_status:
            if assignment_status == "pending":
                conditions.append(ReviewerQueueItem.decided_at.is_(None))
            elif assignment_status == "reviewed":
                conditions.append(ReviewerQueueItem.decided_at.isnot(None))

        query = query.where(and_(*conditions))

        # Get total count
        count_result = await db.execute(
            select(func.count(ReviewerQueueItem.id)).where(and_(*conditions))
        )
        total = count_result.scalar() or 0

        # Get paginated results
        query = query.order_by(ReviewerQueueItem.assigned_at.desc()).limit(limit).offset(offset)
        result = await db.execute(query)
        queue_items = result.scalars().all()

        return queue_items, total

    @staticmethod
    async def submit_review_decision(
        db: AsyncSession,
        contribution_id: int,
        reviewer_id: str,
        decision: str,
        reviewer_notes: Optional[str] = None,
        revision_requests: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, Any]:
        """Submit a reviewer's decision (approve, reject, or revision_requested).

        Returns: review status dict with consensus information
        """
        # Get contribution
        contribution = await ContributionService.get_contribution(db, contribution_id)
        if not contribution:
            raise ValueError(f"Contribution {contribution_id} not found")

        # Check if contribution is in terminal state
        if contribution.status in [ContributionStatus.APPROVED, ContributionStatus.REJECTED]:
            raise ValueError(f"Contribution {contribution_id} is in terminal state")

        # Create feedback record
        feedback = ContributionFeedback(
            contribution_id=contribution_id,
            reviewer_id=reviewer_id,
            decision=decision,
            reviewer_notes=reviewer_notes,
        )

        db.add(feedback)

        # Update reviewer queue item
        queue_result = await db.execute(
            select(ReviewerQueueItem).where(
                and_(
                    ReviewerQueueItem.contribution_id == contribution_id,
                    ReviewerQueueItem.reviewer_id == reviewer_id,
                )
            )
        )
        queue_item = queue_result.scalar_one_or_none()
        if queue_item:
            queue_item.decision = decision
            queue_item.reviewer_notes = reviewer_notes
            queue_item.decided_at = datetime.utcnow()
            db.add(queue_item)

        await db.commit()

        # Check for consensus
        consensus_result, final_state = await ReviewService._check_consensus(
            db, contribution_id
        )

        # If consensus reached, update contribution status
        if final_state:
            await ContributionService.update_contribution_status(
                db, contribution_id, final_state
            )

        # Get feedback count
        feedback_count_result = await db.execute(
            select(func.count(ContributionFeedback.id)).where(
                ContributionFeedback.contribution_id == contribution_id
            )
        )
        feedback_count = feedback_count_result.scalar() or 0

        return {
            "contribution_id": contribution_id,
            "review_status": "pending" if not final_state else "reviewed",
            "feedback_submitted": True,
            "total_feedback_count": feedback_count,
            "consensus_reached": consensus_result,
            "final_state": final_state,
        }

    @staticmethod
    async def _check_consensus(
        db: AsyncSession, contribution_id: int
    ) -> Tuple[bool, Optional[str]]:
        """Check if consensus has been reached on a contribution.

        Simple consensus logic:
        - 2+ approve → auto-approve
        - 1+ reject (and no approvals) → auto-reject
        - Otherwise, pending

        Returns: (consensus_reached, final_state)
        """
        # Get all feedback
        feedback_result = await db.execute(
            select(ContributionFeedback).where(ContributionFeedback.contribution_id == contribution_id)
        )
        feedback_items = feedback_result.scalars().all()

        if not feedback_items:
            return False, None

        # Count decisions
        approve_count = sum(1 for f in feedback_items if f.decision == "approve")
        reject_count = sum(1 for f in feedback_items if f.decision == "reject")
        revision_count = sum(1 for f in feedback_items if f.decision == "revision_requested")

        # Simple consensus logic
        if approve_count >= 2:
            return True, "approved"
        elif reject_count >= 1 and approve_count == 0:
            return True, "rejected"

        return False, None

    @staticmethod
    async def get_review_history(
        db: AsyncSession, contribution_id: int
    ) -> List[ContributionFeedback]:
        """Get all review feedback for a contribution (audit trail)."""
        result = await db.execute(
            select(ContributionFeedback)
            .where(ContributionFeedback.contribution_id == contribution_id)
            .order_by(ContributionFeedback.created_at.asc())
        )
        return result.scalars().all()

    @staticmethod
    async def request_revision(
        db: AsyncSession,
        contribution_id: int,
        revision_requests: List[Dict[str, str]],
        deadline_days: int = 7,
    ) -> Contribution:
        """Request revision from contributor."""
        contribution = await ContributionService.get_contribution(db, contribution_id)
        if not contribution:
            raise ValueError(f"Contribution {contribution_id} not found")

        contribution.status = ContributionStatus.REVISION_REQUESTED
        contribution.required_revisions = revision_requests

        db.add(contribution)
        await db.commit()
        await db.refresh(contribution)
        return contribution


class ContributorStatsService:
    """Service for contributor statistics and reputation calculations."""

    @staticmethod
    async def get_contributor_stats(
        db: AsyncSession, user_id: str
    ) -> Dict[str, Any]:
        """Get contributor statistics and reputation score.

        Returns aggregated stats for a contributor.
        """
        # Get all contributions from this contributor
        result = await db.execute(
            select(Contribution).where(Contribution.contributor_id == user_id)
        )
        contributions = result.scalars().all()

        if not contributions:
            return {
                "user_id": user_id,
                "total_submissions": 0,
                "approved_count": 0,
                "rejected_count": 0,
                "pending_count": 0,
                "revision_requested_count": 0,
                "approval_rate": 0.0,
                "endorsement_score": 0,
                "reputation_tier": "none",
                "first_submission": None,
                "last_submission": None,
            }

        # Count by status
        approved = [c for c in contributions if c.status == ContributionStatus.APPROVED]
        rejected = [c for c in contributions if c.status == ContributionStatus.REJECTED]
        pending = [c for c in contributions if c.status == ContributionStatus.PENDING]
        revision_requested = [c for c in contributions if c.status == ContributionStatus.REVISION_REQUESTED]

        total = len(contributions)
        approved_count = len(approved)
        approval_rate = approved_count / total if total > 0 else 0.0

        # Calculate endorsement score (sum of upvotes on approved items' related content)
        # For now, simplified: count of approved items
        endorsement_score = approved_count * 5  # Simple scoring: 5 points per approval

        # Reputation tier logic
        if approved_count == 0:
            reputation_tier = "none"
        elif approval_rate >= 0.8 and approved_count >= 3:
            reputation_tier = "expert"
        elif approval_rate >= 0.6:
            reputation_tier = "trusted"
        else:
            reputation_tier = "none"

        # Get first and last submission
        contributions_sorted = sorted(contributions, key=lambda c: c.created_at)
        first_submission = contributions_sorted[0].created_at if contributions_sorted else None
        last_submission = contributions_sorted[-1].created_at if contributions_sorted else None

        return {
            "user_id": user_id,
            "total_submissions": total,
            "approved_count": approved_count,
            "rejected_count": len(rejected),
            "pending_count": len(pending),
            "revision_requested_count": len(revision_requested),
            "approval_rate": round(approval_rate, 2),
            "endorsement_score": endorsement_score,
            "reputation_tier": reputation_tier,
            "first_submission": first_submission,
            "last_submission": last_submission,
        }
