"""empty message

Revision ID: 9f401b62bd53
Revises: 06b4a2f91705
Create Date: 2023-02-09 10:26:10.809085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f401b62bd53'
down_revision = '06b4a2f91705'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('park',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('park_code', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('activities', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('topics', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('states', sa.String(), nullable=True),
    sa.Column('phone_numbers', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('emails', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('designation', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('park')
    # ### end Alembic commands ###