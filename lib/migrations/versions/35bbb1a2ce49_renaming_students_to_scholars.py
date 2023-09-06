"""Renaming students to scholars

Revision ID: 35bbb1a2ce49
Revises: 791279dd0760
Create Date: 2023-09-06 10:56:38.890098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35bbb1a2ce49'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
