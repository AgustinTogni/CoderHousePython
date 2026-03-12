from django.urls import path
from clientes.views import *

app_name = "clientes"

urlpatterns = [
    path("", listar_clientes, name="listar_clientes"),
    path("crear_clientes/", crear_clientes, name="crear_clientes"),
    path("buscar_clientes/", buscar_clientes, name="buscar_clientes")
]