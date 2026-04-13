from django import forms
from productos.models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            "imagen",
            "nombre", 
            "precio", 
            "stock"
        ]

        widgets = {
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"})
        }

        error_messages = {
            "imagen": {
                "invalid_image": "El archivo no es una imagen válida o está corrupto.",
                "required": "La imagen es obligatoria.",
            },
            "nombre": {
                "required": "El nombre del producto es obligatorio.",
                "max_length": "El nombre del producto no puede superar los 100 caracteres.",
            },
            "precio": {
                "required": "El precio es obligatorio.",
                "max_digits": "El precio excede la cantidad de dígitos permitidos.",
                "max_decimal_places": "El precio tiene demasiados decimales.",
            },
            "stock": {
                "required": "El stock es obligatorio.",
                "invalid": "Ingresá un número válido para el stock.",
                "min_value": "El stock no puede ser negativo.",
            }
        }

class ProductosUpdateForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            "imagen",
            "nombre", 
            "precio", 
            "stock"
        ]

        widgets = {
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"})
        }

        error_messages = {
            "imagen": {
                "invalid_image": "El archivo no es una imagen válida o está corrupto.",
            },
            "nombre": {
                "required": "El nombre del producto es obligatorio.",
                "max_length": "El nombre no puede superar los 100 caracteres.",
            },
            "precio": {
                "required": "El precio es obligatorio.",
                "max_digits": "El precio excede la cantidad de dígitos permitidos.",
                "max_decimal_places": "El precio tiene demasiados decimales.",
            },
            "stock": {
                "required": "El stock es obligatorio.",
                "invalid": "Ingresá un número válido para el stock.",
                "min_value": "El stock no puede ser negativo.",
            }
        }