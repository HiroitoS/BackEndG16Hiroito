from flask import Flask
from variables import conexion

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


if __name__ == '__main__':
    app.run(debug=True)