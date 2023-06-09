"""adding file row to Res Table

Revision ID: 762de9d606b6
Revises: cbf201d9c30e
Create Date: 2023-05-07 23:43:00.823295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '762de9d606b6'
down_revision = 'cbf201d9c30e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resume', sa.Column('resume_file', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resume', 'resume_file')
    # ### end Alembic commands ###
