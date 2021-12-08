from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# nombre de la db = a la tabla
class PersonaProfesional(models.Model):

    #relacion uno a uno User - profesional
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="profesional")

    tipoDocumento = models.CharField(max_length=2)
    numeroDocumento = models.IntegerField()
    # nombre = models.CharField(max_length=64)
    perfil = models.CharField(max_length=64)
