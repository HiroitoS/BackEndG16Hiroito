from flask import Flask
from flask_migrate import Migrate
from variables import conexion, clienteTwilio
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
from flasgger import Swagger
from json import load


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

swaggerConfig={
    'headers':[],# las cabeceras que podra aceptar nuestra documentacion
    'specs':[
        {
            'endpoint': '',# el endpoint incial de nuestra documentacion 
            # mi ruta base de mi documentacion (hacia donde hara los request)
            'route': '/'
        }
    ],
    # Donde cargara los archivos staticos de swagger para la interfaz grafica 
    # para idnicar esto tenemos que colocar la opcion 'swagger_ui: True sino podemos
    # obviar este paso
    'static_url_path': '/flassger_static',
    # el endpoint en el cual ahora estara alojada la documentacion de swagger 
    'specs_route': '/documentacion'

}


swaggerTemplate= load(open('swagger_template.json'))

Swagger(app=app, template=swaggerTemplate, config=swaggerConfig)

JWTManager(app=app)
# Esto crea la utilizacion de las migraciones en nuestro proyecto de flask
Migrate(app=app, db=conexion)

# Agrego mis rutas

api.add_resource(InvitadosController, '/invitados')
api.add_resource(BarmanController, '/barman')
api.add_resource(LoginController, '/login')
api.add_resource(LoginInvitadoController, '/login-invitado')
api.add_resource(PedidosController, '/pedidos')
api.add_resource(TragosController, '/tragos')



@app.route('/preparar-pedido/<int:id>', methods=['POST'])
@validar_barman
def prepararPedido(id):
    """
    file: prepararPedido.yml
    """
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
            Pedido.estado:EstadoPedidoEnum.PREPARADO})
    
    
    conexion.session.commit()

    mensaje= clienteTwilio.messages.create(
        from_ = '+18704844820',
        to=f'+51{pedido_encontrado.invitado.telefono}',
        body = f'''Hola {pedido_encontrado.invitado.nombre}.
Tu pedido de la barra ya esta listo, puedes retirarlo 🍸'''
    )
    # sid> identificador del mensaje por si lo queremos validar en la pagina de twilio
    print(mensaje.sid)

    return{
        'message': 'Pedido encontrado'
    },200
    

if __name__ == "__main__":
    app.run(debug= True)

