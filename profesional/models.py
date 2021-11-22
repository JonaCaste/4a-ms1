from django.db import models

# Create your models here.

# nombre de la db = a la tabla
class PersonaProfesional(models.Model):
    tipoDocumento = models.CharField(max_length=2)
    numeroDocumento = models.IntegerField()
    nombre = models.CharField(max_length=64)
    perfil = models.CharField(max_length=64)
