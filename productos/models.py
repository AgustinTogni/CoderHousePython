from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Productos(models.Model):
    numero_producto = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="El precio debe ser mayor a 0.")]
    )
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre