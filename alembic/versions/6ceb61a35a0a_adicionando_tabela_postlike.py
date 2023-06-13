"""adicionando tabela PostLike

Revision ID: 6ceb61a35a0a
Revises: 54e07237f3d0
Create Date: 2023-05-29 21:15:55.135551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ceb61a35a0a'
down_revision = '54e07237f3d0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_like',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('date_updated', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_like')
    # ### end Alembic commands ###