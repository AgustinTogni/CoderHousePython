from django.db import models

# Create your models here.

class Productos(models.Model):
    numero_producto = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre