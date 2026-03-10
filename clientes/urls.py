from django.urls import path
from clientes.views import *

urlpatterns = [
    path("", listar_clientes, name="listar_clientes")
]