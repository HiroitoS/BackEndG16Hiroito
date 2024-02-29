# aca estran declaradas todas las rutas relacionadas a la aplicacion de gestion
from django.urls import path
from .views import (mostrarRecetas, 
                    vistaPrueba, 
                    controlladorInicial, 
                    PlatosController, 
                    PlatoController,
                    IngresdientesController,
                    listarIngredientesPlato,
                    crearPreparacion,
                    buscarRecetas, crearCheff)

from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('prueba/', view=vistaPrueba),
    path('mostrar-recetas/', view=mostrarRecetas),
    path('prueba-drf/', view=controlladorInicial),
    path('platos/', view=PlatosController.as_view()),
    path('plato/<int:id>', view=PlatoController.as_view()),
    path('ingredientes/', view=IngresdientesController.as_view()),
    path('plato/<int:id>/ingredientes', view=listarIngredientesPlato),
    path('preparacion', view=crearPreparacion),
    path('buscar-recetas/', view=buscarRecetas),
    path('registro-cheff/', view=crearCheff),
    path('login/', view=TokenObtainPairView.as_view()),
]
