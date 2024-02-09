from flask import Flask
from flask_migrate import Migrate
from variables import conexion
from dotenv import load_dotenv
# os > operating system
from os import environ
from models import *
from controllers import *
from flask_restful import Api
from flask_jwt_extended import JWTManager, get_jwt_identity
from datetime import timedelta
from decoradores import validar_barman
from models.pedido import EstadoPedidoEnum


# leera el archivo .env si existe y agregara las variablesal entorno 
#como si fueses variables de entorno del sistema
# tiene que ir en la parte mas alta del archivo principal para que pueda ser utilizado en otdo el proyecto
load_dotenv()


app= Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# configuraciones para mi JWT



app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCES_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=30) #90

conexion.init_app(app)

JWTManager(app=app)
# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app, db=conexion)

# Agrego mis rutas

api.add_resource(InvitadosController, '/invitados')
api.add_resource(BarmanController, '/barman')
api.add_resource(LoginController, '/login')
api.add_resource(LoginInvitadoController, '/login-invitado')
api.add_resource(PedidosController, '/pedidos')



@app.route('/preparar-pedido/<int:id>', methods=['POST'])
@validar_barman
def prepararPedido(id):
    barmanId=get_jwt_identity()
    # primero buscar si existe el pedido con ese id

    # buscar si el pedido aun no tiene un barman seleccionado
    pedido_encontrado = conexion.session.query(Pedido).filter(
        Pedido.id == id, Pedido.barmanId == None).first()
    # si lo tiene entonces retornar un 400 e indicar que el pedido ya tiene un barman
    if not pedido_encontrado:
        return{
            'message': 'EL pedido a buscar no existe o ya fue tomado por otro barman'
        }, 400
    #Actualizar el pedido y configurar el barman y cambiar el estado del pedido a 'PREPARADO'
    conexion.session.query(Pedido).filter_by(
        id=pedido_encontrado.id).update({
            Pedido.barmanId: barmanId, 
            Pedido.estado:EstadoPedidoEnum.PREPARANDO
        })
    conexion.session.commit()

    return{
        'message': 'Pedido configurado existosamente'
    }

@app.route('/pedido-preparado/<int:id>', methods=['POST'])
@validar_barman
def pedidoPreparado(id):
    barmanId = get_jwt_identity()
    #buscar el pedido con el id y con el barmanId
    pedido_encontrado = conexion.session.query(Pedido).filter(
        Pedido.id == id, 
        Pedido.barmanId == barmanId,
        Pedido.estado == EstadoPedidoEnum.PREPARANDO
        ).first()

    # Si no existe el pedido indicar que no existe
    if not pedido_encontrado:
        return{
            'message': 'El pedido no existe'
        },400
    #Cambiar su estado a 
    conexion.session.query(Pedido).filter(
        Pedido.id==pedido_encontrado.id).update({
            Pedido.estado:EstadoPedidoEnum.PREPARADO
        })
    conexion.session.commit()
    return{
        'message': 'Pedido encontrado'
    },200
    

if __name__ == "__main__":
    app.run(debug= True)

