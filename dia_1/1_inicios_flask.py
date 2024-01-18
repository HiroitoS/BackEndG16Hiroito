from flask import Flask, request
# request > donde se almacenara toda la infromacion de la peticion actual del cliente
#cada vez que el cleinte realice una peticion toda esa informacion se almacenara en el request

# variable de python que sirve para indicar 
# si el archivo que estanmos utilizando es el archivo principal del proyecto 
# esto srive para que la instancia de flask solamente corra en el archivo 
#princiapl y asi evitar instancias de flask en archivos secundarios del proyecto

app = Flask(__name__)# es el encargado de crear mi servidor del backemd

# si el archivo es el archivo proncipal el calor de __name__  sera __main__

# Decoradores
#srive para utilizar un metodo son la necesidad de modificarlo desde la clase en la cual
#estamos haciendo la referencia
@app.route('/', methods = ['GET', 'POST','PUT'])

def inicio():

    if request.method == 'PUT':

        return{
            'message':'Actualizacion exitosa'
        },202 #estado de respuesta http(ok)
    elif request.method == 'GET':
        return{
            'message':'Devolucion existosa'
        },200 # ok
    elif request.method == 'POST':
        return{
            'message':'Creacion existosa'
        }, 201#created
    

    print(request.method)

    return{
        'message': 'Bienvenido a mi primera API con Flask',
        'content': 'Hola'
    }

#levantamos nuestro servidor de flask

app.run(debug=True)