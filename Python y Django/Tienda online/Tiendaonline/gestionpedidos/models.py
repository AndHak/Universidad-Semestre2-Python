from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField()
    telefono = models.CharField(max_length = 10)

class Articulo(models.Model):
    nombre = models.CharField(max_length = 30)
    seccion = models.CharField(max_length = 50)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} Sección: {self.seccion} Precio: {self.precio}'

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()