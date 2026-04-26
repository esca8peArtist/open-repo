"""Add federation conflicts table for Wave 4 Phase 4.

Revision ID: 002
Revises: 001
Create Date: 2026-04-26 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create federation_conflicts table for Phase 4 conflict logging."""

    # Create conflict_type enum
    conflict_type_enum = postgresql.ENUM(
        'signature_mismatch', 'key_expired', 'key_revoked', 'trust_failure',
        name='conflict_type',
        create_type=True
    )
    conflict_type_enum.create(op.get_bind(), checkfirst=True)

    # Create conflict_status enum
    conflict_status_enum = postgresql.ENUM(
        'active', 'resolved',
        name='conflict_status',
        create_type=True
    )
    conflict_status_enum.create(op.get_bind(), checkfirst=True)

    # Create conflict_resolution_action enum
    conflict_resolution_enum = postgresql.ENUM(
        'auto_downgrade', 'manual_review', 'ignore',
        name='conflict_resolution_action',
        create_type=True
    )
    conflict_resolution_enum.create(op.get_bind(), checkfirst=True)

    # Create federation_conflicts table
    op.create_table(
        'federation_conflicts',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('partner_id', sa.BigInteger(), nullable=False),
        sa.Column('activity_id', sa.BigInteger(), nullable=True),
        sa.Column('conflict_type', conflict_type_enum, nullable=False),
        sa.Column('status', conflict_status_enum, nullable=False, server_default='active'),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('resolution_action', conflict_resolution_enum, nullable=True),
        sa.Column('resolved_by', sa.String(255), nullable=True),
        sa.Column('resolution_notes', sa.Text(), nullable=True),
        sa.Column('detected_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('resolved_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['partner_id'], ['federation_partners.id']),
        sa.ForeignKeyConstraint(['activity_id'], ['activities.id']),
    )

    # Create indexes
    op.create_index('idx_federation_conflicts_partner_id', 'federation_conflicts', ['partner_id'])
    op.create_index('idx_federation_conflicts_activity_id', 'federation_conflicts', ['activity_id'])
    op.create_index('idx_federation_conflicts_conflict_type', 'federation_conflicts', ['conflict_type'])
    op.create_index('idx_federation_conflicts_status', 'federation_conflicts', ['status'])
    op.create_index('idx_federation_conflicts_detected_at', 'federation_conflicts', ['detected_at'])
    op.create_index('idx_federation_conflicts_resolved_at', 'federation_conflicts', ['resolved_at'])


def downgrade() -> None:
    """Drop federation_conflicts table and enums."""

    # Drop indexes
    op.drop_index('idx_federation_conflicts_resolved_at', 'federation_conflicts')
    op.drop_index('idx_federation_conflicts_detected_at', 'federation_conflicts')
    op.drop_index('idx_federation_conflicts_status', 'federation_conflicts')
    op.drop_index('idx_federation_conflicts_conflict_type', 'federation_conflicts')
    op.drop_index('idx_federation_conflicts_activity_id', 'federation_conflicts')
    op.drop_index('idx_federation_conflicts_partner_id', 'federation_conflicts')

    # Drop table
    op.drop_table('federation_conflicts')

    # Drop enum types
    conflict_resolution_enum = postgresql.ENUM(
        'auto_downgrade', 'manual_review', 'ignore',
        name='conflict_resolution_action'
    )
    conflict_resolution_enum.drop(op.get_bind(), checkfirst=True)

    conflict_status_enum = postgresql.ENUM(
        'active', 'resolved',
        name='conflict_status'
    )
    conflict_status_enum.drop(op.get_bind(), checkfirst=True)

    conflict_type_enum = postgresql.ENUM(
        'signature_mismatch', 'key_expired', 'key_revoked', 'trust_failure',
        name='conflict_type'
    )
    conflict_type_enum.drop(op.get_bind(), checkfirst=True)
