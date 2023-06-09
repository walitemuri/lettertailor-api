"""adding set null on delete constraint

Revision ID: cbf201d9c30e
Revises: 262fe50e80b0
Create Date: 2023-05-02 20:01:58.062122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf201d9c30e'
down_revision = '262fe50e80b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_resume_id_key', 'users', type_='unique')
    op.drop_constraint('users_resume_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'resume', ['resume_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_resume_id_fkey', 'users', 'resume', ['resume_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint('users_resume_id_key', 'users', ['resume_id'])
    # ### end Alembic commands ###
