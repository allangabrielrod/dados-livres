"""add table favorite def

Revision ID: afb3556458da
Revises: 4e44aa1c80c9
Create Date: 2020-03-31 15:08:32.870898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb3556458da'
down_revision = '4e44aa1c80c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sa.VARCHAR(length=600), nullable=True))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    # ### end Alembic commands ###
