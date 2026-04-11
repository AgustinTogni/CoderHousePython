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