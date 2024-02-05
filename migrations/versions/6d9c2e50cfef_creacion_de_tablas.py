"""creacion de tablas

Revision ID: 6d9c2e50cfef
Revises: 
Create Date: 2024-02-04 22:50:32.858712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d9c2e50cfef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tragos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('disponible', sa.Boolean(), server_default='1', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('estado', sa.Enum('ATENDIDO', 'EN_ESPERA', 'PREPARANDO', 'PREPARADO', name='estadopedidoenum'), nullable=True),
    sa.Column('invitado_id', sa.Integer(), nullable=False),
    sa.Column('man_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invitado_id'], ['invitados.id'], ),
    sa.ForeignKeyConstraint(['man_id'], ['barmans.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalle_pedido',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('trago_id', sa.Integer(), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedidos.id'], ),
    sa.ForeignKeyConstraint(['trago_id'], ['tragos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalle_pedido')
    op.drop_table('pedidos')
    op.drop_table('tragos')
    # ### end Alembic commands ###
