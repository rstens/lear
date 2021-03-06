"""empty message

Revision ID: 52553d4d6309
Revises: 441a5e6cf682
Create Date: 2019-12-06 13:42:23.908893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52553d4d6309'
down_revision = '441a5e6cf682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('colin_last_update_last_event_id_key', 'colin_last_update', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('colin_last_update_last_event_id_key', 'colin_last_update', ['last_event_id'])
    # ### end Alembic commands ###
