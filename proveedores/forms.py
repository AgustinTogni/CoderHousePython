from django import forms
from proveedores.models import Proveedores

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = [
            "negocio",
            "nombre",
            "apellido",
            "numero_telefonico",
            "email"
        ]

        widgets = {
            "negocio": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "numero_telefonico": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

        error_messages = {
            "negocio": {
                "required": "El nombre del negocio es obligatorio.",
                "max_length": "El negocio no puede superar los 100 caracteres.",
            },
            "nombre": {
                "required": "El nombre es obligatorio.",
                "max_length": "El nombre no puede superar los 100 caracteres.",
            },
            "apellido": {
                "required": "El apellido es obligatorio.",
                "max_length": "El apellido no puede superar los 100 caracteres.",
            },
            "numero_telefonico": {
                "required": "El teléfono es obligatorio.",
                "max_length": "El teléfono no puede superar los 10 caracteres.",
                "unique": "Ya existe un proveedor con este número de teléfono.",
            },
            "email": {
                "required": "El email es obligatorio.",
                "invalid": "Ingresá un email válido (ej: usuario@correo.com).",
                "unique": "Ya existe un proveedor con este email.",
            }
        }

class ProveedoresUpdateForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = [
            "negocio",
            "nombre",
            "apellido",
            "numero_telefonico",
            "email"
        ]

        widgets = {
            "negocio": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "numero_telefonico": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }

        error_messages = {
            "negocio": {
                "required": "El nombre del negocio es obligatorio.",
                "max_length": "El negocio no puede superar los 100 caracteres.",
            },
            "nombre": {
                "required": "El nombre es obligatorio.",
                "max_length": "El nombre no puede superar los 100 caracteres.",
            },
            "apellido": {
                "required": "El apellido es obligatorio.",
                "max_length": "El apellido no puede superar los 100 caracteres.",
            },
            "numero_telefonico": {
                "required": "El teléfono es obligatorio.",
                "max_length": "El teléfono no puede superar los 10 caracteres.",
                "unique": "Ya existe un proveedor con este número de teléfono.",
            },
            "email": {
                "required": "El email es obligatorio.",
                "invalid": "Ingresá un email válido (ej: usuario@correo.com).",
                "unique": "Ya existe un proveedor con este email.",
            },
        }