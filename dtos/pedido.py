from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Pedido, DetallePedido, Trago
from models.pedido import EstadoPedidoEnum
from marshmallow_enum import EnumField

class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)



class CrearPedidoDTO(Schema):
    # nested sirve para indicar que esta anidado
    detalle = fields.List(fields.Nested(ItemPedidoDTO))

class TragoDTO(SQLAlchemyAutoSchema):
    class Meta:
        model= Trago

        fields = ['nombre']


class DetallePedidoDTO(SQLAlchemyAutoSchema):
    trago = fields.Nested(nested=TragoDTO, attribute='trago')
    class  Meta:
        model = DetallePedido
        fields = ['trago', 'cantidad']
        # si queremos mostrar las llavaes foraneas de nuestro modelo entonces definimos el atributos include_fk con True
        # include_fk = True

class ListarPedidosDTO(SQLAlchemyAutoSchema):
    # cuando en un modelo tenemos una columna que va a ser de tipo enum tenemos que
    # indicar a Marshmallow
    # tenemos que indicar que enum tiene que utilizar para hacer las conversiones correspondientes
    estado = EnumField(EstadoPedidoEnum)
    # si colocamos un nombre diferente del atributo virtual entonoces no hara match y por ende no mostrara la 
    # informacion, caso contrario si concuerda mostrara la informacion
    # en ese caso como un pedido 
    # puede tener muchos detallePedidos tenemos que colocar el parametro many = True
    # para que lo itere
    # si quisieramos cambiar el nombre a mostrar entonces deberiamos colocar el parametro atribute
    # hacemos esto, entonces el atributo include:relationships ya no debe estar presente en el DTO

    detallePedidos = fields.Nested(
        nested=DetallePedidoDTO, many=True, attribute= 'detallePedidos')

    class Meta:
        model = Pedido
         #
        include_relationships = True