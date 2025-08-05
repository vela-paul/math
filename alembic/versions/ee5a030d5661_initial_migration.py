"""initial migration

Revision ID: ee5a030d5661
Revises: 
Create Date: 2025-08-05 12:04:31.471008

"""
from typing import Sequence, Union

from alembic import op  # type: ignore
import sqlalchemy as sa  # type: ignore


# revision identifiers, used by Alembic.
revision: str = 'ee5a030d5661'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands manually adjusted to create requests_logs table ###
    op.create_table(
        'requests_logs',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('operation', sa.String(), nullable=False),
        sa.Column('parameters', sa.JSON(), nullable=False),
        sa.Column('result', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands manually adjusted to drop requests_logs table ###
    op.drop_table('requests_logs')
    # ### end Alembic commands ###
