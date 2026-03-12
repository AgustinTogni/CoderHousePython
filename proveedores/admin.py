from django.contrib import admin
from proveedores.models import Proveedores

# Register your models here.

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ("numero_proveedor", "negocio", "nombre", "apellido", "numero_telefonico", "email")
    list_display_links = ("negocio",)
    search_fields = ("negocio",)
    ordering = ("numero_proveedor",)