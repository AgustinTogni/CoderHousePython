from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

def get_code():
    return uuid.uuid4().hex

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Perfiles(AbstractUser):
    numero_usuario = models.PositiveIntegerField(unique=True)
    dni = models.CharField(max_length=8, unique=True)
    numero_telefonico = models.CharField(max_length=10, unique=True)
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/default.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )

    def __str__(self):
        return f"Usuario: {self.username} - Numero: {self.numero_usuario}"