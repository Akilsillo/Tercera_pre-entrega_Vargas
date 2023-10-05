from django.urls import path
from FirstApp.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('juegos/', games, name="Games"),
    path('proyectos/', projectsToDo, name="Projects"),
    path('hobbies/', hobbies, name="Hobbies"),
    path('buscar_juego/', searchGame, name="Buscar_juego"),
]
