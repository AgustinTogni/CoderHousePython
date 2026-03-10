from django.urls import path
from proveedores.views import *

urlpatterns = [
    path("", listar_proveedores, name="listar_proveedores")
]