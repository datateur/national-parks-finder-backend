"""empty message

Revision ID: 00d3724ec67a
Revises: 55508b89bc28
Create Date: 2023-02-11 19:49:05.035522

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '00d3724ec67a'
down_revision = '55508b89bc28'
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
    sa.Column('types', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('addresses', sa.ARRAY(sa.JSON()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('park')
    # ### end Alembic commands ###