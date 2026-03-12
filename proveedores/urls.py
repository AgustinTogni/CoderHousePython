from django.urls import path
from proveedores.views import *

app_name = "proveedores"

urlpatterns = [
    path("", listar_proveedores, name="listar_proveedores"),
    path("crear_proveedores/", crear_proveedores, name="crear_proveedores"),
    path("buscar_proveedores/", buscar_proveedores, name="buscar_proveedores")
]