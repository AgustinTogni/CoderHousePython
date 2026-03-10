from django.urls import path
from productos.views import *

urlpatterns = [
    path("", listar_productos, name="listar_productos")
]