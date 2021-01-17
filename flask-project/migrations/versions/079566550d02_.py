"""empty message

Revision ID: 079566550d02
Revises: 
Create Date: 2021-01-15 13:12:07.032162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079566550d02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('desgination', sa.String(length=200), nullable=False))
    op.add_column('employee', sa.Column('email', sa.String(length=100), nullable=False))
    op.add_column('employee', sa.Column('number', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'number')
    op.drop_column('employee', 'email')
    op.drop_column('employee', 'desgination')
    # ### end Alembic commands ###
