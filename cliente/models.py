from django.db import models

from django.contrib.auth.models import User  #modelo para la relacion muchos a muchos

# Create your models here.

# nombre de la db = a la tabla
class PersonaCliente(models.Model):

    # crear columnas
    ## id por defecto
    tipoDocumento = models.CharField(max_length=2)
    numeroDocumento = models.IntegerField()
    nombre = models.CharField(max_length=64)
    sexo = models.CharField(max_length=15)
    edad = models.IntegerField()
    #email = models.EmailField(default="")
