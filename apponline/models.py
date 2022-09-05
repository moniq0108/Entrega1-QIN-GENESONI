from django.db import models

class Carteras(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock_disponible = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}'


class Camperas(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock_disponible = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}'

class Zapatos(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock_disponible = models.IntegerField()

class Accesorios(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock_disponible = models.IntegerField()
