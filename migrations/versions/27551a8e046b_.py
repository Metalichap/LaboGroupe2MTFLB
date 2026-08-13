"""empty message

Revision ID: 27551a8e046b
Revises: 28cca5e08257
Create Date: 2026-08-13 08:19:02.443176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '27551a8e046b'
down_revision = '28cca5e08257'
branch_labels = None
depends_on = None


priority_level_enum = postgresql.ENUM(
    'URGENT', 'NORMAL', 'LOW',
    name='prioritylevel'
)


def upgrade():
    #creating enum
    priority_level_enum.create(op.get_bind(), checkfirst=True)

    #alter column
    with op.batch_alter_table('priorities', schema=None) as batch_op:
        batch_op.alter_column(
            'priority_level',
            existing_type=sa.INTEGER(),
            type_=priority_level_enum,
            existing_nullable=False,
            postgresql_using='priority_level::text::prioritylevel'  # important, voir plus bas
        )


def downgrade():
    with op.batch_alter_table('priorities', schema=None) as batch_op:
        batch_op.alter_column(
            'priority_level',
            existing_type=priority_level_enum,
            type_=sa.INTEGER(),
            existing_nullable=False
        )


    priority_level_enum.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###