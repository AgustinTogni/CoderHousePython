from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            "negocio",
            "nombre",
            "apellido",
            "dni",
            "numero_telefonico",
            "email"
        ]

        widgets = {
            "negocio": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
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
            "dni": {
                "required": "El DNI es obligatorio.",
                "max_length": "El DNI no puede superar los 8 caracteres.",
                "unique": "Ya existe un cliente con este DNI.",
            },
            "numero_telefonico": {
                "required": "El teléfono es obligatorio.",
                "max_length": "El teléfono no puede superar los 10 caracteres.",
                "unique": "Ya existe un cliente con este número de teléfono.",
            },
            "email": {
                "required": "El email es obligatorio.",
                "invalid": "Ingresá un email válido (ej: usuario@correo.com).",
                "unique": "Ya existe un cliente con este email.",
            }
        }

class ClientesUpdateForm(forms.ModelForm):
    class Meta:
        model = Clientes
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
                "unique": "Ya existe un cliente con este número de teléfono.",
            },
            "email": {
                "required": "El email es obligatorio.",
                "invalid": "Ingresá un email válido (ej: usuario@correo.com).",
                "unique": "Ya existe un cliente con este email.",
            }
        }