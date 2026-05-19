"""Add zim_exports table for Phase 5 offline export tracking."""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import BigInteger, Integer, String, DateTime, Float, Text, Boolean
from datetime import datetime

# revision identifiers
revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    """Create zim_exports table."""
    op.create_table(
        'zim_exports',
        sa.Column('id', BigInteger(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('zim_uuid', String(36), nullable=False, unique=True, index=True),
        sa.Column('name', String(255), nullable=False, index=True),
        sa.Column('flavour', String(50), nullable=False, index=True),
        sa.Column('language', String(10), nullable=False),
        sa.Column('period', String(10), nullable=False, index=True),
        sa.Column('article_count', Integer(), nullable=False),
        sa.Column('file_size_bytes', BigInteger(), nullable=False),
        sa.Column('sha256', String(64), nullable=False),
        sa.Column('title', String(255), nullable=False),
        sa.Column('description', String(80), nullable=False),
        sa.Column('cdn_url', String(512), nullable=True),
        sa.Column('local_path', String(512), nullable=True),
        sa.Column('status', String(20), nullable=False, default='generating', index=True),
        sa.Column('is_current', Boolean(), nullable=False, default=False, index=True),
        sa.Column('is_reference', Boolean(), nullable=False, default=False),
        sa.Column('export_scope', String(20), nullable=False),
        sa.Column('scope_value', String(100), nullable=True),
        sa.Column('include_images', Boolean(), nullable=False, default=False),
        sa.Column('zimcheck_passed', Boolean(), nullable=True),
        sa.Column('zimcheck_output', Text(), nullable=True),
        sa.Column('generation_duration_seconds', Float(), nullable=True),
        sa.Column('started_at', DateTime(), nullable=False, default=datetime.utcnow),
        sa.Column('completed_at', DateTime(), nullable=True),
        sa.Column('superseded_at', DateTime(), nullable=True),
        sa.Column('deleted_at', DateTime(), nullable=True),
        sa.Column('created_at', DateTime(), nullable=False, default=datetime.utcnow),
        sa.Column('updated_at', DateTime(), nullable=False, default=datetime.utcnow),
    )
    op.create_index('idx_zim_exports_name_flavour', 'zim_exports', ['name', 'flavour'])
    op.create_index('idx_zim_exports_is_current', 'zim_exports',
                   ['is_current'], postgresql_where=sa.text("is_current = TRUE"))


def downgrade():
    """Drop zim_exports table."""
    op.drop_index('idx_zim_exports_is_current')
    op.drop_index('idx_zim_exports_name_flavour')
    op.drop_table('zim_exports')
