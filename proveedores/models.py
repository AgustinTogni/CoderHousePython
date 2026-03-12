from django.db import models

# Create your models here.

class Proveedores(models.Model):
    numero_proveedor = models.PositiveIntegerField(unique=True)
    negocio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_telefonico = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.negocio