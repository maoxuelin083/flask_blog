"""empty message

Revision ID: 82cdab79cb49
Revises: 8de3c57d0cea
Create Date: 2019-12-02 22:42:17.686729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82cdab79cb49'
down_revision = '8de3c57d0cea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_models', sa.Column('permission', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_models', 'permission')
    # ### end Alembic commands ###
