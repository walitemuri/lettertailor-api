"""empty message

Revision ID: ffd5e296e5b1
Revises: ced321c995a4
Create Date: 2023-05-01 02:03:40.145638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd5e296e5b1'
down_revision = 'ced321c995a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resume', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resume', 'created_at')
    # ### end Alembic commands ###
