from django import forms
from proveedores.models import Proveedores

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = [
            "numero_proveedor",
            "negocio",
            "nombre",
            "apellido",
            "numero_telefonico",
            "email"
        ]

        widgets = {
            "numero_proveedor": forms.NumberInput(attrs={"class": "form-control"}),
            "negocio": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "numero_telefonico": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
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