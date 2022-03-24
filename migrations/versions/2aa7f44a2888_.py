"""empty message

Revision ID: 2aa7f44a2888
Revises: 8875c3544c0d
Create Date: 2022-03-23 14:37:06.976249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa7f44a2888'
down_revision = '8875c3544c0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('artist', 'website')
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('venue', 'website_link')
    op.add_column('artist', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('artist', 'website_link')
    # ### end Alembic commands ###
