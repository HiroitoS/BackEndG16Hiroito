from django.shortcuts import render # devolver un html django django fue pensando para trabjar una aplicacion monolitica
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato
from .serializers import PlatoSerializers
from rest_framework import status
from os import remove



def vistaPrueba(request):
    usuario = {
        'nombre': 'Hiroito',
        'apellido': 'Sanchez',
        'hobbies': [
            {
                'descripcion': 'Jugar futbol'
            },
            {
                'descripcion': 'Comer'
            }
        ]
    }
    return render(request=request, template_name='prueba.html', context= usuario)

def mostrarRecetas(request):
    return render(request, 'mostrarRecetas.html')

# siempre en una funcion que trbaja como controlador recibiremos el request (informacion entrante del cliente)
@api_view(http_method_names=['GET', 'POST'])
def controlladorInicial(request):
    return Response (data={
        'message': 'Bienvenido a mi API'
    })
class PlatosController(APIView):
    def get(self, request):
        # select * from platos
        resultado = Plato.objects.all()
        print(resultado) 
        # instance>cuando tenemos instancias de modelo para serializar
        # data> cuando tenemos informacion que vamos a guardar, modificar en la base de datos proveniente del cliente
        serializador = PlatoSerializers(instance=resultado, many=True)
        return Response(data={
            'message': 'Me hicieron un get',
            'content': serializador.data

        })
    
    def post(self, request):
        print(request.data)
        serializador = PlatoSerializers(data=request.data)
        validacion= serializador.is_valid()# valida si la informacion enviada por el cliente es correcta o no, osea devolvera un booleano
        if validacion:
            #el serializador al momento de vincularlo con un modelo se crea metodos para guardar (save) y actualizar (update)
            serializador.save()

            return Response(data={
                'message': 'Plato creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
           'message': 'Error al crear el plato', 
            'content': serializador.errors # errores al moemnto de hacer la validacion
            }, status=status.HTTP_400_BAD_REQUEST)
        
class PlatoController(APIView):
    def get(self, request, id):
        plato_encontrado = Plato.objects.filter(id=id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        serializador = PlatoSerializers(instance=plato_encontrado)
        return Response(data={
            'content': serializador.data
        })
    def put(self, request, id):
        plato_encontrado = Plato.objects.filter(id=id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        imagen_antigua= plato_encontrado.foto.path

        serializador = PlatoSerializers(data=request.data)

        if serializador.is_valid():
            # es un metodo que tmb se encuentra al momento de usar un MOdelSerializer y sirve para actualizarel registro 
            # sin mucho trabajo
            resultado=serializador.update(instance=plato_encontrado, 
                                validated_data=serializador.validated_data)
            print(resultado)
            # ya se actualizo mi registro en la base de datos
            remove(imagen_antigua)
            return Response(data={
                'message':'Plato actualizado existosamente'
            })
        else:
            return Response(data={
                'message': 'Error al actualizar el plato',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        plato_encontrado = Plato.objects.filter(id=id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_antigua = plato_encontrado.foto.path

        Plato.objects.filter(id=id).delete()

        remove(imagen_antigua)

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)