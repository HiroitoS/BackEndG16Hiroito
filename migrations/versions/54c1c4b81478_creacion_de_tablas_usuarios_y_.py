"""creacion de tablas usuarios y direcciones

Revision ID: 54c1c4b81478
Revises: 
Create Date: 2024-01-25 19:33:19.819720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54c1c4b81478'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('correo', sa.String(length=100), nullable=True),
    sa.Column('sexo', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('direcciones',
    sa.Column('<built-in function id>', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('calle', sa.Text(), nullable=True),
    sa.Column('numero', sa.Text(), nullable=True),
    sa.Column('referencias', sa.Text(), nullable=True),
    sa.Column('predeterminada', sa.Boolean(), nullable=True),
    sa.Column('usuarios_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuarios_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('<built-in function id>')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('direcciones')
    op.drop_table('usuarios')
    # ### end Alembic commands ###
