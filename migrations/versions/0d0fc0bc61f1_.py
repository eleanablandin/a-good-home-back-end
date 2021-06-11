"""empty message

Revision ID: 0d0fc0bc61f1
Revises: 2b0b30488eb0
Create Date: 2021-06-10 17:31:59.352410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d0fc0bc61f1'
down_revision = '2b0b30488eb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent', sa.Column('name', sa.String(length=80), nullable=False))
    op.add_column('agent', sa.Column('last_name', sa.String(length=80), nullable=False))
    op.add_column('agent', sa.Column('phone', sa.String(length=16), nullable=False))
    op.add_column('agent', sa.Column('salt', sa.String(length=40), nullable=False))
    op.add_column('agent', sa.Column('hashed_password', sa.String(length=240), nullable=False))
    op.create_unique_constraint(None, 'agent', ['phone'])
    op.drop_column('agent', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent', sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'agent', type_='unique')
    op.drop_column('agent', 'hashed_password')
    op.drop_column('agent', 'salt')
    op.drop_column('agent', 'phone')
    op.drop_column('agent', 'last_name')
    op.drop_column('agent', 'name')
    # ### end Alembic commands ###