from sqlalchemy import Column, types, ForeignKey
from variables import conexion
from enum import Enum
from sqlalchemy.sql import func
class EstadoPedidoEnum(Enum):
    ATENDIDO = 'ATENDIDO'
    EN_ESPERA = 'EN_ESPERA'
    PREPARANDO = 'PREPARANDO'
    PREPARADO = 'PREPARADO'



class Pedido(conexion.Model):
    __tablename__ = 'pedidos'

    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True)
    fecha_creacion = Column(type_=types.DateTime,
                            server_default=func.now(), 
                            nullable=False)
    
    estado = Column(type_=types.Enum(EstadoPedidoEnum), 
                    server_default=EstadoPedidoEnum.EN_ESPERA.value)

    invitadoId = Column(ForeignKey(column='invitados.id'), 
                      nullable=False, name='invitado_id')

    barmanId = Column(ForeignKey(column='barmans.id'),
                    name='man_id')
