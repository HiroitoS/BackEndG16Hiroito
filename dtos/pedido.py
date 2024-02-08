from marshmallow import Schema, fields


class ItemPedidoDTO(Schema):
    tragoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)



class CrearPedidoDTO(Schema):
    # nested sirve para indicar que esta anidado
    detalle = fields.List(fields.Nested(ItemPedidoDTO))