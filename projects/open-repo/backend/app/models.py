"""SQLAlchemy ORM models for content items and endorsements."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON, Text, Integer, ForeignKey, Enum
from sqlalchemy.orm import declarative_base
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
