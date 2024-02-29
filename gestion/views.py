from django.shortcuts import render # devolver un html django django fue pensando para trabjar una aplicacion monolitica
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plato, Ingrediente
from .serializers import (PlatoSerializers, IngredienteSerializer, PreparacionSerializer, 
                          PlatoConIngredientesYPreparacionesSerializer,
                          RegistroCheffSerializer,Cheff)
from rest_framework import status
from os import remove
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# IsadminUser > verificara si el usuario que envia la token es un usuario de tipo admin (is_superuser=True) y lo permitira hacer todo
# IsAuthenticated > verificara si hay una token en la peticion, no interesa que privilegios tenga ese usuario
# Is AuthenticatedReadOnly > si es un get o un options no necesita enviar una token, pero si es un post , put o delete si no manda
# token no le permitira hacer la operacion
# AllowAny > permite accedes a los recursos con o sin token

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


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
    permission_classes=[IsAuthenticatedOrReadOnly,]

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
        print(request.user)# instancia del usuario que esta haciendo la peticion y no hay devolvera None
        print(request.auth)# el metodo por el cual esta mandandno la autorizacion osea el JWT
        # agregamos una nueva propiedad a nuestra data que seria el id del cheff
        request.data['cheffId'] = request.user.id
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

    permission_classes=[IsAuthenticatedOrReadOnly,]

    def get(self, request, id):
        plato_encontrado = Plato.objects.filter(id=id).first()
        if not plato_encontrado:
            return Response(data={
                'message': 'El plato no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializador = PlatoConIngredientesYPreparacionesSerializer(instance=plato_encontrado)
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
    



class IngresdientesController(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):

        cheff = request.user
        # Validar la data con el serializador creado(IngredienteSerializer) y si es que no es correcto indicar que no lo es con un 
        # estado 400
        # caso contrario crear el ingrediente y retornar el mensaje de exito

        print(request.data)
        serializador = IngredienteSerializer(data=request.data)
        # buscar si el plato le pertenece a este cheff, si no no permitir el guardado
        # request. data > [descripcion: '100gr de azucar']

        validacion= serializador.is_valid()
        if validacion:
            plato_encontrado = serializador.validated_data.get('platoId')
           
            if plato_encontrado.cheffId and plato_encontrado.cheffId.id != cheff.id:
                # el cheff no es el propietario de ese plato{
                return Response(data={
                    'message': 'No tienes acceso para modificar'
                }, status=status.HTTP_401_UNAUTHORIZED)

            serializador.save()

            return Response(data={
                'message': 'Ingrediente creado exitosamente',
                'content': serializador.data # esto nos devolvera la infromacion agregada a la base de datos
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el ingrediente', 
                'content': serializador.errors 
            }, status=status.HTTP_400_BAD_REQUEST)
@api_view(http_method_names=['GET'])

def listarIngredientesPlato(request, id):
    ingrediente_encontrado = Ingrediente.objects.filter(platoId=id).all()
    if not ingrediente_encontrado:
        return Response({
            'message':'El plato no tiene ingredientes'
        })
    
    else:
        serializador = IngredienteSerializer(instance=ingrediente_encontrado, many=True)
        return Response({
            'content': serializador.data
        })


@swagger_auto_schema(method='post',
                     request_body=PreparacionSerializer,
                     responses={
                         201: openapi.Response('respuesta exitosa',
                                               examples={
                                                   'application/json': {
                                                       'message': 'Preparacion agregada con exitosamente al plato',
                                                       'content': {
                                                           'id': 1,
                                                           'descripcion': '',
                                                           'orden': 1,
                                                           'platoId': 10
                                                       }
                                                   }
                                               }),
                         400: openapi.Response('respuesta fallida',
                                               examples={
                                                   'application/json': {
                                                       'message': 'Error al crear la preparacion',
                                                       'content': ' errores'
                                                   }
                                               })})
@api_view(http_method_names=['POST'])
def crearPreparacion(request):
    serializador= PreparacionSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(data={
            'message': 'Preparacion agregada exitosamente al plato',
            'content': serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            'message': 'Error al crar la preparacion',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={201: openapi.Response(description = 'recetas', examples={
    'application/json':{
        'content': 'PlatoConIngredientesYPreparacionesModel'
    }
}, schema=PlatoConIngredientesYPreparacionesSerializer)})
@api_view(http_method_names=['GET'])
def buscarRecetas(request):
    print(request.query_params)
    #https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups
    if request.query_params.get('nombre'):
        # obtenemos el calor del query áram
        nombre= request.query_params.get('nombre')
        # buscamos los platos por su filtro
        resultado = Plato.objects.filter(
            nombre__icontains = nombre).all()#.query
        # le pasamos al serializador nuestro resultado
        serializador= PlatoConIngredientesYPreparacionesSerializer(
            instance=resultado, many=True)
        
        print(resultado)
        return Response(data={
            'content':serializador.data
        })
    else:
        return Response(data={
            'message': 'Falta el nombre en el query param'
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['POST'])
def crearCheff(request):
    serializador = RegistroCheffSerializer(data=request.data)
    if serializador.is_valid():
        nuevo_cheff = Cheff(nombre= serializador.data.get('nombre'), 
              correo = serializador.data.get('correo'))
        # set_password > sirve para generar el hash de nuestra password

        nuevo_cheff.set_password(serializador.validated_data.get('password'))    

        nuevo_cheff.save() 
        print(request.data.get('correo'))

        return Response(data={
            'message': 'cheff creado exitosamente',
            'content': serializador.data

        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            'message': 'Error al crear el cheff',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST0)