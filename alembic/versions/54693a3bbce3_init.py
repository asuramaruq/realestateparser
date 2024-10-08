"""init

Revision ID: 54693a3bbce3
Revises: baa875906414
Create Date: 2023-07-11 15:24:18.777642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54693a3bbce3'
down_revision = 'baa875906414'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('developer', sa.Column('buildingId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'developer', 'building', ['buildingId'], ['buildingId'])
    op.add_column('location', sa.Column('buildingId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'location', 'building', ['buildingId'], ['buildingId'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_column('location', 'buildingId')
    op.drop_constraint(None, 'developer', type_='foreignkey')
    op.drop_column('developer', 'buildingId')
    # ### end Alembic commands ###
