from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS


app = Flask(__name__)

# Para configurar mis CORS lo hago de la  siguiente manera
# Si lo dejamos sin nu¿inguna configuracion adicional lo que va a suceder 
#es que en teoria va a permitir que todos los origenes y todos  los metodos 
#y todos los headers sean permitidos
CORS(app=app, 
     # que metodos pueden acceder a mi API
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     # que dominios, puede acceder a mi API, si queremos que cualquier origen se conecte colocamos el *
     origins=['http://localhost:5500', 'http://127.0.0.1:5500'], 
     # que headers (cabeceras), pueden enviar a mi API, '*
     allow_headers=['accept', 'authorization', 'content-type']
    )

productos= [
    {
        'id' : uuid4(),
        'nombre' : 'Palta fuerte',
        'precio' : 7.50,
        'disponibilidad' : True
    },
    {
        'id' : uuid4(),
        'nombre' : 'Lechuga Carola',
        'precio' : 1.50,
        'disponibilidad' : True
    }
]

@app.route('/', methods = ['GET'])
def incio():
    return{
        'message': 'Bienvenido a la API productos'
    }, 200
@app.route('/productos', methods = ['GET'])
def gestionProdcutos():
    return{
        'message': 'Los productos son',
        'content' : productos
    },200

# si voy a recibir un parametro dianmico (que va a cambiar su valor) y eso lo voy a manejar internamente
# Los formatos que puedo parsear son:
# String > recibir texto
# int > para recibbir solo numeros
# float> para recibir numeros con puntos
#path > que con string pero tmb acoetan slashes
#uuid> acpetar UUID's
# al colocar un parseador su el formato que me envia el cliente no cumple con esta conversion no acpetara la conversion

@app.route('/producto/<uuid:id>', methods = ['GET'])
def gestionProducto(id):
    # tenemos una lista de productos en el cual en cada posicion tenemos un diccionario y una llave llamada id
    # iteren esos productos y vean si existe el producto con determinado id
    #si no existe entonces retornar un message que diga 'Producto no esxiste' con un estado 404
    #PISTA: hacer un for con if y else de el 
    for producto in productos:
        if producto['id'] == id:
            return{
                'content': producto
            },200
        
    return{
        'message': 'producto no existe'
    },404

@app.route('/producto', methods=['POST'])
def crearProductos():
    data = request.get_json()# convierte la data del body en un diccionario en un json
    # antes de guardar la informacion en los productos agregarle el id
    data['id'] = uuid4()
    productos.append(data)
    return{
        'message': 'Producto creado exitosamente',
        'content': data
    }, 201# Created

if __name__ == '__main__':
    app.run(debug=True)