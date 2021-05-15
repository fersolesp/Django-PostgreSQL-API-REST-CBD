from django.db import models
from django.core.validators import URLValidator

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    url_foto = models.URLField(validators=[URLValidator()])

    def __str__(self):
        return self.nombre

class Combustible(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CajaCambios(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Traccion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50, null=True, blank=True)
    longitud = models.CharField(max_length=50, null=True, blank=True)
    combustibles = models.ManyToManyField(Combustible)
    potencia = models.CharField(max_length=50, null=True, blank=True)
    cajas_cambios = models.ManyToManyField(CajaCambios)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    tracciones = models.ManyToManyField(Traccion)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    url_foto = models.URLField(validators=[URLValidator()])
    fecha = models.DateField()
    contenido = models.TextField()
    autor = models.CharField(max_length=200)
    modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Version(models.Model):
    nombre = models.CharField(max_length=100)
    url_foto = models.URLField(validators=[URLValidator()])
    tipo_vehiculo =  models.ForeignKey(TipoVehiculo, on_delete=models.DO_NOTHING)
    modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre






