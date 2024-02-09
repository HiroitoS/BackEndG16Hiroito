"""agregue valor default al estado

Revision ID: 68117fffd182
Revises: ab8244705cd8
Create Date: 2024-02-08 19:31:47.393665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68117fffd182'
down_revision = 'ab8244705cd8'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='pedidos', column_name='estado',
                    server_default='EN_ESPERA')
    


def downgrade():
    op.alter_column(table_name='pedidos', 
                    column_name='estado',server_default=None)
