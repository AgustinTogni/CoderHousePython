from django.urls import path
from clientes.views import *

app_name = "clientes"

urlpatterns = [
    path("", listar_clientes, name="listar_clientes"),
    path("crear_clientes/", crear_clientes, name="crear_clientes"),
    path("actualizar_clientes/<str:dni>/", actualizar_clientes, name="actualizar_clientes")
]