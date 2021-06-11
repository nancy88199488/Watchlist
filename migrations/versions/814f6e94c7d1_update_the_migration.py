"""update the  Migration

Revision ID: 814f6e94c7d1
Revises: 05a0a147aa2f
Create Date: 2021-06-11 19:29:48.610170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814f6e94c7d1'
down_revision = '05a0a147aa2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
