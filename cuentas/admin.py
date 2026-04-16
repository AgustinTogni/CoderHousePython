from django.contrib import admin
from cuentas.models import Perfiles

# Register your models here.

@admin.register(Perfiles)
class PerfilesAdmin(admin.ModelAdmin):
    list_display = ("numero_usuario", "username", "first_name", "last_name", "dni", "numero_telefonico", "email")
    list_display_links = ("username",)
    search_fields = ("username",)
    ordering = ("numero_usuario",)
