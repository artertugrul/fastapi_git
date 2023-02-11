"""create posts table

Revision ID: 5ad27e2ef521
Revises: 
Create Date: 2023-01-27 22:51:47.214371

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '5ad27e2ef521'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False)
        )
    pass


def downgrade():
    op.drop_table("posts")
    pass
