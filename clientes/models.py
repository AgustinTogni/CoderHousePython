from django.db import models

# Create your models here.

class Clientes(models.Model):
    negocio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=9, unique=True)
    numero_telefonico = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.negocio