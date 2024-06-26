"""initial migration

Revision ID: d93278e4a454
Revises: 
Create Date: 2024-06-03 09:36:03.206913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93278e4a454'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###
