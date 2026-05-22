"""SQLAlchemy ORM models for content items, endorsements, contributions, and reviews."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON, Text, Integer, ForeignKey, Enum, BigInteger, Boolean, Float
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


class TrustStatus(str, enum.Enum):
    """Trust status enumeration for federation partners."""

    PENDING = "pending"
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"
    REVOKED = "revoked"


class FederationPartner(Base):
    """Federation partner model - tracks partner nodes and their public keys."""

    __tablename__ = "federation_partners"

    # Primary key: UUID
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Partner identification
    name = Column(String(255), nullable=False, unique=True, index=True)
    base_url = Column(String(512), nullable=False, unique=True, index=True)  # https://node-b.example.com

    # Public key and signature info
    public_key_pem = Column(Text, nullable=False)  # PEM-encoded RSA public key
    key_id = Column(String(512), unique=True, index=True, nullable=False)  # Key identifier URI

    # Trust state machine
    trust_state = Column(
        Enum(TrustStatus),
        nullable=False,
        default=TrustStatus.PENDING,
        index=True,
    )

    # Signature failure tracking
    failed_signature_count = Column(Integer, nullable=False, default=0)

    # Timestamps
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    public_key_expires_at = Column(DateTime, nullable=True)
    last_key_refresh_at = Column(DateTime, nullable=True)
    last_activity_at = Column(DateTime, nullable=True, index=True)

    def __repr__(self):
        return f"<FederationPartner id={self.id} name={self.name} trust_state={self.trust_state}>"


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

    # Wave 4 Federation Partner fields
    partner_id = Column(BigInteger, ForeignKey("federation_partners.id"), nullable=True, index=True)
    signature_header = Column(String(1024), nullable=True)  # Raw Signature header for audit
    signature_verified = Column(Integer, nullable=False, default=0)  # 1 = verified, 0 = unverified/failed

    def __repr__(self):
        return f"<Activity id={self.id} type={self.activity_type} actor={self.actor_url}>"


class ConflictType(str, enum.Enum):
    """Federation conflict type enumeration for Wave 4 Phase 4."""

    SIGNATURE_MISMATCH = "signature_mismatch"
    KEY_EXPIRED = "key_expired"
    KEY_REVOKED = "key_revoked"
    TRUST_FAILURE = "trust_failure"


class ConflictResolutionAction(str, enum.Enum):
    """Federation conflict resolution action enumeration."""

    AUTO_DOWNGRADE = "auto_downgrade"
    MANUAL_REVIEW = "manual_review"
    IGNORE = "ignore"


class ConflictStatus(str, enum.Enum):
    """Federation conflict status enumeration."""

    ACTIVE = "active"
    RESOLVED = "resolved"


class FederationConflict(Base):
    """Federation conflict model - tracks signature/key/trust conflicts.

    Wave 4 Phase 4: Conflict logging and admin dashboard for federation monitoring.
    Stores records of signature verification failures, key issues, and trust failures.
    """

    __tablename__ = "federation_conflicts"

    # Primary key
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # Foreign keys
    partner_id = Column(BigInteger, ForeignKey("federation_partners.id"), nullable=False, index=True)
    activity_id = Column(BigInteger, ForeignKey("activities.id"), nullable=True, index=True)  # Nullable for key-level conflicts

    # Conflict metadata
    conflict_type = Column(Enum(ConflictType), nullable=False, index=True)
    status = Column(Enum(ConflictStatus), nullable=False, default=ConflictStatus.ACTIVE, index=True)

    # Conflict details
    error_message = Column(Text, nullable=True)  # Error details from verification failure

    # Resolution tracking
    resolution_action = Column(Enum(ConflictResolutionAction), nullable=True)
    resolved_by = Column(String(255), nullable=True)  # Admin user ID or system identifier
    resolution_notes = Column(Text, nullable=True)

    # Timestamps
    detected_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    resolved_at = Column(DateTime, nullable=True, index=True)

    def __repr__(self):
        return f"<FederationConflict id={self.id} partner_id={self.partner_id} type={self.conflict_type} status={self.status}>"


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


class ZimExportStatus(str, enum.Enum):
    """Status enum for ZIM export lifecycle."""

    GENERATING = "generating"
    COMPLETE = "complete"
    FAILED = "failed"
    SUPERSEDED = "superseded"
    DELETED = "deleted"


class ZimExport(Base):
    """
    ORM model for the zim_exports table (migration 003).

    Tracks each ZIM archive generated by the offline export pipeline.
    One row per ZIM file. The OPDS catalog is populated from this table.

    Lifecycle:
        GENERATING → COMPLETE (successful export)
        GENERATING → FAILED (exception during export)
        COMPLETE   → SUPERSEDED (newer ZIM for same name+flavour published)
        Any state  → DELETED (soft delete; file may remain on CDN for a grace period)

    The is_current flag is true for exactly one COMPLETE row per (name, flavour)
    combination at any point in time. The partial index idx_zim_exports_is_current
    on (is_current=TRUE) enforces fast lookup of the current export.
    """

    __tablename__ = "zim_exports"

    # Primary key — surrogate integer; ZIM identity uses zim_uuid
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    # ZIM identity — UUID assigned at export start; stable across retries
    zim_uuid = Column(String(36), nullable=False, unique=True, index=True)

    # ZIM naming (openZIM convention: {project}_{lang}_{flavour})
    name = Column(String(255), nullable=False, index=True)
    flavour = Column(String(50), nullable=False, index=True)
    language = Column(String(10), nullable=False)
    period = Column(String(10), nullable=False, index=True)  # YYYY-MM

    # Content metrics
    article_count = Column(Integer, nullable=False)
    file_size_bytes = Column(BigInteger, nullable=False)
    sha256 = Column(String(64), nullable=False)

    # Metadata fields mirroring ZimMetadata
    title = Column(String(255), nullable=False)
    description = Column(String(80), nullable=False)

    # Distribution
    cdn_url = Column(String(512), nullable=True)    # Cloudflare R2 / CDN URL
    local_path = Column(String(512), nullable=True)  # Absolute path on local filesystem

    # Lifecycle state
    status = Column(String(20), nullable=False, default=ZimExportStatus.GENERATING, index=True)
    is_current = Column(Boolean, nullable=False, default=False, index=True)
    is_reference = Column(Boolean, nullable=False, default=False)  # Pinned reference export

    # Export scope (mirrors ExportConfig)
    export_scope = Column(String(20), nullable=False)  # LOCAL_ONLY, DOMAIN, FULL
    scope_value = Column(String(100), nullable=True)   # domain name or None for FULL

    # Content options
    include_images = Column(Boolean, nullable=False, default=False)

    # Validation
    zimcheck_passed = Column(Boolean, nullable=True)
    zimcheck_output = Column(Text, nullable=True)

    # Performance
    generation_duration_seconds = Column(Float, nullable=True)

    # Timestamps
    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    superseded_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return (
            f"<ZimExport id={self.id} name={self.name} flavour={self.flavour} "
            f"period={self.period} status={self.status} is_current={self.is_current}>"
        )

    @classmethod
    def from_zim_write_result(
        cls,
        result: object,
        export_scope: str,
        scope_value: str | None = None,
        include_images: bool = False,
        cdn_url: str | None = None,
        local_path: str | None = None,
    ) -> "ZimExport":
        """
        Construct a ZimExport from a ZimWriteResult + export configuration.

        This is the standard factory method used by the export pipeline service
        after a successful create_zim() call.

        Args:
            result: ZimWriteResult dataclass returned by ZimWriter.create_zim()
            export_scope: ExportScope value ("LOCAL_ONLY", "DOMAIN", "FULL")
            scope_value: Domain name for DOMAIN scope; None for FULL scope
            include_images: Whether images were included in this export
            cdn_url: CDN URL if the ZIM was uploaded; None if local only
            local_path: Absolute path to the ZIM file on disk

        Returns:
            ZimExport: Unsaved ORM instance ready to be added to the session.
        """
        import uuid
        return cls(
            zim_uuid=str(uuid.uuid4()),
            name=result.name,
            flavour=result.flavour,
            language="eng",          # Default; caller should override for multi-language
            period=result.output_path.stem.rsplit("_", 1)[-1] if "_" in result.output_path.stem else "",
            article_count=result.article_count,
            file_size_bytes=result.file_size_bytes,
            sha256=result.sha256,
            title="",                # Caller populates from ZimMetadata
            description="",          # Caller populates from ZimMetadata
            cdn_url=cdn_url,
            local_path=str(local_path) if local_path else str(result.output_path),
            status=ZimExportStatus.COMPLETE,
            is_current=False,        # Caller sets is_current after superseding previous export
            is_reference=False,
            export_scope=export_scope,
            scope_value=scope_value,
            include_images=include_images,
            zimcheck_passed=result.zimcheck_passed,
            zimcheck_output=None,
            generation_duration_seconds=result.generation_duration_seconds,
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow(),
        )
