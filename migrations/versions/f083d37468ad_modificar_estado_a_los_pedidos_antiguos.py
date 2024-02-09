"""modificar estado a los pedidos antiguos

Revision ID: 6a074731c793
Revises: 68117fffd182
Create Date: 2024-02-08 19:46:19.054400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a074731c793'
down_revision = '68117fffd182'
branch_labels = None
depends_on = None


def upgrade():
    # Si queremos realizar en la migracion un comando de ejecucion SQL podemos usar el metodo execute
    op.execute("UPDATE pedidos SET estado = 'EN_ESPERA' WHERE estado IS NULL")


def downgrade():
    pass
