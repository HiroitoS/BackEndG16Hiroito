from flask import request
from flask import Flask
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel
from flask_migrate import Migrate
from datetime import datetime
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)
print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto flask
# NOTA: No confundir con las variables de entorno!

# ahora agregamos una nueva llave a nuestra variable de configuracion 

#dialecto://usuario:contraseña@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'

# Inicializar la conexion a nuestra BD
# al momento de pasarle la aplicacion de flask en esta se encontrara la cadenas de conexion a la BD

conexion.init_app(app)


# #Migrate sirve para registrar los cambios en nuestra base de datos realizados desde nuestra ORM
Migrate(app=app, db=conexion)
# # before_request > se mandara a llamar a esta funcionalidad antes de cualquier request(peticion)
# @app.before_request
# def inicializacion():
# # create_all >  crea todas las tablas que no se han creado en la BD
#     conexion.create_all()

class UsuarioDTO(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str()
    correo = fields.Email(required=True) # hace la validacion que contenga un @
    fechaNacimiento = fields.Date()
    sexo = fields.Str()

class UsuarioModelDTO(SQLAlchemyAutoSchema):
    class Meta:
        # model sirve para indicar desde que modelo nos vamos a referenciar para jalar toda la informacion de nuestro DTO
        # en base a las columnas las configuraciones para pedir el tipo de dato necesario, si es que null o no 
        #si es AI ya no lo pide ni las llaves primarias y toda la configuracion
        model = UsuarioModel


@app.route('/usuarios', methods=['GET'])
def gestionarUsuarios():
    # session > una actividad que tenemos con la base de datos 
    # SELECT * FROM
    resultado = conexion.session.query(UsuarioModel).all()
    # el moetdo dump solamente convertira un usuario a la vez
    # a no se que le coloquemos el parametro que le estamos pasando muchos
    # many indicamos que le estamos pasando una lista de registros por lo que lo s tendra que oterar y convertir cada uno de ellos 
    validador = UsuarioModelDTO()

    usuarios = validador.dump(resultado, many=True)
    # usuarios = []
    # for usuario in resultado:
    #     usuarios.append({
    #         'id': usuario.id,
    #         'nombre' : usuario.nombre,
    #         'apellido': usuario.apellido,
    #         'correo': usuario.correo,
    #         'sexo': usuario.sexo,
    #         # string from time > oconvertir un valor de tipo fecha y hora a string pero colocando el formato
    #         # %Y> devolver el año 
    #         # %y > devolver los dos ulrimo digitos del año
    #         # %m > devuelve los digitos del mes
    #         # %B > devuelve el nombre del mes
    #         # %b > devuelve las tres primeras letras del mes
    #         # %d> dia del mes
    #         # %H > hora
    #         # %M > minutos
    #         # %S > segundos
    #         'fechaNacimiento': datetime.strftime(usuario.fechaNacimiento, '%Y-%m-%d')
    #     })
    print(usuarios)
    return{
        'content' : usuarios
    }, 200

@app.route('/usuario', methods=['POST'])
def crearUsuario():
    try:
        #capturar la informacion
        data = request.get_json()
        # validador = UsuarioDTO()
        validador = UsuarioModelDTO()
        # pasarle la informacion y ver si es correcta o no y si lo es devolvera la informacion transformada
        dataValidada = validador.load(data)

        
        
        #creo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**dataValidada)
        
    
    
        conexion.session.add(nuevoUsuario)
        print('Antes del commit',nuevoUsuario.id)
        # commit sirve para transacciones y permite que todos los cambios realizados en la base de datos permanezcan de 
        #manera persistente

        conexion.session.commit()
        print('despues del commit',nuevoUsuario.id)
        # usuarioCreado = {
        #     'id': nuevoUsuario.id,
        #     'nombre': nuevoUsuario.nombre,
        #     'apellido': nuevoUsuario.apellido,
        #     'correo' : nuevoUsuario.correo,
        #     'sexo' :nuevoUsuario.sexo,
        #     'fechaNacimiento' :datetime.strftime(nuevoUsuario.fechaNacimiento, '%Y-%m-%d')
        # }
        usuarioCreado =  validador.dump(nuevoUsuario)

        return{
            'message' : 'Usuario creado exitosamente',
            'content' : usuarioCreado
        },201
    except Exception as error:
        return{
            'message': 'Error al crear el usuario',
            'content' : error.args
        },400
    

@app.route('/usuario/<int:id>', methods = ['GET'])
def gestionarUsuario(id):
    usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
    # si queremos definir que columnas utilizar al momento de hacer la consulta
    prueba = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.correo, UsuarioModel.nombre).all()
    print(prueba)
    if usuarioEncontrado is None:
        return{
            'message' : 'El usuario no existe'
        }, 404

    # usar el UsuarioModelDTO para devolver la informacion
    validador = UsuarioModelDTO()
    resultado = validador.dump(usuarioEncontrado)
    return{
        'content' : resultado
    },200



@app.route('/')
def incial():
    return{
        'message':'Bienvenido a mi API de usuarios'
    },

if __name__ == '__main__':
    app.run(debug=True)