from django.contrib import admin
from clientes.models import Clientes

# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("numero_negocio", "negocio", "nombre", "apellido", "dni", "numero_telefonico", "email")
    list_display_links = ("negocio",)
    search_fields = ("negocio",)
    ordering = ("numero_negocio",)