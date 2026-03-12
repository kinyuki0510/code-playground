"""create users table

Revision ID: 93bf40a812b6
Revises: 
Create Date: 2026-03-12 11:55:33.206024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93bf40a812b6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('age', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
