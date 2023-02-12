"""empty message

Revision ID: ee42dd6571e0
Revises: 8a32e97b4d9a
Create Date: 2023-02-11 17:26:33.474204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee42dd6571e0'
down_revision = '8a32e97b4d9a'
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
    sa.Column('activities', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('topics', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('states', sa.String(), nullable=True),
    sa.Column('phone_numbers', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('emails', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('fees', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('operating_hours', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('images', sa.ARRAY(sa.JSON()), nullable=True),
    sa.Column('designations', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('addresses', sa.ARRAY(sa.JSON()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('park')
    # ### end Alembic commands ###