from sqlalchemy import Column, types
#  Si queremos  utilizar un tipo de dato especial para un determinado 
# motor de base de datos
# from sqlalchemy.dialects.postgressql.types import MONEY
from variables import conexion
# PAraindicar que estra clase sera una tabla en la base de datostuilizamos
# conexion a la base de datos
class UsuarioModel(conexion.Model):
    id = Column(name= 'id', 
                type_=types.Integer,
                autoincrement= True,
                primary_key=True)
    # si no colocamos el parametro name entonces el nombre de la columna sera el mismo que 
    # el nombre del atributo
    # nulable > puede admitir valores nulos o no, su valor por defecto es TRUE
    nombre = Column(type_=types.String(100), nullable=False)
    apellido = Column(type_ = types.String(100))
    fechaNacimiento = Column(name = 'fecha_nacimiento', type_=types.Date)
    correo = Column(type_=types.String(100), unique=True, nullable=False)
    sexo = Column(type_=types.String(50), server_default='NINGUNO')
    # cuando agrgamos una nueva columna y la tabla ya existe al utilizar un va
    activo = Column(type_=types.Boolean, server_default='1')
    # ahora para indicar como queremos que se llame esta tabla en la bd
    __tablename__ = 'usuarios'
