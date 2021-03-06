"""added language for posts

Revision ID: 3570da67eb96
Revises: 3a2d6e380a53
Create Date: 2021-01-20 13:57:31.676150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3570da67eb96'
down_revision = '3a2d6e380a53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
