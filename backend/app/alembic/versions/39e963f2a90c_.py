"""

Revision ID: 39e963f2a90c
Revises: 42987bba616e
Create Date: 2020-07-07 15:36:55.109596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39e963f2a90c'
down_revision = '42987bba616e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('menu_type', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menu', 'menu_type')
    # ### end Alembic commands ###