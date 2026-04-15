from django.contrib import admin
from productos.models import Productos

# Register your models here.

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("imagen", "numero_producto", "nombre", "marca", "precio", "stock", "ultima_actualizacion")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("numero_producto",)