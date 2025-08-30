# mypy: ignore-errors
# ruff: noqa: INP001
"""Insert first rows.

Revision ID: 3f101b21d66a
Revises: 032adc3dc50f
Create Date: 2025-08-30 23:33:57.354283

"""

from collections.abc import Sequence

from alembic import op

from migrations.queries.first_rows import (
    insert_first_rows_with_async_connection,
)

# revision identifiers, used by Alembic.
revision: str = "3f101b21d66a"
down_revision: str | Sequence[str] | None = "032adc3dc50f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.run_async(insert_first_rows_with_async_connection)


def downgrade() -> None:
    """Downgrade schema."""
