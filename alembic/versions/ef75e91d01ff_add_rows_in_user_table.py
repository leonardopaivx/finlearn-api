"""Add rows in user table

Revision ID: ef75e91d01ff
Revises: 91009795dc83
Create Date: 2023-04-03 13:04:06.882889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef75e91d01ff'
down_revision = '91009795dc83'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(), nullable=True))
    op.add_column('user', sa.Column('name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('telephone', sa.String(), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_column('user', 'telephone')
    op.drop_column('user', 'name')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
