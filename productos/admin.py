from django.contrib import admin
from productos.models import Productos

# Register your models here.

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("numero_producto", "nombre", "precio", "stock")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("numero_producto",)