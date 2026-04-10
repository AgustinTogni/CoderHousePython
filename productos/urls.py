from django.urls import path
from productos.views import *

app_name = "productos"

urlpatterns = [
    path("", listar_productos, name="listar_productos"),
    path("crear_productos/", crear_productos, name="crear_productos")
]