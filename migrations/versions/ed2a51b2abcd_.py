"""empty message

Revision ID: ed2a51b2abcd
Revises: 15227b31825e
Create Date: 2022-11-14 13:56:19.885953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed2a51b2abcd'
down_revision = '15227b31825e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    # ### end Alembic commands ###