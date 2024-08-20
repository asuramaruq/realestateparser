"""some_text

Revision ID: 61da35b2d6e2
Revises: 1838704fbb3e
Create Date: 2024-06-19 10:45:23.973870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61da35b2d6e2'
down_revision = '1838704fbb3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_building',
    sa.Column('buildingId', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('minPriceSqm', sa.Float(), nullable=True),
    sa.Column('minPrice', sa.Float(), nullable=True),
    sa.Column('minPriceSqmByLayouts', sa.Float(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('salesStatus', sa.String(), nullable=True),
    sa.Column('hasTaxInclusion', sa.Boolean(), nullable=True),
    sa.Column('isDeveloperPhoneShown', sa.Boolean(), nullable=True),
    sa.Column('developerCallTracking', sa.Boolean(), nullable=True),
    sa.Column('realtyCount', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('subLocalityNominative', sa.String(), nullable=True),
    sa.Column('constructionStatus', sa.String(), nullable=True),
    sa.Column('whatsAppPhone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('buildingId')
    )
    op.create_table('test_building_attributes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buildingId', sa.Integer(), nullable=True),
    sa.Column('att_name', sa.String(), nullable=True),
    sa.Column('att_value', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['buildingId'], ['test_building.buildingId'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_developer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buildingId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('developerId', sa.Integer(), nullable=True),
    sa.Column('isBranded', sa.Boolean(), nullable=True),
    sa.Column('hexColor', sa.String(), nullable=True),
    sa.Column('logoWhiteNoTextSvg', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['buildingId'], ['test_building.buildingId'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buildingId', sa.Integer(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['buildingId'], ['test_building.buildingId'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_building_attributes')
    op.drop_table('test_location')
    op.drop_table('test_developer')
    op.drop_table('test_building')
    # ### end Alembic commands ###
