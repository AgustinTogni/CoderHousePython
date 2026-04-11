from django.urls import path
from productos.views import *

app_name = "productos"

urlpatterns = [
    path("", ProductosListView.as_view(), name="listar_productos"),
    path("crear_productos/", ProductosCreateView.as_view(), name="crear_productos"),
    path("visualizar_productos/<int:numero_producto>/", ProductosDetailView.as_view(), name="visualizar_producto"),
    path("actualizar_productos/<int:numero_producto>/", ProductosUpdateView.as_view(), name="actualizar_productos"),
    path("eliminar_productos/<int:numero_producto>/", ProductosDeleteView.as_view(), name="eliminar_productos")
]