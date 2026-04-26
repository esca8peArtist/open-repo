"""Service for endorsement propagation via ActivityPub Announce/Undo activities.

Phase 4 Wave 3: Distributed vote synchronization across federation partners.
When a user votes on an item, an Announce activity is generated and sent to
all federation partners. Vote counts aggregate locally + remotely.
"""

import json
import uuid
import httpx
import logging
from datetime import datetime
from typing import Optional, Dict, Tuple, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_

from app.models import Activity, ActivityType, Endorsement, EndorsementType
from app.http_signatures import HTTPSignatureUtils

logger = logging.getLogger(__name__)


class EndorsementPropagationService:
    """Service for generating, sending, and ingesting Announce/Undo activities."""

    @staticmethod
    async def generate_announce_activity(
        db: AsyncSession,
        item_cid: str,
        user_id: str,
        endorsement_type: str,
        node_url: str,
        private_key: str,
    ) -> Activity:
        """Generate an Announce activity when user votes on item.

        Args:
            db: Database session
            item_cid: Content item CID being voted on
            user_id: User performing the vote
            endorsement_type: 'upvote' | 'downvote'
            node_url: This node's base URL
            private_key: Private key for signing (unused here, used for sending)

        Returns:
            Activity object with Announce type
        """
        # Step 1: Get current vote stats for item
        upvote_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType.UPVOTE)
            )
        )
        local_upvote_count = upvote_result.scalar() or 0

        downvote_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType.DOWNVOTE)
            )
        )
        local_downvote_count = downvote_result.scalar() or 0

        # Step 2: Build Announce JSON-LD
        activity_id = f"{node_url}/activities/announce-{uuid.uuid4()}"
        timestamp = datetime.utcnow().isoformat() + "Z"

        announce_data = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": activity_id,
            "type": "Announce",
            "actor": f"{node_url}/actor",
            "object": f"{node_url}/items/{item_cid}",
            "published": timestamp,
            "content": {
                "item_cid": item_cid,
                "vote_type": endorsement_type,
                "user_id": user_id,
                "source_node": node_url,
                "local_upvote_count": local_upvote_count,
                "local_downvote_count": local_downvote_count,
                "timestamp": timestamp,
            }
        }

        # Step 3: Create Activity record with activity_type=Announce, local=1
        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id=activity_id,
            actor_url=f"{node_url}/actor",
            object_id=f"{node_url}/items/{item_cid}",
            activity_data=announce_data,
            local=1,  # Generated locally
            published=datetime.utcnow(),
        )

        # Step 4: Store in database
        db.add(activity)
        await db.commit()
        await db.refresh(activity)

        return activity

    @staticmethod
    async def send_announce_to_federation_partners(
        db: AsyncSession,
        activity: Activity,
        private_key: str,
    ) -> Dict[str, Tuple[bool, Optional[str]]]:
        """Send Announce activity to all federation partners.

        Args:
            db: Database session
            activity: The Activity object to send
            private_key: Private key for HTTP signature

        Returns:
            Dict mapping partner_url to (success: bool, error_msg: optional)
        """
        results = {}

        # For now, return empty results - federation_partners table not yet implemented
        # When implemented, this will:
        # 1. Query federation_partners table
        # 2. For each partner, create HTTP signature and POST to inbox_url
        # 3. Collect results and log failures
        #
        # This is a fire-and-forget operation - don't fail local vote if delivery fails

        logger.info(f"Announce activity {activity.activity_id} ready for federation (no partners configured yet)")
        return results

    @staticmethod
    async def ingest_announce_activity(
        db: AsyncSession,
        activity: Activity,
    ) -> bool:
        """Ingest received Announce activity from remote node.

        Stores activity in audit log for vote aggregation.
        Does NOT create local Endorsement record (only remote activities).

        Args:
            db: Database session
            activity: The received Activity object with type=Announce

        Returns:
            True if successfully ingested, False on error
        """
        try:
            # Step 1: Validate activity has required fields
            if activity.activity_type != ActivityType.ANNOUNCE:
                logger.warning(f"Invalid activity type for ingest_announce: {activity.activity_type}")
                return False

            if not activity.activity_data:
                logger.warning("Activity data missing")
                return False

            content = activity.activity_data.get("content", {})
            if not content.get("item_cid"):
                logger.warning("Missing item_cid in Announce activity")
                return False

            if not activity.actor_url:
                logger.warning("Missing actor_url in Announce activity")
                return False

            # Step 2: Mark as remote and store
            activity.local = 0

            # Step 3: Store in database
            db.add(activity)
            await db.commit()
            await db.refresh(activity)

            logger.info(f"Ingested Announce activity {activity.activity_id} from {activity.actor_url}")
            return True

        except Exception as e:
            logger.error(f"Failed to ingest Announce activity: {e}")
            return False

    @staticmethod
    async def generate_undo_activity(
        db: AsyncSession,
        announce_activity_id: str,
        node_url: str,
        private_key: str,
    ) -> Activity:
        """Generate Undo activity to retract a vote.

        Called when user removes their endorsement.

        Args:
            db: Database session
            announce_activity_id: ID of the original Announce activity to undo
            node_url: This node's base URL
            private_key: Private key for signing

        Returns:
            Activity object with Undo type
        """
        # Step 1: Fetch the original Announce activity by ID
        result = await db.execute(
            select(Activity).where(Activity.activity_id == announce_activity_id)
        )
        original_announce = result.scalar_one_or_none()

        if not original_announce:
            logger.warning(f"Original Announce activity not found: {announce_activity_id}")
            raise ValueError(f"Original Announce activity not found: {announce_activity_id}")

        # Step 2: Build Undo JSON-LD
        undo_id = f"{node_url}/activities/undo-{uuid.uuid4()}"
        timestamp = datetime.utcnow().isoformat() + "Z"

        undo_data = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": undo_id,
            "type": "Undo",
            "actor": f"{node_url}/actor",
            "object": announce_activity_id,
            "published": timestamp,
        }

        # Step 3: Create Activity record with activity_type=Undo, local=1
        activity = Activity(
            activity_type=ActivityType.UNDO,
            activity_id=undo_id,
            actor_url=f"{node_url}/actor",
            object_id=announce_activity_id,
            activity_data=undo_data,
            local=1,  # Generated locally
            published=datetime.utcnow(),
        )

        # Step 4: Store in database
        db.add(activity)
        await db.commit()
        await db.refresh(activity)

        logger.info(f"Generated Undo activity {undo_id} for {announce_activity_id}")
        return activity

    @staticmethod
    async def ingest_undo_activity(
        db: AsyncSession,
        activity: Activity,
    ) -> bool:
        """Ingest received Undo activity from remote node.

        Args:
            db: Database session
            activity: The received Activity object with type=Undo

        Returns:
            True if successfully ingested, False on error
        """
        try:
            # Step 1: Validate activity has required fields
            if activity.activity_type != ActivityType.UNDO:
                logger.warning(f"Invalid activity type for ingest_undo: {activity.activity_type}")
                return False

            if not activity.activity_data:
                logger.warning("Activity data missing for Undo")
                return False

            original_announce_id = activity.activity_data.get("object")
            if not original_announce_id:
                logger.warning("Missing object (original Announce ID) in Undo activity")
                return False

            # Step 2: Find the original Announce activity by ID
            result = await db.execute(
                select(Activity).where(Activity.activity_id == original_announce_id)
            )
            original_announce = result.scalar_one_or_none()

            if not original_announce:
                # Original not found - log but still ingest the Undo for audit trail
                logger.warning(f"Original Announce activity not found for Undo: {original_announce_id}")

            # Step 3: Mark as remote and store Undo activity with local=0
            activity.local = 0

            # Step 4: Store in database
            db.add(activity)
            await db.commit()
            await db.refresh(activity)

            logger.info(f"Ingested Undo activity {activity.activity_id} from {activity.actor_url}")
            return True

        except Exception as e:
            logger.error(f"Failed to ingest Undo activity: {e}")
            return False

    @staticmethod
    async def get_aggregated_vote_count(
        db: AsyncSession,
        item_cid: str,
        endorsement_type: str = "upvote",
    ) -> Dict[str, Any]:
        """Get local + remote vote counts for an item.

        Aggregates votes from:
        - endorsements table (local votes only)
        - activities table (remote Announce activities)

        Args:
            db: Database session
            item_cid: Content item CID
            endorsement_type: 'upvote' | 'downvote'

        Returns:
            {
                "local": 10,      # Local votes only
                "remote": 7,      # Remote votes from federation partners
                "total": 17,      # Sum
                "breakdown": {    # By partner node
                    "https://node-b.example.com": 7
                }
            }
        """
        # Step 1: Count local votes
        local_result = await db.execute(
            select(func.count(Endorsement.id)).where(
                (Endorsement.item_cid == item_cid)
                & (Endorsement.endorsement_type == EndorsementType(endorsement_type))
            )
        )
        local_count = local_result.scalar() or 0

        # Step 2: Get all remote Announce activities for this item
        # (excluding those that have been undone)
        remote_result = await db.execute(
            select(Activity).where(
                (Activity.activity_type == ActivityType.ANNOUNCE)
                & (Activity.object_id.contains(item_cid))  # Simple match for item reference
                & (Activity.local == 0)  # Remote activities only
            )
        )
        announce_activities = remote_result.scalars().all()

        # Get all Undo activity IDs to exclude their targets
        undo_result = await db.execute(
            select(Activity.object_id).where(
                Activity.activity_type == ActivityType.UNDO
            )
        )
        undo_ids = set(r[0] for r in undo_result.all() if r[0])

        # Step 3: Filter Announces by vote type and count by source_node
        breakdown = {}
        remote_count = 0

        for activity in announce_activities:
            # Skip if this announce has been undone
            if activity.activity_id in undo_ids:
                continue

            content = activity.activity_data.get("content", {})

            # Check if this is the right vote type
            vote_type = content.get("vote_type", "")
            if vote_type != endorsement_type:
                continue

            # Check if item_cid matches
            activity_item_cid = content.get("item_cid", "")
            if activity_item_cid != item_cid:
                continue

            source_node = content.get("source_node", "unknown")
            breakdown[source_node] = breakdown.get(source_node, 0) + 1
            remote_count += 1

        # Step 4: Return aggregated dict
        total = local_count + remote_count
        return {
            "local": local_count,
            "remote": remote_count,
            "total": total,
            "breakdown": breakdown,
        }

    @staticmethod
    async def get_all_vote_stats(
        db: AsyncSession,
        item_cid: str,
    ) -> Dict[str, Any]:
        """Get comprehensive vote statistics (upvotes, downvotes, flags).

        Args:
            db: Database session
            item_cid: Content item CID

        Returns:
            {
                "upvote_count": {local: X, remote: Y, total: Z, breakdown: {...}},
                "downvote_count": {...},
                "flag_count": {...},
                "score": X - Y  # upvotes - downvotes
            }
        """
        upvote_stats = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "upvote"
        )
        downvote_stats = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "downvote"
        )
        flag_stats = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "flag"
        )

        # Calculate score: upvotes - downvotes
        score = upvote_stats["total"] - downvote_stats["total"]

        return {
            "upvote_count": upvote_stats,
            "downvote_count": downvote_stats,
            "flag_count": flag_stats,
            "score": score,
        }
