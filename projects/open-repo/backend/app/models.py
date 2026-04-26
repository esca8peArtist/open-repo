"""SQLAlchemy ORM models for content items, endorsements, contributions, and reviews."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON, Text, Integer, ForeignKey, Enum, BigInteger
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()


class ContentItem(Base):
    """Content item model - stores OpenRepoItem JSON-LD objects."""

    __tablename__ = "content_items"

    # Primary key: CID (content hash)
    cid = Column(String(255), primary_key=True, index=True)

    # Item metadata
    title = Column(String(500), nullable=False, index=True)
    item_type = Column(String(50), nullable=False, index=True)  # procedure, recipe, schematic, plan, service-listing
    domain = Column(String(50), nullable=False, index=True)  # procedural, etc
    license = Column(String(50), nullable=False)

    # Full JSON-LD content
    content_jsonld = Column(JSON, nullable=False)

    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Source attribution
    source_url = Column(String(500), nullable=True)
    source_title = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<ContentItem cid={self.cid} type={self.item_type} title={self.title}>"


class EndorsementType(str, enum.Enum):
    """Endorsement type enumeration."""

    UPVOTE = "upvote"
    DOWNVOTE = "downvote"
    FLAG = "flag"


class Endorsement(Base):
    """Endorsement model - user feedback on content items."""

    __tablename__ = "endorsements"

    # Primary key: auto-increment ID
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Foreign key: reference to content item
    item_cid = Column(String(255), nullable=False, index=True)

    # User identifier (simple string; in production would be DID)
    user_id = Column(String(255), nullable=False, index=True)

    # Endorsement type
    endorsement_type = Column(Enum(EndorsementType), nullable=False, index=True)

    # Timestamp
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)

    def __repr__(self):
        return f"<Endorsement user={self.user_id} item={self.item_cid} type={self.endorsement_type}>"


class ContributionStatus(str, enum.Enum):
    """Contribution status enumeration - state machine."""

    PENDING = "pending"
    REVISION_REQUESTED = "revision_requested"
    APPROVED = "approved"
    REJECTED = "rejected"


class ContributionType(str, enum.Enum):
    """Contribution type enumeration."""

    NEW_ITEM = "new_item"
    EDIT_ITEM = "edit_item"


class Contribution(Base):
    """Contribution model - tracks user submissions (new items or edits)."""

    __tablename__ = "contributions"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Contribution type
    contribution_type = Column(Enum(ContributionType), nullable=False, index=True)

    # Status (state machine)
    status = Column(Enum(ContributionStatus), nullable=False, index=True, default=ContributionStatus.PENDING)

    # Contributor metadata
    contributor_id = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Content references
    target_item_cid = Column(String(255), ForeignKey("content_items.cid"), nullable=True, index=True)  # For edits
    proposed_cid = Column(String(255), nullable=True, index=True)  # CID of proposed content (for new items)

    # Full proposed content as JSON-LD
    item_data = Column(JSON, nullable=False)

    # Edit-specific: structured diff
    edit_diff = Column(JSON, nullable=True)

    # Decision metadata
    reviewer_notes = Column(Text, nullable=True)
    rejection_reason = Column(Text, nullable=True)
    required_revisions = Column(JSON, nullable=True)  # Array of {field: string, suggestion: string}

    # Relationships
    reviewer_queue_items = relationship(
        "ReviewerQueueItem",
        back_populates="contribution",
        cascade="all, delete-orphan",
        foreign_keys="ReviewerQueueItem.contribution_id",
        lazy="select",
    )
    feedback_items = relationship(
        "ContributionFeedback",
        back_populates="contribution",
        cascade="all, delete-orphan",
        foreign_keys="ContributionFeedback.contribution_id",
        lazy="select",
    )

    def __repr__(self):
        return f"<Contribution id={self.id} type={self.contribution_type} status={self.status}>"


class ReviewerQueueItem(Base):
    """ReviewerQueueItem model - tracks reviewer assignments for round-robin review."""

    __tablename__ = "reviewer_queue_items"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Foreign keys
    contribution_id = Column(BigInteger, ForeignKey("contributions.id"), nullable=False, index=True)
    reviewer_id = Column(String(255), nullable=False, index=True)

    # Assignment metadata
    assigned_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    decided_at = Column(DateTime, nullable=True)

    # Reviewer decision
    decision = Column(String(50), nullable=True)  # 'approve', 'reject', 'revision_requested'
    reviewer_notes = Column(Text, nullable=True)

    # Relationships
    contribution = relationship(
        "Contribution",
        back_populates="reviewer_queue_items",
        foreign_keys=[contribution_id],
    )

    def __repr__(self):
        return f"<ReviewerQueueItem contribution_id={self.contribution_id} reviewer_id={self.reviewer_id}>"


class FeedbackType(str, enum.Enum):
    """Feedback type enumeration."""

    TEXT_ONLY = "text_only"
    MINOR_CORRECTION = "minor_correction"
    MISSING_FIELD = "missing_field"


class FeedbackSeverity(str, enum.Enum):
    """Feedback severity enumeration."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ContributionFeedback(Base):
    """ContributionFeedback model - audit trail of reviewer feedback."""

    __tablename__ = "contribution_feedback"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Foreign key
    contribution_id = Column(BigInteger, ForeignKey("contributions.id"), nullable=False, index=True)

    # Feedback metadata
    feedback_type = Column(Enum(FeedbackType), nullable=False, index=True)
    severity = Column(Enum(FeedbackSeverity), nullable=False, index=True)
    message = Column(Text, nullable=False)

    # Resolution tracking
    resolved = Column(Integer, nullable=False, default=0)  # 0 = unresolved, 1 = resolved
    resolved_at = Column(DateTime, nullable=True)

    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)

    # Relationships
    contribution = relationship(
        "Contribution",
        back_populates="feedback_items",
        foreign_keys=[contribution_id],
    )

    def __repr__(self):
        return f"<ContributionFeedback id={self.id} contribution_id={self.contribution_id} severity={self.severity}>"


