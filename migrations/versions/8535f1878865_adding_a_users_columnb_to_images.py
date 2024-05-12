from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '8535f1878865'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Drop the existing _alembic_tmp_image table if it exists
    op.drop_table('_alembic_tmp_image')

    # Add the user_id column to the image table
    op.add_column('image', sa.Column('user_id', sa.String(length=10), nullable=True))

    # Populate the user_id column with default values
    op.execute("UPDATE image SET user_id = 'default_user_id'")

    # Add the foreign key constraint
    op.create_foreign_key('fk_image_user_id', 'image', 'user', ['user_id'], ['id'])

    # Modify the user_password column in the user table
    op.alter_column('user', 'user_password', existing_type=sa.VARCHAR(length=10), type_=sa.String(length=128), existing_nullable=False)

def downgrade():
    # Remove the foreign key constraint
    op.drop_constraint('fk_image_user_id', 'image', type_='foreignkey')

    # Remove the user_id column from the image table
    op.drop_column('image', 'user_id')

    # Modify the user_password column in the user table
    op.alter_column('user', 'user_password', existing_type=sa.String(length=128), type_=sa.VARCHAR(length=10), existing_nullable=False)
