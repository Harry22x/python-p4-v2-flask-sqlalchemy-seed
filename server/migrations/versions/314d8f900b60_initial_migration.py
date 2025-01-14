"""Initial migration.

Revision ID: 314d8f900b60
Revises: 
Create Date: 2025-01-14 11:40:06.650556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '314d8f900b60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