# ============================================================================
# Phase 4: ActivityPub Federation Models
# ============================================================================


class ActivityType(str, enum.Enum):
    """Activity type enumeration per ActivityPub spec."""

    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    ANNOUNCE = "Announce"
    UNDO = "Undo"
    FOLLOW = "Follow"
    ACCEPT = "Accept"


class Activity(Base):
    """Activity model - stores ActivityPub activities for federation."""

    __tablename__ = "activities"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Activity metadata
    activity_type = Column(Enum(ActivityType), nullable=False, index=True)
    activity_id = Column(String(512), unique=True, index=True, nullable=False)  # Unique activity URI

    # Actor (who performed the action)
    actor_url = Column(String(512), nullable=False, index=True)  # Full actor URL

    # Object and target (what the activity was about)
    object_id = Column(String(512), nullable=True, index=True)  # Object URI or inline object ID
    object_data = Column(JSON, nullable=True)  # Full object (for Create/Update activities)

    # Full activity as JSON-LD
    activity_data = Column(JSON, nullable=False)

    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    published = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Federation metadata
    local = Column(Integer, nullable=False, default=1)  # 1 = generated locally, 0 = received from remote

    def __repr__(self):
        return f"<Activity id={self.id} type={self.activity_type} actor={self.actor_url}>"


class NodePublicKey(Base):
    """Node public key storage for HTTP signature verification."""

    __tablename__ = "node_public_keys"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Key metadata
    key_id = Column(String(512), unique=True, index=True, nullable=False)  # Unique key URI
    public_key_pem = Column(Text, nullable=False)  # PEM-encoded public key
    node_url = Column(String(512), nullable=False, index=True)  # Source node URL

    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<NodePublicKey id={self.id} key_id={self.key_id} node={self.node_url}>"
