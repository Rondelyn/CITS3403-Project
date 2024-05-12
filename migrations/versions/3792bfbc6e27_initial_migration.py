"""Initial migration.

Revision ID: 3792bfbc6e27
Revises: e2ee78265483
Create Date: 2024-05-11 20:02:59.249081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3792bfbc6e27'
down_revision = 'e2ee78265483'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        
        batch_op.drop_column('user_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=128), nullable=False))

    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(length=10), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['user_id'])

    # ### end Alembic commands ###
