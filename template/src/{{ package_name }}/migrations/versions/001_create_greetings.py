"""Create greetings table

Revision ID: 001
Revises: 
Create Date: 2026-03-10

# To reset the database (if needed):
# pdm run drop_db   # For SQLite
# docker compose -p {{ package_name }} down -v  # For PostgreSQL (removes volume)
# pdm run migrate
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'greetings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('message', sa.String(500), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('greetings')