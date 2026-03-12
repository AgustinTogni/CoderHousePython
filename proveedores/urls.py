from django.urls import path
from proveedores.views import *

app_name = "proveedores"

urlpatterns = [
    path("", listar_proveedores, name="listar_proveedores")
]