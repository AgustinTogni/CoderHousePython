from django import forms
from productos.models import Productos

class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = [
            "numero_producto", 
            "nombre", 
            "precio", 
            "stock",
        ]

        widgets = {
            "numero_producto": forms.NumberInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
        }