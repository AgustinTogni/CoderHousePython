from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from cuentas.models import Perfiles

class PerfilesCreateForm(UserCreationForm):
    class Meta:
        model = Perfiles
        fields = [
            "username",
            "first_name",
            "last_name",
            "dni",
            "email",
            "numero_telefonico",
            "avatar"
        ]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "numero_telefonico": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }

        error_messages = {
            "username": {
                "required": "El usuario es obligatorio.",
                "unique": "Este nombre de usuario ya está en uso.",
                "max_length": "El usuario es demasiado largo.",
            },
            "first_name": {
                "max_length": "El nombre es demasiado largo.",
            },
            "last_name": {
                "max_length": "El apellido es demasiado largo.",
            },
            "dni": {
                "required": "El DNI es obligatorio.",
                "max_length": "El DNI no puede superar los 8 caracteres.",
                "unique": "Este DNI ya está registrado.",
            },
            "email": {
                "invalid": "Ingresá un email válido (ej: usuario@correo.com).",
            },
            "numero_telefonico": {
                "required": "El teléfono es obligatorio.",
                "max_length": "El teléfono no puede superar los 10 caracteres.",
                "unique": "Este número ya está registrado.",
            }
        }

        password1 = forms.CharField(
            label="Contraseña",
            widget=forms.PasswordInput(attrs={"class": "form-control"}),
            error_messages={
                "required": "La contraseña es obligatoria.",
            },
        )

        password2 = forms.CharField(
            label="Confirmar contraseña",
            widget=forms.PasswordInput(attrs={"class": "form-control"}),
            error_messages={
                "required": "Debés confirmar la contraseña.",
            },
        )

class PerfilesChangeForm(UserChangeForm):
    password = None

    password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = Perfiles
        fields = [
            "username",
            "first_name",
            "last_name",
            "dni",
            "email",
            "numero_telefonico",
            "avatar"
        ]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "numero_telefonico": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get("password1")

        if password1:
            user.set_password(password1)

        if commit:
            user.save()

        return user