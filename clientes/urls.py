from django.urls import path
from clientes.views import *

app_name = "clientes"

urlpatterns = [
    path("", listar_clientes, name="listar_clientes")
]