from django.shortcuts import render # devolver un html django django fue pensando para trabjar una aplicacion monolitica
from rest_framework.decorators import api_view
from rest_framework.response import Response




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