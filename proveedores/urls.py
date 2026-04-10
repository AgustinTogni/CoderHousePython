from django.urls import path
from proveedores.views import *

app_name = "proveedores"

urlpatterns = [
    path("", listar_proveedores, name="listar_proveedores"),
    path("crear_proveedores/", crear_proveedores, name="crear_proveedores"),
    path("actualizar_proveedores/<str:numero_proveedor>/", actualizar_proveedores, name="actualizar_proveedores")
]