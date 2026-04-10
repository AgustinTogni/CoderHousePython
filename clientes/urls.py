from django.urls import path
from clientes.views import *

app_name = "clientes"

urlpatterns = [
    path("", listar_clientes, name="listar_clientes"),
    path("crear_clientes/", crear_clientes, name="crear_clientes"),
    path("visualizar_clientes/<str:dni>/", visualizar_clientes, name="visualizar_clientes"),
    path("actualizar_clientes/<str:dni>/", actualizar_clientes, name="actualizar_clientes"),
    path("eliminar_clientes/<str:dni>/", eliminar_clientes, name="eliminar_clientes")
]