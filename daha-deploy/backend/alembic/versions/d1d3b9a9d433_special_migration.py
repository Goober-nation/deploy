"""special migration

Revision ID: d1d3b9a9d433
Revises: 06b21976bcfb
Create Date: 2025-07-10 11:26:17.957309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1d3b9a9d433'
down_revision: Union[str, Sequence[str], None] = '06b21976bcfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
