"""Add federation partners table and activity extensions for Wave 4.

Revision ID: 001
Revises:
Create Date: 2026-04-26 11:20:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create federation_partners table and extend activities table."""

    # Create trust_status enum type
    trust_status_enum = postgresql.ENUM(
        'pending', 'trusted', 'untrusted', 'revoked',
        name='trust_status',
        create_type=True
    )
    trust_status_enum.create(op.get_bind(), checkfirst=True)

    # Create federation_partners table
    op.create_table(
        'federation_partners',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('base_url', sa.String(512), nullable=False),
        sa.Column('public_key_pem', sa.Text(), nullable=False),
        sa.Column('key_id', sa.String(512), nullable=False),
        sa.Column('trust_state', trust_status_enum, nullable=False, server_default='pending'),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('failed_signature_count', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('public_key_expires_at', sa.DateTime(), nullable=True),
        sa.Column('last_key_refresh_at', sa.DateTime(), nullable=True),
        sa.Column('last_activity_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name', name='uq_federation_partners_name'),
        sa.UniqueConstraint('base_url', name='uq_federation_partners_base_url'),
        sa.UniqueConstraint('key_id', name='uq_federation_partners_key_id'),
    )
    op.create_index('idx_federation_partners_name', 'federation_partners', ['name'])
    op.create_index('idx_federation_partners_base_url', 'federation_partners', ['base_url'])
    op.create_index('idx_federation_partners_trust_state', 'federation_partners', ['trust_state'])
    op.create_index('idx_federation_partners_last_activity', 'federation_partners', ['last_activity_at'])

    # Add columns to activities table
    op.add_column('activities', sa.Column('partner_id', sa.BigInteger(), nullable=True))
    op.add_column('activities', sa.Column('signature_header', sa.String(1024), nullable=True))
    op.add_column('activities', sa.Column('signature_verified', sa.Integer(), nullable=False, server_default='0'))

    # Create foreign key and index
    op.create_foreign_key(
        'fk_activities_partner_id',
        'activities', 'federation_partners',
        ['partner_id'], ['id']
    )
    op.create_index('idx_activities_partner_id', 'activities', ['partner_id'])


def downgrade() -> None:
    """Drop federation_partners table and remove activity extensions."""

    # Drop indexes and constraints from activities
    op.drop_index('idx_activities_partner_id', 'activities')
    op.drop_constraint('fk_activities_partner_id', 'activities', type_='foreignkey')

    # Remove columns from activities
    op.drop_column('activities', 'signature_verified')
    op.drop_column('activities', 'signature_header')
    op.drop_column('activities', 'partner_id')

    # Drop federation_partners table
    op.drop_index('idx_federation_partners_last_activity', 'federation_partners')
    op.drop_index('idx_federation_partners_trust_state', 'federation_partners')
    op.drop_index('idx_federation_partners_base_url', 'federation_partners')
    op.drop_index('idx_federation_partners_name', 'federation_partners')
    op.drop_table('federation_partners')

    # Drop enum type
    trust_status_enum = postgresql.ENUM(
        'pending', 'trusted', 'untrusted', 'revoked',
        name='trust_status'
    )
    trust_status_enum.drop(op.get_bind(), checkfirst=True)
